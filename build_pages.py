#!/usr/bin/env python3
"""One-off generator for Savannah Foundation Repair Co pages.

Per the microsite-agent skill: structure (nav, footer, schema shape, section
order) is generated so it can't drift between pages, while every piece of
CONTENT is a required, visibly-different input per page -- so nothing can be
silently copy-pasted.

FAQ questions/answers are written ONCE per page and used to render both the
visible <details> markup and the FAQPage JSON-LD, which makes the two
physically unable to disagree (check_faq_schema.py still verifies).

Run from the project root:  python build_pages.py
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://www.savannahfoundationrepairco.com"
BRAND = "Savannah Foundation Repair Co"
PHONE_DISPLAY = "(912) 555-0142"
PHONE_HREF = "+19125550142"
EMAIL = "info@savannahfoundationrepairco.com"
ASSET_V = "5"

SERVICES = [
    ("crawl-space-repair", "Crawl Space Repair"),
    ("foundation-piering", "Foundation Piering"),
    ("concrete-slab-leveling", "Concrete Slab Leveling"),
    ("foundation-crack-repair", "Foundation Crack Repair"),
    ("crawl-space-encapsulation", "Crawl Space Encapsulation"),
]

AREAS = [
    ("downtown-savannah-ga", "Downtown &amp; Historic Savannah", "Downtown & Historic Savannah"),
    ("midtown-savannah-ga", "Midtown Savannah &amp; Ardsley Park", "Midtown Savannah & Ardsley Park"),
    ("southside-savannah-ga", "Southside Savannah", "Southside Savannah"),
    ("georgetown-ga", "Georgetown", "Georgetown"),
    ("isle-of-hope-ga", "Isle of Hope", "Isle of Hope"),
    ("thunderbolt-ga", "Thunderbolt", "Thunderbolt"),
    ("whitemarsh-island-ga", "Whitemarsh Island", "Whitemarsh Island"),
    ("wilmington-island-ga", "Wilmington Island", "Wilmington Island"),
    ("skidaway-island-ga", "Skidaway Island", "Skidaway Island"),
    ("tybee-island-ga", "Tybee Island", "Tybee Island"),
    ("garden-city-ga", "Garden City", "Garden City"),
    ("port-wentworth-ga", "Port Wentworth", "Port Wentworth"),
    ("pooler-ga", "Pooler, GA", "Pooler, GA"),
    ("bloomingdale-ga", "Bloomingdale", "Bloomingdale"),
    ("richmond-hill-ga", "Richmond Hill, GA", "Richmond Hill, GA"),
    ("rincon-ga", "Rincon", "Rincon"),
    ("springfield-ga", "Springfield", "Springfield"),
    ("hinesville-ga", "Hinesville", "Hinesville"),
]


def p(depth, path):
    """Relative path from a page at `depth` directories deep."""
    return ("../" * depth) + path


def faq_blocks(faqs):
    """Render visible FAQ markup. Same source as the JSON-LD below."""
    out = []
    for q, a in faqs:
        out.append(
            f'      <details class="faq-item">\n'
            f'        <summary>{q}</summary>\n'
            f'        <p>{a}</p>\n'
            f'      </details>'
        )
    return "\n".join(out)


def faq_schema(faqs):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": html.unescape(q),
             "acceptedAnswer": {"@type": "Answer", "text": html.unescape(a)}}
            for q, a in faqs
        ],
    }, indent=2, ensure_ascii=False)


def head(depth, title, desc, canonical, schemas):
    blocks = "\n".join(
        f'<script type="application/ld+json">\n{s}\n</script>' for s in schemas
    )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="{BRAND}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%2314293f'/%3E%3Ctext x='32' y='43' font-family='Arial,Helvetica,sans-serif' font-weight='700' font-size='26' fill='%23e05a00' text-anchor='middle'%3ESFR%3C/text%3E%3C/svg%3E">
<link rel="canonical" href="{canonical}">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="{p(depth, 'css/style.css')}?v={ASSET_V}">
{blocks}
</head>'''


def header(depth):
    sub = "\n".join(
        f'            <li><a href="{p(depth, "services/" + slug + ".html")}">{name}</a></li>'
        for slug, name in SERVICES
    )
    return f'''<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="utility-bar">
  <div class="container">
    <span>Free structural inspections across Savannah &amp; Chatham County</span>
    <a href="tel:{PHONE_HREF}">📞 {PHONE_DISPLAY}</a>
  </div>
</div>

<header class="site-header">
  <div class="container nav-row">
    <a href="{p(depth, 'index.html')}" class="logo">
      <img class="logo-img" src="{p(depth, 'images/logo.svg')}" alt="{BRAND}" width="38" height="38">
      {BRAND}
    </a>
    <nav class="main-nav" data-nav aria-label="Primary">
      <button class="nav-close" type="button" data-nav-close aria-label="Close menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
      <ul class="nav-list">
        <li><a href="{p(depth, 'index.html')}">Home</a></li>
        <li class="nav-group">
          <span class="nav-group-label">Services <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 9l6 6 6-6"/></svg></span>
          <ul class="nav-sub">
{sub}
          </ul>
        </li>
        <li><a href="{p(depth, 'service-areas/index.html')}">Service Areas</a></li>
        <li><a href="{p(depth, 'about.html')}">About</a></li>
        <li><a href="{p(depth, 'faq.html')}">FAQ</a></li>
        <li><a href="{p(depth, 'contact.html')}">Contact</a></li>
      </ul>
      <div class="nav-cta">
        <a class="btn btn-outline btn-block" href="sms:{PHONE_HREF}">Text Us</a>
        <a class="btn btn-primary btn-block" href="{p(depth, 'free-inspection.html')}">Free Inspection</a>
      </div>
    </nav>
    <div class="nav-actions">
      <a class="btn btn-outline btn-sm" href="tel:{PHONE_HREF}">Call Now</a>
      <button class="nav-toggle" type="button" data-nav-toggle aria-label="Open menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
      </button>
    </div>
  </div>
</header>
<div class="nav-overlay" data-nav-overlay></div>

<main id="main">
'''


def footer(depth):
    svc = "\n".join(
        f'        <a href="{p(depth, "services/" + slug + ".html")}">{name}</a>'
        for slug, name in SERVICES
    )
    ar = "\n".join(
        f'        <a href="{p(depth, "service-areas/" + slug + ".html")}">{label}</a>'
        for slug, label, _ in AREAS[:6]
    )
    return f'''
</main>

<footer class="site-footer">
  <div class="container">
    <div>
      <div class="footer-logo">
        <img class="logo-img" src="{p(depth, 'images/logo.svg')}" alt="{BRAND}" width="38" height="38">
        {BRAND}
      </div>
      <p class="muted">Foundation repair, crawl space stabilization, piering, slab leveling, and encapsulation for homes across Savannah and Chatham County, Georgia. Free structural inspections, written scope before any work starts.</p>
      <div class="badge-list">
        <span>Free Inspections</span><span>Written Scope</span><span>Locally Focused</span>
      </div>
    </div>
    <div>
      <h4>Services</h4>
      <div class="footer-links">
{svc}
      </div>
    </div>
    <div>
      <h4>Service Areas</h4>
      <div class="footer-links">
{ar}
        <a href="{p(depth, 'service-areas/index.html')}">All areas</a>
      </div>
    </div>
    <div>
      <h4>Get In Touch</h4>
      <div class="footer-links">
        <a href="tel:{PHONE_HREF}">📞 {PHONE_DISPLAY}</a>
        <a href="sms:{PHONE_HREF}">💬 Text Us</a>
        <a href="mailto:{EMAIL}">✉️ {EMAIL}</a>
        <a href="{p(depth, 'faq.html')}">FAQ</a>
        <a href="{p(depth, 'privacy-policy.html')}">Privacy Policy</a>
        <a href="{p(depth, 'terms.html')}">Terms of Service</a>
      </div>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span data-year></span> {BRAND}. All rights reserved.</span>
    <span>Serving Savannah &amp; Chatham County, GA</span>
  </div>
</footer>

<div class="mobile-action-bar">
  <a href="tel:{PHONE_HREF}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.34 1.79.65 2.65a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.43-1.27a2 2 0 0 1 2.11-.45c.86.31 1.75.53 2.65.65A2 2 0 0 1 22 16.92z"/></svg>Call</a>
  <a href="sms:{PHONE_HREF}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/></svg>Text</a>
  <a href="{p(depth, 'free-inspection.html')}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 2v4M16 2v4M3 10h18M5 4h14a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Z"/></svg>Free Inspection</a>
</div>

<script src="{p(depth, 'js/main.js')}?v={ASSET_V}"></script>
</body>
</html>
'''


def cta_band(depth, heading, blurb):
    return f'''
  <section>
    <div class="container">
      <div class="cta-band">
        <div>
          <h2>{heading}</h2>
          <p>{blurb}</p>
        </div>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="{p(depth, 'free-inspection.html')}">Get a Free Inspection</a>
          <a class="btn btn-ghost" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a>
        </div>
      </div>
    </div>
  </section>
'''


def breadcrumb(items):
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            ({"@type": "ListItem", "position": i + 1, "name": name, "item": url}
             if url else {"@type": "ListItem", "position": i + 1, "name": name})
            for i, (name, url) in enumerate(items)
        ],
    }, indent=2, ensure_ascii=False)


def write(relpath, content):
    out = ROOT / relpath
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print("wrote", relpath)
