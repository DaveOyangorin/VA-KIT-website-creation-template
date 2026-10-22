"""Builds the skybridgeroofings.com redesign.

  python -I build.py <out_site> <out_preview>

Same URLs and canonicals as the current Shopify site (/pages/<handle>, no trailing slash), plus the blog at
/blogs/noticias with one new post, and a 404 page. Shopify leftovers (/pages/plantilla-servicios, a Spanish template with
placeholder text, and /collections/frontpage) are not rebuilt; see the notes for the 301s.
site/    : files to put live (folder per page; the host must serve /pages/roof-repair without a trailing slash)
preview/ : private review copy (links to index.html, forms off, CSS/JS inline; site home in home/)
The current site has no analytics tag to keep.
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://skybridgeroofings.com/"
BIZ_ID = U + "#business"
TODAY = "2026-10-18"
HOME_OG = "drone-metal-roof-new-build"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))

# NAP: name and address from the Google profile (report, 5 Oct 2026); phone shown the way the client's contact page shows it,
# "(435) 659-4915" (the Google profile lists it as +1435-659-4915). Email and hours from the contact page, copied exactly.
S = {"name": "Sky Bridge Roofing", "phone": "(435) 659-4915", "tel": "+14356594915",
     "street": "3007 S W Temple St", "city": "South Salt Lake", "st": "UT", "zip": "84115",
     "email": "cesar@skybridgeroofing.com", "hours": "Monday &ndash; Friday: 8:00 AM &ndash; 6:00 PM"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
CONTACT = "pages/contact/"
BLOG_POST = ("Do You Need a Permit to Replace a Roof in South Salt Lake?", "blogs/noticias/do-you-need-a-permit-to-replace-a-roof-in-south-salt-lake/")

# Services, in the order the report ranks them, with the client's current page handles (the typo in roof-raplecement is
# their live URL and is kept so links and rankings carry over).
SERVICES = [("roof-repair", "Roof Repair", "pages/roof-repair/", "Leaks, damaged shingles and flashing, found and fixed at the source."),
            ("replacement", "Roof Replacement", "pages/roof-raplecement/", "Tear-off to new deck covering, for roofs past repair."),
            ("metal", "Metal Roofing", "pages/metal-roofing/", "Standing seam, corrugated panels and metal shingles."),
            ("inspection", "Roof Inspection", "pages/roof-inspection/", "Free inspections that catch problems while they are small."),
            ("shingles", "Shingle Roofing", "pages/shingles/", "Asphalt and architectural shingles for homes."),
            ("tpo", "TPO Roofing", "pages/tpo/", "Heat-welded single-ply membrane for flat and commercial roofs."),
            ("epdm", "EPDM Roofing", "pages/epdm/", "Rubber membrane roofing for low-slope roofs."),
            ("coatings", "Roof Coatings", "pages/roof-coatings/", "Silicone coatings that add a seamless layer over an existing roof."),
            ("gutters", "Gutters", "pages/gutters/", "Seamless gutters and downspouts, 5-inch and 6-inch."),
            ("walls", "Wall Panels", "pages/wall-panels/", "Architectural metal wall panels and cladding.")]


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def video(src, poster, cls="", label=""):
    return (f'<video class="{cls}" autoplay muted loop playsinline preload="metadata" poster="@img/{poster}.webp"'
            f'{f" aria-label=\"{label}\"" if label else " aria-hidden=\"true\""}><source src="@root/assets/video/{src}.mp4" type="video/mp4"></video>')


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/sky-bridge-roofing-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "18:00"}]}
    if full:
        n.update({"description": "Sky Bridge Roofing is a roofing company in South Salt Lake, Utah: roof repair and replacement, metal and shingle roofing, TPO and EPDM membranes, roof coatings, gutters, wall panels and free roof inspections.",
                  "areaServed": [{"@type": "City", "name": "South Salt Lake", "containedInPlace": {"@type": "State", "name": "Utah"}}],
                  "knowsAbout": [s[1] for s in SERVICES]})
    return [n]


def crumbs_ld(path, trail):
    return {"@type": "BreadcrumbList", "@id": U + path.rstrip("/") + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub(r"<[^>]+>", "", n)), "item": U + p.rstrip("/")} for i, (n, p) in enumerate(trail)]}


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
        out.append(f'<details{" open" if i == 0 else ""}><summary><span class="q-n">Q.{i + 1:02d}</span>{q}</summary><div class="a">{a}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def header():
    drop = "".join(f'<a href="@/{p}"><span class="mono">{i + 1:02d}</span>{n}</a>' for i, (k, n, p, d) in enumerate(SERVICES))
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Sky Bridge Roofing home">{img("sky-bridge-roofing-logo", "Sky Bridge Roofing", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{drop}</div></details></li>
<li><a href="@/pages/about-us/">About</a></li><li><a href="@/blogs/noticias/">Guides</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call or text</small>{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Free Estimate</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{drop}</div>
<a href="@/pages/about-us/">About</a><a href="@/blogs/noticias/">Guides</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{CONTACT}">Get a Free Estimate</a><a class="menu-phone" href="tel:{S["tel"]}">{S["phone"]}</a></div></details>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="@/{p}">{n}</a></li>' for k, n, p, d in SERVICES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Drawn at the desk.<br><span>Built on the roof.</span></p>
<div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a></div></div>
<div class="foot">
<div class="fbrand">{img("sky-bridge-roofing-logo", "Sky Bridge Roofing logo", cls="logo")}
<address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p class="mono">{S["hours"]}<br>Emergency response available.</p></div>
<div><h3>Services</h3><ul class="cols2">{svc}</ul></div>
<div><h3>Company</h3><ul><li><a href="@/pages/about-us/">About us</a></li><li><a href="@/{CONTACT}">Contact</a></li><li><a href="@/blogs/noticias/">Guides</a></li><li><a href="@/sitemap.xml">Sitemap</a></li></ul></div>
<div><h3>Reach us</h3><ul><li><a href="tel:{S["tel"]}">Call {S["phone"]}</a></li><li><a href="sms:{S["tel"]}">Text {S["phone"]}</a></li><li><a href="mailto:{S["email"]}">{S["email"]}</a></li></ul></div>
</div>
<div class="fbottom"><span>&copy; 2026 Sky Bridge Roofing &middot; South Salt Lake, Utah</span><span class="mono">SBR &middot; Sheet 00 of 16</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="sms:{S["tel"]}">Text</a><a href="@/{CONTACT}">Estimate</a></div>'''


def cta(title="Tell us about the roof.", text="Residential, commercial or just a question: call, text or send a few details and we&rsquo;ll set up a free estimate.", image="drone-metal-roof-barn"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="grid-ov" aria-hidden="true"></div><div class="wrap">
<div class="reveal"><p class="label light">Free estimate</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call or text</small><b>{S["phone"]}</b></a><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a><p class="mono small">{S["hours"]}</p></div></div></section>'''


def tblock(rows):
    return '<dl class="tblock">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


def phero(trail, h1, lede, label, image=None, alt="", sheet="R-00", detail=None, buttons=True):
    bg = f'<div class="ph-bg">{img(image, alt, priority=True)}</div>' if image else '<div class="ph-bg plan" aria-hidden="true"></div>'
    rows = [("Project", "Sky Bridge Roofing"), ("Location", "South Salt Lake, UT"), ("Sheet", sheet)]
    side = f'<figure class="ph-detail">{detail}</figure>' if detail else tblock(rows)
    btns = f'<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero">{bg}<div class="grid-ov" aria-hidden="true"></div><div class="wrap ph-in">
<div class="ph-text">{crumbs_html(trail)}<p class="label light">{label}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btns}</div>
{side}</div></section>'''


def quote_form(title="Get a free estimate"):
    # The current form's three project types, plus name, phone, email and message. Needs a form handler before go-live.
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<fieldset class="ptype"><legend>Project type</legend>
<label><input type="radio" name="type" value="Residential project" checked><span>Residential project</span></label>
<label><input type="radio" name="type" value="Commercial project"><span>Commercial project</span></label>
<label><input type="radio" name="type" value="Consultation"><span>Consultation</span></label></fieldset>
<label for="q-name">Name *<input id="q-name" name="name" autocomplete="name" required></label>
<div class="row"><label for="q-phone">Phone *<input id="q-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="q-email">Email<input id="q-email" type="email" name="email" autocomplete="email"></label></div>
<label for="q-msg">Tell us about the roof<textarea id="q-msg" name="message" placeholder="Address or city, roof type, what you&rsquo;re seeing"></textarea></label>
<button class="btn" type="submit">Send Request {ARROW}</button>
<p class="note">* Required. We reply by phone or text.</p></form>'''


def head(page):
    url = page["canonical"] if page.get("canonical") else U + page["path"]
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
<meta property="og:site_name" content="Sky Bridge Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a1520">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@500;700;800;900&family=Red+Hat+Text:ital,wght@0,400;0,500;0,600;1,400&family=Red+Hat+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
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
        if p not in known: return U + p.rstrip("/") + frag
        if mode == "preview": return pre + (p or "home/") + "index.html" + frag
        return (pre + p or "./") + frag
    doc = re.sub(r'@/([A-Za-z0-9\-/\._#]*)', link, doc)
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known):
    draft = '<div class="draft-strip">DRAFT PREVIEW for skybridgeroofings.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() + '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() +
           '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
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
    pages = make_pages()
    known = {p["path"] for p in pages}
    for mode, root in (("site", site_dir), ("preview", prev_dir)):
        os.makedirs(os.path.join(root, "assets"), exist_ok=True)
        if mode == "site":
            shutil.copy(os.path.join(HERE, "style.css"), os.path.join(root, "assets", "style.css"))
            shutil.copy(os.path.join(HERE, "site.js"), os.path.join(root, "assets", "site.js"))
        else:
            for sub in ("img", "video"):
                shutil.copytree(os.path.join(site_dir, "assets", sub), os.path.join(root, "assets", sub), dirs_exist_ok=True)
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
