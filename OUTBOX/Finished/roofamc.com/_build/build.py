"""Builds the roofamc.com redesign.

  python -I build.py <out_site> <out_preview>

Two builds come out of one source:
  site/     - the files to put live. Links are clean folder URLs (../roof-repair/),
              the same URLs and canonicals the current WordPress site uses.
  preview/  - the private review copy. Same pages, but links point at index.html
              files so they work inside the preview host, forms are off and a draft
              strip sits on top.
"""
import json, os, re, shutil, sys, html

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

SITE = {
    "name": "Advanced Roofing & Moisture Control",
    "legal": "Advanced Roofing & Moisture Control, Inc.",
    "url": "https://roofamc.com",
    "phone": "(801) 326-9708", "tel": "+18013269708",
    "emerg": "(801) 671-2282", "emerg_tel": "+18016712282",
    "email": "info@roofamc.com",
    "street": "2212 South West Temple #31",
    "city": "Salt Lake City", "state": "Utah", "st": "UT", "zip": "84115",
    "hours": "Mon–Sat, 9 am – 5 pm",
    "facebook": "https://www.facebook.com/p/Advanced-Roofing-and-Moisture-Control-100063747680394/",
    "yelp": "https://www.yelp.com/biz/advanced-moisture-control-salt-lake-city",
    "bbb": "https://www.bbb.org/us/ut/salt-lake-city/profile/waterproofing-contractors/advanced-roofing-moisture-control-inc-1166-90012980/addressId/95966",
    "maps": "https://www.google.com/maps/search/?api=1&query=2212+South+West+Temple+%2331+Salt+Lake+City+UT+84115",
}
BIZ_ID = SITE["url"] + "/#business"
TODAY = "2026-10-16"
IMG_META = json.load(open(os.path.join(HERE, "imgmeta.json")))

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'


def img(name, alt, cls="", lazy=True, sizes=None, priority=False):
    w, h, _ = IMG_META[name]
    attrs = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: attrs.append(f'class="{cls}"')
    if priority: attrs.append('fetchpriority="high"')
    elif lazy: attrs.append('loading="lazy"')
    attrs.append('decoding="async"')
    return "<img " + " ".join(attrs) + ">"


def biz_node(full=True):
    node = {
        "@type": "RoofingContractor", "@id": BIZ_ID,
        "name": SITE["name"], "legalName": SITE["legal"],
        "url": SITE["url"] + "/",
        "telephone": "+1-801-326-9708", "email": SITE["email"],
        "address": {"@type": "PostalAddress", "streetAddress": SITE["street"],
                    "addressLocality": SITE["city"], "addressRegion": SITE["st"],
                    "postalCode": SITE["zip"], "addressCountry": "US"},
    }
    if full:
        node.update({
            "logo": SITE["url"] + "/assets/img/logo-advanced-roofing-moisture-control.png",
            "image": SITE["url"] + "/assets/img/white-flat-roof-wasatch-mountains.webp",
            "description": "Licensed, insured roofing contractor in Salt Lake City for residential and commercial roofing, roof repair, waterproofing and pond liner installation.",
            "geo": {"@type": "GeoCoordinates", "latitude": 40.7301, "longitude": -111.8969},
            "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                "opens": "09:00", "closes": "17:00"}],
            "areaServed": [{"@type": "City", "name": c} for c in
                           ["Salt Lake City, UT", "Park City, UT", "West Jordan, UT", "Sandy, UT", "South Salt Lake, UT"]]
                          + [{"@type": "AdministrativeArea", "name": "Salt Lake County, UT"}],
            "contactPoint": [{"@type": "ContactPoint", "telephone": "+1-801-671-2282", "contactType": "emergency"}],
            "sameAs": [SITE["facebook"], SITE["bbb"], SITE["yelp"]],
        })
    return node


def crumbs_schema(trail):
    return {"@type": "BreadcrumbList", "@id": None, "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE["url"] + "/" + p}
        for i, (n, p) in enumerate(trail)]}


