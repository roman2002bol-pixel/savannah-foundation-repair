#!/usr/bin/env python3
"""Location page content + generation. Run: python build_areas.py

Every `facts` block below traces to research logged in STATUS.md and links
out to the source it came from (the standing outbound-authority-link rule).
Nothing here is a template with the place name swapped -- the construction
era, foundation type, soil and the failure mode genuinely differ per area,
which is the whole reason these pages are defensible.
"""
from build_pages import (SITE, BRAND, PHONE_DISPLAY, PHONE_HREF, SERVICES,
                         head, header, footer, cta_band, breadcrumb,
                         faq_blocks, faq_schema, write)
import json

D = 1

PAGES = [
    {
        "slug": "downtown-savannah-ga",
        "photo": "downtown-savannah-home.jpg",
        "photo_alt": "Historic brick building in downtown Savannah under live oaks",
        "name": "Downtown &amp; Historic Savannah",
        "plain": "Downtown & Historic Savannah",
        "zip": "31401",
        "lede": "Brick pier foundations under houses older than the state's building codes, on ground that has been built up and built over for nearly three centuries.",
        "facts": 'Savannah\'s historic core is the hardest foundation work in the county, and the reason is age. Many houses here sit on <a href="https://en.wikipedia.org/wiki/Savannah_Historic_District_(Georgia)" target="_blank" rel="noopener">Historic District</a> pier-and-beam foundations of brick or tabby laid long before compaction standards existed – including Savannah Grey brick, which is soft, porous, and unforgiving once mortar starts washing out of the joints. Add a water table a few feet down and crawl spaces that stay humid most of the year, and you get the two failure modes we see constantly downtown: piers that have settled or lost mortar, and sill plates and joists softened by decades of moisture.',
        "note_head": "Work in the Historic District has an extra step",
        "note": 'Exterior work on a contributing structure in the Historic District generally goes through the city\'s review process before it starts. Foundation and pier work that changes anything visible from the street can fall under that, so the timeline needs to account for it. The <a href="https://www.savannahga.gov/" target="_blank" rel="noopener">City of Savannah</a> is the authority on what applies to a specific address, and confirming it early beats discovering it mid-job.',
        "focus": ["Settled and cracked masonry piers", "Rotted sill plates and joist ends", "Crawl space moisture in tight, low clearances"],
        "faqs": [
            ("Do you work on historic homes downtown?",
             "Yes, and they need a different approach than a 1990s slab house. Soft historic brick, original framing, and plaster finishes all limit how fast a structure can be lifted, so recovery is staged more gradually and the target elevation is set from what the building will actually tolerate."),
            ("Does foundation work downtown need approval first?",
             "It can. Exterior work on a contributing structure in the Historic District generally goes through the city's review process, and foundation or pier work visible from the street can fall under it. Check with the City of Savannah for your specific address before scheduling – we'll flag it at the inspection if it looks likely."),
            ("Do you serve all of downtown Savannah?",
             "Yes, all of the 31401 ZIP – the Historic District, the Victorian District, and the surrounding downtown blocks."),
        ],
    },
    {
        "slug": "pooler-ga",
        "photo": "pooler-new-home.jpg",
        "photo_alt": "Newer two-storey home with a concrete driveway, typical of Pooler subdivisions",
        "name": "Pooler, GA",
        "plain": "Pooler, GA",
        "zip": "31322",
        "lede": "One of Georgia's fastest-growing cities, and almost all of it built recently on ground that used to be farm and forest.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Pooler,_Georgia" target="_blank" rel="noopener">Pooler</a> has grown faster than almost anywhere in the state, and nearly all of that growth is new subdivisions along the I-16 and I-95 corridors built on land that was agricultural or wooded a decade or two ago. That matters structurally: a new-construction lot is usually graded and filled before the slab is poured, and fill that was not compacted properly settles under load afterward. It shows up first in the flatwork – a driveway or garage apron dropping at one edge – and sometimes later in the slab itself. Pooler is mostly a slab-on-grade market rather than a crawl space one, which changes which repairs apply.',
        "note_head": "Newer house, still settling",
        "note": "A five-year-old home with a cracked, dropping driveway is not a defective house – it is fill soil finishing its settlement. Lifting the slab and correcting the drainage that is washing fines out from under it usually resolves it for good, and it is a much smaller job than owners fear when they first see the crack.",
        "focus": ["Sunken driveways, aprons, and patios on newer lots", "Slab cracking over poorly compacted fill", "Drainage washing soil out from under flatwork"],
        "faqs": [
            ("My house is nearly new – why is the concrete already sinking?",
             "Because the concrete is sitting on fill, not on undisturbed ground. Most new Pooler lots are graded and filled before building, and if that fill wasn't compacted to spec it keeps consolidating under load for years afterward. It's the single most common thing we see out here, and slab lifting handles it without replacing the concrete."),
            ("Do Pooler homes have crawl spaces?",
             "Mostly not. The newer subdivisions here are predominantly slab-on-grade, so the work is usually slab levelling, crack repair, and occasionally piering rather than the crawl space stabilisation that dominates closer to the water."),
            ("Do you serve all of Pooler?",
             "Yes, all of Pooler, GA (31322), including the newer neighbourhoods off Pooler Parkway and the older sections toward Pine Barren Road."),
        ],
    },
    {
        "slug": "richmond-hill-ga",
        "photo": "richmond-hill-home.jpg",
        "photo_alt": "Brick family home of the kind built across Richmond Hill's newer neighbourhoods",
        "name": "Richmond Hill, GA",
        "plain": "Richmond Hill, GA",
        "zip": "31324",
        "lede": "Bryan County, not Chatham – sandy loam over clay, the Ogeechee River on the eastern edge, and a building boom that has not slowed down.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Richmond_Hill,_Georgia" target="_blank" rel="noopener">Richmond Hill</a> sits in Bryan County rather than Chatham, southwest of Savannah with the Ogeechee River forming its eastern boundary. The soil here is coastal-plain sandy loam over clay layers, with the same high water table as the rest of the region – a profile that drains fast at the surface and holds water below. The county has been growing hard, and a great deal of the housing stock is recent construction on newly developed ground, which brings the same fill-settlement pattern seen in Pooler. Closer to the river, older properties add moisture exposure on top of it.',
        "note_head": "Different county, same coastal-plain soil",
        "note": "Being in Bryan County changes the permitting authority, not the engineering. The sandy-loam-over-clay profile and the shallow water table behave the same way here as in Chatham, so the repairs are the same ones – it is worth stating plainly because the county line confuses people looking for a local contractor.",
        "focus": ["Fill settlement under newer construction", "Slab and flatwork levelling", "Crawl space moisture on older riverside properties"],
        "faqs": [
            ("You're a Savannah company – do you actually come to Richmond Hill?",
             "Yes. Richmond Hill is in Bryan County rather than Chatham, but it is part of the same metro and the same drive, and the soil conditions are effectively identical. It is a regular part of our service area, not an outlying exception."),
            ("Is the soil here different from Savannah proper?",
             "Not meaningfully. It's the same coastal-plain profile – sandy loam over clay layers with a high water table. What differs is the housing stock: a lot of Richmond Hill is recent construction on newly developed ground, so fill settlement is proportionally more of what we see."),
            ("Do you serve all of Richmond Hill?",
             "Yes, all of Richmond Hill, GA (31324), including the newer master-planned communities and the older neighbourhoods nearer the Ogeechee River."),
        ],
    },
    {
        "slug": "skidaway-island-ga",
        "photo": "skidaway-marsh.jpg",
        "photo_alt": "Tidal marsh and creeks surrounding Skidaway Island at sunset",
        "name": "Skidaway Island",
        "plain": "Skidaway Island",
        "zip": "31411",
        "lede": "A private island community whose oldest homes are now past fifty, built among tidal marsh and maritime forest.",
        "facts": 'The first homes at <a href="https://en.wikipedia.org/wiki/Skidaway_Island,_Georgia" target="_blank" rel="noopener">The Landings on Skidaway Island</a> went up in 1972, once the two bridges connecting the island to the mainland were finished, and the bulk of the community was built out between then and the late 1990s. That puts a large share of the housing stock in the window where original framing, original crawl spaces and original support posts are all reaching the age where coastal humidity has had time to do real damage. The island is surrounded by tidal marsh and estuary, so the moisture load under these houses is relentless even well back from the water.',
        "note_head": "The Landings Association reviews exterior work",
        "note": 'Tree removal at The Landings already goes through the Association, and exterior alterations generally fall under its architectural review as well. Foundation work that changes anything visible – exterior piers, grading, drainage runs – is worth confirming with <a href="https://landings.org/" target="_blank" rel="noopener">The Landings Association</a> before scheduling. Gate access for crews and equipment needs arranging in advance too.',
        "focus": ["Fifty-year-old crawl space framing and support posts", "Persistent humidity from surrounding tidal marsh", "Coordinating work inside a gated community"],
        "faqs": [
            ("Do you need approval from the Association for foundation work?",
             "Often, yes, where the work changes something visible from outside – exterior piers, grading, or drainage. The Landings Association's architectural review covers exterior alterations, so confirming with them before scheduling avoids a stoppage mid-job. We'll raise it at the inspection if it looks like it applies."),
            ("Why do homes here have so much crawl space moisture?",
             "The island is ringed by tidal marsh and estuary, so the ground and the air under these houses stay humid year-round, not just in summer. Combine that with a housing stock largely built between the 1970s and 1990s, and you get framing that has been in a damp environment for decades."),
            ("Do you serve all of Skidaway Island?",
             "Yes, all of Skidaway Island and The Landings (31411). Gate access for our crew is arranged ahead of the visit."),
        ],
    },
    {
        "slug": "wilmington-island-ga",
        "photo": "wilmington-island-marsh.jpg",
        "photo_alt": "Coastal marshland of the kind that surrounds Wilmington Island",
        "name": "Wilmington Island",
        "plain": "Wilmington Island",
        "zip": "31410",
        "lede": "Sixties and seventies ranch houses on pier-and-beam foundations, between the Wilmington River and the marsh – the toughest moisture conditions in the county.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Wilmington_Island,_Georgia" target="_blank" rel="noopener">Wilmington Island</a> is characteristically sprawling ranch homes from the 1960s and 70s, a great many of them on pier-and-beam foundations suited to the low-lying ground. The groundwater table here is extremely shallow, so even an ordinary rain event can put water into a crawl space, and high-tide flooding reaches some streets through ageing stormwater infrastructure. Salt is the extra factor most inland contractors underestimate: it corrodes metal fasteners, connectors and hardware, and it stays in building materials afterward, drawing moisture back in long after the water has gone.',
        "note_head": "Why galvanised hardware is not optional here",
        "note": "On the islands, anything steel that is permanently in the ground or in the crawl space gets galvanised protection as standard. Salt-laden air and repeated wetting will find untreated hardware, and a support jack that corrodes at the base has quietly stopped doing its job years before anyone notices the floor moving again.",
        "focus": ["Pier-and-beam settling on low-lying lots", "Rotted framing from repeated crawl space wetting", "Salt corrosion of fasteners, connectors, and support hardware"],
        "faqs": [
            ("Water gets into my crawl space after heavy rain – is that normal here?",
             "It's common on the island because the groundwater table is very shallow, but common isn't the same as acceptable. Repeated wetting is what rots joists and girders, so the fix is drainage and encapsulation rather than living with it. What's not normal is water that stays for days, which points to a drainage problem worth solving first."),
            ("Does salt air really affect a foundation?",
             "Yes, specifically the metal in it. Salt corrodes fasteners, connectors, and support hardware, and it stays in materials after the water dries, pulling moisture back in. That's why galvanised hardware is standard for us out here rather than an upgrade option."),
            ("Do you serve all of Wilmington Island?",
             "Yes, all of Wilmington Island (31410), including the neighbouring Whitemarsh Island and Talahi Island areas."),
        ],
    },
    {
        "slug": "georgetown-ga",
        "photo": "georgetown-ranch-home.jpg",
        "photo_alt": "Single-storey ranch home typical of Georgetown's 1970s and 1980s build-out",
        "name": "Georgetown",
        "plain": "Georgetown",
        "zip": "31419",
        "lede": "A large seventies and eighties suburb southwest of the city, across the Little Ogeechee – now at the age where original foundations start showing their history.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Georgetown,_Chatham_County,_Georgia" target="_blank" rel="noopener">Georgetown</a> sits about fourteen miles southwest of downtown Savannah, across the Little Ogeechee River, and was built out mostly through the 1970s and 1980s with brick ranch homes and Lowcountry cottages, plus newer phases since. That build era is the useful detail: these houses are now forty to fifty years old, which is exactly when original crawl space framing, support posts, and driveway slabs reach the end of their first service life in this climate. The failures here are less dramatic than on the islands and more a matter of accumulated age.',
        "note_head": "A mixed-age neighbourhood means mixed repairs",
        "note": "Because Georgetown was built in phases over several decades, two houses a few streets apart can need entirely different work – one a crawl space with tired framing, the next a newer slab with settled flatwork. It is the main reason we do not quote this neighbourhood over the phone.",
        "focus": ["Ageing crawl space framing and support posts", "Settled driveways and walkways", "Original-era piers reaching end of service life"],
        "faqs": [
            ("My house is from the eighties – is foundation work expected by now?",
             "Not inevitable, but it's the age where original support framing and flatwork in this climate commonly need attention for the first time. Forty-odd years of Georgia coastal humidity under a crawl space adds up, and catching it at the tired stage costs considerably less than catching it at the failed stage."),
            ("Is Georgetown in the city of Savannah?",
             "It's an unincorporated community in Chatham County, just across the Little Ogeechee River from the city limits, about fourteen miles southwest of downtown. It's well inside our normal service area either way."),
            ("Do you serve all of Georgetown?",
             "Yes, all of Georgetown (31419), from the original 1970s sections through to the newer phases."),
        ],
    },
]


