# VieNeu API Client

Job-based Vietnamese TTS over `https://vieneu-api.danangdragons.com`.
Trigger: **video-audio requests only**. Prefer this API when the local
VieNeu studio (`https://vieneu-studio.vercel.app`) is unavailable; otherwise
use the local studio.

## Safe config (no key stored here)

| Item | Value |
|---|---|
| Base | `https://vieneu-api.danangdragons.com` |
| Key source | env `VIENEU_AGENT_KEY` **only** — never hardcode, print, or commit |
| Voice | `Nam - Nhật Phong` |
| Default speed | `1.1` (project overrides allowed, e.g. video v2 uses `1.15`) |
| Max input | 20,000 chars |
| Response | `wav` |

Headers per request: `Authorization: Bearer <env key>`,
`Content-Type: application/json`, `X-Task-Id: <UUID4, one per task>`,
`X-VieNeu-Worker: auto`.

## Protocol

1. `POST /v1/audio/speech` with
   `{"input":"<text>","voice":"Nam - Nhật Phong","speed":1.1,"response_format":"wav"}`
   → returns a **job**, not audio.
2. `GET /jobs/{id}` every ~2s. `completed` → step 3.
   `failed`/`interrupted`/`expired`/`rejected` → stop and report.
3. `GET /jobs/{id}/audio` (same bearer) → save WAV.
4. **Persist the WAV to app storage before Sunday 03:00 (Asia/Ho_Chi_Minh)** —
   completed-job audio is cleaned up then.

## Failure map

- POST timeout → look up by the same `X-Task-Id`; never mint a new id.
  Retries keep id + payload + worker selection.
- `401` → key missing/revoked (check env / secret store).
- `409` → task-id conflict.
- Cloudflare block → log HTTP code + `CF-Ray` only, never the key.
  Plain HTTPS; no TLS impersonation.
- Both workers offline (Mac27 → Mac14 priority is server-side) → report
  clearly; never claim cloud synthesis.

## Setting VIENEU_AGENT_KEY (no plaintext)

- **This VM / Linux:** export via your secret manager, or
  `export VIENEU_AGENT_KEY="$(secret-tool lookup ...)"` in the shell
  profile — never paste the value into chat or files.
- **Mac (Mac27 / Mac14):** store in Keychain
  (`security add-generic-password -s VIENEU_AGENT_KEY -a agent -w`),
  then expose to the needed process via a launch agent
  (`launchctl setenv VIENEU_AGENT_KEY "$(security find-generic-password -s VIENEU_AGENT_KEY -a agent -w)"`)
  or read it inside the app at runtime. Do not write it into plist files.

Verify without exposing the value:

```bash
test -n "$VIENEU_AGENT_KEY" && echo true || echo false
```

## Client

`vieneu_client.py` implements all of the above with stdlib only:

```bash
python3 vieneu_client.py --text "Xin chào, đây là kiểm thử." --out test.wav --speed 1.1
```

Exit non-zero with a `VIENEU ERROR:` line on any terminal failure.
