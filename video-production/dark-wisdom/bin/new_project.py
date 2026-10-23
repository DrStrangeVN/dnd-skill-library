#!/usr/bin/env python3
"""Scaffold a new motion-video project from the canonical template.

Usage:
    python3 bin/new_project.py --slug <ten-du-an> --title "<tieu de>"

Copies index.html + fonts from ~/workspace/skills-video (canonical v2
template), creates fresh renders/qa/voice dirs. Does NOT copy old
renders, voice segments, or audio beds.
"""
import argparse
import os
import shutil
import sys

TEMPLATE = os.path.expanduser("~/workspace/skills-video")
SKILL_FONTS = os.path.expanduser("~/workspace/skills/motion-video/assets/fonts")
WORKSPACE = os.path.expanduser("~/workspace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True, help="project dir name, e.g. my-topic-video")
    ap.add_argument("--title", default="", help="working title (recorded in PROJECT.md)")
    args = ap.parse_args()

    if not os.path.isfile(os.path.join(TEMPLATE, "index.html")):
        print(f"template not found: {TEMPLATE}/index.html", file=sys.stderr)
        return 1

    dest = os.path.join(WORKSPACE, args.slug)
    if os.path.exists(dest):
        print(f"exists: {dest}", file=sys.stderr)
        return 1

    os.makedirs(os.path.join(dest, "renders", "qa"))
    os.makedirs(os.path.join(dest, "voice"))
    os.makedirs(os.path.join(dest, "tmprender"))
    shutil.copy(os.path.join(TEMPLATE, "index.html"), dest)
    shutil.copytree(os.path.join(TEMPLATE, "fonts"), os.path.join(dest, "fonts"))
    # merge the skill's premium font library (v2.1) into the project
    if os.path.isdir(SKILL_FONTS):
        for fn in os.listdir(SKILL_FONTS):
            src = os.path.join(SKILL_FONTS, fn)
            if os.path.isfile(src):
                shutil.copy(src, os.path.join(dest, "fonts", fn))

    with open(os.path.join(dest, "PROJECT.md"), "w") as f:
        f.write(f"# {args.title or args.slug}\n\n")
        f.write("Motion-video project (skill `motion-video`).\n\n")
        f.write("Pipeline: voice -> composition -> render -> audio mix -> QA -> deliver.\n")
        f.write("See ~/workspace/skills/motion-video/references/pipeline.md\n")

    print(f"OK {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
