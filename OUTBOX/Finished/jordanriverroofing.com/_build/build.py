"""Builds the jordanriverroofing.com redesign.

  python -I build.py <out_site> <out_preview>

The current site is a single-page app: every URL returns the same empty shell, with one title, one meta description
and canonical="/" on all 92 routes. The new site is plain HTML on the same 92 URLs (no trailing slash, as today),
each with its own title, description and canonical, plus a new blog post.
site/    : files to put live. Each URL is a folder with index.html; links are root-relative ("/about").
           The host must serve /about from about/index.html without forcing a trailing slash (Netlify, Cloudflare Pages
           and most static hosts do). The current site has no tracking code to keep.
preview/ : private review copy (relative links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://jordanriverroofing.com"
BIZ_ID = U + "/#business"
TODAY = "2026-10-17"
HOME_OG = "jordan-river-roofing-truck-owner"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))

# NAP copied from the current site (header, contact page and its own schema), 17 Oct 2026.
# Hours: the header and the site's schema say Mon-Fri 8-6, Sat 8-4 (the contact page says 7-6; see notes).
S = {"name": "Jordan River Roofing", "email": "phil@jordanriverroofing.com", "phone": "801-857-1417", "tel": "+18018571417",
     "street": "1278 W Kimman Lane", "city": "Taylorsville", "st": "UT", "zip": "84123",
     "map": "https://maps.google.com/?q=1278+W+Kimman+Lane+Taylorsville+UT+84123", "hours": "Mon&ndash;Fri 8am&ndash;6pm &middot; Sat 8am&ndash;4pm"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
CONTACT = "contact"

# The 13 service cities, south to north through the valley. Branch = east-bench city off the river corridor.
# ZIPs are the ones the client lists on /service-areas.
CITIES = [("draper", "Draper", "84020", False), ("riverton", "Riverton", "84065", False), ("south-jordan", "South Jordan", "84095", False),
          ("sandy", "Sandy", "84070", True), ("west-jordan", "West Jordan", "84088", False), ("cottonwood-heights", "Cottonwood Heights", "84121", True),
          ("murray", "Murray", "84107", False), ("taylorsville", "Taylorsville", "84123", False), ("holladay", "Holladay", "84117", True),
          ("west-valley-city", "West Valley City", "84119", False), ("millcreek", "Millcreek", "84107", True), ("south-salt-lake", "South Salt Lake", "84115", False),
          ("north-salt-lake", "North Salt Lake", "84054", False)]
CITY = {c[0]: c for c in CITIES}

# Services: slug, name, line code, color class, one-liner (from the client's services page)
SERVICES = [("new-roof-replacement", "New Roof &amp; Replacement", "RR", "l1", "Complete tear-off and a new architectural shingle roof."),
            ("roof-repairs-maintenance", "Roof Repairs &amp; Maintenance", "RP", "l2", "Leaks, missing shingles, flashing, plus annual maintenance."),
            ("commercial-roofing", "Commercial Roofing", "CM", "l3", "Flat and low-slope systems: TPO, EPDM, modified bitumen, coatings."),
            ("emergency-insurance-claims", "Emergency &amp; Insurance Claims", "EM", "l4", "Storm and leak response, tarping, photo reports, adjuster meetings."),
            ("attic-ventilation-skylights", "Attic Ventilation &amp; Skylights", "AV", "l5", "Ridge and soffit ventilation, attic fans, skylight install and repair.")]
SVC = {s[0]: s for s in SERVICES}
BLOG = ("Ridge Vent vs. Turtle Vents: Which Is Better?", "blog/ridge-vent-vs-turtle-vents")


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def canon(path):
    return U + "/" + path if path else U + "/"


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U + "/", "telephone": S["tel"], "email": S["email"],
         "logo": U + "/assets/img/jordan-river-roofing-logo.png", "image": U + "/assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"],
                     "postalCode": S["zip"], "addressCountry": "US"},
         "geo": {"@type": "GeoCoordinates", "latitude": 40.6544137, "longitude": -111.931162}, "hasMap": S["map"]}
    if full:
        n.update({"description": "Jordan River Roofing is a roofing company in Taylorsville, Utah, founded in 2019 by Phil: roof replacement, roof repairs and maintenance, commercial flat roofing, storm and insurance claim help, attic ventilation and skylights across the Salt Lake Valley.",
                  "foundingDate": "2019", "founder": {"@type": "Person", "name": "Philip Jordan"},
                  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"},
                                                {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday"], "opens": "08:00", "closes": "16:00"}],
                  "areaServed": [{"@type": "City", "name": c[1], "containedInPlace": {"@type": "State", "name": "Utah"}} for c in CITIES],
                  "knowsAbout": ["Roof replacement", "Roof repair", "Commercial flat roofing", "TPO", "EPDM", "Storm damage", "Insurance claims", "Attic ventilation", "Skylights"]})
    return [n]


def crumbs_ld(path, trail):
    return {"@type": "BreadcrumbList", "@id": canon(path) + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub(r"<[^>]+>", "", n)), "item": canon(p)} for i, (n, p) in enumerate(trail)]}


def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": html.unescape(re.sub(r"<[^>]+>", "", q)),
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", " ", a)).strip()}} for q, a in faqs]}


def crumbs_html(trail):
    out = []
    for i, (n, p) in enumerate(trail):
        out.append(f'<li aria-current="page">{n}</li>' if i == len(trail) - 1 else f'<li><a href="@/{p}">{n}</a></li>')
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">' + "".join(out) + "</ol></nav>"


def faq_html(faqs):
    out = []
    for i, (q, a) in enumerate(faqs):
        a = a if a.lstrip().startswith("<") else f"<p>{a}</p>"
        out.append(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a">{a}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


# The 13 reviews shown on the client's home page, word for word (reviewer names as shown there).
REVIEWS = [
    ("Highly recommended. Phil listens. He listened to what we wanted, then advised us whether what we were asking for was possible. Far too many in the business employ the hard sell, and know what's best; instead of treating customers as clients, not someone to walk all over and take advantage of. High quality materials and workmanship. The crew took care to protect the foliage and cleaned up after themselves. Phil went the extra mile. Again, highly recommended.", "Larry Hop"),
    ("Very pleased with the quality of work and the cost. Phil and his crew were great to work with did an excellent job. Went above and beyond. Project was completed before the time it was supposed to be. Very happy with everything about the project. Highly recommend.", "Joe Curtis"),
    ("Phil and his team were fantastic to work with from start to finish. Phil was very patient and explained everything in great detail and answered all of my questions without any hesitation. He and his crew were prompt, punctual, courteous, and professional throughout the process and the quality of workmanship was impressive even with all of the challenges my roof presented - there is a LOT going on up there. And, on top of all this, they offered an incredibly competitive price and left the work site absolutely spotless. I've already referred Jordan River Roofing to neighbors of mine and would happily recommend them to anyone who asks.", "Michael Lee"),
    ("Wonderful experience with Jordan River Roofing. Our roof had to be completely redone, a total tear off of the old shingles with new underlayment, and new high-quality shingles, new 3 vents, 2 chimneys expertly roofed around them, a soffit, gutter area properly repaired. The new roof really shines! Phil was very professional, and explained in detail what had to be done. He had a folder with a detailed contract, and other papers related to the roofing job. His crew did a complete clean up each day, although the new roof took only 1.5 days. Phil was very easy to work with, pleasant, friendly. Really delighted with the new roof, looks great! You will make the right choice to hire Jordan River Roofing for Any of your roofing needs! Excellent company!", "Judy Morrison"),
    ("Wow. Excellent service and an incredibly responsive team. I went from someone who knows nothing about roofing, to feeling quite confident that I made the best decision possible. I am very grateful for the education, the excellent service, and the reasonable price. They also installed super fast which was important for my situation, and kept me Informed all the way through the replacement.", "Amy Birkner Brown"),
    ("I chose to use Jordan River Roofing because of the professional presentation of the team and the costs were explained very clearly and inline with what my budget was. The start date was chosen and the work started and was completed within two days. The only holdup was the fact that the roof caps weren't available. As soon as the caps were ready, the work was done within one hour. I would definitely recommend Jordan River Roofing.", "Pat Hailes"),
    ("HIGHLY RECOMMEND Jordan River Roofing! Phil and his crew did a phenomenal job on my re-roof. Quality and service for a very reasonable price. I could not have asked for a better finished product - from tear down to installation these guys kept everything clean! They are extremely knowledgeable and have helped me achieve a fully ventilated attic space. I will be coming to these guys for any future roofing needs!!", "Kevin Muenzenmeyer"),
    ("JRR is a gem in the roofing industry. After interviewing Philip(the owner) I was immediately sold on his knowledge, experience, honest demeanor and a very reasonable price point. He took the time to explain the new technologies and installations of roofing from the past 30 years to the present. For example, other roof bidders were more expensive and didn't even include the new ridge venting system. These bidders wanted to keep the old inefficient turtle vents, slap the roof on and run. Philip knows what will last and will work the best for the long haul. Let's face it, your probably stuck in your home forever so get it done right with confidence and peace of mind--You will NOT have to look any further than JRR.", "Ket Knok"),
    ("I cannot say enough good things about this company. From the moment you meet Phil you are filled with confidence in his expertise and trustworthiness. His team was professional, courteous, and performed work of exceptional quality. They worked quickly and performed cleanups each night during the tear off and installation. The roof looks beautiful! It updated the whole appearance of the house. I am so grateful that we found Phil and Jordan River Roofing!!", "Deni Weeks"),
    ("Seriously top notch service. Phil was extremely knowledgeable and helpful. We are in the process of selling our house and during inspection a leak in our roof was reported and needed to be taken care of right away or the deal with our buyers could have potentially fallen through. Highly stressful situation. I gave Jordan River Roofing a call and they were out the very next day taking care of the issue. We highly recommend giving them a call for any of your roofing needs.", "Kristen Pastrano"),
    ("Phil was great to work with through the whole process. He followed through with everything that was promised which is such an anomaly these days. We appreciate his attention to detail in completing our project. We would definitely refer them.", "Chante' Christensen"),
    ("Phil is fantastic! Great company, and very professional in every aspect of the job! He went above and beyond to assure my satisfaction. I would highly recommend him to anyone wants a quality roof! Thank you Jordan River Roofing!", "Jack McCoy"),
    ("I worked with Phil to get a new roof put on my house. His bid was the cheapest and he also came with the best reviews by far. It's hard to find a contractor that you really feel comfortable with and trust. Phil is just that. I'd recommend JRR in a heartbeat to anyone who needs a new roof.", "Dan van der Merwe"),
]


def quotes_html(idx, title="What homeowners say about Phil and the crew", label="Reviews"):
    cards = "".join(f'<figure class="quote"><blockquote><p>&ldquo;{html.escape(REVIEWS[i][0])}&rdquo;</p></blockquote><figcaption><span class="av">{html.escape(REVIEWS[i][1][0])}</span>{html.escape(REVIEWS[i][1])}</figcaption></figure>' for i in idx)
    return f'<section class="sec reviews"><div class="wrap"><div class="head reveal"><p class="label">{label}</p><h2>{title}</h2></div><div class="quotes" tabindex="0" aria-label="Reviews, scroll sideways">{cards}</div></div></section>'


def reviews_marquee():
    """All 13 home-page reviews on two slow-moving rails (pause on hover; static for reduced motion)."""
    def card(i):
        t, n = REVIEWS[i]
        short = html.escape(t if len(t) < 240 else t[:t.rfind(" ", 0, 225)].rstrip(",.;") + "…")
        return f'<figure class="mq-card"><blockquote><p>&ldquo;{short}&rdquo;</p></blockquote><figcaption><span class="av">{html.escape(n[0])}</span>{html.escape(n)}</figcaption></figure>'
    a = "".join(card(i) for i in range(0, 7)); b = "".join(card(i) for i in range(7, 13))
    return f'''<div class="mq" aria-label="Reviews from the client&rsquo;s home page"><div class="mq-row"><div class="mq-track">{a}{a.replace('<figure class="mq-card">', '<figure class="mq-card" aria-hidden="true">')}</div></div>
<div class="mq-row rev"><div class="mq-track">{b}{b.replace('<figure class="mq-card">', '<figure class="mq-card" aria-hidden="true">')}</div></div></div>'''


def chip(code, cls):
    return f'<span class="chip {cls}">{code}</span>'


def valley_line(current=None, link_city=lambda c: f"service-areas/{c}"):
    """The service area drawn as a transit line: 13 stops, south to north (vertical list version)."""
    stops = []
    for slug, name, z, branch in CITIES:
        cls = "stop" + (" branch" if branch else "") + (" hq" if slug == "taylorsville" else "") + (" here" if slug == current else "")
        tag = '<em>Home base</em>' if slug == "taylorsville" else ('<em>East bench</em>' if branch else "")
        stops.append(f'<li class="{cls}"><a href="@/{link_city(slug)}"><b>{name}</b><span>{z}</span>{tag}</a></li>')
    return ('<div class="valley"><p class="dir mono">North &uarr; to Great Salt Lake</p><ol class="line">' + "".join(reversed(stops)) +
            '</ol><p class="dir mono">South &darr; to the Jordan Narrows</p></div>')


def valley_map(current=None):
    """The Valley Line as a transit diagram: the river corridor on the main line, the east-bench cities on a branch."""
    X = lambda i: 70 + i * 92
    MY, BY = 176, 76
    pos = {c[0]: (X(i), BY if c[3] else MY) for i, c in enumerate(CITIES)}
    main = [c for c in CITIES if not c[3]]
    main_d = "M30 176 " + " ".join(f"L{pos[c[0]][0]} {MY}" for c in main) + f" L{X(12) + 50} 176"
    br_d = f"M{X(2)} {MY} L{X(3) - 40} {BY} L{X(10)} {BY} L{X(11) - 30} {MY}"
    river = "M10 214 C 120 196, 200 236, 320 214 S 520 196, 640 220 S 860 236, 980 210 S 1150 196, 1250 214"
    stops, k = [], 0
    for i, (slug, name, z, br) in enumerate(CITIES):
        x, y = pos[slug]
        hq = slug == "taylorsville"
        if br: ly, anchor = BY - 26, "middle"
        else:
            ly = MY + (40 if k % 2 == 0 else 62); k += 1
        cls = "st" + (" hq" if hq else "") + (" here" if slug == current else "") + (" br" if br else "")
        tick = "" if br else f'<path class="tk" d="M{x} {MY + 12} V{ly - 14}"/>'
        stops.append(f'<a href="@/service-areas/{slug}" class="{cls}" aria-label="{name}, Utah {z}">{tick}<circle cx="{x}" cy="{y}" r="{14 if hq else 9}"/>'
                     f'<text x="{x}" y="{ly}" text-anchor="middle">{name}</text><text class="z" x="{x}" y="{ly + 15}" text-anchor="middle">{z}</text></a>')
    return f'''<div class="vmap"><svg viewBox="0 0 1250 260" role="img" aria-labelledby="vm-t"><title id="vm-t">Jordan River Roofing service area as a transit line: 13 cities from Draper in the south to North Salt Lake in the north, with Taylorsville as home base</title>
<path class="river" d="{river}"/><text class="rl" x="1240" y="259" text-anchor="end">Jordan River</text>
<path class="ln br-ln" d="{br_d}"/><path class="ln" d="{main_d}"/>
<text class="dirx" x="30" y="150">&larr; South</text><text class="dirx" x="1220" y="150" text-anchor="end">North &rarr;</text><text class="brl" x="{X(6)}" y="{BY - 50}" text-anchor="middle">East bench branch</text>
{"".join(stops)}</svg></div>'''


MENU_SVC = "".join(f'<a href="@/services/{s}">{chip(c, k)}<span><b>{n}</b><small>{d}</small></span></a>' for s, n, c, k, d in SERVICES)
MOB_SVC = "".join(f'<a href="@/services/{s}">{chip(c, k)}{n}</a>' for s, n, c, k, _ in SERVICES)


def header():
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Jordan River Roofing home">{img("jordan-river-roofing-logo", "Jordan River Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop"><p class="label">Five lines of work</p>{MENU_SVC}<a class="all" href="@/services">All services &rarr;</a></div></details></li>
<li><a href="@/service-areas">Service areas</a></li><li><a href="@/warranties">Warranty</a></li><li><a href="@/gallery">Gallery</a></li><li><a href="@/about">About</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call Phil&rsquo;s office</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{CONTACT}">Free Inspection</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{MOB_SVC}<a href="@/services">All services</a></div>
<a href="@/service-areas">Service areas</a><a href="@/warranties">Warranty</a><a href="@/gallery">Gallery</a><a href="@/about">About</a><a href="@/{BLOG[1]}">Guide: ridge vents</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="@/services/{s}">{chip(c, k)}{n}</a></li>' for s, n, c, k, _ in SERVICES)
    cities = "".join(f'<a href="@/service-areas/{c[0]}">{c[1]}</a>' for c in sorted(CITIES, key=lambda c: c[1]))
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Draper to North Salt Lake.<br><span>Taylorsville in the middle.</span></p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></div>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("jordan-river-roofing-logo", "Jordan River Roofing logo", cls="logo")}</span>
<p>A Taylorsville roofing company, founded in 2019 by Phil. Roofs across the Salt Lake Valley, from Draper to North Salt Lake.</p></div>
<div><h3>Services</h3><ul class="fsvc">{svc}</ul></div>
<div><h3>Company</h3><ul><li><a href="@/about">About</a></li><li><a href="@/warranties">DiamondShield Warranty</a></li><li><a href="@/gallery">Gallery</a></li><li><a href="@/service-areas">Service areas</a></li><li><a href="@/{BLOG[1]}">Ridge vent vs. turtle vents</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></div>
<div><h3>Office</h3><address>{S["name"]}<br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p><p class="mono">{S["hours"]}</p></div>
</div><div class="fcities"><span class="mono">Stops</span>{cities}</div>
<div class="fbottom"><span>&copy; 2026 Jordan River Roofing &middot; Taylorsville, Utah</span><span><a href="@/privacy-policy">Privacy Policy</a> &middot; <a href="@/terms-and-conditions">Terms</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Free Inspection</a></div>'''


def cta(title="Get a free roof inspection", text="Call the office or send a message. Phil or the team will set up a time to look at your roof and give you a clear, itemized estimate."):
    return f'''<section class="cta"><div class="cta-lines" aria-hidden="true"><i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i><i class="l5"></i></div><div class="wrap"><div class="reveal"><p class="label light">Free inspection</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call Phil&rsquo;s office</small><b>{S["phone"]}</b></a>
<a class="btn" href="@/{CONTACT}">Send a message {ARROW}</a><a class="cta-mail" href="mailto:{S["email"]}">{S["email"]}</a></div></div></section>'''


def phero(trail, h1, lede, label, image=None, alt="", code=None):
    pic = f'<figure class="ph-card">{img(image, alt, priority=True)}<figcaption class="mono">{alt}</figcaption></figure>' if image else ""
    c = f'{chip(*code)} ' if code else ""
    line = code[1] if code else "l2"
    return f'''<section class="phero{" has-img" if image else ""}"><div class="ph-lines {line}" aria-hidden="true"><i></i></div><div class="wrap"><div class="ph-text">{crumbs_html(trail)}
<p class="label light">{c}{label}</p><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>{pic}</div></section>'''


def contact_form(title="Request a free inspection"):
    # Same fields as the current contact form. It needs a form handler before go-live (see notes).
    opts = "".join(f"<option>{o}</option>" for o in ["General Inquiry", "Free Roof Inspection", "Roof Repair", "Roof Replacement", "Storm Damage / Insurance", "Commercial Roofing", "Emergency Service"])
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Full name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-subj">Subject<select id="f-subj" name="subject">{opts}</select></label></div>
<label for="f-msg">Message *<textarea id="f-msg" name="message" required></textarea></label>
<button class="btn" type="submit">Send Message {ARROW}</button></form>'''


def head(page):
    url = page.get("canonical") or canon(page["path"])
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "/#website", "url": U + "/", "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "/assets/img/" + (page.get("og") or HOME_OG) + ".webp"
    t = html.escape(page["title"], quote=False); m = html.escape(page["meta"], quote=True)
    canon_tag = "" if page["path"] == "404.html" else f'<link rel="canonical" href="{url}">'
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")}">
{canon_tag}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="Jordan River Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{canon(page["path"]) if page["path"] != "404.html" else U + "/"}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14284a">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Overpass:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,700;1,800&family=Overpass+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>'''


def out_path(path, mode):
    if path == "404.html": return "404.html"
    if mode == "preview" and path == "": return "home/index.html"
    return (path + "/" if path else "") + "index.html"


def resolve(doc, page, mode, known):
    here = out_path(page["path"], mode)
    pre = "../" * here.count("/")

    def link(m):
        p = m.group(1)
        frag = ""
        if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
        if p.endswith((".xml", ".txt")): return ("/" + p if mode == "site" else pre + p) + frag
        if p not in known: return U + "/" + p + frag
        if mode == "site": return "/" + p + frag
        return pre + out_path(p, mode) + frag
    doc = re.sub(r'@/([A-Za-z0-9\-_/\.#]*)', link, doc)
    if mode == "site":
        return doc.replace("@img/", "/assets/img/").replace("@root/", "/")
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known):
    draft = '<div class="draft-strip">DRAFT PREVIEW for jordanriverroofing.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() + '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() +
           '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
    if mode == "preview":
        pre = "../" * out_path(page["path"], mode).count("/")
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
    return doc


def main(site_dir, prev_dir):
    from pages import make_pages
    pages = make_pages()
    known = {p["path"] for p in pages}
    for mode, root in (("site", site_dir), ("preview", prev_dir)):
        os.makedirs(os.path.join(root, "assets"), exist_ok=True)
        if mode == "site":
            shutil.copy(os.path.join(HERE, "style.css"), os.path.join(root, "assets", "style.css"))
            shutil.copy(os.path.join(HERE, "site.js"), os.path.join(root, "assets", "site.js"))
        else:
            shutil.copytree(os.path.join(site_dir, "assets", "img"), os.path.join(root, "assets", "img"), dirs_exist_ok=True)
        for pg in pages:
            out = os.path.join(root, out_path(pg["path"], mode))
            os.makedirs(os.path.dirname(out) or root, exist_ok=True)
            open(out, "w", encoding="utf-8", newline="\n").write(render(pg, mode, known))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in pages:
            if pg.get("sitemap", True) and not pg.get("canonical"):
                sm.append(f'  <url><loc>{canon(pg["path"])}</loc><lastmod>{TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    print("built", len(pages), "pages;", sum(1 for p in pages if p.get("canonical")), "canonicalized to a main page")


if __name__ == "__main__":
    main(*sys.argv[1:3])
