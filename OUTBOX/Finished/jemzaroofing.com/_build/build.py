"""Builds the jemzaroofing.com redesign.

  python -I build.py <out_site> <out_preview>

Same URLs as the current site (the .php file names are kept, so nothing moves), with canonicals added.
site/    : files to put live. Pages are plain HTML saved under the same .php names; videos stay where they are on the server.
preview/ : private review copy (folder links, forms off, CSS/JS inline; site home in home/, review page at the root)
The current site has no tracking code to keep.
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://jemzaroofing.com/"
BIZ_ID = U + "#organization"
TODAY = "2026-10-17"
HOME_OG = "metal-roof-05"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))  # local name -> [w, h, kb]

# NAP and facts copied from the current site's header, footer and about page (17 Oct 2026).
S = {"name": "Jemza Roofing", "email": "Jemza@jemzaroofing.com", "phone": "(385) 261-2942", "tel": "+13852612942",
     "street": "2212 S West Temple Ste. #38", "city": "Salt Lake City", "st": "Utah", "st2": "UT", "zip": "84115",
     "map": "https://maps.app.goo.gl/ELnG4Wwpc8FyXmu38"}

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>'
CONTACT = "contact.php"
VID = U + "img/"   # the client's job videos stay on the server at their current paths (about 170 MB in all)


def img(name, alt, cls="", lazy=True, priority=False, sizes=""):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def video(path, label):
    """A job video from the client's server. The preview swaps it for a link (outside media can't load there)."""
    return (f'<figure class="vid"><video controls preload="none" playsinline src="{VID}{path}"></video>'
            f'<figcaption>{label}</figcaption></figure>')


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/jemza-roofing-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st2"],
                     "postalCode": S["zip"], "addressCountry": "US"},
         "hasMap": S["map"]}
    if full:
        n.update({"description": "Jemza Roofing is a licensed and insured roofing company in Salt Lake City, Utah, founded in Millcreek, with 18 years of experience in residential and commercial roofing: metal roofing, asphalt shingles, chimneys, chimney caps and shrouds, gutters, soffit and fascia, metal wall panels and snow bars.",
                  "slogan": "Quality over quantity always",
                  "knowsLanguage": ["en", "es"],
                  "paymentAccepted": "Cash, Credit Card, Square, Check",
                  "areaServed": {"@type": "GeoCircle", "geoMidpoint": {"@type": "GeoCoordinates", "postalCode": S["zip"], "addressLocality": S["city"]}, "geoRadius": "80467"},
                  "knowsAbout": ["Metal roofing", "Asphalt shingles", "Roof replacement", "Cedar shingles", "Chimney caps and shrouds",
                                 "Gutter, soffit and fascia installation", "Metal wall panels", "Snow bars", "Roof repair", "Roof inspections"]})
    return [n]


def crumbs_ld(path, trail):
    return {"@type": "BreadcrumbList", "@id": canon(path) + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub(r"<[^>]+>", "", n)), "item": canon(p)} for i, (n, p) in enumerate(trail)]}


def faq_ld(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": html.unescape(re.sub(r"<[^>]+>", "", q)),
            "acceptedAnswer": {"@type": "Answer", "text": html.unescape(re.sub(r"<[^>]+>", " ", a)).strip()}} for q, a in faqs]}


def canon(path):
    return U if path in ("", "index.php") else U + path


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


# The four reviews shown on the client's own home page, word for word.
REVIEWS = [
    ("Very happy with the whole experience! Omar is knowledgeable, professional, and a great communicator. Did not try to upsell me. The installation was done professionally, quickly and cleanly. The couple of small things that needed to be addressed after the main work were done rapidly and well.", "Leila Dethlefsen"),
    ("Omar and Jemza roofing were great. always got back to me to answer all my questions. Started when he said he would and finished on time. Did a great job at a fair price. I had existing roof stripped and replaced added ridge vents and all new gutters. Looks great wife and I very happy with their work.", "Paul Stempniak"),
    ("We had new gutter installation on our old (and crooked) house. They were on time, efficient, did a great job and even let us know about a tricky part of our roof that might need an additional spout and if we noticed any leakage that they’d come back and add it for us. Highly recommend their service!", "R P"),
    ("Omar was amazing to work with! Super responsive and on top of everything. Great crew as well. Very hard workers. Did an excellent job on our roof and gutters. They also did a great job cleaning up. I would recommend Jemza roofing to anyone.", "Aspen Landgren"),
]


def quotes_html(title="What customers say", limit=4, head=True):
    cards = "".join(f'<figure class="quote reveal"><blockquote><p>&ldquo;{html.escape(q)}&rdquo;</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
                    for q, a in REVIEWS[:limit])
    h = f'<div class="head reveal"><p class="label">Reviews</p><h2>{title}</h2></div>' if head else ""
    return f'<section class="sec"><div class="wrap">{h}<div class="quotes">{cards}</div></div></section>'


SERVICES = [  # (label, path, hero image, one-liner)
    ("Metal roofing", "metal-roofing.php", "metal-roof-01", "Standing-seam roofs chosen to fit your budget and the look of the house."),
    ("Asphalt shingles", "asphalt-shingles.php", "asphalt-shingle-roof-05", "Weather-resistant shingle roofs in a range of styles and colors."),
    ("Chimney", "chimney.php", "chimney-01", "From inspection to reconstruction, built to be safe and look right."),
    ("Chimney caps &amp; shrouds", "ChimneyCap-Shroud.php", "chimney-shroud-07", "Custom metal and copper caps and shrouds."),
    ("Gutter, soffit &amp; fascia", "gutter-soffit-fascia.php", "gutter-soffit-fascia-09", "Installation and repair, copper included."),
    ("Metal wall panels", "wall-panels.php", "metal-wall-panels-02", "Metal cladding for walls, matched to the roof."),
    ("Snow bars", "snow_bars.php", "snow-bars-02", "Snow retention for metal roofs."),
    ("Pavers &amp; ballasted roofs", "pavers_and_ballested.php", "ballasted-paver-roof-02", "Paver and ballast work on flat and low-slope roofs."),
]
BLOG = ("Chimney Cap vs. Chimney Shroud", "chimney-cap-vs-chimney-shroud.php")


BADGE = '''<div class="badge" aria-hidden="true"><svg viewBox="0 0 120 120"><defs><path id="bdg" d="M60,60 m-46,0 a46,46 0 1,1 92,0 a46,46 0 1,1 -92,0"/></defs>
<text textLength="286" lengthAdjust="spacing"><textPath href="#bdg" textLength="286" lengthAdjust="spacing">Hablamos espa&#241;ol &#183; English &#183;</textPath></text></svg><span>ES</span></div>'''


def header():
    svc = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span>{l}</a>' for i, (l, p, _, _) in enumerate(SERVICES)) + '<a class="all" href="@/services.php">All services &rarr;</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="Jemza Roofing home">{img("jemza-roofing-logo", "Jemza Roofing, quality over quantity always", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{svc}</div></details></li>
<li><a href="@/portfolio.php">Portfolio</a></li><li><a href="@/about.php">About</a></li><li><a href="@/testimonials.php">Reviews</a></li><li><a href="@/{BLOG[1]}">Guide</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small lang="es">Hablamos espa&ntilde;ol</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{CONTACT}">Get a Quote</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{svc}</div>
<a href="@/portfolio.php">Portfolio</a><a href="@/about.php">About</a><a href="@/testimonials.php">Reviews</a><a href="@/{BLOG[1]}">Guide: caps vs. shrouds</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>'''


def footer():
    lis = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p, _, _ in SERVICES)
    return f'''<footer class="site-footer"><div class="wrap">
<p class="foot-word">Quality over quantity, <em>always.</em></p>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("jemza-roofing-logo", "Jemza Roofing logo", cls="logo")}</span>
<p>Founded in Millcreek, Utah. Residential and commercial roofing within 50 miles of Salt Lake City.</p>
<p class="mono">Licensed &amp; insured &middot; English / Espa&ntilde;ol</p></div>
<div><h3>Services</h3><ul>{lis}</ul></div>
<div><h3>Company</h3><ul><li><a href="@/about.php">About</a></li><li><a href="@/services.php">All services</a></li><li><a href="@/portfolio.php">Portfolio</a></li><li><a href="@/testimonials.php">Reviews</a></li><li><a href="@/{BLOG[1]}">Chimney caps vs. shrouds</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></div>
<div><h3>Office</h3><address>{S["name"]}<br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p>
<p class="mono">Cash, card, Square and check</p><p><a href="{S["map"]}" rel="noopener">Directions on Google Maps</a></p></div>
</div><div class="fbottom"><span>&copy; 2026 Jemza Roofing &middot; Salt Lake City, Utah</span><span><a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{CONTACT}">Get a Quote</a></div>'''


def cta(title="Tell us about your roof", text="Call the office or send a message for a quote. We cover 50 miles around Salt Lake City, and we speak English and Spanish.", image="new-roof-01"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap"><div class="reveal"><p class="label light">Get a quote</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Office &middot; English / Espa&ntilde;ol</small><b>{S["phone"]}</b></a>
<a class="btn" href="@/{CONTACT}">Send a message {ARROW}</a><a class="cta-mail" href="mailto:{S["email"]}">{S["email"]}</a></div></div></section>'''


def phero(trail, h1, lede, image, alt, label):
    return f'''<section class="phero"><div class="ph-bg">{img(image, alt, priority=True)}</div><div class="wrap">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1><p class="lede">{lede}</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>{BADGE}</section>'''


def gallery(items, cls="grid"):
    """items: (image, caption)"""
    return f'<div class="{cls}">' + "".join(f'<figure class="reveal">{img(n, c)}<figcaption>{c}</figcaption></figure>' for n, c in items) + "</div>"


def contact_form(title="Request a quote"):
    # Same field names as the current form (process.php). The live form's token/captcha come from the client's PHP; see notes.
    return f'''<form class="form" method="post" action="process.php">
<h3>{title}</h3>
<div class="row"><label for="f-name">First name *<input id="f-name" name="name" autocomplete="given-name" required></label><label for="f-last">Last name<input id="f-last" name="last_name" autocomplete="family-name"></label></div>
<div class="row"><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label><label for="f-phone">Phone<input id="f-phone" type="tel" name="phone" autocomplete="tel"></label></div>
<label for="f-project">Project (for example: metal roof, gutters, chimney shroud)<input id="f-project" name="project"></label>
<label for="f-msg">Message *<textarea id="f-msg" name="message" required></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button>
<p class="note">English or Spanish, whichever you prefer.</p></form>'''


def head(page):
    url = canon(page["path"])
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "#website", "url": U, "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "assets/img/" + page.get("og", HOME_OG) + ".webp"
    t = html.escape(page["title"], quote=False); m = html.escape(page["meta"], quote=True)
    canon_tag = "" if page["path"] == "404.html" else f'<link rel="canonical" href="{url}">'
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")}">
{canon_tag}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="Jemza Roofing">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#16191d">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,300..600&family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>'''


def out_path(path, mode):
    """Where a page is written: the site keeps the .php names; the preview uses folders (home/ for the home page)."""
    if path == "404.html": return "404.html"
    if mode == "site": return path or "index.php"
    stem = path[:-4] if path.endswith(".php") else path
    return (stem or "home") + "/index.html"


def resolve(doc, page, mode, known):
    here = out_path(page["path"], mode)
    pre = "../" * here.count("/")

    def link(m):
        p = m.group(1)
        frag = ""
        if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
        if p.endswith((".xml", ".txt")): return pre + p + frag
        if p not in known: return U + p + frag
        if mode == "site": return (p or "./") + frag
        return pre + out_path(p, mode) + frag
    doc = re.sub(r'@/([A-Za-z0-9\-_/\.#]*)', link, doc)
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known):
    draft = '<div class="draft-strip">DRAFT PREVIEW for jemzaroofing.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() + '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() +
           '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
    if mode == "preview":
        pre = "../" * out_path(page["path"], mode).count("/")
        css = open(os.path.join(HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
        # the client's job videos live on their server and can't load inside the private preview
        doc = re.sub(r'<video controls preload="none" playsinline src="([^"]+)"></video>',
                     lambda m: f'<a class="vid-note" href="{m.group(1)}" rel="noopener">{PLAY}<b>Job video</b><span>Plays here on the live site. Open the video file</span></a>', doc)
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
            out = os.path.join(root, out_path(pg["path"], mode))
            os.makedirs(os.path.dirname(out) or root, exist_ok=True)
            open(out, "w", encoding="utf-8", newline="\n").write(render(pg, mode, known))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in pages:
            if pg.get("sitemap", True):
                sm.append(f'  <url><loc>{canon(pg["path"])}</loc><lastmod>{TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    used = {"jemza-roofing-logo.png", "favicon.png"}
    for dp, _, fs in os.walk(prev_dir):
        for f in fs:
            if f.endswith(".html"): used |= set(re.findall(r"assets/img/([\w.-]+)", open(os.path.join(dp, f), encoding="utf-8").read()))
    imgdir = os.path.join(prev_dir, "assets", "img")
    for f in os.listdir(imgdir):
        if f not in used: os.remove(os.path.join(imgdir, f))
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main(*sys.argv[1:3])
