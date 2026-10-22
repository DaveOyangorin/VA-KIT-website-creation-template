"""Pages for the xperienceroofing.com redesign: "The Collection".

The client already writes like a catalogue: five named "signature systems", a "Material World" of layers, an "Installer's
Standard" of six principles and a six-step process. The redesign presents those as a collection: a system selector with an
original profile drawing for each system, the layer stack drawn exploded, the standard and the process as numbered plates.
There are no real photos on the current site (every image is stock, several with invented city captions such as "Standing
seam metal - Draper, UT"), so none are used; the design is type and drawings until the client sends job photos.
Home and the blog post are written by hand. All 34 other pages keep the client's own text (cleaned out of the Next.js markup),
with a new title, meta and opening paragraph; report (17 Oct 2026): home targets "roofing company midvale" and every service
page names Midvale. Dropped: stock-photo captions with city names, lifespans and warranty-length figures, and form blocks.
"""
import html, re
from engine import crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, CITIES, NAME, U, HERE, DOMAIN
from migrate import migrate
from illus import profile, stack
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CONTACT = "contact/"
HOME = ("Home", "")
LOGO = '<img src="@img/xperience-logo-light.svg" alt="Xperience Roofing" width="353" height="128">'
DROP = re.compile(r"\d+\s*[–-]\s*\d+\+?\s*(?:year|yr)|lifetime|Name \*|Request My Free Estimate|reply STOP|It.s OK to text", re.I)
STOPS = re.compile(r"Start (?:with an|at) |Price This System|Where It Fits|What Happens Next|Where it goes|Free Estimate|Related Services|Start Your", re.I)

SERVICES = [("services/roof-replacement/", "Roof Replacement", "services_roof_replacement", "roof replacement"),
            ("services/roof-repair/", "Roof Repair", "services_roof_repair", "roof repair"),
            ("services/roof-inspections/", "Roof Inspections", "services_roof_inspections", "roof inspections"),
            ("services/commercial-roofing/", "Commercial Roofing", "services_commercial_roofing", "commercial roofing"),
            ("services/metal-roofing/", "Metal Roofing", "services_metal_roofing", "metal roofing"),
            ("services/solar-detach-reset/", "Solar Detach &amp; Reset", "services_solar_detach_reset", "solar detach and reset")]
SYSTEMS = [("systems/the-classic/", "The Classic", "Architectural Asphalt Shingle", "classic", "Fiberglass-based asphalt with ceramic granules", "Entry &mdash; High End",
            ["Charcoal", "Weathered Wood", "Pewter Gray", "Driftwood", "Onyx"], ["#3b3d40", "#7b6a58", "#8a8d90", "#a89a86", "#1f2023"], "systems_the_classic"),
           ("systems/the-standing-seam/", "The Standing Seam", "Metal Roofing", "standing", "Galvanized or Galvalume steel, 24&ndash;26 gauge", "Premium",
            ["Galvalume", "Slate Gray", "Charcoal", "Matte Black", "Copper Penny"], ["#b9bdbf", "#6d7378", "#3e4246", "#1d1e20", "#a8633a"], "systems_the_standing_seam"),
           ("systems/the-heritage/", "The Heritage", "Clay &amp; Concrete Tile", "heritage", "Fired clay or cast concrete with pigment", "Mid &mdash; High End",
            ["Terracotta", "Mission Red", "Sand Blend", "Slate", "Antique Buff"], ["#b7643c", "#8e3a26", "#cbb08a", "#5b6064", "#d6c3a0"], "systems_the_heritage"),
           ("systems/the-summit/", "The Summit", "Metal Shake", "summit", "Pre-painted steel or aluminum panels", "Premium",
            ["Weathered Zinc", "Aged Cedar", "Mountain Bronze", "Charcoal Oak", "Warm Copper"], ["#8d9597", "#8a6a4c", "#5c4a36", "#3d3a36", "#b06a3e"], "systems_the_summit"),
           ("systems/the-flat-line/", "The Flat Line", "TPO / EPDM Low-Slope &amp; Commercial", "flat", "TPO or EPDM membrane, 45&ndash;90 mil", "Entry &mdash; High End",
            ["White TPO", "Light Gray", "Gray", "Black EPDM", "Dark Gray"], ["#f2f2ef", "#c9cbcc", "#8f9396", "#1c1d1f", "#4b4e51"], "systems_the_flat_line")]
