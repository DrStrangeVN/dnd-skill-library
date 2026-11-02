# SETUP — using this library on a fresh Muse machine

## 1. Get the skills

```bash
git clone <this-private-repo> ~/workspace/skill-library-repo
mkdir -p ~/workspace/custom-skills
# copy every skill folder (each category dir holds skill folders + a CATALOG.md)
for cat in ~/workspace/skill-library-repo/*/; do
  for skill in "$cat"*/; do
    [ -f "$skill/SKILL.md" ] && cp -R "$skill" ~/workspace/custom-skills/
  done
done
ls ~/workspace/custom-skills | wc -l   # expect 2384
```

Skills are plain folders: `SKILL.md` (frontmatter `name` + `description` is the
trigger) plus any `references/`, `scripts/`, `assets/` they ship. No build step
is needed for the skills themselves. Pick skills via `INDEX.md` or the
per-category `CATALOG.md`.

## 2. Toolchains per pack

Most of the 2,384 skills are instruction-only. The authored production packs
below drive local tooling that must exist on the machine (paths are the origin
machine's layout — recreate equivalents):

### deck-studio pack (`slides-presentation/deck-*`, master `deck-studio`)
- Engine (NOT in this repo): `~/workspace/deck-studio/` — `deckkit.py` single
  geometry model → `build_deck.py` (HTML studio) + `export_pptx.py` (editable
  PPTX); style = one `theme.json` per skill in the engine's `themes/` folder.
- Python venv with **python-pptx + Pillow**:
  `python3 -m venv ~/workspace/tools/deck-venv && ~/workspace/tools/deck-venv/bin/pip install python-pptx Pillow`
- Slide screenshots/QA: Node + `puppeteer-core` driving a Chrome Headless Shell
  (the video-kit's Remotion install provides one).
- Glass styles (e.g. `deck-sky-glass-deck`) use the v3 standard: real artwork
  assets + baked-blur PPTX glass (see the skill and the engine README).

### Video packs (`video-production/`: ReelCrew `*-video`, Opus55 `opus-*`/`opus55-*`, `opuscar-telestrator`, `motion-video`, `local-real-estate-video`)
- Pipeline (not in this repo): `~/workspace/video-kit/` — Node 24, Remotion 4,
  per-demo sources, `tools/finish.sh` (loudness −14 LUFS) and `tools/sheet.sh`
  (contact sheets). `finish.sh` needs `bc`: use the shim at
  `~/workspace/video-kit/.bin/bc`, prepended to PATH.
- `ffmpeg`/`ffprobe` on PATH. WebGL headless renders need Chrome Headless Shell
  with `--use-angle=swiftshader --enable-unsafe-swiftshader`.
- Manim (only `math-explainer-3b1b-video`): venv at `~/workspace/tools/manim-venv`;
  no LaTeX on the origin machine — MathTex unused, use MarkupText.
- Fonts in `~/.fonts`: Be Vietnam Pro (use Black 900 for large Vietnamese
  display text — Anton/Oswald misplace Vietnamese tone marks at large sizes),
  Playfair Display, Space Grotesk, IBM Plex Mono, Baloo 2, Archivo.
- Voice: VieNeu-TTS local at `~/workspace/tools/VieNeu-TTS` (`uv sync`; set
  `HF_HUB_DISABLE_XET=1` — the origin proxy blocks HuggingFace's Xet route).
  Local clone voice "Nhật Phong (Local Clone)" is for demos; production uses
  the API voice "Nam - Nhật Phong" (vieneu skills cover the API client).

### Web pack (`web-dev/web-liquid-glass-landing`)
- No toolchain: output is a single self-contained HTML file; QA via headless
  Chrome screenshots (same puppeteer-core setup as above).

### claude-code-harness pack (`ai-agents-llm/`: `harness-*`, `breezing`, `cursor-*`, `ci`, `memory`, `maintenance`, `agent-browser`, `session-send`, `failure-codifier`, `cc-update-review`, `japanese-writing-drafter`)
- These 23 skills are verbatim copies from Chachamaru127/claude-code-harness
  v5.16.0 (MIT). They are NOT self-contained: most of them call the plugin
  runtime via `${HARNESS_PLUGIN_ROOT}/scripts/...`, `bin/harness`, hooks, and
  the `harness_mem` MCP server. Install the plugin itself in Claude Code /
  Codex / Cursor / Grok (upstream: `/plugin marketplace add
  Chachamaru127/claude-code-harness`, then `/plugin install
  harness@claude-code-harness-marketplace`, then `/harness-setup`) before
  relying on them. Copying the skill folders into `~/workspace/custom-skills/`
  alone does not install the plugin.
- Not in this repo: the plugin's `scripts/`, `bin/`, `hooks/`, `agents/`,
  `docs/`, Go code, `skills/routing-rules.md`, and the Codex/OpenCode skill
  variants.

### ScrapeCreators pack (`marketing-growth/`: 13 skills from ScrapeCreators/social-media-research-skills @ 64ba7b4, MIT)
- These skills call the ScrapeCreators REST API (`https://api.scrapecreators.com`, `x-api-key` header). Set `SCRAPECREATORS_API_KEY` from a key obtained at scrapecreators.com before use; without a key the skills cannot fetch data. Never commit a key to this repo.
- The 8 guide skills added 2026-11-02 (`*-guide`) are documentation only: the Local Deep Research, Short Video Factory, AI YouTube Shorts Generator apps and the FLUX.2, Kokoro, ACE-Step models are not installed by copying the skill folders — install each upstream separately, following its own README and licence (see the guide skill for the verified upstream and its limits).

## 3. Verify after setup

1. `ls ~/workspace/custom-skills | wc -l` → **2384**.
2. Skill search finds e.g. `deck-sky-glass-deck`, `opuscar-telestrator`,
   `beat-motion-video`.
3. Deck smoke test (needs the engine): build the sample spec with two themes,
   run the engine's `verify.py` — expect ALL PASS, 9 slides / 65 text shapes /
   notes 9/9.
4. Video smoke test: `ffprobe` any deliverable MP4 and read its QA.md sheet —
   specs + loudness (−14 LUFS ±0.5) must match the QA record.
5. Spot-check one `samples/` folder renders the expected stills.

## 4. House rules that travel with the library

- Public posts always need the user's fresh approval; no auto-posting.
- Secrets are never written into skills, files or this repo (`.env.example`
  templates with empty values are fine).
- Forecasts as scenarios/probabilities; never claim "done" before the
  acceptance checks in the relevant skill have actually run.
