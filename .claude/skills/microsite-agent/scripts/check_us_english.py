#!/usr/bin/env python3
"""Fail if British spellings appear on a US local-SEO site.

Why this exists: these sites are written for one American city, and British
spellings are a tell that the copy was not written by someone local. It has
happened twice on the Savannah foundation site -- 58 occurrences found in one
pass (levelling, stabilisation, vapour, neighbourhood, behaviour) and another
58 in the next (galvanised, storey, ageing, localised, recognise) -- because
the words arrive one at a time inside otherwise good prose and nothing
flags them. Grepping for a list is instant; noticing them by eye is not.

Checks HTML, the Python generators and llms.txt, so a fix lands in
the generator rather than only in its output.

Run from a site root:  python .claude/skills/microsite-agent/scripts/check_us_english.py
"""
import pathlib
import re
import sys

# british -> american. Ordered longest-first within a family so that
# "two-storey" is reported as itself rather than as bare "storey".
PAIRS = [
    ("levelling", "leveling"),
    ("stabilis", "stabiliz"),
    ("galvanis", "galvaniz"),
    ("vapour", "vapor"),
    ("neighbourhood", "neighborhood"),
    ("behaviour", "behavior"),
    ("colour", "color"),
    ("favour", "favor"),
    ("harbour", "harbor"),
    ("labour", "labor"),
    ("ageing", "aging"),
    ("storey", "story"),
    ("localis", "localiz"),
    ("recognis", "recogniz"),
    ("organis", "organiz"),
    ("utilis", "utiliz"),
    ("prioritis", "prioritiz"),
    ("modernis", "moderniz"),
    ("apologis", "apologiz"),
    ("summaris", "summariz"),
    ("analys", "analyz"),
    ("defence", "defense"),
    ("licence", "license"),
    ("practise", "practice"),
    ("centre", "center"),
    ("metre", "meter"),
    ("fibre", "fiber"),
    ("mould", "mold"),
    ("enquir", "inquir"),
    ("whilst", "while"),
    ("towards the", "toward the"),
]

# Words that merely contain a pattern above but are correct American English.
# "analysis" contains "analys"; "paralysis" and "catalyst" do too.
ALLOW = re.compile(r"\b(analysis|analyses|analyst\w*|paralys\w*|catalys\w*)\b", re.I)

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".claude"}
# .md is deliberately excluded: STATUS.md and CLAUDE.md are internal notes
# that legitimately quote these words when recording the fix.
EXTS = {".html", ".py", ".txt"}


def main(root="."):
    root = pathlib.Path(root).resolve()
    hits = []
    for f in sorted(root.rglob("*")):
        if f.suffix.lower() not in EXTS or not f.is_file():
            continue
        if SKIP_DIRS & set(f.parts):
            continue
        for lineno, line in enumerate(f.read_text(encoding="utf-8",
                                                  errors="replace").splitlines(), 1):
            stripped = ALLOW.sub("", line)
            for bad, good in PAIRS:
                for m in re.finditer(re.escape(bad), stripped, re.I):
                    word = re.search(r"[A-Za-z-]*" + re.escape(bad) + r"[A-Za-z]*",
                                     stripped[m.start():m.start() + 40], re.I)
                    hits.append((f.relative_to(root), lineno,
                                 word.group(0) if word else bad, good))
                    break  # one report per pattern per line is enough

    if not hits:
        print(f"OK - no British spellings in {len(EXTS)} file types under {root}")
        return 0

    print(f"{len(hits)} British spelling(s) on a US local site:\n")
    for path, lineno, found, good in hits:
        print(f"  {path}:{lineno}  {found}  ->  ...{good}...")
    print("\nFix these in the GENERATOR (build_*.py) where one exists, not just "
          "in the generated HTML, or the next build puts them back.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
