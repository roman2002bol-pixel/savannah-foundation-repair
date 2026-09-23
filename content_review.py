from pathlib import Path
import re, json, ast

ROOT = Path(__file__).resolve().parent

CSS = '''
/* Practical examples: editorial guidance, never presented as completed jobs. */
.field-guide { border-top:1px solid var(--border,#ddd); }
.field-guide .guide-intro { max-width:70ch; }
.field-guide .guide-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,280px),1fr)); gap:1.25rem; }
.field-guide article { border:1px solid var(--border,#ddd); border-radius:12px; padding:1.5rem; background:var(--surface,#fff); color:var(--ink,#182b32); }
.field-guide h3 { margin-top:0; font-size:1.3rem; }
.field-guide dt { font-weight:700; margin-top:1rem; }
.field-guide dd { margin:.3rem 0 0; line-height:1.65; }
.field-guide .guide-source { font-size:.9rem; margin-top:1.5rem; max-width:75ch; }
.hero-trust strong { font-size:1.05rem; }
@media(max-width:600px) { .field-guide article { padding:1.1rem; } .hero-trust { gap:1rem; } }
'''

F_CASES = {
'crack': ('A stair-step crack beside a window', 'A masonry joint opens near a window, but a photograph does not establish whether movement is active.', 'Record crack width and dates, compare floor elevations, inspect the support below and check whether doors have changed.', 'A stable surface defect may need monitoring or masonry work. Active movement requires a support assessment before cosmetic sealing.'),
'slab': ('A driveway edge drops beside the garage', 'The outside concrete is lower than the garage floor after rain.', 'Check whether the panel is separate from the house foundation, map the level difference, and inspect runoff and visible voids.', 'Sound independent flatwork may be a lifting candidate. Broken concrete, ongoing erosion or movement in a load-bearing slab changes the scope.'),
'framing': ('A soft floor near a bathroom', 'The floor gives underfoot in one room rather than sloping evenly across the house.', 'Trace leaks, measure accessible timber moisture and inspect joists, sill plates, connections and existing bearings.', 'Damaged timber needs a repair design and moisture correction. Adding a jack beneath weakened wood alone does not resolve the cause.'),
'drainage': ('Water collects at the crawl-space entrance', 'A wet patch appears after heavy rain and the crawl space smells damp.', 'Follow roof discharge and surface runoff, inspect plumbing, and identify a lawful discharge route before specifying equipment.', 'Correct bulk-water entry first. A ground membrane or dehumidifier addresses a different part of the moisture problem.'),
'encapsulation': ('A damp crawl space with intact supports', 'Condensation and a musty smell are present without confirmed structural damage.', 'Inspect for standing water, leaks, timber damage, ventilation and equipment that may affect an enclosure design.', 'Drainage and repairs come before enclosure. Membrane detailing and humidity control must suit the actual crawl space.'),
'level': ('A hallway slopes toward an interior support', 'Furniture tilts near the center of a raised floor.', 'Take repeatable elevation readings and inspect the beam, pier footing and load path; note fragile finishes and utility connections.', 'The repair may involve timber, footing or support work. A controlled adjustment target depends on the building, not a promise to make every floor perfectly level.'),
'inspection': ('A door starts sticking after a wet season', 'One door binds, but the owner has not recorded floor or crack changes.', 'Check hinges and seasonal swelling, then compare nearby cracks and elevations before attributing it to settlement.', 'Minor joinery issues may need no foundation work. Several connected signs justify a closer structural assessment.'),
'excavation': ('Movement continues after a cosmetic repair', 'A repaired wall crack reopens and level readings show a change.', 'Review earlier repairs, drainage, footing access and loads; determine whether engineering or soil investigation is needed.', 'A support system is selected from measured conditions and design requirements. A neighborhood name cannot establish bearing depth or pier quantity.'),
'driveway': ('A trip edge on a concrete walkway', 'Adjacent panels no longer meet evenly.', 'Check panel condition, roots, washout and drainage; distinguish a walkway defect from movement in the house.', 'Leveling, replacement or drainage work may be appropriate. Repairing the walkway is not evidence that the home needs underpinning.')}
T_CASES = {
'tree-removal': ('A tree crowds a roof and fence', 'Branches extend over a roof and the trunk is close to a boundary.', 'Inspect tree condition, ownership, lean, overhead services, gate width and space for controlled lowering.', 'Retention or pruning may be possible. If removal is justified, access and targets determine the dismantling method and debris plan.'),
'emergency-storm-tree-removal': ('A storm leaves a suspended branch', 'A broken limb is caught above a driveway.', 'Keep people clear. Identify utility involvement from a safe position and report a tree touching a line to the utility.', 'The site must be made safe before cutting begins. Arrival timing depends on access, hazards and storm demand, and must be confirmed.'),
'large-hazardous-tree-removal': ('A large leaning tree beside a house', 'The crown extends over a building and there is little clear landing space.', 'Assess changes in lean, root-plate disturbance, defects, loads and equipment access; determine whether specialist tree-risk assessment is needed.', 'Rigging or a crane may be considered after the site assessment. Tree size alone does not decide whether a crane is appropriate.'),
'tree-trimming-pruning': ('Branches rub against a roof', 'Live limbs contact roofing when the wind moves them.', 'Identify the species, branch attachments, deadwood and the clearance needed without stripping the canopy.', 'Specify individual cuts and a pruning objective. Topping is not a substitute for a considered clearance plan.'),
'stump-grinding-removal': ('A stump blocks a new garden bed', 'The owner wants to plant where a tree once stood.', 'Check underground utilities, irrigation, gate width, surrounding hardscape and the intended planting depth.', 'Agree on grinding depth, chip removal, backfill and remaining roots. Grinding a stump does not remove the entire root system.')}
N_CASES = {
'standard-detail': ('Sand after a beach visit', 'Loose sand collects in mats, seat tracks and the cargo area.', 'Identify fabric and trim materials, separate removable mats and check whether sand is loose or embedded.', 'A maintenance detail suits light buildup. Embedded sand, stains or heavy pet hair may require a deeper interior service and a revised quote.'),
'interior-deep-clean': ('A drink spill in a fabric seat', 'A visible ring and odor remain after the surface dries.', 'Identify the material, spill history, colorfastness and moisture near switches or seat electronics.', 'Test the cleaning method in a small area and control moisture. Old staining or odor below the upholstery may not be fully removable.'),
'full-detail': ('A daily driver needs an interior and paint reset', 'The cabin has accumulated dirt and the paint feels rough after washing.', 'Assess interior materials, bonded exterior contamination and visible paint defects under suitable lighting.', 'Cleaning and decontamination address dirt and deposits. Paint correction is a separate decision based on finish condition, not an automatic promise of scratch removal.'),
'ceramic-coating': ('A dark car shows swirls in sunlight', 'The owner wants protection but also expects the swirls to disappear.', 'Inspect the washed paint, discuss correction goals and establish a suitable sheltered application and curing arrangement.', 'Correction and surface preparation come before coating where required. A coating does not fill deep scratches or make paint immune to water spots.')}