def build(page):
    url = f"{SITE}/service-areas/{page['slug']}.html"
    title = f"Foundation Repair in {page['plain']} | {BRAND}"
    desc = (f"Foundation repair and crawl space work in {page['plain']} "
            f"({page['zip']}) – {page['focus'][0].lower()}. Free structural inspection.")
    schemas = [
        breadcrumb([("Home", f"{SITE}/"),
                    ("Service Areas", f"{SITE}/service-areas/index.html"),
                    (page["plain"], None)]),
        json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": "Foundation Repair",
            "provider": {"@type": "HomeAndConstructionBusiness", "name": BRAND,
                         "telephone": "+1-912-555-0142"},
            "areaServed": {"@type": "Place", "name": page["plain"]},
            "url": url,
        }, indent=2, ensure_ascii=False),
        faq_schema(page["faqs"]),
    ]

    focus = "\n".join(
        f'            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>{f}</li>'
        for f in page["focus"]
    )
    svc_cards = "\n".join(f'''        <div class="service-card">
          <h3><a href="../services/{slug}.html" style="color:inherit">{name}</a></h3>
          <a class="link" href="../services/{slug}.html">See details →</a>
        </div>''' for slug, name in SERVICES)

    others = [a for a in PAGES if a["slug"] != page["slug"]][:3]
    nearby = "\n".join(
        f'        <a class="area-chip" href="{o["slug"]}.html">{o["name"]} '
        f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>'
        for o in others
    )

    body = f'''
  <section class="page-hero" style="background-image:linear-gradient(180deg, rgba(11,26,41,.58), rgba(11,26,41,.82)), url(&quot;../images/{page["photo"]}&quot;)">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / <a href="index.html">Service Areas</a> / {page["name"]}</div>
      <h1>Foundation Repair in {page["name"]}</h1>
      <p class="lede">{page["lede"]}</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="../free-inspection.html">Get a Free Inspection</a>
        <a class="btn btn-ghost" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Local to {page["name"]}</span>
          <h2>ZIP {page["zip"]} and the surrounding area</h2>
          <p>{page["facts"]}</p>
          <div class="badge-list">
            <span>Free Inspections</span><span>Written Scope</span><span>ZIP {page["zip"]}</span>
          </div>
          <div class="img-slot" style="--ar:16/9; margin-top:1.5rem">
            <img src="../images/{page["photo"]}" alt="{page["photo_alt"]}" loading="lazy">
            <span class="img-slot-label">{page["plain"]}</span>
          </div>
        </div>
        <div class="local-callout">
          <h3 style="margin-top:0">{page["note_head"]}</h3>
          <p>{page["note"]}</p>
          <ul class="package-list" style="margin-bottom:0">
{focus}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">Services Here</span>
        <h2>What we handle in {page["name"]}</h2>
      </div>
      <div class="service-grid">
{svc_cards}
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">FAQ</span>
        <h2>Foundation repair in {page["name"]} – common questions</h2>
      </div>
{faq_blocks(page["faqs"])}
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Nearby</span>
        <h2>We also work in these areas</h2>
      </div>
      <div class="area-grid">
{nearby}
        <a class="area-chip" href="index.html">All service areas <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>
      </div>
    </div>
  </section>
{cta_band(D, f"Something moving at your place in {page['name']}?", "Free inspection, real measurements, and a straight answer on whether it needs work now.")}'''

    return (head(D, title, desc, url, schemas)
            + header(D) + body + footer(D))