def service_schema(page, name, desc, area=None, faq=None):
    url = SITE["url"] + "/" + page["path"]
    g = [{"@type": "Service", "@id": url + "#service", "name": name, "description": desc,
          "serviceType": name, "provider": {"@id": BIZ_ID}, "url": url,
          "areaServed": area or [{"@type": "City", "name": "Salt Lake City, UT"}]}]
    return g


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}}
        for q, a in faqs]}


def faq_html(faqs, open_first=True):
    out = ['<div class="faq">']
    for i, (q, a) in enumerate(faqs):
        out.append(f'<details{" open" if i == 0 and open_first else ""}><summary>{q}</summary><p>{a}</p></details>')
    out.append("</div>")
    return "\n".join(out)


def crumbs_html(trail):
    items = []
    for i, (n, p) in enumerate(trail):
        if i == len(trail) - 1:
            items.append(f'<li aria-current="page">{n}</li>')
        else:
            items.append(f'<li><a href="@/{p}">{n}</a></li>')
    return '<nav aria-label="Breadcrumb"><ol class="crumbs">' + "".join(items) + "</ol></nav>"


NAV_SERVICES = [("Roof Repair", "roof-repair/"), ("Residential Roofing", "residential/"),
                ("Commercial Roofing", "commercial/"), ("Waterproofing", "waterproofing/"),
                ("Ponds &amp; Water Features", "ponds/")]
NAV_PROJECTS = [("Salt Lake City Projects", "salt-lake-city-commercial-roofing-and-residential-roofing/"),
                ("Park City Projects", "park-city-commercial-roofing-and-waterproofing-solutions/"),
                ("Utah Service Area", "utah-commercial-and-residential-roofers/"),
                ("Our Clients", "clients/")]


def header(active):
    def a(label, p):
        cur = ' aria-current="page"' if p == active else ""
        return f'<a href="@/{p}"{cur}>{label}</a>'
    svc = "".join(a(l, p) for l, p in NAV_SERVICES)
    prj = "".join(a(l, p) for l, p in NAV_PROJECTS)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{SITE["name"]} home">{img("logo-advanced-roofing-moisture-control", SITE["name"] + " logo", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{svc}</div></details></li>
