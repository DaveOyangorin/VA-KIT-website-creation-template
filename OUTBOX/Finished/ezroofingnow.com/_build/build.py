"""Builds the ezroofingnow.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs, canonicals and page purposes as the current site.
site/    : files to put live (Google tag, GA4, Google Ads, Meta Pixel and CallRail kept; clean folder links)
preview/ : private review copy (no tracking, links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://ezroofingnow.com/"
BIZ_ID = U + "#organization"
UT_ID, AR_ID = U + "#utah", U + "#arkansas"
TODAY = "2026-10-17"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

# Copied exactly from the footer of the current site (17 Oct 2026). The Utah block matches the Google profile.
S = {"name": "EZ Roofing", "legal": "EZ Contracting LLC", "email": "info@ezroofingnow.com", "hours": "Daily 9:00am – 5:00pm",
     "license": "#0428111225",
     "ut": {"name": "EZ Roofing Utah", "street": "357 S 200 E, #205", "city": "Salt Lake City", "st": "UT", "zip": "84111",
            "phone": "(888) 575-3025", "tel": "+18885753025"},
     "ar": {"name": "EZ Roofing Arkansas", "street": "13 Nalley Road, #C", "city": "Cabot", "st": "AR", "zip": "72023",
            "phone": "(501) 691-4283", "tel": "+15016914283"},
     "emergency": "(501) 462-5371", "emergency_tel": "+15014625371"}
# Phone numbers on the live site are swapped by CallRail for tracking. The base numbers above are the ones printed
# in the footer; CallRail (kept in tracking_head.html) keeps swapping them on the live build.

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'

TRACK_HEAD = open(os.path.join(HERE, "tracking_head.html"), encoding="utf-8").read()
TRACK_BODY = open(os.path.join(HERE, "tracking_body.html"), encoding="utf-8").read()
CONTACT = "contact/"
INSPECT = "our-free-inspection/"


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def loc_node(k, nid):
    L = S[k]
    return {"@type": "RoofingContractor", "@id": nid, "name": L["name"], "url": U, "telephone": L["phone"], "email": S["email"],
            "parentOrganization": {"@id": BIZ_ID},
            "address": {"@type": "PostalAddress", "streetAddress": L["street"], "addressLocality": L["city"], "addressRegion": L["st"],
                        "postalCode": L["zip"], "addressCountry": "US"},
            "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                          "opens": "09:00", "closes": "17:00"},
            "areaServed": {"@type": "State", "name": "Utah" if k == "ut" else "Arkansas"}}


def biz(full=True):
    org = {"@type": "Organization", "@id": BIZ_ID, "name": S["name"], "legalName": S["legal"], "url": U, "email": S["email"],
           "logo": U + "assets/img/ez-roofing-logo.png", "foundingDate": "2017",
           "subOrganization": [{"@id": UT_ID}, {"@id": AR_ID}]}
    if not full: return [org]
    org.update({"description": "EZ Roofing is a family owned roofing and exterior contractor with local teams in Salt Lake City, Utah and Cabot, Arkansas: roof repair and replacement, storm damage, free inspections, siding, windows and doors.",
                "knowsAbout": ["Roof repair", "Roof replacement", "Storm damage roofing", "Roof inspection", "Commercial roofing", "Stone coated steel roofing", "Siding", "Windows", "Doors"]})
    return [org, loc_node("ut", UT_ID), loc_node("ar", AR_ID)]


def crumbs_ld(url, trail):
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub(r"<[^>]+>", "", n)), "item": U + p} for i, (n, p) in enumerate(trail)]}


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


def quotes_html(tests, title="What homeowners say"):
    if not tests: return ""
    cards = "".join(f'<figure class="quote{" big" if i == 0 else ""} reveal"><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
                    for i, (q, a) in enumerate(tests[:5]))
    return f'<section class="sec white"><div class="wrap"><div class="head reveal"><p class="label">Reviews</p><h2>{title}</h2></div><div class="quotes">{cards}</div></div></section>'


MENU = [
    ("Residential", [("Our free inspection", "our-free-inspection/"), ("Storm damage", "roof-storm-damage/"), ("New roof", "get-a-new-roof/"),
                     ("Stone coated steel", "stone-coated-steel-roofing/"), ("Shingle repair", "shingle-roof-repair-in-utah-and-arkansas/"),
                     ("RV roofing", "rv-roofing/"), ("Christmas lights", "lights/")]),
    ("Commercial", [("Commercial roofing", "commercial-roofing-services/"), ("Single-ply commercial roofing", "commercial-roof/"),
                    ("Apartment roofing", "apartments/"), ("Pre-cast concrete", "pre-cast-concrete/")]),
    ("Locations", [("Salt Lake City, Utah", "utah-city/salt-lake-city/"), ("All Utah cities", "utah-city/"), ("Utah services", "utah/"),
                   ("Cabot, Arkansas", "arkansas-city/cabot/"), ("All Arkansas cities", "arkansas-city/"), ("Arkansas services", "arkansas/")]),
    ("About", [("About EZ Roofing", "about-ez-roofing/"), ("Our process", "the-ez-process/"), ("Meet our team", "ez-roofing-team/"),
               ("Customer reviews", "roofing-reviews-salt-lake-city/"), ("Welcome Home Guarantee", "welcome-home-guarantee/"),
               ("Financing", "financing/"), ("Projects", "projects/"), ("Blog", "ez-roofing-blog/")]),
]


def header():
    nav = ""
    mob = ""
    for top, items in MENU:
        links = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span>{l}</a>' for i, (l, p) in enumerate(items))
        nav += f'<li><details><summary>{top}</summary><div class="drop">{links}</div></details></li>'
        mob += f'<p class="mh">{top}</p><div class="sub">{links}</div>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="EZ Roofing home">{img("ez-roofing-logo", "EZ Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>{nav}<li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["ut"]["tel"]}"><small>Utah &middot; Arkansas {S["ar"]["phone"]}</small><strong>{S["ut"]["phone"]}</strong></a><a class="btn" href="@/{INSPECT}">Free Inspection {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{INSPECT}">Schedule a Free Inspection {ARROW}</a></div></details>
</div></header>'''


def footer():
    def loc(k):
        L = S[k]
        return f'<p class="fname">{L["name"]}</p><address>{L["street"]}<br>{L["city"]}, {L["st"]} {L["zip"]}</address><p><a class="fphone" href="tel:{L["tel"]}">{L["phone"]}</a></p>'
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Every roof starts with <span>a free evaluation.</span></p><a class="btn" href="@/{INSPECT}">Schedule a Free Inspection {ARROW}</a></div>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("ez-roofing-logo", "EZ Roofing logo", cls="logo")}</span>
<p>Family owned and operated since 2017. Roofing, siding, windows and doors, with local teams in Utah and Arkansas.</p>
<p class="small">Licensed, bonded &amp; insured in Utah and Arkansas. License number {S["license"]}.</p>
<div class="emerg"><b>Emergency?</b> Call or text <a href="tel:{S["emergency_tel"]}">{S["emergency"]}</a> for 24-hour emergency service.</div></div>
<div><h3>Services</h3><ul><li><a href="@/our-free-inspection/">Free roof inspection</a></li><li><a href="@/roof-storm-damage/">Storm damage</a></li><li><a href="@/get-a-new-roof/">New roof</a></li><li><a href="@/shingle-roof-repair-in-utah-and-arkansas/">Shingle repair</a></li><li><a href="@/stone-coated-steel-roofing/">Stone coated steel</a></li><li><a href="@/commercial-roofing-services/">Commercial roofing</a></li><li><a href="@/financing/">Financing</a></li></ul></div>
<div><h3>Salt Lake City</h3><ul><li><a href="@/utah-city/salt-lake-city/">Roofing in Salt Lake City</a></li><li><a href="@/utah/salt-lake-city-roof-repair/">Roof repair</a></li><li><a href="@/utah/salt-lake-city-roof-replacement/">Roof replacement</a></li><li><a href="@/utah/salt-lake-city-roof-installation/">Roof installation</a></li><li><a href="@/utah/salt-lake-city-free-roof-inspection/">Roof inspection</a></li><li><a href="@/utah/salt-lake-city-commercial-roofing/">Commercial roofing</a></li><li><a href="@/utah-city/">All Utah cities</a></li><li><a href="@/arkansas-city/">All Arkansas cities</a></li></ul></div>
<div><h3>Contact</h3>{loc("ut")}{loc("ar")}<p><a href="mailto:{S["email"]}">{S["email"]}</a><br>Hours: {S["hours"]}</p></div>
</div><div class="fbottom"><span>&copy; 2026 EZ Roofing &middot; {S["legal"]}</span><span><a href="@/privacy-policy-terms-conditions/">Privacy Policy</a> &middot; <a href="@/sms-terms/">SMS Terms</a> &middot; <a href="@/careers/">Careers</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["ut"]["tel"]}">{PHONE} Call Utah</a><a href="@/{INSPECT}">Free Inspection</a></div>'''


def cta(title="Book your free roof inspection", text="We look at the whole roof, plus soffit, fascia, gutters, windows and siding, and tell you what we find. No cost, no obligation.", image="king-2-1"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap"><div class="reveal"><p class="label light">Free property evaluation</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-locs"><a href="tel:{S["ut"]["tel"]}"><small>Utah &middot; Salt Lake City</small><b>{S["ut"]["phone"]}</b></a><a href="tel:{S["ar"]["tel"]}"><small>Arkansas &middot; Cabot</small><b>{S["ar"]["phone"]}</b></a>
<a class="btn" href="@/{INSPECT}">Schedule a Free Inspection {ARROW}</a></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Free inspection</p><h3>Not sure what your roof needs?</h3>
<p>Start with a free, in-person property evaluation.</p><a class="phone" href="tel:{S["ut"]["tel"]}">{S["ut"]["phone"]}</a><p class="small">Arkansas: <a href="tel:{S["ar"]["tel"]}">{S["ar"]["phone"]}</a></p>
<a class="btn" href="@/{INSPECT}">Schedule an Inspection {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero"><div class="ph-bg">{img(image, alt, priority=True)}</div><div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Free Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["ut"]["tel"]}">{PHONE} {S["ut"]["phone"]}</a></div></div></section>'''


def quote_form(title="Schedule your free inspection"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-region">Region *<select id="f-region" name="region" required><option value="">Select region</option><option>Utah</option><option>Arkansas</option></select></label></div>
<label for="f-addr">Property address *<input id="f-addr" name="address" autocomplete="street-address" required></label>
<div class="row"><label for="f-type">Project type *<select id="f-type" name="type" required><option value="">Choose one</option><option>Roof Replacement</option><option>Roof Repair</option><option>Storm Damage Roof Inspection</option><option>Christmas Lights</option></select></label>
<label for="f-time">Preferred time<select id="f-time" name="time"><option value="">Any time</option><option>9AM-11AM</option><option>11AM-1PM</option><option>1PM-3PM</option><option>3PM-5PM</option></select></label></div>
<label class="consent"><input type="checkbox" name="sms"><span>Yes, text me updates. By checking this box, I consent to receive text messages related to my project from EZ Contracting LLC EZ Roofing &amp; Restoration. Message and data rates may apply. Reply STOP to opt-out, HELP for help. Message frequency may vary. See our <a href="@/privacy-policy-terms-conditions/">Privacy Policy</a> and <a href="@/sms-terms/">SMS Terms &amp; Conditions</a>.</span></label>
<button class="btn" type="submit">Book Now {ARROW}</button>
<p class="note">* Required.</p></form>'''


def head(page):
    url = U + page["path"]
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", "dji-20260219105641-0157-d") + ".webp"
    t = html.escape(page["title"], quote=False); m = html.escape(page["meta"], quote=True)
    canon = f'<link rel="canonical" href="{page["canonical"]}">' if page.get("canonical") else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")}">
{canon}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="EZ Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#681214">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..100,600..900&family=Source+Sans+3:wght@400;600;700&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
@@TRACK_HEAD@@
<script type="application/ld+json">
{ld}
</script>
</head>'''


def resolve(doc, page, mode, known, redirects):
    pre = "../" * page["path"].count("/")

    def link(m):
        p = m.group(1)
        frag = ""
        if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
        if p.endswith((".xml", ".txt", ".html")): return pre + p + frag
        p = redirects.get(p, p)
        if p not in known:
            return U + p + frag  # page that is not part of this build: point at the live URL
        if mode == "preview": return pre + (p or "home/") + "index.html" + frag  # preview: site home lives in home/, the review page is the root
        return (pre + p or "./") + frag
    doc = re.sub(r'@/([A-Za-z0-9\-/\._#]*)', link, doc)
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known, redirects):
    draft = '<div class="draft-strip">DRAFT PREVIEW for ezroofingnow.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + ("@@TRACK_BODY@@\n" if mode == "site" else "") + draft + header() +
           '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() + '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known, redirects)
    if mode == "site":
        doc = doc.replace("@@TRACK_HEAD@@", TRACK_HEAD.strip()).replace("@@TRACK_BODY@@", TRACK_BODY.strip())
    else:
        pre = "../" * page["path"].count("/")
        doc = doc.replace("@@TRACK_HEAD@@\n", "")
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
    return doc


def main(ex_path, site_dir, prev_dir):
    from pages import make_pages
    pages, redirects = make_pages(json.load(open(ex_path, encoding="utf-8")))
    known = {p["path"] for p in pages}
    for mode, root in (("site", site_dir), ("preview", prev_dir)):
        os.makedirs(os.path.join(root, "assets"), exist_ok=True)
        if mode == "site":
            shutil.copy(os.path.join(HERE, "style.css"), os.path.join(root, "assets", "style.css"))
            shutil.copy(os.path.join(HERE, "site.js"), os.path.join(root, "assets", "site.js"))
        else:
            shutil.copytree(os.path.join(site_dir, "assets", "img"), os.path.join(root, "assets", "img"), dirs_exist_ok=True)
        for pg in pages:
            if mode == "preview" and pg["path"] == "": pg = dict(pg, path="home/")
            out = os.path.join(root, "404.html") if pg["path"] == "404.html" else os.path.join(root, pg["path"], "index.html")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8", newline="\n").write(render(pg, mode, known, redirects))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in pages:
            if pg.get("sitemap", True):
                sm.append(f'  <url><loc>{pg["canonical"]}</loc><lastmod>{pg.get("modified") or TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    # preview: drop images no page uses, so the artifact stays under its file limit
    used = {"ez-roofing-logo.png", "favicon.png"}
    for dp, _, fs in os.walk(prev_dir):
        for f in fs:
            if f.endswith(".html"): used |= set(re.findall(r"assets/img/([\w.-]+)", open(os.path.join(dp, f), encoding="utf-8").read()))
    imgdir = os.path.join(prev_dir, "assets", "img")
    for f in os.listdir(imgdir):
        if f not in used: os.remove(os.path.join(imgdir, f))
    json.dump(redirects, open(os.path.join(HERE, "redirects.json"), "w"), indent=1)
    print("built", len(pages), "pages;", len(redirects), "redirects kept out")


if __name__ == "__main__":
    main(*sys.argv[1:4])
