"""All pages for the oakleyroofingslc.com redesign, on the client's current URLs plus a blog, a new post and a 404.

Facts come only from the client's own site (17 Oct 2026): founded 1993 by Bryce Oakley; owner involved from bid to final
inspection; most business from referrals and repeat customers; licensed crew trained and certified by the product
manufacturers, some with the company 10+ years; custom fabrication shop in Salt Lake City; TPO, EPDM, PVC, shingle and
metal roofing; commercial roofs 900-45,000 sq ft, homes 900-15,000 sq ft; building types; FHA roof inspections; Tesla
Certified Solar Roof Installers; the Tesla tile and Powerwall specs the site lists; spring and fall inspections advice;
free quotes; the three named reviews on the home page, word for word.
Not used (see notes): "best/premier/#1 roofer in Utah", "we guarantee your roof will withstand any type of weather",
the $20,000 solar savings figure (no source), the "Class 3 ... Best Hail Rating" line (Class 4 is the top FM 4473 class),
the solar pages' other phone numbers and email, the service area (the site says both "Northern Utah" and "Utah, Nevada,
Colorado & Wyoming"), the partner logos, and the 4.6-star / 14-review Google rating (not on the site; ask the client).
Report (17 Oct 2026): home targets "roofing company salt lake city"; every service page names Salt Lake City.
"""
import html
from build import (U, S, ARROW, PHONE, CHECK, CONTACT, BLOG, LINES, IMG, img, phero, cta, faq_html, faq_ld, crumbs_ld, quote_form, title_block)
import p_blog

HOME = ("Home", "")
REVIEWS = [("Oakley Roofing helped repair my mom&rsquo;s roof. Bryce was professional and easy to communicate with. We found that they were affordable, and got the job done fast while providing quality work. We will not hesitate to refer them to our friends and family. Thank you Oakley Roofing!!", "Jaselyn Short"),
           ("Had them assigned to us by a contractor after our house was impaled by a fallen tree, and they did amazing work. In and out in 2 days with a new garage roof and main house roof. Highly recommend them!", "Stevan Thibodeaux"),
           ("They did an amazing job on my roof like I don&rsquo;t even know how they don&rsquo;t have more reviews. I wish I could give more than five stars if it were my choice I would give 20 stars. The service there is amazing and the work is honest.", "Felicia West")]
PROJECTS = [("single-ply-roof-deck-new-install", "Commercial", "Single-ply membrane", "A new white single-ply roof deck, with the Wasatch on the horizon"),
            ("restaurant-metal-roof-aerial", "Restaurant", "Metal roof", "Metal roofing over a restaurant, from the air"),
            ("apartment-new-build-white-roof", "Apartments", "White membrane, new build", "A new white membrane roof on an apartment building under construction"),
            ("commercial-flat-roof-aerial", "Commercial", "Low-slope roof", "A low-slope commercial roof with rooftop units, from the air"),
            ("residential-new-construction-roof", "Custom home", "New construction", "A custom home under construction, with the lift and crew truck on site"),
            ("solar-roof-home-aerial", "Residential", "Solar roof", "A home with a solar roof, from the air"),
            ("white-membrane-roof-sunset", "Commercial", "White membrane", "A finished white membrane roof at sunset")]
BUILDINGS = ["Office buildings", "Retail locations", "Restaurants", "Warehouses", "Factories", "Condominium complexes", "Apartment complexes"]
MEMBRANES = {"tpo": ("TPO", "Thermoplastic polyolefin", [("Seams", "Heat-welded"), ("Usual color", "White"), ("Standard", "ASTM D6878")],
                     "A thermoplastic sheet that softens with heat, so the seams are welded together on the roof. No added plasticizers."),
             "epdm": ("EPDM", "Synthetic rubber", [("Seams", "Adhesive or tape"), ("Usual color", "Black or white"), ("Standard", "ASTM D4637")],
                      "A thermoset rubber that doesn&rsquo;t melt once cured, so seams are bonded with tape or adhesive. Sheets come up to 50 ft wide."),
             "pvc": ("PVC", "Poly(vinyl chloride)", [("Seams", "Heat-welded"), ("Usual color", "White or light"), ("Standard", "ASTM D4434")],
                     "Also heat-welded. Resists oils and grease, which is why it suits restaurant and kitchen exhaust areas.")}


def checks(items):
    return '<ul class="checks">' + "".join(f"<li><i>{CHECK}</i><span>{x}</span></li>" for x in items) + "</ul>"


def iso(x, y, z, ox=410, oy=232):
    return (ox + (x - y) * 0.866, oy + (x + y) * 0.5 - z)


def slab(z, t, cls, W=360, D=260):
    p = lambda x, y, zz: "%.1f,%.1f" % iso(x, y, zz)
    top = f'<polygon class="{cls} top" points="{p(0,0,z+t)} {p(W,0,z+t)} {p(W,D,z+t)} {p(0,D,z+t)}"/>'
    right = f'<polygon class="{cls} side-r" points="{p(W,0,z+t)} {p(W,D,z+t)} {p(W,D,z)} {p(W,0,z)}"/>'
    front = f'<polygon class="{cls} side-f" points="{p(0,D,z+t)} {p(W,D,z+t)} {p(W,D,z)} {p(0,D,z)}"/>'
    return top + right + front


