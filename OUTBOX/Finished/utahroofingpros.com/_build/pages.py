"""Pages for the utahroofingpros.com redesign: "sun over the ridge".

The client's logo is a sun rising behind a roof ridge, and most of their own job photos have the Wasatch behind the roof. So the
site works in that one image: arched (half-sun) photo frames, a horizon line under each section head, the navy and sun yellow of
the logo, and a real detail only this company has: their 52 service-area cities plotted on a map, in the five regions they use,
with the Cottonwood Heights office marked. Home targets "roofing company cottonwood heights" (report, 17 Oct 2026); every
service page names Cottonwood Heights in its title, H1 and opening paragraph. City pages keep the client's own local text.
Left out (see notes): "GAF Certified" and "Owens Corning Preferred" badges, "Up to 50-Year" and "Lifetime" warranty lines,
"85+ verified 5-star reviews", "12 months no payments / no interest", "over a decade of combined experience", "trusted by major
commercial clients", "24/7", the AI-generated city photos and mock-ups, and the test-homepagedesign page.
"""
import html, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, U, HERE, DOMAIN, REGIONS, FOUNDED
from migrate import migrate
from illus import map_svg, sun
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CONTACT = "contact-us/"
INSPECT = "get-started/schedule-free-roof-inspection/"
HOME = ("Home", "")
DROP = re.compile(r"GAF|Owens|50-Year|Lifetime|12 months|No Payments|No Interest|No Upfront|85\+|decade|major commercial|24/7|guarantee|\bthe best\b(?! (?:option|next|long|way|fit|solution|choice))|best roof|fight|same-day|"
                  r"top-rated|most trusted|top-tier|top-grade|certified expert|within minutes|exceed expectations|Utah.s trusted", re.I)
NODROP = re.compile(r"(?!x)x")
CTA_P = re.compile(r"^(Get|Schedule|Book|Call|Contact|Connect|Talk|Learn|Explore|Request|Ask|See|View|Find|Start|Let.s Talk|Submit)\b[^.]{0,48}!?$", re.I)
CITIES = [(slug, name, ri, reg) for ri, (reg, cs) in enumerate(REGIONS) for slug, name, *_ in cs]
POOL = ["shingle-ridge-wasatch", "aerial-new-roof-foothills", "new-roof-mountain-view", "roof-vents-mountains", "aerial-white-house", "red-shingle-roof-mountains",
        "roof-wood-siding-aerial", "dormer-roof-aerial", "aerial-roof-fall-trees", "aerial-tudor-home-roof", "ridge-cap-city", "garage-roof-new"]
ALT = {"shingle-ridge-wasatch": "New shingle roof with a chimney and the Wasatch Mountains behind", "aerial-new-roof-foothills": "Aerial view of new shingle roofs below the foothills",
       "new-roof-mountain-view": "Finished gray shingle roof with mountains in the distance", "roof-vents-mountains": "Shingle roof with roof vents and snow-capped mountains",
       "aerial-white-house": "Aerial view of a white house with a new dark roof", "red-shingle-roof-mountains": "Red shingle roof on a home with mountains behind",
       "roof-wood-siding-aerial": "Aerial view of a new roof on a home with wood siding", "dormer-roof-aerial": "Aerial view of a dormer on a finished roof",
       "aerial-roof-fall-trees": "Aerial view of a red-brown shingle roof among fall trees", "aerial-tudor-home-roof": "Aerial view of a Tudor-style home with a new shingle roof",
       "ridge-cap-city": "New ridge cap on a shingle roof in the city", "garage-roof-new": "New roof over a garage"}


