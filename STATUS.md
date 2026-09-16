# STATUS — Savannah Foundation Repair Co

Breadcrumb log. Read before starting a session, update after finishing one.

---

## Site identity

- **Brand:** Savannah Foundation Repair Co
- **Domain:** `savannahfoundationrepairco.com` — verified unregistered
  2026-09-14, Roman confirmed this is the choice and is registering it.
  Recommended registrar: Cloudflare Registrar (~$10.44/yr, at-cost renewal,
  WHOIS privacy included).
- **Naming note (known, accepted):** a live lead-gen competitor operates as
  **"Savannah Foundation Repair Service"** (`savannahfoundationrepairservice.com`)
  — same city, same niche, same lead-gen business model, name differing only
  in the last word. This was flagged in detail before the decision and Roman
  chose this name anyway with the risk explicitly on the table. Do not
  re-litigate it; do keep the two straight when doing competitor research.
- **Market reality:** crawl-space / slab market, NOT a basement market — see
  `CLAUDE.md`.

## Facts still needed before real content goes live — DO NOT FABRICATE

- [ ] Real local phone number (912 area code)
- [ ] Real contact email (currently placeholder `info@savannahfoundationrepairco.com`)
- [ ] Who actually fulfils a lead — determines what About/team copy may say.
      **No named "team members" until a real person exists to name.**
- [ ] Licensing / insurance / bonding specifics — omit entirely until real
- [ ] **Warranty and financing claims.** Roman's source plan proposed
      "Lifetime Transferable Warranty" and "0% Financing for 12–60 Months"
      as hero trust bars. These are *factual commercial claims a customer
      would rely on* and cannot be published until a real fulfilling
      contractor actually offers them. Left out of the build for now;
      replaced with claims that are true for a lead-gen site (free
      inspection, no obligation, local coverage).

## Market research done (2026-09-14)

Niche Validator (Roman, live data): **Foundation Repair Savannah = 79/100**
— ~220 monthly searches core terms, $16.46 avg CPC (top bids ~$60),
$1,600–$4,100 average ticket, weakest map-pack business has 9 reviews and
2 of 3 map-pack businesses have no real website.

Live SERP checks run for each planned service page:

| Sub-niche | What's actually ranking | Read |
|---|---|---|
| Foundation repair (head term) | Yelp/Angi/HomeAdvisor directories + national franchise landing pages (Ram Jack, Groundworks/Mount Valley, Atlas Piers) | Soft — directories in top 5 |
| Crawl space repair / sagging floor joists | Lowcountry (strong, since 1996), Groundworks, plus small players | Medium |
| Concrete leveling / polyjacking | Mostly franchise network pages (PolyLevel, Foamjection, PolyLift) | Soft-medium |
| Crawl space encapsulation | **Most contested** — several dedicated local EMD-ish sites already exist (savannahcrawlspacepros.com, healthy-crawlspace.com, healthy-crawlspace-savannah.com, islandscrawlspace.com) | Hardest of the four |

Real, established local contractor for a future lease/rev-share
conversation: **Lowcountry Foundation and Crawl Space Repair**
(lowcountryfoundationrepair.com, since 1996). Real company — never claim
any affiliation with them on the site.

Cost data point found in research: floor joist repair in Savannah runs
~$1,285–$4,875 (consistent with the $1,600–$4,100 ticket estimate).

## Full page plan — build checklist

Legend: `[x]` built and verified · `[ ]` not built yet (link 404s until it is)

**Core pages (8)**
- [x] `index.html` — homepage / hub
- [x] `free-inspection.html` — the main conversion page (form + what happens on an inspection)
- [x] `about.html`
- [x] `contact.html`
- [x] `faq.html`
- [x] `service-areas/index.html` — areas hub
- [x] `privacy-policy.html`
- [x] `terms.html`

**Service pages (5)**
- [x] `services/crawl-space-repair.html`
- [x] `services/foundation-piering.html`
- [x] `services/concrete-slab-leveling.html`
- [x] `services/foundation-crack-repair.html`
- [x] `services/crawl-space-encapsulation.html`

**Location pages (18)** — each needed real per-location research first, and
the `facts` block on each cites the source it came from

*Savannah proper*
- [x] `downtown-savannah-ga.html` (31401) — historic brick/tabby piers, city review
- [x] `midtown-savannah-ga.html` (31405) — Ardsley Park 1909–30s, Casey Canal basin
- [x] `southside-savannah-ga.html` (31406) — Windsor Forest, late-50s planned suburb
- [x] `georgetown-ga.html` (31419) — 1970s–80s build-out