def assembly_svg():
    """Exploded axonometric of a low-slope single-ply roof: deck, insulation, cover board, membrane."""
    W, D = 360, 260
    L = lambda x1, y1, z1, x2, y2, z2, c: '<path class="%s" d="M%.1f %.1f L%.1f %.1f"/>' % ((c,) + iso(x1, y1, z1) + iso(x2, y2, z2))
    deck = slab(0, 12, "deck") + "".join(L(x, 0, 12, x, D, 12, "rib") for x in range(18, W, 24))
    ins = slab(70, 26, "ins") + "".join(L(x, 0, 96, x, D, 96, "joint") for x in (120, 240)) + L(0, 130, 96, W, 130, 96, "joint")
    cover = slab(140, 8, "cover") + "".join(L(x, 0, 148, x, D, 148, "joint2") for x in (90, 180, 270))
    mem = slab(196, 3, "mem") + "".join(L(x, 0, 199, x, D, 199, "seam") for x in (120, 240))
    fast = "".join('<circle class="fast" cx="%.1f" cy="%.1f" r="2.2"/>' % iso(x, y, 199) for x in (114, 126, 234, 246) for y in range(30, D, 55))
    # label column on the right; leaders run from the front-right corner of each layer
    labels = [(199, 70, "05", "Membrane", "TPO, EPDM or PVC"), (148, 160, "04", "Cover board", "A hard, smooth base for the membrane"),
              (96, 250, "03", "Insulation", "Rigid boards, staggered joints"), (42, 340, "02", "Vapor retarder", "Where the design calls for one"),
              (12, 430, "01", "Roof deck", "Steel, wood or concrete")]
    lab = ""
    for z, ly, n, t, d in labels:
        x0, y0 = iso(W, D * 0.62, z)
        lab += (f'<circle class="dot" cx="{x0:.1f}" cy="{y0:.1f}" r="3"/><path class="lead" d="M{x0:.1f} {y0:.1f} L{x0 + 40:.1f} {ly:.1f} H770"/>'
                f'<text class="ln" x="780" y="{ly - 6:.1f}">{n}</text><text class="lt" x="808" y="{ly - 6:.1f}">{t}</text><text class="ld" x="808" y="{ly + 14:.1f}">{d}</text>')
    return f'''<svg class="assembly" viewBox="0 0 1060 560" role="img" aria-labelledby="as-t as-d"><title id="as-t">A low-slope roof assembly, exploded</title>
<desc id="as-d">From the bottom: the roof deck, a vapor retarder where the design calls for one, rigid insulation boards with staggered joints, a cover board, and the single-ply membrane on top, with its seams and fasteners.</desc>
<g class="layer l1">{deck}</g><g class="layer l2">{ins}</g><g class="layer l3">{cover}</g><g class="layer l4">{mem}{fast}</g>
<g class="labels">{lab}</g></svg>
<ol class="asm-legend"><li><b>05</b> Membrane</li><li><b>04</b> Cover board</li><li><b>03</b> Insulation</li><li><b>02</b> Vapor retarder</li><li><b>01</b> Roof deck</li></ol>'''


def assembly_block():
    tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if k == "tpo" else "false"}" data-m="{k}"{"" if k == "tpo" else " tabindex=\"-1\""}>{v[0]}</button>' for k, v in MEMBRANES.items())
    panels = "".join(f'''<div class="mem-panel" data-m="{k}"{"" if k == "tpo" else " hidden"}><p class="mem-name"><b>{v[0]}</b> {v[1]}</p><dl>{"".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in v[2])}</dl><p>{v[3]}</p></div>''' for k, v in MEMBRANES.items())
    return f'''<div class="asm" data-m="tpo"><div class="asm-draw">{assembly_svg()}</div>
<div class="asm-side"><div class="mem-tabs" role="tablist" aria-label="Membrane">{tabs}</div>{panels}
<a class="more" href="@/{BLOG[1]}">TPO vs. EPDM vs. PVC, compared {ARROW}</a></div></div>'''


def project_index(items=PROJECTS):
    rows = "".join(f'''<li data-img="{n}"><a href="@/{"commercial/" if t not in ("Custom home", "Residential") else ("solar/" if s == "Solar roof" else "residential/")}"><span class="pi-n">{i + 1:02d}</span><span class="pi-t">{t}</span><span class="pi-s">{s}</span><span class="pi-th">{img(n, c)}</span></a></li>''' for i, (n, t, s, c) in enumerate(items))
    prev = "".join(f'<figure class="pi-shot{" on" if i == 0 else ""}" data-img="{n}">{img(n, c)}<figcaption class="mono">{c}</figcaption></figure>' for i, (n, t, s, c) in enumerate(items))
    return f'<div class="pindex"><div class="pi-prev" aria-hidden="true">{prev}</div><ol class="pi-list">{rows}</ol></div>'


def reviews_html():
    return '<div class="revs">' + "".join(f'<figure class="rev reveal"><blockquote><p>&ldquo;{q}&rdquo;</p></blockquote><figcaption><span class="mono">{i + 1:02d}</span>{n}</figcaption></figure>' for i, (q, n) in enumerate(REVIEWS)) + "</div>"


def lines_cards():
    pics = {"commercial": "apartment-new-build-white-roof", "residential": "residential-new-construction-roof", "solar": "solar-roof-home-aerial"}
    out = ""
    for i, (k, n, p, d, subs) in enumerate(LINES):
        sub = "".join(f'<li><a href="@/{sp}">{sn} {ARROW}</a></li>' for sn, sp in subs)
        out += f'''<article class="line-card reveal"><a class="lc-img" href="@/{p}">{img(pics[k], d)}<span class="mono">{i + 1:02d} / 03</span></a>
<div class="lc-body"><h3><a href="@/{p}">{n}</a></h3><p>{d}</p><ul>{sub}</ul></div></article>'''
    return f'<div class="lines">{out}</div>'


