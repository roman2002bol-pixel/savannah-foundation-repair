#!/usr/bin/env python3
"""
check_broken_links.py — verify every internal href/src across a static
microsite actually resolves to a real file on disk.

Why this exists: hub-and-spoke microsites cross-link constantly (nav,
footer, breadcrumbs, area-chips, FAQ answers). A single typo'd path or a
page that references a not-yet-built sibling silently 404s in production
— GitHub Pages / Cloudflare Pages give no build-time warning for this on
a plain static site. Run this after every batch of new/edited pages,
before committing.

Usage (from the project root, i.e. the folder containing index.html):
    python .claude/skills/microsite-agent/scripts/check_broken_links.py

Or from anywhere, passing the project root explicitly:
    python check_broken_links.py /path/to/project

Exits with status 1 and a non-empty report if anything is broken;
exits 0 and prints a one-line summary if everything resolves.

What it checks: every href="..." and src="..." in every *.html file
found recursively under the project root, excluding external links
(http/https), tel:, sms:, mailto:, in-page anchors (#...), and data:
URIs. Query strings (?v=1) and in-page anchors (#services) are stripped
before resolving, since those aren't part of the filesystem path.

What it does NOT check: external URLs actually resolving (that's a
different, slower check — not needed for a pre-commit sanity pass), or
whether a resolved file is itself valid HTML.
"""
import re
import os
import sys
import glob

def find_html_files(root):
    return glob.glob(os.path.join(root, "**", "*.html"), recursive=True)

def check(root):
    files = find_html_files(root)
    broken = []
    for f in files:
        with open(f, "r", encoding="utf-8") as fh:
            content = fh.read()
        base_dir = os.path.dirname(f)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', content):
            href = m.group(1)
            if href.startswith(("http://", "https://", "tel:", "sms:", "mailto:", "#", "data:", "javascript:")):
                continue
            path_part = href.split("#")[0].split("?")[0]
            if not path_part:
                continue
            resolved = os.path.normpath(os.path.join(base_dir, path_part))
            if not os.path.isfile(resolved):
                broken.append((os.path.relpath(f, root), href, resolved))
    return files, broken

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    root = os.path.abspath(root)
    files, broken = check(root)
    if broken:
        print(f"BROKEN LINKS/ASSETS ({len(broken)}):")
        for f, href, resolved in broken:
            print(f"  {f} -> {href}")
        sys.exit(1)
    else:
        print(f"OK — no broken internal links or asset references across {len(files)} HTML files under {root}")
        sys.exit(0)

if __name__ == "__main__":
    main()
