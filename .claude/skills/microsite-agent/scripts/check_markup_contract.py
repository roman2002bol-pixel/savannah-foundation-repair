#!/usr/bin/env python3
"""Check that the HTML only uses CSS classes and JS hooks that actually exist.

Why this exists
---------------
On the Savannah Foundation Repair build (2026-09-15) a homepage was written
from memory of "what the markup usually looks like" instead of from the
project's real stylesheet. Twelve of the class names did not exist in
css/style.css at all. Because CSS silently ignores selectors it has no rule
for, nothing errored -- the page just rendered wrong in ways that each
looked like a separate mystery bug:

  * .link-arrow undefined  -> the inline SVG inside it had no size rule, so
                              it rendered at full container width: one
                              enormous arrow filling an entire card.
  * .check-list undefined  -> a <ul> inherited .feature-card's
                              text-align:center and became centred bullets.
  * .footer-grid undefined -> footer columns never laid out and the links
                              kept the global dark link colour on the dark
                              footer: invisible text.
  * data-booking-form      -> main.js listens for [data-quote-form], so the
                              submit handler never bound and the button was
                              simply dead.

Every one of those is invisible to a broken-link check and to a FAQ-schema
check. This script closes that gap: it is a contract test between the markup
and the assets it depends on.

Usage:  python check_markup_contract.py [project_root]
Exit 0 = clean, exit 1 = problems found.
"""
import pathlib
import re
import sys

# Classes that are styled by a parent/descendant selector, set from JS, or
# intentionally unstyled hooks. Add here only with a reason.
KNOWN_UNSTYLED = {
    "is-open",      # toggled by main.js
    "is-empty",     # toggled by main.js image fallback
    "is-visible",   # toggled by main.js form status
    "ok", "err",    # form-status state modifiers
    "cols-2",       # .form-grid.cols-2 compound selector
    "center",       # .section-head.center compound selector
    "chevron",
    "icon",
    "item",
    "link",
    "img-slot-label",
}


def main(root_arg: str) -> int:
    root = pathlib.Path(root_arg).resolve()
    css_files = [p for p in root.rglob("*.css") if ".claude" not in p.parts]
    js_files = [p for p in root.rglob("*.js") if ".claude" not in p.parts]
    html_files = sorted(p for p in root.rglob("*.html") if ".claude" not in p.parts)

    if not html_files:
        print(f"No HTML files found under {root}")
        return 1

    css_text = "\n".join(p.read_text(encoding="utf-8") for p in css_files)
    js_text = "\n".join(p.read_text(encoding="utf-8") for p in js_files)

    defined_classes = set(re.findall(r"\.([a-zA-Z][\w-]*)", css_text))
    # data-* attributes the JS actually queries for
    js_hooks = set(re.findall(r'\[(data-[\w-]+)\]', js_text))

    problems = []

    for path in html_files:
        rel = path.relative_to(root)
        html = path.read_text(encoding="utf-8")

        # 1. classes used but never defined in any stylesheet.
        #    An element the browser is already told to hide inline needs no
        #    rule -- Web3Forms' honeypot ships as
        #    `class="hidden" style="display:none"`, which is not a bug.
        used = set()
        for m in re.finditer(r'<[^>]*class="([^"]*)"[^>]*>', html):
            tag = m.group(0)
            if re.search(r'style="[^"]*display\s*:\s*none', tag):
                continue
            used.update(m.group(1).split())
        for cls in sorted(used - defined_classes - KNOWN_UNSTYLED):
            problems.append(f"{rel}: class '{cls}' is used but defined in no stylesheet")

        # 2. inline SVGs with no effective sizing.
        #    An SVG with a viewBox and no width/height fills its container.
        #    Three things can size it, and all three count:
        #      a) its own width/height attributes
        #      b) a rule on a class the <svg> itself carries
        #      c) an `<ancestor-class> svg {width|height}` rule
        #    Missing (a) and (b) is how this check used to report a sized icon
        #    as broken -- a checker that cries wolf stops being read.
        for m in re.finditer(r'<(\w+)[^>]*class="([^"]*)"[^>]*>\s*(<svg[^>]*>)', html):
            classes, svg_tag = m.group(2).split(), m.group(3)
            if not classes:
                continue
            if re.search(r'\swidth\s*=', svg_tag) and re.search(r'\sheight\s*=', svg_tag):
                continue                                              # (a)
            own = re.search(r'class="([^"]*)"', svg_tag)
            candidates = classes + (own.group(1).split() if own else [])
            sized = any(
                re.search(re.escape(c) + r"[^{}]*svg\s*\{[^}]*(width|height)", css_text)
                or re.search(r"\." + re.escape(c) + r"\s*\{[^}]*(width|height)", css_text)
                for c in candidates
            )                                                         # (b) and (c)
            if not sized:
                problems.append(
                    f"{rel}: <svg> directly inside .{'.'.join(classes)} -- no "
                    f"'svg{{width/height}}' rule matches it, so it will render "
                    f"at full container width"
                )

        # 3. data-* hooks in HTML that no JS listens for, and vice versa
        html_hooks = set(re.findall(r'\b(data-[\w-]+)(?==|[\s>])', html))
        # only care about behavioural hooks, i.e. ones some JS file uses a
        # sibling of; skip pure-data attributes like data-year if unused
        for hook in sorted(html_hooks):
            if hook.startswith("data-") and hook not in js_hooks:
                if hook in {"data-endpoint-ready", "data-year"}:
                    continue  # read via getAttribute / used by name elsewhere
                problems.append(
                    f"{rel}: attribute [{hook}] is in the markup but no JS "
                    f"queries it -- dead hook (did the name drift?)"
                )

    if problems:
        print(f"MARKUP CONTRACT PROBLEMS ({len(problems)}):")
        for p in problems:
            print("  " + p)
        return 1

    print(
        f"OK - every class resolves to a stylesheet rule, every inline SVG is "
        f"sized, and every JS hook is bound, across {len(html_files)} HTML "
        f"files under {root}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
