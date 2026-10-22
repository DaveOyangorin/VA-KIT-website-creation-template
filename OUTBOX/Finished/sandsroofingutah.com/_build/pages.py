"""Pages for the sandsroofingutah.com redesign, v2 (20 Oct 2026): "Above the valley".

A roofer works where nobody else stands: up top, looking out over the Salt Lake Valley. S&S has the drone photos to prove it, so
the site is built from that vantage point. References (screenshotted 20 Oct 2026): Carhartt (yellow and black, condensed caps
over real work photography), Liquid Death (oversized headlines, full-bleed confidence), Ableton (asymmetric, overlapping tiles).
Motif: the 6/12 roof pitch (26.6 degrees): diagonal section cuts, gable-topped cards and pitch readouts as section markers.
Signature: "Layer by layer" (s_layers.py), a drawn roof section built from deck to final inspection by dragging up the slope,
paired with real crew photos of each step. Also: a full-bleed valley hero with parallax, an asymmetric sector collage, a services
index with photos that follow the cursor, a drifting crew film strip, the refugee hub as a before/after spread, a wall of the
channels people find them through, and a review rotator.
Home targets "roofing company west valley city" (report, 17 Oct 2026); service pages name West Valley City in title, H1 and first
paragraph. The 16 ad landing pages keep their URLs and forms (noindex, out of the sitemap: see notes).
Left out until confirmed: "35+ years of combined experience", "Customer Satisfaction Guaranteed", "the best materials", the
"Happy Clients" counter, the roof-calculator link, and star ratings on the testimonials.
"""
import html, json, os, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, SHORT, U, HERE, DOMAIN, AREAS, CHANNELS
from migrate import migrate
import p_blog
import s_layers

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CONTACT = "contact-us/"
HOME = ("Home", "")
DROP = re.compile(r"35\+|over 35|guarantee|best materials|the best|top tier|top-tier|happy clients|calculat|Call us today at|^contact$|Click here|Phone Number|Full Physical|Select Choice|Send Message|^Name \*", re.I)
CTA_P = re.compile(r"^(Get|Schedule|Book|Call|Contact|Talk|Learn|Explore|Request|Ask|See|View|Find|Start|Click|Read More|Download)\b[^.]{0,48}!?$", re.I)
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CITIES = [("roofing_services_in_west_valley_city_utah", "West Valley City"), ("roofing_services_in_salt_lake_city_utah", "Salt Lake City"), ("roofing_services_in_west_jordan_utah", "West Jordan"),
          ("roofing_services_in_south_jordan_utah", "South Jordan"), ("roofing_services_in_kearns_utah", "Kearns"), ("reliable_roofers_in_taylorsville_utah", "Taylorsville"),
          ("roofer_in_murray_utah", "Murray"), ("roofing_in_midvale_utah", "Midvale"), ("reliable_roofers_in_sandy_utah", "Sandy"), ("roofing_in_draper_utah", "Draper"),
          ("roofers_in_riverton_utah", "Riverton"), ("roofing_company_in_millcreek_utah", "Millcreek"), ("roofing_company_in_south_salt_lake_utah", "South Salt Lake"),
          ("roofing_company_in_north_salt_lake_utah", "North Salt Lake"), ("roofing_company_in_farmington_utah", "Farmington"), ("roofing_company_in_ogden_utah", "Ogden")]
QUOTES = [("Austin was awesome. Great company good ratings honest service. Very responsive. Quick and thorough estimates. Excellent customer skills.", "Marilyn Barrigar"),
          ("Several years ago I had to choose a roofing company to replace my many layered roof. I researched S and S and found them the best for my needs. I still call them for any other roof related issues. They added some turbines for me two years. I totally recommend S and S Roofing.", "Heidi Nielson"),
          ("Excellent job replacing our roof. Great value for the money. They also did a good job cleaning up and hauling away debris. Completed the replacement roof very quickly.", "Eric Weber")]
