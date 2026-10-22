"""Pages for the utahoneroofing.com redesign: "the ops board".

The client is veteran-owned (their own words on every service page), so the site borrows the order and plainness of an
operations board: stencil numerals, field photos as numbered cards, a four-step "standard" (the client's own process), and
an area-of-operations grid of the seven counties they list. Only the client's own job photos are used.
Home and the blog post are written by hand; the 8 other real pages keep the client's own text, cleaned, with a new title,
meta, H1 and opening paragraph naming Salt Lake City (report, 17 Oct 2026).
Left out (see notes): theme demo content (lorem ipsum, "Robert C. Simmons, CEO Roof Inc." and the other placeholder team,
the placeholder testimonials, "32k partners", "Project Completed / Awards Win" counters), the 9 demo blog posts about Colorado
and the Twin Cities, the category/tag/author archives, and unsupported claims: "top-rated", "best", "more than 10 years",
"24/7" and "24-hour response", "up to 100 years", price ranges, and the financing terms.
"""
import html, re
import engine as E
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, COUNTIES, NAME, LEGAL, U, HERE, DOMAIN
from migrate import migrate
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
STAR = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="m12 2 2.9 6.9 7.1.6-5.4 4.7 1.7 7-6.3-3.9-6.3 3.9 1.7-7L2 9.5l7.1-.6z"/></svg>'
CONTACT = "contact/"
HOME = ("Home", "")
DROP = re.compile(r"top[- ]rated|\bbest\b|more than 10 years|10\+ years|24/7|24-hour|up to 100 years|\$\d|same-as-cash|financing|low-rate|top roofing companies|"
                  r"top-quality|lorem|variations of passages|32k|disabled veteran|no-interest|There many variations|tax incentive|\bguarantee", re.I)

SVC = [("residential_roofing", "residential-roofing/", "Residential Roofing", "01", "home-new-shingle-roof", "A home with a new shingle roof and a deck",
        "Residential Roofing in Salt Lake City | Utah One Roofing",
        "Residential roofing in Salt Lake City from a veteran-owned team: shingle, tile and metal roofs installed, replaced and repaired. Free estimates.",
        "Residential Roofing in Salt Lake City", "Utah One Roofing installs, replaces and repairs home roofs in Salt Lake City and across Salt Lake, Davis, Utah, Summit and Tooele counties, in asphalt shingle, tile and metal. We are a veteran-owned company, and every job starts with a free estimate."),
       ("commercial_roofing", "commercial-roofing/", "Commercial Roofing", "02", "tpo-commercial-roof-crew", "Crew installing a white TPO membrane on a commercial roof with the Wasatch behind",
        "Commercial Roofing in Salt Lake City | Utah One Roofing",
        "Commercial roofing in Salt Lake City: TPO, PVC, metal and modified bitumen roofs for commercial buildings, planned to keep your business running.",
        "Commercial Roofing in Salt Lake City", "Utah One Roofing handles commercial roofing in Salt Lake City: TPO, PVC, metal and modified bitumen roofs, from full installs to repairs and maintenance, planned to keep disruption to tenants and customers low."),
       ("roof_repair", "roof-repair/", "Roof Repair", "03", "tear-off-crew-on-roof", "Utah One Roofing crew removing old roofing",
        "Roof Repair in Salt Lake City, UT | Utah One Roofing",
        "Roof repair in Salt Lake City for leaks, missing shingles, flashing and storm damage. Veteran-owned Utah One Roofing. Call (801) 928-9570 for a free estimate.",
        "Roof Repair in Salt Lake City", "Utah One Roofing repairs roofs in Salt Lake City and nearby counties: leaks, missing or damaged shingles, pipe flashing and storm damage. Small leak or major damage, we find the cause, give you a clear estimate and fix it."),
       ("insurance_restoration", "insurance-restoration/", "Insurance Restoration", "04", "shake-roof-tear-off", "Old wood shake roofing torn off a damaged roof",
        "Roof Insurance Restoration in Salt Lake City | Utah One",
        "Insurance roof restoration in Salt Lake City: storm, hail, fire and falling-debris damage inspected, documented and repaired, with help on your claim.",
        "Insurance Roof Restoration in Salt Lake City", "Utah One Roofing helps Salt Lake City homeowners through roof insurance restoration: we inspect and document storm, hail, fire, water and falling-debris damage, help with the claim, and complete the repair or replacement."),
       ("skylight_installation", "skylight-installation/", "Skylight Installation", "05", "drone-home-new-roof", "Drone view of a finished home roof",
        "Skylight Installation in Salt Lake City | Utah One Roofing",
        "Velux skylight installation in Salt Lake City: ventilated, fixed and tubular skylights installed and flashed by a roofing crew. Free estimates.",
        "Skylight Installation in Salt Lake City", "Utah One Roofing installs Velux skylights in Salt Lake City homes: ventilated skylights for kitchens and bathrooms, fixed skylights for high ceilings, and tubular skylights for small rooms, flashed into the roof by the same crew that roofs it.")]


