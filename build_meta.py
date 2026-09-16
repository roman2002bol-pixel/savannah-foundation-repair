#!/usr/bin/env python3
"""sitemap.xml and the llms.txt area list, generated. Run: python build_meta.py

These two files used to be maintained by hand, which is a standing invitation
to add a page and forget one of them. Both are now derived from the same
SERVICES / area data the pages themselves are built from, so a new location
page cannot be missing from the sitemap.
"""
import datetime
import html as H
import pathlib
import re

from build_pages import SITE, SERVICES, ROOT
from build_areas import PAGES as AREA_PAGES

TODAY = datetime.date.today().isoformat()

CORE = [
    ("free-inspection.html", "0.8"),
    ("about.html", "0.6"),
    ("contact.html", "0.6"),
    ("faq.html", "0.6"),
    ("privacy-policy.html", "0.3"),
    ("terms.html", "0.3"),
]


def build_sitemap():
    urls = [("", "1.0")]
    urls += CORE
    urls += [(f"services/{slug}.html", "0.9") for slug, _ in SERVICES]
    urls += [("service-areas/index.html", "0.8")]
    urls += [(f"service-areas/{a['slug']}.html", "0.7") for a in AREA_PAGES]

    body = "\n".join(
        f"  <url>\n"
        f"    <loc>{SITE}/{path}</loc>\n"
        f"    <lastmod>{TODAY}</lastmod>\n"
        f"    <priority>{pri}</priority>\n"
        f"  </url>"
        for path, pri in urls
    )
    out = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{body}\n</urlset>\n")
    (ROOT / "sitemap.xml").write_text(out, encoding="utf-8")
    print(f"  sitemap.xml: {len(urls)} URLs")


def build_llms_areas():
    """Rewrite only the area list in llms.txt, between the marker comments.
    The prose around it is hand-written and stays that way."""
    path = ROOT / "llms.txt"
    s = path.read_text(encoding="utf-8")
    lines = "\n".join(
        f"- [{H.unescape(a['name'])} ({a['zip']})]"
        f"({SITE}/service-areas/{a['slug']}.html) – "
        + ", ".join(f.lower() for f in a["focus"])
        for a in AREA_PAGES
    )
    pattern = r"<!-- areas:start -->.*?<!-- areas:end -->"
    new = "<!-- areas:start -->\n" + lines + "\n<!-- areas:end -->"
    s, n = re.subn(pattern, lambda _m: new, s, flags=re.S)
    assert n == 1, "llms.txt area markers missing"
    path.write_text(s, encoding="utf-8")
    print(f"  llms.txt: {len(AREA_PAGES)} areas listed")


if __name__ == "__main__":
    build_sitemap()
    build_llms_areas()
    print("\nmeta files generated")
