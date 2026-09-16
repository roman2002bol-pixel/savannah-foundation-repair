#!/usr/bin/env python3
"""Location page content + generation. Run: python build_areas.py

Every `facts` block below traces to research logged in STATUS.md and links
out to the source it came from (the standing outbound-authority-link rule).
Nothing here is a template with the place name swapped -- the construction
era, foundation type, soil and the failure mode genuinely differ per area,
which is the whole reason these pages are defensible.
"""
from build_pages import (SITE, BRAND, PHONE_DISPLAY, PHONE_HREF, SERVICES, WORK_SHOTS,
                         head, header, footer, cta_band, breadcrumb,
                         faq_blocks, faq_schema, write)
import json

D = 1

PAGES = [
    {
        "slug": "downtown-savannah-ga",
        "work": "crack",
        "photo": "downtown-savannah-home.jpg",
        "photo_alt": "Historic brick building in downtown Savannah under live oaks",
        "name": "Downtown &amp; Historic Savannah",
        "plain": "Downtown Savannah, GA",
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
        "work": "slab",
        "photo": "pooler-new-home.jpg",
        "photo_alt": "Newer two-story home with a concrete driveway, typical of Pooler subdivisions",
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
             "Mostly not. The newer subdivisions here are predominantly slab-on-grade, so the work is usually slab leveling, crack repair, and occasionally piering rather than the crawl space stabilization that dominates closer to the water."),
            ("Do you serve all of Pooler?",
             "Yes, all of Pooler, GA (31322), including the newer neighborhoods off Pooler Parkway and the older sections toward Pine Barren Road."),
        ],
    },
    {
        "slug": "richmond-hill-ga",
        "work": "slab",
        "photo": "richmond-hill-home.jpg",
        "photo_alt": "Brick family home of the kind built across Richmond Hill's newer neighborhoods",
        "name": "Richmond Hill, GA",
        "plain": "Richmond Hill, GA",
        "zip": "31324",
        "lede": "Bryan County, not Chatham – sandy loam over clay, the Ogeechee River on the eastern edge, and a building boom that has not slowed down.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Richmond_Hill,_Georgia" target="_blank" rel="noopener">Richmond Hill</a> sits in Bryan County rather than Chatham, southwest of Savannah with the Ogeechee River forming its eastern boundary. The soil here is coastal-plain sandy loam over clay layers, with the same high water table as the rest of the region – a profile that drains fast at the surface and holds water below. The county has been growing hard, and a great deal of the housing stock is recent construction on newly developed ground, which brings the same fill-settlement pattern seen in Pooler. Closer to the river, older properties add moisture exposure on top of it.',
        "note_head": "Different county, same coastal-plain soil",
        "note": "Being in Bryan County changes the permitting authority, not the engineering. The sandy-loam-over-clay profile and the shallow water table behave the same way here as in Chatham, so the repairs are the same ones – it is worth stating plainly because the county line confuses people looking for a local contractor.",
        "focus": ["Fill settlement under newer construction", "Slab and flatwork leveling", "Crawl space moisture on older riverside properties"],
        "faqs": [
            ("You're a Savannah company – do you actually come to Richmond Hill?",
             "Yes. Richmond Hill is in Bryan County rather than Chatham, but it is part of the same metro and the same drive, and the soil conditions are effectively identical. It is a regular part of our service area, not an outlying exception."),
            ("Is the soil here different from Savannah proper?",
             "Not meaningfully. It's the same coastal-plain profile – sandy loam over clay layers with a high water table. What differs is the housing stock: a lot of Richmond Hill is recent construction on newly developed ground, so fill settlement is proportionally more of what we see."),
            ("Do you serve all of Richmond Hill?",
             "Yes, all of Richmond Hill, GA (31324), including the newer master-planned communities and the older neighborhoods nearer the Ogeechee River."),
        ],
    },
    {
        "slug": "skidaway-island-ga",
        "work": "encapsulation",
        "photo": "skidaway-marsh.jpg",
        "photo_alt": "Tidal marsh and creeks surrounding Skidaway Island at sunset",
        "name": "Skidaway Island",
        "plain": "Skidaway Island, GA",
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
        "work": "framing",
        "photo": "wilmington-island-marsh.jpg",
        "photo_alt": "Coastal marshland of the kind that surrounds Wilmington Island",
        "name": "Wilmington Island",
        "plain": "Wilmington Island, GA",
        "zip": "31410",
        "lede": "Sixties and seventies ranch houses on pier-and-beam foundations, between the Wilmington River and the marsh – the toughest moisture conditions in the county.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Wilmington_Island,_Georgia" target="_blank" rel="noopener">Wilmington Island</a> is characteristically sprawling ranch homes from the 1960s and 70s, a great many of them on pier-and-beam foundations suited to the low-lying ground. The groundwater table here is extremely shallow, so even an ordinary rain event can put water into a crawl space, and high-tide flooding reaches some streets through aging stormwater infrastructure. Salt is the extra factor most inland contractors underestimate: it corrodes metal fasteners, connectors and hardware, and it stays in building materials afterward, drawing moisture back in long after the water has gone.',
        "note_head": "Why galvanized hardware is not optional here",
        "note": "On the islands, anything steel that is permanently in the ground or in the crawl space gets galvanized protection as standard. Salt-laden air and repeated wetting will find untreated hardware, and a support jack that corrodes at the base has quietly stopped doing its job years before anyone notices the floor moving again.",
        "focus": ["Pier-and-beam settling on low-lying lots", "Rotted framing from repeated crawl space wetting", "Salt corrosion of fasteners, connectors, and support hardware"],
        "faqs": [
            ("Water gets into my crawl space after heavy rain – is that normal here?",
             "It's common on the island because the groundwater table is very shallow, but common isn't the same as acceptable. Repeated wetting is what rots joists and girders, so the fix is drainage and encapsulation rather than living with it. What's not normal is water that stays for days, which points to a drainage problem worth solving first."),
            ("Does salt air really affect a foundation?",
             "Yes, specifically the metal in it. Salt corrodes fasteners, connectors, and support hardware, and it stays in materials after the water dries, pulling moisture back in. That's why galvanized hardware is standard for us out here rather than an upgrade option."),
            ("Do you serve all of Wilmington Island?",
             "Yes, all of Wilmington Island (31410). Whitemarsh Island shares the same ZIP but is a separate island with newer housing, so it has its own page."),
        ],
    },
    {
        "slug": "georgetown-ga",
        "work": "slab",
        "photo": "georgetown-ranch-home.jpg",
        "photo_alt": "Single-story ranch home typical of Georgetown's 1970s and 1980s build-out",
        "name": "Georgetown",
        "plain": "Georgetown, Savannah",
        "zip": "31419",
        "lede": "A large seventies and eighties suburb southwest of the city, across the Little Ogeechee – now at the age where original foundations start showing their history.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Georgetown,_Chatham_County,_Georgia" target="_blank" rel="noopener">Georgetown</a> sits about fourteen miles southwest of downtown Savannah, across the Little Ogeechee River, and was built out mostly through the 1970s and 1980s with brick ranch homes and Lowcountry cottages, plus newer phases since. That build era is the useful detail: these houses are now forty to fifty years old, which is exactly when original crawl space framing, support posts, and driveway slabs reach the end of their first service life in this climate. The failures here are less dramatic than on the islands and more a matter of accumulated age.',
        "note_head": "A mixed-age neighborhood means mixed repairs",
        "note": "Because Georgetown was built in phases over several decades, two houses a few streets apart can need entirely different work – one a crawl space with tired framing, the next a newer slab with settled flatwork. It is the main reason we do not quote this neighborhood over the phone.",
        "focus": ["Aging crawl space framing and support posts", "Settled driveways and walkways", "Original-era piers reaching end of service life"],
        "faqs": [
            ("My house is from the eighties – is foundation work expected by now?",
             "Not inevitable, but it's the age where original support framing and flatwork in this climate commonly need attention for the first time. Forty-odd years of Georgia coastal humidity under a crawl space adds up, and catching it at the tired stage costs considerably less than catching it at the failed stage."),
            ("Is Georgetown in the city of Savannah?",
             "It's an unincorporated community in Chatham County, just across the Little Ogeechee River from the city limits, about fourteen miles southwest of downtown. It's well inside our normal service area either way."),
            ("Do you serve all of Georgetown?",
             "Yes, all of Georgetown (31419), from the original 1970s sections through to the newer phases."),
        ],
    },
    {
        "slug": "midtown-savannah-ga",
        "work": "drainage",
        "photo": "midtown-savannah-bungalow.jpg",
        "photo_alt": "Clapboard bungalow with a deep front porch, the housing type across Savannah's midtown streets",
        "name": "Midtown Savannah &amp; Ardsley Park",
        "plain": "Midtown Savannah, GA",
        "zip": "31405",
        "lede": "Wood-frame houses from the 1910s and 1920s standing on some of the city's worst-draining ground – old piers plus a stormwater basin the city is still rebuilding.",
        "facts": 'The <a href="https://en.wikipedia.org/wiki/Ardsley_Park%E2%80%93Chatham_Crescent_Historic_District" target="_blank" rel="noopener">Ardsley Park–Chatham Crescent Historic District</a> was laid out as two subdivisions in 1909–1910 and built out through the 1930s: 400 acres, 998 contributing buildings, National Register listed since 1985, and overwhelmingly wood-frame houses on masonry pier foundations. The second fact about midtown matters just as much. These streets sit in the Casey Canal drainage basin, and the flooding here is bad enough that the City of Savannah has a multi-phase <a href="https://www.savannahga.gov/3900/Casey-South-Project" target="_blank" rel="noopener">Casey Canal drainage improvement program</a> still working through it. A hundred-year-old pier foundation that stands in water several times a year is the exact combination that undermines footings and keeps a crawl space from ever drying out.',
        "note_head": "Drainage is half the foundation problem here",
        "note": "Water that pools against the foundation after every heavy rain washes the fines out from under piers and holds the crawl space at a moisture level where framing cannot dry. Repairing the framing without changing where the water goes means doing the same job again. On these streets the grading and drainage part of the scope is not an upsell – it is what makes the structural repair last.",
        "focus": ["Century-old masonry piers under wood-frame houses", "Crawl spaces that stay wet in the Casey Canal basin", "Cracked plaster and sticking doors from uneven settlement"],
        "faqs": [
            ("My house is from the 1920s – isn't some settling just normal at that age?",
             "Some is. A century-old house that moved early, stopped, and has been stable since is not a project. What is worth acting on is movement that is still happening: cracks that reopen after being filled, doors that were fine last year and stick now, or a floor that has developed a slope you can feel. Elevation readings tell those two apart, which is the point of measuring rather than guessing."),
            ("Does the flooding on my street actually affect my foundation?",
             "Yes, though indirectly. Standing water does not push a house over. What it does is wash soil out from under pier footings and keep the crawl space humid enough that framing never dries, and both of those are slow, cumulative, and entirely fixable once the water is redirected."),
            ("Is Ardsley Park a protected historic district?",
             "It is a National Register historic district and also a locally designated conservation district under the Metropolitan Planning Commission. National Register listing on its own does not restrict what a private owner does, but local conservation-district rules can apply to visible exterior work, so it is worth confirming for your address before exterior foundation work starts."),
            ("Do you serve all of Midtown Savannah?",
             "Yes, the 31405 area – Ardsley Park, Chatham Crescent, Habersham Village, and the streets either side of Victory Drive."),
        ],
    },
    {
        "slug": "southside-savannah-ga",
        "work": "framing",
        "photo": "southside-cracked-driveway.jpg",
        "photo_alt": "Cracked concrete driveway running alongside a suburban house and garage",
        "name": "Southside Savannah",
        "plain": "Southside Savannah, GA",
        "zip": "31406",
        "lede": "Savannah's first big planned suburb and everything built after it – late-fifties through seventies housing now well into its second half-century.",
        "facts": 'Windsor Forest, developed by Delta Land Corp from the late 1950s between Abercorn and White Bluff, was marketed as Savannah\'s first planned community and at the time the largest residential development in Georgia – platted for around 3,000 home sites with its own church, school and golf-course land. The <a href="http://ghs.galileo.usg.edu/ghs/view?docId=ead%2FMS+1790-ead.xml" target="_blank" rel="noopener">Georgia Historical Society</a> holds the developer\'s papers on it. Build-out ran through the 1960s and the neighborhoods around it kept going into the 1970s. That history is the whole story structurally: the Southside housing stock is dominated by fifty- to seventy-year-old ranch homes, built quickly and at volume, on slabs and crawl spaces poured and framed to the standards of the day.',
        "note_head": "Built fast, at scale, sixty years ago",
        "note": "A neighborhood that went up in a few years also ages in a few years, which is why one street can produce several near-identical jobs in a season. The upside is that the failures out here are predictable. An inspection on the Southside usually confirms a known pattern for the build era rather than turning up a surprise.",
        "focus": ["Sixty-year-old crawl space framing and support posts", "1960s slabs cracking over lightly prepared subgrade", "Settled driveways, walkways and carport slabs"],
        "faqs": [
            ("Why do so many houses around here seem to need the same repair?",
             "Because they were built at the same time, by the same methods, on the same ground. Original support posts, original flatwork and original drainage all reach the end of their first service life at roughly the same point, and in this climate that point is somewhere around the fifty-year mark. It is not a defect in your house specifically."),
            ("Is Windsor Forest part of what you cover?",
             "Yes. Windsor Forest and the neighborhoods either side of Abercorn Street and White Bluff Road are a regular part of the work. So is the older housing closer to DeRenne."),
            ("Slab or crawl space – which do Southside houses have?",
             "Both, and often on the same street. The earlier phases lean toward raised crawl space construction and the later ones toward slab-on-grade, which is exactly why the inspection starts by establishing what is actually under your house rather than assuming."),
            ("Do you serve all of Southside Savannah?",
             "Yes, the 31406 area and the adjoining blocks, from the Windsor Forest area across to the neighborhoods off Eisenhower and Montgomery Cross Road."),
        ],
    },
    {
        "slug": "isle-of-hope-ga",
        "work": "framing",
        "photo": "isle-of-hope-southern-home.jpg",
        "photo_alt": "Raised Southern house with double porches under live oaks draped in Spanish moss",
        "name": "Isle of Hope",
        "plain": "Isle of Hope, GA",
        "zip": "31406",
        "lede": "Nineteenth-century summer cottages on a bluff above the Skidaway River – the oldest residential foundations in the county outside the historic district.",
        "facts": 'Savannah\'s wealthier residents began building summer houses on the banks of the Skidaway River here around the middle of the nineteenth century, escaping the heat and the fevers of the city, and Isle of Hope stayed a resort into the early twentieth. The <a href="https://www.myhsf.org/what-we-do/historic-districts/isle-of-hope/" target="_blank" rel="noopener">Historic Savannah Foundation</a> records the district as larger historic properties along riverfront Bluff Drive with smaller cottages on the inland lots, two frame churches from the 1870s, and a few houses believed to be early nineteenth century. In practice that means raised wood-frame cottages on brick or tabby piers, sitting directly over a tidal river, in the most humid exposure in Chatham County short of the barrier island itself.',
        "note_head": "Old framing, new moisture",
        "note": "These houses lasted a century and a half because they were built raised and vented over ground that drained. Where modern landscaping, an added patio slab, or a retrofitted HVAC system has changed how air and water move under the house, that balance breaks – and rot appears in framing that had been perfectly sound for generations. Working out what changed is usually more useful than replacing more wood.",
        "focus": ["Nineteenth-century brick and tabby pier foundations", "Sill plate and joist-end rot around the perimeter", "Tidal-river humidity under raised cottages"],
        "faqs": [
            ("Is a house from the 1800s too old to work on?",
             "No. Old heart-pine framing is often in better condition than people expect, and the failures are usually localized – sill plates and joist ends at the perimeter, and piers that have lost mortar. What an old house does need is a slower approach: less aggressive lifting, staged over more visits, so plaster and original finishes are not cracked to gain a level floor."),
            ("Is Isle of Hope in a historic district?",
             "Yes, it is a recognized historic district, roughly bounded by the Skidaway River on one side. National Register status by itself does not restrict what a private owner does to their own house, but it is still worth confirming locally before work that changes anything visible from Bluff Drive."),
            ("Why is moisture worse here than a few miles inland?",
             "Because the ground under the house is tidal-river bank. The water table is high, the air is humid year round, and a raised crawl space over that ground never gets the dry spell that would let framing recover. It is the same reason encapsulation gets quoted alongside structural work here more often than anywhere else in the county."),
            ("Do you serve all of Isle of Hope?",
             "Yes, the whole of Isle of Hope in 31406, from the Bluff Drive waterfront to the streets back from it."),
        ],
    },
    {
        "slug": "thunderbolt-ga",
        "work": "excavation",
        "photo": "thunderbolt-shrimp-dock.jpg",
        "photo_alt": "Shrimp boat and stacked crab pots tied up at a working river dock",
        "name": "Thunderbolt",
        "plain": "Thunderbolt, GA",
        "zip": "31404",
        "lede": "A working river town on the Wilmington – shrimp docks, compact older houses, and ground that has been at the water's edge since 1733.",
        "facts": 'Oglethorpe named the place in 1733; it was incorporated as Warsaw in 1856, took the name Thunderbolt back in 1921, and spent most of the twentieth century as a seafood port with hundreds of shrimp boats working both banks of the Wilmington River, according to the <a href="https://www.thunderboltga.org/community/history.php" target="_blank" rel="noopener">Town of Thunderbolt</a>. That history set the housing: compact working houses close to the water, a great many of them pier-and-beam, on low ground beside a tidal river. The foundation problems here come from the setting more than the age – shallow groundwater, tidal influence, and salt in the air working on every piece of metal under the house.',
        "note_head": "A separate town, with its own permitting",
        "note": "Thunderbolt is its own incorporated municipality inside Chatham County, not a Savannah neighborhood, so structural permits go through the town rather than the city. It is a small administrative difference that only matters for scheduling – but discovering it after a crew is booked is worse than raising it at the inspection.",
        "focus": ["Pier-and-beam settling on low riverside lots", "Shallow groundwater under the crawl space", "Salt corrosion of jacks, fasteners and connectors"],
        "faqs": [
            ("Is Thunderbolt part of the city of Savannah?",
             "No. It is a separate incorporated town within Chatham County with its own government, which is why permitting for structural work goes through the town rather than the city. For our purposes it is a ten-minute drive from downtown and part of the normal service area."),
            ("Does being right on the river make the work harder?",
             "It makes it more specific. Shallow groundwater limits how deep a footing can go before it meets water, and salt in the air shortens the life of untreated metal, so galvanized hardware and a drainage plan are standard rather than optional. The repairs themselves are the same ones we do elsewhere."),
            ("Do you serve all of Thunderbolt?",
             "Yes, the whole town in 31404, including the streets running down to the Wilmington River."),
        ],
    },
    {
        "slug": "whitemarsh-island-ga",
        "work": "drainage",
        "photo": "whitemarsh-tidal-creeks.jpg",
        "photo_alt": "Tidal creeks winding through salt marsh at the edge of an island community",
        "name": "Whitemarsh Island",
        "plain": "Whitemarsh Island, GA",
        "zip": "31410",
        "lede": "The first island off the mainland – mostly built since the 1970s, ringed by Richardson and Turner Creeks, and tidal on almost every side.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Whitemarsh_Island,_Georgia" target="_blank" rel="noopener">Whitemarsh Island</a> is an unincorporated community and census-designated place in Chatham County, population 6,983 at the 2020 census, bordered by Richardson Creek to the north and Turner Creek to the east. The islands area developed largely from the 1970s onward, which puts the housing stock here between Wilmington Island\'s sixties ranches and Pooler\'s new subdivisions – a lot of 1980s through 2000s construction on lots cut close to the marsh edge. Flood exposure is the defining constraint rather than age: properties toward Johnny Mercer Boulevard, Grays Creek and the Turner Creek marsh carry real flood risk, and a foundation that takes water around it several times a year is a foundation whose crawl space never dries.',
        "note_head": "Newer house, same salt and water",
        "note": "A 1990s house on Whitemarsh is not old enough to be failing from age, but it sits in the same salt air and the same shallow groundwater as the 1960s houses one island further out. What we find here is nearly always moisture-driven – crawl space humidity, corroded hardware, drainage that has stopped working – rather than framing that has simply worn out.",
        "focus": ["Crawl space moisture on lots cut close to the marsh", "Corroded hardware and fasteners in salt air", "Drainage failures around 1980s–2000s foundations"],
        "faqs": [
            ("Whitemarsh or Wilmington – aren't they the same place?",
             "They share the 31410 ZIP and people use the names loosely, but they are separate islands with different housing. Whitemarsh is the one you cross first coming from the mainland and skews newer; Wilmington, further out, is dominated by 1960s and 70s ranch homes on pier-and-beam. The failure patterns differ enough that they are worth separating."),
            ("The water floods my yard but never the house. Does that matter?",
             "For the foundation, yes. Water standing around the perimeter soaks the ground the footings bear on and pushes humidity up into the crawl space, and repeated cycles of that are what rot joists and corrode support hardware. The house staying dry inside means you have time to deal with it, not that there is nothing to deal with."),
            ("Do you serve all of Whitemarsh Island?",
             "Yes, all of Whitemarsh Island in 31410, including Talahi Island and the neighborhoods off Johnny Mercer Boulevard."),
        ],
    },
    {
        "slug": "tybee-island-ga",
        "work": "excavation",
        "photo": "tybee-raised-beach-house.jpg",
        "photo_alt": "Beachfront house raised on pilings above the dune line",
        "name": "Tybee Island",
        "plain": "Tybee Island, GA",
        "zip": "31328",
        "lede": "A barrier island where base flood elevation is nine feet and the city's own grant program is lifting houses higher still – the most demanding structural environment in the county.",
        "facts": 'Building high is not a modern idea on Tybee: the raised Tybee cottage dates from the island\'s 1910–1939 building era, and the <a href="https://en.wikipedia.org/wiki/Tybee_Island_Strand_Cottages_Historic_District" target="_blank" rel="noopener">Strand Cottages Historic District</a> preserves eighteen of them largely unchanged. What has changed is the standard. Under the city\'s FEMA-funded elevation program, homes are raised above a base flood elevation of nine feet plus two feet of freeboard – at least eleven feet above sea level – and the island has drawn roughly $1.5 million in Hazard Mitigation Grant funding for elevations after Hurricane Irma, at 85% grant with the owner covering the rest. The <a href="https://www.cityoftybee.org/297/Flood-Information-for-Homeowners" target="_blank" rel="noopener">City of Tybee Island</a> publishes what applies to a given property.',
        "note_head": "Elevation is a different job from repair – we will say which you need",
        "note": "Lifting a whole house onto new piers to meet flood elevation is structural moving work, done under an engineer's design and a permit, and it is not what we do. What we do is the repair side: piers and support under a house at its existing elevation, the framing damage that salt and flooding produce, and the moisture work underneath. If elevation is genuinely what your property needs, knowing that before anyone quotes you for something else saves real money.",
        "focus": ["Pier and piling support under raised cottages", "Salt corrosion of every metal connector under the house", "Framing damage from repeated flood exposure"],
        "faqs": [
            ("Can you raise my house to meet flood elevation?",
             "No, and that is worth being direct about. Full house elevation is specialist structural moving work carried out under an engineered design and a city permit. We handle foundation repair – support, piers, framing and moisture – at the elevation your house already sits at. If elevation is what you actually need, we will tell you that at the inspection rather than quoting around it."),
            ("Why does hardware fail so much faster out here?",
             "Salt. It corrodes fasteners, connectors, straps and support hardware, and it stays in the material after the water has gone, drawing moisture back in. A support jack quietly corroding at its base has stopped carrying load long before anyone notices the floor moving again, which is why galvanized hardware is standard on the island rather than an upgrade."),
            ("Is flood damage under the house covered by insurance?",
             "That depends entirely on your policy and whether it is an NFIP flood policy or a standard homeowners policy – we are not the right people to answer it and would be guessing. What we can do is document what we find under the house in writing, which is usually what a claim needs."),
            ("Do you serve all of Tybee Island?",
             "Yes, all of 31328, from the north end through mid-island to the south end, including the back-river streets."),
        ],
    },
    {
        "slug": "garden-city-ga",
        "work": "slab",
        "photo": "garden-city-port-terminal.jpg",
        "photo_alt": "Stacked shipping containers and a gantry crane at a river container terminal",
        "name": "Garden City",
        "plain": "Garden City, GA",
        "zip": "31408",
        "lede": "Built in 1939 to house port and factory workers, and still sitting alongside the busiest single container terminal on the East Coast.",
        "facts": '<a href="https://www.gardencity-ga.gov/about-garden-city" target="_blank" rel="noopener">Garden City</a> was incorporated on 8 February 1939 as Industrial City Gardens – literally a community created to house the workforce for the new factories and chemical plants west of downtown Savannah – and renamed in 1941. It is now home to the Georgia Ports Authority\'s largest and busiest ocean terminal. Two things follow for foundations. The core housing stock is small, economically built mid-century workforce housing, much of it eighty years old, on shallow footings or slabs poured to the standards of the day. And the ground is low, filled, industrial river-plain land rather than the sandy ridge the older parts of Savannah sit on.',
        "note_head": "Modest houses, real structural work",
        "note": "Mid-century workforce housing was built to a price – thinner slabs, shallower footings, less soil preparation underneath. That does not make a house unrepairable. It does mean the fix is often adding support that was never there to begin with, rather than replacing support that failed, and that is a different conversation than the one a 1990s house needs.",
        "focus": ["Shallow footings under 1940s–60s workforce housing", "Slab cracking on low, filled river-plain ground", "Settled driveways, steps and entry slabs"],
        "faqs": [
            ("Is a small older house actually worth repairing?",
             "Usually yes, and usually for less than people assume. Support work under a modest single-story house is a smaller job than under a large two-story one, because there is less load and better access. We price on the number of support points and the difficulty of getting to them, not on what the house is worth."),
            ("Does all the port and truck traffic nearby affect foundations?",
             "Honestly, not much. Vibration from nearby traffic gets blamed for a lot of cracks that are actually soil and moisture movement. We would rather measure and tell you it is the ground than sell you a story about the trucks."),
            ("Do you serve all of Garden City?",
             "Yes, the whole of Garden City in 31408, from the older streets near Augusta Road out to the newer sections."),
        ],
    },
    {
        "slug": "port-wentworth-ga",
        "work": "driveway",
        "photo": "port-wentworth-new-subdivision.jpg",
        "photo_alt": "Aerial view of a recently built subdivision of similar houses on curving streets",
        "name": "Port Wentworth",
        "plain": "Port Wentworth, GA",
        "zip": "31407",
        "lede": "An old sugar-refinery town that has more than tripled since 2000 – so a house here is usually either eighty years old or eight.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Port_Wentworth,_Georgia" target="_blank" rel="noopener">Port Wentworth</a> has grown faster than almost anywhere in the state: 5,359 residents at the 2010 census, 10,878 in 2020, and an estimated 18,600 now, still adding several percent a year. The older core grew up around the sugar refinery that has operated here for generations. That leaves a genuinely split housing stock – a small older center of mid-century houses, and a very large volume of recent subdivision building on land that was marsh, timber or farm until recently. New lots are graded and filled before the slab goes down, and fill that was not compacted to specification keeps consolidating under load for years afterward.',
        "note_head": "Two towns in one, two different repairs",
        "note": "A 1950s house near the refinery and a 2021 house off Highway 21 fail in completely different ways – one from age and shallow footings, the other from fill settlement under new flatwork. Both are common here in roughly equal measure, which is why this is not an area we will quote from a phone description.",
        "focus": ["Fill settlement under new-construction slabs and driveways", "Older core housing on shallow mid-century footings", "Drainage washing fines out from under flatwork"],
        "faqs": [
            ("My house is three years old and the driveway has already dropped. Is that a builder defect?",
             "Usually it is fill consolidation rather than a defect – the concrete is fine, the ground under it is still settling. Check your builder's warranty first, because some cover flatwork for a period and it costs nothing to ask. Where the warranty has expired or does not apply, lifting the slab back is a small job compared with replacing it."),
            ("Is Port Wentworth in Chatham County?",
             "Yes, it is an incorporated city in Chatham County on the northwest side of Savannah, next to Garden City and near the Effingham County line."),
            ("Do you serve all of Port Wentworth?",
             "Yes, all of 31407 – the older streets near the refinery through to the newer subdivisions along Highway 21."),
        ],
    },
    {
        "slug": "bloomingdale-ga",
        "work": "drainage",
        "photo": "bloomingdale-rural-lot.jpg",
        "photo_alt": "House set well back on a large rural lot with a gravel track and open field",
        "name": "Bloomingdale",
        "plain": "Bloomingdale, GA",
        "zip": "31302",
        "lede": "The rural northwestern corner of Chatham County – bigger lots, older houses, and properties that handle their own drainage.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Bloomingdale,_Georgia" target="_blank" rel="noopener">Bloomingdale</a> is a small incorporated town on the northwestern edge of Chatham County, bordered by Port Wentworth, Pooler, the western edge of Savannah and Effingham County, with a population of 2,790 at the 2020 census. It was incorporated in 1974 and has stayed rural where everything east of it suburbanised. The pattern out here is different as a result: larger lots, a mix of older frame houses and manufactured homes, well and septic still common, and properties that manage their own stormwater rather than draining to a street system. Crawl spaces on large rural lots tend to hold more standing water and see less maintained grading than anything inside the city.',
        "note_head": "No storm sewer to take the water away",
        "note": "On a rural lot, water that pools against the house has nowhere to go except into the ground underneath it. Getting the grading and a drainage run right is often more than half of a lasting repair here – considerably more than it is in a neighborhood where the street takes the runoff away for you.",
        "focus": ["Standing water in crawl spaces on large rural lots", "Older frame houses on original pier foundations", "Grading and drainage as the primary fix, not an add-on"],
        "faqs": [
            ("Do you actually come out this far west?",
             "Yes. Bloomingdale is a straightforward run out Highway 80 past Pooler and it is inside our normal service area, not an outlying exception we charge extra for."),
            ("Can you relevel a manufactured or mobile home?",
             "Generally no, and it is better to say so. A manufactured home on a HUD-standard pier set is releveled by a manufactured-home specialist, which is a different trade with different equipment. Where a manufactured home has been placed on a permanent engineered foundation, that foundation is work we do – we will tell you which situation you are in at the inspection."),
            ("Do you serve all of Bloomingdale?",
             "Yes, all of Bloomingdale in 31302 and the surrounding rural west Chatham addresses."),
        ],
    },
    {
        "slug": "rincon-ga",
        "work": "driveway",
        "photo": "rincon-house-framing.jpg",
        "photo_alt": "New house under construction with the wood framing up before the exterior goes on",
        "name": "Rincon",
        "plain": "Rincon, GA",
        "zip": "31326",
        "lede": "Effingham County's largest city, up more than 160% since 2000 – almost entirely new houses on ground that was farm or timber a generation ago.",
        "facts": '<a href="https://en.wikipedia.org/wiki/Rincon,_Georgia" target="_blank" rel="noopener">Rincon</a> began as a railroad town after the South Bound Railroad laid track through in 1891, was incorporated in 1927, and still had barely a thousand residents in 1960. Growth took off in the 1980s with the arrival of the Savannah River Mill and easy access down to the interstates, and the population went from 2,697 in 1990 to 8,836 in 2010 to 10,934 in 2020, sitting near 11,900 now. Effectively every house in the subdivisions off Highway 21 stands on land converted from farm or timber within the last thirty years. This is the fill-settlement market in its purest form – the same thing that drives the work in Pooler, concentrated.',
        "note_head": "Effingham County, not Chatham",
        "note": "Rincon sits in Effingham County, so permitting goes through Effingham rather than Chatham. The ground is the same coastal-plain sand over clay with the same shallow water table, and the repairs are the ones we do in Pooler every week. It is the paperwork that changes, not the engineering.",
        "focus": ["Fill settlement under recent subdivision slabs", "Sunken driveways, garage aprons and patios", "Drainage undercutting new flatwork"],
        "faqs": [
            ("Do you cover Effingham County?",
             "Yes. Rincon is a normal part of the service area – it is closer to the north side of Savannah than several places inside Chatham County are."),
            ("My subdivision is only a few years old. Why is the concrete already cracking?",
             "Because the concrete is bearing on fill rather than undisturbed ground. Lots here are graded and filled before building, and fill that was not compacted to specification keeps consolidating under load for years. It shows up in the flatwork first because that is the thinnest, least reinforced concrete on the property."),
            ("Do you serve all of Rincon?",
             "Yes, all of Rincon in 31326, including the subdivisions off Highway 21 and the older center of town."),
        ],
    },
    {
        "slug": "springfield-ga",
        "work": "framing",
        "photo": "springfield-historic-corner.jpg",
        "photo_alt": "Old white timber building on a small-town street corner",
        "name": "Springfield",
        "plain": "Springfield, GA",
        "zip": "31329",
        "lede": "Effingham's county seat since 1799 – a small historic core with new subdivisions spreading out around it.",
        "facts": 'Springfield became the county seat in 1799, taking over from Ebenezer, the Salzburger settlement founded on Ebenezer Creek in 1734 about twenty-five miles up the river from Savannah, and was incorporated in 1838 – the history is set out by the <a href="https://www.georgiaencyclopedia.org/articles/counties-cities-neighborhoods/effingham-county/" target="_blank" rel="noopener">New Georgia Encyclopedia</a>. The town keeps a small older core of historic frame houses around the courthouse while newer residential growth spreads outward as Effingham absorbs commuters from the Savannah metro. Those two halves need opposite work: the old frame houses stand on original piers over crawl spaces well past a century of service, and the new ones stand on fill.',
        "note_head": "The county seat is a two-era town",
        "note": "Springfield is small enough that people expect one answer for the whole town, and there is not one. A house near the courthouse and a house in a subdivision two miles out have essentially nothing in common structurally – different foundations, different soil preparation, different failure modes, different repairs.",
        "focus": ["Century-old pier foundations in the historic core", "Fill settlement in the newer subdivisions", "Crawl space moisture under original, pre-code framing"],
        "faqs": [
            ("Is Springfield too far out for you?",
             "No. It is a straight run up Highway 21 from Savannah through Rincon, and Effingham County is a normal part of the service area rather than an occasional trip."),
            ("What is different about an older county house compared with one in the city?",
             "Mostly the water. Rural and small-town properties usually manage their own drainage rather than feeding a municipal storm system, and many are on well and septic, which adds a second set of things that keep the ground near the house wet. The framing problems are the same ones – it is the cause upstream of them that differs."),
            ("Do you serve all of Springfield?",
             "Yes, all of Springfield in 31329, from the historic streets near the courthouse to the newer developments on the edge of town."),
        ],
    },
    {
        "slug": "hinesville-ga",
        "work": "level",
        "photo": "hinesville-brick-home.jpg",
        "photo_alt": "Single-story brick home with a lawn and attached garage, typical of the area's rental housing",
        "name": "Hinesville",
        "plain": "Hinesville, GA",
        "zip": "31313",
        "lede": "Liberty County's seat and Fort Stewart's home town – a rental-heavy housing stock that changes hands faster than anywhere else in the region.",
        "facts": 'Hinesville became the seat of Liberty County in 1837 and was incorporated in 1916, but the event that made the modern town was 1940, when 280,000 acres next door were taken for what became Fort Stewart – the largest Army installation east of the Mississippi, today supporting around 16,000 troops. The <a href="https://www.georgiaencyclopedia.org/articles/counties-cities-neighborhoods/hinesville/" target="_blank" rel="noopener">New Georgia Encyclopedia</a> traces how the base drove the town\'s growth to the 34,891 residents counted in 2020. That history matters structurally in one specific way: a large share of the housing is rental that turns over on posting cycles, so problems get reported late, by a tenant, after several seasons of getting worse.',
        "note_head": "A landlord's inspection beats a tenant's complaint",
        "note": "The cheap version of this work is the one booked when a floor first feels soft underfoot. The expensive version is the one booked when a joist has already gone. For rental property changing hands every couple of years, a scheduled look under the house between tenancies costs nothing and catches it while it is still the cheap version.",
        "focus": ["Sagging floors reported late in rental property", "Original crawl space framing in mid-century housing", "Moisture damage found between tenancies"],
        "faqs": [
            ("Do you work with landlords and property managers?",
             "Yes, and the between-tenancies window is the easiest time to do it – the house is empty, access is straightforward, and the work does not have to be scheduled around anyone living there. The written findings are also the document you want if a tenant later raises the issue."),
            ("Is Hinesville too far from Savannah?",
             "It is around forty miles down US-84 and I-95, roughly three quarters of an hour, and it is a regular part of the service area. We schedule Liberty County visits together rather than treating each one as a special trip."),
            ("Do you serve all of Hinesville?",
             "Yes, all of Hinesville in 31313 and the surrounding Liberty County addresses. Work on Fort Stewart itself goes through the installation's own contracting process, not through us."),
        ],
    },
]

