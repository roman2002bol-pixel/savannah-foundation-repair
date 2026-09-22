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

PAGES = [{'slug': 'downtown-savannah-ga',
  'work': 'crack',
  'photo': 'downtown-savannah-home.jpg',
  'photo_alt': 'Historic brick building in downtown Savannah under live oaks',
  'name': 'Downtown &amp; Historic Savannah',
  'plain': 'Downtown Savannah, GA',
  'zip': '31401',
  'lede': 'Foundation and crawl-space assessment in Downtown Savannah, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'For a property in a Savannah historic district, establish whether visible exterior changes need '
           'preservation review. Record fragile masonry and plaster before planning any lift; street access '
           'also affects equipment staging. Reference: <a href="https://www.thempc.org/Application" '
           'target="_blank" rel="noopener">Metropolitan Planning Commission applications</a>.',
  'note_head': 'Historic finishes and access',
  'note': 'Record crack width and dates, compare floor elevations, inspect the support below and check '
          'whether doors have changed. A stable surface defect may need monitoring or masonry work. Active '
          'movement requires a support assessment before cosmetic sealing.',
  'focus': ['A stair-step crack beside a window',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Downtown Savannah, GA?',
            'A masonry joint opens near a window, but a photograph does not establish whether movement is '
            'active. Photograph the affected area safely, note when it changed, and bring any earlier repair '
            'records.'),
           ('Does this symptom prove I need foundation repair?',
            'Record crack width and dates, compare floor elevations, inspect the support below and check '
            'whether doors have changed. A stable surface defect may need monitoring or masonry work. Active '
            'movement requires a support assessment before cosmetic sealing.'),
           ('What local checks should happen before work?',
            'For a property in a Savannah historic district, establish whether visible exterior changes need '
            'preservation review. Record fragile masonry and plaster before planning any lift; street access '
            'also affects equipment staging.')]},
 {'slug': 'pooler-ga',
  'work': 'slab',
  'photo': 'pooler-new-home.jpg',
  'photo_alt': 'Newer two-story home with a concrete driveway, typical of Pooler subdivisions',
  'name': 'Pooler, GA',
  'plain': 'Pooler, GA',
  'zip': '31322',
  'lede': 'Foundation and crawl-space assessment in Pooler, GA: start with the building, drainage and access '
          'at your address.',
  'facts': 'For a Pooler driveway or garage apron, determine whether the affected concrete is independent '
           'flatwork. Review drainage and construction records where available; a newer house does not prove '
           'poor compaction or establish a warranty outcome. Reference: <a '
           'href="https://www.pooler-ga.gov/online-services/applications-forms/" target="_blank" '
           'rel="noopener">City of Pooler applications and forms</a>.',
  'note_head': 'Check the panel before choosing a repair',
  'note': 'Check whether the panel is separate from the house foundation, map the level difference, and '
          'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
          'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.',
  'focus': ['A driveway edge drops beside the garage',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Pooler, GA?',
            'The outside concrete is lower than the garage floor after rain. Photograph the affected area '
            'safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check whether the panel is separate from the house foundation, map the level difference, and '
            'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
            'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.'),
           ('What local checks should happen before work?',
            'For a Pooler driveway or garage apron, determine whether the affected concrete is independent '
            'flatwork. Review drainage and construction records where available; a newer house does not '
            'prove poor compaction or establish a warranty outcome.')]},
 {'slug': 'richmond-hill-ga',
  'work': 'slab',
  'photo': 'richmond-hill-home.jpg',
  'photo_alt': "Brick family home of the kind built across Richmond Hill's newer neighborhoods",
  'name': 'Richmond Hill, GA',
  'plain': 'Richmond Hill, GA',
  'zip': '31324',
  'lede': 'Foundation and crawl-space assessment in Richmond Hill, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'A Richmond Hill mailing address does not by itself identify the permit authority. Bryan County '
           'building inspection guidance applies to unincorporated areas; confirm city limits before '
           'submitting a scope. Reference: <a '
           'href="https://www.bryancountyga.gov/government/departments-a-g/community-development/building-and-codes/building-inspections" '
           'target="_blank" rel="noopener">Bryan County building inspections</a>.',
  'note_head': 'City and county boundaries matter',
  'note': 'Check whether the panel is separate from the house foundation, map the level difference, and '
          'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
          'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.',
  'focus': ['A driveway edge drops beside the garage',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Richmond Hill, GA?',
            'The outside concrete is lower than the garage floor after rain. Photograph the affected area '
            'safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check whether the panel is separate from the house foundation, map the level difference, and '
            'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
            'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.'),
           ('What local checks should happen before work?',
            'A Richmond Hill mailing address does not by itself identify the permit authority. Bryan County '
            'building inspection guidance applies to unincorporated areas; confirm city limits before '
            'submitting a scope.')]},
 {'slug': 'skidaway-island-ga',
  'work': 'encapsulation',
  'photo': 'skidaway-marsh.jpg',
  'photo_alt': 'Tidal marsh and creeks surrounding Skidaway Island at sunset',
  'name': 'Skidaway Island',
  'plain': 'Skidaway Island, GA',
  'zip': '31411',
  'lede': 'Foundation and crawl-space assessment in Skidaway Island, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'For a property within The Landings, confirm current community requirements and contractor access '
           'before scheduling exterior work. Provide the proposed scope rather than assuming that community '
           'approval replaces any public permit. Reference: <a '
           'href="https://landings.org/member-welcome-guide/" target="_blank" rel="noopener">The Landings '
           'resident service guidance</a>.',
  'note_head': 'Community review and work access',
  'note': 'Check hinges and seasonal swelling, then compare nearby cracks and elevations before attributing '
          'it to settlement. Minor joinery issues may need no foundation work. Several connected signs '
          'justify a closer structural assessment.',
  'focus': ['A door starts sticking after a wet season',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Skidaway Island, GA?',
            'One door binds, but the owner has not recorded floor or crack changes. Photograph the affected '
            'area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check hinges and seasonal swelling, then compare nearby cracks and elevations before '
            'attributing it to settlement. Minor joinery issues may need no foundation work. Several '
            'connected signs justify a closer structural assessment.'),
           ('What local checks should happen before work?',
            'For a property within The Landings, confirm current community requirements and contractor '
            'access before scheduling exterior work. Provide the proposed scope rather than assuming that '
            'community approval replaces any public permit.')]},
 {'slug': 'wilmington-island-ga',
  'work': 'framing',
  'photo': 'wilmington-island-marsh.jpg',
  'photo_alt': 'Coastal marshland of the kind that surrounds Wilmington Island',
  'name': 'Wilmington Island',
  'plain': 'Wilmington Island, GA',
  'zip': '31410',
  'lede': 'Foundation and crawl-space assessment in Wilmington Island, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'For a Wilmington Island raised-floor home, inspect timber and supports separately from ground '
           'moisture. A musty crawl space does not by itself establish that piers have settled or that the '
           'floor needs lifting. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Moisture versus loss of support',
  'note': 'Trace leaks, measure accessible timber moisture and inspect joists, sill plates, connections and '
          'existing bearings. Damaged timber needs a repair design and moisture correction. Adding a jack '
          'beneath weakened wood alone does not resolve the cause.',
  'focus': ['A soft floor near a bathroom',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Wilmington Island, GA?',
            'The floor gives underfoot in one room rather than sloping evenly across the house. Photograph '
            'the affected area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Trace leaks, measure accessible timber moisture and inspect joists, sill plates, connections '
            'and existing bearings. Damaged timber needs a repair design and moisture correction. Adding a '
            'jack beneath weakened wood alone does not resolve the cause.'),
           ('What local checks should happen before work?',
            'For a Wilmington Island raised-floor home, inspect timber and supports separately from ground '
            'moisture. A musty crawl space does not by itself establish that piers have settled or that the '
            'floor needs lifting.')]},
 {'slug': 'georgetown-ga',
  'work': 'slab',
  'photo': 'georgetown-ranch-home.jpg',
  'photo_alt': "Single-story ranch home typical of Georgetown's 1970s and 1980s build-out",
  'name': 'Georgetown',
  'plain': 'Georgetown, Savannah',
  'zip': '31419',
  'lede': 'Foundation and crawl-space assessment in Georgetown, Savannah: start with the building, drainage '
          'and access at your address.',
  'facts': 'For a Georgetown address, check the actual jurisdiction and any neighborhood drainage '
           'responsibilities. A swale or shared drainage feature should not be altered as part of a repair '
           'without establishing who controls it. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Drainage beyond the property line',
  'note': 'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge route '
          'before specifying equipment. Correct bulk-water entry first. A ground membrane or dehumidifier '
          'addresses a different part of the moisture problem.',
  'focus': ['Water collects at the crawl-space entrance',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Georgetown, Savannah?',
            'A wet patch appears after heavy rain and the crawl space smells damp. Photograph the affected '
            'area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge '
            'route before specifying equipment. Correct bulk-water entry first. A ground membrane or '
            'dehumidifier addresses a different part of the moisture problem.'),
           ('What local checks should happen before work?',
            'For a Georgetown address, check the actual jurisdiction and any neighborhood drainage '
            'responsibilities. A swale or shared drainage feature should not be altered as part of a repair '
            'without establishing who controls it.')]},
 {'slug': 'midtown-savannah-ga',
  'work': 'drainage',
  'photo': 'midtown-savannah-bungalow.jpg',
  'photo_alt': "Clapboard bungalow with a deep front porch, the housing type across Savannah's midtown "
               'streets',
  'name': 'Midtown Savannah &amp; Ardsley Park',
  'plain': 'Midtown Savannah, GA',
  'zip': '31405',
  'lede': 'Foundation and crawl-space assessment in Midtown Savannah, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'Around Midtown and Ardsley Park, compare the original structure with any later addition. A '
           'change at the junction can involve separate supports or drainage paths; the age of the '
           'neighborhood alone does not explain it. Reference: <a href="https://www.thempc.org/Application" '
           'target="_blank" rel="noopener">Metropolitan Planning Commission applications</a>.',
  'note_head': 'Additions and original supports',
  'note': 'Trace leaks, measure accessible timber moisture and inspect joists, sill plates, connections and '
          'existing bearings. Damaged timber needs a repair design and moisture correction. Adding a jack '
          'beneath weakened wood alone does not resolve the cause.',
  'focus': ['A soft floor near a bathroom',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Midtown Savannah, GA?',
            'The floor gives underfoot in one room rather than sloping evenly across the house. Photograph '
            'the affected area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Trace leaks, measure accessible timber moisture and inspect joists, sill plates, connections '
            'and existing bearings. Damaged timber needs a repair design and moisture correction. Adding a '
            'jack beneath weakened wood alone does not resolve the cause.'),
           ('What local checks should happen before work?',
            'Around Midtown and Ardsley Park, compare the original structure with any later addition. A '
            'change at the junction can involve separate supports or drainage paths; the age of the '
            'neighborhood alone does not explain it.')]},
 {'slug': 'southside-savannah-ga',
  'work': 'framing',
  'photo': 'southside-cracked-driveway.jpg',
  'photo_alt': 'Cracked concrete driveway running alongside a suburban house and garage',
  'name': 'Southside Savannah',
  'plain': 'Southside Savannah, GA',
  'zip': '31406',
  'lede': 'Foundation and crawl-space assessment in Southside Savannah, GA: start with the building, '
          'drainage and access at your address.',
  'facts': 'On a Southside property, identify whether damaged concrete is a driveway, patio or part of the '
           'building foundation before discussing repair. Check where downspouts discharge and whether water '
           'crosses the affected joint. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Separate paving from structural slabs',
  'note': 'Check panel condition, roots, washout and drainage; distinguish a walkway defect from movement in '
          'the house. Leveling, replacement or drainage work may be appropriate. Repairing the walkway is '
          'not evidence that the home needs underpinning.',
  'focus': ['A trip edge on a concrete walkway',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Southside Savannah, GA?',
            'Adjacent panels no longer meet evenly. Photograph the affected area safely, note when it '
            'changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check panel condition, roots, washout and drainage; distinguish a walkway defect from movement '
            'in the house. Leveling, replacement or drainage work may be appropriate. Repairing the walkway '
            'is not evidence that the home needs underpinning.'),
           ('What local checks should happen before work?',
            'On a Southside property, identify whether damaged concrete is a driveway, patio or part of the '
            'building foundation before discussing repair. Check where downspouts discharge and whether '
            'water crosses the affected joint.')]},
 {'slug': 'isle-of-hope-ga',
  'work': 'framing',
  'photo': 'isle-of-hope-southern-home.jpg',
  'photo_alt': 'Raised Southern house with double porches under live oaks draped in Spanish moss',
  'name': 'Isle of Hope',
  'plain': 'Isle of Hope, GA',
  'zip': '31406',
  'lede': 'Foundation and crawl-space assessment in Isle of Hope, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'At an Isle of Hope property, record the crawl-space opening, available clearance and the route '
           'taken by rainwater. Check the address on the flood map rather than assuming that every lot near '
           'a creek has the same exposure. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Crawl-space access and runoff',
  'note': 'Inspect for standing water, leaks, timber damage, ventilation and equipment that may affect an '
          'enclosure design. Drainage and repairs come before enclosure. Membrane detailing and humidity '
          'control must suit the actual crawl space.',
  'focus': ['A damp crawl space with intact supports',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Isle of Hope, GA?',
            'Condensation and a musty smell are present without confirmed structural damage. Photograph the '
            'affected area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Inspect for standing water, leaks, timber damage, ventilation and equipment that may affect an '
            'enclosure design. Drainage and repairs come before enclosure. Membrane detailing and humidity '
            'control must suit the actual crawl space.'),
           ('What local checks should happen before work?',
            'At an Isle of Hope property, record the crawl-space opening, available clearance and the route '
            'taken by rainwater. Check the address on the flood map rather than assuming that every lot near '
            'a creek has the same exposure.')]},
 {'slug': 'thunderbolt-ga',
  'work': 'excavation',
  'photo': 'thunderbolt-shrimp-dock.jpg',
  'photo_alt': 'Shrimp boat and stacked crab pots tied up at a working river dock',
  'name': 'Thunderbolt',
  'plain': 'Thunderbolt, GA',
  'zip': '31404',
  'lede': 'Foundation and crawl-space assessment in Thunderbolt, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'For Thunderbolt, confirm the municipal authority for the address and use parcel-specific flood '
           'information. A nearby tidal waterway is a reason to investigate drainage and elevation, not '
           'proof of foundation failure. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Address-specific flood information',
  'note': 'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge route '
          'before specifying equipment. Correct bulk-water entry first. A ground membrane or dehumidifier '
          'addresses a different part of the moisture problem.',
  'focus': ['Water collects at the crawl-space entrance',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Thunderbolt, GA?',
            'A wet patch appears after heavy rain and the crawl space smells damp. Photograph the affected '
            'area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge '
            'route before specifying equipment. Correct bulk-water entry first. A ground membrane or '
            'dehumidifier addresses a different part of the moisture problem.'),
           ('What local checks should happen before work?',
            'For Thunderbolt, confirm the municipal authority for the address and use parcel-specific flood '
            'information. A nearby tidal waterway is a reason to investigate drainage and elevation, not '
            'proof of foundation failure.')]},
 {'slug': 'whitemarsh-island-ga',
  'work': 'drainage',
  'photo': 'whitemarsh-tidal-creeks.jpg',
  'photo_alt': 'Tidal creeks winding through salt marsh at the edge of an island community',
  'name': 'Whitemarsh Island',
  'plain': 'Whitemarsh Island, GA',
  'zip': '31410',
  'lede': 'Foundation and crawl-space assessment in Whitemarsh Island, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'On Whitemarsh Island, photographs taken safely after rainfall can help distinguish surface '
           'runoff from persistent crawl-space dampness. Include the downspouts and yard slope, and check '
           'the property flood information. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'After-rain observations',
  'note': 'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge route '
          'before specifying equipment. Correct bulk-water entry first. A ground membrane or dehumidifier '
          'addresses a different part of the moisture problem.',
  'focus': ['Water collects at the crawl-space entrance',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Whitemarsh Island, GA?',
            'A wet patch appears after heavy rain and the crawl space smells damp. Photograph the affected '
            'area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge '
            'route before specifying equipment. Correct bulk-water entry first. A ground membrane or '
            'dehumidifier addresses a different part of the moisture problem.'),
           ('What local checks should happen before work?',
            'On Whitemarsh Island, photographs taken safely after rainfall can help distinguish surface '
            'runoff from persistent crawl-space dampness. Include the downspouts and yard slope, and check '
            'the property flood information.')]},
 {'slug': 'tybee-island-ga',
  'work': 'excavation',
  'photo': 'tybee-raised-beach-house.jpg',
  'photo_alt': 'Beachfront house raised on pilings above the dune line',
  'name': 'Tybee Island',
  'plain': 'Tybee Island, GA',
  'zip': '31328',
  'lede': 'Foundation and crawl-space assessment in Tybee Island, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'At a Tybee property, establish the building elevation, flood designation and function of lower '
           'enclosures before modifying them. A moisture proposal must not casually block flood openings or '
           'change an engineered support system. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Flood openings and elevated structures',
  'note': 'Inspect for standing water, leaks, timber damage, ventilation and equipment that may affect an '
          'enclosure design. Drainage and repairs come before enclosure. Membrane detailing and humidity '
          'control must suit the actual crawl space.',
  'focus': ['A damp crawl space with intact supports',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Tybee Island, GA?',
            'Condensation and a musty smell are present without confirmed structural damage. Photograph the '
            'affected area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Inspect for standing water, leaks, timber damage, ventilation and equipment that may affect an '
            'enclosure design. Drainage and repairs come before enclosure. Membrane detailing and humidity '
            'control must suit the actual crawl space.'),
           ('What local checks should happen before work?',
            'At a Tybee property, establish the building elevation, flood designation and function of lower '
            'enclosures before modifying them. A moisture proposal must not casually block flood openings or '
            'change an engineered support system.')]},
 {'slug': 'garden-city-ga',
  'work': 'slab',
  'photo': 'garden-city-port-terminal.jpg',
  'photo_alt': 'Stacked shipping containers and a gantry crane at a river container terminal',
  'name': 'Garden City',
  'plain': 'Garden City, GA',
  'zip': '31408',
  'lede': 'Foundation and crawl-space assessment in Garden City, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'For a Garden City property, bring records of additions, converted spaces or prior support '
           'repairs. Compare the observed movement with actual load paths; nearby industrial activity is not '
           'evidence of a cause at the house. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Loads and previous alterations',
  'note': 'Review earlier repairs, drainage, footing access and loads; determine whether engineering or soil '
          'investigation is needed. A support system is selected from measured conditions and design '
          'requirements. A neighborhood name cannot establish bearing depth or pier quantity.',
  'focus': ['Movement continues after a cosmetic repair',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Garden City, GA?',
            'A repaired wall crack reopens and level readings show a change. Photograph the affected area '
            'safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Review earlier repairs, drainage, footing access and loads; determine whether engineering or '
            'soil investigation is needed. A support system is selected from measured conditions and design '
            'requirements. A neighborhood name cannot establish bearing depth or pier quantity.'),
           ('What local checks should happen before work?',
            'For a Garden City property, bring records of additions, converted spaces or prior support '
            'repairs. Compare the observed movement with actual load paths; nearby industrial activity is '
            'not evidence of a cause at the house.')]},
 {'slug': 'port-wentworth-ga',
  'work': 'driveway',
  'photo': 'port-wentworth-new-subdivision.jpg',
  'photo_alt': 'Aerial view of a recently built subdivision of similar houses on curving streets',
  'name': 'Port Wentworth',
  'plain': 'Port Wentworth, GA',
  'zip': '31407',
  'lede': 'Foundation and crawl-space assessment in Port Wentworth, GA: start with the building, drainage '
          'and access at your address.',
  'facts': 'For Port Wentworth, note whether cracks cross an addition joint or occur only in outside '
           'concrete. Construction records and level readings are more useful than assuming every local '
           'house sits on the same fill. Reference: <a '
           'href="https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens" target="_blank" '
           'rel="noopener">Chatham County flood-map guidance</a>.',
  'note_head': 'Old and new sections of a property',
  'note': 'Check whether the panel is separate from the house foundation, map the level difference, and '
          'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
          'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.',
  'focus': ['A driveway edge drops beside the garage',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Port Wentworth, GA?',
            'The outside concrete is lower than the garage floor after rain. Photograph the affected area '
            'safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check whether the panel is separate from the house foundation, map the level difference, and '
            'inspect runoff and visible voids. Sound independent flatwork may be a lifting candidate. Broken '
            'concrete, ongoing erosion or movement in a load-bearing slab changes the scope.'),
           ('What local checks should happen before work?',
            'For Port Wentworth, note whether cracks cross an addition joint or occur only in outside '
            'concrete. Construction records and level readings are more useful than assuming every local '
            'house sits on the same fill.')]},
 {'slug': 'bloomingdale-ga',
  'work': 'drainage',
  'photo': 'bloomingdale-rural-lot.jpg',
  'photo_alt': 'House set well back on a large rural lot with a gravel track and open field',
  'name': 'Bloomingdale',
  'plain': 'Bloomingdale, GA',
  'zip': '31302',
  'lede': 'Foundation and crawl-space assessment in Bloomingdale, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'For a Bloomingdale property with a detached garage or workshop, assess that foundation '
           'separately from the house. Different loads, slab construction and drainage can require different '
           'scopes even on one lot. Reference: <a '
           'href="https://www.pooler-ga.gov/online-services/applications-forms/" target="_blank" '
           'rel="noopener">City of Pooler applications and forms</a>.',
  'note_head': 'Outbuildings need their own assessment',
  'note': 'Check panel condition, roots, washout and drainage; distinguish a walkway defect from movement in '
          'the house. Leveling, replacement or drainage work may be appropriate. Repairing the walkway is '
          'not evidence that the home needs underpinning.',
  'focus': ['A trip edge on a concrete walkway',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Bloomingdale, GA?',
            'Adjacent panels no longer meet evenly. Photograph the affected area safely, note when it '
            'changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check panel condition, roots, washout and drainage; distinguish a walkway defect from movement '
            'in the house. Leveling, replacement or drainage work may be appropriate. Repairing the walkway '
            'is not evidence that the home needs underpinning.'),
           ('What local checks should happen before work?',
            'For a Bloomingdale property with a detached garage or workshop, assess that foundation '
            'separately from the house. Different loads, slab construction and drainage can require '
            'different scopes even on one lot.')]},
 {'slug': 'rincon-ga',
  'work': 'driveway',
  'photo': 'rincon-house-framing.jpg',
  'photo_alt': 'New house under construction with the wood framing up before the exterior goes on',
  'name': 'Rincon',
  'plain': 'Rincon, GA',
  'zip': '31326',
  'lede': 'Foundation and crawl-space assessment in Rincon, GA: start with the building, drainage and access '
          'at your address.',
  'facts': 'For a property inside Rincon, start with the city building office when checking permit '
           'requirements. Provide the repair scope and address; an Effingham County mailing address alone '
           'does not establish county jurisdiction. Reference: <a '
           'href="https://www.cityofrincon.com/resources/planning-development/building-zoning-fees/" '
           'target="_blank" rel="noopener">City of Rincon building and zoning</a>.',
  'note_head': 'Use the correct building office',
  'note': 'Take repeatable elevation readings and inspect the beam, pier footing and load path; note fragile '
          'finishes and utility connections. The repair may involve timber, footing or support work. A '
          'controlled adjustment target depends on the building, not a promise to make every floor perfectly '
          'level.',
  'focus': ['A hallway slopes toward an interior support',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Rincon, GA?',
            'Furniture tilts near the center of a raised floor. Photograph the affected area safely, note '
            'when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Take repeatable elevation readings and inspect the beam, pier footing and load path; note '
            'fragile finishes and utility connections. The repair may involve timber, footing or support '
            'work. A controlled adjustment target depends on the building, not a promise to make every floor '
            'perfectly level.'),
           ('What local checks should happen before work?',
            'For a property inside Rincon, start with the city building office when checking permit '
            'requirements. Provide the repair scope and address; an Effingham County mailing address alone '
            'does not establish county jurisdiction.')]},
 {'slug': 'springfield-ga',
  'work': 'framing',
  'photo': 'springfield-historic-corner.jpg',
  'photo_alt': 'Old white timber building on a small-town street corner',
  'name': 'Springfield',
  'plain': 'Springfield, GA',
  'zip': '31329',
  'lede': 'Foundation and crawl-space assessment in Springfield, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'For a Springfield property, collect earlier foundation invoices or drawings and identify which '
           'supports were changed. Check the city permit route for an address inside the city before '
           'committing to structural alterations. Reference: <a href="https://springfieldga.org/" '
           'target="_blank" rel="noopener">City of Springfield</a>.',
  'note_head': 'Document earlier repairs',
  'note': 'Review earlier repairs, drainage, footing access and loads; determine whether engineering or soil '
          'investigation is needed. A support system is selected from measured conditions and design '
          'requirements. A neighborhood name cannot establish bearing depth or pier quantity.',
  'focus': ['Movement continues after a cosmetic repair',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Springfield, GA?',
            'A repaired wall crack reopens and level readings show a change. Photograph the affected area '
            'safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Review earlier repairs, drainage, footing access and loads; determine whether engineering or '
            'soil investigation is needed. A support system is selected from measured conditions and design '
            'requirements. A neighborhood name cannot establish bearing depth or pier quantity.'),
           ('What local checks should happen before work?',
            'For a Springfield property, collect earlier foundation invoices or drawings and identify which '
            'supports were changed. Check the city permit route for an address inside the city before '
            'committing to structural alterations.')]},
 {'slug': 'hinesville-ga',
  'work': 'level',
  'photo': 'hinesville-brick-home.jpg',
  'photo_alt': "Single-story brick home with a lawn and attached garage, typical of the area's rental "
               'housing',
  'name': 'Hinesville',
  'plain': 'Hinesville, GA',
  'zip': '31313',
  'lede': 'Foundation and crawl-space assessment in Hinesville, GA: start with the building, drainage and '
          'access at your address.',
  'facts': 'For Hinesville, arrange owner authorization and access to all affected rooms and the crawl '
           'space. Send the proposed structural scope to the relevant inspections office when confirming '
           'permit requirements. Reference: <a '
           'href="https://www.cityofhinesville.org/128/Inspections-Department" target="_blank" '
           'rel="noopener">City of Hinesville inspections</a>.',
  'note_head': 'Inspection access and repair records',
  'note': 'Check hinges and seasonal swelling, then compare nearby cracks and elevations before attributing '
          'it to settlement. Minor joinery issues may need no foundation work. Several connected signs '
          'justify a closer structural assessment.',
  'focus': ['A door starts sticking after a wet season',
            'Documented levels and accessible support condition',
            'Drainage and repair-scope review'],
  'faqs': [('What should I record before an inspection in Hinesville, GA?',
            'One door binds, but the owner has not recorded floor or crack changes. Photograph the affected '
            'area safely, note when it changed, and bring any earlier repair records.'),
           ('Does this symptom prove I need foundation repair?',
            'Check hinges and seasonal swelling, then compare nearby cracks and elevations before '
            'attributing it to settlement. Minor joinery issues may need no foundation work. Several '
            'connected signs justify a closer structural assessment.'),
           ('What local checks should happen before work?',
            'For Hinesville, arrange owner authorization and access to all affected rooms and the crawl '
            'space. Send the proposed structural scope to the relevant inspections office when confirming '
            'permit requirements.')]}]

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
    ("The islands and the riverside", "Address-specific flood information, crawl-space access and drainage checks.",
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
      <p class="lede">Find your area for inspection planning, local references and the property details that can affect a repair.</p>
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
        <p class="muted">Explore Chatham County and nearby communities in Bryan, Effingham and Liberty. Check local inspection planning and permit contacts, then confirm coverage for your exact address.</p>
      </div>
    </div>
  </section>
{groups}

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Not Listed?</span>
          <h2>Check service at your address</h2>
          <p>Send the property address and a short description of the issue so coverage and inspection access can be confirmed before an appointment.</p>
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
