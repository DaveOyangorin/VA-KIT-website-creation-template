"""Builds the customroofs.biz redesign.

  python -I build.py <out_site> <out_preview>

Same URLs, canonicals and page purposes as the current site (customroofs.biz has no tracking code to keep).
site/    : files to put live (clean folder links)
preview/ : private review copy (links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://customroofs.biz/"
BIZ_ID = U + "#organization"
TODAY = "2026-10-17"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]

S = {"name": "Custom Roofing LLC", "short": "Custom Roofing",
     "phone": "801-889-4220", "tel": "+18018894220", "phone2": "385-371-7423", "tel2": "+13853717423",
     "email": "jaime@customroofs.biz", "city": "Lehi", "st": "UT",
     "fb": "https://www.facebook.com/Customroofs.biz"}
# Phones and email copied from the client's contact block ("Primary: 801-889-4220 / Secondary: 385-371-7423").
# No street address: the site shows none ("Located in Lehi, UT serving all throughout Utah") and the Google
# profile's address is shared with another client. Angelo decides before an address goes on the site.

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>'

# The patina scale: the hues copper passes through as it weathers (Construction Canada, 2017).
PATINA = [("Salmon pink", "#e59a7a"), ("Russet brown", "#b5652f"), ("Chocolate brown", "#6e3f22"), ("Slate gray", "#4a4d4f"), ("Blue-green", "#6fb3a3")]


def patina_bar(cls=""):
    return f'<div class="patina {cls}" aria-hidden="true">' + "".join(f'<i style="background:{c}"></i>' for _, c in PATINA) + "</div>"


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": ["Organization", "RoofingContractor"], "@id": BIZ_ID, "name": S["name"], "url": U,
         "telephone": "+1-" + S["phone"], "email": S["email"],
         "address": {"@type": "PostalAddress", "addressLocality": S["city"], "addressRegion": S["st"], "addressCountry": "US"}}
    if full:
        n.update({"logo": U + "assets/img/custom-roofing-logo.png", "image": U + "assets/img/copper-roof-ladder-trees.webp",
                  "description": "Custom Roofing LLC is a Lehi, Utah roofing company specializing in copper roofing, copper siding and roof repair and maintenance along the Wasatch Front.",
                  "areaServed": [{"@type": "State", "name": "Utah"}, {"@type": "City", "name": "Salt Lake City"}, {"@type": "City", "name": "Lehi"}],
                  "knowsAbout": ["Copper roofing", "Copper siding", "Copper gutters", "Roof repair", "Roof maintenance"],
                  "contactPoint": [{"@type": "ContactPoint", "telephone": "+1-" + S["phone"], "contactType": "customer service", "areaServed": "US-UT"},
                                   {"@type": "ContactPoint", "telephone": "+1-" + S["phone2"], "contactType": "customer service", "areaServed": "US-UT"}],
                  "sameAs": [S["fb"]]})
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
        f'<details{" open" if i == 0 else ""}><summary>{q}</summary><div class="a"><p>{a}</p></div></details>' for i, (q, a) in enumerate(faqs)) + "</div>"


def quotes_html(tests):
    cards = []
    for i, (q, a) in enumerate(tests):
        cards.append(f'<figure class="quote{" big" if i == 0 else ""} reveal"><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>')
    return '<div class="quotes">' + "".join(cards) + "</div>"


NAV = [("Copper Roofing", "copper-roofing-utah/"), ("Siding", "lehi-custom-siding-home-value/"),
       ("Repair &amp; Maintenance", "custom-roofing-maintenance-utah/"), ("Services", "home/roofing-services-lehi-quality-guaranteed/"),
       ("Copper Guide", "blog/why-does-copper-turn-green/")]
CONTACT = "copper-roofing-lehi/"


def header():
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in NAV)
    mob = "".join(f'<a href="@/{p}">{l}</a>' for l, p in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{S["short"]} home">{img("custom-roofing-logo", "Custom Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>{lis}</ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call Jaime&rsquo;s team</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a></div></details>
</div></header>'''


def footer():
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>'
    return f'''<footer class="site-footer">{patina_bar("foot-patina")}<div class="wrap foot-top"><p class="foot-say">Every roof should fit <em>the house it&rsquo;s on.</em></p><a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a></div><div class="wrap foot">
<div>{img("custom-roofing-logo", "Custom Roofing logo", cls="logo")}
<p style="margin-top:18px;max-width:34ch">Copper roofing, copper siding, and roof repair and maintenance. Located in Lehi, Utah, serving Salt Lake City and the Wasatch Front.</p>
<div class="socials"><a href="{S["fb"]}" rel="noopener" aria-label="Custom Roofing on Facebook">{fb}</a></div></div>
<div><h3>Services</h3><ul><li><a href="@/copper-roofing-utah/">Copper roofing in Utah</a></li><li><a href="@/lehi-custom-siding-home-value/">Copper siding</a></li><li><a href="@/custom-roofing-maintenance-utah/">Repair &amp; maintenance</a></li><li><a href="@/home/roofing-services-lehi-quality-guaranteed/">All services &amp; recent work</a></li></ul></div>
<div><h3>Learn</h3><ul><li><a href="@/blog/">Copper roofing guide</a></li><li><a href="@/blog/why-does-copper-turn-green/">Why copper turns green</a></li><li><a href="@/{CONTACT}">Contact &amp; quotes</a></li></ul></div>
<div><h3>Contact</h3><p style="margin:0 0 6px"><strong style="color:#fff">{S["name"]}</strong><br>Lehi, Utah</p>
<p style="margin:10px 0 2px"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></p>
<p style="margin:0 0 6px;font-size:.9rem">Secondary: <a href="tel:{S["tel2"]}">{S["phone2"]}</a></p>
<p style="margin:0"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
</div><div class="wrap fbottom"><span>&copy; 2026 Custom Roofing LLC. All rights reserved.</span><span><a href="https://customroofs.biz/es/" hreflang="es">Espa&ntilde;ol</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call Now</a><a href="@/{CONTACT}">Request a Quote</a></div>'''


def cta(title="Planning a copper roof, or need yours looked at?", text="Call us or send a message with your project location and what you have in mind. We&rsquo;ll set up a consultation and build your project plan."):
    return f'''<section class="cta">{img("copper-curved-dormer", "Curved copper dormer with an arched window on a slate roof")}
<div class="wrap"><div class="reveal"><p class="label">Talk to Custom Roofing</p><h2>{title}</h2><p class="lede" style="margin-top:14px">{text}</p></div>
<div class="reveal"><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a><p class="alt">Secondary line: <a href="tel:{S["tel2"]}">{S["phone2"]}</a></p><div class="btn-row" style="margin-top:22px"><a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a><a class="btn ghost" href="mailto:{S["email"]}">{MAIL} Email us</a></div></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta">{patina_bar()}<p class="label light">Talk to us</p><h3>Start with a consultation</h3>
<p>Tell us where the project is and what you&rsquo;d like to do. We&rsquo;ll walk you through the options.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a></div>
<div class="card-list"><h3>Related</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero">{img(image, alt, priority=True)}<div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row" style="margin-top:26px"><a class="btn" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a><a class="btn ghost" href="@/{CONTACT}">Request a Quote {ARROW}</a></div></div>{patina_bar("hero-patina")}</section>'''


def quote_form(title="Request a quote"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone<input id="f-phone" type="tel" name="phone" autocomplete="tel"></label></div>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-loc">Project city<input id="f-loc" name="location" autocomplete="address-level2" placeholder="e.g. Lehi, Salt Lake City"></label></div>
<label for="f-need">Project<select id="f-need" name="need"><option value="">Choose one</option><option>Copper roof</option><option>Copper accents (dormer, valley, chimney cap)</option><option>Copper siding</option><option>Copper gutters</option><option>Roof repair or maintenance</option><option>Something else</option></select></label>
<label for="f-msg">Message *<textarea id="f-msg" name="message" required></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button>
<p class="note">* Required.</p></form>'''


def head(page):
    url = U + page["path"]
    graph = [biz(page.get("full_biz", True)),
             {"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["short"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", "copper-roof-ladder-trees") + ".webp"
    t = html.escape(page["title"], quote=False); m = html.escape(page["meta"], quote=True)
    canon = f'<link rel="canonical" href="{page["canonical"]}">' if page.get("canonical") else ""
    es = f'<link rel="alternate" hreflang="en" href="{url}">\n<link rel="alternate" hreflang="es" href="{U}es/{page["path"]}">' if page.get("es") else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")}">
{canon}
{es}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="Custom Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f1614">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,500..800;1,6..96,500..700&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@500&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>'''


def resolve(doc, page, mode, known, redirects):
    depth = page["path"].count("/")
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for customroofs.biz &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() +
           '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() + '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known, redirects)
    doc = re.sub(r"\n{3,}", "\n\n", doc).replace("<link rel=\"canonical\"", "<link rel=\"canonical\"")
    if mode == "preview":
        pre = "../" * page["path"].count("/")
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
    return doc


def main(site_dir, prev_dir):
    from pages import make_pages
    pages, redirects = make_pages()
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
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main(*sys.argv[1:3])