# Geographic adjacency for the "We also work in these areas" block. Picking the
# first three from the list would put the same three on all eighteen pages;
# these are the places a reader in that area would actually recognize as next
# door, which is also the internal-linking pattern that makes sense to a crawler.
NEAR = {
    "downtown-savannah-ga":   ["midtown-savannah-ga", "thunderbolt-ga", "garden-city-ga"],
    "midtown-savannah-ga":    ["downtown-savannah-ga", "southside-savannah-ga", "isle-of-hope-ga"],
    "southside-savannah-ga":  ["georgetown-ga", "midtown-savannah-ga", "isle-of-hope-ga"],
    "georgetown-ga":          ["southside-savannah-ga", "richmond-hill-ga", "pooler-ga"],
    "isle-of-hope-ga":        ["thunderbolt-ga", "southside-savannah-ga", "skidaway-island-ga"],
    "thunderbolt-ga":         ["isle-of-hope-ga", "whitemarsh-island-ga", "downtown-savannah-ga"],
    "whitemarsh-island-ga":   ["wilmington-island-ga", "thunderbolt-ga", "tybee-island-ga"],
    "wilmington-island-ga":   ["whitemarsh-island-ga", "skidaway-island-ga", "tybee-island-ga"],
    "skidaway-island-ga":     ["isle-of-hope-ga", "wilmington-island-ga", "southside-savannah-ga"],
    "tybee-island-ga":        ["wilmington-island-ga", "whitemarsh-island-ga", "thunderbolt-ga"],
    "garden-city-ga":         ["port-wentworth-ga", "pooler-ga", "downtown-savannah-ga"],
    "port-wentworth-ga":      ["garden-city-ga", "pooler-ga", "rincon-ga"],
    "pooler-ga":              ["port-wentworth-ga", "bloomingdale-ga", "garden-city-ga"],
    "bloomingdale-ga":        ["pooler-ga", "port-wentworth-ga", "rincon-ga"],
    "richmond-hill-ga":       ["georgetown-ga", "southside-savannah-ga", "hinesville-ga"],
    "rincon-ga":              ["springfield-ga", "port-wentworth-ga", "pooler-ga"],
    "springfield-ga":         ["rincon-ga", "port-wentworth-ga", "bloomingdale-ga"],
    "hinesville-ga":          ["richmond-hill-ga", "georgetown-ga", "pooler-ga"],
}

