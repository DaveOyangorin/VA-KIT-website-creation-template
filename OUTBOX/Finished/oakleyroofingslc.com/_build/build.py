"""Builds the oakleyroofingslc.com redesign.

  python -I build.py <out_site> <out_preview>

Same URLs and canonicals as the current WordPress (Elementor) site, with trailing slashes as today, plus a blog with
one new post and a 404 page. The three WordPress leftovers (hello-world/, category/uncategorized/,
author/supportthemesupport-net/) are kept as noindex pages that point to the blog; see notes for the 301s.
site/    : files to put live (folder links, the client's GA4 tag kept)
preview/ : private review copy (links to index.html, forms off, CSS/JS inline, no tracking; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://oakleyroofingslc.com/"
BIZ_ID = U + "#business"
TODAY = "2026-10-17"
HOME_OG = "single-ply-roof-deck-new-install"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))

# NAP and hours copied from the current contact page (17 Oct 2026). Phone shown as the site shows it.
S = {"name": "Oakley Roofing", "phone": "(801) 651-1000", "tel": "+18016511000",
     "street": "49 West Burton Ave.", "city": "Salt Lake City", "st": "UT", "zip": "84115",
     "hours": "M&ndash;F 8am&ndash;6pm &middot; Sat&ndash;Sun 10am&ndash;4pm"}

# The client's own GA4 tag, copied from the live site's source (17 Oct 2026).
TRACK_HEAD = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-MHKPHZ5LRT"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-MHKPHZ5LRT');</script>"""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
CONTACT = "contact-us/"
BLOG = ("TPO vs. EPDM vs. PVC: Which Flat Roof Membrane Fits Your Building?", "blog/tpo-vs-epdm-vs-pvc/")