SAV = ('Savannah tree ordinance guidance','https://www.savannahga.gov/763/Tree-Ordinance-Administration')
FLOOD = ('Chatham County flood-map guidance','https://engineering.chathamcountyga.gov/FloodZones/FactsForCitizens')
DOE = ('U.S. Department of Energy crawl-space moisture guidance','https://bsesc.energy.gov/energy-basics/crawlspace-capillary-break-crawlspace-floors')
MPC = ('Metropolitan Planning Commission applications','https://www.thempc.org/Application')
POOL = ('City of Pooler applications and forms','https://www.pooler-ga.gov/online-services/applications-forms/')
BRYAN = ('Bryan County building inspections','https://www.bryancountyga.gov/government/departments-a-g/community-development/building-and-codes/building-inspections')
LAND = ('The Landings resident service guidance','https://landings.org/member-welcome-guide/')
LOCAL = {
'downtown-savannah': ('Historic finishes and access', 'For a property in a Savannah historic district, establish whether visible exterior changes need preservation review. Record fragile masonry and plaster before planning any lift; street access also affects equipment staging.', MPC, 'crack'),
'midtown-savannah': ('Additions and original supports', 'Around Midtown and Ardsley Park, compare the original structure with any later addition. A change at the junction can involve separate supports or drainage paths; the age of the neighborhood alone does not explain it.', MPC, 'framing'),
'southside-savannah': ('Separate paving from structural slabs', 'On a Southside property, identify whether damaged concrete is a driveway, patio or part of the building foundation before discussing repair. Check where downspouts discharge and whether water crosses the affected joint.', FLOOD, 'driveway'),
'georgetown': ('Drainage beyond the property line', 'For a Georgetown address, check the actual jurisdiction and any neighborhood drainage responsibilities. A swale or shared drainage feature should not be altered as part of a repair without establishing who controls it.', FLOOD, 'drainage'),
'isle-of-hope': ('Crawl-space access and runoff', 'At an Isle of Hope property, record the crawl-space opening, available clearance and the route taken by rainwater. Check the address on the flood map rather than assuming that every lot near a creek has the same exposure.', FLOOD, 'encapsulation'),
'thunderbolt': ('Address-specific flood information', 'For Thunderbolt, confirm the municipal authority for the address and use parcel-specific flood information. A nearby tidal waterway is a reason to investigate drainage and elevation, not proof of foundation failure.', FLOOD, 'drainage'),
'whitemarsh-island': ('After-rain observations', 'On Whitemarsh Island, photographs taken safely after rainfall can help distinguish surface runoff from persistent crawl-space dampness. Include the downspouts and yard slope, and check the property flood information.', FLOOD, 'drainage'),
'wilmington-island': ('Moisture versus loss of support', 'For a Wilmington Island raised-floor home, inspect timber and supports separately from ground moisture. A musty crawl space does not by itself establish that piers have settled or that the floor needs lifting.', FLOOD, 'framing'),
'skidaway-island': ('Community review and work access', 'For a property within The Landings, confirm current community requirements and contractor access before scheduling exterior work. Provide the proposed scope rather than assuming that community approval replaces any public permit.', LAND, 'inspection'),
'tybee-island': ('Flood openings and elevated structures', 'At a Tybee property, establish the building elevation, flood designation and function of lower enclosures before modifying them. A moisture proposal must not casually block flood openings or change an engineered support system.', FLOOD, 'encapsulation'),
'garden-city': ('Loads and previous alterations', 'For a Garden City property, bring records of additions, converted spaces or prior support repairs. Compare the observed movement with actual load paths; nearby industrial activity is not evidence of a cause at the house.', FLOOD, 'excavation'),
'port-wentworth': ('Old and new sections of a property', 'For Port Wentworth, note whether cracks cross an addition joint or occur only in outside concrete. Construction records and level readings are more useful than assuming every local house sits on the same fill.', FLOOD, 'slab'),
'pooler': ('Check the panel before choosing a repair', 'For a Pooler driveway or garage apron, determine whether the affected concrete is independent flatwork. Review drainage and construction records where available; a newer house does not prove poor compaction or establish a warranty outcome.', POOL, 'slab'),
'bloomingdale': ('Outbuildings need their own assessment', 'For a Bloomingdale property with a detached garage or workshop, assess that foundation separately from the house. Different loads, slab construction and drainage can require different scopes even on one lot.', ('City of Bloomingdale planning and zoning','https://www.bloomingdale-ga.gov/planning-zoning'), 'driveway'),
'richmond-hill': ('City and county boundaries matter', 'A Richmond Hill mailing address does not by itself identify the permit authority. Bryan County building inspection guidance applies to unincorporated areas; confirm city limits before submitting a scope.', BRYAN, 'slab'),
'rincon': ('Use the correct building office', 'For a property inside Rincon, start with the city building office when checking permit requirements. Provide the repair scope and address; an Effingham County mailing address alone does not establish county jurisdiction.', ('City of Rincon building and zoning','https://www.cityofrincon.com/resources/planning-development/building-zoning-fees/'), 'level'),
'springfield': ('Document earlier repairs', 'For a Springfield property, collect earlier foundation invoices or drawings and identify which supports were changed. Check the city permit route for an address inside the city before committing to structural alterations.', ('City of Springfield','https://springfieldga.org/'), 'excavation'),
'hinesville': ('Inspection access and repair records', 'For Hinesville, arrange owner authorization and access to all affected rooms and the crawl space. Send the proposed structural scope to the relevant inspections office when confirming permit requirements.', ('City of Hinesville inspections','https://www.cityofhinesville.org/128/Inspections-Department'), 'inspection')}