# Hub grouping, and the order the pages are listed in everywhere.
GROUPS = [
    ("Savannah proper", "The city itself, from the historic core out to the Southside.",
     ["downtown-savannah-ga", "midtown-savannah-ga", "southside-savannah-ga", "georgetown-ga"]),
    ("The islands and the riverside", "Tidal ground, salt air, and the shallowest water table in the county.",
     ["isle-of-hope-ga", "thunderbolt-ga", "whitemarsh-island-ga", "wilmington-island-ga",
      "skidaway-island-ga", "tybee-island-ga"]),
    ("West Chatham", "Port-side industry, mid-century workforce housing, and the fastest new build in Georgia.",
     ["garden-city-ga", "port-wentworth-ga", "pooler-ga", "bloomingdale-ga"]),
    ("Beyond Chatham County", "Bryan, Effingham and Liberty – same coastal-plain soil, different permitting.",
     ["richmond-hill-ga", "rincon-ga", "springfield-ga", "hinesville-ga"]),
]

ORDER = [slug for _, _, slugs in GROUPS for slug in slugs]
PAGES.sort(key=lambda a: ORDER.index(a["slug"]))
BY_SLUG = {a["slug"]: a for a in PAGES}
assert len(PAGES) == len(ORDER) == len(NEAR), "PAGES, ORDER and NEAR must cover the same areas"


