"""Shared build engine for the Novarte site drafts. Each site's _build has its own cfg (facts), design (header, footer, CSS)
and pages. The engine does the plumbing: images, schema helpers, link resolving, preview vs site output, sitemap.
  site/    : files to put live (folder per page, clean links, the client's tracking kept)
  preview/ : private review copy (links to index.html, CSS/JS inline, forms off, draft strip, home in home/)"""
import json, os, re, html, shutil

C = None  # the site's cfg module


def setup(cfg):
    global C, IMG
    C = cfg
    IMG = json.load(open(os.path.join(cfg.HERE, "imgmeta.json"), encoding="utf-8")) if os.path.exists(os.path.join(cfg.HERE, "imgmeta.json")) else {}


def canon(path):
    if path == "": return C.U
    return C.U + (path if C.TRAIL else path.rstrip("/"))


def img(name, alt, cls="", lazy=True, priority=False):
    w, h, _ = IMG[name]
    ext = "png" if name.endswith("-logo") or name.endswith("-logo-white") else "webp"
    a = [f'src="@img/{name}.{ext}"', f'alt="{html.escape(alt, quote=True)}"', f'width="{w}"', f'height="{h}"']
    if cls: a.append(f'class="{cls}"')
    a.append('fetchpriority="high"' if priority else ('loading="lazy"' if lazy else ""))
    a.append('decoding="async"')
    return "<img " + " ".join(x for x in a if x) + ">"


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


def faq_html(faqs, open_first=True):
    out = []
    for i, (q, a) in enumerate(faqs):
        a = a if a.lstrip().startswith("<") else f"<p>{a}</p>"
        out.append(f'<details{" open" if (i == 0 and open_first) else ""}><summary><span class="q-n">{i + 1:02d}</span>{q}</summary><div class="a">{a}</div></details>')
    return '<div class="faq">' + "".join(out) + "</div>"


def head(page):
    url = page.get("canonical") or canon(page["path"])
    graph = C.biz(page.get("full_biz", True)) + [{"@type": "WebSite", "@id": C.U + "#website", "url": C.U, "name": C.NAME, "publisher": {"@id": C.U + "#business"}, "inLanguage": "en-US"}] + page.get("schema", [])
    ld = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1).replace("</", "<\\/")
    og = C.U + "assets/img/" + (page.get("og") or C.HOME_OG) + ".webp"
    t = html.escape(page["title"], quote=False); m = html.escape(page["meta"], quote=True)
    cn = f'<link rel="canonical" href="{page["canonical"]}">' if page.get("canonical") else ""
    return f'''<!doctype html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{m}">
<meta name="robots" content="{page.get("robots", "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1")}">
{cn}
<meta property="og:type" content="{page.get("ogtype", "website")}">
<meta property="og:site_name" content="{html.escape(C.NAME)}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{m}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="{C.THEME_COLOR}">
<link rel="icon" type="image/png" href="@img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{C.FONTS}">
<link rel="stylesheet" href="@root/assets/style.css">
<script>document.documentElement.classList.add('js')</script>
@@TRACK@@
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
        if p not in known: return canon(p) + frag
        if mode == "preview": return pre + (p or "home/") + "index.html" + frag
        return (pre + p or "./") + frag
    doc = re.sub(r'@/([A-Za-z0-9\-/\._#%]*)', link, doc)
    return doc.replace("@img/", pre + "assets/img/").replace("@root/", pre)


def render(page, mode, known, header, footer):
    draft = f'<div class="draft-strip">DRAFT PREVIEW for {C.DOMAIN} &middot; made by Novarte AI for review &middot; not the live site</div>\n' if mode == "preview" else ""
    doc = (head(page) + "\n<body>\n" + draft + header() + '\n<main id="main">\n' + page["body"] + "\n</main>\n" + footer() +
           '\n<script src="@root/assets/site.js" defer></script>\n</body>\n</html>\n')
    doc = resolve(doc, page, mode, known)
    if mode == "site":
        doc = doc.replace("@@TRACK@@", getattr(C, "TRACK_HEAD", "") or "")
    else:
        pre = "../" * page["path"].count("/")
        doc = doc.replace("@@TRACK@@\n", "")
        css = open(os.path.join(C.HERE, "style.css"), encoding="utf-8").read()
        js = open(os.path.join(C.HERE, "site.js"), encoding="utf-8").read()
        doc = doc.replace(f'<link rel="stylesheet" href="{pre}assets/style.css">', "<style>\n" + css + "\n</style>")
        doc = doc.replace(f'<script src="{pre}assets/site.js" defer></script>', "<script>\n" + js + "\n</script>")
        doc = re.sub(r'<form class="form"[^>]*>', '<form class="form" onsubmit="return false">', doc)
        doc = re.sub(r'<button class="btn" type="submit">[^<]*', '<button class="btn" type="button" disabled>Form is off in this preview ', doc)
    return doc


def build(site_dir, prev_dir, pages, header, footer):
    known = {p["path"] for p in pages}
    for mode, root in (("site", site_dir), ("preview", prev_dir)):
        os.makedirs(os.path.join(root, "assets"), exist_ok=True)
        if mode == "site":
            shutil.copy(os.path.join(C.HERE, "style.css"), os.path.join(root, "assets", "style.css"))
            shutil.copy(os.path.join(C.HERE, "site.js"), os.path.join(root, "assets", "site.js"))
        else:
            for sub in ("img", "video"):
                if os.path.isdir(os.path.join(site_dir, "assets", sub)):
                    shutil.copytree(os.path.join(site_dir, "assets", sub), os.path.join(root, "assets", sub), dirs_exist_ok=True)
        for pg in pages:
            if mode == "preview" and pg["path"] == "": pg = dict(pg, path="home/")
            # this site's URLs are files ("about-us.html", "sump-pump/system.html"); the home stays a folder index
            out = os.path.join(root, pg["path"]) if pg["path"].endswith(".html") else os.path.join(root, pg["path"], "index.html")
            if os.name == "nt": out = "\\\\?\\" + os.path.abspath(out)  # some blog URLs exceed MAX_PATH inside OUTBOX
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "w", encoding="utf-8", newline="\n").write(render(pg, mode, known, header, footer))
        sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for pg in pages:
            if pg.get("sitemap", True) and pg.get("canonical"):
                sm.append(f'  <url><loc>{pg["canonical"]}</loc><lastmod>{C.TODAY}</lastmod></url>')
        sm.append("</urlset>")
        open(os.path.join(root, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write("\n".join(sm) + "\n")
        open(os.path.join(root, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
            "User-agent: *\nAllow: /\n" + "".join(f"Disallow: {d}\n" for d in getattr(C, "DISALLOW", [])) +
            "\n# AI search and answer engines are welcome\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\n\n"
            f"Sitemap: {C.U}sitemap.xml\n")
    print("built", len(pages), "pages")