SERVICES = [("Roof Repair", "Leaks, damaged shingles and other issues, fixed to restore the roof and prevent further damage.", "crew-shingle-nailing"),
            ("Roof Replacement", "From tear-off to final inspection, every layer installed with precision.", "crew-tear-off-deck"),
            ("Skylight Install", "Natural light, installed and flashed to be leak-proof and energy-efficient.", "skylight-install"),
            ("Soffit &amp; Fascia", "Better ventilation and protection from moisture and pests, plus curb appeal.", "soffit-repair-crew"),
            ("Heat Cable", "Melts snow and ice along the roof edges to help prevent ice dams.", "heat-cable-install"),
            ("New Construction", "Roofs built to the project&rsquo;s specifications, on new homes and buildings.", "new-construction-aerial"),
            ("Snow Removal", "Heavy snow cleared safely with the right equipment, before it causes damage.", "snowy-cabin-roof"),
            ("Gutter Install", "Gutters fitted to carry water away from the roof and foundation.", "crew-drip-edge"),
            ("Roof Inspection", "A thorough check of the roof&rsquo;s condition, with a report and recommendations.", "crew-ridge-shingles")]
HOME_FAQ = [("What kinds of roofs do you work on?", "All roof types: asphalt shingles, metal, flat and low-slope roofs (TPO, EPDM, PVC), tile and slate, and modified bitumen and built-up roofing, on homes, multi-family buildings and commercial properties."),
            ("Do you give free quotes?", "Yes. Tell us the address, the roof type (shingle, flat or metal) and whether you need a repair, a full replacement or a recover, and we&rsquo;ll get back to you with a quote."),
            ("Do you work with HOAs and property managers?", "Yes. We help condominium associations, HOA boards and apartment owners with documentation, timelines, budget planning and keeping disruption to residents low."),
            ("Do you offer financing?", "Financing is available. Ask about it when you request your quote."),
            ("Do you serve Park City?", f"Yes. Our Park City line is {S['phone2']}; for the Salt Lake Valley call {S['phone']}.")]


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def tidy(s):
    out = []
    for blk in re.findall(r"<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s, re.S):
        txt = html.unescape(re.sub(r"<[^>]+>", "", blk)).strip()
        if txt.startswith(("Get in Touch", "Customer Satisfaction")): break
        if blk.startswith("<p>") and CTA_P.match(txt): continue
        out.append(blk)
    def minor(b): return b.startswith("<h3>") or re.fullmatch(r"<p><strong>[^<]{0,70}</strong></p>", b) is not None
    def head(b): return b.startswith("<h2>") or minor(b)
    out = [b for i, b in enumerate(out) if not (i + 1 < len(out) and ((minor(b) and head(out[i + 1])) or (b.startswith("<h2>") and out[i + 1].startswith("<h2>"))))]
    while out and head(out[-1]): out.pop()
    return "\n".join(out)


def mig(key, skip=(), drop=DROP):
    return tidy(migrate(HERE, key, DOMAIN, drop, skip_heads=skip))


def secn(n, t, light=False):
    return f'<p class="sec-n{" light" if light else ""}"><b>{n}</b><span>{t}</span></p>'


def header():
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{SHORT} home">{img("ss-roofing-logo", NAME, lazy=False)}<span class="brand-t"><b>S&amp;S Roofing</b><small>Salt Lake &middot; Park City</small></span></a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop"><a href="@/residential-re-roofing-roof-repairs/">Residential re-roofing &amp; repairs</a><a href="@/commercial-roofing/">Commercial roofing</a><a href="@/multi-family-roofing/">Multi-family roofing</a><a href="@/roofing-solutions-for-condominiums-and-hoa-communities-in-utah/">Condos &amp; HOAs</a><a href="@/services/">All services</a></div></details></li>
<li><a href="@/projects/">Projects</a></li><li><a href="@/service-areas/">Service Areas</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/about/">About</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Salt Lake</small><span>(801) 272-7000</span></a><a class="btn" href="@/{CONTACT}">Free Quote</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/residential-re-roofing-roof-repairs/">Residential</a><a href="@/commercial-roofing/">Commercial</a><a href="@/multi-family-roofing/">Multi-family</a><a href="@/services/">All services</a>
<a href="@/projects/">Projects</a><a href="@/service-areas/">Service Areas</a><a href="@/blog/">Blog</a><a href="@/about/">About</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>''')


def footer():
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-big">Roofs for the Salt Lake Valley <span>and Park City.</span></p><a class="btn" href="@/{CONTACT}">Get a free quote {ARROW}</a></div>
<div class="foot">
<div><span class="flogo">{img("ss-roofing-logo", NAME + " logo")}</span><p>{NAME}: roofing for homes, businesses and multi-family properties across the Salt Lake Valley and Park City.</p></div>
<div><h3>Roofing</h3><ul><li><a href="@/residential-re-roofing-roof-repairs/">Residential</a></li><li><a href="@/commercial-roofing/">Commercial</a></li><li><a href="@/multi-family-roofing/">Multi-family</a></li><li><a href="@/roofing-solutions-for-condominiums-and-hoa-communities-in-utah/">Condos &amp; HOAs</a></li><li><a href="@/services/">All services</a></li><li><a href="@/projects/">Projects</a></li></ul></div>
<div><h3>Call</h3><p><span class="small">Salt Lake</span><br><a class="fph" href="tel:{S["tel"]}">{S["phone"]}</a></p><p><span class="small">Park City</span><br><a class="fph" href="tel:{S["tel2"]}">{S["phone2"]}</a></p><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div><h3>Office</h3><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><ul class="hrs">{"".join(f"<li><span>{d}</span><b>{t}</b></li>" for d, t in S["hours"])}</ul></div>
</div>
<p class="fareas"><b>Serving</b> {" &middot; ".join(AREAS)}</p>
<div class="fbottom"><span>&copy; 2026 {NAME}</span><span><a href="@/privacy-policy/">Privacy policy</a> &middot; <a href="@/service-areas/">Service areas</a> &middot; <a href="@/blog/">Blog</a></span></div></div>
<div class="foot-mark" aria-hidden="true">S&amp;S Roofing</div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Free Quote</a></div>''')


