"""All pages for the jordanriverroofing.com redesign, on the client's current 92 URLs plus a new blog post and a 404.

Facts come only from the client's own site (17 Oct 2026), and only where the site agrees with itself:
founded 2019 by Phil (Philip Jordan), a Utah native with over a decade in roofing before that; started as a two-person
crew in Taylorsville; Phil still on site and answering the phone; the five services and their bullet lists; free
inspections with photo reports; itemized estimates; the 4-step process; adjuster meetings; TAMKO DiamondShield (terms
checked against TAMKO's own Edge program brochure); the 13 home-page reviews, word for word.
Not used (contradictory or unverifiable, see notes): "Since 2003", "20+ years", "over 15 years", "5,000+ roofs", "500+",
"4.9 stars", "98% satisfaction", "A+/A-rated", "BBB accredited", "24/7", "same-day", "respond within one business hour",
"100% leak-proof guarantee", "30% HVAC reduction", GAF/CertainTeed/Owens Corning "certified partner" logos.
The 23 AI-looking images on the old site are not used.
Report (17 Oct 2026): home page targets "roofing company taylorsville"; service pages name Taylorsville.
"""
import html, json, os, re
from build import (U, S, ARROW, PHONE, CHECK, CONTACT, SERVICES, SVC, CITIES, CITY, BLOG, REVIEWS, img, chip, phero, cta,
                   quotes_html, reviews_marquee, valley_map, faq_html, faq_ld, crumbs_ld, contact_form, valley_line, canon)
import p_blog

HERE = os.path.dirname(os.path.abspath(__file__))
CT = json.load(open(os.path.join(HERE, "client_text.json"), encoding="utf-8"))
HOME = ("Home", "")
PROCESS = [("Free inspection", "We look at your roof and give you an honest, detailed report, with photos."),
           ("Transparent quote", "A clear, itemized estimate with no hidden fees or surprises."),
           ("Installation", "The crew completes the work with the materials you chose."),
           ("Final walkthrough", "We clean up thoroughly and review the finished work with you.")]


