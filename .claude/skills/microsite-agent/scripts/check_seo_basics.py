#!/usr/bin/env python3
"""On-page SEO basics that are cheap to get wrong and invisible until indexed.

Written after a full-site audit of Savannah Foundation Repair (2026-09-15)
found ten pages with titles over the SERP truncation length -- caused by a
29-character brand name being appended to every title by the generator. None
of the other checks could see it: links resolved, schema matched, markup was
valid. It was only visible by measuring.

Checks, per page:
  * <title> present, unique across the site, <= 62 chars
  * meta description present, unique, 70-160 chars
  * exactly one <h1>
  * canonical link present
  * every JSON-LD block parses as valid JSON
  * every <img> has an alt attribute

Usage:  python check_seo_basics.py [project_root]
Exit 0 = clean, exit 1 = problems found.
"""
import json
import pathlib
import re
import sys

TITLE_MAX = 62
DESC_MIN, DESC_MAX = 70, 160


def main(root_arg: str) -> int:
    root = pathlib.Path(root_arg).resolve()
    pages = sorted(p for p in root.rglob("*.html") if ".claude" not in p.parts)
    if not pages:
        print(f"No HTML files found under {root}")
        return 1

    problems, titles, descs = [], {}, {}

    for path in pages:
        html = path.read_text(encoding="utf-8")
        rel = path.relative_to(root).as_posix()

        m = re.search(r"<title>(.*?)</title>", html, re.S)
        if not m:
            problems.append(f"{rel}: no <title>")
        else:
            title = re.sub("<[^>]+>", "", m.group(1)).strip()
            titles.setdefault(title, []).append(rel)
            if len(title) > TITLE_MAX:
                problems.append(
                    f"{rel}: title is {len(title)} chars (>{TITLE_MAX}); "
                    f"Google will truncate it")

        m = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
        if not m:
            problems.append(f"{rel}: no meta description")
        else:
            desc = m.group(1).strip()
            descs.setdefault(desc, []).append(rel)
            if len(desc) > DESC_MAX:
                problems.append(f"{rel}: meta description {len(desc)} chars (>{DESC_MAX})")
            elif len(desc) < DESC_MIN:
                problems.append(f"{rel}: meta description only {len(desc)} chars (thin)")

        h1s = re.findall(r"<h1[^>]*>", html)
        if len(h1s) != 1:
            problems.append(f"{rel}: {len(h1s)} <h1> tags, must be exactly 1")

        if not re.search(r'<link[^>]+rel="canonical"', html):
            problems.append(f"{rel}: no canonical link")

        for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>',
                                html, re.S):
            try:
                json.loads(block)
            except Exception as exc:
                problems.append(f"{rel}: JSON-LD does not parse -- {exc}")

        for tag in re.findall(r"<img[^>]*>", html):
            if 'alt="' not in tag:
                problems.append(f"{rel}: <img> with no alt attribute")

    for title, where in titles.items():
        if len(where) > 1:
            problems.append(f"duplicate <title> on {where}: {title[:55]!r}")
    for desc, where in descs.items():
        if len(where) > 1:
            problems.append(f"duplicate meta description on {where}")

    if problems:
        print(f"SEO PROBLEMS ({len(problems)}):")
        for p in problems:
            print("  " + p)
        return 1

    print(f"OK - titles unique and within {TITLE_MAX} chars, descriptions unique "
          f"and {DESC_MIN}-{DESC_MAX} chars, one H1 per page, canonicals present, "
          f"JSON-LD valid, every image has alt text, across {len(pages)} pages "
          f"under {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