def coupon(title="Get a free roofing quote."):
    return f'''<div class="coupon"><div class="cp-in"><p class="cp-k">Free quote &middot; Salt Lake &amp; Park City</p><p class="cp-t">{title}</p>
<p class="cp-s">Repair, full replacement or recover. Shingle, flat or metal. Homes, businesses and multi-family.</p>
<div class="cp-row"><a class="btn dark" href="@/{CONTACT}">Request a quote {ARROW}</a></div>
<p class="cp-f"><span>Salt Lake</span><a href="tel:{S["tel"]}">{S["phone"]}</a></p><p class="cp-f"><span>Park City</span><a href="tel:{S["tel2"]}">{S["phone2"]}</a></p></div></div>'''


def cta(title="Need a roof repair or replacement?", text="Don&rsquo;t wait for leaks or damage to get worse. Call the office or send the form, and someone from our team will reach out soon."):
    return f'''<section class="cta"><div class="wrap cta-in"><div class="cta-text"><p class="label">Free quote</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-ph"><a href="tel:{S["tel"]}"><small>Salt Lake</small>{S["phone"]}</a><a href="tel:{S["tel2"]}"><small>Park City</small>{S["phone2"]}</a><a class="btn" href="@/{CONTACT}">Request a quote {ARROW}</a></div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", buttons=True):
    art = f'<figure class="ph-img">{img(image, alt, priority=True)}</figure>' if image else ""
    btn = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Quote {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} (801) 272-7000</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div>{art}</div></section>'''


def quote_form(title="Get a free quote", source=None):
    how = (f'<input type="hidden" name="heard_about" value="{source}">' if source else
           '<label for="f-how">How did you hear about us?<select id="f-how" name="heard_about"><option value="">Choose one</option>' + "".join(f"<option>{c}</option>" for c, p in CHANNELS if c != "TV Commercial") + "<option>Google</option><option>None of the above</option></select></label>")
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label>
<label for="f-addr">Full physical address *<input id="f-addr" name="address" autocomplete="street-address" required></label>
<div class="row"><label for="f-type">Roof type *<select id="f-type" name="roof_type" required><option value="">Choose</option><option>Shingle</option><option>Flat</option><option>Metal</option></select></label>
<label for="f-help">Help needed *<select id="f-help" name="help" required><option value="">Choose</option><option>Repair</option><option>Full Replacement</option><option>Recover</option></select></label></div>
{how}<label for="f-msg">Message<textarea id="f-msg" name="message"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