# ---------------------------------------------------------------- home
def home():
    faqs = [("Do you work on commercial and residential roofs?", "Yes. Oakley Roofing handles commercial roofs from 900 to 45,000 square feet and homes from 900 to 15,000, plus Tesla Solar Roof installation."),
            ("What roofing systems do you install?", f"TPO, EPDM, PVC, shingle and metal roofing. Our guide explains the three flat-roof membranes: <a href=\"@/{BLOG[1]}\">{BLOG[0]}</a>"),
            ("Is the quote free?", "Yes. Call the office at (801) 651-1000 or send a few details through the contact form."),
            ("Who will I deal with?", "Bryce Oakley founded the company in 1993, and the owner works directly with customers from the bid through installation to the final roof inspection."),
            ("Do you do FHA roof inspections?", "Yes. Oakley Roofing provides FHA roof inspections. Call the office to schedule one.")]
    slides = [("single-ply-roof-deck-new-install", "Commercial &middot; single-ply membrane"), ("restaurant-metal-roof-aerial", "Restaurant &middot; metal roof"), ("apartment-new-build-white-roof", "Apartments &middot; new build")]
    sl = "".join(f'<figure class="slide{" on" if i == 0 else ""}">{img(n, html.unescape(c).replace("·", "-"), priority=(i == 0), lazy=(i != 0))}</figure>' for i, (n, c) in enumerate(slides))
    caps = "".join(f'<li class="{"on" if i == 0 else ""}"><span class="mono">{i + 1:02d}</span><b>{c}</b><i></i></li>' for i, (n, c) in enumerate(slides))
    bt = "".join(f"<span>{b}</span>" for b in BUILDINGS)
    body = f'''
<section class="hero"><div class="slides">{sl}</div><div class="frame" aria-hidden="true"></div>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">Oakley Roofing &middot; Salt Lake City &middot; since 1993</p>
<h1>Roofing company in Salt Lake City <span>for the roof you see from above.</span></h1>
<p class="lede">Commercial membranes and metal, residential shingle roofs, repairs, maintenance and the Tesla Solar Roof, from a Salt Lake City company that&rsquo;s been roofing the Wasatch Front since 1993.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="hero-side"><div class="north" aria-hidden="true"><svg viewBox="0 0 40 60"><path d="M20 4 L32 44 L20 36 L8 44 Z"/><text x="20" y="58">N</text></svg></div>
<ol class="slide-caps" aria-label="Photos">{caps}</ol></div>
</div></section>

<section class="sec intro"><div class="wrap intro-grid">
<p class="label">A-001 &middot; The fifth elevation</p>
<p class="big-say reveal">Architects call the roof a building&rsquo;s <em>fifth elevation</em>: the side most people never see, and the one that does the most work. <span>Oakley Roofing has been building them in Salt Lake City since 1993.</span></p>
<dl class="figs reveal"><div><dt>1993</dt><dd>Founded by Bryce Oakley</dd></div><div><dt>45,000</dt><dd>sq ft: the largest commercial roofs we take on</dd></div><div><dt>5</dt><dd>roof systems: TPO, EPDM, PVC, shingle, metal</dd></div></dl>
</div></section>

<section class="sec"><div class="wrap"><div class="head row reveal"><div><p class="label">Three lines of work</p><h2>Commercial, residential and solar</h2></div><a class="more" href="@/services/">All services {ARROW}</a></div>
{lines_cards()}</div></section>

<section class="sec dark asm-sec"><div class="wrap"><div class="head row reveal"><div><p class="label light">A-201 &middot; Section, exploded</p><h2>What&rsquo;s under a flat roof</h2></div>
<p class="head-note">Most commercial roofs in the valley are low-slope assemblies, built in layers. Pick a membrane to see how it&rsquo;s joined and what it&rsquo;s made of.</p></div>
<div class="reveal">{assembly_block()}</div></div></section>

<section class="sec"><div class="wrap"><div class="head row reveal"><div><p class="label">Project index</p><h2>Roofs we&rsquo;ve built</h2></div><p class="head-note">Photos from Oakley Roofing jobs: commercial membranes, metal, new construction and solar.</p></div>
{project_index()}</div></section>

<section class="bt-band" aria-label="Building types"><div class="bt-track">{bt}{bt.replace("<span>", '<span aria-hidden="true">')}</div></section>

<section class="sec owner"><div class="wrap split">
<figure class="reveal owner-img">{img("residential-new-construction-roof", "A custom home under construction, with the lift and crew truck on site")}</figure>
<div class="reveal"><p class="label">Since 1993</p><h2>The owner is on your project, start to finish</h2>
<p class="lede">Bryce Oakley founded Oakley Roofing in 1993. Customers say they recommend us because the owner is involved in their job, and most of our work still comes from referrals and repeat customers.</p>
{checks(["Owner works with you from the bid to the final roof inspection", "Licensed crew, trained and certified by the roofing manufacturers", "Some of our roofers have been with us for more than a decade", "Custom fabrication shop right here in Salt Lake City", "Small businesses, developers, government agencies and homeowners"])}
<a class="more" href="@/about-us/">About Oakley Roofing {ARROW}</a></div></div></section>

<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">Client reviews</p><h2>In our customers&rsquo; words</h2></div>{reviews_html()}</div></section>

<section class="sec solar-band"><div class="wrap split">
<div class="reveal"><p class="label light">Tesla Certified Solar Roof Installers</p><h2>A roof that makes its own power</h2>
<p class="lede">Oakley Roofing is certified by Tesla to install the Tesla Solar Roof in Utah. Solar and non-solar tiles look alike, and the roof can be paired with a Powerwall battery.</p>
<dl class="specs"><div><dt>Tile size</dt><dd>15&Prime; &times; 45&Prime;</dd></div><div><dt>Tile, power &amp; weather warranty</dt><dd>25 years</dd></div><div><dt>Roof pitch</dt><dd>9.5&deg; to 45&deg;</dd></div></dl>
<div class="btn-row"><a class="btn" href="@/solar-roof/">Tesla Solar Roof {ARROW}</a><a class="btn ghost light" href="@/solar-powerwall-2/">Powerwall</a></div></div>
<figure class="reveal">{img("solar-roof-home-aerial", "A home with a solar roof, from the air")}</figure></div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="label">Questions</p><h2>Before you call</h2><p class="lede">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div>
<div class="reveal">{faq_html(faqs)}</div></div></section>

<section class="sec paper"><div class="wrap split top">
<div class="reveal"><p class="label">Contact</p><h2>Get a free quote</h2><p class="lede">{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}<br>{S["hours"]}</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a></div>
<div class="reveal">{quote_form()}</div></div></section>''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company Salt Lake City, UT | Oakley Roofing Since 1993",
            "meta": "Oakley Roofing is a roofing company in Salt Lake City since 1993: commercial TPO, EPDM, PVC and metal roofs, residential roofing, repairs and Tesla Solar Roof.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(faqs)]}


# ---------------------------------------------------------------- service pages
SVC = {
 "residential-roofing-repairs/": dict(
    trail=[HOME, ("Services", "services/"), ("Residential", "residential/"), ("Roof Repairs", "residential-roofing-repairs/")],
    title="Roof Repair Salt Lake City | Residential Roof Repairs | Oakley Roofing",
    meta="Roof repair in Salt Lake City: water leak repair, storm and disaster repair, inspections and preventative maintenance for shingle roofs. Free quotes from Oakley.",
    h1="Roof Repair in Salt Lake City", label="Residential &middot; repairs &amp; maintenance", sheet="R-301", img="residential-new-construction-roof", alt="A home under construction, with the lift and crew truck on site",
    lead="<strong>Oakley Roofing repairs roofs in Salt Lake City:</strong> water leaks, storm and disaster damage, and worn or damaged shingles, plus inspections and preventative maintenance to keep small problems small.",
    body="""<h2>Fix it early, and the roof lasts longer</h2>
<p>Keeping a roof well maintained is the best way to limit the repairs it needs. Replacing damaged shingles and sealing leaks as they appear keeps a roof in good shape, and small spot repairs can push back the day you need a full replacement.</p>
<h2>What we repair</h2>
<ul><li><strong>Water leaks</strong>, traced to where the water is actually getting in</li><li><strong>Disaster and storm damage</strong>, including emergency work after a tree or a storm</li><li><strong>Damaged or missing shingles</strong></li><li><strong>Preventative maintenance</strong> to catch problems before they leak</li><li><strong>Inspections</strong>, including FHA roof inspections for home sales</li></ul>
<p>We clean up and haul away the debris when the work is done, and every quote is free.</p>
<h2>Repair or replace?</h2>
<p>Whatever is going on with your roof, we start with a thorough inspection and tell you what we find. If spot repairs will keep the roof going, we&rsquo;ll say so. If it&rsquo;s time for a new roof, see <a href="@/residential-roofing-installation/">residential roofing installation</a>.</p>
<p>One customer, Stevan, had a fallen tree come through his house: &ldquo;In and out in 2 days with a new garage roof and main house roof.&rdquo;</p>""",
    side=["Water leak repair", "Disaster &amp; storm repair", "Preventative maintenance", "Inspections", "Cleanup and disposal", "Shingle roofs", "Free quotes"],
    faqs=[("Can you repair a roof after storm or tree damage?", "Yes. Disaster repair is part of what we do. One customer&rsquo;s home was hit by a fallen tree, and we replaced the garage roof and main house roof in two days."),
          ("Should I repair or replace my roof?", "It depends on the roof&rsquo;s age and how widespread the damage is. Small spot repairs can extend a roof&rsquo;s life; we inspect first and explain the options."),
          ("Do you offer FHA roof inspections?", "Yes. Call the office at (801) 651-1000 to schedule one.")],
    service="Roof repair"),
 "residential-roofing-installation/": dict(
    trail=[HOME, ("Services", "services/"), ("Residential", "residential/"), ("Roof Installation", "residential-roofing-installation/")],
    title="Roof Installation Salt Lake City | New & Replacement Roofs | Oakley",
    meta="Roof installation in Salt Lake City: new construction roofs, roof replacement and custom homes, in shingle or metal, with a local fabrication shop. Free quotes.",
    h1="Roof Installation in Salt Lake City", label="Residential &middot; installation", sheet="R-201", img="residential-new-construction-roof", alt="A custom home under construction, with the lift and crew truck on site",
    lead="<strong>Oakley Roofing installs roofs in Salt Lake City</strong> on new construction and custom homes, and replaces old roofs with a fast, safe tear-off, in shingle or metal.",
    body="""<h2>New construction and custom homes</h2>
<p>Building a custom home? With a custom fabrication shop right in Salt Lake City and dozens of trusted suppliers, we&rsquo;re ready for the roof you have planned, whether it&rsquo;s shingle or metal.</p>
<h2>Roof replacement</h2>
<p>When an old roof has to come off, the crew tears it down and installs the new one quickly and safely, then cleans up and hauls the debris away. Every replacement is built to code.</p>
<h2>An experienced crew</h2>
<p>Our installers are licensed and trained and certified by the roofing manufacturers whose products we install, and some of our roofers have been with us for more than a decade. We&rsquo;d rather keep experienced people than train new ones every season.</p>
<h2>Small or large projects</h2>
<p>Homes from 900 square feet to 15,000 are in range. Call <a href="tel:+18016511000">(801) 651-1000</a> or <a href="@/contact-us/">send us the details</a> for a free quote.</p>""",
    side=["New construction", "Roof replacement", "Custom residential projects", "Shingle and metal roofing", "Custom fabrication in Salt Lake City", "Code compliance", "Cleanup and disposal", "Free quotes"],
    faqs=[("Do you roof new construction homes?", "Yes, including custom homes. Our custom fabrication shop is in Salt Lake City."),
          ("Do you install metal roofs on homes?", "Yes. We install shingle and metal residential roofs."),
          ("How big a home can you roof?", "We work on homes from about 900 square feet up to 15,000.")],
    service="Roof installation"),
 "commercial-roofing-installation/": dict(
    trail=[HOME, ("Services", "services/"), ("Commercial", "commercial/"), ("Installation", "commercial-roofing-installation/")],
    title="Commercial Roofing Installation Salt Lake City | Oakley Roofing",
    meta="Commercial roofing installation in Salt Lake City: TPO, EPDM, PVC, shingle and metal roofs for new construction and re-roofs, with custom fabrication in SLC.",
    h1="Commercial Roofing Installation in Salt Lake City", label="Commercial &middot; installation", sheet="C-201", img="single-ply-roof-deck-new-install", alt="A new white single-ply roof deck, with the Wasatch on the horizon",
    lead="<strong>Oakley Roofing installs commercial roofs in Salt Lake City:</strong> TPO, EPDM, PVC, shingle and metal systems on new construction and re-roofs, from small buildings to large complexes.",
    body=f"""<h2>New construction and re-roofing</h2>
<p>Re-roofing commercial buildings is our specialty, and we build roofs on new construction too, from apartments and condominiums to offices, retail and warehouses. Tear-off and installation are done fast and safely, and every job is built to code.</p>
<h2>Five roof systems</h2>
<p>We install TPO, EPDM and PVC single-ply membranes, shingle roofs and metal roofs. Each membrane is joined differently and suits different buildings; our guide compares them: <a href="@/{BLOG[1]}">{BLOG[0]}</a></p>
<h2>Custom commercial projects</h2>
<p>Constructing a custom building or complex? With a custom fabrication shop in Salt Lake City and dozens of trusted suppliers, we can take on the roof you have planned.</p>
<h2>Plan for inspections</h2>
<p>We recommend having a commercial roof inspected twice a year, in spring and fall, before the extreme seasons. Between inspections, owners or maintenance staff should keep an eye out for problems, and call us early when they spot one.</p>""",
    side=["New construction", "Roof replacement", "TPO, EPDM, PVC &amp; shingle", "Metal roofing", "Small or large projects", "Custom fabrication in Salt Lake City", "Code compliance", "Free quotes"],
    faqs=[("Which commercial roof systems do you install?", "TPO, EPDM and PVC single-ply membranes, shingle roofs and metal roofs."),
          ("How often should a commercial roof be inspected?", "We recommend twice a year, in spring and fall, before the extreme seasons."),
          ("How large a roof can you take on?", "Commercial roofs from about 900 square feet up to 45,000.")],
    service="Commercial roofing installation"),
 "commercial-roofing-repair-maintenance/": dict(
    trail=[HOME, ("Services", "services/"), ("Commercial", "commercial/"), ("Repair &amp; Maintenance", "commercial-roofing-repair-maintenance/")],
    title="Commercial Roof Repair Salt Lake City | Repair & Maintenance | Oakley",
    meta="Commercial roof repair and maintenance in Salt Lake City: leaks, disaster repair, preventative maintenance and inspections for TPO, EPDM, PVC and metal roofs.",
    h1="Commercial Roof Repair &amp; Maintenance in Salt Lake City", label="Commercial &middot; repair &amp; maintenance", sheet="C-301", img="commercial-flat-roof-aerial", alt="A low-slope commercial roof with rooftop units, from the air",
    lead="<strong>Oakley Roofing repairs and maintains commercial roofs in Salt Lake City:</strong> water leaks, disaster damage, preventative maintenance and inspections on TPO, EPDM, PVC, shingle and metal roofs.",
    body="""<h2>Maintenance first</h2>
<p>A well-maintained roof needs fewer repairs. Sealing leaks and replacing damaged sections as they appear keeps a roof working, and small spot repairs can put off a full replacement.</p>
<h2>What we repair</h2>
<ul><li><strong>Water leaks</strong> on low-slope and steep roofs</li><li><strong>Disaster repair</strong> after storms and other damage</li><li><strong>Preventative maintenance</strong> plans to catch problems early</li><li><strong>Inspections</strong>, ideally in spring and fall</li></ul>
<h2>Keeping the building running</h2>
<p>Your roof keeps employees, customers and inventory dry. We run on time and on budget, and clean up and dispose of debris when the work is done. Whether the issue is a single leak or a roof at the end of its life, we&rsquo;ll inspect it and give you a straight answer.</p>""",
    side=["Water leak repair", "Disaster repair", "Preventative maintenance", "Inspections", "TPO, EPDM, PVC &amp; shingle", "Metal roofs", "Cleanup and disposal", "Free quotes"],
    faqs=[("Do you repair TPO, EPDM and PVC roofs?", "Yes, along with shingle and metal commercial roofs."),
          ("Do you offer maintenance plans?", "We provide preventative maintenance and recommend inspections twice a year, in spring and fall.")],
    service="Commercial roof repair"),
}

HUBS = {
 "residential/": dict(trail=[HOME, ("Services", "services/"), ("Residential", "residential/")], line=1,
    title="Residential Roofing Salt Lake City | Oakley Roofing Since 1993",
    meta="Residential roofing in Salt Lake City since 1993: shingle and metal roofs, new construction, replacements, repairs and maintenance for homes of every size.",
    h1="Residential Roofing in Salt Lake City", sheet="R-100", img="residential-new-construction-roof", alt="A custom home under construction, with the lift and crew truck on site",
    lead="<strong>Oakley Roofing has roofed Salt Lake City homes since 1993:</strong> shingle and metal roofs for new construction and replacements, plus repairs and maintenance, for homes from 900 to 15,000 square feet.",
    body="""<h2>&ldquo;Keeping you covered&rdquo; is what we live by</h2>
<p>Your roof keeps your family protected, warm and dry every day. We&rsquo;ve always called the Wasatch Front home, and we treat every customer like a neighbor.</p>
<p>Our crew is licensed, thoroughly trained and friendly, and we have the materials, expertise and manpower to install the roof you have in mind.</p>"""),
 "residential-roofing-services/": dict(trail=[HOME, ("Services", "services/"), ("Residential Roofing Services", "residential-roofing-services/")], line=1,
    title="Residential Roofing Services Salt Lake City | Oakley Roofing",
    meta="Residential roofing services in Salt Lake City: roof installation and replacement in shingle or metal, and roof repairs and maintenance. Call Oakley Roofing.",
    h1="Residential Roofing Services in Salt Lake City", sheet="R-110", img="solar-roof-home-aerial", alt="A home with a solar roof, from the air",
    lead="<strong>Two ways we help Salt Lake City homeowners:</strong> installing new and replacement roofs in shingle or metal, and repairing and maintaining the roof you have.",
    body="""<h2>Installation or repair</h2>
<p>New roofs and replacements are covered on <a href="@/residential-roofing-installation/">residential roofing installation</a>. Leaks, storm damage and upkeep are on <a href="@/residential-roofing-repairs/">roof repairs</a>. Not sure which you need? We&rsquo;ll inspect the roof and tell you.</p>"""),
 "commercial/": dict(trail=[HOME, ("Services", "services/"), ("Commercial", "commercial/")], line=0,
    title="Commercial Roofing Salt Lake City | TPO, EPDM, PVC & Metal | Oakley",
    meta="Commercial roofing in Salt Lake City since 1993: TPO, EPDM, PVC, shingle and metal roofs for offices, retail, restaurants, warehouses and apartments.",
    h1="Commercial Roofing in Salt Lake City", sheet="C-100", img="restaurant-metal-roof-aerial", alt="Metal roofing over a restaurant, from the air",
    lead="<strong>Oakley Roofing is a commercial roofing contractor in Salt Lake City:</strong> TPO, EPDM, PVC, shingle and metal roofs, from 900 square feet to 45,000, with re-roofing as our specialty.",
    body=f"""<h2>On Salt Lake City&rsquo;s commercial roofs since 1993</h2>
<p>If you own or manage a factory, office building, apartment or condominium complex, or a warehouse, you know how much depends on the roof. We specialize in re-roofing commercial buildings, and we handle repairs and maintenance too. You can count on prompt service from a company that runs on time and on budget.</p>
<p>Small businesses, developers of every size, government agencies and property managers have trusted Oakley Roofing with their roofs.</p>
<h2>Building types</h2>
{checks(BUILDINGS)}"""),
 "commercial-services/": dict(trail=[HOME, ("Services", "services/"), ("Commercial Roofing Services", "commercial-services/")], line=0,
    title="Commercial Roofing Services Salt Lake City | Oakley Roofing",
    meta="Commercial roofing services in Salt Lake City: installation of TPO, EPDM, PVC, shingle and metal roofs, and commercial roof repair and maintenance.",
    h1="Commercial Roofing Services in Salt Lake City", sheet="C-110", img="apartment-new-build-white-roof", alt="A new white membrane roof on an apartment building under construction",
    lead="<strong>Two ways we serve Salt Lake City building owners:</strong> installing new and replacement commercial roofs, and repairing and maintaining the roof you have.",
    body="""<h2>Installation or repair</h2>
<p>New roofs and re-roofs are on <a href="@/commercial-roofing-installation/">commercial roofing installation</a>. Leaks, damage and maintenance plans are on <a href="@/commercial-roofing-repair-maintenance/">commercial repair and maintenance</a>. No job is too big or too small.</p>"""),
}


def side(items, title="What&rsquo;s included"):
    return f'''<aside class="side reveal"><div class="panel spec"><p class="label">{title}</p>{checks(items)}</div>