*The islands and the riverside*
- [x] `isle-of-hope-ga.html` (31406) — 19th-c river cottages, oldest piers outside downtown
- [x] `thunderbolt-ga.html` (31404) — separate town, shrimp port, own permitting
- [x] `whitemarsh-island-ga.html` (31410) — 1980s–2000s, marsh-edge lots, flood risk
- [x] `wilmington-island-ga.html` (31410) — 1960s–70s pier-and-beam, salt corrosion
- [x] `skidaway-island-ga.html` (31411) — The Landings, 1972+, Association review
- [x] `tybee-island-ga.html` (31328) — barrier island, BFE 9ft+2ft, FEMA elevation grants

*West Chatham*
- [x] `garden-city-ga.html` (31408) — 1939 workforce housing, port-side filled ground
- [x] `port-wentworth-ga.html` (31407) — +344% since 2000, split old core / new fill
- [x] `pooler-ga.html` (31322) — new construction on fill, slab market
- [x] `bloomingdale-ga.html` (31302) — rural west, no storm sewer, own drainage

*Beyond Chatham County*
- [x] `richmond-hill-ga.html` (31324) — Bryan County
- [x] `rincon-ga.html` (31326) — Effingham, +163% since 2000
- [x] `springfield-ga.html` (31329) — Effingham county seat, two-era town
- [x] `hinesville-ga.html` (31313) — Liberty County, Fort Stewart, rental-heavy

**Assets / supporting**
- [x] `css/style.css` — re-themed palette + type
- [x] `js/main.js` — re-branded, multi-form fix applied
- [x] `images/foundation-inspection-savannah.jpg` — hero
- [ ] one photo per service page (5)
- [ ] logo (`images/logo.svg`) — currently a text `SFR` monogram mark
- [x] `llms.txt`
- [x] `robots.txt` + `sitemap.xml`

**Live preview:** https://roman2002bol-pixel.github.io/savannah-foundation-repair/
(public repo, temporary host — production is Cloudflare once the domain is bought)

## Planned architecture

**Core pages:** Home, About, Free Structural Inspection, Contact, FAQ,
Privacy Policy, Terms, Service Areas hub.

**Service pages (5 — at the skill's 1–6 cap, each distinct by method and
equipment, which is how a real contractor actually prices them):**
1. `services/crawl-space-repair.html` — sagging floors, rotted joists, jacks
2. `services/foundation-piering.html` — helical/push piers, underpinning
3. `services/concrete-slab-leveling.html` — polyjacking / foam lifting
4. `services/foundation-crack-repair.html` — crack sealing, structural
5. `services/crawl-space-encapsulation.html` — vapor barrier + dehumidifier