def local_for(slug):
    if 'historic-district' in slug: return LOCAL['downtown-savannah']
    return next((v for k,v in LOCAL.items() if k in slug), None)

def block(cases, local=None):
    cards = ''.join('<article><h3>'+c[0]+'</h3><dl>'+''.join('<dt>'+label+'</dt><dd>'+body+'</dd>' for label,body in zip(['Situation','What to check','How the findings change the plan'],c[1:]))+'</dl></article>' for c in cases)
    loc = ''
    if local:
        heading,body,source,*_ = local
        loc = f'<div class="guide-source"><h3>{heading}</h3><p>{body}</p><p>Local reference: <a href="{source[1]}" target="_blank" rel="noopener">{source[0]}</a>.</p></div>'
    return '\n<!-- FIELD-GUIDE START -->\n<section class="field-guide"><div class="container"><span class="eyebrow">Repair &amp; service examples</span><h2>What the work can involve</h2><p class="guide-intro">Illustrative scenarios, not completed customer projects. The inspection and agreed scope determine the work for your property.</p><div class="guide-grid">'+cards+'</div>'+loc+'</div></section>\n<!-- FIELD-GUIDE END -->\n'

def replace_element(text, pattern, replacement):
    m=re.search(pattern,text)
    if not m: return text
    tag=re.match(r'<(\w+)',m.group()).group(1)
    depth=0
    for t in re.finditer(r'</?'+tag+r'\b[^>]*>',text[m.start():]):
        depth += -1 if t.group().startswith('</') else 1
        if depth==0: return text[:m.start()]+replacement+text[m.start()+t.end():]
    raise ValueError(pattern)

