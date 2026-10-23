# ENGINE NOTES — exporter evaluation (2026-10-23, engine v3)

## Question
User judged Sky Glass v2 "chưa đạt" and authorised adopting another
engine if it helps. Candidate: **PptxGenJS** (the library `pptx`
skill's standard creation route). Test: rebuild ONLY the v3 cover
slide with PptxGenJS and compare against our python-pptx exporter.

Test artefacts: `vendor-test/cover-test.js`, `vendor-test/cover-pptxgenjs.pptx`,
rendered via LibreOffice → `vendor-test/genjs-1.png`. Ours:
`~/workspace/skillry-slides/demos/sky-glass-v3/pptx-shots/s-1.png`.

## Comparison (cover slide, LibreOffice renders of both)

| Aspect | python-pptx (ours, v3) | PptxGenJS |
| --- | --- | --- |
| Geometry / text placement | exact (single deckkit model) | exact (hand-mirrored; a second geometry source to maintain) |
| Mixed-type runs (~serif~) | native runs via parse_runs | native runs — equal |
| Letter tracking (caps kickers) | spc XML (v2) | `charSpacing` — equal result |
| Fill transparency | alpha written into fill XML | `transparency: 0–100` — equal result |
| **Frosted glass** | **YES — baked blur**: panel fill = Pillow-blurred crop of the real background under the panel (see README "Frosted glass in PPTX") | **NO backdrop blur exists**. Same Pillow bake would have to be bolted on — at which point the library adds nothing |
| Soft shadow | baked into the panel PNG (renders identically in every renderer) | first-class native shadow API (`blur/offset/opacity`) — nicer API, but renderer-dependent; LO renders it softly, PowerPoint exactly |
| Gradient fills | not supported → PNG (already our method) | not supported → PNG (same workaround) |
| Image cover-crop | manual (picture fills box) | `sizing: {type:'cover'}` — slightly nicer |
| Footguns | alpha XML is verbose but centralised in `set_alpha` | mutates option objects in place; 8-digit hex corrupts the file; `transparency` vs `opacity` split silently ignored if swapped; default layout is 10×5.625in unless set first |
| Verification | verify.py + read-back pass today (55 text frames, notes 6/6) | would need the whole verify chain re-proven |

## Decision
**Keep python-pptx + baked blur. Do not adopt PptxGenJS.**
Per the decision rule it is not *clearly better* on the cover test:
its only real edge is the native shadow API, while the feature that
actually closed the v2 gap — frosted glass — comes from our Pillow
bake, which is exporter-agnostic and already integrated. Rewriting
the exporter would add a second geometry implementation and new
footguns for no visual gain. Revisit only if a future deck needs
PptxGenJS-only features (e.g. native charts/tables at scale).

## From the library skills (skimmed)
- `pptx` SKILL.md: confirms the gotchas above from hard experience;
  its "render and inspect" QA loop matches ours (we use LibreOffice
  → PDF → PNG the same way).
- `slides` SKILL.md: HTML/Chart.js presentation system; its
  design-token discipline is what our `theme.json` already does.
  Nothing transferable to the PPTX glass problem.
