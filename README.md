# Skill Library — Danang Dragons / Vũ Đình Trí

Private consolidated library of every Muse skill built or curated on the
origin machine, organised by category so any of the user's Muse instances can
clone this repo, copy the skills into its own `~/workspace/custom-skills/`, and
work with the same playbooks. See **SETUP.md** for a fresh-machine walkthrough
and **INDEX.md** for the full skill list.

## Contents

- **2,516 skills** in 24 category folders (layout: `<category>/<skill-name>/SKILL.md` + the skill's own references/scripts/assets).
- `INDEX.md` — every skill with its category and one-line description.
- `<category>/CATALOG.md` — per-category table.
- `SETUP.md` — install + toolchain + verification steps for a new machine.
- `BUILD-REPORT.md` — how this repo was assembled: counts, exclusions, secret review, decisions.
- `RESYNC.txt` — folders that must be re-copied from the origin machine before the first push (a fidelity pass was still editing them while this repo was built).

## Provenance

Assembled 2026-10-23 from `~/workspace/custom-skills/` on the origin machine:

- 2,320 skills from the audited library set (`skill-inventory/keep.csv`, audit of 2026-10-23). 225 audited DROP candidates (off-profile, risky, duplicates, broken stubs) are **not** in this repo; they still exist on the origin machine — dropping applies to the repo only.
- 64 skills authored after the audit: the 61 Skillry-Slides style skills (`deck-*`), the `deck-studio` master skill, `opuscar-telestrator` (Lemo distillation) and `web-liquid-glass-landing` (Skillry Web distillation).
- Authored packs (deck-*, Opus55 family, ReelCrew video skills, opuscar-telestrator,
  web-liquid-glass-landing) carry a `samples/` subfolder with representative
  demo stills so a reader can see the output before using the skill.

Update 2026-10-27: +23 skills (11 YouTube `yt-*`, 11 official Remotion skills +
router `remotion-best-practices`, `pr-review-expert`) and the 15 Superpowers
skills refreshed to upstream v7.0.1. Total 2,407.

Update 2026-10-27: +1 skill (`viet-font-kit` v1.0.1, Vietnamese font
vietnamisation, by @nhatmotion) in `design-uiux/`. Total 2,408.

Update 2026-10-29: +1 skill (`clone-website`, rebuild existing web pages as working local code, from JCodesMore/ai-website-cloner-template @ ee3f5a2, MIT) in `web-dev/`. Total 2,409.

Update 2026-10-29: +16 skills (DESIGN:OS Vietnamese v5.2.0, 15 `vietnamese-*` + `vn-design-system-ux`, from jangtrinh/design-os-vietnamese @ 00dea26, PolyForm-Shield-1.0.0 — each skill folder carries the upstream LICENSE) in `design-uiux/`. Total 2,425.

## Updating incrementally

1. On the origin machine, copy the new/changed skill folder into its category
   folder here (use `keep.csv` categories for audited skills; new skills go to
   the category that fits their domain).
2. If it is an authored pack, refresh its `samples/` images.
3. Update `INDEX.md` and the category `CATALOG.md` (one row per skill).
4. Commit with a message naming the skills touched. Keep commits small and
   frequent rather than re-dumping the whole library.
5. Never commit: real credentials or `.env` files (`.gitignore` blocks the
   common patterns), media over ~25 MB per file, `__pycache__`, `node_modules`.

## Companion tooling (not in this repo)

Some packs drive code that lives outside the skill folders on the origin
machine: the **deck-studio engine** (`~/workspace/deck-studio/`, HTML/PPTX
builder + themes), the **video-kit** render pipeline (`~/workspace/video-kit/`,
Remotion + finish/QA tooling) and **VieNeu-TTS** (`~/workspace/tools/VieNeu-TTS`).
SETUP.md lists what each pack needs and how to verify it after copying.

Update 2026-10-30: +44 skills (coreyhaines31/marketingskills @ 820ad2c, MIT — each skill folder carries the upstream LICENSE) in `marketing-growth/`. The 8 same-named skills already in the library (content-strategy, copy-editing, copywriting, launch, marketing-ideas, marketing-psychology, programmatic-seo, seo-audit) were kept unchanged per the user's choice. Total 2,469.

Update 2026-10-30: +23 skills (Chachamaru127/claude-code-harness v5.16.0 @ c2304c3, MIT — verbatim `skills/*` only, each skill folder carries the upstream LICENSE) in `ai-agents-llm/`. REQUIREMENT: these are plugin skills — they need the claude-code-harness plugin runtime (scripts/, bin/harness, hooks, harness_mem MCP) to run fully; the plugin itself, `skills/routing-rules.md` and the Codex/OpenCode variants are not in this repo. Total 2,492.

Update 2026-10-31: +1 skill (`ui-ux` v0.3.27, UI/UX cho dashboard/app — brief, wireframe, dựng, review/refactor, from evondev/evondevKit @ 4d02153, MIT — verbatim `skills/ui-ux/` only, folder carries the upstream LICENSE) in `design-uiux/`. Included as-is: `references/`, `scripts/` (check-update.mjs phones the upstream public VERSION file once a day at most, nothing sent; disable with EVONDEVKIT_NO_UPDATE_CHECK=1; probe.mjs needs Playwright). Not in this repo: `.claude-plugin/` manifests, `archive/`, `images/`, docs (BACKLOG/DARKMODE/NEXT/REVIEW/TESTS/DEVELOP). Total 2,493.

Update 2026-11-02: +13 skills (ScrapeCreators/social-media-research-skills @ 64ba7b4, 2026-08-26, MIT — verbatim `skills/*` only, each skill folder carries the upstream LICENSE) in `marketing-growth/`. REQUIREMENT: the skills call the ScrapeCreators REST API and need a `SCRAPECREATORS_API_KEY` (get a key at scrapecreators.com); no key is stored in this repo. Not in this repo: the upstream `.claude-plugin/` manifests, `scripts/validate-skills.py`, AGENTS.md/CLAUDE.md. Total 2,506.

Update 2026-11-02: +8 guide skills authored on the origin machine from the tools named in the 02/11/2026 Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA" (no repo link in the video; upstreams verified by name search on 02/11/2026): `local-deep-research-guide` in `science-research/` (LearningCircuit/local-deep-research, MIT); `short-video-factory-guide`, `ai-youtube-shorts-generator-guide`, `flux2-guide` in `video-production/` (YILS-LIN/short-video-factory, AGPL-3.0; SamurAIGPT/AI-Youtube-Shorts-Generator, MIT; black-forest-labs/flux2 — model licences differ by variant, klein 4B Apache-2.0, dev/9B non-commercial); `kokoro-tts-guide`, `ace-step-music-guide`, `podcastify-guide` in `audio-music/` (hexgrad/kokoro, Apache-2.0, no Vietnamese voice; ace-step/ACE-Step, Apache-2.0); `social-media-agent-guide` in `marketing-growth/`. The apps/models themselves are NOT in this repo — the guides only explain how to use them and their limits. `podcastify-guide` and `social-media-agent-guide` are explicitly unverified: no matching repo/product was found, and they must not be used to install anything by name. Total 2,514.

Update 2026-11-02: +2 skills (Appllama/appllama-skills @ dd5caae, 2026-09-06, MIT — verbatim `skills/*` only, each skill folder carries the upstream LICENSE) in `mobile-dev/`: `appllama-usage` (v1.1.0) and `appllama-app-design-skill` (v1.3.0). REQUIREMENT: `appllama-usage` runs on the Appllama MCP (https://mcp.appllama.io/mcp), a paid Pro service with per-call credits; `appllama-app-design-skill` works standalone and is sharper with the MCP connected. No MCP connection, account or credential is configured or stored in this repo. Not in this repo: the upstream `.claude-plugin/` / `.cursor-plugin/` manifests and `mcp.json` files. Total 2,516.