def tidy(s):
    out = []
    for blk in re.findall(r"<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s, re.S):
        txt = html.unescape(re.sub(r"<[^>]+>", "", blk)).strip()
        if blk.startswith("<p>") and CTA_P.match(txt): continue
        blk = re.sub(r"\s*[→↓]\s*", " ", blk).replace(" </a>", "</a>").replace(" </h3>", "</h3>")
        blk = re.sub(r"✓\s*", "", blk).replace("⭐", "")
        blk = re.sub(r"<strong>\s*</strong>", "", blk)
        out.append(blk)
    out = [b for i, b in enumerate(out) if not (b.startswith("<h3>") and i + 1 < len(out) and out[i + 1].startswith("<h2>"))]
    return "\n".join(out)


def mig(key, skip=(), drop=DROP):
    return tidy(migrate(HERE, key, DOMAIN, drop, skip_heads=skip))


# key, path, label, group, image, title, meta, h1, intro
SVC = [
    ("services_residential_roofing_roof_repair", "services/residential-roofing/roof-repair/", "Roof Repair", "Residential", "roofer-on-roof",
     "Roof Repair in Cottonwood Heights, UT | Utah Roofing Pros",
     "Roof repair in Cottonwood Heights for leaks, missing shingles, flashing and storm damage. Family-owned Utah Roofing Pros. Free inspection: (801) 688-3853.",
     "Roof Repair in Cottonwood Heights", "Utah Roofing Pros handles roof repair in Cottonwood Heights and across the Salt Lake Valley: leaks, damaged or missing shingles, pipe flashing, seams and skylights. We inspect first, give you a written scope, and fix the cause, so a small problem doesn&rsquo;t turn into a large one."),
    ("services_residential_roofing_roof_replacement", "services/residential-roofing/roof-replacement/", "Roof Replacement", "Residential", "tear-off-in-progress",
     "Roof Replacement in Cottonwood Heights | Utah Roofing Pros",
     "Roof replacement in Cottonwood Heights: tear-off, deck check, underlayment and a new shingle or metal roof, installed cleanly by a family-owned local team.",
     "Roof Replacement in Cottonwood Heights", "When repairs no longer make sense, Utah Roofing Pros replaces roofs in Cottonwood Heights and the surrounding cities: we tear off the old roof, check the deck, and install a new system, guiding you through materials and colors along the way."),
    ("services_residential_roofing_asphalt_shingle_roofing", "services/residential-roofing/asphalt-shingle-roofing/", "Asphalt Shingle Roofing", "Residential", "roofer-nailing-shingles",
     "Asphalt Shingle Roofing in Cottonwood Heights, Utah",
     "Asphalt shingle roofing in Cottonwood Heights: new shingle roofs installed, replaced and repaired by Utah Roofing Pros, with colors and styles for Utah homes.",
     "Asphalt Shingle Roofing in Cottonwood Heights", "Asphalt shingles are the most common roof on homes in Cottonwood Heights and across the Wasatch Front. Utah Roofing Pros installs, replaces and repairs shingle roofs, and helps you choose a style and color that suits the house."),
    ("services_residential_roofing_storm_damage_repair", "services/residential-roofing/storm-damage-repair/", "Storm Damage Repair", "Residential", "hail-damaged-shake-roof",
     "Storm Damage Roof Repair in Cottonwood Heights, UT",
     "Storm damage roof repair in Cottonwood Heights: hail, wind and snow damage inspected, documented with photos and repaired, with help on your insurance claim.",
     "Storm Damage Roof Repair in Cottonwood Heights", "After hail, wind or heavy snow, Utah Roofing Pros inspects roofs in Cottonwood Heights and nearby cities, documents the damage with photos, and repairs it. If you file an insurance claim, we help with the paperwork and meet your adjuster."),
    ("services_residential_roofing_swamp_cooler_removal_roof_repair", "services/residential-roofing/swamp-cooler-removal-roof-repair/", "Swamp Cooler Removal", "Residential", "ladder-brick-home",
     "Swamp Cooler Removal &amp; Roof Repair | Cottonwood Heights",
     "Swamp cooler removal and roof repair in Cottonwood Heights: we take the old unit off, repair and seal the opening, and match the patch to your existing roof.",
     "Swamp Cooler Removal &amp; Roof Repair in Cottonwood Heights", "Utah Roofing Pros removes old roof-mounted swamp coolers in Cottonwood Heights and across the valley, then repairs, seals and reinforces the opening with materials that match the rest of the roof."),
    ("services_residential_roofing", "services/residential-roofing/", "Residential Roofing", "Residential", "aerial-tudor-home-roof",
     "Residential Roofing, Cottonwood Heights | Utah Roofing Pros",
     "Residential roofing in Cottonwood Heights: roof repair, replacement, shingle roofs, storm damage and swamp cooler removal from a family-owned local company.",
     "Residential Roofing in Cottonwood Heights", "Utah Roofing Pros is a family-owned residential roofing company in Cottonwood Heights. We repair and replace home roofs across the Salt Lake Valley, Davis and Weber counties, Utah County and the Wasatch Back, starting with a free inspection."),
    ("services_commercial_roofing", "services/commercial-roofing/", "Commercial Roofing", "Commercial", "saint-anns-flat-roof",
     "Commercial Roofing in Cottonwood Heights | Utah Roofing Pros",
     "Commercial roofing in Cottonwood Heights: TPO membrane and asphalt shingle roofs for offices, retail and other buildings, installed, replaced and repaired.",
     "Commercial Roofing in Cottonwood Heights", "Utah Roofing Pros handles commercial roofing in Cottonwood Heights and across northern Utah: TPO membrane on flat and low-slope roofs, asphalt shingles on pitched commercial buildings, repairs and full replacements, planned to keep your business running."),
    ("services_commercial_roofing_tpo_membrane_roofing", "services/commercial-roofing/tpo-membrane-roofing/", "TPO Membrane Roofing", "Commercial", "flat-roofs-aerial",
     "TPO Roofing in Cottonwood Heights, UT | Utah Roofing Pros",
     "TPO membrane roofing in Cottonwood Heights for flat and low-slope commercial roofs: new installs, re-roofs and repairs by Utah Roofing Pros. Free inspection.",
     "TPO Membrane Roofing in Cottonwood Heights", "Utah Roofing Pros installs and repairs TPO membrane roofs on flat and low-slope commercial buildings in Cottonwood Heights and across the Wasatch Front. TPO is a single-ply white membrane that reflects sunlight and is heat-welded at the seams."),
    ("services_commercial_roofing_commercial_asphalt_shingle_roofing", "services/commercial-roofing/commercial-asphalt-shingle-roofing/", "Commercial Shingle Roofing", "Commercial", "ridge-cap-city",
     "Commercial Asphalt Shingle Roofing in Cottonwood Heights",
     "Commercial asphalt shingle roofing in Cottonwood Heights for offices, churches, multi-family and other pitched-roof buildings, installed by Utah Roofing Pros.",
     "Commercial Asphalt Shingle Roofing in Cottonwood Heights", "Many commercial and multi-family buildings in Cottonwood Heights have pitched roofs. Utah Roofing Pros installs, replaces and repairs asphalt shingle roofs on them, scheduled around the people who use the building."),
]
RES = [r for r in SVC if r[3] == "Residential"]
COM = [r for r in SVC if r[3] == "Commercial"]
GET = [("Free roof inspection", INSPECT), ("Instant estimate", "get-started/instant-roofing-estimate/"), ("Insurance claims", "roof-insurance-claim/"), ("Financing options", "roof-financing/")]


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def _drop(items):
    return "".join(f'<a href="@/{p}">{lab}</a>' for lab, p in items)


def header():
    return Q(_header())


def _header():
    res = _drop([(r[2], r[1]) for r in RES[:-1]] + [("All residential", RES[-1][1])])
    com = _drop([(r[2], r[1]) for r in COM[1:]] + [("All commercial", COM[0][1])])
    reg = _drop([(f"{r} <small>{len(cs)}</small>", f"service-areas/#{re.sub(r'[^a-z]+', '-', r.lower()).strip('-')}") for r, cs in REGIONS] + [("All 52 cities", "service-areas/")])
    get = _drop(GET + [("Start here", "get-started/")])
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("utah-roofing-pros-logo", NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Residential</summary><div class="drop">{res}</div></details></li>
<li><details><summary>Commercial</summary><div class="drop">{com}</div></details></li>
<li><details><summary>Service areas</summary><div class="drop">{reg}</div></details></li>
<li><details><summary>Get started</summary><div class="drop">{get}</div></details></li>
<li><a href="@/about-us/">About</a></li><li><a href="@/our-roofing-projects/">Projects</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{PHONE}<span>{S["phone"]}</span></a><a class="btn" href="@/{INSPECT}">Free Inspection</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Residential</p><div class="sub">{res}</div><p class="mh">Commercial</p><div class="sub">{com}</div>
<p class="mh">Get started</p><div class="sub">{get}</div>
<a href="@/service-areas/">Service areas</a><a href="@/about-us/">About</a><a href="@/our-roofing-projects/">Projects</a><a href="@/blog/">Blog</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>'''


def footer():
    return Q(_footer())


def _footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Family-owned in Cottonwood Heights<br><span>since {FOUNDED}.</span></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{INSPECT}">Book a Free Inspection {ARROW}</a></div></div>
<div class="foot">
<div><span class="flogo">{img("utah-roofing-pros-logo", NAME + " logo")}</span><p>Residential and commercial roofing, roof repair and replacement, storm damage and insurance claim help, founded by John and Phil Panos.</p></div>
<div><h3>Residential</h3><ul>{"".join(f'<li><a href="@/{r[1]}">{r[2]}</a></li>' for r in RES)}</ul></div>
<div><h3>Commercial &amp; more</h3><ul>{"".join(f'<li><a href="@/{r[1]}">{r[2]}</a></li>' for r in COM)}{"".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in GET)}<li><a href="@/blog/">Blog</a></li></ul></div>
<div><h3>Office</h3><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p><p class="mono coords">40.62&deg; N &middot; 111.81&deg; W</p></div>
</div>
<div class="fareas">{"".join(f'<p><b>{r}</b> {" &middot; ".join(f"<a href=@/service-areas/{s}/>{n}</a>" for s, n, *_ in cs)}</p>' for r, cs in REGIONS)}</div>
<div class="fbottom"><span>&copy; 2026 {NAME}</span><span><a href="@/legal/privacy-policy/">Privacy</a> &middot; <a href="@/legal/terms-and-conditions/">Terms</a> &middot; <a href="@/legal/cookie-policy/">Cookies</a> &middot; <a href="@/legal/">Legal</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{INSPECT}">Free Inspection</a></div>'''


def cta(title="Get clear answers about your roof.", text="Book a free inspection. We&rsquo;ll look at the roof, show you what we find, and explain your options before you decide anything."):
    return f'''<section class="cta"><div class="wrap cta-in">
<div><p class="label">Free inspection</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call the office</small><b>{S["phone"]}</b></a><a class="btn" href="@/{INSPECT}">Book a Free Inspection {ARROW}</a></div></div>
{sun("csun")}</section>'''


def phero(trail, h1, lede, tag, image=None, alt="", buttons=True):
    art = f'<figure class="ph-arch">{img(image, alt, priority=True)}</figure>' if image else ""
    btn = f'<div class="btn-row"><a class="btn" href="@/{INSPECT}">Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div>{art}</div></section>'''


def quote_form(title="Book a free inspection"):
    opts = "".join(f"<option>{r[2]}</option>" for r in SVC)
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-first">First name *<input id="f-first" name="first_name" autocomplete="given-name" required></label><label for="f-last">Last name<input id="f-last" name="last_name" autocomplete="family-name"></label></div>
<div class="row"><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label></div>
<label for="f-addr">Street address, city<input id="f-addr" name="address" autocomplete="street-address"></label>
<label for="f-svc">What do you need?<select id="f-svc" name="service"><option value="">Choose one</option>{opts}<option>Insurance claim help</option><option>Something else</option></select></label>
<label for="f-msg">Message<textarea id="f-msg" name="message" placeholder="What are you seeing on the roof?"></textarea></label>
<label class="check"><input type="checkbox" name="consent" required><span>I agree to the <a href="@/legal/privacy-policy/">Privacy Policy</a> and <a href="@/legal/terms-and-conditions/">Terms</a>, and authorize Utah Roofing Pros to contact me.</span></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


def side(extra=""):
    return f'''<aside class="sv-side"><div class="side-card">{sun("ssun")}<p class="label">Free inspection</p><h3>Talk to the office</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a><p class="mono small">{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</p></div>{extra}</aside>'''


HOME_FAQ = [("Is the roof inspection really free?", "Yes. We inspect the roof, document what we find with photos, and explain your options. There&rsquo;s no charge and no pressure to decide on the spot."),
            ("Do I need a repair or a whole new roof?", "Not every roofing problem needs a replacement. A localized leak, flashing problem or damaged seam can often be repaired when the rest of the roof is in good condition. Replacement makes more sense when problems are widespread, the roof is near the end of its life, or repeated repairs stop being economical."),
            ("Do you help with roof insurance claims?", "Yes. After storm, hail or wind damage we inspect and photograph the roof, help you file, meet the adjuster, and then build or repair the roof once the claim is approved."),
            ("What causes most roof leaks?", "Usually the places where the roof is interrupted: pipe and vent flashing, chimneys, skylights, valleys and old swamp-cooler openings, plus shingles lifted or torn by wind. That&rsquo;s why we look at the whole roof, not only the wet spot on the ceiling."),
            ("Do you work on commercial buildings?", "Yes. We install and repair TPO membrane on flat and low-slope roofs and asphalt shingles on pitched commercial and multi-family buildings."),
            ("Where are you based, and how far do you travel?", f"Our office is at {S['street']}, {S['city']}, {S['st']} {S['zip']}. We work across the Salt Lake Valley, the northern Wasatch Front up to North Ogden, Utah County down to Spanish Fork, Park City, Heber City and Tooele.")]
STEPS = [("Free inspection", "We identify the damage and give you a clear overview, with photos."), ("File your claim", "We help you submit the documentation and answer insurance questions."),
         ("Meet the adjuster", "We&rsquo;re there for the adjuster visit to confirm the scope."), ("Claim approval", "Once approved, we coordinate timelines and materials."),
         ("Build or repair", "Our team gets to work: fast, clean and professional."), ("Final walkthrough", "We finalize the paperwork and walk the job with you.")]


def regid(r):
    return re.sub(r"[^a-z]+", "-", r.lower()).strip("-")


def map_block(highlight=None):
    tabs = '<button type="button" class="on" data-r="all">All 52</button>' + "".join(f'<button type="button" data-r="{i}"><i class="sw r{i}"></i>{r} <small>{len(cs)}</small></button>' for i, (r, cs) in enumerate(REGIONS))
    lists = "".join(f'<div class="reg" id="{regid(r)}" data-r="{i}"><h3><i class="sw r{i}"></i>{r}</h3><ul>{"".join(f"<li><a href=@/service-areas/{s}/>{n}</a></li>" for s, n, *_ in cs)}</ul></div>' for i, (r, cs) in enumerate(REGIONS))
    return f'''<div class="mapwrap" data-map><div class="map-fig">{map_svg(highlight)}<p class="mono small">Approximate city positions. I-15 shown for orientation.</p></div>
<div class="map-side"><div class="tabs" role="group" aria-label="Filter by region">{tabs}</div><div class="regs">{lists}</div></div></div>'''


def home():
    svc_cards = [RES[0], RES[1], RES[3], COM[0], COM[1], RES[4]]
    svc = "".join(f'<a class="svc reveal" href="@/{r[1]}"><span class="arch">{img(r[4], ALT.get(r[4], r[2]))}</span><span class="mono">{r[3]}</span><b>{r[2]}</b><em>Learn more {ARROW}</em></a>' for r in svc_cards)
    gal = [("shingle-delivery-boom", "Shingles going up by boom lift"), ("dome-boom-lift", "Working from a lift on a historic dome"), ("aerial-tudor-home-roof", "A Tudor-style home, re-roofed"),
           ("roofer-nailing-shingles", "Shingles going on, row by row"), ("flat-roofs-aerial", "Flat roofs on a brick commercial building"), ("roof-vents-mountains", "Vents and a new roof, Wasatch behind"),
           ("garage-roof-new", "A new garage roof"), ("roofer-boots-shingles", "On the roof, in work boots")]
    galh = "".join(f'<figure class="g{i} reveal">{img(n, c)}<figcaption><span class="mono">{i + 1:02d}</span>{c}</figcaption></figure>' for i, (n, c) in enumerate(gal))
    steps = "".join(f'<li class="reveal"><span class="mono">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div class="hero-text"><p class="label">Family-owned &middot; Cottonwood Heights, Utah &middot; Since {FOUNDED}</p>
<h1>The roofing company in Cottonwood Heights <span>that starts with a straight answer.</span></h1>
<p class="lede">Utah Roofing Pros is a family-owned roofing company in Cottonwood Heights, founded in {FOUNDED} by John and Phil Panos. We repair, replace and install roofs on homes and commercial buildings, help with storm damage and insurance claims, and start every job with a free inspection.</p>
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Book a Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="hero-art"><figure class="sunframe">{img("new-roof-mountain-view", "A finished gray shingle roof with the Wasatch Mountains behind", priority=True)}</figure>{sun("hsun")}</div>
</div><div class="horizon"><div class="wrap"><span class="mono">40.62&deg; N &middot; 111.81&deg; W</span><span class="mono">Office: {S["street"]}, {S["city"]}</span><span class="mono">52 cities &middot; 5 regions</span></div></div></section>

<section class="strip" aria-label="At a glance"><div class="wrap strip-in">
<span>Family-owned</span><span>Founded {FOUNDED}</span><span>Residential &amp; commercial</span><span>Free inspections</span><span>Insurance claim help</span><span>Financing available</span></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label dark">Roofers in Cottonwood Heights</p><h2>Repair, replace, <span>or neither.</span></h2>
<p class="lede">As a roofing contractor in Cottonwood Heights, we look at the roof first and tell you what it actually needs, whether that&rsquo;s a targeted repair, a new roof, or nothing yet. Already have another bid? We&rsquo;re happy to give a second opinion.</p></div>
<div class="svcs">{svc}</div>
<p class="more reveal"><a class="tlink" href="@/services/">All roofing services {ARROW}</a></p>
</div></section>

<section class="sec family"><div class="wrap split">
<figure class="fam-img reveal">{img("team-three-yellow", "The Utah Roofing Pros team in yellow company shirts, reviewing a job on a tablet")}</figure>
<div class="reveal"><p class="label dark">Where it started</p><h2>Two roofers, <span>one family name.</span></h2>
<p>Utah Roofing Pros was founded in {FOUNDED} by John and Phil Panos: a shared vision between two skilled roofers, based in Cottonwood Heights. The idea has stayed simple: craftsmanship, reliable service and personal attention on every roof, whatever its size.</p>
<p>You&rsquo;re not another job on the calendar. We treat clients like family, keep you informed, and approach every roof like it&rsquo;s protecting our own home.</p>
<a class="tlink" href="@/about-us/">About the company {ARROW}</a></div></div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label">Service areas</p><h2>From North Ogden <span>to Spanish Fork.</span></h2>
<p class="lede">We work in 52 cities across five regions, coordinated from our Cottonwood Heights office. Pick a region, or tap a dot to open that city&rsquo;s page.</p></div>
{map_block()}
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label dark">Field photos</p><h2>Our crews, <span>our roofs.</span></h2><p class="lede">Shingle, flat and commercial roofs, from crew phones and the drone. No stock photos.</p></div>
<div class="gal">{galh}</div>
<p class="more reveal"><a class="tlink" href="@/our-roofing-projects/">See the projects {ARROW}</a></p>
</div></section>

<section class="sec feature"><div class="wrap split">
<div class="reveal"><p class="label dark">From the job file</p><h2>A school roof <span>in South Salt Lake.</span></h2>
<p>Our crew&rsquo;s job photos from June 2021 show flat-roof membrane work at Saint Ann&rsquo;s School in South Salt Lake, worked from a boom lift beside the historic brick building, with the Wasatch behind. Flat and low-slope roofs like this are the work our <a href="@/services/commercial-roofing/tpo-membrane-roofing/">TPO membrane</a> page describes.</p>
<a class="tlink" href="@/services/commercial-roofing/">Commercial roofing {ARROW}</a></div>
<div class="duo reveal">{img("saint-anns-school-lift", "Historic brick school building with a boom lift at the roof")}{img("saint-anns-flat-roof", "Flat-roof membrane going down, with the mountains beyond")}</div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label">Storm damage &amp; insurance</p><h2>We handle the claim <span>so you don&rsquo;t have to.</span></h2>
<p class="lede">Hail, wind and heavy snow can damage a roof in ways you can&rsquo;t see from the ground. We document it, help you through the insurance process, and do the work.</p></div>
<ol class="steps">{steps}</ol>
<p class="more reveal"><a class="tlink light" href="@/roof-insurance-claim/">How claim help works {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label dark">Questions</p><h2>Straight answers.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec tight"><div class="wrap"><a class="guide reveal" href="@/{p_blog.POST[1]}"><span class="arch">{img("roof-vents-mountains", "")}</span><span><span class="label dark">From the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></span></a></div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company Cottonwood Heights | Utah Roofing Pros",
            "meta": "Utah Roofing Pros is a family-owned roofing company in Cottonwood Heights: roof repair, replacement, commercial roofing and insurance claim help.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def service(row):
    key, path, lab, grp, im, title, meta, h1, intro = row
    trail = [HOME, ("Services", "services/")] + ([(f"{grp} roofing", RES[-1][1] if grp == "Residential" else COM[0][1])] if path not in (RES[-1][1], COM[0][1]) else []) + [(lab, path)]
    sib = [r for r in (RES if grp == "Residential" else COM) if r[0] != key]
    rel = f'<div class="side-rel"><p class="label dark">{grp}</p><ul>{"".join(f"<li><a href=@/{r[1]}>{r[2]}</a></li>" for r in sib)}</ul></div>'
    body = phero(trail, h1, None, f"{grp} &middot; Cottonwood Heights", im, ALT.get(im, lab + " by Utah Roofing Pros")) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose"><p class="answer">{intro}</p>
{mig(key, skip=(lab, h1))}
</article>{side(rel)}</div></section>''' + cta()
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "og": im,
            "schema": [{"@type": "Service", "@id": canon(path) + "#service", "name": html.unescape(lab), "provider": {"@id": U + "#business"},
                        "areaServed": {"@type": "City", "name": "Cottonwood Heights, UT"}}, crumbs_ld(path, trail)]}


ALT.update({"roofer-on-roof": "Roofer working on a shingle roof", "tear-off-in-progress": "Crew tearing off an old roof next to an apartment building",
            "roofer-nailing-shingles": "Roofer nailing new asphalt shingles", "hail-damaged-shake-roof": "Hail-damaged wood shake roof",
            "ladder-brick-home": "Ladder against a brick home during roof work", "saint-anns-flat-roof": "Flat-roof membrane on a commercial building",
            "flat-roofs-aerial": "Aerial view of flat roofs on a brick building"})


def services():
    trail = [HOME, ("Services", "services/")]
    rows = "".join(f'<a class="row reveal" href="@/{r[1]}">{img(r[4], ALT.get(r[4], r[2]))}<span class="mono">{r[3]}</span><b>{r[2]}</b><i>{ARROW}</i></a>' for r in SVC)
    body = phero(trail, "Roofing Services in Cottonwood Heights", "Repair, replacement, shingle roofs, storm damage, swamp cooler removal and commercial roofing.", "Services", "aerial-new-roof-foothills", ALT["aerial-new-roof-foothills"]) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose"><p class="answer">Utah Roofing Pros offers residential and commercial roofing services from our office in Cottonwood Heights: roof repair and replacement, asphalt shingle roofs, storm damage repair, swamp cooler removal, TPO membrane and commercial shingle roofing, plus insurance claim help and financing.</p>
{mig("services", skip=("Services",))}
</article><aside class="sv-side"><div class="rowlist">{rows}</div></aside></div></section>''' + cta()
    return {"path": "services/", "canonical": canon("services/"), "title": "Roofing Services in Cottonwood Heights | Utah Roofing Pros",
            "meta": "Roofing services in Cottonwood Heights from family-owned Utah Roofing Pros: roof repair, replacement, storm damage, swamp cooler removal and commercial roofs.",
            "body": body, "schema": [crumbs_ld("services/", trail)]}


def about():
    trail = [HOME, ("About Us", "about-us/")]
    body = phero(trail, "About Utah Roofing Pros", "Built on family values. A Cottonwood Heights roofing company since 2017.", "Family-owned &middot; Since 2017", "team-on-roof-clipboard", "Two members of the Utah Roofing Pros team on a roof with a clipboard, mountains behind") + f'''
<section class="sec"><div class="wrap split" style="align-items:start"><article class="prose">
<p class="answer">Utah Roofing Pros is a family-owned roofing company in Cottonwood Heights, Utah, founded in {FOUNDED} by John and Phil Panos. What started as a shared vision between two skilled roofers now serves homeowners and businesses in 52 cities across northern Utah.</p>
{mig("about_us", skip=("About Utah Roofing Pros", "Where it All Started"))}
</article><div class="about-imgs reveal">{img("owners-on-roof", "Two members of the Utah Roofing Pros team on a finished roof")}{img("truck-job-site", "Utah Roofing Pros truck parked at a job site")}</div></div></section>''' + cta()
    return {"path": "about-us/", "canonical": canon("about-us/"), "title": "About Utah Roofing Pros | Family-Owned Roofers Since 2017",
            "meta": "About Utah Roofing Pros: a family-owned roofing company in Cottonwood Heights, founded in 2017 by John and Phil Panos, serving 52 cities in northern Utah.",
            "body": body, "schema": [crumbs_ld("about-us/", trail), {"@type": "AboutPage", "@id": canon("about-us/") + "#page", "url": canon("about-us/")}]}


def contact():
    trail = [HOME, ("Contact Us", CONTACT)]
    body = phero(trail, "Contact Utah Roofing Pros", "Call, email or send a message. We&rsquo;ll get back to you with clear next steps.", "Cottonwood Heights office", buttons=False) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><dl class="info">
<div><dt>Call</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div>
<div><dt>Office</dt><dd>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</dd></div>
<div><dt>Serving</dt><dd>52 cities across the Salt Lake Valley, northern Wasatch Front, Utah County, Wasatch Back and Tooele. <a href="@/service-areas/">See the map</a>.</dd></div></dl>
<div class="prose">{mig("contact_us", skip=("Contact Information", "Get in Touch With Us!"))}</div></div>
<div class="reveal">{quote_form("Send a message")}</div></div></section>'''
    return {"path": CONTACT, "canonical": canon(CONTACT), "title": "Contact Utah Roofing Pros | Cottonwood Heights Roofers",
            "meta": "Contact Utah Roofing Pros in Cottonwood Heights: call (801) 688-3853, email john@utahroofingpros.com, or send us a message to book a free roof inspection.",
            "body": body, "schema": [crumbs_ld(CONTACT, trail), {"@type": "ContactPage", "@id": canon(CONTACT) + "#page", "url": canon(CONTACT)}]}


def areas():
    trail = [HOME, ("Service Areas", "service-areas/")]
    body = phero(trail, "Roofing Service Areas in Utah", "52 cities in five regions, coordinated from our Cottonwood Heights office.", "Service areas", buttons=False) + f'''
<section class="sec"><div class="wrap"><p class="answer narrow">Utah Roofing Pros provides residential and commercial roofing across the Salt Lake Valley, the northern Wasatch Front, Utah County, the Wasatch Back and the Tooele area. Choose your city for local information on roof repair, replacement, inspections, storm damage and commercial roofing. Don&rsquo;t see your city? We may still serve your area: <a href="@/{CONTACT}">contact us</a> to confirm.</p>
{map_block()}</div></section>''' + cta()
    return {"path": "service-areas/", "canonical": canon("service-areas/"), "title": "Roofing Service Areas in Utah: 52 Cities | Utah Roofing Pros",
            "meta": "Utah Roofing Pros service areas: 52 cities across the Salt Lake Valley, northern Wasatch Front, Utah County, Wasatch Back and Tooele, with a map of each.",
            "body": body, "schema": [crumbs_ld("service-areas/", trail)]}


def city(i, slug, name, ri, reg):
    key = "service_areas_" + slug.replace("-", "_")
    path = f"service-areas/{slug}/"
    trail = [HOME, ("Service Areas", "service-areas/"), (name, path)]
    im = POOL[i % len(POOL)]
    near = [c for c in CITIES if c[2] == ri and c[0] != slug][:8]
    rel = f'<div class="side-rel"><p class="label dark">Also in {reg}</p><ul>{"".join(f"<li><a href=@/service-areas/{s}/>{n}</a></li>" for s, n, *_ in near)}</ul><a class="tlink" href="@/service-areas/">All 52 cities {ARROW}</a></div>' if near else ""
    mini = f'<div class="side-map">{map_svg(slug, labels=True, link=False)}<p class="mono small">{name} on the map, with our office in Cottonwood Heights.</p></div>'
    body = phero(trail, f"Roofing Contractor in {name}, Utah", None, f"{reg} &middot; Service area", im, ALT[im]) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">
{mig(key, skip=(f"Roofing Contractor in {name}, Utah",))}
</article>{side(mini + rel)}</div></section>''' + cta(f"Free roof inspection in {name}.")
    title = f"Roofing Contractor in {name}, Utah | Utah Roofing Pros"
    if len(title) > 60: title = f"Roofing Contractor in {name}, UT | Utah Roofing Pros"
    if len(title) > 60: title = f"{name} Roofing Contractor | Utah Roofing Pros"
    meta = f"Roofing contractor in {name}, Utah: roof repair, replacement, inspections, storm damage and commercial roofing from Utah Roofing Pros. Free estimates."
    if len(meta) > 160: meta = meta.replace("commercial roofing", "commercial roofs")
    if len(meta) < 150: meta = meta.replace("Free estimates.", "Free roof estimates.")
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "og": im,
            "schema": [crumbs_ld(path, trail), {"@type": "Service", "@id": canon(path) + "#service", "name": f"Roofing in {name}, Utah", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": name + ", UT"}}]}


def simple(key, path, label, h1, lede, tag, title, meta, image=None, intro="", extra="", skip=(), drop=DROP, crumbs=None, form=False):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    content = f'<p class="answer">{intro}</p>' if intro else ""
    content += mig(key, skip=skip + (h1,), drop=drop) if key else ""
    right = f'<div class="reveal">{quote_form()}</div>' if form else side()
    body = phero(trail, h1, lede, tag, image, ALT.get(image, "") if image else "") + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{content}{extra}</article>{right}</div></section>''' + ("" if form else cta())
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "schema": [crumbs_ld(path, trail)]}


def projects():
    gal = ["aerial-tudor-home-roof", "shingle-delivery-boom", "aerial-roof-fall-trees", "dome-boom-lift", "new-roof-mountain-view", "flat-roof-brick-building", "tear-off-in-progress",
           "roof-wood-siding-aerial", "saint-anns-school-lift", "dormer-roof-aerial", "red-shingle-roof-mountains", "flat-roofs-aerial", "hail-damaged-shake-roof", "aerial-white-house",
           "roofer-nailing-shingles", "garage-roof-new"]
    ALT.update({"shingle-delivery-boom": "Shingles lifted to a roof by boom", "dome-boom-lift": "Boom lift beside a historic dome", "flat-roof-brick-building": "White flat roof on a brick building",
                "saint-anns-school-lift": "Boom lift at Saint Ann's School, South Salt Lake"})
    galh = "".join(f'<figure>{img(n, ALT[n])}<figcaption>{ALT[n]}</figcaption></figure>' for n in gal)
    pg = simple("our_roofing_projects", "our-roofing-projects/", "Our Roofing Projects", "Roofing Projects in Utah", "Homes and commercial buildings across the Wasatch Front, photographed by our crews.", "Projects",
                "Roofing Projects in Utah | Utah Roofing Pros Field Photos",
                "Roofing projects by Utah Roofing Pros: shingle re-roofs, flat and TPO roofs, storm repairs and historic buildings across Salt Lake County and northern Utah.",
                image="aerial-tudor-home-roof", skip=("Our Roofing Projects",))
    pg["body"] = pg["body"].replace('<section class="cta">', f'<section class="sec tight"><div class="wrap"><div class="pgal">{galh}</div></div></section><section class="cta">', 1)
    return pg


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, INSPECT)
    return [_fit(dict(x, body=Q(x["body"]))) for x in _pages()]


def _fit(pg):
    for add in (" Free inspection.", " Family-owned.", " Call (801) 688-3853."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "Try a service below, the service-area map, or call the office.", "404") + f'<section class="sec"><div class="wrap"><div class="svcs">{"".join(f"<a class=\"svc\" href=\"@/{r[1]}\"><span class=\"arch\">{img(r[4], r[2])}</span><span class=\"mono\">{r[3]}</span><b>{r[2]}</b></a>" for r in SVC[:6])}</div></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Utah Roofing Pros", "meta": "This page was not found. See Utah Roofing Pros roofing services in Cottonwood Heights or call (801) 688-3853 for a free roof inspection from a family-owned team.",
            "body": body, "robots": "noindex, follow", "sitemap": False}


def _pages():
    out = [home()] + [service(r) for r in SVC] + [services(), about(), contact(), areas()]
    out += [city(i, *c) for i, c in enumerate(CITIES)]
    gs = [("Get started", "get-started/")]
    out += [
        simple("get_started", "get-started/", "Get started", "Get Started With Your Roof", "Fast. Easy. No pressure.", "Get started",
               "Get a Free Roof Inspection or Estimate | Utah Roofing Pros",
               "Get started with Utah Roofing Pros: book a free roof inspection, request an estimate, get insurance claim help or ask about financing options.",
               image="team-three-yellow", skip=("Get Started",),
               extra='<div class="paths">' + "".join(f'<a href="@/{p}"><b>{l}</b>{ARROW}</a>' for l, p in GET) + "</div>"),
        simple("get_started_schedule_free_roof_inspection", INSPECT, "Free roof inspection", "Free Roof Inspection in Cottonwood Heights", "No pressure. No hidden fees. A careful look at your roof, with photos.", "Free inspection",
               "Free Roof Inspection, Cottonwood Heights | Utah Roofing Pros",
               "Book a free roof inspection in Cottonwood Heights: Utah Roofing Pros checks shingles, flashing, vents and storm damage and shows you photos of what we find.",
               intro="Utah Roofing Pros offers a free roof inspection in Cottonwood Heights and every city we serve. We check the shingles or membrane, flashing, vents, valleys and penetrations, look for storm and hail damage, photograph what we find, and explain whether the roof needs a repair, a replacement, or nothing yet.",
               extra="<h2>What we check</h2><ul><li>Shingles: missing, lifted, cracked or worn</li><li>Flashing at pipes, chimneys, walls and skylights</li><li>Valleys, ridge and roof vents</li><li>Signs of hail and wind damage</li><li>Old swamp-cooler openings and other penetrations</li><li>Gutters and drip edge, and signs of leaks inside</li></ul><h2>What you get</h2><p>Photos of what we found, a clear explanation, and a written estimate if work is needed. Already have another bid? We&rsquo;re happy to give a second opinion.</p>",
               crumbs=gs, form=True),
        simple("get_started_instant_roofing_estimate", "get-started/instant-roofing-estimate/", "Instant estimate", "Request a Roofing Estimate", "No pressure. No hidden fees. A fast estimate, delivered to your inbox.", "Estimate",
               "Request a Roofing Estimate Online | Utah Roofing Pros",
               "Request a roofing estimate from Utah Roofing Pros: tell us about the roof and the work you need, and we'll send an estimate to your inbox. No pressure.",
               intro="Tell us about your roof and what you need, whether that&rsquo;s a repair, a replacement or a commercial roof, and Utah Roofing Pros will send you an estimate. For an exact price we&rsquo;ll still want to see the roof, and that inspection is free.",
               crumbs=gs, form=True),
        simple("roof_financing", "roof-financing/", "Roof financing", "Roof Financing in Cottonwood Heights", "Flexible payment options for roof repairs and replacements.", "Financing",
               "Roof Financing in Cottonwood Heights | Utah Roofing Pros",
               "Roof financing in Cottonwood Heights: ask Utah Roofing Pros about payment options for roof replacement, storm repairs and insurance deductibles.",
               image="aerial-white-house",
               intro="Utah Roofing Pros offers roof financing for qualified homeowners in Cottonwood Heights and the cities we serve, so a needed repair or replacement doesn&rsquo;t have to wait. Ask about current options and qualification requirements when you book your free estimate.",
               skip=("Roof Financing Utah",)),
        simple("roof_insurance_claim", "roof-insurance-claim/", "Roof insurance claim", "Roof Insurance Claim Help in Cottonwood Heights", "From the free inspection to the final walkthrough.", "Insurance claims",
               "Roof Insurance Claim Help in Cottonwood Heights, UT",
               "Roof insurance claim help in Cottonwood Heights: free inspection and photo documentation, help filing, adjuster meetings, and the repair or replacement.",
               image="hail-damaged-shake-roof",
               intro="After storm, hail, wind or falling-debris damage, Utah Roofing Pros helps homeowners in Cottonwood Heights with the roof insurance claim: a free inspection with photo documentation, help filing, a meeting with your adjuster, and then the repair or replacement."),
        projects(),
        simple("legal", "legal/", "Legal", "Legal Information", None, "Legal", "Legal Information | Utah Roofing Pros",
               "Legal information for utahroofingpros.com: the Utah Roofing Pros privacy policy, terms and conditions, and cookie policy, with links to each document.",
               extra='<ul><li><a href="@/legal/privacy-policy/">Privacy Policy</a></li><li><a href="@/legal/terms-and-conditions/">Terms &amp; Conditions</a></li><li><a href="@/legal/cookie-policy/">Cookie Policy</a></li></ul>', drop=NODROP),
    ]
    lg = [("Legal", "legal/")]
    for key, path, lab, t in [("legal_privacy_policy", "legal/privacy-policy/", "Privacy Policy", "privacy policy"), ("legal_terms_and_conditions", "legal/terms-and-conditions/", "Terms &amp; Conditions", "terms and conditions"),
                              ("legal_cookie_policy", "legal/cookie-policy/", "Cookie Policy", "cookie policy")]:
        out.append(simple(key, path, lab, lab, None, "Legal", f"{html.unescape(lab)} | Utah Roofing Pros",
                          f"The Utah Roofing Pros {t} for utahroofingpros.com: what it covers, how it applies to visitors and customers, and how to reach us.",
                          drop=NODROP, crumbs=lg, skip=(html.unescape(lab),)))
    return out + p_blog.pages() + [notfound()]
