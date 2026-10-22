"""Builds the pioneerroofingutah.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs, canonicals and page purposes as the current site.
site/    : files to put live (Google Tag Manager, Microsoft Clarity and the Podium chat widget kept; clean folder links)
preview/ : private review copy (no tracking, links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://pioneerroofingutah.com/"
BIZ_ID = U + "#organization"
SLC_ID, PRICE_ID = U + "#salt-lake-city", U + "#price"
UT_ID, AR_ID = SLC_ID, PRICE_ID
TODAY = "2026-10-17"
HOME_OG = "asphalt-background-1"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

# Copied from the header and footer of the current site (17 Oct 2026). The Salt Lake City address and phone match the
# Google profile. The logo says "Est. 1980".
S = {"name": "Pioneer Roofing", "legal": "Pioneer Roofing Co", "email": "John@pioneerroofer.com", "founded": "1980",
     "phone": "(801) 943-7663", "tel": "+18019437663",
     "slc": {"name": "Pioneer Roofing Co", "street": "7041 S 2700 E", "city": "Salt Lake City", "st": "UT", "zip": "84121"},
     "price": {"name": "Pioneer Roofing Co (Price)", "street": "106 N 4th E", "city": "Price", "st": "UT", "zip": "84501"},
     "fb": "https://www.facebook.com/pioneerroofingutah/"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
HEX = '<svg viewBox="0 0 100 112" aria-hidden="true"><path d="M50 2 96 28v56L50 110 4 84V28z"/></svg>'

TRACK_HEAD = open(os.path.join(HERE, "tracking_head.html"), encoding="utf-8").read()
TRACK_BODY = open(os.path.join(HERE, "tracking_body.html"), encoding="utf-8").read()
CONTACT = "contact-us/"
INSPECT = "book-inspection/"
ESTIMATE = "new-roof-estimator/"


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def loc_node(k, nid):
    L = S[k]
    return {"@type": "RoofingContractor", "@id": nid, "name": L["name"], "url": U, "telephone": S["phone"], "email": S["email"],
            "parentOrganization": {"@id": BIZ_ID}, "image": U + "assets/img/pioneer-roofing-logo.png",
            "address": {"@type": "PostalAddress", "streetAddress": L["street"], "addressLocality": L["city"], "addressRegion": L["st"],
                        "postalCode": L["zip"], "addressCountry": "US"},
            "areaServed": {"@type": "State", "name": "Utah"}}


def biz(full=True):
    org = {"@type": "Organization", "@id": BIZ_ID, "name": S["name"], "legalName": S["legal"], "url": U, "email": S["email"],
           "telephone": S["phone"], "logo": U + "assets/img/pioneer-roofing-logo.png", "foundingDate": S["founded"],
           "sameAs": [S["fb"]], "subOrganization": [{"@id": SLC_ID}, {"@id": PRICE_ID}]}
    if not full: return [org]
    org.update({"description": "Pioneer Roofing is a family run residential and commercial roofing company in Salt Lake City, Utah, established in 1980: roof repair, replacement and inspections in asphalt shingles, TPO, PVC and metal.",
                "knowsAbout": ["Roof repair", "Roof replacement", "Roof inspection", "Commercial roofing", "TPO membrane roofing", "Asphalt shingles", "Metal roofing"]})
    return [org, loc_node("slc", SLC_ID), loc_node("price", PRICE_ID)]


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


def quotes_html(tests, title="What our customers say"):
    if not tests: return ""
    cards = "".join(f'<figure class="quote{" big" if i == 0 else ""} reveal"><div class="stars" aria-label="Rated 5 out of 5">&#9733;&#9733;&#9733;&#9733;&#9733;</div><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
                    for i, (q, a) in enumerate(tests[:5]))
    return f'<section class="sec white"><div class="wrap"><div class="head reveal"><p class="label">Reviews</p><h2>{title}</h2></div><div class="quotes">{cards}</div></div></section>'


MENU = [
    ("Services", [("Roof repairs", "roofing-repairs/"), ("Roof inspections", "roof-inspections/"), ("Residential roofing", "residential-roofing/"),
                  ("Commercial roofing", "commercial-roofing/"), ("All services", "services/")]),
    ("Roof types", [("Asphalt shingles", "asphalt-shingles/"), ("TPO membrane", "tpo-membrane/"), ("Metal roofing", "metal-roofing/"), ("Compare roof types", "roofing-types/")]),
    ("Pricing", [("Pricing", "pricing/"), ("New roof estimator", "new-roof-estimator/")]),
    ("About", [("About Pioneer", "about-2/"), ("Certification &amp; warranty", "certification-and-warranty/"), ("Project gallery", "project-gallery/"),
               ("Areas we serve", "areas-we-serve/"), ("Blog", "blog/")]),
]


SEAL = '''<div class="seal" aria-hidden="true"><svg viewBox="0 0 160 160"><defs><path id="sealp" d="M80,80 m-62,0 a62,62 0 1,1 124,0 a62,62 0 1,1 -124,0"/></defs>
<path class="hx" d="M80 8 142 44v72L80 152 18 116V44z"/><text textLength="384" lengthAdjust="spacing"><textPath href="#sealp" textLength="384" lengthAdjust="spacing">Pioneer Roofing Co &#183; Family run &#183; Salt Lake City &#183;</textPath></text></svg>
<span><small>Est.</small><b>1980</b></span></div>'''


def header():
    nav = mob = ""
    for top, items in MENU:
        links = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span>{l}</a>' for i, (l, p) in enumerate(items))
        nav += f'<li><details><summary>{top}</summary><div class="drop">{links}</div></details></li>'
        mob += f'<p class="mh">{top}</p><div class="sub">{links}</div>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Pioneer Roofing home">{img("pioneer-roofing-logo", "Pioneer Roofing Co, est. 1980", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>{nav}<li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Goes straight to John</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{INSPECT}">Book Inspection {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a></div></details>
</div></header>'''


def footer():
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>'
    def loc(k):
        L = S[k]
        return f'<address>{L["street"]}<br>{L["city"]}, {L["st"]} {L["zip"]}</address>'
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top">{SEAL}<p class="foot-say">Built to work.<br><span>Built to last. Since 1980.</span></p></div>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("pioneer-roofing-logo", "Pioneer Roofing Co logo", cls="logo")}</span>
<p>Family run and operated since 1980. Residential and commercial roofing in Salt Lake City, along the Wasatch Front and throughout Utah.</p>
<p class="small">Fully licensed, bonded &amp; insured.</p>
<div class="socials"><a href="{S["fb"]}" rel="noopener" aria-label="Pioneer Roofing on Facebook">{fb}</a></div></div>
<div><h3>Services</h3><ul><li><a href="@/roofing-repairs/">Roof repairs</a></li><li><a href="@/roof-inspections/">Roof inspections</a></li><li><a href="@/residential-roofing/">Residential roofing</a></li><li><a href="@/commercial-roofing/">Commercial roofing</a></li><li><a href="@/asphalt-shingles/">Asphalt shingles</a></li><li><a href="@/tpo-membrane/">TPO membrane</a></li><li><a href="@/metal-roofing/">Metal roofing</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="@/pricing/">Pricing</a></li><li><a href="@/new-roof-estimator/">New roof estimator</a></li><li><a href="@/certification-and-warranty/">Certification &amp; warranty</a></li><li><a href="@/project-gallery/">Project gallery</a></li><li><a href="@/areas-we-serve/">Areas we serve</a></li><li><a href="@/blog/">Blog</a></li></ul></div>
<div><h3>Contact</h3><p class="fname">{S["legal"]}</p>{loc("slc")}<p class="small">Also at</p>{loc("price")}
<p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
</div><div class="fbottom"><span>&copy; 2026 Pioneer Roofing &middot; Family run since 1980</span><span><a href="@/privacy/">Privacy</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call John</a><a href="@/{INSPECT}">Book Inspection</a></div>'''


def cta(title="Get a straight answer on your roof", text="Call John directly, get an instant estimate online, or book an inspection. Transparent pricing on every quote.", image="pioneer-roofs-0803-scaled-1"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap"><div class="reveal"><p class="label light">Since 1980</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-locs"><a href="tel:{S["tel"]}"><small>Goes straight to the owner</small><b>{S["phone"]}</b></a>
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a><a class="btn ghost light" href="@/{ESTIMATE}">Get an Instant Estimate</a></div></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Talk to the owner</p><h3>Questions about your roof?</h3>
<p>Our service number goes directly to John. No recordings, no answering service.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero"><div class="ph-bg">{img(image, alt, priority=True)}</div><div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Book an Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div></section>'''


def quote_form(title="Request a quote"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone number *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-addr">Address<input id="f-addr" name="address" autocomplete="street-address"></label></div>
<label for="f-msg">Message<textarea id="f-msg" name="message" placeholder="Repair, replacement, inspection? Shingles, TPO or metal?"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button>
<p class="note">* Required. John or our office will get back to you.</p></form>'''


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
<meta property="og:site_name" content="Pioneer Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1c0d0a">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@700;800;900&family=Karla:wght@400;500;700&display=swap">
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for pioneerroofingutah.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
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
    used = {"pioneer-roofing-logo.png", "favicon.png"}
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
