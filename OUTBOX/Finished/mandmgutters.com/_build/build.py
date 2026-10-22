"""Builds the mandmgutters.com redesign.

  python -I build.py <extract.json> <out_site> <out_preview>

Same 183 URLs and canonicals as the current WordPress (Divi) site, plus a new blog post and a 404 page.
site/    : files to put live (folder links, with the client's tracking tags kept)
preview/ : private review copy (links to index.html, forms off, CSS/JS inline, no tracking; site home in home/)
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://mandmgutters.com/"
BIZ_ID = U + "#organization"
TODAY = "2026-10-17"
HOME_OG = "mg-6540"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))
IMGMAP = json.load(open(os.path.join(HERE, "imgmap.json"), encoding="utf-8"))

# NAP and hours copied from the current site's footer and schema (17 Oct 2026). Phone shown as the site shows it.
S = {"name": "M&M Gutters & Exteriors", "email": "info@mandmgutters.com", "phone": "801.280.2222", "tel": "+18012802222",
     "street": "290 S Redwood Rd Suite B", "city": "Salt Lake City", "st": "UT", "zip": "84104", "hours": "Mon&ndash;Fri 8am&ndash;5pm"}
COUNTIES = ["Salt Lake County", "Utah County", "Summit County", "Tooele County", "Davis County", "Weber County"]

# The client's own tracking, copied from the live site's source (17 Oct 2026): two GA/UA gtag configs, a GA4 gtag
# config, two Google Tag Manager containers (these load the Google Ads AW-1000898368, the second GA4 and CallRail),
# and the Podium chat widget. Universal Analytics (UA-) stopped collecting data in 2024; kept as found, see notes.
TRACK_HEAD = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-CF0E9ETG68"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-CF0E9ETG68');gtag('config','UA-53892206-6');gtag('config','UA-131026571-1');</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-57KVKWJJ');</script>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KBLHRZ3');</script>
<script defer id="podium-widget" data-organization-api-token="2612a682-d2f7-4eca-a6d5-cb9fcbc0c221" src="https://connect.podium.com/widget.js#ORG_TOKEN=2612a682-d2f7-4eca-a6d5-cb9fcbc0c221"></script>"""
TRACK_BODY = """<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-57KVKWJJ" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KBLHRZ3" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>"""

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
QUOTE = "request-a-quote/"
CONTACT = "contact-us/"

# Services in the order water meets them, roof to ground (the design's "path of the water")
SERVICES = [("roof", "Roofing", "services/roofing/", "Shingle and metal roofs, with GAF roofing available."),
            ("cable", "Heat Cable &amp; Ice Melting", "services/roof-heat-cable-installation/", "Heat cable and ice-melting systems that keep ice dams off the eaves."),
            ("gutter", "Rain Gutters", "services/rain-gutters-installation/", "Seamless gutters made on site, in copper, aluminum and steel."),
            ("guard", "Leaf Guards", "services/leaf-guards/", "Guards that keep debris out and let water through."),
            ("soffit", "Soffit &amp; Fascia", "services/fascia-and-soffit-installation/", "Ventilation and a finished roof edge."),
            ("window", "Windows", "services/windows/", "Full-home window replacement."),
            ("siding", "Siding", "services/exterior-siding/", "Siding that keeps water and weather out."),
            ("stucco", "Stucco &amp; Stone", "services/stucco-stone-siding-in-salt-lake-city/", "Stucco finishes and natural or manufactured stone.")]
