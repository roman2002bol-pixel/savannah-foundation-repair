#!/usr/bin/env python3
"""Core page generation. Run: python build_core.py"""
from build_pages import (ROOT, SITE, BRAND, AREAS, PHONE_DISPLAY, PHONE_HREF, EMAIL,
                         SERVICES, head, header, footer, cta_band, breadcrumb,
                         faq_blocks, faq_schema, write)
from build_services import PAGES as SERVICE_PAGES, TABS as SERVICE_TABS
import json

D = 0


def service_tabs():
    """The homepage services showcase: a tab rail plus one panel per service.

    Single-sourced from build_services.TABS so a service cannot appear on the
    homepage with copy that contradicts its own page. Without JS every panel
    stays visible (nothing carries [hidden] until main.js runs), so the block
    degrades to a readable stack rather than to one panel and four dead tabs.
    """
    nl = chr(10)
    tabs, panels = [], []
    for i, svc in enumerate(SERVICE_PAGES):
        t = SERVICE_TABS[svc["slug"]]
        tid, pid = f'svctab-{svc["slug"]}', f'svcpanel-{svc["slug"]}'
        sel = "true" if i == 0 else "false"
        tabs.append(
            f'          <button class="svc-tab" type="button" role="tab" data-svc-tab'
            f' id="{tid}" aria-controls="{pid}" aria-selected="{sel}">{svc["nav"]}</button>')
        points = nl.join(f'              <li>{pt}</li>' for pt in t["points"])
        panels.append(
            f'        <div class="svc-panel" role="tabpanel" data-svc-panel id="{pid}"'
            f' aria-labelledby="{tid}"'
            f' style="background-image:linear-gradient(100deg, rgba(11,26,41,.97) 0%,'
            f' rgba(11,26,41,.93) 38%, rgba(11,26,41,.12) 100%),'
            f' url(&quot;images/{svc["photo"]}&quot;)">\n'
            f'          <div class="svc-panel-body">\n'
            f'            <h3>{svc["nav"]} <span class="accent">{t["accent"]}</span></h3>\n'
            f'            <p>{t["blurb"]}</p>\n'
            f'            <ul class="svc-points">\n{points}\n            </ul>\n'
            f'            <div class="svc-actions">\n'
            f'              <a class="btn btn-primary" href="services/{svc["slug"]}.html">'
            f'See how it is done</a>\n'
            f'              <a class="btn btn-ghost" href="free-inspection.html">'
            f'Get a free inspection</a>\n'
            f'            </div>\n'
            f'          </div>\n'
            f'        </div>')
    return ('      <div class="svc-tabs" data-svc-tabs>\n'
            '        <div class="svc-tablist" role="tablist" aria-label="Services">\n'
            + nl.join(tabs) + '\n        </div>\n'
            '        <div class="svc-panels">\n' + nl.join(panels) + '\n        </div>\n'
            '      </div>')


def patch_home_faq():
    """index.html is hand-written, but its FAQ is NOT -- it is stamped in here
    from the same FAQS list faq.html uses, between the marker comments. That is
    what keeps the homepage FAQ, the FAQ page, and both FAQPage blocks in sync."""
    import re
    path = ROOT / "index.html"
    s = path.read_text(encoding="utf-8")
    nl = chr(10)
    body = (faq_blocks(FAQS[:5]) + nl
            + '      <p class="text-center" style="margin-top:1.5rem">Still not sure what '
              'you are looking at? <a class="link" href="free-inspection.html">Book a free '
              'inspection →</a></p>')
    schema = '<script type="application/ld+json">' + nl + faq_schema(FAQS[:5]) + nl + '</script>'
    chev = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
            '<path d="M9 18l6-6-6-6"/></svg>')
    areas = nl.join(
        f'        <a class="area-chip" href="service-areas/{slug}.html">{label} {chev}</a>'
        for slug, label, _ in AREAS)
    areas += (nl + '        <a class="area-chip" href="service-areas/index.html">'
                   f'All service areas {chev}</a>')
    for start, end, new in (("<!-- FAQ-BODY:START -->", "<!-- FAQ-BODY:END -->", body),
                            ("<!-- FAQ-SCHEMA:START -->", "<!-- FAQ-SCHEMA:END -->", schema),
                            ("<!-- AREAS:START -->", "<!-- AREAS:END -->", areas),
                            ("<!-- SERVICE-TABS:START -->", "<!-- SERVICE-TABS:END -->",
                             service_tabs())):
        pattern = re.escape(start) + r".*?" + re.escape(end)
        s, n = re.subn(pattern, lambda _m: start + nl + new + nl + end, s, flags=re.S)
        assert n == 1, f"marker {start} not found exactly once in index.html"
    path.write_text(s, encoding="utf-8")
    print(f"  patched index.html FAQ ({len(FAQS)} questions)")


