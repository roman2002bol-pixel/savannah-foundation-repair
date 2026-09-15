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
- [ ] `free-inspection.html` — the main conversion page (form + what happens on an inspection)
- [ ] `about.html`
- [ ] `contact.html`
- [ ] `faq.html`
- [ ] `service-areas/index.html` — areas hub
- [ ] `privacy-policy.html`
- [ ] `terms.html`

**Service pages (5)**
- [ ] `services/crawl-space-repair.html`
- [ ] `services/foundation-piering.html`
- [ ] `services/concrete-slab-leveling.html`
- [ ] `services/foundation-crack-repair.html`
- [ ] `services/crawl-space-encapsulation.html`

**Location pages — Phase 1 (6)** — each needs real per-location research first
- [ ] `service-areas/downtown-savannah-ga.html` (31401)
- [ ] `service-areas/pooler-ga.html` (31322)
- [ ] `service-areas/richmond-hill-ga.html` (31324)
- [ ] `service-areas/skidaway-island-ga.html` (31411)
- [ ] `service-areas/wilmington-island-ga.html` (31410)
- [ ] `service-areas/georgetown-ga.html` (31419)

**Assets / supporting**
- [x] `css/style.css` — re-themed palette + type
- [x] `js/main.js` — re-branded, multi-form fix applied
- [x] `images/foundation-inspection-savannah.jpg` — hero
- [ ] one photo per service page (5)
- [ ] logo (`images/logo.svg`) — currently a text `SFR` monogram mark
- [ ] `llms.txt`
- [ ] `robots.txt` + `sitemap.xml`

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
5. `services/crawl-space-encapsulation.html` — vapour barrier + dehumidifier

Deliberately NOT built as separate pages (near-duplicate intent — would be
thin/doorway content): "cracked foundation repair" (= #4), "sinking /
settlement foundation repair" (= #2), "house / structural foundation
repair" (= homepage), "basement waterproofing" (wrong market entirely).

**Location pages — Phase 1 (not yet built):** Downtown/Historic Savannah
31401, Pooler 31322, Richmond Hill 31324, Skidaway Island 31411,
Wilmington Island 31410, Georgetown 31419. Each needs real per-location
research before writing (see skill). Phase 2 later.

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
