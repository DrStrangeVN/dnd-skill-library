---
name: vieneu-tts
description: Convert Vietnamese text to speech with the VieNeu Studio API (voice "Nam - Nhật Phong"). Use when the user asks for TTS/voiceover audio, narration segments for a video, or says "dùng API VieNeu". Handles the async job flow: create job, poll, download WAV. Authenticates via the Secure Vault `vieneu` connector (surrogate exchange) — the real API key is never written to source, logs, or repos.
---

# VieNeu TTS (Vietnamese text-to-speech)

Server-rendered Vietnamese voiceover for video narration and any spoken audio. Default voice: **"Nam - Nhật Phong"** (male voice the user approved 2026-10-09).

## API contract (per user-supplied docs, 2026-10-09)

- **Base:** `https://vieneu-api.danangdragons.com`
- **Auth:** `Authorization: Bearer <API_KEY>` on every request. Plain HTTP clients (requests/curl) work — the Cloudflare exception is configured, **no Chrome TLS emulation needed** (verified 2026-10-09).
- **Create:** `POST /v1/audio/speech`
  - Headers: `Content-Type: application/json`, `X-Task-Id: <uuid4 per task>`, `X-VieNeu-Worker: auto`
  - JSON: `{"input": "<text>", "voice": "Nam - Nhật Phong", "speed": 1.1, "response_format": "wav"}`
  - Max **20,000 chars** per request. `speed` 1.1 ≈ natural; video standard uses up to 1.2.
  - Returns a job object (no audio yet).
- **Poll:** `GET /jobs/{id}` every ~2s until `state == "completed"`.
- **Download:** `GET /jobs/{id}/audio` with the same auth → save as `.wav` (48kHz mono).
- **Failure states:** `failed`, `interrupted`, `expired`, `rejected` → report the state and stop polling.

## Error handling

- **401:** key missing/expired/revoked → ask the user to reconnect the `vieneu` connector (Secure Vault card), do not retry blindly.
- **409:** `X-Task-Id` already used with different content → generate a new UUID only for genuinely new content.
- **Timeout on create:** re-check with the *same* `X-Task-Id` — never create a new ID and resend immediately (risk of duplicate audio).
- **Cloudflare error:** record the code and `CF-Ray` for the system owner; do not disable HTTPS verification.
- Never write the API key into source, logs, or a git repo. Never echo it in chat.

## Housekeeping

- Server deletes completed audio every Sunday 03:00 (Asia/Ho_Chi_Minh) — download results promptly; the download link requires the API key and is not a public share link.

## Usage

```bash
# One segment -> output.wav
python3 ~/workspace/skills/vieneu-tts/scripts/vieneu_tts.py \
  --text "Xin chào, đây là bản tin." \
  --out /tmp/narration/seg1.wav \
  --speed 1.1

# From a file (longer scripts; script chunks at 20k chars automatically)
python3 ~/workspace/skills/vieneu-tts/scripts/vieneu_tts.py \
  --text-file /tmp/script.txt \
  --out-dir /tmp/narration/ \
  --voice "Nam - Nhật Phong" --speed 1.15
```

## Auth resolution order (script)

1. `VIENEU_AGENT_KEY` env var if set.
2. Secure Vault surrogate: `authdc cred surrogate custom.vieneu` (short-lived; sent as Bearer, authd swaps it for the real credential at egress).
3. Otherwise exit with a clear message asking the user to connect the `vieneu` connector.
