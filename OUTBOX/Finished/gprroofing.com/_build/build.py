"""Builds the gprroofing.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs, canonicals and page purposes as the current site.
site/    : files to put live (Google Tag Manager, Google tag, GA4, Meta Pixel and the LeadConnector chat widget kept; clean folder links)
preview/ : private review copy (no tracking, links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://gprroofing.com/"
BIZ_ID = U + "#organization"
SLC_ID = U + "#west-valley-city"
TODAY = "2026-10-17"
HOME_OG = "6937c156578cc788f4a548a0"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

# Phone, email and service area copied from the current site's header and footer (17 Oct 2026).
# The street address is from the Google profile (the site itself only says "Salt Lake County").
S = {"name": "Go Pro Roofing", "email": "jose@go-proroofing.com", "phone": "(801) 232-5823", "tel": "+18012325823",
     "street": "5291 W Ted Wy", "city": "West Valley City", "st": "UT", "zip": "84120",
     "fb": "https://www.facebook.com/GPR.ROOFING/", "ig": "https://www.instagram.com/gprroofing/",
     "tt": "https://www.tiktok.com/@gpr_construction", "yt": "https://www.youtube.com/@GoProRoofing-UT"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'

TRACK_HEAD = open(os.path.join(HERE, "tracking_head.html"), encoding="utf-8").read()
TRACK_BODY = open(os.path.join(HERE, "tracking_body.html"), encoding="utf-8").read()
CONTACT = "contact/"
INSPECT = "contact/"
ESTIMATE = "contact/"


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["phone"], "email": S["email"],
         "logo": U + "assets/img/go-pro-roofing-logo.png", "image": U + "assets/img/go-pro-roofing-logo.png",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"],
                     "postalCode": S["zip"], "addressCountry": "US"},
         "sameAs": [S["fb"], S["ig"], S["tt"], S["yt"]]}
    if full:
        n.update({"description": "Go Pro Roofing is a licensed and insured roofing contractor in West Valley City, Utah: roof repair, roof replacement, metal roofing and free roof inspections across Salt Lake and Utah counties. Owens Corning Preferred Contractor.",
                  "areaServed": [{"@type": "City", "name": "West Valley City"}, {"@type": "AdministrativeArea", "name": "Salt Lake County"}, {"@type": "AdministrativeArea", "name": "Utah County"}],
                  "knowsAbout": ["Roof repair", "Roof replacement", "Metal roofing", "Asphalt shingle roofing", "TPO roofing", "Roof inspection"]})
    return [n]


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


def quotes_html(tests, title="What West Valley homeowners say", limit=6):
    if not tests: return ""
    cards = "".join(f'<figure class="quote{" big" if i == 0 else ""} reveal"><div class="stars" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)} &middot; Google review</figcaption></figure>'
                    for i, (q, a) in enumerate(tests[:limit]))
    return f'<section class="sec white"><div class="wrap"><div class="head reveal"><p class="label">Reviews</p><h2>{title}</h2></div><div class="quotes">{cards}</div></div></section>'


MENU = [
    ("Services", [("Roof replacement", "roof-replacement-services-utah/"), ("Roof repair", "roof-repair-west-valley-city/"),
                  ("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/"), ("Asphalt shingles", "asphalt-shingle-roofing-west-valley-city-ut/"),
                  ("TPO roofing", "tpo-roofing-contractors-salt-lake-city-utah/"), ("Residential roof installation", "residential-roof-installation-utah/"),
                  ("All services", "services/")]),
    ("About", [("About Go Pro Roofing", "about-go-pro-roofing-west-valley-city/"), ("Reviews", "reviews/"), ("Gallery", "gallery/"), ("Blog", "blog/")]),
]


def header():
    nav = mob = ""
    for top, items in MENU:
        links = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span>{l}</a>' for i, (l, p) in enumerate(items))
        nav += f'<li><details><summary>{top}</summary><div class="drop">{links}</div></details></li>'
        mob += f'<p class="mh">{top}</p><div class="sub">{links}</div>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Go Pro Roofing home">{img("go-pro-roofing-logo", "Go Pro Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>{nav}<li><a href="@/gallery/">Gallery</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>24/7 emergency</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{CONTACT}">Free Quote {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/gallery/">Gallery</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a></div></details>
</div></header>'''


def footer():
    ic = {"fb": '<path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/>',
          "ig": '<path d="M12 7.3a4.7 4.7 0 1 0 0 9.4 4.7 4.7 0 0 0 0-9.4zm0 7.7a3 3 0 1 1 0-6 3 3 0 0 1 0 6zM17 2H7a5 5 0 0 0-5 5v10a5 5 0 0 0 5 5h10a5 5 0 0 0 5-5V7a5 5 0 0 0-5-5zm3 15a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3h10a3 3 0 0 1 3 3zm-2.6-11.6a1.1 1.1 0 1 1-2.2 0 1.1 1.1 0 0 1 2.2 0z"/>',
          "tt": '<path d="M16.6 5.8A4.3 4.3 0 0 1 15.5 3h-3.1v12.4a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.7a5.8 5.8 0 1 0 4.9 5.7V9.1a7.4 7.4 0 0 0 4.3 1.4V7.4a4.3 4.3 0 0 1-3.2-1.6z"/>',
          "yt": '<path d="M21.6 7.2a2.5 2.5 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.5 2.5 0 0 0 2.4 7.2 26 26 0 0 0 2 12a26 26 0 0 0 .4 4.8 2.5 2.5 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.5 2.5 0 0 0 1.8-1.8A26 26 0 0 0 22 12a26 26 0 0 0-.4-4.8zM10 15V9l5.2 3z"/>'}
    soc = "".join(f'<a href="{S[k]}" rel="noopener" aria-label="Go Pro Roofing on {n}"><svg viewBox="0 0 24 24" aria-hidden="true">{ic[k]}</svg></a>'
                  for k, n in (("fb", "Facebook"), ("ig", "Instagram"), ("tt", "TikTok"), ("yt", "YouTube")))
    return f'''<footer class="site-footer"><div class="wrap">
<p class="foot-word">Pro-grade <span>roofs.</span></p>
<div class="foot">
<div class="fbrand">{img("go-pro-roofing-logo", "Go Pro Roofing logo", cls="logo")}
<p>Licensed and insured roofing contractor in West Valley City, serving Salt Lake and Utah counties. Owens Corning Preferred Contractor.</p>
<div class="socials">{soc}</div></div>
<div><h3>Services</h3><ul><li><a href="@/roof-replacement-services-utah/">Roof replacement</a></li><li><a href="@/roof-repair-west-valley-city/">Roof repair</a></li><li><a href="@/metal-roofing-contractors-west-valley-city-ut/">Metal roofing</a></li><li><a href="@/asphalt-shingle-roofing-west-valley-city-ut/">Asphalt shingles</a></li><li><a href="@/tpo-roofing-contractors-salt-lake-city-utah/">TPO roofing</a></li><li><a href="@/residential-roof-installation-utah/">Residential roof installation</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="@/about-go-pro-roofing-west-valley-city/">About</a></li><li><a href="@/reviews/">Reviews</a></li><li><a href="@/gallery/">Gallery</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/sitemap/">Sitemap</a></li></ul></div>
<div><h3>Contact</h3><p class="fname">{S["name"]}</p><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
</div><div class="fbottom"><span>&copy; 2026 Go Pro Roofing &middot; West Valley City, Utah</span><span><a href="@/privacy-policy/">Privacy Policy</a> &middot; <a href="@/terms-of-service/">Terms of Service</a> &middot; <a href="@/sitemap.xml">XML Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call Now</a><a href="@/{CONTACT}">Free Quote</a></div>'''


def cta(title="Get a fast, honest roof quote", text="Free estimates and free roof inspections across Salt Lake and Utah counties. Transparent pricing with no hidden fees."):
    return f'''<section class="cta"><div class="cta-slash" aria-hidden="true"></div><div class="wrap"><div class="reveal"><p class="label light">Free estimates</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-locs"><a href="tel:{S["tel"]}"><small>Call or text &middot; 24/7 emergency service</small><b>{S["phone"]}</b></a>
<a class="btn light" href="@/{CONTACT}">Get a Free Quote {ARROW}</a></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Free estimate</p><h3>Talk to a local roofer</h3>
<p>Free roof inspections and estimates in West Valley City and across the Salt Lake Valley.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn light" href="@/{CONTACT}">Get a Quote {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero"><div class="ph-bg">{img(image, alt, priority=True)}</div><div class="ph-slash" aria-hidden="true"></div><div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div></section>'''


def quote_form(title="Get a free quote"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label><label for="f-addr">Address<input id="f-addr" name="address" autocomplete="street-address"></label></div>
<label for="f-msg">How can we help?<textarea id="f-msg" name="message" placeholder="Leak, storm damage, new roof, metal roof?"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button>
<p class="note">* Required.</p></form>'''


def head(page):
    url = U + page["path"]
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", HOME_OG) + ".webp"
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
<meta property="og:site_name" content="Go Pro Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1c1b1f">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@0,500;0,600;0,700;0,800;1,700;1,800;1,900&family=Manrope:wght@400;500;600;700&display=swap">
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for gprroofing.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
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
        # outside widgets (Roofr estimator, TidyCal booking) can't load inside the preview: show where they go
        doc = re.sub(r'<div class="embed-live"><iframe src="(https://app\.roofr\.com[^"]+)"[^>]*></iframe></div>',
                     r'<div class="embed-note"><b>The live Roofr instant estimator appears here on the real site.</b><span>It can&rsquo;t load inside this private preview.</span><a class="btn" href="\1" rel="noopener">Open the estimator</a></div>', doc)
        doc = re.sub(r'<div class="embed-live"><div class="tidycal-embed"[^>]*></div><script[^>]*></script></div>',
                     '<div class="embed-note"><b>The live TidyCal booking calendar appears here on the real site.</b><span>It can&rsquo;t load inside this private preview.</span><a class="btn" href="https://tidycal.com/mason2/roof-inspection" rel="noopener">Open the booking calendar</a></div>', doc)
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
    used = {"go-pro-roofing-logo.png", "favicon.png"}
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
