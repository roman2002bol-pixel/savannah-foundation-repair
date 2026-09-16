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
        "lede": "If the floor flexes when you walk across it, the problem is almost never the floor. It's the joists, girders, or support posts underneath – and in a Savannah crawl space, moisture is usually what weakened them.",
        "intro": [
            "Most Savannah homes sit on a raised crawl space, supported by a grid of piers and wood framing that was sized correctly the day it was built. Two things degrade that over the decades here: soil that shifts under the footings as it wets and dries, and humidity that never leaves the crawl space, softening the wood from below until it can no longer carry the span.",
            "Repair means restoring the load path, not leveling the surface. We identify which support points have dropped and by how much, replace the framing that's gone soft, and set adjustable steel jacks on poured footings that bear on stable soil instead of loose fill.",
        ],
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
        "cost_note": "Local pricing for this work commonly runs from roughly $1,300 for a small run of joist and jack work up to about $4,900 when several bays need framing replaced. Broader structural jobs go higher. You get a firm number in writing after the inspection, never a phone estimate.",
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
        "intro": [
            "Savannah's coastal plain soil is sandy loam over clay layers, sitting above a water table that's rarely more than a few feet down. That profile carries a house perfectly well until something changes it – a long drought, a broken supply line, poorly compacted fill under an addition, or years of downspouts discharging against one corner.",
            "When it does change, the footing goes with it. Piers are the structural answer: steel driven or screwed down past the unstable layer to soil that can carry the load, with brackets that transfer the building's weight onto them.",
        ],
        "situations_head": "Signs that point to piering rather than a surface repair",
        "situations": [
            "Stair-step cracks through brick or block mortar joints",
            "One corner or one wall of the house visibly lower than the rest",
            "Cracks that keep reopening after being patched",
            "Doors and windows binding on one side of the house only",
            "Gaps opening between exterior trim, brick, and the frame",
            "A chimney separating from the wall it's attached to",
        ],
        "method_head": "Helical piers and push piers – the difference",
        "method": [
            "<strong>Helical piers</strong> are screwed into the ground with a measured torque that correlates to capacity, so you know what each one will hold as it goes in. They suit lighter loads and situations where you need confirmation of capacity during installation.",
            "<strong>Push piers</strong> use the weight of the structure itself to drive sections down until they meet refusal on a firm bearing layer. They suit heavier loads and deeper unstable soil.",
            "<strong>Galvanized steel, not raw.</strong> Within reach of salt air, corrosion protection on anything permanently in the ground isn't an upgrade, it's the baseline.",
            "<strong>Stabilize, then lift where it's safe.</strong> Every pier job stops the movement. Recovering the original elevation is a separate judgement call, made from the measurements and what the structure can take.",
        ],
        "cost_head": "What drives the cost",
        "cost": [
            "How many piers the affected span needs, and their spacing",
            "How deep the piers have to go before reaching bearing soil",
            "Access for equipment around that side of the house",
            "Whether interior finishes need making good afterward",
        ],
        "cost_note": "Piering is the highest-ticket repair on this list – a settling corner is usually a several-thousand-dollar job, and a full side of a house is more. That is exactly why the inspection and the elevation readings come first: if the movement turns out to be seasonal rather than progressive, piering may not be the right answer at all, and we would rather tell you that.",
        "faqs": [
            ("How do you know the foundation is still moving and not settled long ago?",
             "Cracks that have been patched and reopened, doors that got worse over one season, and measurable elevation differences across the span all point to active movement. Where it isn't clear, the honest answer is to monitor it – marking and dating a crack and re-measuring in a few months costs nothing and tells you more than a guess."),
            ("Will piers lift the house back to level?",
             "Piers reliably stop further settlement. How much elevation comes back depends on what the structure will tolerate – brick, plaster, and tile all have limits, and pushing past them trades a foundation problem for a finishes problem. We give you the measurements and the realistic recovery before the work is scheduled."),
            ("Is this disruptive to the inside of the house?",
             "Most residential piering is done from outside, excavating at each pier location along the affected footing. The yard takes the disruption rather than your living space, and the excavations are backfilled when the work is complete."),
        ],
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
        "lede": "A driveway slab that dropped at one edge doesn't need tearing out. Polyurethane foam injected underneath lifts it back and fills the void that let it drop – normally within a few hours.",
        "intro": [
            "Concrete outside a Savannah home sits on sandy soil that water moves through easily. Over time, rain running off the roof and along the drive washes fines out from under the slab, leaving a void. The slab is strong enough to span it for a while, then it settles into it – usually at one corner, usually where the water goes.",
            "Polyjacking fixes the cause and the symptom together. Small ports are drilled through the slab, expanding polyurethane is injected below it, and the foam fills the void and lifts the concrete back to grade as it expands.",
        ],
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
            "<strong>It does not wash out.</strong> Closed-cell foam is unaffected by the groundwater that erodes a soil-based slurry – which matters a great deal on this coast.",
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
             "Not from the same void – the foam fills it permanently and doesn't wash away. What can cause new settling is the original water problem continuing, so if a downspout or a grading issue is feeding water under that slab, fixing it is part of the job rather than an afterthought."),
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
        "intro": [
            "Concrete cracks. Some of it is ordinary curing shrinkage that appeared in the first year and has not changed since, and that genuinely is cosmetic. What matters is telling that apart from a crack that is tracking active movement in the footing below.",
            "The pattern usually gives it away. Hairline vertical cracks in poured concrete are typically shrinkage. Stair-step cracks following the mortar joints in block or brick, cracks wider at one end than the other, and cracks that reopen after being patched are all movement – and the repair for those starts underneath, not at the surface.",
        ],
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
        "lede": "A vented crawl space in coastal Georgia doesn't dry out in summer – it pulls humid outside air onto cool surfaces and condenses it. Encapsulation ends that cycle.",
        "intro": [
            "The logic behind crawl space vents assumed outdoor air is drier than crawl space air. On the Georgia coast in July it very often isn't. Warm, humid air entering a cool crawl space raises the relative humidity against the framing, and wood that stays above roughly twenty percent moisture content is wood that rots and grows mold.",
            "Encapsulation treats the crawl space as part of the building rather than as outdoors: a heavy sealed liner across the ground and up the piers and walls, vents closed, and a dehumidifier sized for the volume to hold the space at a stable humidity year-round.",
        ],
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
             "In this climate, yes. The liner stops moisture coming up from the soil, but it can't remove what's already in the air or what enters when the hatch opens. A correctly sized dehumidifier is what actually holds the humidity down year-round, and without one an encapsulation underperforms."),
            ("Will this fix a floor that already sags?",
             "No – encapsulation stops the cause, it doesn't restore the structure. Framing that has already lost strength needs the structural repair as well. The two are usually done together for exactly that reason: one fixes what happened, the other stops it happening again."),
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