def apply_site(site):
    kind='foundation' if 'foundation' in site.name else 'tree' if 'tree-removal' in site.name else 'nexus'
    for path in site.rglob('*.html'):
        if any(p.startswith('.') for p in path.relative_to(site).parts): continue
        text=path.read_text(encoding='utf-8'); original=text
        slug=path.stem; rel=path.relative_to(site).as_posix()
        text=re.sub(r'\n?<!-- FIELD-GUIDE START -->.*?<!-- FIELD-GUIDE END -->\n?', '', text, flags=re.S)
        text=re.sub(r'(css/style\.css\?v=)[^"\s]+',r'\g<1>20260922',text)
        cases=[]; local=None
        if kind=='foundation':
            if rel.startswith('service-areas/') and slug!='index':
                local=local_for(slug); cases=[F_CASES[local[3]]] if local else []
            elif rel.startswith('services/'):
                key=next((k for term,k in [('crack','crack'),('encapsulation','encapsulation'),('crawl','framing'),('slab','slab'),('level','level'),('pier','excavation')] if term in slug),'inspection')
                cases=[F_CASES[key]];local=('Moisture is one part of the investigation','For Savannah-area crawl spaces, identify bulk-water entry before choosing a membrane or humidity equipment. Moisture control and structural support repair solve different problems.',DOE)
            elif slug=='index' and '/' not in rel: cases=[F_CASES['framing'],F_CASES['slab']]
            text=replace_element(text,r'<div class="stat-row">','')
            text=text.replace('Foundation Repair &amp; Crawl Space Stabilization <span class="accent">in Savannah, GA</span>','Foundation Repair <span class="accent">in Savannah, GA</span>')
            text=text.replace('Sagging floors, cracked walls, and settling foundations don\'t level out on their own. We find what moved and why, then fix the support underneath it – across Savannah and Chatham County.','Sagging floors, cracked walls or settling concrete? Start with an on-site assessment of the supports, levels and drainage.')
            text=re.sub(r'<p>Plenty of foundation quotes.*?</p>','<p>A crack photo cannot show what the supports are doing. Compare floor elevations, inspect accessible framing and footings, and trace water entry before choosing jacks, piers, concrete lifting or monitoring.</p>',text,flags=re.S)
            text=re.sub(r'<p>We work Chatham County and the counties around it rather.*?</p>','<p>The same symptom can have different causes on neighboring properties. The written scope should identify the evidence, any inaccessible areas, the proposed repair and its limits.</p>',text,flags=re.S)
        elif kind=='tree':
            if rel.startswith('services/'): cases=[T_CASES[slug]]
            elif rel.startswith('service-areas/') and slug!='index':
                entry=local_for(slug)
                source=POOL if 'pooler' in slug else LAND if 'skidaway' in slug else SAV if 'historic' in slug else BRYAN if 'richmond' in slug else FLOOD
                body={'pooler-ga':'Pooler lists a tree-removal permit application. Check whether the proposed removal and property fall within its requirements before scheduling; also confirm any neighborhood review.', 'skidaway-island-the-landings':'For a property in The Landings, confirm current tree-work review and contractor access through resident services. Public requirements and community approval are separate checks.', 'historic-district-downtown-savannah':'For a downtown Savannah site, check tree-ordinance applicability and the space available for trucks, pedestrians and controlled lowering. Confirm ownership of street-side trees before specifying removal.', 'richmond-hill-ga':'Confirm whether the address is inside Richmond Hill or unincorporated Bryan County before checking tree-work requirements. Include boundaries, access and the proposed scope in the inquiry.'}.get(slug,'For this address, verify tree ownership, gate width, overhead services and drainage-sensitive equipment routes. In the Savannah area, a mailing address alone does not establish which tree rules apply; confirm the jurisdiction and any neighborhood review.')
                local=('Before scheduling at this address',body,source)
                cases=[T_CASES['large-hazardous-tree-removal' if 'island' in slug else 'tree-removal']]
            elif rel=='index.html': cases=[T_CASES['tree-removal'],T_CASES['stump-grinding-removal']]
            text=text.replace('Same-day response for trees down on your house, car, or driveway after a storm.','Storm-damaged tree assessment and removal, with access and arrival time confirmed for the situation.')
        else:
            if rel.startswith('services/'): cases=[N_CASES[slug]]
            elif rel.startswith('areas/') or rel=='index.html': cases=[N_CASES['standard-detail'],N_CASES['ceramic-coating']]
            if cases: local=('Preparing a Ponte Vedra appointment','For a home or office appointment, confirm parking permission, space around the vehicle and any community access instructions. Coastal sand needs careful removal before wiping surfaces; choose a work position that controls runoff and keeps wash water away from storm drains.',('St. Johns County stormwater guidance','https://www.sjcfl.us/stormwater-pollution/'))
            text=text.replace('Mobile Detailing That Comes to You – Ponte Vedra Beach &amp; St. Johns County','Mobile Detailing in Ponte Vedra Beach')
            text=text.replace('Upfront pricing, no surprises, 365 days a year.','Tell us about your vehicle and location; we confirm the scope, price and appointment with you.')
            text=text.replace('Book Now','Request an Appointment')
            text=re.sub(r'<p>Pick a slot, tell us about the car,.*?</p>','<p>Send your vehicle details and preferred time, or call us. Your appointment is confirmed directly, and pricing is agreed before work starts.</p>',text,flags=re.S)
        if 'class="hero-trust"' in text:
            labels={'foundation':[('Floor levels','Compare movement across rooms'),('Support condition','Inspect accessible framing and bearings'),('Water paths','Trace drainage and moisture')], 'tree':[('Tree condition','Defects, lean and nearby targets'),('Site access','Gate width and equipment route'),('Written scope','Removal, stump and debris details')], 'nexus':[('From $120','Standard detail starting price'),('At your location','Home or office appointments'),('Direct confirmation','Agree on scope and time')]}[kind]
            text=replace_element(text,r'<div class="hero-trust">','<div class="hero-trust">'+''.join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a,b in labels)+'</div>')
        if cases:
            addition=block(cases,local)
            if kind=='nexus': addition=addition.replace('Repair &amp; service examples','Detailing examples').replace('for your property','for your vehicle')
            # Insert before the final CTA so the guide belongs to the page, outside existing sections.
            cta=text.rfind('<div class="cta-band">')
            at=text.rfind('<section',0,cta) if cta>=0 else -1
            if at<0: at=text.find('</main>')
            if at<0: at=text.find('<footer')
            if at<0: raise ValueError(path)
            text=text[:at]+addition+text[at:]
        if text!=original: path.write_text(text,encoding='utf-8')
    if kind == 'foundation':
        from local_research import apply_site as apply_local_research
        apply_local_research(site)
    css=site/'css/style.css'; text=css.read_text(encoding='utf-8')
    if '/* Practical examples:' not in text: css.write_text(text+CSS,encoding='utf-8')

if __name__ == "__main__":
    apply_site(ROOT)
