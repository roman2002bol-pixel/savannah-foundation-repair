---
name: microsite-agent
description: |
  Architecture, SEO, and honesty rules for building hub-and-spoke local-SEO
  microsites (the "3-layer" model: core pages, 1-6 service pages, a phased
  set of location pages). Distinct from web-dev-agent (Project1's detailing
  sites, Roman's own businesses) because these sites may route/rent leads to
  a third-party contractor, which raises the bar on trust-claim honesty.
  Trigger whenever building or editing a site under Microsites/.
---

# Microsite Agent — Local-SEO Hub-and-Spoke Playbook

This is the complete, detailed playbook for building one of these sites
end to end — architecture, SEO, honesty rules, and every concrete
workflow (naming, images, location research, logo, verification,
temporary hosting) refined across the actual build of Savannah Tree
Removal Co (2026-09-07 through 2026-09-09). The goal of this file is
that a session can read it and execute a build without re-deriving any
of this from scratch or from re-reading old transcripts. Where a
workflow has a runnable script, it's in `scripts/`; where it has a
worked example, it's in `references/`.

## Where this idea came from, and what got filtered out

This playbook is based on several "rank and rent" / microsite-blueprint
concepts sourced from creator-research content about paid SEO courses
(core+service+location pages, hub-and-spoke internal linking, a
CLAUDE.md+STATUS.md continuity system, competitor recon, per-location
research before writing copy). **Every time content like this gets
pasted, extract only the SEO-architecture-sound parts and explicitly
reject the rest** — see "Filtering rank-and-rent source material" below
for the specific pattern and worked examples of what got kept vs.
rejected across three separate pasted sources so far.

## The 3-layer architecture

1. **Core pages (~8)** — Home, About, Contact, Free Estimate/Quote, Service
   Areas (hub page listing all locations), Privacy Policy, Terms, FAQ.
   These exist to look like a real, legitimate local business, not to rank
   on their own.
2. **Service pages (hard cap: 1–6)** — one per genuinely distinct service.
   Do not create a standalone page (or a standalone site) for a narrow,
   situational long-tail like "emergency tree removal" if keyword tools
   show ~0 search volume for the exact phrase — that volume is real but
   fragmented across dozens of situational phrasings tools don't capture
   ("tree fell on house", "storm cleanup savannah", etc.). Fold it into
   the broader service's page instead of treating zero measured volume as
   zero demand. See `references/niche-research.md` for the full reasoning.
3. **Location pages (phased, not all at once)** — one per real neighborhood/
   suburb, **not** one page per service-per-location. A location page
   covers all services for that area; a service page covers that service
   across the whole metro and links out to relevant areas. This is the
   actual hub-and-spoke shape — a full service×location matrix is a
   doorway-page pattern, not this pattern.

## Location-page rollout is phased, not all-at-once

Publishing 20–30 near-identical location pages the day a domain goes live
is a real scaled-content-abuse risk signal, not just a style preference —
Google's own guidance explicitly targets exactly this pattern. Roll out in
phases:

- **Phase 1 (launch)**: core pages + service pages + a **small, real** set
  of location pages — enough to prove the model, few enough that each one
  can carry genuine local detail (real streets/landmarks/neighborhood
  character), not a copy-pasted paragraph with the city name swapped.
- **Phase 2 (once Phase 1 is indexed and stable — typically a few weeks)**:
  add the remaining locations, now that the domain has an established,
  legitimate footprint to expand from.

For this site (Savannah, GA / tree removal), Phase 1 locations are:

| Neighborhood | ZIP |
|---|---|
| Pooler, GA | 31322 |
| Richmond Hill, GA | 31324 |
| Wilmington Island | 31410 |
| Skidaway Island (The Landings) | 31411 |
| Georgetown (Savannah) | 31419 |
| Isle of Hope | 31406 |
| Historic District / Downtown Savannah | 31401 |

Phase 2 (do not build yet) adds the remaining smaller suburbs once Phase 1
is indexed and ranking.

## Non-negotiable honesty rules

These are the things that must never be reintroduced without a real fact
behind them — this list grew from two sources (the original filtered
course material, and a rank-and-rent video pasted 2026-09-08 that
described GBP video-verification fraud and other gray-hat tactics):

- **Never publish a specific licensing/insurance/bonding claim
  ("Fully licensed, bonded, and covered by $2,000,000 general liability
  insurance") unless it is literally true for the real contractor doing the
  work right now.** This is not a placeholder like a fake phone number —
  it's a factual claim a real customer will rely on. If the real numbers
  aren't confirmed yet, use only what's actually true (e.g. "Locally
  owned and operated", "Free, no-obligation estimates") and flag the gap
  explicitly to the owner rather than inventing specifics. The moment a
  fact IS confirmed (e.g. "10 years of experience, fully licensed" —
  confirmed 2026-09-08 for this site), apply the exact confirmed wording
  — not embellished, not rounded up — across every page in one pass (see
  "Confirmed-fact propagation" below), and record it in STATUS.md with
  the date it was confirmed.
- **No cross-linking between sibling sites in `Microsites/`.** Each site
  must look, to Google, like a completely independent business. Any two
  sites in this folder linking to each other is a textbook private-link-
  network signal and risks Google devaluing or penalizing the whole set at
  once. Internal linking (hub-and-spoke) is only ever within one site.
- **Never fake a Google Business Profile verification, review, or Q&A.**
  A pasted video (2026-09-08) described staging a vehicle with a car
  magnet and tools to pass GBP's AI video-verification, disabling precise
  location to spoof geolocation during that verification, and writing
  site copy "as if I am the brand" with an invented "20 years experience"
  before any real business exists behind it. All of this is fraud against
  Google's verification system or fabricated trust claims — reject it
  outright, do not implement any version of it, and say so plainly to the
  owner when this kind of content gets pasted (see the filtering section).
- **Never use a real photo that shows a third-party competitor's
  branding** (a company name/logo visible on a worker's clothing, a
  vehicle, or equipment) — see "Image sourcing workflow" below for the
  exact screening step that catches this before an image gets used.
- **Never claim a specific regulatory/HOA fact without sourcing it.**
  Location pages will often want to mention something like "this area
  requires a permit" or "this HOA has a tree policy" because it's exactly
  the kind of genuine, differentiating local detail that makes a page not
  read as templated. That's good instinct, but the fact itself has to be
  real — WebSearch it and cite what you found before publishing it (see
  "Location-page research workflow").

## Brand name & domain vetting — MANDATORY before finalizing any name

**This did not exist as a formal step until 2026-09-09, after "Savannah
Tree Pros" (chosen 2026-09-07 without this check) turned out to already
belong to two live, active competitor sites** — `savannahtreepros.com`
and `savannahgatreepros.com`, both real tree-service lead-gen operations
with near-identical positioning to the site being built. This cost a
full rebrand across 19 HTML files, the AI-generated logo (which had to
be deleted — the old name was traced into its vector artwork, not
editable text), and the favicon. That mistake is now a mandatory gate:
**never finalize a brand name for one of these sites without doing all
three checks below first**, whether the name was your own idea or came
from a pasted "recommendation."

1. **WebFetch the exact matching domain(s) directly** — `https://
   {candidatename}.com` and any obvious variant (`.net`, a "ga"/state-
   abbreviation-inserted version, a common misspelling). Ask the fetch
   to describe what it finds: is this a live business site, and if so
   what services/area does it claim? A domain that resolves to an active
   competitor in the same niche and metro is disqualifying — full stop,
   don't rationalize around it ("it's just aggressive, we could still...").
2. **WebSearch the exact candidate business name** (in quotes) + the
   metro name. Look for an existing real business or GBP listing using
   that name — not just a domain. A name can be "available" as a domain
   while already belonging to an unregistered-domain local business
   found only via Maps/Yelp/Facebook; the search catches that case a
   domain check alone would miss.
3. **WebFetch each serious candidate's proposed domain to check DNS
   resolution** (a fetch that fails with `ENOTFOUND` / similar is a
   *soft signal* the domain is unregistered — not proof. A domain can be
   registered with no hosting attached and still fail to resolve.
   **Always tell the owner to do one final check on an actual registrar
   (Namecheap/GoDaddy) before spending money** — don't imply your check
   is a substitute for that.

**When multiple candidates survive all three checks, don't silently pick
one yourself** — this is a costly, identity-defining decision (domain
purchase, eventual GBP creation, printed materials down the line). Lay
out the verified options with their real tradeoffs (e.g. "cleanest
option vs. strongest exact-match keyword but a soft collision with an
existing similarly-named competitor") and let the owner choose. This
mirrors the general rule about not re-litigating decisions that are
genuinely the owner's to make — a brand name is squarely in that
category, doubly so after getting one wrong already.

**If a rename does become necessary** (name already chosen and built,
then found to collide), the mechanical fix is a single scripted pass —
see the Python one-liner pattern used for the 2026-09-09 rename:
```python
content = content.replace('Old Brand Name', 'New Brand Name')
content = content.replace('oldbranddomain.com', 'newbranddomain.com')
# plus any monogram/favicon-initial change, then re-run both
# verification scripts (see below) before committing
```
**Grep the whole repo for the old name and the old domain across ALL file
types, not just `*.html`** — the 2026-09-09 rename pass here only swept the
HTML, and five days later `js/main.js` was still carrying the retired name
in two places, one of them genuinely damaging: the estimate form's
`mailto:` fallback was still addressed to `info@savannahtreepros.com`, and
`savannahtreepros.com` is a **live competitor's domain** — so any visitor
whose submission hit the mailto fallback would have emailed their own lead
straight to the competitor the rename existed to get away from. A stale
brand string in a JS string literal is not cosmetic; treat `*.js`, `*.css`,
`*.txt` (llms.txt!), and `*.md` as in scope every time:
```bash
grep -rn "Old Brand Name\|oldbranddomain" --include="*.html" --include="*.css" \
  --include="*.js" --include="*.txt" --include="*.md" .
```
(STATUS.md's historical entries are the one place the old name *should*
survive — that's the audit trail, leave those.)

Check specifically for: page `<title>`/meta/OG tags, canonical URLs,
every JSON-LD `"name"` field, header/footer wordmark text, the copyright
line, the contact email placeholder, **every user-facing string inside
`js/main.js` (mailto subject lines and target addresses, form status
messages)**, and the favicon's inline monogram
(if the favicon is an inline data-URI SVG with a text initials mark, its
literal text needs updating too — grep for it, don't assume). **Also
check whether the logo has the old name baked into its actual artwork**
(true for any AI-generated/traced logo, since that's rasterized/traced
shapes, not editable text) — if so, delete it and revert to the plain
text-based header treatment until a new logo is generated under the
correct name; do not leave a factually-wrong logo live even temporarily.

## Domain-specific facts still needed before real content goes live

Track these in `STATUS.md` — do not fabricate any of them in the meantime:
- Real business/brand name and domain (see vetting process above)
- Real local (912 area code, or the appropriate local area code) phone number
- Real contact email
- Real licensing/insurance details, if and when confirmed
- Who actually fulfills a lead once the site starts working (the owner
  themselves, or a specific contractor) — determines what "Team"/"About"
  content can honestly say

## Confirmed-fact propagation — when the owner confirms something

When the owner confirms a previously-unconfirmed fact (e.g. "the
contractor has 10 years of experience and holds all required licenses"
— confirmed 2026-09-08 for this site), do all three of these in the same
pass, not just the first:
1. **Apply the exact confirmed wording everywhere it belongs** — don't
   embellish ("10 years" doesn't become "over a decade of trusted
   service") and don't round up. For a fact this central, that usually
   means: homepage trust-strip, the shared footer paragraph + badge list
   (which appears on every page), and the About page if one exists.
   A single global find-and-replace across all HTML files is the right
   tool for this once you know every place the old/generic phrasing
   lived — don't hand-edit each file individually and risk missing one.
2. **Update STATUS.md's "Site identity" section** with the fact and the
   date confirmed, and remove/adjust the corresponding line in the open-
   questions list if this closes one out.
3. **Do not let this become a wedge to add unconfirmed adjacent claims.**
   "Licensed" confirmed does NOT mean it's now safe to also say "bonded"
   or "$2M insured" or name a specific certification — each of those
   needs its own separate confirmation.

## Page formula for a service page

1. **H1**: `[Exact Service] in Savannah, GA` (or the broader metro name —
   not a hyper-specific long-tail per the zero-volume note above).
2. **Opening paragraph**: direct answer to the implied query, natural
   keyword placement, not stuffed.
3. **Bulleted list of specific situations this service covers** — people
   scan for their own situation, not prose.
4. **Equipment/credibility signals** — real equipment names, real
   certifications, actually true statements only (see honesty rules above).
5. **Pricing factors** (not necessarily an exact price) — "How much does
   X cost in Savannah?" is a real, high-intent query; answer it with a
   real range and the factors that move it, never a bare "contact us."
6. **Hub-and-spoke links out** — to the relevant location pages ("We
   provide this across Pooler, Richmond Hill, ...") and back to the
   Service Areas hub.
7. **Full-bleed photo hero** (added as a pattern 2026-09-08): give the
   `.page-hero` section a dark-green-gradient-overlay background image
   using that page's own already-sourced service photo — see the exact
   CSS/inline-style pattern in "Image sourcing workflow" below. Don't
   source a second image just for the hero; reuse the page's existing one.

## Homepage engagement pattern: a "Check Your Area" hero CTA

Add a third hero button (alongside call and free-estimate) that links to
the Service Areas hub — e.g. `Check Your Area` → `service-areas/index.html`
(always the explicit `index.html`, matching this project's own internal-
link convention — a bare directory link like `service-areas/` will fail
`check_broken_links.py`, which resolves paths literally). This isn't
decorative: a visitor who clicks through to the areas hub goes deeper into
the site and spends longer on it than one who bounces after reading the
hero, and that's a genuine on-page-behavior signal (dwell time, pages per
session) separate from anything schema- or backlink-related. Cheap to add,
worth doing on every hub-and-spoke build's homepage by default.

## Outbound authority links — cite the actual source, not just the fact

Every location page already has to trace its claims back to real research
(see the workflow below) — the missing last step is **linking the claim to
its real source** directly in the page copy, not just having done the
research privately. Two tiers:

- **A specific regulatory/HOA/historical claim** → link straight to the
  actual governing body's own page (a city ordinance page, an HOA
  association's own policy announcement) — this is the highest-value case,
  since it's the exact primary source the claim came from. Example from
  this build: the Historic District page's tree-ordinance sentence links to
  `savannahga.gov`'s own Tree Ordinance Administration page; the Skidaway
  Island/Landings page's HOA-policy sentence links to `landings.org`'s own
  published policy announcement.
- **General place history/geography** → link the place name to its
  Wikipedia article (verify the exact article exists and title-cases/
  underscores correctly before using the URL — don't guess the slug).
- Mechanically: link the location/claim's first natural mention in the
  local-facts paragraph, `target="_blank" rel="noopener"` (visitor leaves
  the page, external site, standard treatment), and re-run
  `check_broken_links.py` after — it only checks internal paths, so an
  external link can't fail it, but a typo'd Wikipedia slug still won't
  resolve for a real visitor even though the checker stays silent about it.

This is a genuine E-E-A-T signal (the page visibly cites where its specific
claims come from, the same way a well-sourced article does) and it's
essentially free once the research step already happened — don't skip it
as a "nice to have" on a future build.

## Don't copy a fabricated "meet the team" section from a reference site

When benchmarking against another lead-gen site in the same rank-and-rent
space, a **named founder/team-member section with photos and job titles**
("Founder Mark Ellison", "Project Lead Denise Carter") is common — and on a
site with no real, staffed local office, it is very likely fabricated
identity, not a real team. This is the same category of problem as the
already-rejected "write copy as if I am the brand" tactic and the
already-rejected fake-review problem — inventing named people with
specific roles to manufacture trust is fabricating a fact a real customer
would reasonably rely on. **Do not add a team/founder section to one of
these sites until there's an actual real person or contractor to name
honestly.** Once a real fulfillment contractor is lined up, a truthful
version of this section (crediting the real business/technicians who
actually do the work) is a legitimate, valuable trust element — the
problem is inventing people, not naming real ones.

## Filtering rank-and-rent source material, worked example #4 (2026-09-14)

A long Skool community Q&A transcript ("Rank & Expand Academy") got pasted
covering a full exact-match-domain (EMD) microsite methodology. Applying
the filtering process above to it specifically:

**Kept:**
- Outbound authority links to Wikipedia/governing bodies for E-E-A-T (see
  above — this is the one genuinely new, adopted idea from this source).
- A hero "check availability/your area" CTA button to reduce bounce and
  deepen page views (see above).
- Practical tooling tip: **Cloudflare Registrar** ($10.44/yr .com, sold at
  cost, no renewal-year price jump, WHOIS privacy included) as a
  cost-effective domain registrar recommendation to pass along when an
  owner is about to buy a domain — this is neutral, useful consumer
  advice, not a gray-hat tactic.
- WhatConverts (call tracking with recordings/transcripts) and Vapi (AI
  phone answering) are legitimate, real tools **worth knowing about for
  later** — once a site is actually live and a real business wants to buy
  its leads, call tracking that proves lead source/quality is a genuine,
  honest value-add for that arrangement. Not needed for the initial build;
  don't wire these in speculatively before there's a paying lead-buyer.

**Explicitly rejected, by name:**
- **Buying or claiming an existing/abandoned Google Business Profile** (the
  transcript's Q8: "people sell them in niche Facebook groups for $200–
  $300"). This is a direct extension of the already-rejected "fake GBP
  verification" rule — a GBP is supposed to represent a real, specific
  business; buying or repurposing one to represent a different business is
  deceptive to both Google and to real customers who trust that listing.
  Never do this for one of these sites.
- **"Vary the naming conventions" / avoid a shared footer credit specifically
  to keep Google from spotting a coordinated network of sites** (the
  transcript's Q17, framed as avoiding a "footprint"). The existing
  no-cross-linking rule already exists for a legitimate reason (each site
  should stand as its own real business); explicitly optimizing to *evade
  detection* of coordinated site ownership is a different thing — it's
  detection evasion, not an honest architecture choice, and isn't something
  this skill will help implement. In practice this doesn't even come up:
  building each site with genuinely distinct research, prose, and identity
  (already the standing rule here) produces sites with no shared footprint
  as a side effect, without ever needing to think about it as evasion.
- **The "build 50 mediocre sites, keep the winners, prune the rest"
  portfolio philosophy** conflicts with this project's standing rules
  (phased location rollout, no thin/templated pages, real per-location
  research before publishing). Adopting the EMD/volume model's speed would
  mean giving up the things that make a single site defensible under
  Google's spam guidance. Not adopted — this playbook stays with fewer,
  higher-quality, honestly-differentiated sites.
- **Mass third-party indexing services (Omega Indexer)** — not rejected as
  dishonest, just unnecessary: a real, honestly-built site with a normal
  sitemap indexes fine through standard means. Not worth the added paid
  dependency for this build's scale.

## Location-page research workflow (the actual step-by-step)

This is the single most important workflow in this file — it's the
difference between a location page that's a genuine, defensible piece of
local SEO and one that's textbook thin/templated content Google
penalizes. **Do the research before writing a single word of location
page copy.**

1. **For each Phase-1 location, run 1-2 targeted WebSearches** looking
   for something *specific and true* to that place — not generic filler
   ("beautiful neighborhood with great trees"). Good search patterns
   that worked for this build:
   - `"{neighborhood}" {city} {state} history` — surfaces founding
     history, historic figures, notable eras (worked for Richmond Hill:
     turned up its Henry Ford history in one search).
   - `{HOA/community name} tree removal policy` or `... architectural
     review` — for any gated/HOA-governed area, there is very often a
     real, specific, sourceable policy (worked for The Landings on
     Skidaway Island: found an exact circumference threshold and
     approval-day schedule from the Association's own site).
   - `{city} protected tree ordinance permit` — for any area with a
     historic district or a reputation for canopy/tree culture, check
     whether there's an actual municipal ordinance (worked for
     Savannah's Historic District: found the real Landscape and Tree
     Protection Ordinance, permit requirement, and replacement-planting
     rule from the city's own site).
   - `{neighborhood} {city} population growth` / `new construction` —
     for fast-growing suburbs, real growth statistics are a genuine,
     citable differentiator (worked for Pooler: ~33% population growth
     since the 2020 census).
   - `{neighborhood} {city} marsh / waterfront / geography` — for
     coastal or waterfront areas, the real geographic character (barrier
     island, tidal marsh, flood exposure) is both true and relevant to
     the actual service (tree work near water/marsh access is genuinely
     different).
2. **Every claim that will appear on the page must trace back to
   something found in that research** — if a search comes up empty for
   a given location, that location either gets a more generic (but still
   honest) treatment, or isn't ready for Phase 1 yet. Never invent a
   "founded in [year]" story, a fake HOA rule, or a fake ordinance to
   fill the gap.
3. **Watch for adjacent-but-wrong facts** — e.g. a neighborhood that
   *sounds* like it's in the same county as the rest of the site's
   service area may not be (Richmond Hill, GA is in Bryan County, not
   Chatham County, despite being part of the same metro). State this
   correctly on that location's own page even if the site's generic
   sitewide copy says something broader — accuracy on the specific page
   matters more than sitewide phrasing consistency here.
4. **Write the page** using the researched facts as the core of the
   "why this area" section — see `references/example-location-page-
   generator.py` for the exact page shape (hero, local-facts two-col
   section with an optional "special note" callout for a regulatory/HOA
   quirk, services-offered grid, a 3-item FAQ with at least one
   location-specific question, nearby-area cross-links, CTA).
5. **If there's no special regulatory/historical quirk for a location**
   (this is fine and expected — not every neighborhood has one), don't
   fabricate one. Use a plain, honest "Quick facts" box instead (ZIP +
   "we cover all of X" + free-estimate mention) rather than forcing a
   fake differentiator. See `build_note_block()`'s fallback behavior in
   the generator script.
6. **Use a one-off Python generator script for the actual HTML**, not
   hand-writing each file — see `references/example-location-page-
   generator.py`. This keeps structure (nav, footer, section order,
   schema shape) identical across pages while forcing content to stay
   genuinely distinct, since the researched `facts` field is a required,
   visibly-different input per location rather than something that can
   silently get copy-pasted.
7. **Run both verification scripts immediately after generating the
   batch** (see "Verification scripts" below) — broken-link check and
   FAQ-schema-match check. Do this before considering the location-page
   batch done, not as an afterthought.

## Page formula for a location page

- **Title**: `Tree Removal in [Location] | [Brand]` (or `[Primary
  Service] in [Location], GA | [Brand]` if the niche isn't "tree
  removal")
- **H1**: `Tree Removal in [Location]`
- Real local detail from the research workflow above — never just the
  template with the city name swapped.
- A services-offered grid linking to every service page, with
  descriptive (not generic) anchor text.
- The ZIP code(s) for that area, stated plainly (helps both users and
  Google confirm geographic match).
- 3-item FAQ, at least one of which is location-specific (not just the
  generic "do you serve my neighborhood" / pricing pair repeated
  verbatim on every page).
- Nearby-area cross-links (2-3 sibling locations + a link back to the
  Service Areas hub) — this is what keeps location pages from being
  orphaned in the link graph (Whitespark on-page factor #16, see below).

## Image sourcing workflow

**Non-negotiable starting point: real (non-AI-generated) stock photos
for every content image, sourced fresh per page — the sole exception is
the logo, which is AI-generated per a separate, explicit decision (AI-
generated photos are increasingly flagged/de-weighted by Google's image
understanding; a logo is a graphic mark, not a photo, and isn't subject
to the same signal).**

**Standing rule: match the photo to the page's specific action, not just
its general topic — "on-topic" and "thematically precise" are not the
same bar.** A photo of a peaceful oak tree is on-topic for a tree-service
site; it is not a good photo for a page whose H1 is a specific service
like "Large & Hazardous Tree Removal," because it shows neither
largeness/hazard nor removal-in-progress. Prefer a photo that shows the
specific thing that page is about happening: for a removal page, someone
actually cutting/rigging/taking a tree down, not just a tree standing
there; for a storm/emergency page, a worker responding to or clearing
storm damage, not just a fallen tree with no one in frame; for a
trimming page, a pole saw or pruning shears actually mid-cut. This
applies retroactively too — re-audit a page's existing photo whenever
you're back in that file for another reason, the same way the homepage
hero got upgraded from a scenic oak/Spanish-moss shot to an actual
chainsaw-cutting-a-trunk action shot once that mismatch was pointed out,
and two more service pages (large/hazardous, storm/emergency) got the
same upgrade the same day. The one honest exception: if no genuine,
clean, on-topic action shot exists for a given specific service after a
real search attempt (tried for stump grinding three separate times, no
usable stump-grinder-in-action photo existed on Pexels), keep the best
available honest photo of the *situation* that service addresses (a
stump in a yard) rather than forcing a mismatched action shot from an
unrelated trade (a metalworking grinder, an industrial forestry
harvester) just to have "an action shot."

Step by step (uses the in-app Browser, not WebSearch — WebSearch doesn't
return usable direct image URLs for this):
1. **Navigate to a Pexels search URL directly**:
   `https://www.pexels.com/search/{url-encoded query}/`. Use a specific,
   multi-word query close to what the page actually needs — a vague
   query like "tree" returns garbage; "live oak spanish moss" or
   "arborist cutting tree chainsaw" returns usable, on-topic results.
2. **Extract candidate photo IDs and alt text via `javascript_exec`**:
   ```js
   Array.from(document.querySelectorAll('img[src*="images.pexels.com/photos/"]'))
     .map(img => { const m = img.src.match(/\/photos\/(\d+)\//); return m ? {id: m[1], alt: img.alt} : null; })
     .filter(v=>v).filter((v,i,a)=>a.findIndex(x=>x.id===v.id)===i)
   ```
   **Filter by alt text before downloading anything** — Pexels' search
   results include recommended/related tiles that are often completely
   off-topic (a search for oak trees returned an alligator, a barn owl,
   and a magnolia in one pass). An ID that recurs across multiple
   unrelated searches (e.g. the same handful of IDs showing up for both
   "oak tree" and "arborist chainsaw" queries) is very likely an
   injected recommendation tile, not a real result — don't trust it just
   because it appeared.
3. **Refine the search if the first pass doesn't surface a strong,
   specific match** — e.g. "oak tree canopy sunlight" was too generic
   and returned decorative canopy shots with no Spanish moss; "spanish
   moss tree" (the literal, specific term) found the real match. Don't
   settle for "close enough" on the first query.
4. **Download 4-6 strong candidates at small preview size** (`w=500&q=60`
   via Pexels' own URL params:
   `https://images.pexels.com/photos/{id}/pexels-photo-{id}.jpeg?auto=compress&cs=tinysrgb&w=500&q=60`)
   into the scratchpad, then **use the Read tool to actually view each
   one** — don't pick based on alt text alone.
5. **Zoom into any candidate showing a person before finalizing it** —
   crop and view just the clothing/vehicle area at higher resolution
   (a quick PIL crop-and-resize, or the browser's `zoom` action) to check
   for a legible third-party company name or logo. Two otherwise-good
   candidates got rejected this way in this build: a bucket-truck worker
   with "ST..." visible on a hoodie, and a pole-saw worker with a
   legible lawn-care company logo on his t-shirt. **A visible tool-brand
   name (Stihl, Husqvarna, Hyundai on a chainsaw) is fine** — that's just
   a real equipment brand, not a competing local service company; what's
   disqualifying is another *business's* name/logo.
6. **Download the final pick at the exact required pixel dimensions**
   using Pexels' crop params: `...&w=900&h=675&fit=crop` (this site's
   `.img-slot` convention is 900×675, 4:3 — check the project's own
   convention before assuming this number). Save directly into the
   project's `images/` folder with a descriptive filename matching the
   page it's for (e.g. `stump-grinding-savannah.jpg`, not `photo1.jpg`).
7. **Verify the final dimensions** with a one-liner:
   ```python
   from PIL import Image
   print(Image.open('images/whatever.jpg').size)  # must match exactly
   ```
8. No attribution is required under Pexels' license, but double-check
   there's no visible watermark in the final crop regardless.

**Homepage/service-page hero backgrounds**: once a page's main content
image is sourced, reuse it as the section's full-bleed background too
(rather than sourcing a second image) — apply the same dark-green
gradient-overlay treatment used sitewide:
```html
<section class="page-hero" style="background-image:linear-gradient(180deg, rgba(15,46,33,.86), rgba(15,46,33,.86)), url(&quot;../images/whatever.jpg&quot;)">
```
This requires the CSS class itself to declare `background-size:cover;
background-position:center` (and a `background-color` fallback) as
*separate longhand properties*, not as one `background: ...` shorthand
— otherwise the inline `background-image` override collides with the
shorthand instead of layering cleanly on top of it.

## Logo workflow

The logo is the one place AI generation is explicitly fine — this is a
deliberate, separate decision from the real-stock-photo rule for content
images, made explicit to the owner so it's never accidentally treated as
a blanket "no AI" rule. That said, **after building one logo each way for
this project, hand-authoring the SVG directly (no image model at all) is
usually the better default** — it sidesteps every problem the AI-then-
trace path caused: no huge blank-canvas viewBox to measure and crop, no
name-baked-into-non-editable-artwork risk on a future rename, and the
background/contrast treatment is fully under your control from the
start. Reach for AI generation only when the owner specifically wants a
look that's genuinely hard to hand-code (a detailed illustrative style,
photoreal elements) — for a clean geometric mark or a circular badge
with arced text, hand-coding is faster and more robust end to end. Both
paths are documented below; read the hand-authored path first.

### Hand-authored SVG (preferred default)

1. Design directly in markup — for a circular-badge style (arced brand
   name on top, arced tagline on bottom, an icon in the center), use
   real `<text>` + `<textPath>` elements bound to two `<path>` arcs
   defined in `<defs>`, not an image-generation tool. The text stays
   genuinely editable forever this way — a future rename is a one-line
   string replace, never a full asset regeneration.
2. **Always add a solid background shape behind the whole mark** (e.g. a
   white disc sized to fill inside the outermost ring) — this is what
   lets one SVG file work correctly in both a light header and a dark
   footer. The AI-generated logo in this project never had one, which
   is exactly why it needed two different footer/header treatments;
   a hand-authored one doesn't have to make that compromise.
3. **Preview at real render sizes before finalizing — the local-file
   browser preview sandboxes scripts (CSP blocks them), so serve the
   file over a plain local HTTP server first**: `python -m http.server
   {port}` from the project root, then navigate the browser to
   `http://localhost:{port}/images/logo.svg` (or a copy of the draft
   under a temporary filename inside the project so it's servable). Test
   at three sizes minimum: large (to check overall composition), header
   height (~38px — confirm whether arced/small text is legible or purely
   decorative, matching the pairing decision below), and against both a
   white and the site's actual dark footer background color (toggle via
   `document.documentElement.style.background` in `javascript_exec` —
   this works fine on an HTTP-served page even though it's blocked on a
   local-file one).
4. **Iterate on real, specific problems the preview shows, not
   assumptions** — e.g. text overflowing its arc (shorten the string
   and/or reduce font-size/increase arc radius; don't guess at numbers
   without re-checking), an accent icon that reads as an unrecognizable
   blob at small size (simplify or drop it — a shape has to survive
   being simplified in your head before it survives being drawn in
   `<path>` coordinates by hand).
5. Once finalized, delete every draft/preview copy from the project
   folder (they're scratch work, not project assets) and stop the local
   HTTP server.

### AI-generated + traced (when genuinely warranted)

1. **Generation is manual, not automated.** Browser automation of Google
   AI Studio proved unreliable in this project (submissions returned
   "An internal error has occurred" repeatedly, and a bypass attempt via
   keyboard shortcuts didn't work in the sandboxed browser context).
   **Give the owner a clean, complete prompt in chat and let them paste
   it into their own AI Studio session themselves** — don't keep
   retrying automation.
2. **When the logo comes back, inspect it before wiring it in.** An AI
   image tool export can arrive as an oversized SVG with a huge amount
   of blank canvas around the actual mark (this build's export had a
   1408×768 viewBox where the real content only occupied roughly a
   675×665 region in one corner). Measure the real bounding box and crop
   the viewBox tightly:
   ```js
   // in the browser, with the SVG open as its own document/tab:
   const bbox = document.documentElement.getBBox();
   JSON.stringify({x:bbox.x, y:bbox.y, width:bbox.width, height:bbox.height})
   // (JSON.stringify on a raw DOMRect gives "{}" — pull x/y/width/height
   // out as plain numbers first, as shown, since they're inherited
   // getters, not own properties)
   ```
   Then rewrite the SVG's `viewBox` attribute to `"{x-padding} {y-padding}
   {width+2*padding} {height+2*padding}"` and drop the explicit
   `width`/`height` attributes so it scales via CSS using the new
   viewBox's aspect ratio.
3. **Decide header treatment based on legibility at small size, not on
   principle.** A circular badge/seal-style logo (arced text around a
   central emblem) reads fine at a large size but turns into an
   illegible smudge at a typical header height (~2.4rem / 38px) — in
   that case, keep the logo as a small icon *next to* the existing text
   wordmark rather than fully replacing the text with the image. A
   tighter, purpose-built horizontal wordmark logo (like NEXUS's) can
   fully replace the text. Check by actually looking at it rendered at
   header size before deciding, not by assumption.
4. **Check contrast against the footer background separately from the
   header.** If the footer has a dark background and the logo is solid
   black (or otherwise low-contrast against dark), it will vanish there
   even if it looks fine in the (usually white/light) header. In that
   case, keep the pre-existing text-based `logo-mark` treatment in the
   footer and only use the image in the header — this is the same
   pattern NEXUS already used, not a new one invented for this site.
   **Or fix it at the source instead**: some AI-vectorized exports (as
   opposed to a flat potrace trace) include a fully opaque background
   layer — a literal full-canvas rectangle path (e.g. `M 0 0 L 2048 0 L
   2048 1989 L 0 1989 L 0 0 z`) filled white, sitting behind the actual
   badge. That's what breaks footer use, not the badge itself. Grep the
   raw SVG for a suspiciously simple 4-corner rectangle path matching
   the full viewBox dimensions, delete just that one path, then add a
   properly-sized white circle (or shape matching the badge's own
   outline) behind the remaining content instead — this makes the badge
   itself transparent outside its border and the *same file* works in
   both the header and the footer, no dual-treatment workaround needed.
   Re-measure `getBBox()` after removing the rect, since it was very
   likely inflating the measured bounding box to the full canvas size
   and hiding how tightly the actual content was already cropped.
5. **If the brand name ever changes after a logo exists, check whether
   the name is baked into the artwork itself** (true for anything
   AI-generated then rasterized/traced — the letters are vector path
   shapes, not an editable `<text>` element) before assuming a find-
   replace will fix it. It won't. Delete the now-wrong logo and revert
   to the text-only header treatment until a new one is generated under
   the correct name — see the rename mechanics in the "Brand name &
   domain vetting" section above.
6. **The favicon is usually a separate, simpler asset** — a small
   inline data-URI SVG with a 2-3 letter monogram in `<text>` (real,
   editable markup, unlike a traced logo). Keep it simple and bold
   rather than trying to shrink the full logo down to 16-32px; update
   its monogram text on a rename (grep for it, it's a literal
   `%3ETXT%3C/text%3E` substring in the percent-encoded data URI).

## Page build sequence — follow this order, it is not optional

Learned the hard way on the Foundation Repair homepage (2026-09-15), which
was written from memory of "what the markup usually looks like" and shipped
with twelve nonexistent CSS classes and a dead form. The owner found it
immediately by looking at the live page. CSS fails *silently* on a selector
it has no rule for, so none of it errored — it just rendered wrong in five
different ways that each looked like a separate mystery bug. Order matters
because each step below makes the next one's mistakes impossible:

**1. Extract the real class vocabulary BEFORE writing any markup.** When
adapting from a sibling site, the CSS is the contract; your memory is not.
Two commands, run first, every time:
```bash
# what the stylesheet actually defines
grep -o '^\.[a-zA-Z][a-zA-Z0-9_-]*' css/style.css | sort -u
# what the working sibling page actually uses (the proven vocabulary)
python -c "import re,sys;print(' '.join(sorted(set(w for m in re.finditer(r'class=\"([^\"]+)\"',open(sys.argv[1],encoding='utf-8').read()) for w in m.group(1).split()))))" ../other-site/index.html
```
Write markup only from that list. If a component you want doesn't exist,
either add a real CSS rule for it or use the existing component — never
invent a class name and assume it will be styled.

**2. Check the JS hook names the same way.** `grep -o '\[data-[a-z-]*\]'
js/main.js`. On this build the form was written with `data-booking-form`
while `main.js` binds `[data-quote-form]` — the submit button was simply
dead, and nothing anywhere said so.

**3. Every inline SVG needs a sizing rule that matches it.** In this design
system every `svg` is sized by a container-scoped rule
(`.trust-strip .item svg{width:2rem}`, `.service-card .icon svg{...}`). An
SVG with a `viewBox` and no width/height and no matching rule expands to
the full container width — that's where the giant arrow came from. Either
put the SVG inside a container that already has a sizing rule, or use a
text glyph (`→`) like the sibling site's `.link` does.

**4. Run all three verification scripts** (below) before looking at the
page at all. They catch in two seconds what takes ten minutes to spot by eye.

**5. Serve it over a real local HTTP server and audit the rendered page**
— not the file, not a screenshot alone. Run the contrast + overflow +
oversized-SVG audit in `references/rendered-page-audit.js`. Screenshots
show you what you thought to look at; the audit checks everything.

**6. Only then look at it visually**, desktop and 375px mobile.

**7. Bump `?v=N` on every page whenever css or js changed** — skipping this
means step 5 audits a stale cached stylesheet and reports problems you
already fixed (happened on this very build).

## Global colour utilities inside dark components — check both, always

`.muted` is defined once as a dark grey, which is correct against the light
page body and drops to ~2.7:1 against the dark footer — effectively
invisible. This is the *same bug class* as the already-documented inline
colour override that matches its own background, just arriving through a
global utility class instead of an inline style. The fix is a scoped
override (`.site-footer .muted{color:#9fb0c4;}`), not deleting the class
from the markup.

**This bug was inherited**: it existed on the tree-removal site first and
was copied into the second site along with the stylesheet. When you adapt a
stylesheet from a sibling project, its latent bugs come with it — run the
rendered-page contrast audit on the *source* site too, and fix both.

## Verification scripts

Two scripts live in `scripts/` and should be run after any batch of new
or edited pages, before committing — both exit non-zero with a specific
report if something's wrong, and exit 0 with a one-line summary if clean:

```bash
python .claude/skills/microsite-agent/scripts/check_broken_links.py .
python .claude/skills/microsite-agent/scripts/check_faq_schema.py .
```

- **`check_broken_links.py`** — walks every `*.html` file, extracts every
  `href=`/`src=` that isn't external/`tel:`/`sms:`/`mailto:`/`#`/`data:`,
  strips query strings and anchors, and confirms the resolved path is a
  real file on disk. This is exactly the kind of thing that silently
  404s in production on a static site with no build-time link checking
  — hub-and-spoke sites cross-link constantly (nav, footer, breadcrumbs,
  area-chips, in-FAQ links), so this needs to be routine, not occasional.
- **`check_faq_schema.py`** — for every page with a `FAQPage` JSON-LD
  block, confirms the questions listed in the schema exactly match the
  visible `<summary>` text, in the same order. This caught a real bug in
  this build (curly vs. straight quotes around the word "hazardous" —
  the JSON-LD had been typed slightly differently from the visible
  markup) — treat any mismatch it reports as a real bug to fix, not a
  false positive, until proven otherwise.

Both scripts are intentionally simple (regex over the raw HTML, no DOM
parser dependency) so they run instantly with zero setup on any machine
that has Python — that's deliberate, don't "improve" them into needing
`pip install` something for a one-shot pre-commit check.

## Filtering rank-and-rent source material (the recurring pattern)

Owners researching this space paste YouTube transcripts and course
content fairly often. The pattern for handling this, refined across
three separate pastes so far:

1. **Read the whole thing before reacting.** Most of it is legitimate,
   mainstream local-SEO practice (bottom-of-funnel keyword focus,
   service+location page structure, internal linking that funnels
   authority to the homepage, competitor recon before building, a
   persistent-memory/continuity system for the AI). Don't reject
   wholesale just because the source is a "rank and rent" course.
2. **Identify the specific tactics that cross a real line**, and reject
   *only those*, explicitly, by name, when responding — don't vaguely
   gesture at "some of this isn't great." Concrete examples actually
   encountered and rejected so far:
   - GBP video-verification fraud (staging a vehicle/tools to fool an
     AI reviewer, spoofing geolocation).
   - Writing site copy "as if I am the brand" with an invented
     "N years of experience" before any real business exists.
   - Doorway-page-style near-duplicate content across dozens of
     hyper-local variants with no real differentiation.
   - "Grey hat" image scraping ("grab images and hope you don't get
     caught") — the opposite of this skill's sourcing workflow.
   - Fake/seeded reviews or review-gating.
3. **State clearly to the owner which parts were kept and which were
   filtered, and why**, referencing the specific honesty rule each
   rejected tactic violates. This isn't just a courtesy — it's what lets
   the owner correct you if you filtered something they actually wanted
   to discuss further, and it's what makes the eventual STATUS.md
   breadcrumb entry meaningful instead of "did some SEO stuff."
4. **Architecture-only lessons still get adopted even from a source with
   bad tactics mixed in** — e.g. the WordPress/SFTP-based build video
   that also described GBP fraud still contributed one genuinely useful,
   adopted idea: research each location for real, sourced facts *before*
   writing its page, instead of templating the city name in. Adopting
   that one idea doesn't require adopting the source's WordPress/SFTP
   tooling choices, which this project deliberately doesn't use (see
   Stack and hosting below) — pull the technique, not the stack.

## GitHub Pages as temporary preview hosting

The final production host for these sites is Cloudflare Pages (see
below), but a quick, shareable, public preview link is often wanted
before the real domain/hosting is connected — for the owner to view
progress on another device, for instance. GitHub Pages is the fast path
for this, entirely separate from the eventual Cloudflare Pages setup:

```bash
# from the project root, with a git repo already initialized/committed:
gh repo create {repo-name} --public --source=. --remote=origin
git push -u origin main
gh api repos/{owner}/{repo-name}/pages -X POST -f "source[branch]=main" -f "source[path]=/"

# poll until the build finishes (usually 30-60s):
for i in 1 2 3 4 5 6; do
  status=$(gh api repos/{owner}/{repo-name}/pages/builds/latest 2>&1 | grep -o '"status":"[a-z]*"' | head -1)
  echo "attempt $i: $status"
  if [ "$status" = '"status":"built"' ]; then break; fi
  sleep 8
done
```
Live URL is `https://{owner}.github.io/{repo-name}/`. Every subsequent
`git push` to `main` auto-rebuilds it — after any push meant to be
visible immediately, re-run the same polling loop and then actually
navigate to a page and check its content (via `get_page_text` or
`read_network_requests` on a known asset, not just a screenshot — the
in-app browser sometimes shows a stale cached page on the very first
check after a push; a hard navigate with a cache-busting query string
or a second fetch resolves it).

**This is explicitly a public repo and a public preview** — say so to
the owner plainly when setting it up (real content, real placeholder
phone numbers, etc. become visible to anyone with the link).

## Technical / on-page checklist (applies to every page)

- Local-area-code phone number as a `tel:` link in a sticky header —
  never a toll-free number, it reads as less local/trustworthy.
- NAP (business name, service area, phone, hours) in the footer of every
  page, worded identically everywhere (consistency matters more than any
  single wording choice).
- `LocalBusiness` (or the closest matching subtype) JSON-LD on every page,
  with real `areaServed`, `telephone`, and `makesOffer` — only include
  fields that are actually true; omit rather than fabricate.
- `FAQPage` JSON-LD matching visible FAQ content exactly (same rule as
  `Project1`'s sites) — verify with `check_faq_schema.py`, not by eye.
- Regional/climate detail where genuinely relevant (coastal Georgia heat,
  hurricane season June–November, old oak canopy with Spanish moss driving
  large-tree-removal demand) — this is a real expertise signal, not filler,
  as long as it's accurate.
- Zero broken internal links/asset references — verify with
  `check_broken_links.py`, not by eye, after every batch of changes.
- **No inline color override that matches its own background** — a real
  bug found on this build: every `.cta-band` (dark green background) had
  its ghost button hand-styled with `style="border-color:var(--forest);
  color:var(--forest)"`, the exact same color as the section it sat in,
  making the button completely invisible. It happened because that
  inline override was copy-pasted onto every CTA band across every page
  (and into the location-page generator script) without re-checking
  that the color still made sense against *that* component's actual
  background — it only would have been correct on a light background.
  The lesson: when a button/badge/text color is set with an inline
  style rather than inherited from its component class, treat that as a
  flag to double check contrast against the actual element it's sitting
  in, especially right after copy-pasting the same snippet onto a new
  page — a class's default styling (here, `.btn-ghost`'s `color:#fff`)
  is usually already correct for the background its component is
  designed for; an inline override fighting the class is more often a
  mistake than a deliberate choice. When auditing for this class of bug,
  grep for `style="` blocks containing `color:` and check each one
  against the actual background of its containing section.

## Mobile QA — a real bug this project shipped, and the testing mistake that missed it

A prior "mobile audit" on this project concluded the mobile nav worked
by running `document.querySelector('[data-nav-toggle]').click()` in the
browser and observing the panel's `is-open` class get added. **That
tested the JS handler's logic, not whether the button was actually
visible/tappable by a real user** — and it wasn't: `.nav-toggle` had
`display:none` as its unconditional base style, and the mobile media
query (which correctly showed the close button, the slide-out panel,
and the mobile CTA buttons) never included a rule to make the *open*
button visible again. Every mobile visitor on every page had a
completely inaccessible primary nav — no way to reach About, FAQ, or
Contact at all, since the footer doesn't link to those either. Roman
caught this by looking at an actual screenshot, not by anything an
automated check had verified.

**The concrete lesson: calling `.click()` or dispatching a synthetic
click on an element proves its event handler *logic* works. It proves
nothing about whether a real user could ever find or tap that element.**
Before trusting any interactive-element test, separately check the
trigger element's actual visibility:
```js
const el = document.querySelector('[data-nav-toggle]');
const rect = el.getBoundingClientRect();
const style = getComputedStyle(el);
({ visible: rect.width > 0 && rect.height > 0 && style.display !== 'none' && style.visibility !== 'hidden' })
```
Do this for every interactive control a mobile-QA pass touches (nav
toggle, nav close, accordion labels, form submit buttons) — not just
the ones that seem likely to have a display:none problem. The general
pattern to grep for when auditing a new site: any selector styled
`display:none` at baseline, check that *every* breakpoint where it's
supposed to reappear actually contains a rule that un-hides it — it's
easy to correctly write the close button, the overlay, and the slide-out
panel for a mobile nav while forgetting the one button that opens it in
the first place, especially when the open button's default state is
"hidden until a media query says otherwise" and that media query rule
never got written.

**Second lesson from the same session: don't mistake a frozen test
environment for a real animation bug.** After fixing the above, checking
whether the panel's CSS transition (`transform: translateX(...)`)
actually animated open showed the computed transform stuck at its
closed-state value even ~400ms after dispatching the click — looking
exactly like a second real bug (class toggles, but the visual slide-in
doesn't happen). Before concluding that, check `el.getAnimations()`:
```js
document.querySelector('[data-nav]').getAnimations()
  .map(a => ({ playState: a.playState, currentTime: a.currentTime }))
```
If `currentTime` is stuck at `0` (or otherwise not advancing) despite
real wall-clock time passing, the animation timeline itself is frozen —
almost always because the browser-pane tool isn't actively compositing
the tab to a real display surface in that moment (a known limitation,
distinct from `document.hidden`, which can still report `false`). Cross-
check by confirming the *static* properties from the same CSS rule block
did apply correctly (position, width, display, the class name itself) —
if those are all correct and only the transitioning property is stuck,
it's the test tool's compositor, not the site. Don't report this as a
bug; don't "fix" CSS that isn't broken chasing it.

**Mobile QA checklist to actually run (not just assert), every time:**
- Every interactive trigger element (nav toggle, nav close, accordion
  labels): check real visibility (`getBoundingClientRect` + computed
  `display`/`visibility`), not just that dispatching a click updates
  some class.
- Horizontal overflow: `document.documentElement.scrollWidth >
  window.innerWidth` on at least the homepage, one service page, one
  location page.
- Any long text string in a persistent/sticky element (a utility bar,
  an announcement banner) at the narrowest realistic width (375px, not
  just "below 960px") — long sentences that fit fine at 700px can wrap
  to two or three dominant lines at 375px and need their own, tighter
  breakpoint, not just inheriting the same font-size as the tablet range.
- Form field widths on the actual mobile viewport, not just at desktop
  width scaled down.
- The fixed mobile action bar's reserved bottom padding still matches
  its rendered height (they can drift apart if either changes later).

## Ongoing ranking-factor audits

`references/whitespark-ranking-factors-checklist.md` holds the full,
categorized Whitespark Local Search Ranking Factors list (On-Page,
Citation, GBP, Review, Link/Behavioral/Personalization/Social signals).
**Only the On-Page Signals category is something a site-code session can
audit and fix directly** — the rest depend on a live GBP, real reviews,
and real backlinks that don't exist yet for a fresh build. Re-run the
On-Page audit (grep titles/headings/schema, check images aren't AI-
generated or generic unrelated stock, check internal links resolve,
check mobile CSS) after any batch of page changes, especially after
closing an internal-linking gap (adding location pages that previously
404'd, for instance) — that's exactly the kind of change this audit is
meant to catch regressions or improvements on.

## Stack and hosting

- Static HTML/CSS/JS, no build step — same proven approach as `Project1`'s
  sites, easiest to maintain via Claude Code, zero-dependency to host.
- **Do not** reach for a generator framework (Astro/Node) or a CMS
  (WordPress) just because source material used one — it adds a real
  dependency to maintain for no benefit at this page count (~20 pages at
  Phase 1), and this project already has an equivalent to whatever an
  "LLM wiki" / SFTP-to-WordPress workflow is trying to achieve: static
  HTML + git + this file + `STATUS.md`. If hand-writing location pages
  gets repetitive, use a local one-off Python script that reads
  per-location data and writes out the final static HTML files (see
  `references/example-location-page-generator.py`) — the output is
  still plain static HTML with nothing to run at request time, just a
  convenience during authoring.
- **Hosting: Cloudflare Pages** (not Vercel/GitHub Pages like `Project1`'s
  sites) — drag-and-drop the built folder, or connect a GitHub repo for
  auto-deploy on push, same idea as the Vercel-on-push setup already
  working for NEXUS. GitHub Pages (above) is a fine *temporary* preview
  host in the meantime, but say so explicitly — it isn't the plan.

## Cross-reference

For everything NOT specific to the rank-and-rent/microsite model (cache-
busting, nav dropdown bugs, browser-automation testing gotchas, deployment
verification habits), the lessons in `Project1`'s `web-dev-agent` skill
still apply — this skill only covers what's different about the microsite
model.