def process_html():
    return '<ol class="steps">' + "".join(f'<li class="reveal"><span class="mono">0{i+1}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(PROCESS)) + "</ol>"


def svc_ld(path, name, desc, area="Taylorsville"):
    return {"@type": "Service", "@id": canon(path) + "#service", "name": name, "serviceType": name, "description": desc,
            "provider": {"@id": U + "/#business"}, "areaServed": {"@type": "City", "name": area, "containedInPlace": {"@type": "State", "name": "Utah"}}}


def city_links(svc_slug):
    return '<div class="citygrid">' + "".join(f'<a href="@/services/{svc_slug}/{c[0]}">{c[1]}</a>' for c in CITIES) + "</div>"


def checklist(items):
    return '<ul class="checks">' + "".join(f"<li><i>{CHECK}</i><span>{x}</span></li>" for x in items) + "</ul>"


# ---------------------------------------------------------------- service pages (Taylorsville-targeted)
SERVICE_PAGES = {
    "new-roof-replacement": {
        "title": "Roof Replacement in Taylorsville, UT | Jordan River Roofing",
        "h1": "New Roof &amp; Roof Replacement in Taylorsville",
        "meta": "Roof replacement in Taylorsville, UT: full tear-off, ice and water shield, 50-year rated architectural shingles and new flashing. Free inspection. Call Phil.",
        "lede": "Jordan River Roofing replaces roofs in Taylorsville and across the Salt Lake Valley: a complete tear-off down to the deck, new underlayment and ice and water shield, 50-year rated architectural shingles, and new flashing and ventilation.",
        "img": ("tudor-brick-home-tear-off", "Crew tearing off the old roof on a brick Tudor home"),
        "included": ["Complete tear-off and disposal", "Deck inspection", "Premium underlayment and ice and water shield", "50-year rated architectural shingles", "New flashing and ventilation"],
        "body": f'''<h2>Repair or replace? An honest answer first</h2>
<p>Not every old roof needs replacing. Knowing when to repair and when to replace protects your home and your budget, so the first step is a free inspection and a straight answer. If targeted repairs will keep a sound roof going, we&rsquo;ll say so. Reviewers mention it too: &ldquo;Phil listens. He listened to what we wanted, then advised us whether what we were asking for was possible.&rdquo;</p>
<h2>What a full replacement includes</h2>
<p>A replacement starts with a complete tear-off, so the crew can inspect the roof deck itself. Then comes premium underlayment and ice and water shield, the architectural shingles, and new flashing and ventilation. Ventilation matters more than most people think: one customer, Ket, chose us because other bidders &ldquo;didn&rsquo;t even include the new ridge venting system&rdquo; and wanted to keep the old turtle vents. We explain the difference in <a href="@/{BLOG[1]}">{BLOG[0]}</a>.</p>
<h2>How long it takes</h2>
<p>Every roof is different, but two customers&rsquo; reviews give a feel for it. Judy&rsquo;s full tear-off, with new underlayment, new vents and two chimneys roofed around, &ldquo;took only 1.5 days&rdquo;, with a complete clean-up each day. Pat&rsquo;s was &ldquo;completed within two days&rdquo;.</p>
<h2>Warranty</h2>
<p>On qualifying TAMKO roofs, we offer the TAMKO DiamondShield warranty: up to 25 years of workmanship coverage and a 50-year Full Start period. It needs TAMKO Titan XT or StormFighter FLEX shingles plus four TAMKO accessory products. <a href="@/warranties">How the DiamondShield warranty works &rarr;</a></p>''',
        "faqs": [("How long does a roof replacement take?", "It depends on the size and complexity of the roof. Customers&rsquo; reviews mention a full tear-off and new roof finished in 1.5 days and in two days."),
                 ("Do you tear off the old roof?", "Yes. A complete replacement includes a full tear-off and disposal, so the deck can be inspected before the new roof goes on."),
                 ("Is the new roof warrantied?", "Qualifying TAMKO roofs can carry the TAMKO DiamondShield warranty, with up to 25 years of workmanship coverage. See the warranty page for what qualifies.")],
        "reviews": [3, 5]},
    "roof-repairs-maintenance": {
        "title": "Roof Repair in Taylorsville, UT | Jordan River Roofing",
        "h1": "Roof Repair &amp; Maintenance in Taylorsville",
        "meta": "Roof repair in Taylorsville, UT: leak detection and sealing, shingle replacement, flashing and gutter repair, ventilation fixes and annual maintenance.",
        "lede": "Jordan River Roofing repairs roofs in Taylorsville and across Salt Lake County: leak detection and sealing, missing or damaged shingles, flashing and gutter repair, ventilation corrections and annual maintenance plans.",
        "img": ("crew-tear-off-with-truck", "Jordan River Roofing truck at a home while the crew works on the roof"),
        "included": ["Leak detection and sealing", "Shingle and tile replacement", "Flashing and gutter repair", "Ventilation corrections", "Annual maintenance plans"],
        "body": '''<h2>Small problems, fixed before they grow</h2>
<p>A single missing shingle or a lifted piece of flashing is a small repair. Left alone through a Utah winter, it can let water into the deck, the insulation and the ceiling below. Repairs are about finding where the water actually gets in, which isn&rsquo;t always right above the stain, and fixing it properly.</p>
<h2>Signs your roof needs attention</h2>
<ul><li>Missing, broken or curling shingles</li><li>Water stains or damp spots on ceilings and walls</li><li>Sagging along the ridge or roof deck</li><li>Daylight showing through the attic boards</li><li>Lots of shingle granules in the gutters</li><li>Lifted, rusted or missing flashing around chimneys and vents</li><li>Moss or algae on shaded slopes</li></ul>
<h2>When it can&rsquo;t wait</h2>
<p>Kristen was selling her house when the buyer&rsquo;s inspection found a leak, and the sale depended on fixing it. In her words: &ldquo;I gave Jordan River Roofing a call and they were out the very next day taking care of the issue.&rdquo; For storm damage and active leaks, see <a href="@/services/emergency-insurance-claims">emergency and insurance claims</a>.</p>
<h2>Repair or replace?</h2>
<p>If a roof is near the end of its life, repeated repairs can cost more than they save. The free inspection tells you which one you&rsquo;re looking at, with photos, so you can decide. <a href="@/services/new-roof-replacement">Roof replacement &rarr;</a></p>''',
        "faqs": [("Is the roof inspection really free?", "Yes. Inspections are free and come with a photo-documented report of the roof&rsquo;s condition, with no obligation."),
                 ("Do you offer roof maintenance plans?", "Yes, annual maintenance plans are part of our repair and maintenance service. Ask about one when we inspect your roof."),
                 ("Can you match my existing shingles?", "We replace missing and damaged shingles as part of a repair. Whether an exact match is still made depends on the shingle; we&rsquo;ll tell you what&rsquo;s available after looking.")],
        "reviews": [9, 10]},
    "commercial-roofing": {
        "title": "Commercial Roofing in Taylorsville, UT | Jordan River",
        "h1": "Commercial Roofing in Taylorsville",
        "meta": "Commercial roofing in Taylorsville, UT: TPO, EPDM, modified bitumen, roof coatings and metal for warehouses, offices and retail. Free roof assessment. Call us.",
        "lede": "Jordan River Roofing installs and maintains commercial roofs in Taylorsville and across Salt Lake County: flat and low-slope TPO, EPDM and modified bitumen systems, roof coatings and metal roofing, for warehouses, offices and retail buildings.",
        "img": None,
        "included": ["TPO and EPDM single-ply systems", "Modified bitumen", "Roof coatings", "Metal roofing", "Preventative maintenance"],
        "body": '''<h2>Flat and low-slope roofs for business buildings</h2>
<p>Commercial roofs are mostly flat or low-slope, and they fail differently from a house roof: water that doesn&rsquo;t drain, seams that open up, flashing around rooftop equipment. We install TPO, EPDM, modified bitumen and metal systems, and coatings that can extend the life of an existing roof, planned around your building and budget, with as little disruption to your business as possible.</p>
<h2>TPO, EPDM or modified bitumen?</h2>
<p><strong>TPO</strong> is a single-ply membrane with heat-welded seams and a reflective white surface, which helps keep a building cooler in summer. <strong>EPDM</strong> is a durable rubber membrane. <strong>Modified bitumen</strong> is a multi-layer asphalt-based system. Which one fits depends on the building, the roof deck and what&rsquo;s already there. We&rsquo;ll walk you through the options after looking at the roof.</p>
<h2>Warning signs on a commercial roof</h2>
<ul><li>Bubbles or blisters in the membrane</li><li>Water still standing 48 hours after rain</li><li>Stained ceiling tiles or damp drywall inside</li><li>Cracking, exposed insulation or sagging</li><li>Rusted or lifted flashing around HVAC units and parapets</li></ul>''',
        "faqs": [("What commercial roofing systems do you install?", "TPO and EPDM single-ply membranes, modified bitumen, roof coatings and metal roofing."),
                 ("Can you work around our business hours?", "We plan commercial jobs to keep disruption to your operations as low as possible. Tell us your schedule when we assess the roof.")],
        "reviews": [2]},
    "emergency-insurance-claims": {
        "title": "Storm Damage &amp; Roof Insurance Claims | Jordan River Roofing",
        "h1": "Storm Damage &amp; Insurance Claims in Taylorsville",
        "meta": "Storm damage roof help in Taylorsville, UT: emergency tarping, hail and wind damage assessment, photo reports for insurance and on-site adjuster meetings.",
        "lede": "Jordan River Roofing helps Taylorsville and Salt Lake County homeowners after wind, hail and storm damage: emergency tarping to stop active leaks, a damage assessment with photo documentation, and help with your insurance claim, including meeting your adjuster on site.",
        "img": None,
        "included": ["Emergency tarping", "Hail and wind damage assessment", "Photo documentation for your insurance claim", "Meeting your adjuster on site", "Itemized estimates", "Permanent repairs or replacement"],
        "body": '''<h2>First, stop the water</h2>
<p>After a storm, the first job is protecting the inside of your home. Heavy-duty tarps over the damaged area keep water out of the ceilings, walls and floors until the permanent repair can be done.</p>
<h2>Then, document everything</h2>
<p>An insurance claim depends on clear evidence of the damage and its cause. We inspect the roof and document the damage with detailed photos, then write an itemized estimate for the repair.</p>
<h2>Working with your adjuster</h2>
<p>We meet your insurance company&rsquo;s adjuster on site to go over the damage and the scope of work, and make sure the proposed repairs meet current building code. You stay in control of your claim; we handle the roofing side of it.</p>
<h2>What we can&rsquo;t promise</h2>
<p>Whether a repair is covered depends on your policy and on what caused the damage, and only your insurance company can decide that. What we can do is make sure the damage is properly documented and explained.</p>''',
        "faqs": [("Will homeowner&rsquo;s insurance pay for my roof repair?", "It depends on your policy and on the cause of the damage; storm damage is often covered and normal wear usually isn&rsquo;t. Your insurer decides. We document the damage and meet the adjuster so the claim is based on a clear picture."),
                 ("Should I call you or my insurance company first?", "If water is coming in, call us to get the roof protected, and let your insurer know about the damage. A documented inspection helps either way."),
                 ("What do you do at the adjuster&rsquo;s inspection?", "We meet the adjuster on site, show the damage we documented, and go over the scope of the repair and any code requirements.")],
        "reviews": [9]},
    "attic-ventilation-skylights": {
        "title": "Attic Ventilation &amp; Skylights, Taylorsville UT | Jordan River",
        "h1": "Attic Ventilation &amp; Skylights in Taylorsville",
        "meta": "Attic ventilation and skylights in Taylorsville, UT: ridge and soffit vents, attic fans, skylight installation and repair, and help with ice dams.",
        "lede": "Jordan River Roofing improves attic ventilation and installs skylights in Taylorsville and across Salt Lake County: ridge and soffit ventilation, attic fan installation, and skylight installation and repair.",
        "img": None,
        "included": ["Ridge and soffit ventilation", "Attic fan installation", "Skylight installation and repair", "Skylight flashing and seal repair", "Help preventing ice dams"],
        "body": f'''<h2>Why attic ventilation matters</h2>
<p>An attic that can&rsquo;t breathe gets very hot in summer and holds moisture in winter. That heat and moisture shorten the life of shingles and roof decking, can lead to mold, and help ice dams form along the eaves in a Utah winter. Balanced ventilation, with air coming in low at the soffits and leaving high at the ridge, keeps the attic closer to the outside temperature.</p>
<h2>Ridge vents, not a patchwork</h2>
<p>Many older homes have a row of box (&ldquo;turtle&rdquo;) vents. When we re-roof, we&rsquo;ll talk through whether a continuous ridge vent with soffit intake is the better design for your attic. One customer, Kevin, wrote that the crew &ldquo;helped me achieve a fully ventilated attic space.&rdquo; Our guide explains the trade-offs: <a href="@/{BLOG[1]}">{BLOG[0]}</a>.</p>
<h2>Skylights</h2>
<p>A skylight brings daylight into a room, but only if it stays watertight. We install new skylights and repair existing ones: worn flashing, failed seals and leaks around the frame.</p>
<h2>Signs to look for</h2>
<ul><li>Hot, stuffy upstairs rooms in summer</li><li>Ice dams along the eaves in winter</li><li>Condensation or fogging between skylight panes</li><li>Ceiling stains or mildew in upper rooms</li><li>Musty smells in the attic</li></ul>''',
        "faqs": [("Should I keep my turtle vents when I add a ridge vent?", f"Usually not. The vent manufacturer Air Vent advises against mixing different types of exhaust vents over one attic, because it can short-circuit the airflow. More in our guide, <a href=\"@/{BLOG[1]}\">{BLOG[0]}</a>."),
                 ("Can you fix a leaking skylight?", "Yes. We repair skylight leaks, including worn flashing and failed weather seals, and replace skylights when repair isn&rsquo;t worth it.")],
        "reviews": [6, 7]},
}


def service_page(slug):
    d = SERVICE_PAGES[slug]; s = SVC[slug]; path = "services/" + slug
    trail = [HOME, ("Services", "services"), (s[1], path)]
    image = d["img"]
    body = phero(trail, d["h1"], d["lede"], "Taylorsville, Utah", image[0] if image else None, image[1] if image else "", (s[2], s[3])) + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{d["body"]}</div>
<aside class="side reveal"><div class="card"><p class="label">What&rsquo;s included</p>{checklist(d["included"])}</div>
<div class="card navy"><p class="label light">Free inspection</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><p>{S["hours"]}</p><a class="btn lime" href="@/{CONTACT}">Request an inspection {ARROW}</a></div></aside></div></section>
<section class="sec mist"><div class="wrap"><div class="head reveal"><p class="label">How a job goes</p><h2>From first call to final walkthrough</h2></div>{process_html()}</div></section>
''' + quotes_html(d["reviews"], "In our customers&rsquo; words") + f'''
<section class="sec"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>{html.unescape(s[1]).replace("&", "&amp;")}: common questions</h2></div><div class="reveal">{faq_html(d["faqs"])}</div></div></section>
<section class="sec mist"><div class="wrap"><div class="head reveal"><p class="label">Service area</p><h2>{s[1]} across the valley</h2><p class="lede">Based in Taylorsville, serving 13 cities in the Salt Lake Valley.</p></div>{city_links(slug)}</div></section>''' + cta()
    return {"path": path, "title": d["title"].replace("&amp;", "&"), "meta": d["meta"], "body": body, "og": image[0] if image else None, "full_biz": False,
            "schema": [crumbs_ld(path, trail), svc_ld(path, html.unescape(s[1]), d["lede"]), faq_ld(d["faqs"])]}


def svc_city_page(slug, city):
    s = SVC[slug]; c = CITY[city]; path = f"services/{slug}/{city}"
    trail = [HOME, ("Services", "services"), (s[1], "services/" + slug), (c[1], path)]
    d = SERVICE_PAGES[slug]
    others = "".join(f'<a class="rowlink" href="@/services/{o[0]}/{city}">{chip(o[2], o[3])}<b>{o[1]} in {c[1]}</b>{ARROW}</a>' for o in SERVICES if o[0] != slug)
    body = phero(trail, f"{s[1]} in {c[1]}", f"{s[4]} Jordan River Roofing serves {c[1]}, Utah ({c[2]}) from our base in Taylorsville.", f"{c[1]}, Utah", code=(s[2], s[3])) + f'''
<section class="sec"><div class="wrap split top"><div class="prose reveal">
<h2>{s[1]} for {c[1]} homes and businesses</h2>
<p>Jordan River Roofing offers {html.unescape(s[1]).lower().replace("&", "and")} in {c[1]} and the rest of the Salt Lake Valley. The work and the process are the same wherever you are in the valley, and the full details are on our main <a href="@/services/{slug}">{s[1]}</a> page.</p>
<h3>What&rsquo;s included</h3>{checklist(d["included"])}
<p>Every job starts with a free inspection and a clear, itemized estimate. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/{CONTACT}">send a message</a>.</p>
<p><a href="@/service-areas/{city}">More about roofing in {c[1]} &rarr;</a></p></div>
<div class="reveal"><p class="label">Other services in {c[1]}</p><div class="rowlinks">{others}</div></div></div></section>''' + cta()
    return {"path": path, "title": f"{html.unescape(s[1])} in {c[1]}, UT | Jordan River Roofing",
            "meta": f"{html.unescape(s[1])} in {c[1]}, Utah from Jordan River Roofing, based in Taylorsville. {html.unescape(s[4])} Free inspection.",
            "body": body, "full_biz": False, "canonical": canon("services/" + slug),  # localized copy of the main service page
            "schema": [crumbs_ld(path, trail)]}


def area_page(city):
    slug, name, z, branch = CITY[city]
    path = "service-areas/" + city
    trail = [HOME, ("Service areas", "service-areas"), (name, path)]
    i = [x[0] for x in CITIES].index(city)
    nb = [CITIES[j] for j in (i - 1, i + 1) if 0 <= j < len(CITIES)]
    rows = "".join(f'<a class="rowlink" href="@/services/{s[0]}/{city}">{chip(s[2], s[3])}<b>{s[1]}</b><span>{s[4]}</span>{ARROW}</a>' for s in SERVICES)
    where = ("our home base, where the company started in 2019" if city == "taylorsville" else
             ("on the east bench of the valley" if branch else "along the Jordan River corridor of the Salt Lake Valley"))
    lede = (f"Jordan River Roofing is a roofing company in Taylorsville, Utah ({z}): roof replacement, repairs, commercial roofing, storm damage help, attic ventilation and skylights."
            if city == "taylorsville" else
            f"Jordan River Roofing serves {name}, Utah ({z}) from our base in Taylorsville: roof replacement, repairs, commercial roofing, storm damage help, attic ventilation and skylights.")
    body = phero(trail, f"Roofing in {name}", lede, f"{name}, UT {z}") + f'''
<section class="sec"><div class="wrap split top"><div class="reveal">
<p class="label">Services in {name}</p><h2>What we do in {name}</h2>
<p>{name} is {where}. Every service below is available here, starting with a free roof inspection and a clear, itemized estimate.</p>
<div class="rowlinks">{rows}</div>
<p class="small">Nearby: {" &middot; ".join(f'<a href="@/service-areas/{n[0]}">{n[1]}</a>' for n in nb)}</p></div>
<div class="reveal">{valley_line(current=city)}</div></div></section>''' + quotes_html([(i * 2) % 13, (i * 2 + 1) % 13], "What homeowners say") + cta(f"Roofing in {name}? Start with a free inspection")
    return {"path": path, "title": f"Roofing in {name}, UT | Jordan River Roofing",
            "meta": f"Roofing in {name}, Utah ({z}) from Jordan River Roofing in Taylorsville: replacement, repairs, commercial, storm damage. Free inspection.",
            "body": body, "full_biz": False, "schema": [crumbs_ld(path, trail)]}


JOBLOG = [("tudor-brick-home-tear-off", "Tear-off", "Crew stripping the old roof on a brick Tudor"),
          ("victorian-home-reroof", "Re-roof", "A two-story Victorian with a turret, mid re-roof"),
          ("crew-tear-off-with-truck", "Tear-off", "Crew on the roof, truck at the curb"),
          ("finished-architectural-shingle-roof", "Finished", "A finished architectural shingle roof"),
          ("truck-and-dump-trailer-on-job", "Set-up", "Truck and dump trailer at a split-level"),
          ("yard-banner-finished-roof", "Finished", "The yard banner goes up when the job is done")]


def home():
    lines = "".join(f'<a class="route reveal {k}" href="@/services/{s}">{chip(c, k)}<b>{n}</b><span>{d}</span><i>{ARROW}</i></a>' for s, n, c, k, d in SERVICES)
    log = "".join(f'<figure class="log reveal"><div class="log-img">{img(n, c)}</div><figcaption><span class="mono">{i + 1:02d} &middot; {t}</span>{c}</figcaption></figure>' for i, (n, t, c) in enumerate(JOBLOG))
    faqs = [("Do you offer free roof inspections?", "Yes. Inspections are free, with a photo-documented report on your roof&rsquo;s condition and no obligation."),
            ("Which cities do you serve?", "Thirteen cities in the Salt Lake Valley, from Draper and Riverton in the south to North Salt Lake in the north. See the <a href=\"@/service-areas\">service areas</a>."),
            ("Who will I be dealing with?", "Phil founded Jordan River Roofing in 2019 and is still personally involved in every project. Nearly every review mentions him by name."),
            ("What warranty do you offer?", "Qualifying TAMKO roofs can carry the TAMKO DiamondShield warranty, with up to 25 years of workmanship coverage. See <a href=\"@/warranties\">how it works</a>."),
            ("Do you help with insurance claims?", "Yes. We document storm damage with photos, write an itemized estimate and meet your adjuster on site.")]
    steps = "".join(f'<li class="reveal"><span class="n">{i + 1:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(PROCESS))
    body = f'''
<section class="hero"><div class="hero-lines" aria-hidden="true"><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><i class="l5"></i></div>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">Jordan River Roofing &middot; Taylorsville, Utah &middot; since 2019</p>
<h1>Roofing company in Taylorsville, <em>where the owner still answers the phone.</em></h1>
<p class="lede">Founded in 2019 by Phil, a Utah native. We replace and repair roofs, handle commercial flat roofs and storm damage, and fix attic ventilation across the Salt Lake Valley.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Roof Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="hero-cards" aria-label="Photos from Jordan River Roofing jobs">
<figure class="hc hc1">{img("jordan-river-roofing-truck-owner", "A Jordan River Roofing truck at a customer's home", priority=True)}<figcaption class="mono">On the job</figcaption></figure>
<figure class="hc hc2">{img("tudor-brick-home-tear-off", "Crew re-roofing a brick Tudor home", lazy=False)}<figcaption class="mono">Tear-off &middot; brick Tudor</figcaption></figure>
<figure class="hc hc3">{img("victorian-home-reroof", "Re-roofing a two-story Victorian with a turret", lazy=False)}<figcaption class="mono">Re-roof &middot; Victorian</figcaption></figure>
</div></div>
<div class="board wrap" aria-label="Quick facts"><div class="board-in">
<div><span class="mono">Founded</span><b>2019</b><small>Taylorsville</small></div>
<div><span class="mono">Inspections</span><b>Free</b><small>with photo reports</small></div>
<div><span class="mono">Estimates</span><b>Itemized</b><small>no surprises</small></div>
<div><span class="mono">Warranty</span><b>DiamondShield</b><small>on qualifying TAMKO roofs</small></div>
<div><span class="mono">Stops</span><b>13</b><small>valley cities</small></div></div></div>
</section>

<section class="sec"><div class="wrap"><div class="head row reveal"><div><p class="label">Roofing contractor in Taylorsville</p><h2>Five lines of work</h2></div><a class="more" href="@/services">All services {ARROW}</a></div>
<div class="routes">{lines}</div></div></section>

<section class="sec navy map-sec"><div class="wrap"><div class="head row reveal"><div><p class="label light">Service area</p><h2>13 stops on the Valley Line</h2></div>
<p class="head-note">The Jordan River runs north through the Salt Lake Valley, from the narrows at Draper to the Great Salt Lake. Our service area follows it, with Taylorsville in the middle. Pick a stop.</p></div>
<div class="reveal">{valley_map()}</div><div class="map-list">{valley_line()}</div></div></section>

<section class="sec"><div class="wrap story">
<div class="reveal story-text"><p class="label">The company</p><h2>Started with two people in Taylorsville</h2>
<p class="lede">Phil spent over a decade in the roofing industry before founding Jordan River Roofing in 2019, to build a company that treats every roof like it&rsquo;s on his own home.</p>
<p>The team has grown, and Phil is still on site, still personally involved in every project, and still answers the phone when you call. It&rsquo;s the thing customers mention most.</p>
<blockquote class="pull">&ldquo;Phil was very patient and explained everything in great detail and answered all of my questions without any hesitation.&rdquo;<cite>Michael Lee, Google review</cite></blockquote>
<a class="more" href="@/about">About Jordan River Roofing {ARROW}</a></div>
<div class="joblog">{log}</div>
</div></section>

<section class="sec mist reviews-sec"><div class="wrap"><div class="head row reveal"><div><p class="label">Reviews</p><h2>What homeowners say about Phil and the crew</h2></div><a class="more" href="@/about">More about Phil {ARROW}</a></div></div>
{reviews_marquee()}</section>

<section class="sec navy warr-sec"><div class="wrap split">
<div class="reveal"><p class="label light">Warranty</p><h2>TAMKO DiamondShield</h2><p class="lede">On qualifying TAMKO roofs, the DiamondShield enhanced warranty covers workmanship for up to 25 years, with a 50-year Full Start period, and can be transferred once within 20 years.</p>
<a class="btn" href="@/warranties">How the warranty works {ARROW}</a></div>
<dl class="warr reveal"><div><dt>25</dt><dd>years of workmanship coverage</dd></div><div><dt>50</dt><dd>year Full Start period</dd></div><div><dt>1&times;</dt><dd>transfer within 20 years</dd></div></dl></div></section>

<section class="sec"><div class="wrap"><div class="head reveal"><p class="label">How it works</p><h2>From first call to final walkthrough</h2></div><ol class="route-steps">{steps}</ol></div></section>

<section class="sec mist"><div class="wrap split top">
<div class="reveal"><p class="label">Questions</p><h2>Before you call</h2><p class="lede">Or just call: <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div>
<div class="reveal">{faq_html(faqs)}</div></div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="label">Contact</p><h2>Request a free inspection</h2><p class="lede">{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}<br>{S["hours"]}</p><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div class="reveal">{contact_form()}</div></div></section>
''' + cta()
    return {"path": "", "title": "Roofing Company Taylorsville, UT | Jordan River Roofing",
            "meta": "Jordan River Roofing is a roofing company in Taylorsville, UT: roof replacement, repairs, commercial roofs, storm damage and ventilation. Free inspections.",
            "body": body, "og": "jordan-river-roofing-truck-owner", "schema": [crumbs_ld("", [HOME]), faq_ld(faqs)]}


def services_index():
    trail = [HOME, ("Services", "services")]
    rows = "".join(f'''<article class="svc-row reveal"><div>{chip(c, k)}</div><div><h2><a href="@/services/{s}">{n}</a></h2><p>{d}</p>{checklist(SERVICE_PAGES[s]["included"][:4])}</div><a class="btn" href="@/services/{s}">Details {ARROW}</a></article>''' for s, n, c, k, d in SERVICES)
    body = phero(trail, "Roofing Services in Taylorsville &amp; the Salt Lake Valley", "Jordan River Roofing offers five services in Taylorsville and across the Salt Lake Valley: roof replacement, roof repairs and maintenance, commercial roofing, storm damage and insurance claims, and attic ventilation and skylights.", "Our services") + f'''
<section class="sec"><div class="wrap"><div class="svc-list">{rows}</div></div></section>
<section class="sec mist"><div class="wrap"><div class="head reveal"><p class="label">How we work</p><h2>A simple process, from first call to final nail</h2></div>{process_html()}</div></section>''' + cta()
    return {"path": "services", "title": "Roofing Services in Taylorsville, UT | Jordan River Roofing",
            "meta": "Roofing services from Jordan River Roofing in Taylorsville, UT: replacement, repairs, maintenance, commercial roofing, storm damage, ventilation, skylights.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("services", trail)] + [svc_ld("services/" + s, html.unescape(n), d) for s, n, _, _, d in SERVICES]}


def areas_index():
    trail = [HOME, ("Service areas", "service-areas")]
    cards = "".join(f'<a class="city reveal" href="@/service-areas/{s}"><b>{n}</b><span class="mono">UT {z}</span>{"<em>Home base</em>" if s == "taylorsville" else ""}</a>' for s, n, z, b in sorted(CITIES, key=lambda c: c[1]))
    body = phero(trail, "Roofing Across the Salt Lake Valley", "Jordan River Roofing serves 13 cities in the Salt Lake Valley from our base in Taylorsville, from Draper and Riverton in the south to North Salt Lake in the north.", "Service areas") + f'''
<section class="sec"><div class="wrap split top"><div class="reveal"><p class="label">The Valley Line</p><h2>South to north</h2>
<p class="lede">The Jordan River flows north from the Jordan Narrows to the Great Salt Lake. Our cities follow it, with the east-bench cities branching off.</p>
<p>Not sure if you&rsquo;re in our area? Call <a href="tel:{S["tel"]}">{S["phone"]}</a> with your address.</p></div>
<div class="reveal">{valley_line()}</div></div></section>
<section class="sec mist"><div class="wrap"><div class="head reveal"><p class="label">A to Z</p><h2>All 13 cities</h2></div><div class="cities">{cards}</div></div></section>''' + cta()
    return {"path": "service-areas", "title": "Salt Lake Valley Service Areas | Jordan River Roofing",
            "meta": "Jordan River Roofing serves 13 Salt Lake Valley cities from Taylorsville: Draper, Riverton, South Jordan, Sandy, West Jordan, Murray, West Valley City and more.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("service-areas", trail)]}


def about():
    trail = [HOME, ("About", "about")]
    values = [("Integrity", "Honest assessments, fair pricing, no upselling."), ("Quality", "Good materials and careful installation. No compromises on the things that protect your home."),
              ("Community", "We&rsquo;re your neighbors. Every roof should be one we&rsquo;d be proud to live under."), ("Teamwork", "Crews that are trained and treated like family.")]
    vals = "".join(f'<div class="val reveal"><b>{t}</b><p>{d}</p></div>' for t, d in values)
    body = phero(trail, "About Jordan River Roofing", "Jordan River Roofing is a roofing company in Taylorsville, Utah, founded in 2019 by Phil, a Utah native who spent over a decade in the roofing industry first.", "About us", "jordan-river-roofing-truck-owner", "A Jordan River Roofing truck parked at a customer's home") + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">
<h2>Our story</h2>
<p>Phil spent over a decade in the roofing industry before deciding to build something different: a company that treats every roof like it&rsquo;s on his own home. He founded Jordan River Roofing in 2019, as a two-person operation in Taylorsville.</p>
<p>It has since grown into a team serving the whole Salt Lake Valley. Phil is still on site, still personally involved in every project, and still answers the phone when you call.</p>
<blockquote><p>&ldquo;To protect Utah homes and businesses with roofing work that outlasts the elements, delivered with honesty and craftsmanship.&rdquo;</p><p class="mono">Phil, founder</p></blockquote>
<h2>Milestones</h2>
<ol class="timeline"><li><b>2019</b><span>Phil founds Jordan River Roofing in Taylorsville with a two-person crew.</span></li><li><b>2024</b><span>Becomes a TAMKO Pro Certified Contractor.</span></li></ol>
</div><aside class="side reveal"><div class="card navy"><p class="label light">Office</p><p>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><p>{S["hours"]}</p></div></aside></div></section>
<section class="sec mist"><div class="wrap"><div class="head reveal"><p class="label">Our values</p><h2>What drives us</h2></div><div class="vals">{vals}</div></div></section>
''' + quotes_html([2, 8, 1, 11, 12, 10], "Reviews that mention Phil") + cta()
    return {"path": "about", "title": "About Jordan River Roofing | Taylorsville, UT Roofers",
            "meta": "Jordan River Roofing was founded in Taylorsville in 2019 by Phil, a Utah native with over a decade in roofing. He is still on site for every project.",
            "body": body, "full_biz": True, "og": "jordan-river-roofing-truck-owner",
            "schema": [crumbs_ld("about", trail), {"@type": "AboutPage", "@id": canon("about") + "#webpage", "url": canon("about"), "name": "About Jordan River Roofing", "about": {"@id": U + "/#business"}}]}


def warranties():
    trail = [HOME, ("Warranty", "warranties")]
    edge = "https://www.tamko.com/Edge"
    faqs = [("What is the TAMKO DiamondShield warranty?", "TAMKO&rsquo;s top enhanced limited system warranty, available only through TAMKO certified contractors at the qualifying level. It adds contractor workmanship coverage to the material warranty."),
            ("How long is workmanship covered?", "Up to 25 years under DiamondShield, according to TAMKO&rsquo;s contractor program."),
            ("What is the Full Start period?", "The opening period of the warranty during which coverage isn&rsquo;t prorated. TAMKO lists a 50-year Full Start period for DiamondShield."),
            ("Can I transfer it if I sell my home?", "Yes, once within the first 20 years."),
            ("What does a roof need to qualify?", "TAMKO Titan XT or StormFighter FLEX shingles, at least four TAMKO accessory products, a full tear-off or new installation, and registration by the contractor.")]
    body = phero(trail, "TAMKO DiamondShield Warranty", "On qualifying TAMKO roofs, Jordan River Roofing offers the TAMKO DiamondShield enhanced warranty: up to 25 years of workmanship coverage, a 50-year Full Start period, and one transfer within 20 years.", "Warranty") + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">
<h2>What it covers</h2>
<p>Most shingle warranties cover the material only. DiamondShield is TAMKO&rsquo;s top enhanced limited system warranty, and it adds contractor <strong>workmanship coverage for up to 25 years</strong>: if there&rsquo;s an installation error, labor, tear-off and re-installation are covered.</p>
<p>The material side has a <strong>50-year Full Start period</strong>, the opening stretch of the warranty during which coverage isn&rsquo;t reduced by proration.</p>
<h2>Selling your home?</h2>
<p>The warranty can be <strong>transferred once within the first 20 years</strong> to the next owner.</p>
<h2>What a roof needs to qualify</h2>
<ul><li>Installed by a TAMKO certified contractor at the qualifying level</li><li>TAMKO Titan XT or StormFighter FLEX shingles</li><li>At least four specified TAMKO accessory products</li><li>A full tear-off or new installation</li><li>Registered with TAMKO by the contractor after the job</li></ul>
<p>We register the warranty with TAMKO when the project is done.</p>
<p class="sources">Terms checked against TAMKO&rsquo;s own TAMKO Edge contractor program summary (<a href="{edge}" rel="noopener">tamko.com/edge</a>), 17 October 2026. The full terms are in the warranty document itself.</p>
</div><aside class="side reveal"><dl class="warr dark"><div><dt>25</dt><dd>years of workmanship coverage</dd></div><div><dt>50</dt><dd>year Full Start period</dd></div><div><dt>1&times;</dt><dd>transfer within 20 years</dd></div></dl>
<a class="btn" href="@/{CONTACT}">Ask about DiamondShield {ARROW}</a></aside></div></section>
<section class="sec mist"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>Warranty FAQ</h2></div><div class="reveal">{faq_html(faqs)}</div></div></section>''' + cta()
    return {"path": "warranties", "title": "TAMKO DiamondShield Warranty | Jordan River Roofing, Utah",
            "meta": "How the TAMKO DiamondShield warranty works on a Jordan River roof: up to 25 years of workmanship coverage, 50-year Full Start, transferable once in 20 years.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("warranties", trail), faq_ld(faqs)]}


def gallery():
    trail = [HOME, ("Gallery", "gallery")]
    items = [("tudor-brick-home-tear-off", "Tearing off the old roof on a brick Tudor home"),
             ("victorian-home-reroof", "Re-roofing a two-story Victorian with a turret"), ("crew-tear-off-with-truck", "Tear-off underway on a single-story home"),
             ("finished-architectural-shingle-roof", "A finished architectural shingle roof"), ("truck-and-dump-trailer-on-job", "Truck and trailer set up at a split-level home"),
             ("yard-banner-finished-roof", "Jordan River Roofing yard banner at a finished job"), ("jordan-river-roofing-truck-owner", "A Jordan River Roofing truck at a customer&rsquo;s home")]
    grid = "".join(f'<figure class="reveal">{img(n, html.unescape(c))}<figcaption>{c}</figcaption></figure>' for n, c in items)
    body = phero(trail, "Project Gallery", "Real photos from Jordan River Roofing jobs in the Salt Lake Valley: tear-offs, re-roofs and finished roofs.", "Gallery") + f'''
<section class="sec"><div class="wrap"><div class="grid">{grid}</div></div></section>''' + cta("Your home could be next")
    return {"path": "gallery", "title": "Roofing Project Gallery | Jordan River Roofing, Taylorsville",
            "meta": "Photos of Jordan River Roofing jobs around the Salt Lake Valley: tear-offs, re-roofs on Tudor and Victorian homes, and finished architectural shingle roofs.",
            "body": body, "full_biz": False, "og": "tudor-brick-home-tear-off",
            "schema": [crumbs_ld("gallery", trail), {"@type": "CollectionPage", "@id": canon("gallery") + "#webpage", "url": canon("gallery"), "name": "Jordan River Roofing project gallery"}]}


def contact():
    trail = [HOME, ("Contact", "contact")]
    body = phero(trail, "Contact Jordan River Roofing", f"Call {S['phone']}, email {S['email']} or send a message for a free roof inspection in Taylorsville and the Salt Lake Valley.", "Contact") + f'''
<section class="sec"><div class="wrap split top">
<div class="reveal contact-card"><h2>Office</h2><dl>
<dt>Phone</dt><dd><a class="big" href="tel:{S["tel"]}">{S["phone"]}</a></dd>
<dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd>
<dt>Address</dt><dd><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><a href="{S["map"]}" rel="noopener">Open in Google Maps</a></dd>
<dt>Hours</dt><dd>{S["hours"]}</dd></dl></div>
<div class="reveal">{contact_form("Send us a message")}</div></div></section>'''
    return {"path": "contact", "title": "Contact Jordan River Roofing | Taylorsville, UT Roofer",
            "meta": "Contact Jordan River Roofing at 1278 W Kimman Lane, Taylorsville, UT 84123. Call 801-857-1417 or send a message to book a free roof inspection.",
            "body": body, "full_biz": True,
            "schema": [crumbs_ld("contact", trail), {"@type": "ContactPage", "@id": canon("contact") + "#webpage", "url": canon("contact"), "name": "Contact Jordan River Roofing", "about": {"@id": U + "/#business"}}]}


def legal(path, title, meta):
    trail = [HOME, (html.escape(title), path)]
    items = CT[path][1:]
    out, in_list = [], False
    for tag, txt in items:
        txt = html.escape(re.sub(r"^(\d+)([A-Z])", r"\1. \2", txt)) if tag == "h2" else html.escape(txt)
        if tag == "li" and not in_list: out.append("<ul>"); in_list = True
        if tag != "li" and in_list: out.append("</ul>"); in_list = False
        out.append(f"<{tag}>{txt}</{tag}>")
    if in_list: out.append("</ul>")
    out.append(f'<p>{S["name"]}<br>{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}<br>{S["phone"]} &middot; <a href="mailto:{S["email"]}">{S["email"]}</a></p>')
    body = f'<section class="sec"><div class="wrap">{"".join([])}<div class="prose legal">' + crumbs_html_plain(trail) + f'<h1>{html.escape(title)}</h1>' + "".join(out) + "</div></div></section>"
    return {"path": path, "title": f"{title} | Jordan River Roofing", "meta": meta, "body": body, "full_biz": False, "schema": [crumbs_ld(path, trail)]}


def crumbs_html_plain(trail):
    from build import crumbs_html
    return crumbs_html(trail).replace('class="crumbs"', 'class="crumbs dark"')


def notfound():
    body = f'''<section class="sec"><div class="wrap"><p class="label">404</p><h1>That stop isn&rsquo;t on the line.</h1>
<p class="lede">Try the <a href="@/">home page</a>, our <a href="@/services">services</a> or the <a href="@/service-areas">service areas</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></section>'''
    return {"path": "404.html", "title": "Page Not Found | Jordan River Roofing", "meta": "This page isn't on the Jordan River Roofing site. Try the home page, services or service areas, or call 801-857-1417.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def make_pages():
    pages = [home(), about(), services_index(), areas_index(), warranties(), gallery(), contact(),
             legal("privacy-policy", "Privacy Policy", "How Jordan River Roofing collects, uses and protects the personal information you share through our website and services."),
             legal("terms-and-conditions", "Terms & Conditions", "The terms that govern your use of the Jordan River Roofing website and services in Taylorsville and the Salt Lake Valley.")]
    pages += [service_page(s[0]) for s in SERVICES]
    pages += [area_page(c[0]) for c in CITIES]
    pages += [svc_city_page(s[0], c[0]) for s in SERVICES for c in CITIES]
    pages += [p_blog.page(), notfound()]
    return pages
