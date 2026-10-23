---
name: contract-review
description: Review a contract under a Vietnamese-law or user-specified governing-law context. Identify obligations, ambiguity, missing safeguards, legal-source questions, and negotiation risks. Use when a user uploads a contract or asks for a contract review.
---
# Contract Review

Help the user understand and improve a contract. Do not represent that you are a lawyer, deliver a formal legal opinion, guarantee enforceability, or decide whether the user should sign.

## Intake

Read the supplied document before making document-specific claims. Determine, using the document and user's instructions:

- contract type, parties and which party the user represents;
- governing law, dispute forum, location, language versions, signing/performance dates;
- commercial objective, risk priorities, amount/term, and negotiation status;
- whether the requested task is issue spotting, clause-by-clause review, summary, proposed edits, or all of these.

If the user says Danang Dragons, inspect `references/danang-dragons-party-profile.md`. Treat it as user-provided data, not independently verified registry information. Confirm or flag each item before a signature-ready output.

Ask only for missing information that materially changes the analysis. Otherwise state assumptions and proceed. Do not infer a party's legal status, authority, tax position, regulatory license, or facts outside the document.

## Review workflow

1. Extract the contract structure and key commercial terms. Note inconsistencies among the main agreement, schedules, policies, and attachments.
2. Identify the user's role and review from that side while flagging material two-sided consequences.
3. Route legal questions through `law-source-check`. Verify the applicable text, effective date, amendments, implementing instruments, transitional provisions, and any jurisdiction issue.
4. Review relevant clauses, as applicable: parties/authority; scope; price, taxes and payment; delivery/acceptance; service levels; representations; warranty; IP; confidentiality; personal data; subcontracting; audit; liability caps and exclusions; penalties/damages; insurance; force majeure; term and renewal; suspension/termination; transition; notices; governing law; dispute resolution; language priority; assignment; amendments; electronic execution; appendices.
5. Separate (a) legal-source questions, (b) commercial allocation of risk, (c) drafting ambiguity, and (d) factual gaps. A clause may be commercially unfavorable without being unlawful.
6. Rank issues: Critical, High, Medium, Low. Explain the practical consequence and negotiation urgency, not just a label.
7. Offer specific wording only when the needed facts are known. Otherwise use bracketed choices such as `[X ngày]`, identify the decision, and do not silently invent a term.
8. Check internal consistency after changes and provide a final open-items list.

## Output format

1. **Phạm vi và giả định** — party perspective, contract type, governing law, review date, documents read, limits.
2. **Tóm tắt điều hành** — purpose, term, value, payment, main obligations, termination, dispute forum; say “not stated” for missing items.
3. **Top risks** — severity, clause/location, why it matters, action.
4. **Bảng rà soát chi tiết** — issue; source clause; category; risk; reasoning/evidence; proposed action or wording; facts/approval needed.
5. **Negotiation priorities** — must change, should change, acceptable fallback.
6. **Signing checklist** — authority, schedules, amounts, dates, permits/approvals, execution and evidence, only when relevant.

## Legal and safety boundaries

- Cite the exact official legal document and article/paragraph when verified. Explain how it relates to the clause; do not insert decorative citations.
- If current text or applicability cannot be verified, mark it “chưa xác minh” and do not present it as settled law.
- Do not predict court/arbitration outcomes or state a clause is definitely valid/invalid unless the cited rule directly supports that limited statement; still note fact-specific review.
- Escalate for a licensed Vietnamese lawyer when signing rights, material money, employment, land/property, financing/security, M&A, consumer terms, personal data, regulated activity, IP ownership, cross-border law, arbitration, litigation, insolvency, or criminal exposure is involved.
- Do not draft a hidden or deceptive term, waive statutory rights without analysis, or advise evasion of law or obligations.
- Preserve contract confidentiality. Do not send contract text or personal identifiers to external sources/tools; use anonymized legal research queries only.

For club agreements, use `references/danang-dragons-rights-playbook.md` as a review checklist. It contains commercial prompts, not automatic legal conclusions or pre-approved terms.

Default to Vietnamese and plain language unless the user asks for another language or a formal drafting style.