<div class="panel dark"><p class="label light">Free quote</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><p class="small">{S["hours"]}</p><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a></div></aside>'''


def related(cur):
    cards = ""
    for k, n, p, d, subs in LINES:
        for sn, sp in [(n + " roofing", p)] + subs:
            if sp == cur: continue
            cards += f'<li><a href="@/{sp}"><span class="mono">{n}</span><b>{sn}</b>{ARROW}</a></li>'
    return f'<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">More services</p><h2>Everything we roof</h2></div><ul class="rel">{cards}</ul></div></section>'


def service_page(path):
    d = SVC[path]
    body = phero(d["trail"], d["h1"], "", d["label"], d["img"], d["alt"], d["sheet"]) + f'''
<section class="intro-lead-sec"><div class="wrap"><p class="intro-lead reveal">{d["lead"]}</p></div></section>
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{d["body"]}</div>{side(d["side"])}</div></section>
<section class="sec dark"><div class="wrap split top"><div class="reveal"><p class="label light">Questions</p><h2>Common questions</h2></div><div class="reveal">{faq_html(d["faqs"])}</div></div></section>''' + related(path) + cta()
    return {"path": path, "canonical": U + path, "title": d["title"], "meta": d["meta"], "body": body, "og": d["img"], "full_biz": False,
            "schema": [crumbs_ld(path, d["trail"]), faq_ld(d["faqs"]),
                       {"@type": "Service", "@id": U + path + "#service", "name": d["service"], "serviceType": d["service"], "provider": {"@id": U + "#business"},
                        "areaServed": {"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}},
                        "description": html.unescape(d["lead"].replace("<strong>", "").replace("</strong>", ""))}]}


def hub_page(path):
    d = HUBS[path]
    k, n, p, desc, subs = LINES[d["line"]]
    cards = "".join(f'<a class="hub-card reveal" href="@/{sp}"><span class="mono">{i + 1:02d}</span><b>{sn}</b>{ARROW}</a>' for i, (sn, sp) in enumerate(subs) if sp != path)
    body = phero(d["trail"], d["h1"], "", f"{n} roofing", d["img"], d["alt"], d["sheet"]) + f'''