def page(slug, title, desc, body, schemas=None):
    url = f"{SITE}/{slug}"
    return (head(D, title, desc, url, schemas or
                 [breadcrumb([("Home", f"{SITE}/"), (title.split(" | ")[0], None)])])
            + header(D) + body + footer(D))


# --------------------------------------------------------------- inspection
INSPECTION_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / Free Inspection</div>
      <h1>Book a Free Structural Inspection</h1>
      <p class="lede">Elevation readings, a look at the actual failure, and a written scope with a real number – before you commit to anything, and at no cost whether you go ahead or not.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Request an Inspection</span>
          <h2>Tell us what you're seeing</h2>
          <p>The more specific you can be about the symptom and when it started, the more useful the first visit is. A photo by text before we arrive helps too.</p>
          <form data-quote-form data-endpoint-ready="false">
            <div class="form-grid cols-2">
              <div class="field">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required autocomplete="name">
              </div>
              <div class="field">
                <label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" required autocomplete="tel">
              </div>
            </div>
            <div class="form-grid cols-2" style="margin-top:1rem">
              <div class="field">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" autocomplete="email">
              </div>
              <div class="field">
                <label for="zip">Property ZIP code</label>
                <input type="text" id="zip" name="zip" required inputmode="numeric" autocomplete="postal-code" placeholder="e.g. 31401">
              </div>
            </div>
            <div class="field" style="margin-top:1rem">
              <label for="issue">What are you noticing?</label>
              <select id="issue" name="issue">
                <option>Sagging or bouncy floors</option>
                <option>Cracks in drywall, brick, or foundation</option>
                <option>Doors or windows sticking</option>
                <option>Sinking concrete driveway or patio</option>
                <option>Moisture or standing water in the crawl space</option>
                <option>Not sure – need it looked at</option>
              </select>
            </div>
            <div class="field" style="margin-top:1rem">
              <label for="details">When did you first notice it, and is it getting worse?</label>
              <textarea id="details" name="details" rows="4"></textarea>
            </div>
            <button class="btn btn-primary btn-block" type="submit" style="margin-top:1.25rem">Request My Free Inspection</button>
            <p class="form-status" data-form-status role="status"></p>
            <p class="field-note" style="margin-top:.75rem">We use your details to arrange the inspection and nothing else.</p>
          </form>
        </div>
        <div class="feature-card">
          <h3 style="margin-top:0">Faster by phone</h3>
          <p class="muted">If there's water standing under the house right now, or the floor moved suddenly, call rather than filling in a form.</p>
          <p><a class="btn btn-primary btn-block" href="tel:{PHONE_HREF}">Call {PHONE_DISPLAY}</a></p>
          <p style="margin-bottom:0"><a class="btn btn-outline btn-block" href="sms:{PHONE_HREF}">Send a photo by text</a></p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">What Happens</span>
        <h2>What the inspection actually involves</h2>
      </div>
      <div class="service-grid">
        <div class="service-card">
          <h3><span class="step-num">1</span> Elevation readings</h3>
          <p>Measurements across the floor to establish where the low points are and how far out of level things have gone. This is the part that turns opinion into numbers.</p>
        </div>
        <div class="service-card">
          <h3><span class="step-num">2</span> Under the house</h3>
          <p>Into the crawl space where there is one, checking framing, piers, moisture, and drainage – or a close look at the slab and the exterior where there isn't.</p>
        </div>
        <div class="service-card">
          <h3><span class="step-num">3</span> Findings, in writing</h3>
          <p>What we found, what it means, what it costs to fix, and what happens if you leave it. If nothing needs doing, that is what the report says.</p>
        </div>
      </div>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Permits</span>
          <h2>Does foundation work need a permit here?</h2>
          <p>Structural repair usually does. In unincorporated Chatham County the authority is <a href="https://buildingsafety.chathamcountyga.gov/PermitsInspections/WhenPermitsRequired" target="_blank" rel="noopener">Chatham County Building Safety &amp; Regulatory Services</a>, which publishes exactly when a permit is required – underpinning, structural framing replacement and foundation alterations generally fall inside that. Inside Savannah city limits, and in a historic district especially, the city is the authority instead.</p>
          <p>Work in Bryan County (Richmond Hill) goes through that county rather than Chatham, and a gated community such as The Landings adds its own architectural review on top of the public permit.</p>
          <p class="muted">We raise whichever applies at the inspection rather than discovering it once a crew is on site. If a job genuinely does not need a permit, we will say so rather than padding the timeline.</p>
        </div>
        <div class="feature-card">
          <h3 style="margin-top:0">Check before you schedule</h3>
          <p class="muted">The county publishes its own guidance on when a building permit is required, which is worth a look if you are comparing quotes.</p>
          <p style="margin-bottom:0"><a class="btn btn-outline btn-block" href="https://buildingsafety.chathamcountyga.gov/PermitsInspections/WhenPermitsRequired" target="_blank" rel="noopener">Chatham County permit guidance</a></p>
        </div>
      </div>
    </div>
  </section>
{cta_band(D, "Prefer to just talk it through first?", "Call and describe it – sometimes that is enough to tell you whether a visit is even warranted.")}'''

# --------------------------------------------------------------------- about
ABOUT_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / About</div>
      <h1>About {BRAND}</h1>
      <p class="lede">Foundation and crawl-space repair planning for Savannah and nearby communities, based on the condition of each property.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Our Approach</span>
          <h2>Diagnose first, quote second</h2>
          <p>A useful inspection connects visible symptoms to the supports below. Record elevation readings, accessible framing and footing condition, water paths and any earlier repairs before selecting a method.</p>
          <p>Ask for the findings in writing, including any area that could not be inspected. The outcome may be a repair scope, monitoring or further investigation; each recommendation should explain the evidence supporting it.</p>
          <h2 style="margin-top:2rem">Moisture, materials and the repair scope</h2>
          <p>For a Savannah-area home, investigate water entry and material condition alongside movement. Soil, drainage, foundation type and exposure vary between properties. Corroded connectors or damaged timber need to be documented rather than assumed from the address.</p>
          <p>The proposed materials, corrosion protection, drainage work and structural connections should be stated in the scope. Enclosure or dehumidification is considered where the moisture assessment supports it, not automatically attached to every structural repair.</p>
        </div>
        <div class="local-callout">
          <h3 style="margin-top:0">Straight about what we are</h3>
          <p>We connect homeowners in the Savannah area with foundation and crawl-space repair services. Inspections take place at the property; there is no walk-in office.</p>
          <p style="margin-bottom:0">Before authorizing work, confirm the contractor carrying it out, the written scope, permit responsibilities, payment terms and any warranty offered for that specific repair.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section-alt">
    <div class="container">
      <div class="section-head center">
        <span class="eyebrow">What We Do</span>
        <h2>Five repairs, done properly</h2>
      </div>
      <div class="service-grid">
''' + "\n".join(f'''        <div class="service-card">
          <h3><a href="services/{slug}.html" style="color:inherit">{name}</a></h3>
          <a class="link" href="services/{slug}.html">See details →</a>
        </div>''' for slug, name in SERVICES) + f'''
      </div>
    </div>
  </section>
{cta_band(D, "Want a real answer about your house?", "Free structural inspection, measurements included, no obligation attached.")}'''

