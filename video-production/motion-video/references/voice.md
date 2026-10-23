# Voice — Nhật Phong (VieNeu)

## Primary: VieNeu API (preferred when local studio unavailable)
Use the `vieneu-api-client` skill:
`~/workspace/skills/vieneu-api-client/vieneu_client.py`.

- Voice: `Nam - Nhật Phong`. **Never substitute another voice.**
- Default speed: `1.1`. Project may override (e.g. 1.15) — apply with
  `atempo=` (pitch-locked), never pitch-shifted.
- Key source: env `VIENEU_AGENT_KEY` **only**, or the Secure Vault custom
  connector `vieneu` (host `vieneu-api.danangdragons.com`, Bearer auth).
  Never hardcode, print, or commit the key.
- Job protocol: POST `/v1/audio/speech` → poll `GET /jobs/{id}` ~2s →
  `GET /jobs/{id}/audio` on `completed`. Max 20k chars/request.
  Terminal `failed/interrupted/expired/rejected` → stop, report.
  Retry keeps the same `X-Task-Id`.
- Persist WAVs to app storage before Sunday 03:00 Asia/Ho_Chi_Minh
  (completed-job audio cleanup).

## Fallback: local studio
`https://vieneu-studio.vercel.app` — voice `Nam - Nhật Phong`
(connection code `12345676` saved from prior session; usually enters directly).

## Script rules
- Write spoken Vietnamese (numbers as words: "chín mươi ba nghìn sao").
- Keep sentences short; split narration into segments per scene for
  karaoke timing (segment duration / word count).
- Verify durations with `ffprobe` — never estimate.

## Env check (true/false only, never the value)
```bash
test -n "$VIENEU_AGENT_KEY" && echo true || echo false
```
