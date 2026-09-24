# Local SEO content playbook

Updated September 23, 2026. These practices were implemented on the existing microsite, not a plan for a future redesign.

## What to carry forward

1. Give each area page an address-relevant decision: the correct authority, local records, access constraint or documented local infrastructure. Connect the fact to what the customer should check before agreeing to work. A city name substituted into generic service prose is insufficient.
2. Put a primary-source link beside the claim it supports. Check jurisdiction and scope. A county rule may cover only unincorporated land; association rules do not cover an entire island. Recheck time-sensitive rules before changing them.
3. Distinguish local context from a diagnosis. Flood maps, nearby drainage projects and neighborhood age do not prove structural failure, a soil type or a particular repair requirement.
4. Use area hubs to help visitors choose: short, distinct summaries explain what each researched guide answers. Link related service pages to area guidance using descriptive text, and link area guidance back to the relevant service.
5. Keep illustrative service scenarios explicitly labeled. They belong on relevant service pages or the homepage; repeating the same scenario on every area page adds little value. Actual case studies need verified work, location, outcome and permission to use photographs.
6. Replace generic trust labels such as Local / Free / Fast with concrete inspection or scope information. Do not restore the removed “18 AREAS WRITTEN UP” display or use page counts as evidence of expertise.
7. Do not copy video tactics uncritically. No ranking guarantees, invented prices, fabricated reviews, or unverified credentials. No automatic claim that an outbound source link, geotag or special AI markup improves rankings.

## Implemented content and sources

See LOCAL-RESEARCH.md for the video references and official local sources. The six-site-page research effort produced three detailed area guides on this site, a three-card area-hub section and three contextual service links. Remaining area pages retain shorter local notes; they have not all received the same depth of new research.

Content lives in local_research.json. local_research.py renders marked LOCAL-RESEARCH sections, removes repeated FIELD-GUIDE scenarios from area pages, and maintains LOCAL-LINK passages on related service pages. Repeated runs replace the marked content rather than adding another copy. Edit the data rather than only generated HTML.

No design, CSS or JavaScript change was needed for this pass. Existing field-guide components provide the responsive layout. Do not remove the marker comments without updating the renderer.

## Verification and publication

For content batches, run the existing broken-links, FAQ-schema, image-reuse, markup-contract, SEO-basics and US-English audits. FAQ answers must match visible text and JSON-LD. Check representative pages on desktop and at 375px, and follow new internal links. Verify the deployed commit and live content before reporting publication complete.

September 23 verification: all six audits passed across 20 Tree and 31 Foundation pages; desktop/mobile content checked; a Tree area-to-service link verified in the browser. Both GitHub Pages builds completed, and new local blocks were confirmed on the public sites.

## Open work, not completed

The previews still use placeholder business contacts and a lead form without a production endpoint. Configure the real domain, canonical URLs, sitemap host and contact/lead destination together before a production launch. No Search Console submission, actual case-study publication or ranking improvement has been verified. There are no new verified soil-series or housing-age statistics in this pass.

## Keep this record current

With each future change, update STATUS.md and the relevant research/playbook entry. Include what changed, why, source and date where applicable, affected pages, validation, deployment status and remaining limitations. Preserve a clear distinction between completed work, proposed ideas and user-supplied facts.

## Foundation implementation details

Deep guides: Downtown Savannah, Midtown Savannah and Pooler. Repeated examples were removed from all eighteen area pages. New facts cover MPC masonry guidance, Casey South drainage context and Pooler elevation-certificate resources. They are planning information, not property diagnoses.

The existing build_pages.write function calls content_review.apply_site, which now calls local_research.apply_site. This preserves researched blocks after the core, area or service generators run. A standalone `python local_research.py` refreshes researched content from its JSON data. Service examples remain managed by content_review.py. Do not bypass these post-processing steps when rebuilding.

Published content commit: `e96514d5fe96f0802b3d358197341ded4d860005`.


## September 24 update – visible citations and visual video review

See VIDEO-REVIEW-2026-09-24.md for observed frames, the visible research prompt and an adapted reusable brief. Citation links must be recognizable without hover: underline and sufficient color contrast, including keyboard focus. Put the source in the paragraph containing its claim; do not rely on a distant reference box. CSS cache version is now 20260924 across public pages and Foundation generators.

Researched local sections now appear after the page hero. Keep the single marked section and the idempotent local_research renderer. Foundation service citations belong in build_services.py; Tree service citations are in the static service HTML. Update these sources when rebuilding. The previous note that this pass made no CSS change applies only to September 23.