<li><details><summary>Projects</summary><div class="drop">{prj}</div></details></li>
<li>{a("Reviews", "testimonials/")}</li>
<li>{a("Blog", "blog/")}</li>
<li>{a("Contact", "contact/")}</li>
</ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{SITE["tel"]}"><small>Call for a free quote</small><strong>{SITE["phone"]}</strong></a><a class="btn" href="@/get-a-quote/">Get a Quote {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/roof-repair/">Services</a><div class="sub">{svc}</div>
<a href="@/salt-lake-city-commercial-roofing-and-residential-roofing/">Projects</a><div class="sub">{prj}</div>
<a href="@/testimonials/">Reviews</a><a href="@/blog/">Blog</a><a href="@/contact/">Contact</a>
<a class="btn" href="@/get-a-quote/">Get a Free Quote {ARROW}</a>
</div></details>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in NAV_SERVICES)
    prj = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in NAV_PROJECTS)
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>'
    yelp = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M11 2.2 11.4 13c0 .6-.7.9-1.1.4L4.9 6.7c-.4-.5 0-1.3.7-1.3C8 3.6 9.5 2.6 10.2 2.3c.4-.2.8 0 .8-.1zm2.5 12.3 5.3 1.7c.6.2.7 1 .2 1.3-1.4 1.3-2.6 2-3.4 2.3-.5.2-1-.2-1-.7l-.3-4c0-.4.4-.7.8-.6h.4zm-.6-2.2 4.4-3.3c.5-.4 1.2-.1 1.3.5.3 1.6.3 3 .1 3.8-.1.5-.6.8-1.1.6l-4.3-.8c-.6-.1-.8-.5-.4-.8zM11 15.9l-.1 5.5c0 .6-.6 1-1.2.7-1.6-.6-2.8-1.4-3.4-2-.4-.4-.3-1 .2-1.3l3.7-3.4c.4-.3.8 0 .8.5z"/></svg>'
    return f'''<footer class="site-footer"><div class="wrap foot-say-row"><p class="foot-say">Snow isn&rsquo;t the problem. <span>Meltwater is.</span></p><a class="btn" href="@/get-a-quote/">Get a Free Quote {ARROW}</a></div><div class="wrap foot-top">
<div>{img("logo-advanced-roofing-moisture-control", SITE["name"] + " logo")}
<p style="margin-top:20px;max-width:34ch">Roofing, roof repair and waterproofing for homes and commercial buildings in Salt Lake City, Park City and across Utah.</p>
<div class="socials"><a href="{SITE["facebook"]}" rel="noopener" aria-label="Facebook">{fb}</a><a href="{SITE["yelp"]}" rel="noopener" aria-label="Yelp">{yelp}</a></div></div>
<div><h3>Services</h3><ul>{svc}</ul></div>
<div><h3>Projects</h3><ul>{prj}<li><a href="@/testimonials/">Testimonials</a></li><li><a href="@/blog/">Blog</a></li></ul></div>
<div><h3>Contact</h3><address><strong style="color:#fff">{SITE["name"]}</strong><br>{SITE["street"]}<br>{SITE["city"]}, {SITE["state"]} {SITE["zip"]}</address>
<p style="margin:14px 0 4px"><a class="big-phone" href="tel:{SITE["tel"]}">{SITE["phone"]}</a></p>
<p style="margin:0">Emergencies: <a href="tel:{SITE["emerg_tel"]}">{SITE["emerg"]}</a><br><a href="mailto:{SITE["email"]}">{SITE["email"]}</a><br>{SITE["hours"]}</p></div>
</div><div class="wrap foot-bottom"><span>&copy; 2026 {SITE["legal"]}</span><span><a href="@/contact/">Contact</a> &middot; <a href="@/get-a-quote/">Free quote</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></footer>
<div class="callbar"><a href="tel:{SITE["tel"]}">{PHONE} Call Now</a><a href="@/get-a-quote/">Free Quote</a></div>'''


def cta_band(title="Leak, storm damage or an old roof?", text="Call for a free quote. If water is coming in right now, use the emergency line."):
    return f'''<section class="cta">{img("slc-skyline-golden-hour", "Salt Lake City skyline at golden hour with mountains behind")}
<div class="wrap"><div class="reveal"><p class="eyebrow light">Free quotes &middot; {SITE["hours"]}</p><h2>{title}</h2><p class="lede" style="margin-top:16px">{text}</p></div>
<div class="reveal d1"><a class="phone-big" href="tel:{SITE["tel"]}">{SITE["phone"]}</a><p style="margin:14px 0 22px;color:rgba(255,255,255,.8)">Emergencies: <a href="tel:{SITE["emerg_tel"]}" style="color:#fff;font-weight:600">{SITE["emerg"]}</a></p>
<div class="btn-row"><a class="btn" href="@/get-a-quote/">Request a Quote {ARROW}</a><a class="btn ghost" href="@/contact/">Contact Us</a></div></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta"><p class="eyebrow light">Free estimate</p><h3>Talk to a roofer</h3>
<p>Tell us what you're seeing. We'll come look and give you a written quote.</p>
<a class="phone-big" href="tel:{SITE["tel"]}">{SITE["phone"]}</a><p style="margin:0">Emergencies: <a href="tel:{SITE["emerg_tel"]}" style="color:#fff">{SITE["emerg"]}</a></p>
<a class="btn" href="@/get-a-quote/">Get a Quote {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def page_hero(trail, h1, lede, image, alt, eyebrow):
    return f'''<section class="page-hero">{img(image, alt, priority=True)}<span class="diag" aria-hidden="true"></span>