MATERIALS = [("materials/surface/", "Surface Layer", "materials_surface", "001"), ("materials/underlayment/", "The Underlayment", "materials_underlayment", "002"),
             ("materials/flashing-trim/", "Flashing &amp; Trim", "materials_flashing_trim", "003")]
PRINCIPLES = [("Preparation", "A roof is only as good as what&rsquo;s under it. Every deck is inspected, repaired and dried in before any surface material goes down."),
              ("Flashing", "Water finds every gap. Valleys, penetrations, step flashing, drip edge: this is where most roof failures begin."),
              ("Ventilation", "Trapped heat and moisture destroy roofs from the inside. Intake and exhaust are worked out before the first shingle is laid."),
              ("Layering", "Ice-and-water shield, synthetic underlayment, proper overlap: the layers that are invisible once we&rsquo;re done matter most."),
              ("Precision", "Nail placement, exposure, alignment. A roof installed by hand deserves hand-level attention. Every course is checked."),
              ("Clean site", "The job isn&rsquo;t done until your property looks like we were never there. Materials staged, debris removed.")]
STEPS = [("Inspection", "Free, thorough, documented. We get on the roof and into the attic, photograph what we find and walk you through it."),
         ("Estimate", "A written scope with system options and real numbers. No pressure, and no expiring &ldquo;today only&rdquo; pricing."),
         ("Materials", "Your system, color and components confirmed, then ordered and staged so install day starts at the deck."),
         ("Installation", "Most residential roofs take one to two days. Deck first, then every layer in order, every course checked."),
         ("Walkthrough", "We inspect the finished roof together: flashing, ridge lines, cleanup, the magnetic nail sweep."),
         ("Warranty", "A manufacturer warranty on the system and a workmanship warranty on the install, both in writing and explained.")]


def xmig(key, skip=()):
    s = migrate(HERE, key, DOMAIN, DROP, skip_heads=skip)
    s = re.sub(r"<(h2|h3)>(.*?)</\1>", lambda m: f"<{m.group(1)}>{re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(2))).strip()}</{m.group(1)}>", s, flags=re.S)
    out = []
    for blk in re.findall(r"<(h2|h3|p|ul|ol|blockquote)>.*?</\1>", s, re.S):
        pass
    for m in re.finditer(r"<(h2|h3|p|ul|ol|blockquote)>(.*?)</\1>", s, re.S):
        tag, inner = m.group(1), m.group(2)
        txt = re.sub(r"<[^>]+>", " ", inner); txt = re.sub(r"\s+", " ", txt).strip()
        if tag in ("h2", "h3") and STOPS.search(txt): break
        if tag == "p" and (re.fullmatch(r"[\d\s/.\-]+", txt) or (len(txt.split()) < 14 and not re.search(r"[.!?:]\s*$", txt))): continue
        if tag == "p" and re.search(r"—\s*[A-Z][a-z]+(?: [A-Z][a-z]+)?, UT\b", txt): continue
        out.append(m.group(0))
    s = "\n".join(out)
    s = re.sub(r'href="/([^"#?]*)"', lambda m: f'href="@/{m.group(1)}/"' if m.group(1) else 'href="@/"', s)
    return s.replace('href="@//"', 'href="@/"')


