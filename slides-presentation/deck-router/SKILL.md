---
name: deck-router
description: Route a presentation request to the right Presentation Pro workflow when the user asks generally to make, improve, analyze, or structure a PowerPoint, presentation, deck, report, proposal, sponsor deck, event deck, pitch deck, or executive presentation.
---
# Deck Router

Use this skill when the user asks for presentation work but does not name a specific Presentation Pro workflow.

## Routing rules

1. Classify the primary goal before creating slides.
2. Choose one primary workflow and add supporting workflows only when they materially help.
3. Respect explicit user instructions over defaults.
4. Do not force the user to choose a mode when the request is clear enough to route automatically.

## Primary routes

- Performance, KPI, monthly, quarterly, season, campaign, financial or operating review -> `report-deck`.
- Client, partnership, service, project or business proposal -> `proposal-deck`.
- Sponsor, rights package, activation, renewal, commercial partnership -> `sponsor-deck`.
- Event concept, launch, activation, run-of-show, event plan -> `event-deck`.
- Investor, fundraising, strategic business case or project pitch -> `pitch-deck`.
- Existing PowerPoint that needs cleanup, modernization or restructuring -> `deck-redesign`.
- Spreadsheet, table or raw metrics that must become charts and insight slides -> `data-to-slide` plus the relevant primary route.
- Brand kit, visual identity, template or style consistency request -> `brand-system` plus the relevant primary route.
- Review before delivery -> `deck-qa`.
- Very short leadership summary or 1-3 slide synthesis -> `executive-summary`.
- User asks to choose a reusable visual format -> `template-system`.

## Recommended pipeline

For a full deck, prefer:
`route -> source review -> storyline -> content -> data visuals -> brand/template -> build -> QA -> final artifact`.

Do not invent missing business facts. If a missing detail is non-critical, proceed with a clearly marked assumption rather than blocking the task.