<section class="intro-lead-sec"><div class="wrap"><p class="intro-lead reveal">{d["lead"]}</p></div></section>
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{d["body"]}</div>
<div class="reveal"><p class="label">{n} services</p><div class="hub-cards">{cards}</div></div></div></section>''' + (f'''
<section class="sec dark asm-sec"><div class="wrap"><div class="head reveal"><p class="label light">A-201 &middot; Section, exploded</p><h2>What&rsquo;s under a flat roof</h2></div>{assembly_block()}</div></section>''' if k == "commercial" else "") + \
        f'<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">Client reviews</p><h2>In our customers&rsquo; words</h2></div>{reviews_html()}</div></section>' + cta()
    return {"path": path, "canonical": U + path, "title": d["title"], "meta": d["meta"], "body": body, "og": d["img"], "full_biz": False,
            "schema": [crumbs_ld(path, d["trail"])]}


def services_index():
    trail = [HOME, ("Services", "services/")]
    body = phero(trail, "Roofing Services in Salt Lake City", "Commercial, residential and solar roofing from Oakley Roofing, a Salt Lake City company since 1993.", "Our services",
                 "white-membrane-roof-sunset", "A finished white membrane roof at sunset", "A-010") + f'''
<section class="sec"><div class="wrap">{lines_cards()}</div></section>
<section class="sec dark"><div class="wrap"><div class="head reveal"><p class="label light">Project index</p><h2>Roofs we&rsquo;ve built</h2></div>{project_index()}</div></section>''' + cta()
    return {"path": "services/", "canonical": U + "services/", "title": "Roofing Services Salt Lake City | Commercial, Residential, Solar | Oakley",
            "meta": "Roofing services in Salt Lake City from Oakley Roofing: commercial TPO, EPDM, PVC and metal, residential shingle and metal, repairs, and Tesla Solar Roof.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("services/", trail)]}


# ---------------------------------------------------------------- solar
def solar_page(path):
    if path == "solar/":
        trail = [HOME, ("Services", "services/"), ("Solar", "solar/")]
        h1, title = "Tesla Solar Roof Installers in Salt Lake City", "Tesla Solar Roof Installer Salt Lake City | Oakley Roofing"
        meta = "Oakley Roofing is a Tesla Certified Solar Roof Installer in Utah: the Tesla Solar Roof and Powerwall for Salt Lake City homes from 900 to 15,000 sq ft."
        lead = "<strong>Oakley Roofing is certified by Tesla to install the Tesla Solar Roof in Utah.</strong> We&rsquo;re locally owned in Salt Lake City and handle the complete installation, for homes from 900 to 15,000 square feet."
        body = """<h2>A roofing company that installs solar</h2>
<p>The Tesla Solar Roof is a roof first: solar tiles and non-solar tiles that look the same, laid as a complete new roof. It makes sense to have it installed by a roofing company, and Oakley Roofing has been roofing Salt Lake City since 1993.</p>
<h2>What we handle</h2>
<ul><li><strong>Installation</strong> of the complete Tesla Solar Roof</li><li><strong>Upgrades</strong> for homeowners replacing an existing roof</li><li><strong>Upkeep and repair</strong> of your roof over time</li><li><strong>Powerwall</strong> battery storage, to keep power on when the grid goes down</li></ul>
<p>Book a free consultation to talk through your roof, your home and your energy use.</p>"""
        sheet, image, alt = "S-100", "solar-roof-home-aerial", "A home with a solar roof, from the air"
        faqs = [("Is Oakley Roofing a certified Tesla Solar Roof installer?", "Yes. Oakley Roofing is certified by Tesla to install the Solar Roof in Utah."),
                ("Can I add a Powerwall?", "Yes. The Powerwall stores energy and takes over automatically when the grid goes down. See <a href=\"@/solar-powerwall-2/\">Tesla Powerwall</a>.")]
        svc = "Tesla Solar Roof installation"
    elif path == "solar-roof/":
        trail = [HOME, ("Services", "services/"), ("Solar", "solar/"), ("Tesla Solar Roof", "solar-roof/")]
        h1, title = "The Tesla Solar Roof in Salt Lake City", "Tesla Solar Roof Salt Lake City | Tiles, Specs & Install | Oakley"
        meta = "The Tesla Solar Roof in Salt Lake City: tempered-glass solar tiles that look like the rest of the roof, a 25-year tile, power and weather warranty, installed by Oakley."
        lead = "<strong>The Tesla Solar Roof replaces your roof with tiles that make power.</strong> Solar and non-solar tiles look virtually the same, and Oakley Roofing installs it across Salt Lake City and Utah."
        body = """<h2>Solar you can&rsquo;t pick out from the street</h2>
<p>Each solar and non-solar tile is virtually indistinguishable in color and trim, so the roof looks the same from every angle. The tiles are tempered glass, engineered for all-weather durability, including active snow and ice melting.</p>
<h2>More tiles, more power</h2>
<p>A single larger tile in each module means more of the roof can produce energy, so the system can be sized to what your home uses. Tesla designs each roof with drone analysis and sun and shade modeling, and the modular design installs in a matter of days.</p>
<h2>Tile ratings</h2>
<p>These are the figures the site lists for the tiles; your proposal will confirm the details for your roof.</p>"""
        sheet, image, alt = "S-200", "solar-roof-home-aerial", "A home with a solar roof, from the air"
        faqs = [("What warranty comes with the Tesla Solar Roof tiles?", "25 years, covering the tiles, power and weather, as listed on the specification."),
                ("Will it work on my roof&rsquo;s pitch?", "The tiles are rated for roof pitches from 9.5&deg; to 45&deg;. We&rsquo;ll check your roof during the consultation.")]
        svc = "Tesla Solar Roof"
    else:
        trail = [HOME, ("Services", "services/"), ("Solar", "solar/"), ("Tesla Powerwall", "solar-powerwall-2/")]
        h1, title = "Tesla Powerwall Installation in Salt Lake City", "Tesla Powerwall Salt Lake City | Home Battery Backup | Oakley"
        meta = "Tesla Powerwall in Salt Lake City from Oakley Roofing: a home battery that stores solar energy and takes over automatically when the grid goes down."
        lead = "<strong>The Powerwall is a home battery.</strong> It stores energy, detects outages, and becomes your home&rsquo;s power source automatically when the grid goes down. Pair it with solar and it recharges from sunlight."
        body = """<h2>Backup without the generator</h2>
<p>Unlike a gasoline generator, a Powerwall keeps the lights on and phones charged with no upkeep, fuel or noise. Pair it with a Tesla Solar Roof and it recharges from your own roof.</p>
<h2>Specifications</h2>
<p>The figures below are the Powerwall 2 specifications listed on this page; Tesla updates the product, so we&rsquo;ll confirm the current model and specs in your proposal.</p>"""
        sheet, image, alt = "S-300", "solar-roof-home-aerial", "A home with a solar roof, from the air"
        faqs = [("What does a Powerwall do in an outage?", "It detects the outage and automatically becomes your home&rsquo;s energy source until the grid comes back."),
                ("Can it be installed outdoors?", "Yes. The listed specification allows floor or wall mounting, indoors or outdoors.")]
        svc = "Tesla Powerwall installation"
    specs = ""
    if path == "solar-roof/":
        specs = '<dl class="specs light">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [("Tile size", "15&Prime; wide, 45&Prime; long"), ("Tile, power &amp; weather warranty", "25 years"), ("Roof pitch", "9.5&deg; to 45&deg;"), ("Material", "Tempered glass")]) + "</dl>"
    if path == "solar-powerwall-2/":
        specs = '<dl class="specs light">' + "".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in [("Energy capacity", "13.5 kWh, 100% depth of discharge"), ("Power", "7 kW peak / 5 kW continuous"), ("Round-trip efficiency", "90%"), ("Size", "45.3&Prime; &times; 29.6&Prime; &times; 5.75&Prime;, 251.3 lb"), ("Installation", "Floor or wall, indoor or outdoor, up to 10 units"), ("Operating range", "&minus;4&deg;F to 122&deg;F, IP67"), ("Warranty", "10 years")]) + "</dl>"
    subs = "".join(f'<a class="hub-card reveal" href="@/{sp}"><span class="mono">{i + 1:02d}</span><b>{sn}</b>{ARROW}</a>' for i, (sn, sp) in enumerate([("Solar", "solar/"), ("Tesla Solar Roof", "solar-roof/"), ("Tesla Powerwall", "solar-powerwall-2/")]) if sp != path)
    body = phero(trail, h1, "", "Solar &middot; Tesla Certified Solar Roof Installers", image, alt, sheet) + f'''
