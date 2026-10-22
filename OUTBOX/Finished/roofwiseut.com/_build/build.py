"""Builds the roofwiseut.com redesign.

  python -I build.py <out_site> <out_preview>

The current site is a Lovable app on the client's domain. Same 10 URLs (no trailing slash, as today), each with its
own absolute canonical, plus a new blog post. The old robots.txt and sitemap point to roofwise-clear-path.lovable.app;
the new ones point to roofwiseut.com.
site/    : files to put live. Each URL is a folder with index.html; links are root-relative ("/roof-repair").
           The host must serve /about from about/index.html without forcing a trailing slash.
preview/ : private review copy (relative links, forms off, CSS/JS inline; site home in home/)
The current site has Lovable's own scripts but no analytics tag of the client's to keep.
"""
import json, os, re, sys, html, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
U = "https://roofwiseut.com"
BIZ_ID = U + "/#business"
TODAY = "2026-10-17"
HOME_OG = "drone-reroof-crew-on-roof"
IMG = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))

# Contact details exactly as the current site shows them (17 Oct 2026). The site shows no street address and no hours;
# the Google profile's address is not used until the client confirms it (see notes).
S = {"name": "RoofWise", "email": "roofwisesaltlake@gmail.com", "phone": "(435) 655-1246", "tel": "+14356551246"}
COUNTIES = ["Weber County", "Davis County", "Salt Lake County", "Utah County", "Tooele County", "Wasatch County"]

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7"/></svg>'
INFO = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></svg>'
SCHED = "schedule-inspection"

SERVICES = [("roof-replacement", "Roof Replacement", "A clear replacement plan, quality materials, and workmanship built to last."),
            ("roof-repair", "Roof Repair", "Leaks, damaged shingles, storm and wind damage, flashing issues."),
            ("insurance-claims", "Insurance Claims Help", "Inspection, documentation and roofing-side guidance when storm damage may be involved."),
            ("commercial-roofing", "Commercial Roofing", "Inspections, clear project scope and practical planning for commercial properties."),
            ("gutters", "Gutters", "Gutter installation and repair that moves water away from the roofline and foundation.")]