# ------------------------------------------------------------------- contact
CONTACT_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / Contact</div>
      <h1>Contact {BRAND}</h1>
      <p class="lede">Call, text a photo, or send a message – whichever suits. Fastest response is the phone.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="two-col-layout">
        <div>
          <span class="eyebrow">Get In Touch</span>
          <h2>How to reach us</h2>
          <ul class="package-list">
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.12.9.34 1.79.65 2.65a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.43-1.27a2 2 0 0 1 2.11-.45c.86.31 1.75.53 2.65.65A2 2 0 0 1 22 16.92z"/></svg><a href="tel:{PHONE_HREF}">{PHONE_DISPLAY}</a></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2Z"/></svg><a href="sms:{PHONE_HREF}">Text a photo of the problem</a></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16v16H4z"/><path d="m4 6 8 6 8-6"/></svg><a href="mailto:{EMAIL}">{EMAIL}</a></li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>Monday to Saturday, 7am – 6pm</li>
            <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 12-9 12s-9-5-9-12a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>Serving Savannah &amp; Chatham County, GA</li>
          </ul>
          <p class="muted">We work out of vehicles and job sites rather than a storefront, so there is no walk-in office to visit – but there is always someone reachable on the number above during working hours.</p>
        </div>
        <div>
          <span class="eyebrow">Send a Message</span>
          <h2>Or write to us here</h2>
          <form data-quote-form data-endpoint-ready="false">
            <div class="form-grid cols-2">
              <div class="field">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required autocomplete="name">
              </div>
              <div class="field">
                <label for="phone">Phone</label>
                <input type="tel" id="phone" name="phone" required autocomplete="tel">
              </div>
            </div>
            <div class="field" style="margin-top:1rem">
              <label for="zip">Property ZIP code</label>
              <input type="text" id="zip" name="zip" inputmode="numeric" autocomplete="postal-code">
            </div>
            <div class="field" style="margin-top:1rem">
              <label for="message">How can we help?</label>
              <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            <button class="btn btn-primary btn-block" type="submit" style="margin-top:1.25rem">Send Message</button>
            <p class="form-status" data-form-status role="status"></p>
          </form>
        </div>
      </div>
    </div>
  </section>
{cta_band(D, "Need it looked at sooner?", "Call rather than emailing – especially if there is water under the house right now.")}'''

# ----------------------------------------------------------------------- faq
# ONE source for the whole site's FAQ. faq.html and the homepage FAQ section
# are both generated from this list, and so is the FAQPage JSON-LD on each --
# so the visible text and the structured data physically cannot disagree.
FAQS = [('What should a Savannah foundation inspection establish?',
  'The assessment should distinguish movement in supports from damaged timber, surface cracking and '
  'moisture problems. Floor readings, accessible footing and framing condition, drainage and the '
  'history of changes provide the evidence. Soil and groundwater conditions vary by property and cannot '
  'be inferred from the neighborhood alone.'),
 ('What determines the price of foundation repair?',
  'Access, the number and condition of affected supports, engineering requirements, drainage work and '
  'the repair method determine the scope. Request an itemized written proposal after inspection, '
  'including exclusions and any allowance for concealed damage.'),
 ('Does the foundation type change the inspection?',
  'Yes. A raised floor needs inspection of accessible framing and bearings, while a concrete slab needs '
  'a different assessment. Identify the actual construction before choosing a repair; a Savannah '
  'address does not establish the foundation type.'),
 ('How do I know if a sagging or bouncy floor is actually structural?',
  'A floor that flexes as you walk across it, a noticeable dip toward the middle of a room, doors and '
  'windows that stopped latching properly, or new cracks appearing above door frames are the usual '
  'signs that something under the floor has moved or lost support. Any one of them on its own can be '
  'minor. Two or three of them together in the same part of the house usually means the support below '
  'needs looking at.'),
 ('How should a foundation crack be assessed?',
  'Record its location, width, direction and whether it changes. Compare it with floor readings, wall '
  'alignment and drainage. Crack shape alone is not a diagnosis; the surrounding structure and evidence '
  'of movement determine whether monitoring, repair or further engineering assessment is appropriate.'),
 ('Can you fix a sagging floor without replacing it?',
  'Usually, yes. Sagging floors are almost always a support problem rather than a floor problem – '
  'rotted joists or settled posts underneath. Replacing the failed framing and setting adjustable jacks '
  'on proper footings addresses it from below, without pulling up the finished floor.'),
 ('Why does everyone here talk about crawl space humidity?',
  "Because in this climate it's what destroys the structure. Vented crawl spaces pull humid coastal air "
  'onto cool surfaces where it condenses, and wood held above roughly twenty percent moisture content '
  'rots. Structural repairs in a crawl space that stays damp have a limited lifespan, which is why '
  'encapsulation gets quoted alongside them.'),
 ('How long does the work take?',
  'Most residential jobs run one to three days on site. Slab leveling is often finished in a few hours. '
  'Where a badly settled floor is being recovered, the lift itself is staged over several visits across '
  'a few weeks so the structure moves gradually rather than cracking finishes.'),
 ('Do I have to move out during the repair?',
  'Almost never. Crawl space and piering work happens under and outside the house, and slab work is '
  'entirely exterior. You may hear equipment, but the living space stays usable.'),
 ('Is the inspection really free?',
  'Yes, including the elevation readings and the written findings, and whether or not you go ahead with '
  'any work. If the honest answer is that nothing needs doing yet, that is what the report says.'),
 ('Do I need to be home for the inspection?',
  'It helps, because we walk the findings with you at the end rather than leaving a report behind. We '
  'do need access to the crawl space hatch or the affected area, and enough room to work around the '
  'exterior of the house.'),
 ('Do you charge for a second opinion?',
  'No. If you have a quote from another contractor and want the reasoning checked, the inspection is '
  'the same free visit. Bring the quote – comparing what was proposed against what the measurements '
  'show is often the most useful hour in the whole process.'),
 ('Which areas do you cover?',
  'Chatham County in full – downtown, midtown, the Southside and Georgetown, plus every one of the '
  'islands from Isle of Hope and Thunderbolt out to Tybee – and the west side at Garden City, Port '
  'Wentworth, Pooler and Bloomingdale. Outside Chatham we cover Richmond Hill in Bryan County, Rincon '
  'and Springfield in Effingham, and Hinesville in Liberty. There are eighteen area pages on the site '
  'with the detail for each. If you are somewhere small in between, call and ask, because the answer is '
  'usually yes.')]

FAQ_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / FAQ</div>
      <h1>Foundation Repair FAQ – Savannah, GA</h1>
      <p class="lede">Straight answers to what people actually ask before booking an inspection, including the ones about cost.</p>
    </div>
  </section>

  <section>
    <div class="container">
{faq_blocks(FAQS)}
    </div>
  </section>
{cta_band(D, "Question not answered here?", "Call and ask – no charge for a conversation, and no pressure attached to it.")}'''