BLOG = ("5-Inch vs. 6-Inch Gutters: Which Size Does Your Home Need?", "blog/5-inch-vs-6-inch-gutters/")


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def biz(full=True):
    n = {"@type": ["HomeAndConstructionBusiness", "RoofingContractor"], "@id": BIZ_ID, "name": S["name"], "url": U, "telephone": S["tel"], "email": S["email"],
         "logo": U + "assets/img/mm-gutters-exteriors-logo.png", "image": U + "assets/img/" + HOME_OG + ".webp",
         "address": {"@type": "PostalAddress", "streetAddress": S["street"], "addressLocality": S["city"], "addressRegion": S["st"], "postalCode": S["zip"], "addressCountry": "US"},
         "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "08:00", "closes": "17:00"}]}
    if full:
        n.update({"description": "M&M Gutters & Exteriors is a family-owned exterior contractor in Salt Lake City, started in 1990: rain gutters, leaf guards, heat cable and ice-melting systems, soffit and fascia, roofing, windows, siding, stucco and stone.",
                  "foundingDate": "1990", "founder": None,
                  "employee": {"@type": "Person", "name": "Nate Nuttall", "jobTitle": "Owner"},
                  "areaServed": [{"@type": "AdministrativeArea", "name": c + ", Utah"} for c in COUNTIES],
                  "knowsAbout": ["Rain gutters", "Seamless gutters", "Copper gutters", "Leaf guards", "Heat cable", "Ice dams", "Soffit and fascia", "Roofing", "Windows", "Siding", "Stucco"]})
        n.pop("founder")
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


def header():
    svc = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span><i class="ic {k}"></i><b>{n}</b><small>{d}</small></a>' for i, (k, n, p, d) in enumerate(SERVICES))
    msvc = "".join(f'<a href="@/{p}"><i class="ic {k}"></i>{n}</a>' for k, n, p, _ in SERVICES)
    more = '<a href="@/services/rain-gutters-installation/rain-gutter-installation-process/">Gutter installation process</a><a href="@/services/ice-melting-systems/">Ice-melting systems</a><a href="@/services/roofing/gaf-roofing/">GAF roofing</a><a href="@/services/financing/">Financing</a><a href="@/services/">All services</a>'
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="M&amp;M Gutters &amp; Exteriors home">{img("mm-gutters-exteriors-logo", "M&M Gutters & Exteriors", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop"><div class="drop-head"><p class="label">The path of the water</p><p>Every service in the order rain meets your house, from the roof to the ground.</p><div class="drop-more">{more}</div></div><div class="drop-grid">{svc}</div></div></details></li>
<li><a href="@/our-work/">Our work</a></li><li><a href="@/about-mm-gutters-exteriors/">About</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/services/financing/">Financing</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>{S["hours"]}</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{QUOTE}">Free Quote</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{msvc}{more}</div>
<a href="@/our-work/">Our work</a><a href="@/about-mm-gutters-exteriors/">About</a><a href="@/blog/">Blog</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="@/{QUOTE}">Get a Free Quote</a><a class="menu-phone" href="tel:{S["tel"]}">{S["phone"]}</a></div></details>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="@/{p}">{n}</a></li>' for _, n, p, _ in SERVICES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Rain hits the roof first.<br><em>We follow it all the way down.</em></p>
<a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></div>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("mm-gutters-exteriors-logo", "M&M Gutters & Exteriors logo", cls="logo")}</span>
<p>Family-owned exterior contractor in Salt Lake City since 1990. Gutters first, and now everything from the roof to the siding.</p></div>
<div><h3>Services</h3><ul>{svc}<li><a href="@/services/financing/">Financing</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="@/about-mm-gutters-exteriors/">About</a></li><li><a href="@/our-work/">Our work</a></li><li><a href="@/hover/">HOVER 3D models</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/{QUOTE}">Request a quote</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></div>
<div><h3>Office</h3><address>{S["name"]}<br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address>
<p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p><p class="mono">{S["hours"]}</p>
<p class="small-print">Serving {", ".join(c.replace(" County", "") for c in COUNTIES[:-1])} and {COUNTIES[-1].replace(" County", "")} counties</p></div>
</div>
<p class="foot-word" aria-hidden="true">Gutters &amp; Exteriors</p>
<div class="fbottom"><span>&copy; 2026 M&amp;M Gutters &amp; Exteriors &middot; Salt Lake City, Utah</span><span><a href="@/privacy-policy/">Privacy Policy</a> &middot; <a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{QUOTE}">Free Quote</a></div>'''


def cta(title="Quote your next project", text="Tell us about your gutters, roof or siding. We&rsquo;ll come out, measure and give you a free quote.", image="20140530-144851"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap">
<div class="reveal"><p class="label light">Free quote &middot; {S["hours"]}</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call the office</small><b>{S["phone"]}</b></a><a class="btn" href="@/{QUOTE}">Get a Free Quote {ARROW}</a></div></div></section>'''


def phero(trail, h1, lede, label, image=None, alt="", buttons=True):
    pic = f'<div class="ph-bg">{img(image, alt, priority=True)}</div>' if image else '<div class="ph-bg plan" aria-hidden="true"></div>'
    btns = f'<div class="btn-row"><a class="btn" href="@/{QUOTE}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}">{pic}<div class="wrap"><div class="ph-text">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btns}</div></div></section>'''


def quote_form(title="Quote your next project"):
    # Same fields as the current quote form (full name, email, phone). Needs a form handler before go-live.
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<label for="q-name">Full name *<input id="q-name" name="name" autocomplete="name" required></label>
<div class="row"><label for="q-email">Email address *<input id="q-email" type="email" name="email" autocomplete="email" required></label><label for="q-phone">Phone number *<input id="q-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="q-msg">What&rsquo;s the project? (optional)<textarea id="q-msg" name="message"></textarea></label>
<button class="btn" type="submit">Submit {ARROW}</button></form>'''


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
<meta property="og:site_name" content="M&amp;M Gutters &amp; Exteriors">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b1a2f">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:ital,wdth,wght@0,62..125,300..900;1,62..125,300..900&family=Instrument+Serif:ital@0;1&family=IBM+Plex+Mono:wght@500&display=swap">
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
    draft = '<div class="draft-strip">DRAFT PREVIEW for mandmgutters.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + ("@@TRACK_BODY@@\n" if mode == "site" else "") + draft + header() +
           '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() + '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
    if mode == "site":
        doc = doc.replace("@@TRACK_HEAD@@", TRACK_HEAD).replace("@@TRACK_BODY@@", TRACK_BODY)
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


def main(ex_path, site_dir, prev_dir):
    from pages import make_pages
    pages = make_pages(json.load(open(ex_path, encoding="utf-8")))
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
                sm.append(f'  <url><loc>{pg["canonical"]}</loc><lastmod>{pg.get("modified") or TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        shutil.copy(os.path.join(HERE, "robots.txt"), os.path.join(root, "robots.txt"))
    used = {"mm-gutters-exteriors-logo.png", "favicon.png"}
    for dp, _, fs in os.walk(prev_dir):
        for f in fs:
            if f.endswith(".html"): used |= set(re.findall(r"assets/img/([\w.-]+)", open(os.path.join(dp, f), encoding="utf-8").read()))
    imgdir = os.path.join(prev_dir, "assets", "img")
    for f in os.listdir(imgdir):
        if f not in used: os.remove(os.path.join(imgdir, f))
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main(*sys.argv[1:4])
