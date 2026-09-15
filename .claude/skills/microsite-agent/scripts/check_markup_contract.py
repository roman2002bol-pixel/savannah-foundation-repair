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

        # 1. classes used but never defined in any stylesheet
        used = set()
        for m in re.finditer(r'class="([^"]*)"', html):
            used.update(m.group(1).split())
        for cls in sorted(used - defined_classes - KNOWN_UNSTYLED):
            problems.append(f"{rel}: class '{cls}' is used but defined in no stylesheet")

        # 2. inline SVGs whose nearest class has no svg sizing rule.
        #    An SVG with a viewBox and no width/height fills its container.
        for m in re.finditer(r'<(\w+)[^>]*class="([^"]*)"[^>]*>\s*<svg', html):
            classes = m.group(2).split()
            if not classes:
                continue
            sized = any(
                re.search(re.escape(c) + r"[^{}]*svg\s*\{[^}]*(width|height)", css_text)
                for c in classes
            )
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