def header():
    svc = "".join(f'<a href="@/{p}">{n}</a>' for p, n, *_ in SERVICES)
    sysn = "".join(f'<a href="@/{p}"><span class="mono">No. {i + 1:02d}</span>{n}</a>' for i, (p, n, *_ ) in enumerate(SYSTEMS))
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{LOGO}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Systems</summary><div class="drop">{sysn}<a href="@/systems/"><span class="mono">&rarr;</span>The Collection</a></div></details></li>
<li><details><summary>Services</summary><div class="drop">{svc}<a href="@/services/">All services</a></div></details></li>
<li><a href="@/materials/">Materials</a></li><li><a href="@/process/">Process</a></li><li><a href="@/locations/">Locations</a></li><li><a href="@/about/">About</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Systems</p><div class="sub">{sysn}</div><p class="mh">Services</p><div class="sub">{svc}</div>
<a href="@/materials/">Materials</a><a href="@/process/">Process</a><a href="@/locations/">Locations</a><a href="@/about/">About</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call or text {S["phone"]}</a></div></details>
</div></header>'''


def hours():
    return "".join(f"<li><span>{d}</span><b>{t}</b></li>" for d, t in S["hours"])


def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Roofs built to last.<br><em>Service built on trust.</em></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a></div></div>
<div class="foot">
<div>{LOGO}<p>A family-run roofing contractor in Midvale, Utah, serving the Salt Lake Valley since {S["since"]}.</p><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div><h3>The Collection</h3><ul>{"".join(f'<li><a href="@/{p}">{n}</a></li>' for p, n, *_ in SYSTEMS)}</ul></div>
<div><h3>Services</h3><ul>{"".join(f'<li><a href="@/{p}">{n}</a></li>' for p, n, *_ in SERVICES)}</ul></div>
<div><h3>Locations</h3><ul class="cols">{"".join(f'<li><a href="@/{p}">{c}</a></li>' for c, p in CITIES)}</ul><ul class="hrs">{hours()}</ul></div>
</div><div class="fbottom"><span>&copy; 2026 {NAME} &middot; Midvale, Utah</span><span><a href="@/privacy/">Privacy</a> &middot; <a href="@/terms/">Terms</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call or text</a><a href="@/{CONTACT}">Free Estimate</a></div>'''


def cta(title="Start with an inspection.", text="We&rsquo;ll get on the roof, photograph every layer that matters, and walk you through what we find. Free, across the Salt Lake Valley.", photo=False):
    ph = '<div class="cta-ph" data-par="0.1"><img src="@img/xp-emigration.webp" alt="" width="1800" height="1162" loading="lazy"></div>' if photo else ""
    return f'''<section class="cta{" has-ph" if photo else ""}">{ph}<div class="wrap"><div class="reveal"><p class="label">Free estimate</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-side reveal"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call or text</small><b>{S["phone"]}</b></a><a class="btn" href="@/{CONTACT}">Request a Free Estimate {ARROW}</a><ul class="hrs">{hours()}</ul></div></div></section>'''


def phero(trail, h1, lede, label, art=None, buttons=True):
    btn = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{label}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div>{f'<div class="ph-art">{art}</div>' if art else ""}</div></section>'''


def quote_form(title="Request my free estimate"):
    opts = "".join(f"<option>{html.unescape(n)}</option>" for p, n, *_ in SERVICES)
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label><label for="f-zip">ZIP code *<input id="f-zip" name="zip" inputmode="numeric" autocomplete="postal-code" required></label></div>
<label for="f-need">What do you need? *<select id="f-need" name="need" required><option value="">Choose a service&hellip;</option>{opts}<option>Not sure yet</option></select></label>
<label for="f-msg">Tell us about the project<textarea id="f-msg" name="message"></textarea></label>
<label class="chk"><input type="checkbox" name="sms"> It&rsquo;s OK to text me about my estimate request. Message and data rates may apply; reply STOP to opt out.</label>
<button class="btn" type="submit">Request My Free Estimate {ARROW}</button></form>'''


def chips(names, cols):
    return '<ul class="chips">' + "".join(f'<li><i style="background:{c}"></i>{n}</li>' for n, c in zip(names, cols)) + "</ul>"


def selector():
    tabs = "".join(f'<button type="button" class="tab{" on" if i == 0 else ""}" data-t="{i}" aria-pressed="{"true" if i == 0 else "false"}"><span class="mono">No. {i + 1:02d}</span>{n}</button>' for i, (p, n, *_ ) in enumerate(SYSTEMS))
    panes = ""
    for i, (p, n, typ, k, mat, tier, pal, cols, key) in enumerate(SYSTEMS):
        panes += f'''<div class="pane{" on" if i == 0 else ""}" data-p="{i}"><div class="pv">{profile(k)}</div>
<div class="spec"><p class="mono">System No. {i + 1:02d} &middot; A signature system</p><h3>{n}</h3><p class="typ">{typ}</p>
<dl><div><dt>Material</dt><dd>{mat}</dd></div><div><dt>Tier</dt><dd>{tier}</dd></div></dl>
<p class="mono small">Available palette</p>{chips(pal, cols)}<a class="tlink" href="@/{p}">Explore {n} {ARROW}</a></div></div>'''
    return f'<div class="sel reveal"><div class="tabs" role="group" aria-label="Signature systems">{tabs}</div><div class="panes">{panes}</div></div>'


