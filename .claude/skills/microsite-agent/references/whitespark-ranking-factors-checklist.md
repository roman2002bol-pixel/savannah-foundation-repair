# Whitespark Local Search Ranking Factors — standing checklist

Source: https://whitespark.ca/local-search-ranking-factors/ (Whitespark's
annual expert-survey report on Google Local Pack/Maps ranking factors).
Roman asked for this to become a recurring check, not a one-off — re-run
this audit whenever a batch of pages/GBP/citation work is finished, and
before calling any phase "done."

The report groups factors into 8 categories. Only **On-Page Signals** is
something this Claude Code session can fully build and grade by itself —
the rest depend on a live Google Business Profile, real reviews, real
backlinks, and real directory citations, none of which exist yet for this
site. Track those as Roman's/future tasks, not site-build tasks.

## On-Page Signals (fully site-controllable — audit this category every time)

1. HTML NAP Matching GBP NAP
2. Keywords in GBP Landing Page Title Tag
3. Geographic (City/Neighborhood) Keyword Relevance of Content
4. Keywords in GBP Landing Page Headings (H1, H2, etc)
5. Keywords in GBP Custom Service Titles *(GBP-side, not site)*
6. Volume of Searches for Business Name *(brand-dependent, not site)*
7. Dedicated Page for Each Service
8. Quality/Authority of Inbound Links to GBP Landing Page URL *(off-site)*
9. Keywords in GBP Services *(GBP-side)*
10. Website's Degree of Focus on a Specific Niche
11. Keywords in Native Google Reviews *(GBP-side)*
12. Topical (Product/Service) Keyword Relevance Across Entire Website
13. Internal Links TO GBP Landing Page from Other Pages of Website
14. Photo & Video Quality (resolution, clarity, **not stock**, etc)
15. Keywords in Anchor Text of Inbound Links to GBP Landing Page URL *(off-site)*
16. Internal Linking Across Entire Website
17. Keywords in Title Tags Across Entire Website
18. Website Uses HTTPS by default
19. Domain Authority of Website *(off-site, accrues over time)*
20. Mobile-friendly/Responsive Website
21. Freshness of Content on GBP Landing Page
22. Keywords in Headings (H1, H2, etc) Across Entire Website
23. Volume of Quality Content on Service Pages
24. Photos Match Target Keywords
25. Website Content Marked Up in Schema

## Citation Signals (external — GBP/directory work, not a site-code task)

1. Consistency of Citations on Primary Search Engines (Google Maps, Bing Maps, Apple Maps)
2. Consistency of Citations on Key Sites (Yellowpages, Yelp, D&B, CityGrid)
3. Quality/Authority of Unstructured Citations (news, blogs, gov sites, industry associations)
4. Quantity of Citations from Locally-Relevant Domains
5. Quantity of Citations from Industry-Relevant Domains
6. Quality/Authority of Structured Citations
7. Consistency of Citations on Data Aggregators (Infogroup, Localeze, Foursquare/Factual)
8. Enhancement/Completeness of Citations
9. Quantity of Unstructured Citations
10. Quantity of Structured Citations (IYPs, Data Aggregators)
11. Consistency of Citations on Other Citation Sources

**Do not start citation building until real NAP is locked in** — every
citation has to use the exact same name/address/phone as the eventual
GBP, and a fixed-later phone/domain means redoing every citation.

## Google Business Profile Signals (needs a live GBP — future task)

Primary/additional categories, business-title keywords, map-pin accuracy,
profile completeness, hours set correctly ("Business is Open at Time of
Search" is a 2026 addition Whitespark calls high-impact), predefined +
custom services with keywords, attributes, products, description
keywords, service-area settings, Q&A, embedded map, FAQs, booking
feature/URL, photos & videos (quantity, recency, **keyword match** —
same "not stock" spirit as on-page), Google Posts frequency/quantity,
clicks-to-call and driving-direction requests, dwell time/engagement,
verification status, GBP age, address visibility (non-SAB). Full list of
48 items lives in the source page if a future session needs the exact
wording.

## Review Signals (needs real reviews — future task, after GBP exists)

Star rating, quantity/recency/velocity of native Google reviews (text
matters more than stars-only), positive sentiment, reviews with
photos/video, keyword content in reviews, authority reviewer signals
(Local Guides/Yelp Elite), owner responses, third-party review presence
(Yelp, industry-specific sites) and their authority/diversity, Q&A
section with owner-seeded FAQs. **Never fabricate reviews or claim a
star rating that doesn't exist** — same non-negotiable rule as the rest
of this skill.

## Link, Behavioral, Personalization, Social Signals

Not detailed here — all off-site or user-behavior-driven, not something
a static site build produces directly. Revisit once the site has real
traffic and a GBP to analyze.

## How to use this file

When asked to "check against Whitespark" (or similar), re-run only the
**On-Page Signals** section against the current state of the repo (grep
titles/headings/schema, check `.img-slot` sources aren't AI-generated
*or* generic unrelated stock, check internal links resolve, check mobile
CSS) — that's the only category this session can move the needle on
today. Note the rest as blocked on: real NAP + GBP creation (do this once
domain/phone/email are final), then reviews, then citations, then links.
