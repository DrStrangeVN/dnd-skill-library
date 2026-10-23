# BUILD-REPORT — initial consolidation (2026-10-23)

Assembled locally on the origin machine from `~/workspace/custom-skills/`.
**Not pushed** — GitHub auth is pending on the user; this repo has no remote.

## Counts

| Set | Skills |
|---|---|
| Audited library (inventory 2026-10-23) | 2,545 |
| — KEEP per `skill-inventory/keep.csv` | 2,320 |
| — DROP per `skill-inventory/drop.csv` (user approved all 225; repo only, local library untouched) | 225 |
| Authored after the audit (KEEP by default) | 64 |
| **Total in this repo** | **2,384** |

Post-audit additions (64): 61 Skillry-Slides style skills `deck-*-deck`,
master `deck-studio` (→ `slides-presentation`), `opuscar-telestrator`
(→ `video-production`), `web-liquid-glass-landing` (→ `web-dev`).

Categories (24): ai-agents-llm 258 · audio-music 18 · automation-workflow 32 ·
backend-api 233 · business-sales 70 · data-analytics 106 · design-uiux 332 ·
devops-cloud 190 · education 7 · finance 16 · games-interactive 14 ·
image-design 32 · legal-hr-ops 35 · marketing-growth 87 · mobile-dev 6 ·
product-management 3 · productivity-office 208 · science-research 82 ·
security 52 · slides-presentation 127 · software-engineering 107 · sports 2 ·
video-production 184 · web-dev 183.

Repo size at initial commit: ~143 MB working tree (audit estimate was ~116 MB
for skills alone; the difference is the `samples/` images and doc set).

## Category source decision

`categories.csv` in the inventory still holds pre-triage values for some
skills (e.g. `1password-pro` = `uncategorized`). The audit designates
`keep.csv` as the final slug+category list ("Category cuối cùng nằm trong
keep.csv"), so **keep.csv categories were used** for all 2,320 audited skills.

## Exclusions (files, with reasons)

- **dark-wisdom B-roll — 12 × .mp4, ~524 MB total** (DECISIONS.md #1; two files
  >100 MB would also break GitHub limits). The skill itself is included with
  SKILL.md, references, scripts, icons and the B-roll `manifest.json`; only the
  video media stays local:
  broll-nen.mp4 (3.6 MB), broll-toa-nha.mp4 (2.9), broll-pho-dem.mp4 (2.8),
  broll-bokeh-xe.mp4 (2.0), broll-dam-dong.mp4 (2.6), broll-mua-kinh.mp4 (1.6),
  broll-bien-dem.mp4 (34.4), broll-bokeh-xe-full.mp4 (173.6),
  broll-toa-nha-full.mp4 (42.1), broll-nen-full.mp4 (54.8),
  broll-pho-dem-full.mp4 (95.5), broll-bien-dem-full.mp4 (108.0).
  A `.gitignore` pattern blocks re-adding them.
- **__pycache__ dirs (4)**: `motion-video/bin/`, `pptx/scripts/office/helpers/`,
  `pptx/scripts/office/validators/`, `vieneu-api-client/`.
- **>25 MB rule**: besides the dark-wisdom media above, no file in the kept
  set exceeded 25 MB; nothing else was excluded by size.
- No `.git` or `node_modules` directories existed in the kept set; no symlinks.

## Secret review (DECISIONS.md #2 — 18 flagged skills)

16 of the 18 flagged skills are in the repo set; the other two (`gtars`,
`muse-burner`) are in the DROP set and absent. Every secret-suggesting file in
the 16 was listed and read. **Result: no file contained an actual credential
value; zero files excluded.** A filename scan of the whole kept set found no
secret-pattern files beyond these.

| Skill | File(s) reviewed | Verdict |
|---|---|---|
| ai-video-prompts | prompts/lordsecretive-1251476.md | KEEP — a one-line video prompt; "secretive" is the source author's handle, no credential |
| audit-design-system | references/token-taxonomy.md | KEEP — design-token taxonomy doc |
| book-to-skill | scripts/token_budget_estimator.py | KEEP — LLM token-budget estimator |
| building-components | references/design-tokens.mdx | KEEP — design tokens doc |
| design-system | references/{component,primitive,semantic}-tokens.md, token-architecture.md, templates/design-tokens-starter.json | KEEP — design-token docs/template |
| env-secrets-manager | references/secret-patterns.md | KEEP — defensive detection-pattern reference, no values |
| fastmcp-server | references/authentication/token-verification.md | KEEP — how-to doc on verifying tokens |
| figma-plugin-api-rules | references/variables-and-tokens.md | KEEP — Figma variables doc |
| jev-seo | .env.example | KEEP — template, all values empty |
| modal | references/secrets.md | KEEP — Modal docs; examples use placeholders ("value1", "secret-value") |
| perplexity-search | assets/.env.example | KEEP — template; value is the literal placeholder "sk-or-v1-your-api-key-here" |
| publish-artifact-to-sites | scripts/publication-secrets.mjs | KEEP — a defensive scanner that detects credentials before publishing; contains patterns, no values |
| sites | references/identity-and-secrets.md | KEEP — guidance doc; key names only |
| transformers | references/tokenizers.md | KEEP — ML tokenizers doc |
| ui-design-system | scripts/design_token_generator.py | KEEP — design-token generator |
| wp-patterns | references/design-with-tokens.md | KEEP — design tokens doc |

Second line of defence: root `.gitignore` blocks `.env*` (except
`.env.example`), `*.pem`, `*.key`, `*.p12`, `*.keystore`, `id_rsa*`,
`id_ed25519*` for future commits.

## Samples (authored packs)

106 sample images across 101 skills (each skill ≤ ~2 MB, JPEG, max 1600 px):

- 61 × `deck-*`: Skillry preview-1 still; the 4 styles with house demos also
  carry demo sheets (cobalt-dark-pitch, gallery-catalogue, confetti-gathering,
  sky-glass v3 + its side-by-side comparison).
- `deck-studio`: sky-glass-v3 + cobalt demo sheets.
- ReelCrew 23 × `*-video`: demo contact sheet each.
- Opus55 family 14 skills: their demo sheets (canvas/svg-gsap/shader/threejs,
  explainer kinetic + voice, 3D island + raymarch, game breakout + runner).
  `opus-explainer-3d`, `opus-game-threejs`, `opus-game-prd` have **no samples**
  — no dedicated demo was ever produced for them; nothing was fabricated.
- `opuscar-telestrator`: pick-&-roll demo sheet. `web-liquid-glass-landing`:
  Quietline hero screenshot + contact sheet.
- `local-real-estate-video`: **no samples** — no production run exists on the
  origin machine yet, so there is no deliverable to sample.

## Known gaps / decisions made during the build

- The **deck-studio engine code** (`~/workspace/deck-studio/`) and the
  **video-kit pipeline** are companion tooling, not skills, and are **not** in
  this repo (the build spec covered the skill library). SETUP.md documents
  what a fresh machine must recreate. Folding the engine in as a `tools/`
  folder is a sensible follow-up if the user wants one-clone setup.
- **RESYNC.txt**: the 3 deck skills under fidelity rework were copied last;
  re-copy them before the first push as described there.
- Commit identity is repo-local config (the machine has no global git
  identity): "Vu Dinh Tri <gm@danangdragons.com>".
