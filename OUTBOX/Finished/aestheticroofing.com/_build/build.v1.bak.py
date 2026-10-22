"""Builds the aestheticroofing.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs, titles, meta descriptions and canonicals as the current site.
site/    : files to put live (tracking kept, clean folder links)
preview/ : private review copy (no tracking, links to index.html, forms off, CSS/JS inline)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://www.aestheticroofing.com/"
BIZ_ID = U + "#organization"
TODAY = "2026-10-16"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

S = {"name": "Aesthetic Roofing", "phone": "(801) 810-2276", "tel": "+18018102276", "email": "office@aestheticroofing.com",
     "street": "10653 S River Front Pkwy, Ste 250", "city": "South Jordan", "st": "UT", "zip": "84095",
     "fb": "https://www.facebook.com/aestheticroofingllc/", "ig": "https://www.instagram.com/aesthetic.roofing/",
     "yt": "https://www.youtube.com/@AestheticRoofing", "li": "https://www.linkedin.com/company/aesthetic-roofing-utah/",
     "bbb": "https://www.bbb.org/us/ut/south-jordan/profile/roofing-contractors/aesthetic-roofing-llc-1126-90040819/addressId/938339"}

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
        n.update({"logo": U + "assets/img/aesthetic-roofing-logo-dark.png", "image": U + "assets/img/aerial-new-roof-neighborhood.webp",
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + " County, UT"} for c in
                                 ["Utah", "Salt Lake", "Tooele", "Wasatch", "Summit", "Morgan", "Davis", "Weber", "Box Elder", "Cache", "Rich"]],
                  "hasCredential": {"@type": "EducationalOccupationalCredential", "name": "GAF Master Elite Contractor"},
                  "sameAs": [S["fb"], S["ig"], S["yt"], S["li"], S["bbb"]]})
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
    ("Services", [("Roof Replacement", "services/roof-replacement/"), ("Roof Repair", "services/roof-repair/"),
                  ("Storm Damage Roof Repair", "services/storm-damage-roof-repair/"), ("Roof Inspection", "services/roof-inspection/"),
                  ("Gutter Replacement", "services/gutter-replacement/"), ("Gutter Services", "services/gutter-services/")]),
    ("Roof types", [("Asphalt Shingle", "roof-types/asphalt-shingle/"), ("Designer Asphalt", "roof-types/designer-asphalt-roofing/"),
                    ("Metal Roofing", "roof-types/metal-roofing/"), ("Flat Roofing", "roof-types/flat-roofing/"), ("All Roof Types", "roof-types/")]),
]
ROOFS_NAV = [("Salt Lake County", "service-areas/salt-lake-county-ut/"), ("Utah County", "service-areas/utah-county-ut/"), ("All Service Areas", "service-areas/")]
ABOUT_NAV = [("About Us", "about/"), ("Projects", "projects/"), ("Financing", "financing/"), ("Blog", "blog/"), ("Contact", "contact/")]


def header():
    svc = "".join(f'<div><h5>{g}</h5>' + "".join(f'<a href="@/{p}">{l}</a>' for l, p in items) + "</div>" for g, items in SERVICES_NAV)
    areas = "".join(f'<a href="@/{p}">{l}</a>' for l, p in ROOFS_NAV)
    msvc = "".join(f'<a href="@/{p}">{l}</a>' for _, items in SERVICES_NAV for l, p in items)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>New roof in a day &middot; Flexible payments &middot; South Jordan, UT</span><span>Free Roof Health Report: <a href="tel:{S["tel"]}">{S["phone"]}</a></span></div></div>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{S["name"]} home">{img("aesthetic-roofing-logo-white", "Aesthetic Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop wide">{svc}</div></details></li>
<li><details><summary>Service Areas</summary><div class="drop">{areas}</div></details></li>
<li><a href="@/projects/">Projects</a></li>
<li><a href="@/financing/">Financing</a></li>
<li><a href="@/about/">About</a></li>
<li><a href="@/blog/">Blog</a></li>
</ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call or text</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/contact/">Book Online {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/services/">Services</a><div class="sub">{msvc}</div>
<a href="@/service-areas/">Service areas</a><div class="sub">{areas}</div>
<a href="@/projects/">Projects</a><a href="@/financing/">Financing</a><a href="@/about/">About</a><a href="@/blog/">Blog</a><a href="@/contact/">Contact</a>
<a class="btn" href="@/contact/">Book Online {ARROW}</a></div></details>
</div></header>'''


def footer():
    ic = {"fb": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>',
          "ig": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 7a5 5 0 1 0 0 10 5 5 0 0 0 0-10zm0 8.2a3.2 3.2 0 1 1 0-6.4 3.2 3.2 0 0 1 0 6.4zM17.3 5.5a1.2 1.2 0 1 0 0 2.4 1.2 1.2 0 0 0 0-2.4zM12 2c-2.7 0-3.1 0-4.1.1-4 .2-5.7 1.9-5.9 5.9C2 9 2 9.3 2 12s0 3.1.1 4.1c.2 4 1.9 5.7 5.9 5.9 1 .1 1.4.1 4.1.1s3.1 0 4.1-.1c4-.2 5.7-1.9 5.9-5.9.1-1 .1-1.4.1-4.1s0-3.1-.1-4.1c-.2-4-1.9-5.7-5.9-5.9C15.1 2 14.7 2 12 2z"/></svg>',
          "yt": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.8 15V9l5.6 3z"/></svg>',
          "li": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.1c.5-1 1.8-2 3.7-2 4 0 4.7 2.6 4.7 6V21h-4v-5.6c0-1.3 0-3-1.9-3s-2.1 1.4-2.1 2.9V21H9z"/></svg>'}
    soc = "".join(f'<a href="{S[k]}" rel="noopener" aria-label="{n}">{ic[k]}</a>' for k, n in [("fb", "Facebook"), ("ig", "Instagram"), ("yt", "YouTube"), ("li", "LinkedIn")])
    col = lambda items: "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in items)
    return f'''<footer class="site-footer"><div class="wrap foot">
<div>{img("aesthetic-roofing-logo-white", "Aesthetic Roofing logo", cls="logo")}
<p style="margin-top:18px;max-width:34ch">GAF Master Elite&reg; roofing contractor in South Jordan, serving homeowners across Northern Utah.</p>
<div class="socials">{soc}</div></div>
<div><h3>Services</h3><ul>{col(SERVICES_NAV[0][1])}</ul></div>
<div><h3>Roof types &amp; areas</h3><ul>{col(SERVICES_NAV[1][1][:4])}{col(ROOFS_NAV[:2])}</ul></div>
<div><h3>Contact</h3><address><strong style="color:#fff">{S["name"]}</strong><br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p style="margin:14px 0 4px"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></p>
<p style="margin:0"><a href="mailto:{S["email"]}">{S["email"]}</a></p>
<ul style="margin-top:12px">{col(ABOUT_NAV)}</ul></div>
</div><div class="wrap fbottom"><span>&copy; 2026 Aesthetic Roofing. All rights reserved.</span><span><a href="@/privacy-policy/">Privacy Policy</a> &middot; <a href="@/terms-and-conditions/">Terms &amp; Conditions</a> &middot; <a href="@/opt-out-preferences/">SMS Opt-In</a> &middot; <a href="@/sitemap/">Sitemap</a></span></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call Now</a><a href="@/contact/">Book Now</a></div>'''


def cta(title="Find out what your roof really needs.", text="Book a free Roof Health Report. You get a clear summary of what we find and three priced options, with no pressure."):
    return f'''<section class="cta">{img("aerial-roofs-street", "Aerial view of new roofs on homes along a Utah street")}
<div class="wrap"><div class="reveal"><p class="label">Free Roof Health Report</p><h2>{title}</h2><p class="lede" style="margin-top:14px">{text}</p></div>
<div class="reveal"><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a><div class="btn-row" style="margin-top:22px"><a class="btn" href="@/contact/">Book Online {ARROW}</a><a class="btn ghost" href="@/financing/">See Financing</a></div></div></div></section>'''


def side(links, promise=True):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    pr = img("gaf-master-elite", "GAF Master Elite contractor") if promise else ""
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Free Roof Health Report</p><h3>Talk to a South Jordan roofer</h3>
<p>Clear findings, three priced options and financing choices.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn" href="@/contact/">Book Online {ARROW}</a>{pr}</div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero">{img(image, alt, priority=True)}<div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row" style="margin-top:26px"><a class="btn" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a><a class="btn ghost" href="@/contact/">Book Online {ARROW}</a></div></div></section>'''


def quote_form(title="Book your free Roof Health Report"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-first">First name *<input id="f-first" name="first" autocomplete="given-name" required></label><label for="f-last">Last name *<input id="f-last" name="last" autocomplete="family-name" required></label></div>
<div class="row"><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label></div>
<label for="f-street">Property address<input id="f-street" name="address" autocomplete="street-address"></label>
<label for="f-help">What do you need?<select id="f-help" name="service"><option value="">Choose one</option><option>Roof Health Report (free inspection)</option><option>Roof replacement</option><option>Roof repair</option><option>Storm damage</option><option>Gutters</option><option>Something else</option></select></label>
<label for="f-msg">Anything we should know?<textarea id="f-msg" name="message"></textarea></label>
<button class="btn navy" type="submit">Send request {ARROW}</button>
<p class="note">* Required. By submitting you agree to be contacted about your request.</p></form>'''


def head(page):
    url = U + page["path"]
    graph = [biz(page.get("full_biz", True)),
             {"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", "aerial-new-roof-neighborhood") + ".webp"
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
<meta property="og:site_name" content="Aesthetic Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#17181a">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..900&family=Hanken+Grotesk:wght@400;500;600;700&display=swap">
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for aestheticroofing.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + ("@@TRACK_BODY@@\n" if mode == "site" else "") + draft + header() +
           '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() + '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known, redirects)
    if mode == "site":
        doc = doc.replace("@@TRACK_HEAD@@", TRACK_HEAD.strip()).replace("@@TRACK_BODY@@", TRACK_BODY.strip())
        doc = doc.replace("@@REVIEWS_WIDGET@@", "<script defer async src='https://cdn.trustindex.io/loader.js?fa4dd16781fc1458f946ed0e5ce'></script>")
    else:
        depth = page["path"].count("/")
        pre = "../" * depth
        doc = doc.replace("@@TRACK_HEAD@@\n", "")
        doc = doc.replace("@@REVIEWS_WIDGET@@", '<p class="note" style="margin:0;color:rgba(255,255,255,.7)">On the live site, the client\'s Google reviews load here through their Trustindex widget. The preview host blocks outside scripts, so they don\'t show in this draft.</p>')
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
        if page["path"] == "":
            doc = re.sub(r'(?s)^<!doctype html>\s*<html[^>]*>\s*<head>\s*', '', doc)
            doc = doc.replace('<meta charset="utf-8">\n', '').replace('<meta name="viewport" content="width=device-width, initial-scale=1">\n', '')
            doc = re.sub(r'<title>.*?</title>', '<title>Aesthetic Roofing Redesign</title>', doc, count=1)
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
