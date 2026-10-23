#!/usr/bin/env python3
"""
VieNeu TTS via the connected custom.vieneu credential (authd surrogate).

Same job-based API flow as vieneu-api-client/vieneu_client.py, but auth comes
from the Secure Vault connector instead of env VIENEU_AGENT_KEY:
  POST {BASE}/v1/audio/speech -> job id
  GET  {BASE}/jobs/{id}        -> poll until completed
  GET  {BASE}/jobs/{id}/audio  -> WAV bytes (RIFF)

The surrogate value (hsurr:*) is attached by dynamic_credentials and swapped
for the real key on approved egress. Never printed, logged, or persisted.

Usage:
    python3 vieneu_tts.py --text "Xin chào..." --out out.wav [--speed 1.1]
"""
import argparse
import json
import sys
import time
import urllib.request
import urllib.error
import uuid

sys.path.insert(0, "/opt/hatch/skills/skill-creator/bin")
from dynamic_credentials import add_surrogate_to_request

BASE = "https://vieneu-api.danangdragons.com"
ALLOWED_HOSTS = ["vieneu-api.danangdragons.com"]
CREDENTIAL = "custom.vieneu"
VOICE = "Nam - Nh\u1eadt Phong"
DEFAULT_SPEED = 1.1
MAX_CHARS = 20000
POLL_INTERVAL = 2.0
POLL_TIMEOUT = 600


class VieNeuError(Exception):
    pass


def _build_request(method, path, task_id, payload=None):
    url = BASE + path
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    req.add_header("X-Task-Id", task_id)
    req.add_header("X-VieNeu-Worker", "auto")
    # Attaches `Authorization: Bearer hsurr:*` (bearer_header placement).
    add_surrogate_to_request(req, CREDENTIAL, allowed_hosts=ALLOWED_HOSTS)
    return req


def _request(method, path, task_id, payload=None, timeout=30):
    req = _build_request(method, path, task_id, payload)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            ctype = resp.headers.get("Content-Type", "")
            if "json" in ctype or (raw[:1] in (b"{", b"[")):
                return json.loads(raw.decode("utf-8"))
            return raw
    except urllib.error.HTTPError as e:
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
        if code == 401:
            raise VieNeuError(f"HTTP 401: credential rejected. {body}")
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
    payload = {"input": text, "voice": VOICE, "speed": speed, "response_format": "wav"}
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
        if status in ("no_worker", "workers_offline", "offline"):
            raise VieNeuError("Both workers (Mac27, Mac14) are offline per API. Not claiming cloud synthesis.")
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
    ap = argparse.ArgumentParser(description="VieNeu TTS via Secure Vault connector (surrogate auth)")
    ap.add_argument("--text", required=True, help="Vietnamese text (<= 20000 chars)")
    ap.add_argument("--out", required=True, help="Output WAV path")
    ap.add_argument("--speed", type=float, default=DEFAULT_SPEED)
    args = ap.parse_args()
    out, task_id, job_id = synthesize(args.text, args.out, args.speed)
    print(f"OK wav={out} task={task_id} job={job_id}")


if __name__ == "__main__":
    main()
