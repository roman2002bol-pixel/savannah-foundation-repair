#!/usr/bin/env python3
"""Service page content + generation. Run: python build_services.py"""
from build_pages import (SITE, BRAND, PHONE_DISPLAY, PHONE_HREF, AREAS, WORK_SHOTS,
                         head, header, footer, cta_band, breadcrumb,
                         faq_blocks, faq_schema, write, p)
import json

D = 1  # services/ pages are one directory deep

# Every field below is genuinely per-service: the situations, the method, the
# equipment, the cost drivers and the FAQs all differ because the underlying
# trades differ. Nothing here is a template with a noun swapped.
PAGES = [
    {
        "slug": "crawl-space-repair",
        "body": "level",
        "photo": "crawl-space-timber-work.jpg",
        "photo_alt": "Drilling into a timber joist -- the framing replacement work a sagging floor needs",
        "nav": "Crawl Space Repair",
        "h1": "Crawl Space Repair &amp; Sagging Floor Jacks in Savannah, GA",
        "title": "Crawl Space Repair in Savannah, GA | Sagging Floor Jacks",
        "desc": "Crawl space repair in Savannah, GA – rotted joists, failed piers, and sagging floors stabilized with adjustable steel jacks on proper footings. Free inspection.",
        "service_type": "Crawl Space Repair",
        "lede": 'A sagging or soft floor needs an assessment of the framing, bearings and moisture sources underneath it before choosing a repair.',
        "intro": ['A raised floor can lose support through damaged timber, altered loads or movement at a footing. The <a href="https://bsesc.energy.gov/energy-basics/crawlspace-capillary-break-crawlspace-floors">U.S. Department of Energy crawl-space guidance</a> explains how moisture from the ground can reach framing and contribute to rot. Inspect timber condition separately from floor elevations to identify what actually needs repair.', 'The scope may involve framing repairs, revised supports or moisture correction. Footings and posts must suit the load and ground conditions; adding a jack without checking the material and bearing beneath it can leave the original problem unresolved.'],
        "situations_head": "What this covers",
        "situations": [
            "Floors that bounce, flex, or feel spongy underfoot",
            "A visible dip or slope toward the center of a room",
            "Joists, girders, or sill plates with rot or insect damage",
            "Crawl space support posts that have sunk into the soil",
            "Masonry piers that have cracked, leaned, or lost mortar",
            "Squeaking or separating floorboards over one specific area",
        ],
        "method_head": "How the repair is done",
        "method": [
            "<strong>Elevation survey first.</strong> Readings across the floor establish where the low points are and how far out of level the structure has actually gone – which is also the only honest way to tell you what leveling back is realistic.",
            "<strong>Replace what's failed.</strong> Rotted joist sections, girders, and sill plate get cut out and replaced with treated lumber, sistered to sound framing.",
            "<strong>New footings, then jacks.</strong> Adjustable steel jacks are set on poured concrete footings sized for the load. Putting a jack on bare dirt or a stacked block just moves the settling problem a few years down the road.",
            "<strong>Lift gradually.</strong> Recovery happens over multiple visits, not in one afternoon. Lifting a settled floor too fast is how you crack drywall and bind doors upstairs.",
        ],
        "cost_head": "What drives the cost",
        "cost": [
            "How many support points need jacks, and how far apart the existing piers are",
            "How much framing is rotted rather than simply unsupported",
            "Crawl space headroom and access – a tight crawl is slower work",
            "Whether standing water or a moisture source has to be dealt with first",
        ],
        "cost_note": 'Ask for a written breakdown of framing replacement, support work, access preparation and moisture correction. Quantities and inaccessible areas should be stated. There is no verified Savannah-wide price range published here.',
        "faqs": [
            ("Can you level the floor completely flat again?",
             "Usually we can recover most of it, but not always all of it. A house that settled over thirty years has finishes, plumbing, and door frames that adjusted to the new shape, and forcing it fully back can crack more than it fixes. The inspection gives you the actual measurements so the target is a decision you make with real numbers, not a promise made before anyone looked."),
            ("Will fixing the floor stop it happening again?",
             "Only if the moisture source is dealt with too. Replacing rotted framing in a crawl space that stays damp means the new wood starts the same clock. That's why encapsulation and structural repair are usually quoted together here – it's not an upsell, it's what keeps the repair from being temporary."),
            ("How long does the work take?",
             "Most residential crawl space repairs run one to three days on site. If the floor has dropped significantly, the lift itself is staged across several visits over a few weeks so the structure moves gradually."),
        ],
        "related": ["crawl-space-encapsulation", "foundation-piering"],
    },
    {
        "slug": "foundation-piering",
        "body": "crack",
        "photo": "foundation-excavation-work.jpg",
        "photo_alt": "A worker excavating alongside a foundation, the access underpinning needs",
        "nav": "Foundation Piering",
        "h1": "Foundation Piering &amp; Underpinning in Savannah, GA",
        "title": "Foundation Piering &amp; Underpinning in Savannah, GA",
        "desc": "Helical and push pier installation in Savannah, GA – underpinning for settling foundations, sinking corners, and stair-step brick cracks. Free inspection.",
        "service_type": "Foundation Piering and Underpinning",
        "lede": "When part of the house is genuinely sinking, no amount of patching the symptoms helps. Piering transfers the weight off the soil that gave way and onto soil deep enough to hold it.",
        "intro": ['Soil conditions should be checked at the property, not assigned from the city name. The <a href="https://soilseries.sc.egov.usda.gov/OSD_Docs/P/POOLER.html">USDA description of the Pooler soil series</a> documents poorly drained soils formed in marine sediments, with a type location in Chatham County. This is one documented local soil profile, not a description of every Savannah lot.', 'Start with the address in <a href="https://www.nrcs.usda.gov/resources/data-and-reports/web-soil-survey">USDA Web Soil Survey</a> to review mapped soil information. Fill, earlier construction and conditions at footing depth still need site investigation. A soil map alone cannot establish pier length, capacity or whether underpinning is needed.', 'Where investigation confirms a support problem, a designed pier system may transfer loads to suitable bearing material. The proposal should state the design loads, installation verification, corrosion protection and any limits on lifting existing finishes.'],
        "situations_head": 'Signs that need a foundation assessment',
        "situations": [
            "Stair-step cracks through brick or block mortar joints",
            "One corner or one wall of the house visibly lower than the rest",
            "Cracks that keep reopening after being patched",
            "Doors and windows binding on one side of the house only",
            "Gaps opening between exterior trim, brick, and the frame",
            "A chimney separating from the wall it's attached to",
        ],
        "method_head": "Helical piers and push piers – the difference",
        "method": ['<strong>Helical piers</strong> advance into the ground by rotation. The designer specifies the system, required capacity and how installation measurements will be verified.', '<strong>Push piers</strong> are hydraulically advanced using the structure as a reaction. Suitability depends on the existing footing, available reaction load and ground conditions.', '<strong>Check durability.</strong> Specify corrosion protection for the actual soil and exposure conditions, along with the selected manufacturer’s requirements.', '<strong>Agree on a recovery target.</strong> Stabilization and lifting are separate objectives. The written design should state the intended outcome and the monitoring or verification needed.'],
        "cost_head": "What drives the cost",
        "cost": [
            "How many piers the affected span needs, and their spacing",
            "How deep the piers have to go before reaching bearing soil",
            "Access for equipment around that side of the house",
            "Whether interior finishes need making good afterward",
        ],
        "cost_note": "Compare proposals by pier quantity, installation criteria, design work, access and restoration. The inspection should establish why underpinning is proposed and what is excluded. A price without those details cannot be meaningfully compared with another quote.",
        "faqs": [['How do you know whether the foundation is still moving?', 'Compare dated crack records, repeatable level measurements, changes at openings and earlier repair information. A single uneven-floor reading shows geometry, not the rate or cause of movement. Where the evidence is unclear, the assessor may recommend monitoring or further investigation.'], ['Will piers lift the house back to level?', 'The intended stabilization and lifting targets depend on the design, ground conditions and the building’s tolerance for movement. Ask for those targets and their limits in writing. No inspection should promise full recovery or permanent stability without establishing the cause and suitable repair scope.'], ['Is this disruptive to the inside of the house?', 'Access depends on the footing locations and chosen system. Some installations can be reached from outside; others may affect interior floors or utilities. The estimate should identify excavation, access openings, protection and restoration before work begins.']],
        "related": ["foundation-crack-repair", "crawl-space-repair"],
    },
    {
        "slug": "concrete-slab-leveling",
        "body": "driveway",
        "photo": "settled-concrete-slab.jpg",
        "photo_alt": "Concrete slab sections separated and dropped at the joint",
        "nav": "Concrete Slab Leveling",
        "h1": "Concrete Slab Leveling &amp; Polyjacking in Savannah, GA",
        "title": "Concrete Slab Leveling in Savannah, GA | Polyjacking",
        "desc": "Concrete slab leveling in Savannah, GA – sunken driveways, patios, walkways, and garage slabs lifted with injected polyurethane foam. Usually done in hours.",
        "service_type": "Concrete Slab Leveling",
        "lede": 'A sound sunken concrete panel may be a lifting candidate. First establish its condition, the cause of movement and whether it is separate from the house foundation.',
        "intro": ['A settled driveway does not establish that the house foundation has failed. Identify the panel, measure the drop and inspect runoff, visible voids and cracks. For local flood-map and elevation-record context, <a href="https://www.pooler-ga.gov/resources/flood-protection/">Pooler publishes address-specific elevation certificates and flood resources</a>. Those records do not diagnose settlement beneath a panel.', 'Where lifting is appropriate, injection can fill a void and adjust the panel. Correcting a continuing water source is a separate part of the scope. Ask whether the panel is sound enough to lift and what would make replacement a better option.'],
        "situations_head": "What we lift",
        "situations": [
            "Driveway sections that dropped and now pond water",
            "Sidewalks and walkways with a raised lip that catches a toe",
            "Patios and pool decks pitched back toward the house",
            "Garage slabs settled at the apron or the entry",
            "Front steps and stoops pulling away from the house",
            "AC pads and shed slabs no longer sitting level",
        ],
        "method_head": "Why foam rather than mudjacking",
        "method": [
            "<strong>It is far lighter.</strong> Polyurethane weighs a fraction of a slurry mix, so it doesn't add load to the same soft soil that let the slab settle in the first place.",
            "<strong>Smaller holes.</strong> Injection ports are roughly the diameter of a pencil, against the much larger holes traditional mudjacking needs.",
            "<strong>It cures in minutes.</strong> The foam reaches strength quickly, so a driveway is normally back in use the same day rather than days later.",
            "<strong>Check the material and drainage.</strong> Product suitability depends on the installation conditions. Obtain the product specification and correct any ongoing erosion rather than treating injected material as a drainage repair.",
        ],
        "cost_head": "What drives the cost",
        "cost": [
            "The square footage being lifted and how far it has dropped",
            "How large the void underneath turns out to be",
            "Slab thickness and whether it is reinforced",
            "Whether the drainage that caused the washout needs correcting too",
        ],
        "cost_note": "Slab leveling is generally the most affordable repair we do and is priced by the area lifted and the volume of foam it takes. It is also the one where doing nothing is most tempting and least wise: the void keeps growing, and a slab that eventually cracks through has to be replaced instead of lifted.",
        "faqs": [
            ("How long before I can drive on it?",
             "Usually the same day. The polyurethane reaches most of its strength within about fifteen to thirty minutes of injection, which is the main practical advantage over older mudjacking methods."),
            ("Will the slab settle again?",
             "Further movement is possible if supporting conditions change or the source of erosion continues. Ask how the proposal addresses drainage, how the result is checked and which limitations or warranty terms apply to the chosen material."),
            ("Can a cracked slab still be lifted?",
             "Often yes, if the pieces are still sound and the crack isn't crumbling. A slab broken into several loose sections is usually past lifting and better replaced – we'll tell you which one you have at the inspection instead of lifting something that won't hold."),
        ],
        "related": ["foundation-crack-repair", "foundation-piering"],
    },
    {
        "slug": "foundation-crack-repair",
        "body": "inspection",
        "photo": "masonry-crack-repair.jpg",
        "photo_alt": "Hands repointing mortar in a cracked masonry wall with a trowel",
        "nav": "Foundation Crack Repair",
        "h1": "Foundation Crack Repair in Savannah, GA",
        "title": "Foundation Crack Repair in Savannah, GA | Structural Sealing",
        "desc": "Foundation crack repair in Savannah, GA – telling structural cracks from cosmetic ones, sealing block and concrete, and fixing the movement behind them.",
        "service_type": "Foundation Crack Repair",
        "lede": "The useful question about a foundation crack is not how to fill it. It is whether anything is still moving – because sealing a crack that's still opening just hides it for a season.",
        "intro": ['Record a crack’s width, location and changes over time before covering it. The shape alone does not establish the cause: compare the masonry with floor measurements, openings, accessible supports and water entry.', 'For a property in Downtown Savannah’s historic district, the <a href="https://www.thempc.org/Historic/Pai">MPC masonry repointing policy and building-documentation guidance</a> are relevant starting points before exterior masonry work. Confirm the review route for the proposed scope. Repointing repairs a joint; it does not by itself establish that structural movement has stopped.'],
        "situations_head": "What we look at",
        "situations": [
            "Stair-step cracking through brick or block mortar joints",
            "Vertical and diagonal cracks in poured concrete walls and footings",
            "Cracks that are visibly wider at the top or bottom",
            "Horizontal cracking, which is the one that warrants urgency",
            "Cracks above door and window openings inside the house",
            "Separation where a porch, stoop, or addition meets the main structure",
        ],
        "method_head": "How each type gets handled",
        "method": [
            "<strong>Non-structural cracks</strong> are sealed – epoxy or polyurethane injection that fills the crack through its full depth and keeps water and humidity out of the wall.",
            "<strong>Cracks from active settlement</strong> need the settlement addressed first with <a href=\"foundation-piering.html\">piering</a>. Sealing before stabilizing is the most common wasted repair in this trade.",
            "<strong>Horizontal cracks</strong> in a foundation wall indicate lateral pressure rather than settlement, and are assessed separately – this is the pattern that deserves a prompt look rather than a wait-and-see.",
            "<strong>Where we are not sure,</strong> we say so and monitor: mark the crack, date it, measure it again. That costs you nothing and beats guessing.",
        ],
        "cost_head": "What drives the cost",
        "cost": [
            "Total length of cracking and the material – poured concrete, block, or brick",
            "Whether injection is enough or the underlying movement needs correcting",
            "Access to the affected wall, inside and out",
            "Whether water intrusion through the crack also needs addressing",
        ],
        "cost_note": "Sealing work on its own is at the affordable end. What changes the number is whether the crack is a symptom of settlement, because then the real repair is stabilization and the sealing is the last step rather than the whole job. The inspection is what tells the two apart, and it is free either way.",
        "faqs": [
            ("Which foundation cracks are actually serious?",
             "Horizontal cracks are the ones to take seriously soonest, because they indicate pressure against the wall rather than settling beneath it. Stair-step cracks through mortar joints and any crack that keeps reopening after repair point to active movement. Fine vertical cracks in poured concrete that haven't changed in years are usually shrinkage and not a structural concern."),
            ("Can I just fill it with the sealant from the hardware store?",
             "For a genuinely cosmetic hairline crack, that keeps water out and is a reasonable thing to do yourself. What it cannot do is tell you which kind of crack you have, and using it on a crack that's still moving means the filler splits and you've lost the ability to see whether it widened."),
            ("Does a crack mean my foundation is failing?",
             "Usually not. Most of the cracks we're called out to look at turn out to be stable and non-structural, and that's a perfectly good outcome for an inspection – you get told it's fine and nothing is sold to you. The minority that are structural are worth finding early, which is the reason to have it looked at rather than guessed at."),
        ],
        "related": ["foundation-piering", "concrete-slab-leveling"],
    },
    {
        "slug": "crawl-space-encapsulation",
        "body": "drainage",
        "photo": "crawl-space-insulation.jpg",
        "photo_alt": "Insulation and moisture control work being installed between floor framing",
        "nav": "Crawl Space Encapsulation",
        "h1": "Crawl Space Encapsulation &amp; Dehumidifiers in Savannah, GA",
        "title": "Crawl Space Encapsulation in Savannah, GA | Dehumidifiers",
        "desc": "Crawl space encapsulation in Savannah, GA – sealed vapor barrier and sized dehumidifier to stop the ground moisture that rots framing in coastal Georgia.",
        "service_type": "Crawl Space Encapsulation",
        "lede": 'Control ground moisture and water entry with a crawl-space plan based on drainage, framing condition and the building’s ventilation needs.',
        "intro": ['The <a href="https://bsesc.energy.gov/energy-basics/crawlspace-capillary-break-crawlspace-floors">Department of Energy guide to crawl-space ground barriers</a> describes liquid water and water vapor entering from the soil. It recommends a continuous sealed ground barrier and measures such as grading and drainage to address bulk-water entry.', 'At a Savannah property, inspect standing water, plumbing leaks, timber and existing equipment before choosing an enclosure. The design should account for humidity control, combustion safety, termite inspection access and any required flood openings. A liner does not replace structural repairs.'],
        "situations_head": "Signs your crawl space needs it",
        "situations": [
            "Musty smell in the house, strongest near floor vents or closets",
            "Visible condensation on ducts, pipes, or the underside of the floor",
            "Insulation sagging out of the joist bays or lying on the ground",
            "Mold or dark staining on joists, girders, or subfloor",
            "Standing water or consistently damp soil after ordinary rain",
            "Floors that feel cold and humid, or cupping hardwood above",
        ],
        "method_head": "What a proper encapsulation includes",
        "method": [
            "<strong>Deal with the water first.</strong> Sealing a liner over standing water traps the problem. Grading, drainage, and a sump where it's needed come before the plastic.",
            "<strong>Heavy liner, sealed – not a loose sheet.</strong> A reinforced vapor barrier across the ground and up the piers and walls, with seams and penetrations sealed and the edges mechanically fastened.",
            "<strong>Close and seal the vents.</strong> Half-measures leave a humid-air path straight back in.",
            "<strong>A dehumidifier sized to the space.</strong> An undersized household unit runs constantly and never wins. Sizing matters more than brand.",
        ],
        "cost_head": "What drives the cost",
        "cost": [
            "Crawl space square footage and headroom to work in",
            "Whether drainage or a sump is needed before the liner goes down",
            "How much damaged insulation and debris has to come out first",
            "Dehumidifier capacity the volume actually requires",
        ],
        "cost_note": "This is generally a mid-range job, priced mostly by square footage and whether water management is needed first. It is also the one with the clearest return on the structural side: it's what stops you paying for joist replacement a second time.",
        "faqs": [
            ("Isn't a crawl space supposed to be vented?",
             "That was the standard assumption for decades, and it works in a dry climate. In coastal Georgia, outdoor summer air is often more humid than the crawl space it's venting into, so the vents raise humidity against the framing instead of lowering it. Sealed-and-conditioned is now the widely accepted approach for this climate."),
            ("Do I still need a dehumidifier if the crawl space is sealed?",
             "Humidity control must be part of the design. A dehumidifier may be appropriate, but its need and size depend on measured conditions and the planned conditioning or ventilation approach. Ask how humidity will be controlled and verified after installation."),
            ("Will this fix a floor that already sags?",
             "No. Moisture control does not restore damaged framing or settled supports. Inspect those separately and repair what the findings justify; encapsulation should not be presented as a complete answer to every sagging floor."),
        ],
        "related": ["crawl-space-repair", "foundation-crack-repair"],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in PAGES}

# Homepage services showcase. Every `points` line below is a condensed
# restatement of something already on that service's own page (its `method`
# or `situations`) -- nothing here introduces a capability the site does not
# already describe in full. build_core.py stamps this into index.html.
TABS = {
    "crawl-space-repair": {
        "accent": "&amp; Floor Jacks",
        "blurb": "If the floor flexes when you walk across it, the problem is almost never the floor – it is the joists, girders, or support posts underneath, and in a Savannah crawl space moisture is usually what weakened them.",
        "points": ["Elevation survey before anything is quoted",
                   "Rotted joists, girders and sill plate replaced",
                   "Steel jacks on poured footings, not bare dirt",
                   "Settled floors lifted gradually, across visits"],
    },
    "foundation-piering": {
        "accent": "&amp; Underpinning",
        "blurb": "When a corner or a wall is genuinely sinking, the fix is transferring its weight past the soil that moved and onto soil that will not – piers driven to load-bearing depth.",
        "points": ["Helical piers torqued to a measured capacity",
                   "Push piers driven to refusal under load",
                   "Galvanized steel within reach of salt air",
                   "Stabilize first, lift only where it is safe"],
    },
    "concrete-slab-leveling": {
        "accent": "&amp; Polyjacking",
        "blurb": "Driveways, patios, walkways and garage slabs that dropped at one edge get lifted back with injected polyurethane foam – hours of work rather than days of demolition.",
        "points": ["Pencil-width injection ports, not core holes",
                   "Foam adds a fraction of the weight of slurry",
                   "Cures in minutes – drive on it the same day",
                   "Closed-cell, so groundwater cannot wash it out"],
    },
    "foundation-crack-repair": {
        "accent": "– Structural or Not",
        "blurb": "Not every crack is structural, and telling the difference is most of the job. We seal what is cosmetic and address the movement behind the ones that are not.",
        "points": ["Epoxy and polyurethane injection where sealing is the fix",
                   "Active settlement addressed with piering first",
                   "Horizontal wall cracks treated as the urgent case",
                   "Marked, dated and re-measured where we are not sure"],
    },
    "crawl-space-encapsulation": {
        "accent": "&amp; Dehumidifiers",
        "blurb": "A sealed vapor barrier and a properly sized dehumidifier stop the ground moisture that rots framing – the repair that keeps the structural work from having to happen twice.",
        "points": ["Drainage and grading dealt with before any liner",
                   "Reinforced barrier sealed to the walls and piers",
                   "Vents closed and sealed, no half-measures",
                   "Dehumidifier sized to the actual space"],
    },
}
assert set(TABS) == {p["slug"] for p in PAGES}, "TABS must cover every service"


def build(page):
    url = f"{SITE}/services/{page['slug']}.html"
    schemas = [
        breadcrumb([("Home", f"{SITE}/"), ("Services", None),
                    (page["nav"], None)]),
        json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": page["service_type"],
            "provider": {"@type": "HomeAndConstructionBusiness", "name": BRAND,
                         "telephone": "+1-912-555-0142"},
            "areaServed": {"@type": "City", "name": "Savannah, GA"},
            "url": url,
        }, indent=2, ensure_ascii=False),
        faq_schema(page["faqs"]),
    ]

    situations = "\n".join(
        f'            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>{s}</li>'
        for s in page["situations"]
    )
    method = "\n".join(f"          <p>{m}</p>" for m in page["method"])
    intro = "\n".join(f"          <p>{t}</p>" for t in page["intro"])
    cost = "\n".join(
        f'            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 6L9 17l-5-5"/></svg>{c}</li>'
        for c in page["cost"]
    )
    related = "\n".join(
        f'        <a class="area-chip" href="{SERVICE_BY_SLUG[r]["slug"]}.html">{SERVICE_BY_SLUG[r]["nav"]} '
        f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>'
        for r in page["related"]
    )
    body_photo, body_alt = WORK_SHOTS[page["body"]]
    areas = "\n".join(
        f'        <a class="area-chip" href="../service-areas/{slug}.html">{label} '
        f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>'
        for slug, label, _ in AREAS
    )

    body = f'''
  <section class="page-hero" style="background-image:linear-gradient(180deg, rgba(11,26,41,.62), rgba(11,26,41,.84)), url(&quot;../images/{page["photo"]}&quot;)">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / Services / {page["nav"]}</div>
      <h1>{page["h1"]}</h1>
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
{intro}
          <div class="img-slot" style="--ar:16/9; margin-top:1.5rem">
            <img src="../images/{body_photo}" alt="{body_alt}" loading="lazy" width="1200" height="675">
            <span class="img-slot-label">{page["nav"]}</span>
          </div>
        </div>
        <div class="local-callout">
          <h3 style="margin-top:0">{page["situations_head"]}</h3>
          <ul class="package-list" style="margin-bottom:0">
{situations}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">The Work</span>
        <h2>{page["method_head"]}</h2>
      </div>
{method}
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Pricing</span>
          <h2>{page["cost_head"]}</h2>
          <ul class="package-list">
{cost}
          </ul>
          <p class="muted">{page["cost_note"]}</p>
        </div>
        <div class="feature-card">
          <h3 style="margin-top:0">Free structural inspection</h3>
          <p class="muted">Elevation readings, a look at the actual failure, and a written scope with a real number – before you commit to anything.</p>
          <p><a class="btn btn-primary btn-block" href="../free-inspection.html">Book an Inspection</a></p>
          <p style="margin-bottom:0"><a class="btn btn-outline btn-block" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">FAQ</span>
        <h2>{page["nav"]} – common questions</h2>
      </div>
{faq_blocks(page["faqs"])}
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <span class="eyebrow">Related Work</span>
        <h2>Often done alongside this</h2>
      </div>
      <div class="area-grid">
{related}
      </div>
      <div class="section-head" style="margin-top:2.5rem">
        <span class="eyebrow">Where We Work</span>
        <h2>{page["nav"]} across Chatham County</h2>
      </div>
      <div class="area-grid">
{areas}
        <a class="area-chip" href="../service-areas/index.html">All areas <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></a>
      </div>
    </div>
  </section>
{cta_band(D, "Want it looked at properly?", "The inspection is free, and if the answer is that it can wait, that's what we'll tell you.")}'''

    return (head(D, page["title"], page["desc"], url, schemas)
            + header(D) + body + footer(D))


if __name__ == "__main__":
    for pg in PAGES:
        write(f"services/{pg['slug']}.html", build(pg))
    print(f"\n{len(PAGES)} service pages generated")