def build_hub():
    url = f"{SITE}/service-areas/index.html"
    cards = "\n".join(f'''        <div class="service-card">
          <div class="img-slot" style="--ar:16/9">
            <img src="../images/{a["photo"]}" alt="{a["photo_alt"]}" loading="lazy">
            <span class="img-slot-label">{a["plain"]}</span>
          </div>
          <h3><a href="{a["slug"]}.html" style="color:inherit">{a["name"]}</a></h3>
          <p>{a["lede"]}</p>
          <a class="link" href="{a["slug"]}.html">Foundation repair in {a["name"]} →</a>
        </div>''' for a in PAGES)

    schemas = [breadcrumb([("Home", f"{SITE}/"), ("Service Areas", None)])]
    body = f'''
  <section class="page-hero" style="background-image:linear-gradient(180deg, rgba(11,26,41,.58), rgba(11,26,41,.82)), url(&quot;../images/skidaway-marsh.jpg&quot;)">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / Service Areas</div>
      <h1>Service Areas – Savannah &amp; Chatham County</h1>
      <p class="lede">Six areas, six genuinely different sets of foundation problems. Historic piers downtown, fill settlement out west, salt and shallow groundwater on the islands.</p>
      <div class="hero-ctas">
        <a class="btn btn-primary" href="../free-inspection.html">Get a Free Inspection</a>
        <a class="btn btn-ghost" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Where We Work</span>
        <h2>Pick your area</h2>
        <p class="muted">Each page covers what actually fails in that specific area and why – the construction era, the soil, and the moisture conditions are not the same across the county.</p>
      </div>
      <div class="service-grid">
{cards}
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Not Listed?</span>
          <h2>We cover more of the county than we have pages for</h2>
          <p>These six are the areas we work in most often and know best, so they're the ones we've written up properly rather than listing every place name in the county to look bigger.</p>
          <p>If you're elsewhere in Chatham County or the surrounding area – Thunderbolt, Garden City, Isle of Hope, Tybee, Bloomingdale – call and ask. The answer is usually yes.</p>
        </div>
        <div class="feature-card">
          <h3 style="margin-top:0">Check your address</h3>
          <p class="muted">Quickest way to find out is to ask. No obligation, and we'll say so plainly if you're outside what we cover.</p>
          <p><a class="btn btn-primary btn-block" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a></p>
          <p style="margin-bottom:0"><a class="btn btn-outline btn-block" href="../contact.html">Send a message</a></p>
        </div>
      </div>
    </div>
  </section>
{cta_band(D, "Ready for a look at it?", "Free structural inspection anywhere in our service area, with measurements and a written scope.")}'''

    return (head(D, f"Service Areas | Foundation Repair Across Savannah &amp; Chatham County",
                 "Foundation repair and crawl space services across Savannah, Pooler, Richmond Hill, Skidaway Island, Wilmington Island, and Georgetown, GA.",
                 url, schemas)
            + header(D) + body + footer(D))


if __name__ == "__main__":
    for pg in PAGES:
        write(f"service-areas/{pg['slug']}.html", build(pg))
    write("service-areas/index.html", build_hub())
    print(f"\n{len(PAGES)} location pages + hub generated")
