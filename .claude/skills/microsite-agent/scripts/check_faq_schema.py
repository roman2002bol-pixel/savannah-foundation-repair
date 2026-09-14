#!/usr/bin/env python3
"""
check_faq_schema.py — verify FAQPage JSON-LD exactly matches the visible
<details class="faq-item"><summary>...</summary><p>...</p></details>
markup on every page, in the same order.

Why this exists: Google's structured-data guidelines require FAQ schema
to match what a user actually sees on the page — a mismatch (schema
promising an answer that isn't visibly on the page, or visible text that
drifted after an edit while the JSON-LD block wasn't updated to match)
risks a manual action or the rich result simply not being granted. This
is easy to get right on day one and easy to silently break on an edit
(e.g. rewording an FAQ answer in the visible HTML but forgetting the
JSON-LD block above it, or vice versa) — run this after any FAQ edit,
before committing.

Usage (from the project root):
    python .claude/skills/microsite-agent/scripts/check_faq_schema.py

Or with an explicit root:
    python check_faq_schema.py /path/to/project

Only checks pages that actually contain a FAQPage JSON-LD block — pages
without one (e.g. the homepage, if its FAQ isn't schema'd, or legal
pages with no FAQ at all) are silently skipped, not flagged.
"""
import re
import os
import sys
import glob
import html

def find_html_files(root):
    return glob.glob(os.path.join(root, "**", "*.html"), recursive=True)

def extract_faqpage_block(content):
    """Return the raw text inside the FAQPage script's mainEntity array, or None."""
    m = re.search(r'"@type":\s*"FAQPage".*?"mainEntity":\s*\[(.*?)\]\s*\}', content, re.S)
    return m.group(1) if m else None

def unescape_json_string(s):
    # Reverse the minimal JSON string escaping used in this codebase's JSON-LD blocks
    s = s.replace('\\"', '"').replace("\\n", "\n")
    return html.unescape(s.strip())

def check(root):
    files = find_html_files(root)
    mismatches = []
    checked = 0
    for f in files:
        content = open(f, "r", encoding="utf-8").read()
        block = extract_faqpage_block(content)
        if block is None:
            continue
        checked += 1
        schema_questions = re.findall(r'"name":\s*"(.*?)",\s*\n?\s*"acceptedAnswer"', block, re.S)
        schema_questions = [unescape_json_string(q) for q in schema_questions]
        visible_questions = [unescape_json_string(q) for q in re.findall(r"<summary>(.*?)</summary>", content, re.S)]
        if schema_questions != visible_questions:
            mismatches.append((os.path.relpath(f, root), schema_questions, visible_questions))
    return checked, mismatches

def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    root = os.path.abspath(root)
    checked, mismatches = check(root)
    if mismatches:
        print(f"FAQ SCHEMA MISMATCHES ({len(mismatches)} of {checked} pages with FAQPage schema):")
        for f, schema_qs, visible_qs in mismatches:
            print(f"\n  {f}")
            print(f"    schema   ({len(schema_qs)}): {schema_qs}")
            print(f"    visible  ({len(visible_qs)}): {visible_qs}")
        sys.exit(1)
    else:
        print(f"OK — FAQ visible text matches FAQPage JSON-LD exactly on all {checked} pages that have it.")
        sys.exit(0)

if __name__ == "__main__":
    main()
