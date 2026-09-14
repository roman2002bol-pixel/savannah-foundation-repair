# -*- coding: utf-8 -*-
"""
example-location-page-generator.py — a WORKED EXAMPLE, not a drop-in tool.

This is the actual script used to generate all 7 Phase-1 location pages
for the Savannah Tree Removal Co site (2026-09-08/09), lightly
genericized (brand name/domain/phone/email pulled into a CONFIG block
at the top) so it's a realistic starting point for the *next* microsite
build rather than something tied to this one project.

Why a generator script at all, instead of hand-writing each page: the
skill's own "Stack and hosting" section sanctions this explicitly — HTML
structure repeats across location pages (nav, footer, section order,
schema shape), so writing it once as a template and looping over
per-location DATA keeps that structure consistent while forcing the
actual CONTENT (the `facts` field per location) to be genuinely
different per page. The output is still plain static HTML — nothing
runs at request time, this is purely an authoring convenience.

HOW TO ADAPT THIS FOR A NEW PROJECT:
1. Do the location research FIRST (see SKILL.md "Location-page research
   workflow") — you need real facts in hand before touching this file.
2. Copy this file into the new project's scratchpad (not into the new
   project's own repo — this stays a skill reference, not project code).
3. Edit the CONFIG block below for the new brand/domain/phone/email/
   service list/favicon monogram.
4. Replace the LOCATIONS list with the new project's own researched
   locations — the shape (slug/name/zip/meta_desc/lede/facts/
   note_title/note_body/badges/faq) is the contract, keep it, change
   the *content*.
5. Copy the HEAD_TEMPLATE's nav/header/footer HTML out of one of the new
   project's already-built pages (service pages are usually built
   first) so paths and boilerplate match exactly — don't hand-retype it,
   copy-paste it to avoid transcription bugs.
6. Run it, then IMMEDIATELY run check_broken_links.py and
   check_faq_schema.py (see SKILL.md) before considering the batch done.

The LOCATIONS data below is kept as the real Savannah example (not
replaced with foo/bar placeholders) because the *level of research*
each entry represents — a real, sourced, specific fact per location,
not a template with the city name swapped — is the actual point being
demonstrated. See SKILL.md for where each of these facts came from.
"""
import os

# ---------------------------------------------------------------- CONFIG
# Edit these for the new project. Nothing below this block should need
# per-project changes except LOCATIONS and SERVICES.
BRAND_NAME = "Savannah Tree Removal Co"
DOMAIN = "savannahtreeremovalco.com"
PHONE_DISPLAY = "(912) 555-0100"
PHONE_TEL = "+19125550100"
EMAIL = "info@savannahtreeremovalco.com"
FAVICON_MONOGRAM = "STR"
FAVICON_BG = "1b4332"   # forest green, no leading #
FAVICON_FG = "d97706"   # amber, no leading #
LOGO_MARK_TEXT = "ST"   # short text-based header monogram (see SKILL.md logo section)
OUT_DIR = r"C:\path\to\new-project\service-areas"

SERVICES = [
    ("tree-removal.html", "Tree Removal", "Full removal for dead, diseased, or unwanted trees of any size, with clean cleanup after."),
    ("emergency-storm-tree-removal.html", "Emergency &amp; Storm Removal", "Fast response for trees down on your house, car, or driveway after a storm."),
    ("large-hazardous-tree-removal.html", "Large &amp; Hazardous Trees", "Controlled, rigged takedown for oversized or leaning trees near structures and power lines."),
    ("tree-trimming-pruning.html", "Trimming &amp; Pruning", "Keep limbs clear of your roof and power lines, and your canopy healthy year-round."),
    ("stump-grinding-removal.html", "Stump Grinding", "Grind old stumps flush with the yard so you can replant or landscape over them."),
]

