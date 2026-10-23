#!/usr/bin/env python3
"""
VieNeu TTS API client (job-based).

SAFETY RULES (non-negotiable):
- API key comes ONLY from env VIENEU_AGENT_KEY. Never hardcode, never print,
  never commit, never put it in logs or chat.
- Normal HTTPS only. No TLS impersonation / fake Chrome fingerprints.
- One X-Task-Id (UUID4) per task. Retries reuse the SAME id + payload + worker.

Protocol (per operator spec):
- POST {BASE}/v1/audio/speech  -> returns a JOB (not audio)
- GET  {BASE}/jobs/{id}        -> poll ~2s until terminal state
- GET  {BASE}/jobs/{id}/audio  -> download WAV when completed
- Terminal failures: failed / interrupted / expired / rejected -> stop, report.
- POST timeout: look up by X-Task-Id, do NOT mint a new id.
- 401 -> key missing/revoked. 409 -> task-id conflict.
- Cloudflare block: log HTTP code + CF-Ray header only (never the key).
- Completed-job audio is cleaned up Sunday 03:00 (Asia/Ho_Chi_Minh):
  persist the WAV to app storage BEFORE that deadline.
- Worker priority Mac27 -> Mac14 is handled server-side (X-VieNeu-Worker:auto).
  If both workers are offline, report it plainly; never claim cloud synthesis.

Usage:
    python3 vieneu_client.py --text "Xin chào..." --out out.wav [--speed 1.1]
"""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import uuid

BASE = "https://vieneu-api.danangdragons.com"
VOICE = "Nam - Nhật Phong"
DEFAULT_SPEED = 1.1
MAX_CHARS = 20000
POLL_INTERVAL = 2.0
POLL_TIMEOUT = 600


class VieNeuError(Exception):
    pass


def _api_key():
    key = os.environ.get("VIENEU_AGENT_KEY")
    if not key:
        raise VieNeuError(
            "VIENEU_AGENT_KEY is not set in the environment "
            "(equivalent of HTTP 401: key missing or revoked). "
            "Set it via your OS secret store; see SKILL.md."
        )
    return key


def _headers(task_id):
    return {
        "Authorization": "Bearer " + _api_key(),
        "Content-Type": "application/json",
        "X-Task-Id": task_id,
        "X-VieNeu-Worker": "auto",
    }


def _read_error(e):
    """Extract safe diagnostics: HTTP code + CF-Ray, never the key."""
    code = getattr(e, "code", "?")
    ray = ""
    try:
        ray = e.headers.get("CF-Ray", "") if e.headers else ""
    except Exception:
        pass
    body = ""
    try:
        body = e.read().decode("utf-8", "replace")[:300]
    except Exception:
        pass
    return code, ray, body


def _request(method, path, task_id, payload=None, timeout=30):
    url = BASE + path
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=_headers(task_id), method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            if "json" in ctype or (raw[:1] in (b"{", b"[")):
                return json.loads(raw.decode("utf-8"))
            return raw
    except urllib.error.HTTPError as e:
        code, ray, body = _read_error(e)
        if code == 401:
            raise VieNeuError(f"HTTP 401: VIENEU_AGENT_KEY missing or revoked. {body}")
        if code == 409:
            raise VieNeuError(f"HTTP 409: task-id conflict for X-Task-Id={task_id}. {body}")
        if code in (403, 1010) or "cloudflare" in body.lower():
            raise VieNeuError(f"Cloudflare block: HTTP {code} CF-Ray={ray}. Not retrying with tricks.")
        raise VieNeuError(f"HTTP {code} CF-Ray={ray}: {body}")
    except (TimeoutError, urllib.error.URLError) as e:
        raise VieNeuError(f"NETWORK/TIMEOUT on {method} {path}: {e}")


def submit(text, speed=DEFAULT_SPEED, task_id=None):
    if len(text) > MAX_CHARS:
        raise VieNeuError(f"input too long: {len(text)} > {MAX_CHARS} chars")
    task_id = task_id or str(uuid.uuid4())
    payload = {
        "input": text,
        "voice": VOICE,
        "speed": speed,
        "response_format": "wav",
    }
    # Retry keeps the SAME task id + payload + worker selection.
    last = None
    for attempt in (1, 2):
        try:
            res = _request("POST", "/v1/audio/speech", task_id, payload, timeout=60)
            break
        except VieNeuError as e:
            last = e
            if "TIMEOUT" in str(e) and attempt == 1:
                time.sleep(3)
                continue
            raise
    else:
        raise last
    job_id = res.get("id") or res.get("job_id") or res.get("jobId")
    if not job_id:
        raise VieNeuError(f"POST returned no job id: {str(res)[:200]}")
    return task_id, job_id


def wait(job_id, task_id, poll_interval=POLL_INTERVAL, timeout=POLL_TIMEOUT):
    deadline = time.time() + timeout
    while True:
        st = _request("GET", f"/jobs/{job_id}", task_id, timeout=20)
        # API schema 2026-10-09: `state` = job state string
        # ("running"/"completed"/...), `status` = numeric code. Prefer `state`.
        raw_state = st.get("state")
        if not isinstance(raw_state, str):
            raw_state = st.get("status")
        status = (raw_state or "").lower() if isinstance(raw_state, str) else ""
        if status == "completed":
            return st
        if status in ("failed", "interrupted", "expired", "rejected"):
            raise VieNeuError(f"job {job_id} terminal state: {status} ({str(st)[:200]})")
        if status in ("", "unknown"):
            raise VieNeuError(f"job {job_id} returned unparseable status: {str(st)[:200]}")
        if time.time() > deadline:
            raise VieNeuError(f"job {job_id} poll timeout after {timeout}s (last: {status})")
        # both workers offline shows up as a distinct non-progress state
        if status in ("no_worker", "workers_offline", "offline"):
            raise VieNeuError(
                "Both workers (Mac27, Mac14) are offline per API. "
                "Not claiming cloud synthesis; ask the operator to bring a worker online."
            )
        time.sleep(poll_interval)


def download_audio(job_id, task_id, out_path):
    data = _request("GET", f"/jobs/{job_id}/audio", task_id, timeout=120)
    if not data or len(data) < 1000:
        raise VieNeuError(f"audio payload too small ({len(data) if data else 0} bytes)")
    if data[:4] != b"RIFF":
        raise VieNeuError("audio payload is not a WAV (missing RIFF header)")
    with open(out_path, "wb") as f:
        f.write(data)
    return out_path


def synthesize(text, out_path, speed=DEFAULT_SPEED):
    task_id, job_id = submit(text, speed=speed)
    wait(job_id, task_id)
    return download_audio(job_id, task_id, out_path), task_id, job_id


def main():
    ap = argparse.ArgumentParser(description="VieNeu TTS job client (key from env only)")
    ap.add_argument("--text", required=True, help="Vietnamese text (<= 20000 chars)")
    ap.add_argument("--out", required=True, help="output WAV path")
    ap.add_argument("--speed", type=float, default=DEFAULT_SPEED)
    args = ap.parse_args()
    try:
        path, task_id, job_id = synthesize(args.text, args.out, speed=args.speed)
    except VieNeuError as e:
        print(f"VIENEU ERROR: {e}", file=sys.stderr)
        return 1
    # NOTE: task_id/job_id are safe to log (not secrets). Never log the key.
    print(f"OK saved={path} task={task_id} job={job_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
