"""Builds the amcoroof.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs, titles, meta descriptions and canonicals as the current site.
site/    : files to put live (tracking kept, clean folder links)
preview/ : private review copy (no tracking, links to index.html, forms off, CSS/JS inline)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://www.amcoroof.com/"
BIZ_ID = U + "#organization"
TODAY = "2026-10-16"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

S = {"name": "American Roofing Company", "phone": "801-269-1276", "phone_disp": "(801) 269-1276", "tel": "+18012691276",
     "fax": "801-265-8538", "email": "amco@amcoroof.com", "street": "3637 S 300 W", "city": "South Salt Lake", "st": "UT", "zip": "84115",
     "fb": "https://www.facebook.com/American-Roofing-Company-188355214567379/",
     "li": "https://www.linkedin.com/company/american-roofing-company",
     "bbb": "https://www.bbb.org/us/ut/salt-lake-city/profile/roofing-contractors/american-roofing-company-1126-88030002"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'

TRACK_HEAD = open(os.path.join(HERE, "tracking_head.html"), encoding="utf-8").read()
TRACK_BODY = open(os.path.join(HERE, "tracking_body.html"), encoding="utf-8").read()


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": ["Organization", "RoofingContractor"], "@id": BIZ_ID, "name": S["name"], "url": U,
         "telephone": S["phone"], "email": S["email"],
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"],
                     "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"}}
    if full:
        n.update({"faxNumber": S["fax"], "foundingDate": "1954",
                  "logo": U + "assets/img/american-roofing-logo.png", "image": U + "assets/img/roof-work-in-utah-winter.webp",
                  "geo": {"@type": "GeoCoordinates", "latitude": 40.6922874, "longitude": -111.8993327},
                  "areaServed": [{"@type": "AdministrativeArea", "name": a} for a in ["Salt Lake County, UT", "Davis County, UT", "Utah County, UT"]]
                  + [{"@type": "City", "name": c} for c in ["Ogden, UT", "Park City, UT", "Tooele, UT"]],
                  "sameAs": [S["fb"], S["li"], S["bbb"]]})
    return n


def crumbs_ld(url, trail):
    return {"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(n), "item": U + p} for i, (n, p) in enumerate(trail)]}


def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": html.unescape(q),
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", " ", a)).strip()}} for q, a in faqs]}


def crumbs_html(trail):
    out = []
    for i, (n, p) in enumerate(trail):
        out.append(f'<li aria-current="page">{n}</li>' if i == len(trail) - 1 else f'<li><a href="@/{p}">{n}</a></li>')
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">' + "".join(out) + "</ol></nav>"


def faq_html(faqs):
    return '<div class="faq">' + "".join(
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a">{a}</div></details>' for i, (q, a) in enumerate(faqs)) + "</div>"


def quotes_html(tests, title="What our clients are saying"):
    if not tests: return ""
    cards = []
    for i, (q, a) in enumerate(tests[:5]):
        big = " big" if i == 0 else ""
        cards.append(f'<figure class="quote{big} reveal"><div class="stars" aria-hidden="true">★★★★★</div><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>')
    return f'<section class="sec white"><div class="wrap"><div class="head reveal"><p class="label">Reviews</p><h2>{title}</h2></div><div class="quotes">{"".join(cards)}</div></div></section>'


SERVICES_NAV = [
    ("Repairs", [("Roof Repairs", "services/roof-repairs/"), ("Roof Leak Repair", "services/roof-leak-repair-service/"),
                 ("Storm Damage Repair", "services/storm-damage-repair/"), ("Hail Damage Repair", "services/hail-damage-roof-repair/"),
                 ("Emergency Roofing", "services/emergency-roofing-utah/"), ("Roof Maintenance", "services/roof-maintenance-in-utah/"),
                 ("Historic Roof Repair", "services/historic-roof-repair/")]),
    ("Roofing systems", [("Roof Replacements", "services/roof-replacements/"), ("Asphalt Shingles", "services/asphalt-shingles/"),
                 ("Metal Roofing", "services/metal-roofing-services-utah/"), ("Flat Roof Installation", "flat-roof-installation-in-utah/"),
                 ("Single-Ply Membranes", "services/single-ply-membranes/"), ("Built-Up Roofing", "services/built-up-roofing/"),
                 ("Roof Coatings", "services/roof-coatings/")]),
    ("More", [("Rain Gutters", "services/rain-gutters/"), ("Soffit &amp; Fascia", "services/soffit-and-fascia/"),
              ("Dumpster Service", "services/dumpster-service/"), ("Insurance Claim Process", "services/roof-insurance-claim-process/"),
              ("Roofer Financing", "services/affordable-roofer-financing/"), ("Free Roofing Estimates", "free-roofing-estimates/")]),
]
ROOFS_NAV = [("Residential", "residential/"), ("Commercial", "commercial/"), ("Apartment Roof Repair", "apartment-roof-repair/"),
             ("Apartment Roof Replacement", "apartment-roof-replacement/"), ("Condo Roof Repair", "condo-roof-repair/"),
             ("Condo Roof Replacement", "condo-roof-replacement/")]
ABOUT_NAV = [("About Us", "about-us/"), ("Why Choose Us", "about-us/why-choose-us/"), ("Meet the Team", "meet-the-team/"),
             ("Certifications", "about-us/certified-roofing-contractor/"), ("Case Studies", "case-study/"),
             ("Your Local Roofing Company", "about-us/your-local-roofing-company/"), ("Mission Statement", "about-us/mission-statement/")]


def header():
    svc = "".join(f'<div><h5>{g}</h5>' + "".join(f'<a href="@/{p}">{l}</a>' for l, p in items) + "</div>" for g, items in SERVICES_NAV)
    roofs = "".join(f'<a href="@/{p}">{l}</a>' for l, p in ROOFS_NAV)
    about = "".join(f'<a href="@/{p}">{l}</a>' for l, p in ABOUT_NAV)
    msvc = "".join(f'<a href="@/{p}">{l}</a>' for _, items in SERVICES_NAV for l, p in items)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{S["name"]} home">{img("american-roofing-logo", "American Roofing Company, since 1954", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Roofs We Service</summary><div class="drop">{roofs}</div></details></li>
<li><details><summary>Services</summary><div class="drop wide" style="grid-template-columns:repeat(3,minmax(190px,1fr));min-width:680px">{svc}</div></details></li>
<li><details><summary>About</summary><div class="drop">{about}</div></details></li>
<li><a href="@/service-area/">Service Areas</a></li>
<li><a href="@/blog/">Blog</a></li>
</ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call for a free estimate</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/request-free-quote/">Request Free Quote {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/residential/">Roofs we service</a><div class="sub">{roofs}</div>
<a href="@/services/roof-repairs/">Services</a><div class="sub">{msvc}</div>
<a href="@/about-us/">About</a><div class="sub">{about}</div>
<a href="@/service-area/">Service areas</a><a href="@/blog/">Blog</a><a href="@/glossary/">Glossary</a>
<a class="btn" href="@/request-free-quote/">Request Free Quote {ARROW}</a></div></details>
</div></header>'''


def footer():
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>'
    li = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>'
    col = lambda items: "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in items)
    return f'''<footer class="site-footer"><div class="stripe"></div><div class="wrap foot-top"><p class="foot-say">On Utah roofs <span>since 1954.</span></p><a class="btn" href="@/request-free-quote/">Request a Free Quote {ARROW}</a></div><div class="wrap foot">
<div>{img("american-roofing-logo", "American Roofing Company logo", cls="logo")}
<p style="margin-top:18px;max-width:34ch">One of Utah's oldest roofing companies. Residential, commercial, apartment and condo roofing across the Wasatch Front since 1954.</p>
<div class="socials"><a href="{S["fb"]}" rel="noopener" aria-label="Facebook">{fb}</a><a href="{S["li"]}" rel="noopener" aria-label="LinkedIn">{li}</a></div></div>
<div><h3>Roofs we service</h3><ul>{col(ROOFS_NAV)}</ul></div>
<div><h3>Company</h3><ul>{col(ABOUT_NAV[:5])}<li><a href="@/service-area/">Service Areas</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/glossary/">Glossary</a></li><li><a href="@/privacy-policy/">Privacy Policy</a></li></ul></div>
<div><h3>Contact</h3><address><strong style="color:#fff">{S["name"]}</strong><br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p style="margin:14px 0 4px"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></p>
<p style="margin:0">Fax: {S["fax"]}<br><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
</div><div class="wrap fbottom"><span>&copy; Copyright 2026 American Roofing. All rights reserved.</span><span><a href="@/request-free-quote/">Free quote</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call Now</a><a href="@/request-free-quote/">Free Quote</a></div>'''


def cta(title="Get a straight answer about your roof.", text="Free roof evaluation. We'll explain what we find, and if it can be repaired, we won't sell you a replacement."):
    return f'''<section class="cta">{img("utah-roofing-service-areas", "Utah valley neighborhood below the mountains")}
<div class="wrap"><div class="reveal"><p class="label light">Free estimates</p><h2>{title}</h2><p class="lede" style="margin-top:14px">{text}</p></div>
<div class="reveal"><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a><div class="btn-row" style="margin-top:22px"><a class="btn" href="@/request-free-quote/">Request a Free Quote {ARROW}</a><a class="btn ghost" href="@/service-area/">Service Areas</a></div></div></div></section>'''


def side(links, promise=True):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    pr = img("repair-first-promise", "Our Repair-First Promise: if repairable, we won't sell a replacement") if promise else ""
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Free roof evaluation</p><h3>Talk to a Utah roofer</h3>
<p>Complete project pricing before anything is scheduled.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn" href="@/request-free-quote/">Request Free Quote {ARROW}</a>{pr}</div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero">{img(image, alt, priority=True)}<div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row" style="margin-top:26px"><a class="btn" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a><a class="btn ghost" href="@/request-free-quote/">Free Quote {ARROW}</a></div></div></section>'''


def quote_form(title="Schedule your free roof evaluation"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-first">First name<input id="f-first" name="first" autocomplete="given-name"></label><label for="f-company">Company<input id="f-company" name="company" autocomplete="organization"></label></div>
<div class="row"><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label></div>
<div class="row"><label for="f-street">Street address<input id="f-street" name="street" autocomplete="street-address"></label><label for="f-city">City<input id="f-city" name="city" autocomplete="address-level2"></label></div>
<button class="btn" type="submit">Submit {ARROW}</button>
<p class="note">* Required. We'll call to set up a time that works for you.</p></form>'''


def head(page):
    url = U + page["path"]
    graph = [biz(page.get("full_biz", True)),
             {"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", "roof-work-in-utah-winter") + ".webp"
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
<meta property="og:site_name" content="American Roofing Company">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#13284d">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Instrument+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
@@TRACK_HEAD@@
<script type="application/ld+json">
{ld}
</script>
</head>'''


def resolve(doc, page, mode, known, redirects):
    depth = page["path"].count("/") if not page["path"].endswith(".html") else page["path"].count("/")
    pre = "../" * depth

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
    draft = '<div class="draft-strip">DRAFT PREVIEW for amcoroof.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + ("@@TRACK_BODY@@\n" if mode == "site" else "") + draft + header() +
           '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() + '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known, redirects)
    if mode == "site":
        doc = doc.replace("@@TRACK_HEAD@@", TRACK_HEAD.strip()).replace("@@TRACK_BODY@@", TRACK_BODY.strip())
    else:
        depth = page["path"].count("/")
        pre = "../" * depth
        doc = doc.replace("@@TRACK_HEAD@@\n", "")
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
        if page["path"] == "":
            doc = re.sub(r'(?s)^<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', doc)
            doc = doc.replace('<meta charset="utf-8">\n', '').replace('<meta name="viewport" content="width=device-width, initial-scale=1">\n', '')
            doc = re.sub(r'<title>.*?</title>', '<title>American Roofing Redesign</title>', doc, count=1)
            doc = re.sub(r'</head>\s*<body>\s*', '\n', doc)
            doc = re.sub(r'\s*</body>\s*</html>\s*$', '\n', doc)
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
    json.dump(redirects, open(os.path.join(HERE, "redirects.json"), "w"), indent=1)
    print("built", len(pages), "pages;", len(redirects), "redirects kept out")


if __name__ == "__main__":
    main(*sys.argv[1:4])