def side(extra=""):
    return f'''<aside class="sv-side">{coupon()}{extra}</aside>'''


SVC_LINK = {"Roof Repair": "residential-re-roofing-roof-repairs/", "Roof Replacement": "residential-re-roofing-roof-repairs/"}


def home():
    strip = "".join(f'<figure>{img(n, a)}<figcaption>{a}</figcaption></figure>' for n, a in [("crew-membrane-roll", "Rolling out membrane on a flat roof"), ("crew-shingle-nailing", "Nailing shingles"),
                    ("crew-shake-roof", "Cutting wood shakes"), ("crew-flat-roof-seams", "Flat roof seams"), ("crew-tear-off-deck", "A tear-off, down to the deck"),
                    ("crew-ridge-shingles", "Ridge shingles"), ("crew-flat-roof-patch", "Patching a flat roof"), ("parapet-coping-install", "Parapet coping going on"), ("soffit-repair-crew", "Soffit repair")])
    chans = "".join(f"<span>{c}</span>" for c, p in CHANNELS if c not in ("RSVP", "TV Commercial", "Banner Advertisement", "Vehicle Scan"))
    wall = "".join(f'<li><a href="@/{p}"><span class="sw-n">{i + 1:02d}</span><b>{c}</b><em>Found us here {ARROW}</em></a></li>'
                   for i, (c, p) in enumerate([x for x in CHANNELS if x[0] not in ("RSVP", "Banner Advertisement", "Vehicle Scan", "TV Commercial")]))
    svcs = "".join(f'<li><a href="@/{SVC_LINK.get(html.unescape(t), "services/")}"><span class="sv-n">{i + 1:02d}</span><b>{t}</b><span class="sv-d">{d}</span><span class="sv-ar">{ARROW}</span><span class="sv-ph">{img(im, "")}</span></a></li>'
                   for i, (t, d, im) in enumerate(SERVICES))
    HUB = [("The roof", "Leaks, age, visible wear. The home stores food and sometimes shelters families, so leaks, mold or structural damage were a real threat."),
           ("Tear-off", "The entire home and garage roof was stripped down to the bare wood."),
           ("The crew", "Our installers donated their labor, and Roofers Supply donated the materials."),
           ("Every layer", "Every layer was replaced for a secure, leak-free system."),
           ("Finished", "The hub keeps doing its work: a gathering place, a food pantry and a temporary shelter, under a new roof.")]
    hub = "".join(f'<li><span>{i + 1:02d}</span><div><b>{k}</b><p>{d}</p></div></li>' for i, (k, d) in enumerate(HUB))
    revs = "".join(f'<blockquote class="rv{" on" if i == 0 else ""}" data-i="{i}"><p>{q}</p><footer>{n}</footer></blockquote>' for i, (q, n) in enumerate(QUOTES))
    body = f'''
<section class="hero">
<figure class="hero-bg">{img("projects-valley-view", "A home with a new metal roof above the Salt Lake Valley", priority=True)}</figure>
<div class="wrap hero-in">
<div class="hero-text"><p class="kicker"><b>6/12</b>Roofing company &middot; West Valley City, Utah</p>
<h1>Roofing company in West Valley City</h1>
<p class="hero-sub">Shingle, flat, shake and metal.</p>
<p class="lede">S&amp;S Roofing is a roofing company serving West Valley City, Salt Lake City and Park City: roof repair, re-roofing and replacement for homes, businesses and multi-family properties. Our office is on South Redwood Road.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a free quote {ARROW}</a><a class="btn ghost" href="#layers">How a roof goes on</a></div></div>
<aside class="hero-ticket"><p class="ht-k">Call the office</p><a href="tel:{S["tel"]}"><small>Salt Lake</small>{S["phone"]}</a><a href="tel:{S["tel2"]}"><small>Park City</small>{S["phone2"]}</a><p class="ht-h">Mon&ndash;Fri &middot; 8:00am&ndash;5:00pm</p></aside>
</div>
<p class="hero-cap">From our projects &middot; above the Salt Lake Valley</p>
</section>
<section class="seen" aria-label="Where you may have seen us"><div class="seen-in"><b>Seen us around?</b>{chans}{chans}</div></section>

<section class="sec intro"><div class="wrap intro-in">
{secn("01", "Who we are")}
<div class="intro-main"><p class="statement reveal">Started on residential shingle replacements. Grown into a full-service roofer for every roof type, <span>built on honesty, hard work and quality craftsmanship.</span></p>
<div class="intro-meta reveal"><figure class="intro-ph">{img("crew-shingle-nailing", "S&S roofers nailing shingles")}</figure>
<div><p>A locally rooted roofing company in Salt Lake City, roofing homes, businesses and multi-family properties from Ogden and Layton down to Provo, and up to Park City and Heber City.</p><a class="tlink" href="@/about/">About S&amp;S {ARROW}</a></div></div></div>
</div></section>

<section class="sec sectors-sec"><div class="wrap">
<div class="sec-head reveal">{secn("02", "Who we roof for")}<h2>Three kinds of property. <span>One crew.</span></h2></div>
<div class="sectors">
<a class="sector s1 reveal" href="@/residential-re-roofing-roof-repairs/"><figure>{img("drone-home-shingles", "Aerial view of a home with a new shingle roof")}</figure><div class="s-cap"><span>01</span><b>Residential</b><p>Re-roofing and roof repairs for houses, from a small leak to a full new roof.</p><em>Residential roofing {ARROW}</em></div></a>
<a class="sector s2 reveal" href="@/commercial-roofing/"><figure>{img("commercial-flat-roof", "Flat commercial roof with HVAC units")}</figure><div class="s-cap"><span>02</span><b>Commercial</b><p>Installation, repair, replacement and maintenance for business roofs, flat or pitched.</p><em>Commercial roofing {ARROW}</em></div></a>
<a class="sector s3 reveal" href="@/multi-family-roofing/"><figure>{img("multifamily-aerial", "Aerial view of a multi-family roofing project")}</figure><div class="s-cap"><span>03</span><b>Multi-family</b><p>Apartments, condos and townhomes, with one point of contact and minimal disruption to residents.</p><em>Multi-family roofing {ARROW}</em></div></a>
<div class="s-note reveal"><p>Condo association or HOA board? We help with documentation, timelines, budget planning and keeping disruption to residents low.</p><a class="tlink" href="@/roofing-solutions-for-condominiums-and-hoa-communities-in-utah/">Condos &amp; HOAs {ARROW}</a></div>
</div></div></section>

{s_layers.section(secn)}

<section class="sec svc-sec"><div class="wrap">
<div class="sec-head split-head reveal"><div>{secn("04", "Services")}<h2>Everything <span>up top.</span></h2></div><p class="lede">Repairs and full replacements, plus the parts of a roof people forget until they fail: skylights, soffit and fascia, heat cable, gutters and snow.</p></div>
<ol class="svc-list" data-svc>{svcs}</ol>
<p class="more"><a class="tlink" href="@/services/">All roofing services {ARROW}</a></p>
</div></section>

<section class="sec crew-sec"><div class="wrap">
<div class="sec-head split-head reveal"><div>{secn("05", "On the job")}<h2>Every photo here <span>is ours.</span></h2></div><p class="lede">Tear-offs, flat roofs, shakes and shingles across the valley. No stock photos, no models: our crews, on real roofs.</p></div>
</div><div class="filmstrip">{strip}</div></section>

<section class="sec hub-sec"><div class="wrap hub2">
<div class="hub-photos reveal"><figure class="hub-after">{img("refugee-hub-after-1", "The Utah Ukrainian refugee hub with its new roof")}<figcaption>After</figcaption></figure>
<figure class="hub-before">{img("refugee-hub-before", "The refugee hub roof before replacement")}<figcaption>Before</figcaption></figure></div>
<div class="hub-text reveal">{secn("06", "In the community", True)}<h2>A new roof for the <span>Utah Ukrainian refugee hub.</span></h2>
<p class="lede">With materials from Roofers Supply and labor donated by our installers, we replaced the roof on the Utah Ukrainian Refugee Organization&rsquo;s community hub in Salt Lake City: a gathering place, food pantry and temporary shelter for families displaced by the war.</p>
<ol class="hub-list">{hub}</ol>
<a class="tlink light" href="@/sands-roofing-provides-a-new-roof-for-utah-ukrainian-refugee-hub/">Read the whole story {ARROW}</a></div>
</div></section>

<section class="sec seen-sec"><div class="wrap">
<div class="sec-head split-head reveal"><div>{secn("07", "Seen us around?")}<h2>On TV, in the mailbox, <span>in the magazines.</span></h2></div><p class="lede">S&amp;S reaches the valley the hometown way. If one of these is where you found us, start there.</p></div>
<ul class="seen-wall">{wall}</ul>
</div></section>

<section class="sec rev-sec"><div class="wrap rev" data-rev>
<div class="rev-side">{secn("08", "From our customers")}<div class="rev-ctl"><button type="button" class="rv-prev" aria-label="Previous review">{ARROW}</button><span class="rev-n"><b>01</b> / {len(QUOTES):02d}</span><button type="button" class="rv-next" aria-label="Next review">{ARROW}</button></div></div>
<div class="rev-stage" aria-live="polite">{revs}</div>
</div></section>

<section class="sec faq-sec"><div class="wrap faq-grid">
<div class="reveal">{secn("09", "Questions")}<h2>Good to know.</h2>{faq_html(HOME_FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="gm-k">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="form-wrap reveal">{quote_form()}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company West Valley City | S&S Roofing, Inc.",
            "meta": "S&S Roofing is a roofing company serving West Valley City, Salt Lake and Park City: roof repair, re-roofing and replacement for homes, businesses and HOAs.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def simple(key, path, label, h1, lede, tag, title, meta, image=None, alt="", intro="", extra="", skip=(), drop=DROP, crumbs=None, form=False, robots=None, sitemap=True, source=None, schema=None):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    content = (f'<p class="answer">{intro}</p>' if intro else "") + (mig(key, skip=skip + (h1, label), drop=drop) if key else "") + extra
    right = f'<div class="reveal">{quote_form(source=source)}</div>' if form else side()
    body = phero(trail, h1, lede, tag, image, alt) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{content}</article>{right}</div></section>''' + ("" if form else cta())
    pg = {"path": path, "canonical": canon(path), "title": title, "meta": meta, "body": body, "og": image, "schema": [crumbs_ld(path, trail)] + (schema or [])}
    if robots: pg["robots"] = robots
    if not sitemap: pg["sitemap"] = False
    return pg


