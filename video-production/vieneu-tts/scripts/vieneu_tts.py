#!/usr/bin/env python3
"""VieNeu Studio TTS client.

Converts Vietnamese text to speech via https://vieneu-api.danangdragons.com
using the async job flow: POST /v1/audio/speech -> poll GET /jobs/{id} ->
GET /jobs/{id}/audio -> save WAV.

Auth: env VIENEU_AGENT_KEY, else Secure Vault surrogate
`authdc cred surrogate custom.vieneu` (short-lived; never the real secret).
The real API key is never printed, logged, or written to files.
"""
import argparse
import json
import os
import subprocess
import sys
import time
import uuid

import requests

API = "https://vieneu-api.danangdragons.com"
MAX_CHARS = 20000
DEFAULT_VOICE = "Nam - Nhật Phong"
POLL_INTERVAL = 2.0
TERMINAL_STATES = {"failed", "interrupted", "expired", "rejected"}


def get_bearer():
    key = os.environ.get("VIENEU_AGENT_KEY")
    if key:
        return key
    try:
        out = subprocess.run(
            ["authdc", "cred", "surrogate", "custom.vieneu"],
            capture_output=True, text=True, check=True, timeout=30,
        ).stdout
        creds = json.loads(out)["credentials"]
        if not creds:
            sys.exit("No custom.vieneu credential in the vault. Ask the user to connect it via the Secure Vault card.")
        return creds[0]["surrogate"]
    except FileNotFoundError:
        sys.exit("authdc not available and VIENEU_AGENT_KEY unset. Set the env var or connect the `vieneu` connector.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"Surrogate exchange failed: {e.stderr.strip()[:200]}")


def create_job(session, text, voice, speed):
    task_id = str(uuid.uuid4())
    r = session.post(
        API + "/v1/audio/speech",
        headers={
            "X-Task-Id": task_id,
            "X-VieNeu-Worker": "auto",
        },
        json={"input": text, "voice": voice, "speed": speed, "response_format": "wav"},
        timeout=60,
    )
    if r.status_code == 401:
        sys.exit("401: API key missing, expired or revoked. Ask the user to reconnect the `vieneu` connector.")
    if r.status_code == 409:
        sys.exit("409: X-Task-Id conflict. This should not happen with a fresh UUID; retry once with a new ID.")
    if not r.ok:
        sys.exit(f"Create job -> {r.status_code}: {r.text[:500]}")
    body = r.json()
    job_id = body.get("id") or body.get("job_id") or body.get("task_id")
    if not job_id:
        sys.exit(f"Create job returned no job id: {json.dumps(body)[:300]}")
    return job_id, task_id


def poll_job(session, job_id, timeout=600):
    deadline = time.time() + timeout
    while time.time() < deadline:
        r = session.get(API + f"/jobs/{job_id}", timeout=30)
        if not r.ok:
            sys.exit(f"Poll {job_id} -> {r.status_code}: {r.text[:300]}")
        state = (r.json().get("state") or "").lower()
        if state == "completed":
            return
        if state in TERMINAL_STATES:
            sys.exit(f"Job {job_id} ended in state '{state}'. Not retrying.")
        time.sleep(POLL_INTERVAL)
    sys.exit(f"Job {job_id} did not complete within {timeout}s. Re-check later with the same job id.")


def download_audio(session, job_id, out_path):
    r = session.get(API + "/jobs/{0}/audio".format(job_id), timeout=120)
    if not r.ok:
        sys.exit(f"Download {job_id} -> {r.status_code}: {r.text[:300]}")
    with open(out_path, "wb") as f:
        f.write(r.content)
    return out_path


def chunk_text(text, limit=MAX_CHARS):
    chunks, cur = [], []
    cur_len = 0
    for para in text.split("\n\n"):
        if cur_len + len(para) + 2 > limit and cur:
            chunks.append("\n\n".join(cur))
            cur, cur_len = [], 0
        cur.append(para)
        cur_len += len(para) + 2
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def main():
    ap = argparse.ArgumentParser(description="VieNeu Studio Vietnamese TTS")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="Text to speak (<= 20000 chars)")
    src.add_argument("--text-file", help="File with text to speak")
    ap.add_argument("--voice", default=DEFAULT_VOICE)
    ap.add_argument("--speed", type=float, default=1.1)
    ap.add_argument("--out", help="Output WAV path (single text only)")
    ap.add_argument("--out-dir", help="Output dir for chunked text-file jobs")
    ap.add_argument("--poll-timeout", type=int, default=600)
    args = ap.parse_args()

    text = args.text
    if args.text_file:
        with open(args.text_file, encoding="utf-8") as f:
            text = f.read().strip()
    if not text:
        sys.exit("Empty input text.")

    session = requests.Session()
    session.headers["Authorization"] = "Bearer " + get_bearer()

    chunks = chunk_text(text)
    if len(chunks) > 1 and not args.out_dir:
        sys.exit(f"Input splits into {len(chunks)} chunks (>20000 chars); provide --out-dir.")

    outputs = []
    for i, chunk in enumerate(chunks):
        job_id, task_id = create_job(session, chunk, args.voice, args.speed)
        print(f"[{i + 1}/{len(chunks)}] job={job_id} task={task_id} chars={len(chunk)}", flush=True)
        poll_job(session, job_id, timeout=args.poll_timeout)
        if args.out_dir:
            os.makedirs(args.out_dir, exist_ok=True)
            out_path = os.path.join(args.out_dir, f"seg{i + 1:02d}.wav")
        else:
            out_path = args.out or f"vieneu_{job_id}.wav"
        download_audio(session, job_id, out_path)
        print(f"[{i + 1}/{len(chunks)}] saved {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)
        outputs.append(out_path)
    print("DONE " + " ".join(outputs))


if __name__ == "__main__":
    main()