<section class="intro-lead-sec"><div class="wrap"><p class="intro-lead reveal">{lead}</p></div></section>
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{body}{specs}</div><div class="reveal"><p class="label">Solar</p><div class="hub-cards">{subs}</div></div></div></section>
<section class="sec dark"><div class="wrap split top"><div class="reveal"><p class="label light">Questions</p><h2>Common questions</h2></div><div class="reveal">{faq_html(faqs)}</div></div></section>''' + cta("Thinking about a solar roof?", "Book a free consultation. We&rsquo;ll look at the roof and walk you through the Tesla Solar Roof and Powerwall.", "solar-roof-home-aerial")
    return {"path": path, "canonical": U + path, "title": title, "meta": meta, "body": body, "og": image, "full_biz": False,
            "schema": [crumbs_ld(path, trail), faq_ld(faqs), {"@type": "Service", "@id": U + path + "#service", "name": svc, "serviceType": svc, "provider": {"@id": U + "#business"},
                       "areaServed": {"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}}}]}


# ---------------------------------------------------------------- company pages
def about():
    trail = [HOME, ("About", "about-us/")]
    body = phero(trail, "About Oakley Roofing, Salt Lake City Roofers Since 1993", "Bryce Oakley founded Oakley Roofing in 1993 with a mission to cover Utah.", "About us",
                 "apartment-new-build-white-roof", "A new white membrane roof on an apartment building under construction", "A-002") + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">
<h2>Keeping Utah covered</h2>
<p>Bryce Oakley founded Oakley Roofing in 1993 with a mission to cover Utah. An expert in both residential and commercial roofing, he built the company around quality, affordability and customer service.</p>
<p>Small businesses, developers of every size, government agencies and everyday Utahns have trusted Oakley Roofing to repair, replace and maintain roofs of every kind.</p>
<h2>The owner works with you</h2>
<p>Most of our business comes from referrals and repeat customers. Customers tell us they recommend Oakley Roofing because the owner is involved in their project: answering questions during the bid, keeping quality control during installation, and doing the final roof inspection.</p>
<p>We believe in explaining your roofing options so you can choose the right one, and we guide you through the whole process.</p>
<h2>What we do</h2>
<p>New construction roofs, re-roofing, roof installation, repairs and maintenance for residential and commercial customers, FHA roof inspections, and the Tesla Solar Roof, as Tesla Certified Solar Roof Installers.</p>
</div>{side(["Founded 1993 by Bryce Oakley", "Owner involved start to finish", "Licensed, manufacturer-trained crew", "Custom fabrication shop in Salt Lake City", "Tesla Certified Solar Roof Installers", "FHA roof inspections"], "At a glance")}</div></section>
<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">Client reviews</p><h2>In our customers&rsquo; words</h2></div>{reviews_html()}</div></section>''' + cta()
    return {"path": "about-us/", "canonical": U + "about-us/", "title": "About Oakley Roofing | Salt Lake City Roofers Since 1993",
            "meta": "Oakley Roofing was founded in 1993 by Bryce Oakley. The owner works with every customer, from the bid to the final roof inspection. Salt Lake City, Utah.",
            "body": body, "full_biz": True, "og": "apartment-new-build-white-roof",
            "schema": [crumbs_ld("about-us/", trail), {"@type": "AboutPage", "@id": U + "about-us/#webpage", "url": U + "about-us/", "name": "About Oakley Roofing", "about": {"@id": U + "#business"}}]}