# ---------------------------------------------------------- LOCATIONS
# Real worked example — each "facts" value is a sourced, specific claim,
# not a templated paragraph with the city name swapped. See SKILL.md's
# "Location-page research workflow" for how these were found (WebSearch
# per location BEFORE writing a word of copy).
LOCATIONS = [
    {
        "slug": "pooler-ga",
        "name": "Pooler, GA",
        "zip": "31322",
        "meta_desc": "Tree removal, trimming, and stump grinding in Pooler, GA (31322) \u2013 from new-construction lots to established yards. Free estimate.",
        "lede": "One of the fastest-growing communities in coastal Georgia \u2013 new-construction neighborhoods and older wooded lots side by side, both needing a crew who knows the difference.",
        "facts": "Pooler's population has grown roughly a third since the 2020 census, and that growth shows in the trees we see here: brand-new subdivisions with young, recently-planted trees sit next to older wooded lots being cleared for the next phase of development. Around I-95 and I-16, plenty of Pooler properties still have mature pines and oaks left standing from before development \u2013 trees that need experienced hands once they're storm-damaged, dying, or simply in the way of a new driveway or addition.",
        "note_title": "Clearing a lot before you build?",
        "note_body": "Site-clearing removal for a single lot or a small group of trees ahead of new construction is common work for us in Pooler's newer subdivisions. We coordinate around your builder's timeline and haul everything away.",
        "badges": ["New-Construction Ready", "Free Estimates", "Storm Response"],
        "faq": [
            ("Do you remove trees on a lot before new construction?",
             "Yes \u2013 site-clearing removal for a single lot or a small group of trees before a build is common work for us in Pooler's newer subdivisions. We coordinate with your timeline and haul everything away."),
            ("Do you serve all of Pooler?",
             "Yes, all of Pooler, GA (31322), from the older sections near Pine Barren Road to the newer neighborhoods off Pooler Parkway."),
            ("How much does tree removal cost in Pooler?",
             "Most jobs run a few hundred to a few thousand dollars depending on the tree's size, accessibility, and proximity to structures. We confirm a firm price after a free on-site look, not a phone guess."),
        ],
    },
    {
        "slug": "skidaway-island-the-landings",
        "name": "Skidaway Island / The Landings",
        "zip": "31411",
        "meta_desc": "Tree removal at The Landings on Skidaway Island, GA (31411) \u2013 we help navigate the Association's tree removal approval process. Free estimate.",
        "lede": "A gated golf-course community where mature live oaks are part of the landscape design \u2013 and where tree removal on developed property goes through The Landings Association first.",
        "facts": "The Landings Association has a Tree Preservation Policy for residential tree removal: any tree with a trunk circumference of 20 inches or more (measured 36 inches above ground) on a developed property needs evaluation and approval from the Association's Public Works Department before it comes down, and tree removal also falls under the community's architectural review since it counts as an exterior alteration. That's a real extra step compared to removing a tree outside an HOA \u2013 one we're used to working around.",
        "note_title": "Removing a tree at The Landings?",
        "note_body": "We help you navigate the Association's approval process \u2013 evaluation happens on Tuesday and Friday mornings \u2013 so the paperwork doesn't hold up the work longer than it has to.",
        "badges": ["HOA Process Experience", "Free Estimates", "Storm Response"],
        "faq": [
            ("Do I need approval from The Landings Association before removing a tree?",
             "Yes, for any tree with a trunk 20 inches or more in circumference (measured 36 inches up) on a developed lot \u2013 the Association's Public Works Department evaluates these on Tuesday and Friday mornings, and tree removal also falls under architectural review. We can help you through that process."),
            ("Do you serve all of Skidaway Island and The Landings?",
             "Yes, all of Skidaway Island and The Landings, GA (31411)."),
            ("How much does tree removal cost at The Landings?",
             "Most jobs run a few hundred to a few thousand dollars depending on the tree's size and accessibility \u2013 the Association's approval step can add some time to scheduling, which we'll walk you through up front. We confirm a firm price after a free on-site look."),
        ],
    },
    # ... the real build had 7 of these (Richmond Hill, Wilmington Island,
    # Georgetown, Isle of Hope, Historic District too) — trimmed to 2 here
    # to keep this reference file scannable. Same pattern for the other 5;
    # see the site's STATUS.md "Recent changes" log (2026-09-08 entry) for
    # a one-line summary of every location's distinguishing fact and its
    # source, or read the live pages directly.
]