# Three lines of work, as on the current site, with their pages
LINES = [("commercial", "Commercial", "commercial/", "TPO, EPDM, PVC, shingle and metal roofs for offices, retail, restaurants, warehouses, factories, condos and apartments. 900 to 45,000 square feet.",
          [("Commercial roofing services", "commercial-services/"), ("Commercial roofing installation", "commercial-roofing-installation/"), ("Commercial repair &amp; maintenance", "commercial-roofing-repair-maintenance/")]),
         ("residential", "Residential", "residential/", "Shingle and metal roofs for new construction and replacements, plus repairs and maintenance. Homes from 900 to 15,000 square feet.",
          [("Residential roofing services", "residential-roofing-services/"), ("Residential roofing installation", "residential-roofing-installation/"), ("Residential roofing repairs", "residential-roofing-repairs/")]),
         ("solar", "Solar", "solar/", "Tesla Certified Solar Roof Installers in Utah: the Tesla Solar Roof, and the Powerwall battery.",
          [("Tesla Solar Roof", "solar-roof/"), ("Tesla Powerwall", "solar-powerwall-2/")])]


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    ext = "png" if name.startswith("oakley-roofing-logo") else "webp"
    a = [f'src="@img/{name}.{ext}"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["tel"],
         "logo": U + "assets/img/oakley-roofing-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": "49 W Burton Ave", "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"},
                                       {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Saturday", "Sunday"], "opens": "10:00", "closes": "16:00"}]}
    if full:
        n.update({"description": "Oakley Roofing is a Salt Lake City roofing company founded in 1993 by Bryce Oakley: commercial TPO, EPDM, PVC, shingle and metal roofing, residential roofing, repairs and maintenance, FHA roof inspections, and Tesla Solar Roof installation.",
                  "foundingDate": "1993", "founder": {"@type": "Person", "name": "Bryce Oakley"},
                  "areaServed": [{"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}}, {"@type": "State", "name": "Utah"}],
                  "knowsAbout": ["Commercial roofing", "TPO roofing", "EPDM roofing", "PVC roofing", "Metal roofing", "Shingle roofing", "Roof repair", "FHA roof inspection", "Tesla Solar Roof", "Tesla Powerwall"]})
    return [n]


def crumbs_ld(path, trail):
    return {"@type": "BreadcrumbList", "@id": U + path + "#breadcrumb", "itemListElement": [
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
        out.append(f'<details{" open" if i == 0 else ""}><summary><span class="q-n">Q{i + 1:02d}</span>{q}</summary><div class="a">{a}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def header():
    drop = "".join(f'''<div class="drop-col"><a class="drop-h" href="@/{p}"><span class="mono">{i + 1:02d}</span>{n}</a>{"".join(f'<a href="@/{sp}">{sn}</a>' for sn, sp in subs)}</div>'''
                   for i, (k, n, p, d, subs) in enumerate(LINES))
    msub = "".join(f'<a class="mh2" href="@/{p}">{n}</a>' + "".join(f'<a href="@/{sp}">{sn}</a>' for sn, sp in subs) for k, n, p, d, subs in LINES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Oakley Roofing home">{img("oakley-roofing-logo-white", "Oakley Roofing", cls="on-dark", lazy=False)}{img("oakley-roofing-logo", "Oakley Roofing", cls="on-light", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop"><div class="drop-grid">{drop}</div><a class="drop-all" href="@/services/">All services {ARROW}</a></div></details></li>
<li><a href="@/about-us/">About</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Quote</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{msub}<a class="mh2" href="@/services/">All services</a></div>
<a href="@/about-us/">About</a><a href="@/blog/">Blog</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{CONTACT}">Get a Free Quote</a><a class="menu-phone" href="tel:{S["tel"]}">{S["phone"]}</a></div></details>
</div></header>'''


def footer():
    cols = "".join(f'<div><h3>{n}</h3><ul><li><a href="@/{p}">{n} roofing</a></li>{"".join(f"<li><a href=\"@/{sp}\">{sn}</a></li>" for sn, sp in subs)}</ul></div>' for k, n, p, d, subs in LINES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">The roof is the fifth elevation.<br><span>We&rsquo;ve built them in Salt Lake City since 1993.</span></p>
<div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a></div></div>
<div class="foot">
<div class="fbrand">{img("oakley-roofing-logo-white", "Oakley Roofing logo", cls="logo")}
<address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p class="mono">{S["hours"]}</p></div>
{cols}
<div><h3>Company</h3><ul><li><a href="@/about-us/">About</a></li><li><a href="@/services/">Services</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/{CONTACT}">Contact</a></li><li><a href="@/sitemap/">Sitemap</a></li></ul></div>
</div>
<div class="fbottom"><span>&copy; 2026 Oakley Roofing &middot; Salt Lake City, Utah</span><span class="mono">Sheet A-999 &middot; Not to scale</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Free Quote</a></div>'''


def cta(title="Tell us about the roof.", text="Commercial, residential or solar: call the office or send a few details, and we&rsquo;ll set up a free quote.", image="restaurant-metal-roof-aerial"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap">
<div class="reveal"><p class="label light">Free quote</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call the office</small><b>{S["phone"]}</b></a><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a><p class="mono small">{S["hours"]}</p></div></div></section>'''


def title_block(rows):
    """An architect's title block: the label/value grid in the corner of every drawing sheet."""
    return '<dl class="tblock">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def phero(trail, h1, lede, label, image=None, alt="", sheet="A-100", rows=None, buttons=True):
    bg = f'<div class="ph-bg">{img(image, alt, priority=True)}</div>' if image else '<div class="ph-bg plan" aria-hidden="true"></div>'
    rows = rows or [("Project", "Oakley Roofing"), ("Location", "Salt Lake City, UT"), ("Sheet", sheet)]
    btns = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}">{bg}<div class="frame" aria-hidden="true"></div><div class="wrap ph-in">
<div class="ph-text">{crumbs_html(trail)}<p class="label light">{label}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btns}</div>
{title_block(rows)}</div></section>'''


def quote_form(title="Request a free quote"):
    # Same fields as the current contact form (name, phone, email, message). Needs a form handler before go-live.
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<label for="q-name">Name *<input id="q-name" name="name" autocomplete="name" required></label>
<div class="row"><label for="q-phone">Phone *<input id="q-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="q-email">Email address *<input id="q-email" type="email" name="email" autocomplete="email" required></label></div>
<label for="q-msg">Tell us about your project<textarea id="q-msg" name="message"></textarea></label>
<button class="btn" type="submit">Send Message {ARROW}</button></form>'''


def head(page):
    url = U + page["path"]
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + (page.get("og") or HOME_OG) + ".webp"
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
<meta property="og:site_name" content="Oakley Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121212">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Unbounded:wght@400;500;600;700&family=Instrument+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Spline+Sans+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
@@TRACK_HEAD@@
<script type="application/ld+json">
{ld}
</script>
</head>'''


def resolve(doc, page, mode, known):
    pre = "../" * page["path"].count("/")

    def link(m):
        p = m.group(1)
        frag = ""
        if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
        if p.endswith((".xml", ".txt", ".html")): return pre + p + frag
        if p not in known: return U + p + frag
        if mode == "preview": return pre + (p or "home/") + "index.html" + frag
        return (pre + p or "./") + frag
    doc = re.sub(r'@/([A-Za-z0-9\-/\._#]*)', link, doc)
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known):
    draft = '<div class="draft-strip">DRAFT PREVIEW for oakleyroofingslc.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() + '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() +
           '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
    if mode == "site":
        doc = doc.replace("@@TRACK_HEAD@@", TRACK_HEAD)
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
            if mode == "preview" and pg["path"] == "": pg = dict(pg, path="home/")
            out = os.path.join(root, "404.html") if pg["path"] == "404.html" else os.path.join(root, pg["path"], "index.html")
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8", newline="\n").write(render(pg, mode, known))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in pages:
            if pg.get("sitemap", True):
                sm.append(f'  <url><loc>{pg["canonical"]}</loc><lastmod>{TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main(*sys.argv[1:3])