<div class="wrap">{crumbs_html(trail)}<p class="eyebrow light">{eyebrow}</p><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="btn-row" style="margin-top:28px"><a class="btn" href="tel:{SITE["tel"]}">{PHONE} {SITE["phone"]}</a><a class="btn ghost" href="@/get-a-quote/">Free Quote {ARROW}</a></div></div></section>'''


def head(page):
    url = SITE["url"] + "/" + page["path"]
    graph = [biz_node(full=page.get("full_biz", True)),
             {"@type": "WebSite", "@id": SITE["url"] + "/#website", "url": SITE["url"] + "/", "name": SITE["name"], "publisher": {"@id": BIZ_ID}}]
    graph += page.get("schema", [])
    for node in graph:
        if node.get("@type") == "BreadcrumbList" and node.get("@id") is None:
            node["@id"] = url + "#breadcrumb"
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    ogimg = SITE["url"] + "/assets/img/" + page.get("og", "slc-skyline-snowy-wasatch") + ".webp"
    robots = page.get("robots", "index, follow, max-image-preview:large")
    canon = f'<link rel="canonical" href="{url}">' if page.get("canonical", True) else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{page["title"]}</title>
<meta name="description" content="{page["meta"]}">
<meta name="robots" content="{robots}">
{canon}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="{SITE["name"]}">
<meta property="og:title" content="{page["title"]}">
<meta property="og:description" content="{page["meta"]}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#14231a">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Anton&family=Figtree:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>'''


def render(page, mode):
    depth = page["path"].count("/") if page["path"] != "404.html" else 0
    pre = "../" * depth
    body = page["body"]
    doc = (head(page) + "\n<body>\n" +
           (('<div class="draft-strip">DRAFT PREVIEW for roofamc.com &middot; made by Novarte AI for review &middot; not the live site</div>\n') if mode == "preview" else "") +
           header(page.get("active", page["path"])) + '\n<main id="main">\n' + body + "\n</main>\n" + footer() +
           f'\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')

    def link(m):
        p = m.group(1)
        if p.endswith(".xml") or p.endswith(".html"):
            return pre + p
        if mode == "preview":
            return pre + (p or "home/") + "index.html"  # preview: site home lives in home/, the review page is the root
        return (pre + p) or "./"
    doc = re.sub(r'@/([a-z0-9\-/\.]*)', link, doc)
    doc = doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)
    if mode == "preview":
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        NL = "\n"
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>" + NL + css + NL + "</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>" + NL + js + NL + "</script>")
        if page["path"] == "":
            # the preview host adds its own doctype/html/head/body around the main page
            doc = re.sub(r'(?s)^<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', doc)
            doc = doc.replace('<meta charset="utf-8">' + NL, '').replace('<meta name="viewport" content="width=device-width, initial-scale=1">' + NL, '')
            doc = re.sub(r'</head>\s*<body>\s*', NL, doc)
            doc = re.sub(r'\s*</body>\s*</html>\s*$', NL, doc)
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = doc.replace('<button class="btn" type="submit">', '<button class="btn" type="button" disabled>')
        doc = re.sub(r'(<button class="btn" type="button" disabled>)[^<]*', r'\1Form is off in this preview ', doc)
    return doc


def out_path(root, page):
    if page["path"] == "404.html":
        return os.path.join(root, "404.html")
    return os.path.join(root, page["path"], "index.html")


def main(site_dir, prev_dir):
    from pages import PAGES
    for mode, root in (("site", site_dir), ("preview", prev_dir)):
        os.makedirs(os.path.join(root, "assets"), exist_ok=True)
        shutil.copy(os.path.join(HERE, "style.css"), os.path.join(root, "assets", "style.css"))
        shutil.copy(os.path.join(HERE, "site.js"), os.path.join(root, "assets", "site.js"))
        if root != site_dir:
            shutil.copytree(os.path.join(site_dir, "assets", "img"), os.path.join(root, "assets", "img"), dirs_exist_ok=True)
        for page in PAGES:
            if mode == "preview" and page["path"] == "": page = dict(page, path="home/")
            p = out_path(root, page)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            open(p, "w", encoding="utf-8", newline="\n").write(render(page, mode))
        # sitemap + robots
        urls = [pg for pg in PAGES if pg.get("sitemap", True)]
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in urls:
            sm.append(f'  <url><loc>{SITE["url"]}/{pg["path"]}</loc><lastmod>{pg.get("modified", TODAY)}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    print("built", len(PAGES), "pages")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