def contact():
    trail = [HOME, ("Contact", "contact-us/")]
    body = phero(trail, "Contact Oakley Roofing in Salt Lake City", "Free, no-hassle quotes, expert inspections and every roofing service we offer. Call or send a message.", "Contact",
                 "commercial-flat-roof-aerial", "A low-slope commercial roof with rooftop units, from the air", "A-900", buttons=False) + f'''
<section class="sec"><div class="wrap split top">
<div class="reveal"><dl class="contact-list"><div><dt>Our office</dt><dd>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</dd></div>
<div><dt>Office hours</dt><dd>M&ndash;F: 8am &ndash; 6pm<br>Sat&ndash;Sun: 10am &ndash; 4pm</dd></div>
<div><dt>Get in touch</dt><dd><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a></dd></div></dl></div>
<div class="reveal sticky">{quote_form("Get an estimate")}</div></div></section>'''
    return {"path": "contact-us/", "canonical": U + "contact-us/", "title": "Contact Oakley Roofing | Free Roofing Quotes in Salt Lake City",
            "meta": "Contact Oakley Roofing at (801) 651-1000, 49 West Burton Ave., Salt Lake City, UT 84115, for free roofing quotes and inspections. Open seven days.",
            "body": body, "full_biz": True, "schema": [crumbs_ld("contact-us/", trail), {"@type": "ContactPage", "@id": U + "contact-us/#webpage", "url": U + "contact-us/", "name": "Contact Oakley Roofing"}]}


