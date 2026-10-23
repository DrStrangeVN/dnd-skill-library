#!/usr/bin/env python3
"""verify.py — read back exported PPTX files and check them against the spec.

Usage (deck venv python):
  verify.py DECK.json OUT.pptx [OUT2.pptx ...]
Checks per file: slide count == spec, slide 1 contains the deck's cover
title text, every slide has >=1 text frame with text, notes present on
every slide that has notes in the spec.
"""
import json
import sys

from pptx import Presentation


def slide_texts(slide):
    out = []
    for shp in slide.shapes:
        if shp.has_text_frame:
            t = shp.text_frame.text.strip()
            if t:
                out.append(t)
    return out


def main():
    spec = json.load(open(sys.argv[1], encoding="utf-8"))
    slides_spec = spec["slides"]
    cover_title = slides_spec[0].get("title", "").split("\n")[0].strip()
    ok_all = True
    for path in sys.argv[2:]:
        prs = Presentation(path)
        n = len(prs.slides._sldIdLst)
        texts_per_slide = [slide_texts(s) for s in prs.slides]
        notes_ok = 0
        for s, sspec in zip(prs.slides, slides_spec):
            if sspec.get("notes"):
                if s.has_notes_slide and s.notes_slide.notes_text_frame.text.strip():
                    notes_ok += 1
        need_notes = sum(1 for s in slides_spec if s.get("notes"))
        checks = {
            "slide_count": n == len(slides_spec),
            "cover_title_on_slide1": any(cover_title in t for t in texts_per_slide[0]),
            "every_slide_has_text": all(len(t) > 0 for t in texts_per_slide),
            "notes_present": notes_ok == need_notes,
        }
        print(f"== {path}")
        print(f"   slides={n} (spec {len(slides_spec)}), notes {notes_ok}/{need_notes}, "
              f"text frames total={sum(len(t) for t in texts_per_slide)}")
        for k, v in checks.items():
            print(f"   [{'PASS' if v else 'FAIL'}] {k}")
        ok_all = ok_all and all(checks.values())
    print("ALL PASS" if ok_all else "SOME CHECKS FAILED")
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