# ------------------------------------------------------------------- legal
PRIVACY_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / Privacy Policy</div>
      <h1>Privacy Policy</h1>
      <p class="lede">What we collect when you contact us, and what we do with it.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <h2>What we collect</h2>
      </div>
      <p>When you submit a form on this site or contact us by phone, text, or email, we collect the details you give us – typically your name, phone number, email address, property ZIP code, and a description of the problem you are asking about.</p>
      <h2>What we use it for</h2>
      <p>We use those details solely to respond to your inquiry, arrange and carry out an inspection, and follow up about the work discussed. We do not sell your information, and we do not add you to marketing lists you did not ask to join.</p>
      <h2>Who else sees it</h2>
      <p>Your details may be shared with the contractor who carries out the inspection or the repair at your property, because they cannot do the work without them. They are not shared with anyone else for any other purpose.</p>
      <h2>How long we keep it</h2>
      <p>Inquiry records are kept for as long as needed to serve you and to meet ordinary business and tax record-keeping requirements, then deleted.</p>
      <h2>Cookies and analytics</h2>
      <p>This site is static and does not set advertising or tracking cookies. If website analytics are added in future, this page will be updated to say so before they are switched on.</p>
      <h2>Your choices</h2>
      <p>You can ask us what we hold about you, ask us to correct it, or ask us to delete it, at any time – email <a href="mailto:{EMAIL}">{EMAIL}</a> and we will act on it.</p>
      <h2>Changes</h2>
      <p>If this policy changes, the updated version will be posted on this page.</p>
    </div>
  </section>