Deliberately NOT built as separate pages (near-duplicate intent — would be
thin/doorway content): "cracked foundation repair" (= #4), "sinking /
settlement foundation repair" (= #2), "house / structural foundation
repair" (= homepage), "basement waterproofing" (wrong market entirely).

**Location pages (18, all built):** grouped as Savannah proper / the
islands and the riverside / West Chatham / beyond Chatham County. The
grouping is not decoration -- it maps onto four genuinely different
foundation stories (old piers, salt and tide, fill settlement, other
counties' permitting).

**Why all 18 shipped at once rather than in phases.** The skill's default
is a phased location rollout, because a pile of near-identical town pages
published in one day is exactly the scaled-content pattern Google acts on.
Roman's argument for going wide immediately was that Savannah is not
Dallas: the realistic list of distinct places in and around this metro is
about eighteen, not two hundred, so "all of them" is a complete map of a
small market rather than a generated long tail. That holds, with one
condition attached -- each page had to earn its place with researched,
genuinely different content (build era, soil, foundation type, failure
mode, permitting authority), not a template with the name swapped. That
condition was met: every `facts` block links the source it came from, and
no two pages share a focus list, a note, or an FAQ. The site is also not
indexed yet, so all 31 pages go live together regardless.

---

## Log

### 2026-09-14 — Project scaffolded
- Brand and domain decided (see above), after a full 3-step vetting pass
  that rejected "Foundation Repair of Savannah" (collides with the real,
  Yelp-listed "Solid Foundation Repair of Savannah").
- Folder created, `microsite-agent` skill copied in, git repo initialised.
- `css/style.css` and `js/main.js` adapted from the tree-removal site:
  shared structure kept (explicitly fine per the skill), palette and type
  fully re-themed to slate navy + safety orange / Barlow + Inter so the two
  sites don't read as a matched set. Verified zero tree-site strings remain
  in either shared asset.
- Market research + live SERP checks logged above.
- **Next:** homepage build, then the 5 service pages, then Phase-1
  location research.

### 2026-09-15 — Site built out: all 19 pages live

Built with three one-off generator scripts (`build_pages.py` shared
templates + `build_services.py` / `build_areas.py` / `build_core.py`), per
the skill's rule that structure should be generated while content stays a
required per-page input.

- 5 service pages — each with its own situations list, method explanation,
  cost drivers and 3 FAQs. Genuinely per-trade content, not one template
  with the service name swapped.
- 6 location pages + areas hub — each built on the researched facts logged
  above, each linking out to its real source (Wikipedia for place history,
  savannahga.gov and landings.org for the two regulatory notes).
- 6 core pages: free-inspection (main conversion page), about, contact,
  faq (10 Q&As), privacy-policy, terms.
- llms.txt, robots.txt, sitemap.xml (19 URLs).

Verification, all clean: broken-link check, FAQ-schema match on 13 pages,
and the new markup-contract check across all 19 files. Rendered-page audit
run on homepage + a service page: zero low-contrast text, no oversized
SVGs, no horizontal overflow. Mobile QA at 375px: nav toggle, nav close,
accordion label and mobile action bar all confirmed genuinely visible via
getBoundingClientRect (not just by dispatching clicks), and the action
bar's 64px height matches body padding-bottom exactly.

**Honesty position held throughout:** no warranty claim, no financing
claim, no licensing/insurance/bonding claim, and no named team members —
none of those are true of anyone yet. The About page says plainly that
there is no walk-in office rather than implying one.

**Still open before this can go live for real:** real phone number, real
email inbox, a form backend (currently mailto fallback,
`data-endpoint-ready="false"`), the domain purchase, service-page photos,
and a logo beyond the SFR monogram.

### 2026-09-16 — Homepage restructure + location coverage to 18 areas

**Homepage, on Roman's notes:** removed the orange `::before` rule in front
of every eyebrow label (deleted from the stylesheet, so it cannot come back
on a later page). Services moved directly under the hero with the trust
strip after it, background classes swapped so the alternation still holds.
Removed the decorative outline icons -- four in the trust strip, three dark
tiles in How It Works, three on the inspection page -- keeping the numbered
step badges. All 13 FAQ questions now render on the homepage.

**FAQ is now single-sourced.** `index.html` is hand-written, so its FAQ
could previously drift from `faq.html`. Both are now stamped from `FAQS` in
`build_core.py`, visible markup and FAQPage JSON-LD together, into marker
comments in `index.html`. The same mechanism stamps the 18 area chips into
the homepage service-area block.

**`sitemap.xml` and the `llms.txt` area list are now generated** by
`build_meta.py` from the same data the pages are built from. They were
hand-maintained, which meant adding a page and forgetting the sitemap was
a matter of time.

**12 new location pages** (see the checklist above), each with researched
facts and an outbound authority link: Midtown/Ardsley Park, Southside,
Isle of Hope, Thunderbolt, Whitemarsh Island, Tybee Island, Garden City,
Port Wentworth, Bloomingdale, Rincon, Springfield, Hinesville. Nearby-area
links are now real geographic adjacency (`NEAR` in `build_areas.py`)
instead of the first three in the list, which had put the same three
neighbours on every page.

**12 new photos**, Pexels, each downloaded once at the final 1200x675
rather than re-encoded. No AI-looking images and no third-party business
names on people or equipment.

**Two honest scope limits written into the new pages** rather than left
vague: we do not raise houses to flood elevation (Tybee) and we do not
relevel manufactured homes on HUD pier sets (Bloomingdale). Both say so
plainly and say who does.

**Language pass:** 116 British spellings removed from a Georgia site --
levelling, stabilisation, vapour, neighbourhood, galvanised, storey,
ageing, localised, recognise.

All four checkers clean across 31 pages. Honesty sweep re-run: the only
"warranty" on the site is a reference to the homeowner's own builder
warranty on the Port Wentworth page.

### 2026-09-16 (later) — Homepage reworked toward a reference design

Roman sent screenshots of a pool-builder site and asked for three things.

**Hero:** eyebrow pill above the H1, location line in `--orange-light`
(#ff8a3d — the body orange only just clears 3:1 on the navy). Found and
fixed the `.hero` gradient, which was still the tree site's green and only
looked right here because the inline style overrode it.

**Proof band replaces the trust strip, back in front of Services.** Two
columns plus a photo with a floating badge, then four stat boxes. The
reference's stats are 18+ years / 900+ jobs / lifetime warranty — all
untrue of us and not invented. Ours are 4 counties, 18 areas, 5 repairs,
1–3 days: same visual weight, every figure checkable against the site.
See the skill's "take the form, never the unverifiable claims".

**Services is now a tab showcase** — tab rail plus a dark photo panel per
service with an accent heading, blurb, four scope points and two CTAs.
Data lives in `build_services.TABS`, stamped into `index.html` through the
marker mechanism, and every point restates something already on that
service's own page. Keyboard accessible; ships with no `[hidden]`, so
without JS all five stack instead of leaving four dead buttons.

Also: homepage `areaServed` had still listed the original six areas, now
16 entries. Five unused `card-*.jpg` crops deleted. Assets at `?v=5`.
All five checkers clean; mobile verified at 375px via DOM geometry.
