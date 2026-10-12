"""Final generator pass: advertise clean URLs, never `.html`.

The templates build links as `about.html`, `services/<slug>.html`,
`service-areas/index.html` and so on. That is fine on GitHub Pages, but on
Cloudflare -- this site's planned production host -- every `/page.html`
answers with a 307 redirect to `/page`. NEXUS shipped exactly that and Search
Console listed its extensionless twins as "not indexed" while three real pages
were unknown to Google (2026-10-12).

Rather than editing ~90 template strings, this pass runs last and rewrites
every generated page plus sitemap.xml and llms.txt:

  https://www.<domain>/x/page.html  ->  https://www.<domain>/x/page
  https://www.<domain>/index.html   ->  https://www.<domain>/
  href="page.html#anchor"           ->  href="page#anchor"
  href="index.html" / "../index.html" -> href="./" / href="../"

Asset paths are untouched (only `.html` targets change). Both GitHub Pages and
Cloudflare serve the clean form with a 200. It is idempotent: running it on
already-clean output changes nothing.

Called from build_pages.write(), build_core.patch_home_faq() and build_meta.py,
so every route that writes a file ends clean. Do not bypass it when
rebuilding. Verified by .claude/skills/microsite-agent/scripts/check_clean_urls.py.
"""
import pathlib
import re

SKIP = {".git", "node_modules", "__pycache__", ".claude"}


def _abs_pattern(domain):
    return re.compile(r"(https://(?:www\.)?" + re.escape(domain) +
                      r"/)((?:[A-Za-z0-9_-]+/)*)([A-Za-z0-9_-]+)\.html")


def _fix_href(m):
    href = m.group(1)
    if href.startswith(("http://", "https://", "tel:", "sms:", "mailto:", "#",
                        "data:", "javascript:", "//")):
        return m.group(0)
    path, sep, rest = re.match(r"([^#?]*)([#?]?)(.*)", href).groups()
    if not path.endswith(".html"):
        return m.group(0)
    if path == "index.html":
        path = "./"
    elif path.endswith("/index.html"):
        path = path[: -len("index.html")]
    else:
        path = path[: -len(".html")]
    return 'href="' + path + sep + rest + '"'


def clean_text(text, domain, html=True):
    pat = _abs_pattern(domain)
    text = pat.sub(lambda m: m.group(1) + m.group(2) +
                   ("" if m.group(3) == "index" else m.group(3)), text)
    if html:
        text = re.sub(r'href="([^"]+)"', _fix_href, text)
    return text


def apply_site(root, domain):
    root = pathlib.Path(root)
    changed = 0
    for f in root.rglob("*"):
        if not f.is_file() or SKIP & set(f.relative_to(root).parts):
            continue
        if f.suffix == ".html":
            is_html = True
        elif f.name in ("sitemap.xml", "llms.txt"):
            is_html = False
        else:
            continue
        with open(f, encoding="utf-8", newline="") as fh:
            original = fh.read()
        text = clean_text(original, domain, html=is_html)
        if text != original:
            with open(f, "w", encoding="utf-8", newline="") as fh:
                fh.write(text)
            changed += 1
    return changed


if __name__ == "__main__":
    from build_pages import ROOT, SITE
    n = apply_site(ROOT, SITE.split("://", 1)[1].removeprefix("www."))
    print(f"clean URLs: {n} files rewritten")
