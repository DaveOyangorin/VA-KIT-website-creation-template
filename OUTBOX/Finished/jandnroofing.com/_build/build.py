"""Builds the jandnroofing.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same URLs and canonicals as the current site for every page J & N wrote (the 411 posts copied from another site are
left out on purpose; see the notes). The current site has no tracking code to keep.
site/    : files to put live (clean folder links)
preview/ : private review copy (links to index.html, forms off, CSS/JS inline; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://jandnroofing.com/"
BIZ_ID = U + "#organization"
SLC_ID = BIZ_ID
TODAY = "2026-10-17"
HOME_OG = "home-hero"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))      # local name -> [w, h, kb]
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))    # remote url -> local name

# Phones, email and social links copied from the current site's header (17 Oct 2026). The street address is from the
# Google profile and matches the West Valley City listing; the site itself doesn't show one.
S = {"name": "J & N Roofing Maintenance, LLC", "short": "J & N Roofing", "email": "jnroofing@gmail.com",
     "phone": "(801) 969-5759", "tel": "+18019695759", "phone24": "(801) 949-7845", "tel24": "+18019497845",
     "street": "3842 S 2200 W", "city": "West Valley City", "st": "UT", "zip": "84119",
     "fb": "https://www.facebook.com/J-N-Roofing-Maintenance-LLC-8019695759-187801007907291/",
     "yelp": "https://www.yelp.com/biz/j-and-n-roofing-maintenance-llc-west-valley-city"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'

TRACK_HEAD = ""
TRACK_BODY = ""
CONTACT = "contact-us/"
INSPECT = "free-estimate/"
ESTIMATE = "free-estimate/"


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["phone"], "email": S["email"],
         "logo": U + "assets/img/j-n-roofing-logo.png", "image": U + "assets/img/j-n-roofing-logo.png",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"],
                     "postalCode": S["zip"], "addressCountry": "US"},
         "sameAs": [S["fb"], S["yelp"]]}
    if full:
        n.update({"description": "J & N Roofing Maintenance, LLC is a residential roofing and maintenance company in West Valley City, Utah, serving the Salt Lake City metro area: roof repairs, replacement, tear-off, re-roofing, inspections and gutter cleaning. GAF certified.",
                  "contactPoint": [{"@type": "ContactPoint", "telephone": S["phone"], "contactType": "customer service"},
                                   {"@type": "ContactPoint", "telephone": S["phone24"], "contactType": "emergency", "hoursAvailable": "Mo-Su 00:00-23:59"}],
                  "areaServed": [{"@type": "City", "name": c} for c in ("West Valley City", "Salt Lake City", "West Jordan", "South Jordan", "Taylorsville", "Sandy", "Murray")],
                  "knowsAbout": ["Roof repair", "Roof replacement", "Roof tear-off", "Re-roofing", "Low slope roofing", "Roof ventilation", "Gutter cleaning", "Roof inspection"]})
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


def quotes_html(tests, title="What customers say about Norm and the crew", limit=6):
    if not tests: return ""
    cards = "".join(f'<figure class="quote{" big" if i == 0 else ""} reveal"><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
                    for i, (q, a) in enumerate(tests[:limit]))
    return f'<section class="sec white"><div class="wrap"><div class="head reveal"><p class="label">Testimonials</p><h2>{title}</h2></div><div class="quotes">{cards}</div></div></section>'


MENU = [
    ("Services", [("Roofing repairs", "services/roofing-repairs/"), ("Roof replacement", "services/roof-replacement/"), ("Roof tear off", "services/roof-tear-off/"),
                  ("Re-roof (overlay)", "services/re-roof-overlay/"), ("Residential roofing", "services/residential-roofing/"), ("Low slope roofing", "services/low-slope-roofing/"),
                  ("Roof inspections &amp; maintenance", "services/roof-inspections-maintenance/"), ("Roof ventilation", "services/roof-ventilation/"),
                  ("Gutter cleaning", "services/gutter-cleaning/"), ("New construction", "services/new-construction/"), ("Consulting", "services/consulting/"), ("All services", "services/")]),
    ("About", [("About us", "about-us/"), ("The J &amp; N difference", "j-n-roofing-difference/"), ("Service areas", "service-areas/"), ("Warranty support", "warranty-support/"),
               ("Testimonials", "testimonials/"), ("References", "references/"), ("Special offers", "special-offers/"), ("Gallery", "gallery/")]),
    ("Learn", [("Roofing FAQ", "frequently-asked-questions/"), ("Glossary of roofing terms", "glossary-of-roofing-terms/"), ("Blog", "blog/")]),
]


def header():
    nav = mob = ""
    for top, items in MENU:
        links = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span>{l}</a>' for i, (l, p) in enumerate(items))
        nav += f'<li><details><summary>{top}</summary><div class="drop"><p class="drop-h">{top}</p>{links}</div></details></li>'
        mob += f'<p class="mh">{top}</p><div class="sub">{links}</div>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="masthead"><div class="wrap"><span>The roof maintenance handbook &middot; West Valley City, Utah</span><span>24-hour support <a href="tel:{S["tel24"]}">{S["phone24"]}</a></span></div></div>
<div class="wrap bar">
<a class="brand" href="@/" aria-label="J &amp; N Roofing home">{img("j-n-roofing-logo", "J & N Roofing Maintenance, LLC", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>{nav}<li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Free estimates</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{INSPECT}">Free Estimate {ARROW}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{INSPECT}">Request a Free Estimate {ARROW}</a></div></details>
</div></header>'''


def footer():
    fb = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9H17l.5-4h-4V8.8c0-.5.3-.8.5-.8z"/></svg>'
    yelp = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.3 2.2c-.6-.2-4.5 1-5 1.4-.4.3-.5.7-.4 1.1l3.6 6.2c.6 1 1.9.5 1.9-.6V2.9c0-.4-.1-.6-.1-.7zM11 14.3 6.7 15.6c-.6.2-.8.8-.5 1.3.6 1 2.2 3 2.9 3.3.4.2.8.1 1.1-.2l2.3-4.1c.5-.9-.5-1.9-1.5-1.6zm1.8-2.6 4.7-1.4c.6-.2.8-.8.6-1.3-.5-1.1-1.9-2.9-2.6-3.4-.4-.2-.8-.2-1.1.2l-2.9 4.3c-.6.9.3 2 1.3 1.6zm4.9 2.3-4.6-1.5c-1-.3-1.8.8-1.2 1.7l2.7 4c.3.4.7.5 1.1.3.7-.5 2.2-2.5 2.5-3.3.2-.5 0-1-.5-1.2z"/></svg>'
    return f'''<footer class="site-footer"><div class="wrap">
<p class="foot-say">When quality counts, <em>count on us.</em></p>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("j-n-roofing-logo", "J & N Roofing Maintenance, LLC logo", cls="logo")}</span>
<p>Residential roofing and maintenance for West Valley City and the Salt Lake City metro area. GAF certified roofing contractor.</p>
<div class="socials"><a href="{S["fb"]}" rel="noopener" aria-label="J &amp; N Roofing on Facebook">{fb}</a><a href="{S["yelp"]}" rel="noopener" aria-label="J &amp; N Roofing on Yelp">{yelp}</a></div></div>
<div><h3>Services</h3><ul><li><a href="@/services/roofing-repairs/">Roofing repairs</a></li><li><a href="@/services/roof-replacement/">Roof replacement</a></li><li><a href="@/services/roof-tear-off/">Roof tear off</a></li><li><a href="@/services/re-roof-overlay/">Re-roof (overlay)</a></li><li><a href="@/services/low-slope-roofing/">Low slope roofing</a></li><li><a href="@/services/roof-inspections-maintenance/">Inspections &amp; maintenance</a></li><li><a href="@/services/gutter-cleaning/">Gutter cleaning</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="@/about-us/">About us</a></li><li><a href="@/warranty-support/">Warranty support</a></li><li><a href="@/special-offers/">Special offers</a></li><li><a href="@/testimonials/">Testimonials</a></li><li><a href="@/service-areas/">Service areas</a></li><li><a href="@/glossary-of-roofing-terms/">Roofing glossary</a></li><li><a href="@/blog/">Blog</a></li></ul></div>
<div><h3>Contact</h3><p class="fname">{S["name"]}</p><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><br>24-hour support: <a href="tel:{S["tel24"]}">{S["phone24"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
</div><div class="fbottom"><span>&copy; 2026 J &amp; N Roofing Maintenance, LLC</span><span><a href="@/privacy-policy/">Privacy Policy</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call Now</a><a href="@/{INSPECT}">Free Estimate</a></div>'''


def cta(title="When quality counts, count on us", text="Call for a free on-site inspection and estimate. Our 24-hour support line is there when something can&rsquo;t wait."):
    return f'''<section class="cta"><div class="wrap"><div class="reveal"><p class="label light">Free estimate</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-locs"><a href="tel:{S["tel"]}"><small>Free estimates</small><b>{S["phone"]}</b></a><a href="tel:{S["tel24"]}"><small>24-hour support</small><b>{S["phone24"]}</b></a>
<a class="btn light" href="@/{INSPECT}">Request a Free Estimate {ARROW}</a></div></div></section>'''


def side(links):
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in links)
    return f'''<aside class="side"><div class="card-cta"><p class="label light">Free estimate</p><h3>Have a question about your roof?</h3>
<p>Call for a free on-site inspection and estimate in West Valley City and the Salt Lake metro.</p><a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a>
<a class="btn light" href="@/{INSPECT}">Request an Estimate {ARROW}</a></div>
<div class="card-list"><h3>Related reading</h3><ul>{lis}</ul></div></aside>'''


def phero(trail, h1, lede, image, alt, label, extra=""):
    lede_html = f'<p class="lede">{lede}</p>' if lede else ""
    return f'''<section class="phero"><div class="wrap ph-grid"><div class="ph-text">{crumbs_html(trail)}
<p class="label">{label}</p><h1>{h1}</h1>{lede_html}{extra}
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<figure class="plate">{img(image, alt, priority=True)}<figcaption><span>Plate</span> {html.escape(alt) if alt else "J &amp; N Roofing"}</figcaption></figure></div></section>'''


def quote_form(title="Request a free estimate"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Best phone number *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label><label for="f-addr">Address<input id="f-addr" name="address" autocomplete="street-address"></label></div>
<label for="f-msg">Briefly describe what you&rsquo;re looking for<textarea id="f-msg" name="message"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button>
<p class="note">* Required. Your name and contact information will never be shared, sold or distributed.</p></form>'''


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
<meta property="og:site_name" content="J &amp; N Roofing Maintenance">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0f1114">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,300..600&family=Work+Sans:wght@400;500;600;700&family=Courier+Prime:wght@400;700&display=swap">
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for jandnroofing.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
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
    used = {"j-n-roofing-logo.png", "favicon.png"}
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