# ------------------------------------------------------------- TEMPLATE
HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Tree Removal in __NAME__ | {brand}</title>
<meta name="description" content="__META_DESC__">
<meta property="og:type" content="website">
<meta property="og:title" content="Tree Removal in __NAME__ | {brand}">
<meta property="og:description" content="__META_DESC__">
<meta property="og:url" content="https://www.{domain}/service-areas/__SLUG__.html">
<meta property="og:site_name" content="{brand}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23{fav_bg}'/%3E%3Ctext x='32' y='43' font-family='Arial,Helvetica,sans-serif' font-weight='700' font-size='26' fill='%23{fav_fg}' text-anchor='middle'%3E{fav_mono}%3C/text%3E%3C/svg%3E">
<link rel="canonical" href="https://www.{domain}/service-areas/__SLUG__.html">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@700;800&family=Work+Sans:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="../css/style.css?v=1">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.{domain}/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Service Areas", "item": "https://www.{domain}/service-areas/index.html" }},
    {{ "@type": "ListItem", "position": 3, "name": "__NAME__" }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "Tree Removal",
  "provider": {{ "@type": "HomeAndConstructionBusiness", "name": "{brand}", "telephone": "+1-{phone_e164_no_plus}" }},
  "areaServed": {{ "@type": "Place", "name": "__NAME__" }},
  "url": "https://www.{domain}/service-areas/__SLUG__.html"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
__FAQ_JSONLD__
  ]
}}
</script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="utility-bar">
  <div class="container">
    <span>Tree removal &amp; storm cleanup across Savannah &amp; Chatham County</span>
    <a href="tel:{phone_tel}">\U0001F4DE {phone_display}</a>
  </div>
</div>

<header class="site-header">
  <div class="container nav-row">
    <a href="../index.html" class="logo">
      <span class="logo-mark">{logo_mark}</span>
      {brand}
    </a>
    <!-- copy the FULL nav block from an already-built page in this project
         instead of retyping it here — see step 5 in the module docstring -->
  </div>
</header>
<div class="nav-overlay" data-nav-overlay></div>

<main id="main">

  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / <a href="index.html">Service Areas</a> / __NAME__</div>
      <h1>Tree Removal in __NAME__</h1>
      <p class="lede muted" style="color:#cfe0d5">__LEDE__</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="../free-estimate.html">Get a Free Estimate</a>
        <a class="btn btn-ghost" href="tel:{phone_tel}">Call {phone_display}</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Local to __NAME__</span>
          <h2>ZIP __ZIP__ and the surrounding area</h2>
          <p>__FACTS__</p>
          <div class="badge-list">
            __BADGES__
          </div>
        </div>
__NOTE_BLOCK__
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">Services Here</span>
        <h2>Tree services we provide in __NAME__</h2>
      </div>
      <div class="service-grid">
__SERVICE_CARDS__
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">FAQ</span>
        <h2>Tree removal in __NAME__ \u2013 common questions</h2>
      </div>
      <div style="max-width:760px;margin-inline:auto">
__FAQ_HTML__
      </div>
    </div>
  </section>

  <section class="section-alt" id="service-area">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">Nearby Areas</span>
        <h2>We also serve these areas near __NAME__</h2>
      </div>
      <div class="area-grid">
__NEIGHBOR_CHIPS__
        <a class="area-chip" href="index.html">See all service areas <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="cta-band">
        <div>
          <h2>Have a tree that needs to come down in __NAME__?</h2>
          <p>Free estimate, straight answer on price and timing.</p>
        </div>
        <div class="hero-ctas">
          <a class="btn btn-primary" href="../free-estimate.html">Get a Free Estimate</a>
          <a class="btn btn-ghost" href="tel:{phone_tel}">Call {phone_display}</a>
        </div>
      </div>
    </div>
  </section>

</main>

<footer class="site-footer">
  <!-- copy the FULL footer block from an already-built page too, for the
       same reason as the nav above — this is illustrative, not a source
       of truth for the current footer content -->
</footer>

