#!/usr/bin/env python3
"""Fail if a site that uses clean URLs still advertises `.html` addresses.

Why this exists: Cloudflare's static hosting answers every `/page.html` with a
307 redirect to `/page`. NEXUS shipped canonical tags, og:url, JSON-LD, the
sitemap and every internal link as `.html`, so 9 of its 10 sitemap URLs
redirected to a page whose canonical pointed back at the redirecting URL.
Search Console then listed the extensionless twins as "not indexed", which
read as half the site missing (2026-10-12).

The rule: whatever the visitor and Google are served with a 200 is the URL
the site must name. On Cloudflare that is the extensionless form, so:

  * <link rel="canonical">, og:url and JSON-LD url/item/@id values
  * every <loc> in sitemap.xml
  * every relative internal href

must not end in `.html`, and must not name `index.html` (use `./`, `../`,
or the bare domain with a trailing slash).

Run from a site root:
    python .claude/skills/microsite-agent/scripts/check_clean_urls.py
"""

import pathlib
import re
import sys

SKIP_DIRS = {".git", "node_modules", "__pycache__", ".claude"}
HTML_URL = re.compile(r"\.html(?:[#?]|$)")


def bad(url):
    return bool(HTML_URL.search(url))


def main(root="."):
    root = pathlib.Path(root).resolve()
    problems = []
    pages = 0
    for f in sorted(root.rglob("*.html")):
        if SKIP_DIRS & set(f.relative_to(root).parts):
            continue
        pages += 1
        rel = f.relative_to(root)
        s = f.read_text(encoding="utf-8", errors="replace")

        for m in re.finditer(r'<link rel="canonical" href="([^"]+)"', s):
            if bad(m.group(1)):
                problems.append(f"{rel}: canonical {m.group(1)}")
        for m in re.finditer(r'<meta property="og:url" content="([^"]+)"', s):
            if bad(m.group(1)):
                problems.append(f"{rel}: og:url {m.group(1)}")
        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            for m in re.finditer(r'"(?:url|item|@id)"\s*:\s*"([^"]+)"', block):
                if bad(m.group(1)):
                    problems.append(f"{rel}: JSON-LD {m.group(1)}")
        for m in re.finditer(r'href="([^"]+)"', s):
            href = m.group(1)
            if href.startswith(("http://", "https://", "tel:", "sms:", "mailto:",
                                "#", "data:", "javascript:", "//")):
                continue
            if bad(href):
                problems.append(f"{rel}: link {href}")

    sitemap = root / "sitemap.xml"
    if sitemap.exists():
        for loc in re.findall(r"<loc>([^<]+)</loc>", sitemap.read_text(encoding="utf-8")):
            if bad(loc.strip()):
                problems.append(f"sitemap.xml: {loc.strip()}")

    if not problems:
        print(f"OK - no .html URLs advertised in canonicals, og:url, JSON-LD, "
              f"sitemap or internal links, across {pages} HTML files under {root}")
        return 0

    # group by file so 400 links on 20 pages reads as 20 lines, not 400
    by_file = {}
    for p in problems:
        by_file.setdefault(p.split(":", 1)[0], []).append(p.split(": ", 1)[1])
    print(f"{len(problems)} .html URL(s) advertised on a clean-URL site:\n")
    for f, items in by_file.items():
        print(f"  {f} ({len(items)}): " + ", ".join(items[:3]) + (" ..." if len(items) > 3 else ""))
    print("\nOn Cloudflare each of these answers with a redirect. Name the URL "
          "that is actually served with 200 -- without .html.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