def sitemap_page(pages):
    trail = [HOME, ("Sitemap", "sitemap/")]
    lis = "".join(f'<li><a href="@/{p["path"]}">{html.escape(p["title"].split(" | ")[0])}</a></li>' for p in pages if p.get("sitemap", True) and p["path"] not in ("sitemap/",))
    body = phero(trail, "Sitemap", "Every page on the Oakley Roofing site.", "Sitemap", None, "", "A-998", buttons=False) + f'<section class="sec"><div class="wrap"><ul class="sm-list">{lis}</ul></div></section>'
    return {"path": "sitemap/", "canonical": U + "sitemap/", "title": "Sitemap | Oakley Roofing", "meta": "All pages on the Oakley Roofing website: commercial, residential and solar roofing services in Salt Lake City, plus the blog.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("sitemap/", trail)]}


def leftover(path, name):
    """WordPress leftovers: kept on their URLs so nothing 404s, but noindex and out of the sitemap (see notes for the 301s)."""
    body = phero([HOME, (name, path)], name, "This page has moved. Roofing guides from Oakley Roofing are on the blog.", "Moved", None, "", "A-997", buttons=False) + \
        f'<section class="sec"><div class="wrap"><a class="btn" href="@/blog/">Go to the blog {ARROW}</a></div></section>'
    return {"path": path, "canonical": U + "blog/", "title": f"{name} | Oakley Roofing", "meta": "This page has moved. Roofing guides from Oakley Roofing in Salt Lake City are on the blog.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def blog_index():
    trail = [HOME, ("Blog", "blog/")]
    body = phero(trail, "Oakley Roofing Blog", "Plain answers to roofing questions from a Salt Lake City roofing company.", "Blog", None, "", "B-000", buttons=False) + f'''
<section class="sec"><div class="wrap"><a class="feature reveal" href="@/{BLOG[1]}"><figure>{img("single-ply-roof-deck-new-install", "A new white single-ply roof deck")}</figure>
<div><p class="label light">Guide &middot; commercial roofing</p><h2>{BLOG[0]}</h2><p>How the three single-ply membranes differ, what Utah&rsquo;s building code asks for, and how to choose one for your building.</p><span class="more light">Read the guide {ARROW}</span></div></a></div></section>''' + cta()
    return {"path": "blog/", "canonical": U + "blog/", "title": "Roofing Blog | Oakley Roofing, Salt Lake City",
            "meta": "Roofing guides from Oakley Roofing in Salt Lake City: commercial flat roof membranes, repairs, replacement and the Tesla Solar Roof.",
            "body": body, "full_biz": False, "schema": [crumbs_ld("blog/", trail), {"@type": "Blog", "@id": U + "blog/#blog", "url": U + "blog/", "name": "Oakley Roofing blog"}]}


def notfound():
    body = phero([HOME, ("404", "404.html")], "This roof isn&rsquo;t on the plans.", "That page isn&rsquo;t on the Oakley Roofing site. Try the home page, our services or the blog, or call (801) 651-1000.", "404", None, "", "A-404", buttons=False) + \
        f'<section class="sec"><div class="wrap btn-row"><a class="btn" href="@/">Home {ARROW}</a><a class="btn ghost" href="@/services/">Services</a><a class="btn ghost" href="@/blog/">Blog</a></div></section>'
    return {"path": "404.html", "canonical": None, "title": "Page Not Found | Oakley Roofing", "meta": "This page isn't on the Oakley Roofing site. Try the home page, our roofing services or the blog, or call (801) 651-1000.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def make_pages():
    pages = [home(), about(), contact(), services_index()]
    pages += [hub_page(p) for p in HUBS] + [service_page(p) for p in SVC] + [solar_page(p) for p in ("solar/", "solar-roof/", "solar-powerwall-2/")]
    pages += [blog_index(), p_blog.page()]
    pages += [leftover("hello-world/", "Hello world!"), leftover("category/uncategorized/", "Uncategorized"), leftover("author/supportthemesupport-net/", "ThemeSupport")]
    pages.append(sitemap_page(pages))
    pages.append(notfound())
    return pages