'''

TERMS_BODY = f'''
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumbs"><a href="index.html">Home</a> / Terms of Service</div>
      <h1>Terms of Service</h1>
      <p class="lede">The basis on which this website and our estimates are provided.</p>
    </div>
  </section>

  <section>
    <div class="container">
      <div class="section-head">
        <h2>About this site</h2>
      </div>
      <p>This website provides general information about foundation and crawl space repair in the Savannah, Georgia area, and a way to request an inspection. Using it does not create a contract between us.</p>
      <h2>Information is general, not structural advice</h2>
      <p>Descriptions of repairs, symptoms, and typical costs on this site are general guidance about how this work usually goes. They are not a structural assessment of your specific property, and no one should act on them as though they were. Only an on-site inspection of your building can tell you what your building needs.</p>
      <h2>Pricing</h2>
      <p>Any price ranges shown are indicative of typical local jobs and are not quotes. A binding price is given only in a written scope after an inspection, and only for the work described in it.</p>
      <h2>Inspections</h2>
      <p>Inspections are provided free and without obligation. Access to the crawl space, slab, or affected area is required, and safe access is the property owner's responsibility. Where a space cannot be entered safely, we will say what could not be assessed rather than guess at it.</p>
      <h2>Third-party links</h2>
      <p>This site links to external sources – municipal, association, and reference pages – to show where specific local facts came from. We do not control those sites and are not responsible for their content.</p>
      <h2>Limitation</h2>
      <p>To the extent permitted by law, we are not liable for loss arising from reliance on the general information on this website, as distinct from a written scope of work issued after an inspection.</p>
      <h2>Contact</h2>
      <p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a> or {PHONE_DISPLAY}.</p>
    </div>
  </section>