def svc_schema(path, name):
    return [{"@type": "Service", "@id": canon(path) + "#service", "name": name, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "West Valley City, UT"}}]


def pages_main():
    sv = [("Services", "services/")]
    out = [
        simple("services", "services/", "Services", "Roofing Services in West Valley City", "Residential, commercial and multi-family roofing, plus skylights, soffit, heat cable, snow removal and gutters.", "Services",
               "Roofing Services in West Valley City | S&S Roofing, Inc.",
               "Roofing services in West Valley City and the Salt Lake Valley: repair, replacement, skylights, soffit and fascia, heat cable, snow removal, gutters and inspections.",
               image="projects-valley-view", alt="A home with a new roof overlooking the Salt Lake Valley",
               intro="S&amp;S Roofing offers roofing services in West Valley City, across the Salt Lake Valley and in Park City: residential, commercial and multi-family roofing; roof repair, replacement and inspections; and skylight, soffit and fascia, heat cable, gutter and snow removal work.",
               skip=("SERVICES", "Our Services", "What We Have to Offer")),
        simple("residential_re_roofing_roof_repairs", "residential-re-roofing-roof-repairs/", "Residential re-roofing &amp; repairs", "Residential Re-Roofing &amp; Roof Repairs in West Valley City", None, "Residential",
               "Re-Roofing &amp; Roof Repair in West Valley City | S&S Roofing",
               "Residential re-roofing and roof repairs in West Valley City: new roofs, leaks, missing shingles, flashing and storm damage, with clear quotes from S&S Roofing.",
               image="drone-home-shingles", alt="Aerial view of a home with a new shingle roof",
               intro="S&amp;S Roofing handles residential re-roofing and roof repairs in West Valley City and across the Salt Lake Valley: from fixing a leak, missing shingles or damaged flashing to putting a complete new roof on your home.",
               skip=("RESIDENTIAL RE-ROOFING & ROOF REPAIRS", "Residential Re-Roofing & Roof Repairs"), crumbs=sv, schema=svc_schema("residential-re-roofing-roof-repairs/", "Residential re-roofing and roof repair")),
        simple("commercial_roofing", "commercial-roofing/", "Commercial roofing", "Commercial Roofing in West Valley City", None, "Commercial",
               "Commercial Roofing in West Valley City | S&S Roofing, Inc.",
               "Commercial roofing in West Valley City: installation, repair, replacement and maintenance of TPO, EPDM, PVC, metal and modified bitumen roofs for businesses.",
               image="commercial-roof-aerial", alt="Aerial view of a commercial flat roof",
               intro="S&amp;S Roofing provides commercial roofing in West Valley City and the Salt Lake Valley: new installations, repairs, replacements and preventative maintenance on flat and pitched business roofs, planned to keep your operations running.",
               skip=("COMMERCIAL ROOFING",), crumbs=sv, schema=svc_schema("commercial-roofing/", "Commercial roofing")),
        simple("multi_family_roofing", "multi-family-roofing/", "Multi-family roofing", "Multi-Family Roofing in West Valley City", None, "Multi-family",
               "Multi-Family Roofing in West Valley City | S&S Roofing, Inc.",
               "Multi-family roofing in West Valley City for apartments, condos and townhomes: inspections, repairs and replacements with one point of contact and less disruption.",
               image="multifamily-aerial", alt="Aerial view of a multi-family roof project",
               intro="S&amp;S Roofing roofs multi-family properties in West Valley City and across the Salt Lake Valley (apartments, condos and townhomes), with inspections, repairs and full replacements planned around your residents.",
               skip=("MULTI-FAMILY ROOFING",), crumbs=sv, schema=svc_schema("multi-family-roofing/", "Multi-family roofing")),
        simple("about", "about/", "About", "About S&amp;S Roofing", "A locally rooted roofing company in Salt Lake City.", "About",
               "About S&S Roofing, Inc. | Salt Lake City &amp; West Valley Roofers",
               "About S&S Roofing, Inc.: a locally rooted Salt Lake City roofing company that grew from residential shingle replacement into a full-service roofer for all roof types.",
               image="refugee-hub-team", alt="S&S Roofing at the Utah Ukrainian refugee hub",
               intro="S&amp;S Roofing is a locally rooted roofing company in Salt Lake City. It started with residential shingle replacements and has grown into a full-service roofing company that handles all roof types, built on honesty, hard work and quality craftsmanship.",
               skip=("ABOUT", "ABOUT US")),
        simple("contact_us", CONTACT, "Contact Us", "Contact S&amp;S Roofing", "Call, email or send the form, and someone from our team will reach out soon.", "Contact",
               "Contact S&S Roofing, Inc. | Free Roofing Quotes, Salt Lake",
               "Contact S&S Roofing: Salt Lake +1 (801) 272-7000, Park City +1 (435) 658-4344, admin@sandsroofingutah.com, 2331 South Redwood Road. Mon to Fri, 8 to 5.",
               extra=f'''<dl class="info"><div><dt>Salt Lake</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div><div><dt>Park City</dt><dd><a href="tel:{S["tel2"]}">{S["phone2"]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div><div><dt>Office</dt><dd>{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]} USA</dd></div>
<div><dt>Hours</dt><dd>{" &middot; ".join(f"{d} {t}" for d, t in S["hours"])}</dd></div></dl>''', skip=("CONTACT", "Get In Touch", "Send Us A Message"), form=True),
        simple("service_areas", "service-areas/", "Service Areas", "Roofing Service Areas in Utah", "Salt Lake County and surrounding areas, up to Ogden and over to Park City.", "Service areas",
               "Roofing Service Areas in Utah | S&S Roofing, Salt Lake Valley",
               "S&S Roofing serves Salt Lake County and nearby areas, from Ogden and Layton to Provo, Tooele, Park City, Heber City and Midway. See the full list of cities.",
               extra='<ul class="areas">' + "".join(f"<li>{a}</li>" for a in AREAS) + "</ul><h2>City pages</h2><ul class=\"citylinks\">" +
                     "".join(f'<li><a href="@/{EXT[k]["url"].replace(U, "")}">{c}</a></li>' for k, c in CITIES) + "</ul>",
               intro="S&amp;S Roofing proudly serves Salt Lake County and the surrounding areas, from Ogden, Layton and Kaysville in the north to Lehi, Orem and Provo in the south, west to Tooele and Stansbury Park, and up to Park City, Deer Valley, Heber City and Midway."),
        simple("projects", "projects/", "Projects", "Roofing Projects", "Shingle, shake, flat and commercial work by our crews.", "Projects",
               "Roofing Projects | S&S Roofing, Inc., West Valley City &amp; SLC",
               "Roofing projects by S&S Roofing: shingle, shake and flat roofs, commercial and multi-family work, and the new roof for the Utah Ukrainian refugee hub.",
               image="projects-valley-view", alt="A home with a new roof overlooking the Salt Lake Valley", drop=re.compile(DROP.pattern + r"|^(Shingle Roof|Shake Shingle|Shingle Residential|Shingle & Flat|Finished Work:)$", re.I),
               extra='<div class="pgal">' + "".join(f'<figure>{img(n, a)}<figcaption>{a}</figcaption></figure>' for n, a in [
                   ("drone-home-new-roof", "New roof, from the drone"), ("solar-modern-home", "Modern home with solar on the roof"), ("commercial-roof-aerial", "Commercial flat roof"),
                   ("new-construction-aerial", "New construction"), ("flat-roof-tpo-overhead", "Flat roof membrane, from above"), ("parapet-coping-install", "Parapet coping going on"),
                   ("refugee-hub-after-2", "Refugee hub, finished"), ("crew-shake-roof", "Wood shake roof")]) + "</div>"),
        simple("privacy_policy", "privacy-policy/", "Privacy Policy", "Privacy Policy", None, "Legal", "Privacy Policy | S&S Roofing, Inc.",
               "The S&S Roofing, Inc. privacy policy for sandsroofingutah.com: what information we collect through our forms, how we use it, and how to contact us.", drop=re.compile(r"(?!x)x")),
    ]
    for k, c in CITIES:
        v = EXT[k]; path = v["url"].replace(U, "")
        h1 = html.unescape(v["title"].split(" - S&S")[0])
        t = f"{h1} | S&S Roofing"
        if len(t) > 60: t = h1
        out.append(simple(k, path, c, h1, None, "Service area", t,
                          f"{h1}: roof repair, re-roofing, replacement and new roofs for homes, multi-family and commercial buildings in {c}, from S&S Roofing, Inc.",
                          skip=(h1.upper(), h1), crumbs=[("Service Areas", "service-areas/")],
                          schema=[{"@type": "Service", "@id": canon(path) + "#service", "name": f"Roofing in {c}, Utah", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": c + ", UT"}}]))
    for c, p in CHANNELS:
        out.append(simple(None, p, c, f"{c} &middot; Roofing Service Request", "Thank you for considering S&amp;S Roofing. Fill out the form and someone from our team will reach out to you soon.", "Thanks for finding us",
                          f"{c} | S&S Roofing Service Request", f"Saw S&S Roofing in {c}? Request roofing service here: repair, full replacement or recover for shingle, flat and metal roofs in the Salt Lake Valley.",
                          intro=f"Thanks for finding us through {c}. Tell us about your roof below, or call {S['phone']} (Salt Lake) or {S['phone2']} (Park City).",
                          form=True, robots="noindex, follow", sitemap=False, source=c))
    return out


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, CONTACT, tidy)
    out = [home()] + pages_main() + p_blog.pages() + [notfound()]
    return [_fit(dict(x, body=Q(x["body"]))) for x in out]


def _fit(pg):
    for add in (" Free quotes.", " Call (801) 272-7000."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "Try our services, the blog, or call the office.", "404") + f'<section class="sec"><div class="wrap"><p><a class="tlink" href="@/services/">Services {ARROW}</a> &nbsp; <a class="tlink" href="@/blog/">Blog {ARROW}</a></p></div></section>'
    return {"path": "404.html", "title": "Page Not Found | S&S Roofing, Inc.", "meta": "This page was not found. See S&S Roofing services and projects, or call +1 (801) 272-7000 for a free roofing quote in West Valley City and the Salt Lake Valley.",
            "body": body, "robots": "noindex, follow", "sitemap": False}
