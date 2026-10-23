---
name: "vieneu"
description: "Use Vieneu when the user asks for Vieneu or this provider's API."
---

# Vieneu

## Purpose
Use Vieneu with the user-connected `custom.vieneu` credential.

## Tooling
Add service-specific CLIs under `~/workspace/skills/vieneu/bin/`.

Python CLIs must import `/opt/hatch/skills/skill-creator/bin/dynamic_credentials.py` and call `add_surrogate_to_request(...)`, `url_with_surrogate_query_param(...)`, or `url_with_surrogate_path_segment(...)` before authenticated requests, matching where the provider reads the key. If they use `urllib`, read JSON responses with `read_json_response(resp)` from the same helper instead of calling `resp.read()` directly. They must send only `hsurr:*` values, and only to the hosts below.

Available CLIs:
- `bin/vieneu_tts.py` — VieNeu TTS job client (surrogate auth, no env key needed):
  `python3 bin/vieneu_tts.py --text "..." --out out.wav [--speed 1.1]`
  (POST /v1/audio/speech → poll → GET /jobs/{id}/audio; voice "Nam - Nhật Phong").
  Use this INSTEAD of `vieneu-api-client/vieneu_client.py` whenever
  `VIENEU_AGENT_KEY` is not in env.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, call `credentials.request_api_access` with `reconnect` to replace it. The connector is stored as `custom.vieneu`.

## Operating Rules
1. Use this skill when the user asks for Vieneu or this provider's API.
2. Restrict authenticated requests to: vieneu-api.danangdragons.com.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.
