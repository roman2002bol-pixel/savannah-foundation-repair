#!/usr/bin/env python3
"""Fail if any page shows the same photo more than once.

Why this exists: Roman spotted the same excavation photo twice on the
foundation site's homepage (2026-09-16) -- once in the proof band, once in
the geology section, both at full size, a screen apart. Scanning the whole
site then found the same fault on all 23 interior pages, where the page-hero
background and the body image were the same file. It is invisible while you
are writing one section at a time and obvious to anyone who scrolls.

Counts both `<img src>` and CSS `url(...)` backgrounds in inline styles,
because a hero background and a body <img> of the same file is exactly the
case that kept slipping through.

The same photo appearing on SEVERAL pages is fine and not reported -- a shot
of our own work legitimately recurs. Only repeats within one page are errors.

Run from a site root:  python .claude/skills/microsite-agent/scripts/check_image_reuse.py
"""
import collections
import pathlib
import re
import sys

# Marks and icons legitimately repeat within a page (logo in header + footer).
ALLOW_SUFFIX = (".svg",)
ALLOW_NAMES = {"logo.svg", "favicon.ico"}

REF = re.compile(r'(?:src="|srcset="|url\(&quot;|url\(\'|url\("|url\()'
                 r'[^"\')]*?images/([A-Za-z0-9._@-]+)')


def main(root="."):
    root = pathlib.Path(root).resolve()
    problems = []
    pages = 0
    for f in sorted(root.rglob("*.html")):
        if ".claude" in f.parts or "node_modules" in f.parts:
            continue
        pages += 1
        text = f.read_text(encoding="utf-8", errors="replace")
        counts = collections.Counter(
            name for name in REF.findall(text)
            if not name.lower().endswith(ALLOW_SUFFIX) and name not in ALLOW_NAMES
        )
        for name, n in sorted(counts.items()):
            if n > 1:
                problems.append((f.relative_to(root), name, n))

    if not problems:
        print(f"OK - no image is used twice on the same page, across {pages} "
              f"HTML files under {root}")
        return 0

    print(f"{len(problems)} repeated image(s) within a single page:\n")
    for path, name, n in problems:
        print(f"  {path}  ->  {name}  x{n}")
    print("\nGive the page a second, genuinely different photo, or drop one of "
          "the two slots. Reusing the hero photo as the body image counts: "
          "under a dark overlay it reads as texture to whoever wrote it and as "
          "the same picture to everyone else.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