def header():
    nav = "".join(f'<a href="@/{p}"><span class="st">{n_}</span>{lab}</a>' for k, p, lab, n_, *_ in SVC)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("one-roofing-logo-white", NAME, cls="on-dark", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{nav}<a href="@/services/"><span class="st">&rarr;</span>All services</a></div></details></li>
<li><a href="@/about-us/">About</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{nav}</div><a href="@/services/">All services</a>
<a href="@/about-us/">About</a><a href="@/blog/">Blog</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>'''


def hours_html():
    return "".join(f"<li><span>{d}</span><b>{t}</b></li>" for d, t in S["hours"])


def footer():
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">One crew. One standard.<br><span>One roof at a time.</span></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a></div></div>
<div class="foot">
<div>{img("one-roofing-logo-white", LEGAL + " logo", cls="flogo")}<p>{LEGAL}: reliable roofing with integrity, professionalism and service. Veteran-owned. Proudly serving Utah.</p>
<p class="soc"><a href="{S["ig"]}" rel="noopener">Instagram</a> &middot; <a href="{S["fb"]}" rel="noopener">Facebook</a></p></div>
<div><h3>Services</h3><ul>{"".join(f'<li><a href="@/{p}">{lab}</a></li>' for k, p, lab, *_ in SVC)}<li><a href="@/services/">All services</a></li></ul></div>
<div><h3>Contact</h3><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="tel:{S["tel2"]}">{S["phone2"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div><h3>Hours</h3><ul class="hrs">{hours_html()}</ul></div>
</div><div class="fbottom"><span>&copy; 2026 {LEGAL}</span><span>{" &middot; ".join(c + " Co." for c in COUNTIES)}</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Free Estimate</a></div>'''


def cta(title="Ready when you are.", text="Call or send a message for a free estimate. We&rsquo;ll respond as soon as possible.", image="modern-home-metal-roof-mountains"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap">
<div class="reveal"><p class="label">Free estimate</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call</small><b>{S["phone"]}</b></a><a class="btn" href="@/{CONTACT}">Send a Message {ARROW}</a></div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", buttons=True):
    bg = f'<div class="ph-bg">{img(image, alt, priority=True)}</div>' if image else ""
    btn = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" img" if image else ""}">{bg}<div class="wrap"><span class="ph-tag st" aria-hidden="true">{tag}</span>{crumbs_html(trail)}<h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div></section>'''


def quote_form(title="Book for inspection"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label>
<label for="f-svc">Service<select id="f-svc" name="service"><option value="">Choose one</option>{"".join(f"<option>{lab}</option>" for k, p, lab, *_ in SVC)}<option>Something else</option></select></label>
<label for="f-msg">Message<textarea id="f-msg" name="message" placeholder="Address and what you&rsquo;re seeing"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button><p class="note">* Required. We&rsquo;ll respond as soon as possible.</p></form>'''


STEPS = [("Clear communication", "We start with honest, open communication: listening to your needs and keeping you updated every step of the way.", "drone-roof-install-overview"),
         ("Custom design &amp; consultation", "Together we design a roof that fits your style, budget and property, so it meets your specific goals.", "drone-roof-in-progress"),
         ("Expert installation", "The team installs your roof with care, using quality materials and proven techniques for lasting results.", "metal-roof-crew-installing"),
         ("Thorough cleanup", "We protect your property and don&rsquo;t leave until the work area is spotless, like we were never there.", "drone-home-new-roof")]
HOME_FAQ = [("Is your company licensed and insured?", "Absolutely. We&rsquo;re fully licensed and insured, and we&rsquo;re happy to provide documentation, like liability and workers&rsquo; compensation coverage, along with your estimate."),
            ("How can I tell if my roof needs to be replaced?", "Some warning signs include water leaks, missing shingles, visible sagging, or general wear and tear, especially on an older roof. Not sure? We offer professional inspections to assess your roof and guide you on the next steps."),
            ("Will you protect my property during the roofing job?", "Yes, always. We take extra precautions to shield your landscaping, outdoor furniture and surrounding areas."),
            ("Is there anything I need to do before the project starts?", "We recommend moving any vehicles or items close to the work area. We&rsquo;ll walk you through all prep steps in advance."),
            ("What happens once the job is done?", "After installation we inspect everything thoroughly and clean up the site, so you&rsquo;re left with a new roof and a tidy yard.")]


def home():
    cards = [("home-new-shingle-roof", "Residential", "Shingle roof, finished"), ("tpo-commercial-roof-crew", "Commercial", "TPO membrane, Wasatch Front"), ("standing-seam-metal-roof", "Metal", "Standing seam")]
    board = "".join(f'<figure class="card c{i + 1}">{img(n, a, lazy=False)}<figcaption><span class="st">0{i + 1}</span>{a}<em>{c}</em></figcaption></figure>' for i, (n, a, c) in enumerate(cards))
    svc = "".join(f'''<a class="svc reveal" href="@/{p}">{img(im, alt)}<span class="svc-in"><span class="st">{n_}</span><b>{lab}</b><em>View {ARROW}</em></span></a>''' for k, p, lab, n_, im, alt, *_ in SVC)
    steps = "".join(f'''<li class="reveal"><span class="st">0{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div>{img(im, "")}</li>''' for i, (t, d, im) in enumerate(STEPS))
    gal = ["cedar-shake-dormer", "modern-home-metal-roof-mountains", "underlayment-over-deck", "shingles-going-on-mountain-view", "cedar-shake-roof-detail", "drone-roof-in-progress", "new-shingle-ridge-line", "swamp-cooler-roof-removal"]
    caps = ["Cedar shake dormer", "Metal roof, mountain home", "Underlayment over the deck", "Shingles going on", "Cedar shake detail", "Roof in progress, from the air", "New ridge line", "Old swamp cooler coming off"]
    galh = "".join(f'<figure class="g{i} reveal">{img(n, c)}<figcaption><span class="st">F{i + 1:02d}</span>{c}</figcaption></figure>' for i, (n, c) in enumerate(zip(gal, caps)))
    aoo = "".join(f'<li><span class="st">{i + 1}</span><b>{c}</b><small>County</small></li>' for i, c in enumerate(COUNTIES))
    body = f'''
<section class="hero"><div class="hero-bg">{img("modern-home-metal-roof-mountains", "A modern home with a dark metal roof below the Wasatch Mountains", priority=True)}</div>
<span class="hero-one st" aria-hidden="true">1</span>
<div class="wrap hero-in">
<div class="hero-text"><p class="label">Veteran-owned &middot; Salt Lake City, Utah</p>
<h1>A roofing company in Salt Lake City <span>held to one standard.</span></h1>
<p class="lede">Utah One Roofing is a veteran-owned roofing company in Salt Lake City for homes and businesses: roof repair and replacement, insurance restoration, flat and metal roofs, gutters and Velux skylights. Free estimates across seven Utah counties.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Book for Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="board">{board}</div>
</div></section>

<section class="strip" aria-label="At a glance"><div class="wrap strip-in">
<span>{STAR} Veteran-owned</span><span>{STAR} Free estimates</span><span>{STAR} 7 Utah counties</span><span>{STAR} Velux skylights</span><span>{STAR} Homes &amp; businesses</span></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label dark">Roofers in Salt Lake City</p><h2>Five services. <span>One crew.</span></h2>
<p class="lede">As roofing contractors in Salt Lake City, we protect homes and businesses with reliable, durable roofs, and fix the ones that need it.</p></div>
<div class="svcs">{svc}</div>
<p class="more reveal"><a class="tlink" href="@/services/">All services, including flat roofs, metal, gutters and green roofing {ARROW}</a></p>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label">Our process</p><h2>The One standard, <span>in four steps.</span></h2><p class="lede">More than a roof: how every Utah One job runs, from the first call to the last swept nail.</p></div>
<ol class="std">{steps}</ol>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label dark">Field photos</p><h2>Our roofs, <span>on our crews&rsquo; phones.</span></h2><p class="lede">Shingle, cedar shake, metal and TPO: jobs across the Salt Lake Valley and the Wasatch Front.</p></div>
<div class="gal">{galh}</div>
</div></section>

<section class="sec aoo-sec"><div class="wrap split">
<div class="reveal"><p class="label dark">Area of operations</p><h2>Seven counties, <span>one crew.</span></h2>
<p>We take pride in serving communities across Utah. Call {S["phone"]} or {S["phone2"]}.</p>
<ul class="hrs big">{hours_html()}</ul></div>
<ol class="aoo reveal">{aoo}</ol>
</div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Have questions? <span>Here are answers.</span></h2>
{faq_html(HOME_FAQ)}</div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap"><a class="guide reveal" href="@/{p_blog.POST[1]}">{img("drone-roof-underlayment", "")}<span><span class="label dark">From the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></span></a></div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company Salt Lake City | Veteran-Owned Utah One",
            "meta": "Utah One Roofing is a veteran-owned roofing company in Salt Lake City: roof repair, replacement, insurance restoration and skylights. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def service(row):
    key, path, lab, n_, im, alt, title, meta, h1, intro = row
    trail = [HOME, ("Services", "services/"), (lab, path)]
    other = [r for r in SVC if r[0] != key]
    body = phero(trail, h1, None, n_, im, alt) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose"><p class="answer">{intro}</p>
{migrate(HERE, key, DOMAIN, DROP, skip_heads=(lab, lab.replace(" ", " ")))}
</article><aside class="sv-side">
<div class="side-card"><p class="label">Free estimate</p><h3>Talk to the crew</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Book for Inspection {ARROW}</a><ul class="hrs">{hours_html()}</ul></div>
<div class="side-rel"><p class="label dark">Other services</p><ul>{"".join(f'<li><a href="@/{p}"><span class="st">{x}</span>{l}</a></li>' for k, p, l, x, *_ in other)}</ul></div>
</aside></div></section>''' + cta()
    return {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "og": im,
            "schema": [{"@type": "Service", "@id": canon(path) + "#service", "name": lab, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "Salt Lake City"}}, crumbs_ld(path, trail)]}


def services():
    trail = [HOME, ("Services", "services/")]
    rows = "".join(f'<a class="row reveal" href="@/{p}">{img(im, alt)}<span class="st">{n_}</span><b>{lab}</b><i>{ARROW}</i></a>' for k, p, lab, n_, im, alt, *_ in SVC)
    body = phero(trail, "Roofing Services in Salt Lake City", "Roof repair, replacement, insurance restoration, flat roofs, metal roofs, gutters, skylights and green roofing.", "S", "drone-roof-install-overview", "Drone view of a roof install") + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose"><p class="answer">Utah One Roofing ({LEGAL}) is a roofing company in Salt Lake City for roof repair, replacement, insurance restoration, flat roofs, metal roofs and gutter installation, plus Velux skylights and green roofing. We have a service-minded team that focuses on the whole customer experience, not only the technical side of the job.</p>
{migrate(HERE, "services", DOMAIN, DROP, skip_heads=("Services", "What We Do")).replace("@/green-roofing/", "@/" + p_blog.POST[1])}
</article><aside class="sv-side"><div class="rowlist">{rows}</div></aside></div></section>''' + cta()
    return {"path": "services/", "canonical": canon("services/"), "title": "Roofing Services in Salt Lake City | Utah One Roofing",
            "meta": "Roofing services in Salt Lake City from veteran-owned Utah One Roofing: repair, replacement, insurance restoration, flat and metal roofs, gutters, skylights.",
            "body": body, "schema": [crumbs_ld("services/", trail)]}


def about():
    trail = [HOME, ("About Us", "about-us/")]
    body = phero(trail, "About Utah One Roofing, Salt Lake City", "A veteran-owned roofing company serving seven Utah counties.", "A", "tear-off-crew-on-roof", "Utah One Roofing crew at work") + f'''
<section class="sec"><div class="wrap split" style="align-items:start"><article class="prose">
<p class="answer">At {LEGAL} we specialize in reliable solutions for roof repair, replacement, insurance restoration, flat and metal roofing, and gutter installation, serving Salt Lake, Utah, Davis, Summit, Tooele, Weber and Wasatch counties.</p>
<p>Our team is committed to high-quality service, focusing not only on the technical side of the job but on an exceptional customer experience. With integrity, honesty and professionalism, we make sure every project meets the highest standards.</p>
<h2>Veteran-owned</h2>
<p>As veterans, we bring our commitment beyond roofing, with a service rooted in values such as loyalty and teamwork. Just as we&rsquo;ve served our country, we stand by our work and are committed to serving you.</p>
<h2>What we value</h2>
<ul><li>Excellent total customer experience</li><li>Honesty and integrity</li><li>Team loyalty</li><li>Team building</li></ul>
<p>If you are looking for a trusted partner to protect your home or business, <a href="@/{CONTACT}">contact us</a> and request your free estimate.</p>
</article><div class="about-imgs reveal">{img("roof-sheathing-replacement", "Roof sheathing being replaced")}{img("cedar-shake-dormer", "Cedar shake roof on a dormer, with a ladder")}</div></div></section>''' + cta()
    return {"path": "about-us/", "canonical": canon("about-us/"), "title": "About Utah One Roofing | Veteran-Owned SLC Roofers",
            "meta": "About Utah One Roofing (One Roofing LLC): a veteran-owned roofing company in Salt Lake City serving seven Utah counties with integrity and honesty.",
            "body": body, "schema": [crumbs_ld("about-us/", trail), {"@type": "AboutPage", "@id": canon("about-us/") + "#page", "url": canon("about-us/")}]}


def contact():
    trail = [HOME, ("Contact", CONTACT)]
    body = phero(trail, "Contact Utah One Roofing in Salt Lake City", "Send us a message and we&rsquo;ll respond as soon as possible.", "C", buttons=False) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><dl class="info">
<div><dt>Call</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="tel:{S["tel2"]}">{S["phone2"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a><br><a href="mailto:{S["email2"]}">{S["email2"]}</a></dd></div>
<div><dt>Office</dt><dd>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</dd></div>
<div><dt>Hours</dt><dd><ul class="hrs">{hours_html()}</ul></dd></div>
<div><dt>Serving</dt><dd>{", ".join(c + " County" for c in COUNTIES)}</dd></div></dl></div>
<div class="reveal">{quote_form("Send a message")}</div></div></section>'''
    return {"path": CONTACT, "canonical": canon(CONTACT), "title": "Contact Utah One Roofing | Salt Lake City Roofing Estimates",
            "meta": "Contact Utah One Roofing in Salt Lake City: call (801) 928-9570 or (385) 223-9811, email us, or send a message for a free roofing estimate.",
            "body": body, "schema": [crumbs_ld(CONTACT, trail), {"@type": "ContactPage", "@id": canon(CONTACT) + "#page", "url": canon(CONTACT)}]}


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "Off the map.", "That page isn&rsquo;t here. Try a service, or call us.", "404") + f'<section class="sec"><div class="wrap"><div class="svcs">{"".join(f"<a class=\"svc\" href=\"@/{p}\">{img(im, alt)}<span class=\"svc-in\"><span class=\"st\">{n_}</span><b>{lab}</b></span></a>" for k, p, lab, n_, im, alt, *_ in SVC)}</div></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Utah One Roofing", "meta": "This page was not found. See Utah One Roofing services in Salt Lake City or call (801) 928-9570 for a free estimate from a veteran-owned roofing team.",
            "body": body, "robots": "noindex, follow", "sitemap": False}


def _fit(pg):
    for add in (" Free estimates.", " Veteran-owned.", " Call (801) 928-9570."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def make_pages():
    p_blog.setup(phero, cta, ARROW, HOME, CONTACT)
    return [_fit(x) for x in _pages()]


def _pages():
    return [home()] + [service(r) for r in SVC] + [services(), about(), contact()] + p_blog.pages() + [notfound()]