'''

if __name__ == "__main__":
    write("free-inspection.html", page(
        "free-inspection.html",
        "Free Structural Inspection – Savannah, GA",
        "Book a free foundation and crawl space inspection in Savannah, GA – elevation readings, findings in writing, and no obligation.",
        INSPECTION_BODY))

    write("about.html", page(
        "about.html",
        "About Us | Savannah Foundation Repair",
        "A Savannah-focused foundation and crawl space specialist – why coastal Lowcountry conditions need a different approach than inland Georgia.",
        ABOUT_BODY))

    write("contact.html", page(
        "contact.html",
        "Contact | Savannah Foundation Repair Co",
        f"Contact {BRAND} – call {PHONE_DISPLAY}, text a photo of the problem, or send a message. Serving Savannah and Chatham County, GA.",
        CONTACT_BODY))

    write("faq.html", page(
        "faq.html",
        "Foundation Repair FAQ – Savannah, GA",
        "Answers to common foundation repair questions in Savannah – costs, crack severity, sagging floors, crawl space humidity, and what an inspection involves.",
        FAQ_BODY,
        schemas=[breadcrumb([("Home", f"{SITE}/"), ("FAQ", None)]), faq_schema(FAQS)]))

    write("privacy-policy.html", page(
        "privacy-policy.html", "Privacy Policy | Savannah Foundation Repair",
        "How Savannah Foundation Repair Co collects, uses, and protects the details you provide when requesting an inspection.",
        PRIVACY_BODY))

    write("terms.html", page(
        "terms.html", "Terms of Service | Savannah Foundation",
        "Terms on which this website and our inspections and estimates are provided.",
        TERMS_BODY))

    patch_home_faq()
    print("\n6 core pages generated")