<script src="../js/main.js?v=1"></script>
</body>
</html>
""".format(
    brand=BRAND_NAME,
    domain=DOMAIN,
    phone_display=PHONE_DISPLAY,
    phone_tel=PHONE_TEL,
    phone_e164_no_plus=PHONE_TEL.lstrip("+"),
    fav_bg=FAVICON_BG,
    fav_fg=FAVICON_FG,
    fav_mono=FAVICON_MONOGRAM,
    logo_mark=LOGO_MARK_TEXT,
)

def esc(s):
    return s.replace('"', '\\"')

def build_faq_jsonld(faq):
    blocks = []
    for i, (q, a) in enumerate(faq):
        comma = "," if i < len(faq) - 1 else ""
        blocks.append(
            '    {\n      "@type": "Question",\n      "name": "%s",\n      "acceptedAnswer": { "@type": "Answer", "text": "%s" }\n    }%s'
            % (esc(q), esc(a), comma)
        )
    return "\n".join(blocks)

def build_faq_html(faq):
    blocks = []
    for i, (q, a) in enumerate(faq):
        open_attr = " open" if i == 0 else ""
        blocks.append(
            '        <details class="faq-item"%s>\n          <summary>%s</summary>\n          <p>%s</p>\n        </details>'
            % (open_attr, q, a)
        )
    return "\n".join(blocks)

def build_badges(badges):
    return "".join("<span>%s</span>" % b for b in badges)

def build_note_block(loc):
    title = loc["note_title"]
    body = loc["note_body"]
    if not title:
        # IMPORTANT: never fabricate a fake "special note" just to fill
        # the second column — fall back to a plain, honest quick-facts
        # box instead. See SKILL.md's non-negotiable honesty rules.
        title = "Quick facts"
        body = "ZIP %s – we cover all of %s. Free, no-obligation estimates on every job." % (loc["zip"], loc["name"])
    return (
        '        <div class="feature-card" style="align-self:start">\n'
        '          <h3 style="margin-top:0">%s</h3>\n'
        '          <p class="muted" style="margin-bottom:0">%s</p>\n'
        '        </div>\n' % (title, body)
    )

def build_service_cards():
    icons = [
        'M12 2v20M8 8l4-4 4 4M6 14l6-6 6 6',
        'M13 2 3 14h9l-1 8 10-12h-9l1-8z',
        'M12 2 4 6v6c0 5.5 3.8 9 8 10 4.2-1 8-4.5 8-10V6z',
        'M3 3h18v18H3zM3 9h18M9 21V9',
        'M12 2v20M2 12h20',
    ]
    cards = []
    for (href, name, desc), icon in zip(SERVICES, icons):
        cards.append(
            '        <div class="service-card">\n'
            '          <div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="%s"/></svg></div>\n'
            '          <h3><a href="../services/%s" style="color:inherit">%s</a></h3>\n'
            '          <p>%s</p>\n'
            '        </div>' % (icon, href, name, desc)
        )
    return "\n".join(cards)

def build_neighbor_chips(current_slug):
    others = [loc for loc in LOCATIONS if loc["slug"] != current_slug][:3]
    chips = []
    for loc in others:
        chips.append(
            '        <a class="area-chip" href="%s.html">Tree Removal in %s <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>'
            % (loc["slug"], loc["name"])
        )
    return "\n".join(chips)

SERVICE_CARDS_HTML = build_service_cards()

if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    for loc in LOCATIONS:
        page = HEAD_TEMPLATE
        page = page.replace("__NAME__", loc["name"])
        page = page.replace("__SLUG__", loc["slug"])
        page = page.replace("__META_DESC__", loc["meta_desc"])
        page = page.replace("__FAQ_JSONLD__", build_faq_jsonld(loc["faq"]))
        page = page.replace("__LEDE__", loc["lede"])
        page = page.replace("__ZIP__", loc["zip"])
        page = page.replace("__FACTS__", loc["facts"])
        page = page.replace("__BADGES__", build_badges(loc["badges"]))
        page = page.replace("__NOTE_BLOCK__", build_note_block(loc))
        page = page.replace("__SERVICE_CARDS__", SERVICE_CARDS_HTML)
        page = page.replace("__FAQ_HTML__", build_faq_html(loc["faq"]))
        page = page.replace("__NEIGHBOR_CHIPS__", build_neighbor_chips(loc["slug"]))

        out_path = os.path.join(OUT_DIR, loc["slug"] + ".html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(page)
        print("wrote", out_path)
