---
name: pdf-to-word-vietnamese
description: Convert a Vietnamese PDF, including scanned or image-only pages, into an editable DOCX. Use when the user wants PDF-to-Word conversion, OCR transcription, or a faithful editable copy that preserves the source wording and layout. Never silently correct, paraphrase, add, or omit source content; inspect OCR against page images and report unresolved areas separately.
---

# Vietnamese PDF to Editable Word

Convert the user's PDF into an editable `.docx` while preserving the source wording, reading order, and visual structure as closely as the source and available tools allow. The PDF is authoritative. The task is transcription and layout reconstruction, not proofreading or rewriting.

## Required workflow

1. **Inventory the source.** Confirm page count, page dimensions/orientation, whether text is embedded or pages are scans, and whether the PDF has columns, tables, forms, footnotes, handwriting, stamps, signatures, or image-only sections. Keep the source unchanged.
2. **Extract or OCR page by page.** For text PDFs, extract text but also inspect rendered pages where reading order or layout may be ambiguous. For scans, render every page and read the image itself; OCR is a draft, not proof. Preserve paragraph order, line/column order, headings, list numbering, punctuation, capitalization, spacing-sensitive identifiers, and page furniture that carries content.
3. **Transcribe exactly.** Do not spell-correct or normalize the source. Preserve apparent misspellings, inconsistent terms, punctuation, dates, amounts, units, abbreviations, and unusual capitalization exactly as printed. Do not use context to silently resolve illegible text. Do not add a title page, explanatory labels, OCR markers, headers, footers, or page numbers absent from the source.
4. **Rebuild the document.** Use editable Word paragraphs, headings, tables, lists, columns, tab stops, and page/section breaks where suitable. Match page size, orientation, margins, typography, indentation, alignment, line spacing, borders, fills, and page breaks as closely as practical. Do not flatten whole scanned pages into images as the only output: body text must be editable. Preserve non-text visual material such as logos, seals, signatures, photographs, diagrams, and complex form backgrounds as images when accurate editable reconstruction is not feasible; do not invent what they depict.
5. **Verify Vietnamese OCR.** Inspect every page at readable zoom. Check diacritics and visually similar characters in context, especially `a/ă/â`, `e/ê`, `o/ô/ơ`, `u/ư`, `d/đ`; tone marks `sắc/huyền/hỏi/ngã/nặng`; uppercase accented letters; punctuation; `0/O`, `1/I/l`; decimals, thousands separators, dates, account/tax/identity numbers, units, legal references, and footnote markers. Zoom or crop unclear regions rather than guessing.
6. **Check content parity.** Compare source extraction/OCR against DOCX text page by page. Check first and last lines, repeated headers/footers, table rows/columns, list numbering, page transitions, and all numbers/names. Ensure there are no duplicated, dropped, reordered, or normalized words. The comparison must not treat spelling differences as a request to fix the source.
7. **Render and inspect.** Render the finished DOCX to page images. Inspect every page for clipping, overlap, broken Vietnamese glyphs, table overflow, misplaced images, unexpected blank pages, and layout drift. Make corrections and render again. Confirm the output opens as a valid editable DOCX.
8. **Report uncertainty separately.** If any characters or graphic details cannot be confirmed, provide a concise list outside the DOCX body with page number, location/short excerpt, and reason (blur, cut-off, handwriting, seal overlap, low resolution). Do not claim complete accuracy or silently replace uncertainty with a guess. If uncertainty is material to a name, amount, obligation, identifier, or other critical content, call it out prominently.
9. **Deliver.** Return the DOCX, page count, a brief statement on layout fidelity, and any unresolved OCR locations. Do not include QA render images or an extra report file unless requested.

## Fidelity rules

- No paraphrasing, summarizing, translating, rewriting, proofreading, legal interpretation, or fact correction during conversion.
- Do not insert text inferred from context or from outside sources.
- Do not remove duplicated or apparently accidental source content; reproduce what is present.
- Preserve content-bearing footnotes, endnotes, page numbers, running headers/footers, marginal text, form labels, and handwritten entries when legible.
- When text is illegible, retain the best image-supported transcription and flag the precise uncertainty separately. If no defensible transcription is possible, do not fabricate; explain the limitation and preserve the affected region as a source image in the editable document where feasible.
- A DOCX cannot guarantee pixel-identical pagination across Word versions, operating systems, and installed fonts. Describe layout as “faithful” or “close” only after visual inspection.
- Never claim OCR is error-free. Confidence comes from visual comparison, not from OCR output alone.

## File privacy

Keep the document in the current session and use available local PDF/DOCX tools. Do not upload or send document contents to external OCR, file conversion, or web services. Do not browse for a matching copy of a private document.

## Output formatting

- Preserve the original page size, orientation, and visual hierarchy when they can be determined.
- Favor editable Word elements over page screenshots. Keep tables editable when practical and preserve row/column relationships.
- Keep source images for non-text marks or difficult visual elements, at readable resolution and in the corresponding location.
- Do not add editorial cover pages, conversion notes, new page numbers, or new substantive text.
- Save as a descriptive `.docx` filename based on the source filename where possible; never overwrite the PDF.

## Tool guidance

Use available PDF tools for page inventory, text extraction, rendering, and image inspection. Use available document tools to build, render, and validate DOCX. If OCR or DOCX generation is unavailable, say exactly which step could not be completed and provide the best useful alternative; never claim a file was created when it was not.