def build(page):
    url = f"{SITE}/service-areas/{page['slug']}.html"
    title = f"Foundation Repair in {page['plain']} ({page['zip']})"
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

    work_photo, work_alt = WORK_SHOTS[page["work"]]
    others = [BY_SLUG[s] for s in NEAR[page["slug"]]]
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
            <img src="../images/{work_photo}" alt="{work_alt}" loading="lazy" width="1200" height="675">
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

    def card(a):
        return f'''        <div class="service-card has-photo">
          <div class="card-photo"><img src="../images/{a["photo"]}" alt="{a["photo_alt"]}" loading="lazy" width="1200" height="675"></div>
          <div class="card-body">
            <h3><a href="{a["slug"]}.html" style="color:inherit">{a["name"]}</a></h3>
            <p>{a["lede"]}</p>
            <a class="link" href="{a["slug"]}.html">Foundation repair in {a["name"]} →</a>
          </div>
        </div>'''

    groups = "\n".join(f'''
  <section{' class="section-alt"' if i % 2 else ''}>
    <div class="container">
      <div class="section-head">
        <h2>{title}</h2>
        <p class="muted">{blurb}</p>
      </div>
      <div class="service-grid">
{chr(10).join(card(BY_SLUG[s]) for s in slugs)}
      </div>
    </div>
  </section>''' for i, (title, blurb, slugs) in enumerate(GROUPS))

    schemas = [breadcrumb([("Home", f"{SITE}/"), ("Service Areas", None)])]
    body = f'''
  <section class="page-hero" style="background-image:linear-gradient(180deg, rgba(11,26,41,.58), rgba(11,26,41,.82)), url(&quot;../images/savannah-historic-home.jpg&quot;)">
    <div class="container">
      <div class="breadcrumbs"><a href="../index.html">Home</a> / Service Areas</div>
      <h1>Service Areas – Savannah &amp; the Lowcountry</h1>
      <p class="lede">Eighteen areas, and genuinely different foundation problems in each. Historic piers downtown, salt and shallow groundwater on the islands, fill settlement out west – written up one place at a time.</p>
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
        <p class="muted">Chatham County plus Bryan, Effingham and Liberty. Each page covers what actually fails in that specific place and why – the construction era, the soil and the moisture conditions are not the same from one side of the county to the other.</p>
      </div>
    </div>
  </section>
{groups}

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Not Listed?</span>
          <h2>Somewhere we haven't written up yet</h2>
          <p>Eighteen pages covers the Savannah metro and the towns around it, but it is not every address in four counties. Smaller places in between – Vernonburg, Montgomery, Guyton, Ellabell, Pembroke – are usually still a yes.</p>
          <p>We would rather tell you plainly that somewhere is outside what we cover than take the call and then not turn up, so ask.</p>
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

    return (head(D, "Service Areas – Savannah &amp; the Lowcountry, GA",
                 "Foundation repair and crawl space work across 18 areas – Savannah, the islands, Tybee, Pooler, Port Wentworth, Richmond Hill, Rincon and Hinesville, GA.",
                 url, schemas)
            + header(D) + body + footer(D))


if __name__ == "__main__":
    for pg in PAGES:
        write(f"service-areas/{pg['slug']}.html", build(pg))
    write("service-areas/index.html", build_hub())
    print(f"\n{len(PAGES)} location pages + hub generated")
