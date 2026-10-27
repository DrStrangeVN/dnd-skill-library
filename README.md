# Skill Library — Danang Dragons / Vũ Đình Trí

Private consolidated library of every Muse skill built or curated on the
origin machine, organised by category so any of the user's Muse instances can
clone this repo, copy the skills into its own `~/workspace/custom-skills/`, and
work with the same playbooks. See **SETUP.md** for a fresh-machine walkthrough
and **INDEX.md** for the full skill list.

## Contents

- **2,407 skills** in 24 category folders (layout: `<category>/<skill-name>/SKILL.md` + the skill's own references/scripts/assets).
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