HOME_FAQ = [("Is the roof inspection free?", "Yes. The inspection is free, the photos are yours to keep either way, and the estimate arrives in writing."),
            ("Do you help with storm damage and insurance?", "If the inspection turns up hail or wind damage, we record it the way insurance claims require: dated photos, measurements and a written scope. The claim is yours to file; the documentation comes from us."),
            ("How long does a new roof take?", "Most residential roofs take one to two days. The deck is repaired and dried in first, then every layer goes down in order."),
            ("Can you re-roof under solar panels?", "Yes. A solar detach and reset removes the panels and racking, rebuilds the roof, flashes the mounts into the new roof and reinstalls the array, coordinated with your solar installer."),
            ("Where do you work?", "From our shop in Midvale, across the Salt Lake Valley: " + ", ".join(c for c, _ in CITIES) + ".")]


def home():
    plates = "".join(f'<li class="reveal"><span class="pn">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(PRINCIPLES))
    steps = "".join(f'<li class="reveal"><span class="mono">Step {i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))
    svc = "".join(f'<a class="svc reveal" href="@/{p}"><span class="mono">S-{i + 1:02d}</span><b>{n}</b><i>{ARROW}</i></a>' for i, (p, n, *_ ) in enumerate(SERVICES))
    loc = "".join(f'<a href="@/{p}">{c}</a>' for c, p in CITIES)
    body = f'''
<section class="xh"><div class="xh-in">
<div class="xh-text wrap-l"><p class="label">Xperience Roofing &middot; Midvale, Utah &middot; Edition 02</p>
<h1 class="xh-h1"><span class="ln"><span>Midvale&rsquo;s</span></span><span class="ln"><span>roofing company,</span></span><span class="ln"><em>built to last.</em></span></h1>
<p class="lede">Xperience Roofing is a family-run roofing company in Midvale, serving the Salt Lake Valley since {S["since"]}: replacement, repair, inspections and commercial roofing, installed as a complete system and built for Utah snow, wind and sun.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<ul class="facts"><li><b>4.9&#9733;</b><span>average rating</span></li><li><b>{S["since"]}</b><span>serving the valley since</span></li><li><b>Free</b><span>inspections</span></li><li><b>Licensed</b><span>&amp; insured</span></li></ul></div>
<figure class="xh-ph"><img src="@img/xp-lone-peak.webp" alt="Lone Peak in the Wasatch Range under winter snow" width="1200" height="1389" fetchpriority="high" data-par="0.08"><figcaption class="mono">Lone Peak, Wasatch Range &middot; the weather every Salt Lake Valley roof answers to</figcaption>
<div class="xh-plate">{profile("standing")}<span class="mono">Plate 02 &middot; The Standing Seam</span></div></figure>
</div></section>

<section class="xpano"><div class="xpano-img" data-par="0.12"><img src="@img/xp-wasatch-pano.webp" alt="The snow-covered Wasatch Mountains seen from the Salt Lake Valley" width="2400" height="565" loading="lazy"></div>
<div class="wrap xpano-in"><p class="xpano-q reveal">Built for Utah <em>snow, wind and sun.</em></p></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Roofing systems &middot; Five signature systems</p><h2>The Collection.</h2><p class="lede">Not every home calls for the same roof. Climate, architecture, budget and how long you plan to stay all shape the answer. These are the five systems we install as roofers in Midvale and across the valley.</p></div>
{selector()}
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label">How we build &middot; Six principles</p><h2>The Installer&rsquo;s <em>Standard.</em></h2><p class="lede">Every roof we install is held to the same six principles: the parts of the job you&rsquo;ll never see, done as carefully as the parts you will.</p></div>
<ol class="plates">{plates}</ol>
</div></section>

<section class="sec mat-sec"><div class="wrap split">
<div class="reveal"><p class="label">Material World</p><h2>What goes <em>into a roof.</em></h2>
<p>Three layers decide how a roof ages: the surface you see, the underlayment you don&rsquo;t, and the flashing and trim where water tries hardest to get in.</p>
<ul class="mlist">{"".join(f'<li><a href="@/{p}"><span class="mono">XP-MAT-{c}</span>{n}<i>{ARROW}</i></a></li>' for p, n, k, c in MATERIALS)}</ul></div>
<figure class="reveal">{stack()}</figure>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Our process &middot; Six steps</p><h2>From the first photograph <em>to the warranty in your hand.</em></h2></div>
<ol class="steps">{steps}</ol>
<p class="more reveal"><a class="tlink" href="@/process/">The full process {ARROW}</a></p>
</div></section>

<section class="sec paper"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Services</p><h2>Roofers in Midvale, <em>for the whole valley.</em></h2><div class="svcs">{svc}</div>
<p class="label" style="margin-top:44px">Locations</p><div class="locs">{loc}</div></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before <em>you call.</em></h2>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="mono">From the journal</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(HOME_FAQ)}</div></div></section>
<div class="wrap"><p class="xcredit">Landscape photographs, for atmosphere only (not Xperience Roofing jobs): &ldquo;Lone Peak Summit in the Winter&rdquo; by Derrellwilliams, <a href="https://commons.wikimedia.org/wiki/File:Lone_Peak_Summit_in_the_Winter.jpg" rel="noopener">CC BY-SA 4.0</a>; &ldquo;Wasatch Mountains SLV pano4&rdquo; by Leon7, <a href="https://commons.wikimedia.org/wiki/File:Wasatch_Mountains_SLV_pano4.jpg" rel="noopener">CC BY-SA 3.0</a>; &ldquo;Wasatch Range from Emigration Canyon&rdquo; by Kepler Sticka-Jones, <a href="https://commons.wikimedia.org/wiki/File:Wasatch_Range_from_Emigration_Canyon.jpg" rel="noopener">CC BY-SA 4.0</a>. All via Wikimedia Commons; graded for this page.</p></div>
''' + cta(photo=True)
    return {"path": "", "canonical": U.rstrip("/"), "title": "Roofing Company Midvale, UT | Xperience Roofing",
            "meta": "Xperience Roofing is a family-run roofing company in Midvale, Utah: roof replacement, repair, inspections and commercial roofing across the Salt Lake Valley.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def page(path, key, title, meta, h1, label, intro, trail, art=None, side=True, extra=""):
    sideh = f'''<aside class="sv-side"><div class="side-card"><p class="label">Free estimate</p><h3>Talk to the Midvale office</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a><ul class="hrs">{hours()}</ul></div>
<div class="side-rel"><p class="label">The Collection</p><ul>{"".join(f'<li><a href="@/{p}"><span class="mono">No. {i + 1:02d}</span>{n}</a></li>' for i, (p, n, *_ ) in enumerate(SYSTEMS))}</ul></div></aside>''' if side else ""
    body = phero(trail, h1, None, label, art) + f'''
<section class="sec"><div class="wrap {"sv-grid" if side else ""}"><article class="prose">{f'<p class="answer">{intro}</p>' if intro else ""}{extra}
{xmig(key, skip=(html.unescape(h1),))}
</article>{sideh}</div></section>''' + (cta() if side else "")
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "schema": [crumbs_ld(path, trail)]}


def all_pages():
    P = [home()]
    P.append(page("about/", "about", "About Xperience Roofing | Family-Run Roofers in Midvale, UT",
                  "Xperience Roofing is a family-run roofing contractor in Midvale, Utah, serving the Salt Lake Valley since 2019. Quality over volume, documented work, clean sites.",
                  "About Xperience Roofing, Midvale", "About &middot; Built on trust", f"Xperience Roofing is a family-run roofing contractor based in Midvale, Utah, installing, repairing and inspecting roofs across the Salt Lake Valley since {S['since']}.", [HOME, ("About", "about/")]))
    P.append(page("services/", "services", "Roofing Services in Midvale, UT | Xperience Roofing",
                  "Roofing services in Midvale and the Salt Lake Valley: roof replacement, repair, inspections, commercial roofing, metal roofing and solar detach and reset.",
                  "Roofing Services in Midvale, UT", "Services", "Xperience Roofing provides roof replacement, roof repair, roof inspections, commercial roofing, metal roofing and solar detach and reset in Midvale and across the Salt Lake Valley.", [HOME, ("Services", "services/")],
                  extra='<div class="svcs wide">' + "".join(f'<a class="svc" href="@/{p}"><span class="mono">S-{i + 1:02d}</span><b>{n}</b><i>{ARROW}</i></a>' for i, (p, n, *_ ) in enumerate(SERVICES)) + "</div>"))
    ART = {"services_roof_replacement": "classic", "services_roof_repair": "classic", "services_roof_inspections": "summit", "services_commercial_roofing": "flat", "services_metal_roofing": "standing", "services_solar_detach_reset": "standing"}
    for p, n, key, kw in SERVICES:
        P.append(page(p, key, f"{html.unescape(n)} in Midvale, UT | Xperience Roofing",
                      f"{html.unescape(n)} in Midvale and across the Salt Lake Valley from Xperience Roofing, a family-run contractor. Free inspection and a written estimate.",
                      f"{n} in Midvale, UT", "Service", f"Xperience Roofing provides {kw} in Midvale and across the Salt Lake Valley, from our shop on State Street. Every job starts with a free, documented inspection and a written estimate.",
                      [HOME, ("Services", "services/"), (n, p)], art=profile(ART[key])))
    P.append(page("systems/", "systems", "Roofing Systems in Midvale: The Collection | Xperience",
                  "The five signature roofing systems Xperience Roofing installs in Midvale and the Salt Lake Valley: shingle, standing seam, tile, metal shake and low-slope.",
                  "The Collection: Five Signature Roofing Systems", "Roofing systems", "Not every home calls for the same roof. Climate, architecture, budget and what you want your house to feel like from the street all shape the right choice. These are the five systems we build most often across the Salt Lake Valley.",
                  [HOME, ("Systems", "systems/")], side=False, extra=selector()))
    for i, (p, n, typ, k, mat, tier, pal, cols, key) in enumerate(SYSTEMS):
        spec = f'<div class="spec-card"><dl><div><dt>System</dt><dd>{typ}</dd></div><div><dt>Material</dt><dd>{mat}</dd></div><div><dt>Tier</dt><dd>{tier}</dd></div></dl><p class="mono small">Available palette</p>{chips(pal, cols)}</div>'
        t = f"{html.unescape(n)}: {html.unescape(typ)} | Xperience Roofing"
        if len(t) > 60: t = f"{html.unescape(n)}: {html.unescape(typ)} | Xperience"
        if len(t) > 60: t = f"{html.unescape(n)} | Low-Slope & Commercial | Xperience"
        P.append(page(p, key, t,
                      f"{html.unescape(n)}, a signature roofing system from Xperience Roofing in Midvale, Utah: {html.unescape(typ).lower()}, its materials and palette.",
                      f"{n}: {typ}", f"System No. {i + 1:02d}", None, [HOME, ("Systems", "systems/"), (n, p)], art=profile(k), extra=spec))
    P.append(page("materials/", "materials", "Material World: What Goes Into a Roof | Xperience Roofing",
                  "Material World from Xperience Roofing in Midvale: the surface, the underlayment and the flashing and trim that decide how a Utah roof ages over the years.",
                  "Material World: What Goes Into a Roof", "Materials", None, [HOME, ("Materials", "materials/")], art=stack()))
    for p, n, key, c in MATERIALS:
        P.append(page(p, key, f"{html.unescape(n)}: Material World | Xperience Roofing",
                      f"{html.unescape(n)} in Material World from Xperience Roofing, Midvale: what this layer of a roof does and how we specify it for Utah winters and summers.",
                      f"{n}", f"Material World &middot; XP-MAT-{c}", None, [HOME, ("Materials", "materials/"), (n, p)]))
    P.append(page("process/", "process", "Our Roofing Process: Six Steps | Xperience Roofing, Midvale",
                  "The Xperience Roofing process in Midvale: inspection, written estimate, materials, installation, walkthrough and warranty. Six steps, the same on every roof.",
                  "Our Process: Six Steps from Inspection to Warranty", "Process", "Six steps, the same on every roof, from the first photograph on the deck to the warranty in your hand. Documented, unhurried, and checked at every stage.", [HOME, ("Process", "process/")]))
    P.append(page("locations/", "locations", "Roofing Service Area: Salt Lake Valley | Xperience Roofing",
                  "Xperience Roofing serves the Salt Lake Valley from Midvale: Sandy, Draper, Murray, South Jordan, West Jordan, Riverton, Holladay, Cottonwood Heights and SLC.",
                  "Roofing Across the Salt Lake Valley", "Service area", None, [HOME, ("Locations", "locations/")],
                  extra='<div class="locs big">' + "".join(f'<a href="@/{p}">{c}</a>' for c, p in CITIES) + "</div>"))
    for c, p in CITIES:
        key = "locations_" + p.split("/")[1].replace("-", "_")
        P.append(page(p, key, max([t for t in (f"Roofing in {c}, UT | Roof Repair & Replacement | Xperience", f"Roofing in {c}, UT | Roof Replacement & Repair", f"Roofing in {c}, UT | Xperience Roofing, Midvale", f"Roofing in {c}, UT | Xperience Roofing") if len(t) <= 60], key=len),
                      f"Roofing in {c}, UT from Xperience Roofing, a family-run Midvale contractor: roof replacement, repair and free roof inspections.",
                      f"Roofing in {c}, UT", f"Locations &middot; {c}", None, [HOME, ("Locations", "locations/"), (c, p)]))
    for p, key, t, m, h in [("privacy/", "privacy", "Privacy Policy | Xperience Roofing, Midvale, Utah", "Privacy policy for xperienceroofing.com: what information Xperience Roofing collects through this website and estimate forms, and how it is used and protected.", "Privacy Policy"),
                            ("terms/", "terms", "Terms & Conditions | Xperience Roofing, Midvale, Utah", "Terms and conditions for using xperienceroofing.com and requesting estimates from Xperience Roofing, a family-run roofing contractor in Midvale, Utah.", "Terms &amp; Conditions")]:
        P.append(page(p, key, t, m, h, "Legal", None, [HOME, (h, p)], side=False))
    P.append(contact())
    P += p_blog.pages()
    P.append({"path": "404.html", "title": "Page Not Found | Xperience Roofing", "meta": "This page could not be found. Browse the Xperience Roofing collection of roofing systems and services in Midvale, Utah, or call (385) 402-6364.",
              "body": phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t in the collection.", "Try a system below, or call us.", "404") + f'<section class="sec"><div class="wrap">{selector()}</div></section>', "robots": "noindex, follow", "sitemap": False})
    return P


def contact():
    trail = [HOME, ("Contact", CONTACT)]
    body = phero(trail, "Contact Xperience Roofing in Midvale", "Tell us about your roof and we&rsquo;ll set up a free inspection and a written estimate. No cost, no pressure.", "Contact &middot; Free inspection", buttons=False) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><dl class="info">
<div><dt>Call or text</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div>
<div><dt>Office</dt><dd>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}<br><small>Just off State Street.</small></dd></div>
<div><dt>Hours</dt><dd><ul class="hrs">{hours()}</ul></dd></div>
<div><dt>Service area</dt><dd><div class="locs">{"".join(f'<a href="@/{p}">{c}</a>' for c, p in CITIES)}</div></dd></div></dl>
<h2 class="nx">What happens next</h2><ol class="steps three"><li><span class="mono">01</span><h3>We call you back</h3><p>A real person from our Midvale office reaches out within business hours.</p></li><li><span class="mono">02</span><h3>We schedule an inspection</h3><p>We come look at the roof in person. The inspection is free.</p></li><li><span class="mono">03</span><h3>You get a written estimate</h3><p>Clear line items, real options and time to decide.</p></li></ol></div>
<div class="reveal">{quote_form("Start your estimate")}</div></div></section>'''
    return {"path": CONTACT, "canonical": canon(CONTACT), "title": "Contact Xperience Roofing | Free Roof Inspection, Midvale",
            "meta": "Contact Xperience Roofing in Midvale: call or text (385) 402-6364, email, or request a free roof inspection and written estimate. 8034 S State St Suite B.",
            "body": body, "schema": [crumbs_ld(CONTACT, trail), {"@type": "ContactPage", "@id": canon(CONTACT) + "#page", "url": canon(CONTACT)}]}


def _fit(pg):
    for add in (" Free inspections.", " Call (385) 402-6364.", " Serving the Salt Lake Valley.", " Midvale, Utah."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def make_pages():
    p_blog.setup(phero, cta, ARROW, HOME, CONTACT)
    return [_fit(x) for x in all_pages()]