BLOG = ("What Does Hail Damage Look Like on a Roof?", "blog/what-does-hail-damage-look-like-on-a-roof")


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    a = [f'src="@img/{name}.webp"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


def canon(path):
    return U + "/" + path if path else U + "/"


def biz(full=True):
    n = {"@type": "RoofingContractor", "@id": BIZ_ID, "name": S["name"], "url": U + "/", "telephone": S["tel"], "email": S["email"],
         "logo": U + "/assets/img/roofwise-logo.png", "image": U + "/assets/img/" + HOME_OG + ".webp",
         "areaServed": [{"@type": "AdministrativeArea", "name": c + ", Utah"} for c in COUNTIES]}
    if full:
        n.update({"description": "RoofWise is a licensed and insured roofing contractor serving Salt Lake City and Northern Utah: roof inspections, roof repair, roof replacement with a 10-year workmanship warranty, insurance-related roofing, commercial roofing and gutters.",
                  "slogan": "Your trusted roofing experts",
                  "knowsAbout": ["Roof inspection", "Roof repair", "Roof replacement", "Storm damage", "Hail damage", "Insurance claims", "Commercial roofing", "Gutters"]})
    return [n]


def crumbs_ld(path, trail):
    return {"@type": "BreadcrumbList", "@id": canon(path) + "#breadcrumb", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": html.unescape(re.sub(r"<[^>]+>", "", n)), "item": canon(p)} for i, (n, p) in enumerate(trail)]}


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


def notice(text):
    """Ready.gov-style notice box (used for the client's own insurance disclaimer)."""
    return f'<div class="notice" role="note"><i>{INFO}</i><p>{text}</p></div>'


DISCLAIMER = "Insurance coverage and claim decisions are determined by your insurance policy and insurance carrier. Final coverage decisions are made by the insurance carrier according to the applicable policy."


def header():
    svc = "".join(f'<a href="@/{p}"><span class="n">{i + 1:02d}</span><b>{n}</b><small>{d}</small></a>' for i, (p, n, d) in enumerate(SERVICES))
    msvc = "".join(f'<a href="@/{p}">{n}</a>' for p, n, _ in SERVICES)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="RoofWise home">{img("roofwise-logo", "Roof-Wise, your trusted roofing experts", lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop"><div class="drop-grid">{svc}<a class="drop-sched" href="@/{SCHED}"><span class="n">06</span><b>Roof Inspection</b><small>Not sure what&rsquo;s wrong? Start here.</small></a></div></div></details></li>
<li><a href="@/service-area">Service area</a></li><li><a href="@/about">About</a></li><li><a href="@/{BLOG[1]}">Hail guide</a></li><li><a href="@/contact">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}"><small>Call RoofWise</small><strong>{S["phone"]}</strong></a><a class="btn" href="@/{SCHED}">Schedule Inspection</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><p class="mh">Services</p><div class="sub">{msvc}</div>
<a href="@/service-area">Service area</a><a href="@/about">About</a><a href="@/{BLOG[1]}">Hail damage guide</a><a href="@/contact">Contact</a>
<a class="btn" href="@/{SCHED}">Schedule Inspection</a><a class="menu-phone" href="tel:{S["tel"]}">{S["phone"]}</a></div></details>
</div></header>'''


def footer():
    svc = "".join(f'<li><a href="@/{p}">{n}</a></li>' for p, n, _ in SERVICES)
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Inspect. Document. <em>Understand.</em></p><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a></div>
<div class="foot">
<div class="fbrand"><span class="logo-chip">{img("roofwise-logo", "RoofWise logo", cls="logo")}</span>
<p>Quality roofing solutions for Northern Utah homeowners and property owners. Licensed and insured.</p></div>
<div><h3>Services</h3><ul>{svc}<li><a href="@/{SCHED}">Roof inspection</a></li></ul></div>
<div><h3>Company</h3><ul><li><a href="@/about">About</a></li><li><a href="@/service-area">Service area</a></li><li><a href="@/{BLOG[1]}">Hail damage guide</a></li><li><a href="@/contact">Contact</a></li></ul></div>
<div><h3>Contact</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br><a href="mailto:{S["email"]}">{S["email"]}</a></p>
<p class="small-print">Serving {", ".join(c.replace(" County", "") for c in COUNTIES[:-1])} and {COUNTIES[-1].replace(" County", "")} counties</p></div>
</div>
<p class="fnote">{DISCLAIMER}</p>
<p class="foot-word" aria-hidden="true">RoofWise</p>
<div class="fbottom"><span>&copy; 2026 RoofWise &middot; Licensed &amp; insured in Utah</span><span><a href="@/sitemap.xml">Sitemap</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{SCHED}">Schedule Inspection</a></div>'''


def cta(title="Let RoofWise take a look first", text="You don&rsquo;t have to know whether it&rsquo;s storm damage, age, a leak or an insurance matter before you schedule an inspection.", image="drone-reroof-full-property"):
    return f'''<section class="cta"><div class="cta-bg">{img(image, "")}</div><div class="wrap"><div class="reveal vf-box"><p class="label light">Roof inspection</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="reveal cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call RoofWise</small><b>{S["phone"]}</b></a><a class="btn" href="@/{SCHED}">Schedule Inspection {ARROW}</a>
<a class="cta-mail" href="mailto:{S["email"]}">{S["email"]}</a></div></div></section>'''


def report_head(rows):
    """NWS-style 'issued / valid' stamp: label/value pairs."""
    return '<dl class="stamp">' + "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows) + "</dl>"


PH_DEFAULT = ["drone-reroof-hillside-home", "drone-reroof-underlayment", "drone-reroof-full-property", "drone-reroof-crew-on-roof"]


def phero(trail, h1, lede, label, rows=None, image=None, alt="", buttons=True):
    # Every inner page opens on a frame of the client's drone footage; pages without their own photo get one as a darkened backdrop
    bg = image or PH_DEFAULT[sum(map(ord, trail[-1][1])) % len(PH_DEFAULT)]
    st = f'<div class="ph-stamp">{report_head(rows)}</div>' if rows else ""
    btns = f'<div class="btn-row"><a class="btn" href="@/{SCHED}">Schedule Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else " dim"}"><div class="ph-bg">{img(bg, alt if image else "", priority=True)}</div><div class="vf" aria-hidden="true"></div>
<div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}
<p class="label light">{label}</p><h1>{h1}</h1><p class="lede">{lede}</p>{btns}</div>{st}</div></section>'''


def contact_form(title="Send a short note"):
    # Same fields as the current contact form; it needs a form handler before go-live (see notes).
    return f'''<form class="form" method="post" action="" enctype="multipart/form-data">
<h3>{title}</h3>
<div class="row"><label for="f-first">First name *<input id="f-first" name="first_name" autocomplete="given-name" required></label><label for="f-last">Last name *<input id="f-last" name="last_name" autocomplete="family-name" required></label></div>
<div class="row"><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label></div>
<label for="f-addr">Property address<input id="f-addr" name="address" autocomplete="street-address"></label>
<label for="f-msg">How can we help? *<textarea id="f-msg" name="message" required></textarea></label>
<fieldset class="radios"><legend>Preferred contact method</legend><label><input type="radio" name="contact_method" value="phone" checked> Phone</label><label><input type="radio" name="contact_method" value="email"> Email</label><label><input type="radio" name="contact_method" value="text"> Text</label></fieldset>
<label for="f-photo">Optional photo upload<input id="f-photo" type="file" name="photo" accept="image/*"></label>
<button class="btn" type="submit">Send Message {ARROW}</button></form>'''


def head(page):
    url = canon(page["path"]) if page["path"] != "404.html" else U + "/"
    graph = biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": U + "/#website", "url": U + "/", "name": S["name"], "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = U + "/assets/img/" + (page.get("og") or HOME_OG) + ".webp"
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
<meta property="og:site_name" content="RoofWise">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b0f0d">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&family=Inter+Tight:ital,wght@0,600;0,700;0,800;1,500;1,600&family=JetBrains+Mono:wght@500;600&display=swap">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">
{ld}
</script>
</head>'''


def out_path(path, mode):
    if path == "404.html": return "404.html"
    if mode == "preview" and path == "": return "home/index.html"
    return (path + "/" if path else "") + "index.html"


def resolve(doc, page, mode, known):
    here = out_path(page["path"], mode)
    pre = "../" * here.count("/")

    def link(m):
        p = m.group(1)
        frag = ""
        if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
        if p.endswith((".xml", ".txt")): return ("/" + p if mode == "site" else pre + p) + frag
        if p not in known: return U + "/" + p + frag
        if mode == "site": return "/" + p + frag
        return pre + out_path(p, mode) + frag
    doc = re.sub(r'@/([A-Za-z0-9\-_/\.#]*)', link, doc)
    if mode == "site":
        return doc.replace("@img/", "/assets/img/").replace("@root/", "/")
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known):
    draft = '<div class="draft-strip">DRAFT PREVIEW for roofwiseut.com &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
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
    print("built", len(pages), "pages")


if __name__ == "__main__":
    main(*sys.argv[1:3])
