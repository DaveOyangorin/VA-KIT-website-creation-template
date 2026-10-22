"""Pages for the mandmgutters.com redesign, on the client's current 183 URLs plus a new blog post and a 404.

Content comes from the client's own pages (extract.json, 17 Oct 2026): the service and company pages keep the
client's copy, cleaned of page-builder leftovers, under new Salt Lake City titles, H1s and opening answers
(overrides.py). Blog posts are rebuilt on their URLs with their own text. Images: only the client's real job photos
(imgmap.json); stock, Bannerbear banners and Unsplash hotlinks are dropped from every page.
Facts used: started 1990; Nate Nuttall joined 2005, bought the business 2010, owner; family-owned; residential and
commercial; copper, aluminum and steel gutters; seamless gutters made on site; 5" and 6" K-style; HOVER 3D models;
financing plans (OAC); hours Mon-Fri 8-5; the six counties in the footer. The review count on the site (413) differs
from the Google profile in the report (427), so no count or stars are shown.
"""
import re, html
from build import (U, S, ARROW, PHONE, CHECK, QUOTE, CONTACT, SERVICES, BLOG, COUNTIES, IMG, IMGMAP, img, phero, cta, faq_html, faq_ld,
                   crumbs_ld, quote_form)
from overrides import OVERRIDES
import p_blog

HOME = ("Home", "")
STAFF = [("We&rsquo;re not going to sell you a job that you don&rsquo;t need.", "James Connors, Sales Manager"),
         ("We saw the need for more correlation between home services. Nothing is worse than when you go to a job site and the person there is blaming the person before. We want to be an advocate for the homeowner to get the full project done.", "Nate Nuttall, Owner")]
JUNK = re.compile(r"^(learn more!?|read more|get started|submit|get a free quote|click for hover|see all reviews|schedule your exterior tune-up|quote your next project today!?|convinced\? let.s get to work\.?|contact us|call now|request a quote)$", re.I)
GALLERY = ["mm-exteriors-image-21-2", "copper-gutter-4", "image-9", "image-3-with-blue-square", "heat-cable-zig-zagging3", "image-6-with-blue-square",
           "mm-exteriors-image-10", "copper-gutter-6", "soffit-and-fascia", "image-10-with-orange-box", "img-20180913-151545", "standing-seam-metal-roof-custom-steel-snow-rail-and-gutterrx",
           "mm-exteriors-image-16", "heat-cable", "mg-6540", "house-2", "pillars", "window", "mm-exteriors-image-5", "image-4-with-orange-square-1",
           "cedar-soffit-or-siding", "utahs-preferred-ice-melt-systems", "image-8", "mm-exteriors-image-17"]


def local(name):
    return name if name in IMG else None


def find_img(src):
    base = src.split("?")[0].rsplit("/", 1)[-1].lower()
    base = re.sub(r"-\d+x\d+(?=\.\w+$)", "", base)
    for k in (base, re.sub(r"\.(jpe?g|png|webp)$", ".jpg", base), re.sub(r"\.(jpe?g|png|webp)$", ".png", base), re.sub(r"\.(jpe?g|png|webp)$", ".jpeg", base)):
        if k in IMGMAP: return IMGMAP[k]
    stem = re.sub(r"\.\w+$", "", base)
    for k, v in IMGMAP.items():
        if re.sub(r"(-scaled|_resized|-min)?\.\w+$", "", k) == re.sub(r"(-scaled|_resized|-min)$", "", stem): return v
    return None


FIXLINKS = {"roofing-2/": "services/roofing/", "siding/": "services/exterior-siding/", "rain-gutters/": "services/rain-gutters-installation/",
            "windows-2/": "services/windows/", "soffit-fascia/": "services/fascia-and-soffit-installation/", "about-us/": "about-mm-gutters-exteriors/",
            "contact/": "contact-us/", "heating-cables/": "services/roof-heat-cable-installation/", "roof-inspection/": "services/roofing/", "mm_gutter-cleaning/": "services/rain-gutters-installation/",
            "blog/how-long-do-a-roof-last-in-utah/": "blog/how-long-does-a-roof-last-in-utah/", "blog/how-do_gutters-protect-your-home/": "blog/how-do-gutters-protect-your-home/",
            "blog/clog-free-living-top-gutter-city-living-top-gutter-guard-solutions-in-salt-lake-city/": "blog/clog-free-living-top-gutter-guard-solutions-in-salt-lake-city/",
            "blog/3-common-reasons-your-gutter-system-is-leaking/": "blog/3-common-reasons-why-your-gutter-system-is-leaking/"}
UNLINK = {"service-areas/", "blog/category/fascia-and-soffit/"}
FIXED = {}   # old link -> new target, for the notes


def fix_path(p, known):
    """Old or mistyped internal links on the current site -> the real page (they redirect or 404 today)."""
    if p in known: return p
    q = FIXLINKS.get(p) or next((c for c in ("blog/" + p, "services/" + p) if c in known), None)
    if q: FIXED[p] = q
    return q


def clean(content, known):
    """Client content -> safe HTML: real images local, junk button text gone, internal links resolved."""
    def im(m):
        src = html.unescape(m.group(1)); alt = html.unescape(m.group(2))
        n = find_img(src)
        if not n: return ""
        return f'<figure>{img(n, alt or "M&M Gutters & Exteriors project")}</figure>'
    c = re.sub(r'<img src="([^"]*)" alt="([^"]*)">', im, content)

    def a(m):
        href = html.unescape(m.group(1))
        mm = re.match(r"^(?:https?:)?//(?:www\.)?mandmgutters\.com/(.*)$", href) or (re.match(r"^/(?!/)(.*)$", href))
        if mm:
            p = mm.group(1).split("?")[0]
            frag = ""
            if "#" in p: p, frag = p.split("#", 1); frag = "#" + frag
            if p and not p.endswith("/") and "." not in p.rsplit("/", 1)[-1]: p += "/"
            if p in UNLINK or p.startswith("wp-content/"): return '<a href="#">'
            q = fix_path(p, known)
            if q is not None: return f'<a href="@/{q}{frag}">'
            return f'<a href="{U}{p}{frag}">'
        if href.startswith(("tel:", "mailto:")): return f'<a href="{html.escape(href)}">'
        if href.startswith("http"): return f'<a href="{html.escape(href)}" rel="noopener">'
        return "<a>"
    c = re.sub(r'<a href="([^"]*)">', a, c)
    c = re.sub(r'<a href="#">(.*?)</a>', r"\1", c)
    c = re.sub(r"<a>(.*?)</a>", r"\1", c)
    # drop junk short paragraphs/headings (button labels) and empty wrappers
    def junk(m):
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        return "" if (not t and "<figure" not in m.group(2)) or JUNK.match(t) else m.group(0)
    for _ in range(2):
        c = re.sub(r"<(p|h2|h3|h4|li|strong)>(.*?)</\1>", junk, c)
    c = re.sub(r"<(ul|ol)></\1>", "", c)
    c = re.sub(r"<figure>(<figure>.*?</figure>)</figure>", r"\1", c)
    c = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", c)
    c = re.sub(r"<h2>([^<]{3,})</h2>", lambda m: "<h2>" + (m.group(1).title() if m.group(1).isupper() else m.group(1)) + "</h2>", c)
    c = re.sub(r"<h3>([^<]{3,})</h3>", lambda m: "<h3>" + (m.group(1).title() if m.group(1).isupper() else m.group(1)) + "</h3>", c)
    c = re.sub(r"<table>", '<div class="tablebox"><table>', c); c = re.sub(r"</table>", "</table></div>", c)
    # an all-caps line at the top repeats the page title from the old page builder
    c = re.sub(r"^\s*<p>([^<a-z]{12,90})</p>", "", c)
    # runs of two or more photos sit side by side, as on the old layout
    c = re.sub(r"((?:\s*<figure>(?:(?!</figure>).)*</figure>){2,})", r'<div class="figs">\1</div>', c)
    return c


def first_para(content, n=158):
    for p in re.findall(r"<p>(.*?)</p>", content):
        t = html.unescape(re.sub(r"<[^>]+>", "", p)).strip()
        if len(t) > 60:
            if len(t) <= n: return t
            cut = t[:n].rsplit(" ", 1)[0].rstrip(",;:")
            return cut + "."
    return ""


def first_img(content):
    m = re.search(r'src="@img/([\w-]+)\.webp"', content)
    return m.group(1) if m else None


def strip_title(t):
    return re.sub(r"\s*[-|–]\s*M&M Gutters( (&|and) Exteriors)?\s*$", "", t).strip()


def topic(title):
    t = title.lower()
    for k, words in [("Leaf guards", ("leaf", "gutter guard", "guards")), ("Heat cable &amp; ice", ("heat", "ice", "melting", "winter")),
                     ("Windows &amp; doors", ("window", "glass", "door", "sash", "screen", "pane")), ("Siding &amp; stucco", ("siding", "stucco", "stone", "mold")),
                     ("Roofing", ("roof", "felt", "shingle", "metal", "astm", "decking")), ("Gutters", ("gutter", "downspout", "rain")),
                     ("Soffit &amp; fascia", ("soffit", "fascia", "eave"))]:
        if any(w in t for w in words): return k
    return "Home maintenance"


# Hero photo per service page: the clearest large job photo of that service (no framed or captioned graphics)
HERO = {"services/": "20140530-144851", "services/rain-gutters-installation/": "copper-gutter-4",
        "services/rain-gutters-installation/rain-gutter-installation-process/": "copper-gutter-6", "services/leaf-guards/": "down-net-http20250501-83-7dvz01",
        "services/roof-heat-cable-installation/": "heat-cable1", "services/ice-melting-systems/": "heat-cable7",
        "services/fascia-and-soffit-installation/": "cedar-soffit-or-siding", "services/roofing/": "utah-rainer-gutters-01-2",
        "services/roofing/gaf-roofing/": "utah-rainer-gutters-05", "services/windows/": "down-net-http20240904-65-v2w3su-1",
        "services/exterior-siding/": "siding-repair-services", "services/stucco-stone-siding-in-salt-lake-city/": "heat-cable-zig-zagging3",
        "services/financing/": "mg-6540-55"}
BENTO = [("copper-gutter-4", "Copper gutters and downspouts", "Rain gutters", "services/rain-gutters-installation/"),
         ("heat-cable-zig-zagging3", "Heat cable on a stone and stucco home in winter", "Heat cable", "services/roof-heat-cable-installation/"),
         ("utah-rain-gutters-company-03-1024x683-2", "Copper downspout detail", "Copper", "services/rain-gutters-installation/"),
         ("cedar-soffit-or-siding", "Cedar soffit on a covered porch", "Soffit", "services/fascia-and-soffit-installation/"),
         ("utah-rainer-gutters-05", "Roof edge and gutters above the valley", "Gutters", "services/rain-gutters-installation/"),
         ("down-net-http20240904-65-v2w3su-1", "A wall of new windows", "Windows", "services/windows/"),
         ("soffit-fascia", "Soffit and fascia on a commercial building", "Commercial", "services/fascia-and-soffit-installation/")]


def side_services(cur=None):
    lis = "".join(f'<li><a href="@/{p}"><span class="n">{i + 1:02d}</span>{n}</a></li>' for i, (k, n, p, _) in enumerate(SERVICES) if p != cur)
    return f'''<aside class="side reveal"><div class="panel dark"><p class="label light">Free quote</p><h3>Talk to M&amp;M</h3><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><p class="small">{S["hours"]}</p><a class="btn" href="@/{QUOTE}">Get a Free Quote {ARROW}</a></div>
<div class="panel"><p class="label">Roof to ground</p><ul class="svc-links">{lis}</ul></div></aside>'''


# The signature drawing: a section through a house's eave, with the water's path from the roof to the ground.
# Hotspots are the eight services in the order water meets them.
HOTSPOTS = {"roof": (168, 108, "Roof"), "cable": (388, 196, "Heat cable"), "guard": (474, 232, "Leaf guard"), "gutter": (540, 288, "Gutter"),
            "soffit": (384, 318, "Soffit &amp; fascia"), "window": (306, 376, "Window"), "siding": (348, 468, "Siding"), "stucco": (348, 534, "Stone &amp; stucco")}


def water_svg():
    y = lambda x: 64 + (x - 20) * 192 / 432          # roof surface
    shingles = "".join(f'<path d="M{x} {y(x):.1f} l-6 14"/>' for x in range(40, 440, 22))
    zz = " ".join(f"{x},{(y(x) - (0 if i % 2 else 22)):.1f}" for i, x in enumerate(range(336, 446, 11)))
    laps = "".join(f'<path d="M318 {v} l12 3 v26"/>' for v in list(range(298, 326, 29)) + list(range(424, 500, 29)))
    stones = "".join(f'<rect x="{318 + (j % 2) * 3}" y="{506 + j * 13}" width="12" height="11" rx="2"/>' for j in range(4))
    soil = "".join(f'<path d="M{x} 566 l-10 14"/>' for x in range(14, 640, 22))
    vents = "".join(f'<path d="M{x} 293 v6"/>' for x in range(334, 438, 8))
    rain = "".join(f'<path class="rd" style="animation-delay:-{(i * 0.37) % 1.6:.2f}s" d="M{x} {8 + (i * 17) % 30} l-7 16"/>' for i, x in enumerate(range(40, 470, 26)))
    hs = "".join(f'<g class="hs" data-k="{k}" transform="translate({HOTSPOTS[k][0]} {HOTSPOTS[k][1]})"><circle r="13"/><text y="4.5">{i + 1:02d}</text><text class="lbl" x="19" y="4">{HOTSPOTS[k][2]}</text></g>'
                 for i, (k, *_) in enumerate(SERVICES))
    wp = "M40 66 L448 248 Q468 254 478 268 L491 302 L491 540 Q491 554 506 554 L620 554"
    drops = "".join(f'<circle class="drop" r="3.4"><animateMotion dur="7s" repeatCount="indefinite" begin="-{i * 1.75}s"><mpath href="#wpath"/></animateMotion></circle>' for i in range(4))
    return f'''<svg class="section-drawing" viewBox="0 0 640 600" role="img" aria-labelledby="sd-t sd-d">
<title id="sd-t">The path of the water</title><desc id="sd-d">A section drawing through the eave of a house: rain runs down the roof, past the heat cable, into the gutter under a leaf guard, past the soffit and fascia, down the downspout beside the windows, siding and stone, and away from the foundation.</desc>
<defs><pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none"/></pattern>
<pattern id="hatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V8"/></pattern></defs>
<rect class="grid" width="640" height="600" fill="url(#grid)"/>
<g class="rain">{rain}</g>
<g class="ln">
<path class="thick" d="M20 64 L452 256"/><path d="M20 90 L440 277"/>{shingles}
<path class="fill" d="M296 212 L318 222 V296 H296 Z" fill="url(#hatch)"/>
<path d="M20 300 H296"/><path class="ins" d="M24 296 q6 -10 12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0 t12 0"/>
<rect x="440" y="250" width="12" height="48"/><path d="M318 298 H440"/>{vents}
<path d="M296 212 V560 M318 222 V560"/><path class="fill" d="M296 330 H318 V420 H296 Z M296 440 H318 V560 H296 Z" fill="url(#hatch)"/>
<rect class="glass" x="290" y="330" width="34" height="90"/><path d="M307 330 V420 M290 375 H324"/>{laps}{stones}
<path class="k" d="M452 258 V300 H500 Q510 300 508 290 Q504 280 512 272 L514 258"/><path class="mesh" d="M450 256 H516"/>
<path d="M484 300 V540 Q484 548 492 548 H540 M498 300 V538"/><rect x="530" y="556" width="62" height="7"/>
<path class="thick" d="M0 560 H640"/><g class="soil">{soil}</g>
</g>
<polyline class="cable" points="{zz}"/>
<path id="wpath" class="water-line" d="{wp}"/>{drops}
<g class="hots">{hs}</g>
<g class="dims"><path d="M610 256 V560"/><path d="M604 256 H616 M604 560 H616"/><text x="622" y="408" transform="rotate(90 622 408)">roof edge to grade</text></g>
</svg>'''


def path_of_water(active=None):
    """Services in the order water meets them, from the roof to the ground (compact rail used on inner pages)."""
    steps = "".join(f'<li class="{"on" if p == active else ""}"><a href="@/{p}"><span class="n">{i + 1:02d}</span><i class="ic {k}"></i><b>{n}</b><span class="d">{d}</span></a></li>' for i, (k, n, p, d) in enumerate(SERVICES))
    return f'<ol class="water">{steps}</ol>'


def service_page(r, known):
    p = r["path"]; o = OVERRIDES.get(p, {})
    body_html = clean(r["content"], known)
    image = HERO.get(p) or o.get("img") or first_img(body_html)
    trail = [HOME, ("Services", "services/"), (o.get("crumb") or strip_title(r["title"]), p)] if p != "services/" else [HOME, ("Services", "services/")]
    if p.count("/") == 3: trail = [HOME, ("Services", "services/"), (o.get("parent_name", ""), o.get("parent", "")), (o.get("crumb") or strip_title(r["title"]), p)]
    faqs = o.get("faqs")
    idx = next((i for i, s in enumerate(SERVICES) if s[2] == p), None)
    if idx is not None:
        prv = SERVICES[idx - 1] if idx else None
        nxt = SERVICES[idx + 1] if idx + 1 < len(SERVICES) else None
        prv_html = f'<a href="@/{prv[2]}">&larr; {prv[1]}</a>' if prv else '<span>Rain starts here</span>'
        nxt_html = f'<a href="@/{nxt[2]}">{nxt[1]} &rarr;</a>' if nxt else '<span>Then the ground</span>'
        pos = f'''<div class="pos"><p class="label">On the path of the water</p><p class="pos-n"><b>{idx + 1:02d}</b><span>of 08</span></p>
<div class="pos-bar"><i style="width:{(idx + 1) / len(SERVICES) * 100:.1f}%"></i></div><p class="pos-nav">{prv_html}{nxt_html}</p></div>'''
    else:
        pos = f'<div class="pos"><p class="label">Free quote</p><p class="pos-call"><a href="tel:{S["tel"]}">{S["phone"]}</a></p><p class="small">{S["hours"]}</p></div>'
    intro = f'<section class="intro"><div class="wrap intro-grid"><div class="reveal intro-lead">{o["lead"]}</div><div class="reveal">{pos}</div></div></section>' if o.get("lead") else ""
    faq_sec = f'<section class="sec paper"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>Common questions</h2><p class="lede">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div><div class="reveal">{faq_html(faqs)}</div></div></section>' if faqs else ""
    body = phero(trail, o.get("h1") or r["h1"], o.get("lede", ""), "Salt Lake City, Utah", image, o.get("alt", "M&M Gutters & Exteriors project")) + intro + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{body_html}</div>{side_services(p)}</div></section>
{faq_sec}
<section class="sec navy"><div class="wrap"><div class="head row reveal"><div><p class="label light">The path of the water</p><h2>Every part of the exterior, roof to ground</h2></div><a class="more light" href="@/services/">All services {ARROW}</a></div>{path_of_water(p)}</div></section>''' + cta()
    schema = [crumbs_ld(U + p, trail)]
    if o.get("service"):
        schema.append({"@type": "Service", "@id": U + p + "#service", "name": o["service"], "serviceType": o["service"], "provider": {"@id": U + "#organization"},
                       "areaServed": {"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}}, "description": html.unescape(re.sub(r"<[^>]+>", "", o.get("lead", "")))})
    if faqs: schema.append(faq_ld(faqs))
    return {"path": p, "canonical": U + p, "title": o.get("title") or r["title"], "meta": o.get("meta") or r["meta"] or first_para(r["content"]),
            "body": body, "og": image, "full_biz": False, "schema": schema, "modified": r.get("modified")}


def toc(body_html):
    """Adds ids to the article's h2s and returns (body, contents list)."""
    items = []
    def h2(m):
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        sid = re.sub(r"[^a-z0-9]+", "-", html.unescape(t).lower()).strip("-")[:48] or f"s{len(items)}"
        if any(sid == i for i, _ in items): sid += f"-{len(items)}"
        items.append((sid, t)); return f'<h2 id="{sid}">{m.group(1)}</h2>'
    body_html = re.sub(r"<h2>(.*?)</h2>", h2, body_html)
    lis = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    return body_html, (f'<nav class="toc" aria-label="In this article"><p class="label">In this article</p><ol>{lis}</ol></nav>' if len(items) >= 2 else "")


def article(body_html, byline):
    body_html, contents = toc(body_html)
    first = re.search(r"<p>(.*?)</p>", body_html)
    dc = " dc" if first and re.match(r"[A-Za-z]", html.unescape(re.sub(r"<[^>]+>", "", first.group(1))).strip()) else ""
    return f'''<section class="sec article"><div class="wrap art-grid"><aside class="art-side">{contents}
<div class="panel dark small-panel"><p class="label light">Free quote</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{QUOTE}">Get a Free Quote {ARROW}</a></div></aside>
<article class="prose post reveal{dc}"><p class="byline">{byline}</p>{body_html}</article></div></section>'''


def post_page(r, known, posts):
    p = r["path"]
    title = strip_title(r["title"]) or r["h1"]
    body_html = clean(r["content"], known)
    image = first_img(body_html)
    trail = [HOME, ("Blog", "blog/"), (title, p)]
    date = r.get("published") or ""
    author = r.get("author") or S["name"]
    t = topic(title)
    rel = [x for x in posts if x is not r and topic(strip_title(x["title"])) == t][:3]
    rel_html = "".join(f'<li><a href="@/{x["path"]}"><span class="label">{t}</span><b>{html.escape(strip_title(x["title"]))}</b><span class="mono">{x.get("published") or ""}</span></a></li>' for x in rel)
    meta = r["meta"] or first_para(r["content"])
    mins = max(1, round(r["words"] / 230))
    dpart = f" &middot; {date}" if date else ""
    byline = f'By <b>{html.escape(author)}</b>{dpart} &middot; {mins} min read'
    more = f'<section class="sec paper"><div class="wrap"><div class="head reveal"><p class="label">More on {t}</p><h2>Keep reading</h2></div><ul class="cards">{rel_html}</ul></div></section>' if rel_html else ""
    body = phero(trail, html.escape(title), "", f"{t}{dpart}", buttons=False) + article(body_html, byline) + more + cta()
    schema = [crumbs_ld(U + p, trail), {"@type": "BlogPosting", "@id": U + p + "#article", "headline": title[:110], "datePublished": date or None, "dateModified": r.get("modified") or date or None,
              "author": ({"@type": "Person", "name": author} if author != S["name"] else {"@id": U + "#organization"}), "publisher": {"@id": U + "#organization"},
              "mainEntityOfPage": U + p, "image": U + "assets/img/" + (image or "mg-6540") + ".webp", "inLanguage": "en-US", "wordCount": r["words"]}]
    schema[1] = {k: v for k, v in schema[1].items() if v is not None}
    return {"path": p, "canonical": U + p, "title": r["title"], "meta": meta, "body": body, "og": image, "ogtype": "article", "full_biz": False,
            "schema": schema, "modified": r.get("modified") or r.get("published")}


def blog_index(path, posts, title_h1):
    groups = {}
    for r in posts: groups.setdefault(topic(strip_title(r["title"])), []).append(r)
    order = ["Gutters", "Leaf guards", "Heat cable &amp; ice", "Roofing", "Soffit &amp; fascia", "Siding &amp; stucco", "Windows &amp; doors", "Home maintenance"]
    chips = "".join(f'<a href="#t-{i}">{g} <span>{len(groups[g])}</span></a>' for i, g in enumerate(order) if g in groups)
    secs = ""
    for i, g in enumerate(order):
        if g not in groups: continue
        items = sorted(groups[g], key=lambda r: r.get("published") or "", reverse=True)
        lis = "".join(f'<li><a href="@/{r["path"]}"><b>{html.escape(strip_title(r["title"]))}</b><span class="mono">{r.get("published") or ""}</span></a></li>' for r in items)
        secs += f'<section class="topic reveal" id="t-{i}"><div class="topic-head"><span class="n">{len(groups[g]):02d}</span><h2>{g}</h2></div><ul class="post-list">{lis}</ul></section>'
    trail = [HOME, (title_h1, path)]
    body = phero(trail, title_h1, f"{len(posts) + 1} articles from M&amp;M Gutters &amp; Exteriors on gutters, leaf guards, heat cable, roofing, siding and windows for Utah homes.", "Blog", "copper-gutter-6", "Copper gutters on a white stucco home", buttons=False) + f'''
<section class="sec"><div class="wrap"><a class="feature reveal" href="@/{BLOG[1]}"><figure>{img("utah-rain-gutters-company-01-1024x683-2", "White K-style gutters and downspout on a two-story home")}</figure>
<div><p class="label">New guide</p><h2>{BLOG[0]}</h2><p>How to size gutters for a Salt Lake City roof, using NOAA&rsquo;s local rainfall data and the standard sizing method.</p><span class="more">Read the guide {ARROW}</span></div></a>
<nav class="chips reveal" aria-label="Topics">{chips}</nav>{secs}</div></section>''' + cta()
    return body


def home(known):
    faqs = [("Do you install seamless gutters?", "Yes. We fabricate seamless gutters on site, cut to fit your roofline, in copper, aluminum and steel."),
            ("What size gutters do you install?", f"K-style gutters in two sizes: 5-inch, which is standard on most homes, and 6-inch for bigger roofs and heavier runoff. Our guide explains how to choose: <a href=\"@/{BLOG[1]}\">{BLOG[0]}</a>"),
            ("How long does a gutter installation take?", "Most small homes take 2&ndash;6 hours. A two-story home usually takes a full day."),
            ("Can I finance my project?", "Yes, financing is available on all our services, on approved credit. See <a href=\"@/services/financing/\">financing</a>."),
            ("Do you work on commercial buildings?", "Yes. We handle residential and commercial projects, including custom box gutters for commercial properties.")]
    wl = "".join(f'<li data-k="{k}"><a href="@/{p}"><span class="n">{i + 1:02d}</span><span class="t"><b>{n}</b><span>{d}</span></span>{ARROW}</a></li>' for i, (k, n, p, d) in enumerate(SERVICES))
    bento = "".join(f'<figure class="b{i} reveal"><a href="@/{href}">{img(n, alt)}<figcaption><span class="tag">{tag}</span>{alt}</figcaption></a></figure>' for i, (n, alt, tag, href) in enumerate(BENTO))
    body = f'''
<section class="hero"><div class="hero-bg">{img("mg-6540", "Seamless gutters and a finished roof edge around a bay window, installed by M&M", priority=True)}</div>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">M&amp;M Gutters &amp; Exteriors &middot; Salt Lake City &middot; since 1990</p>
<h1>Gutter installation in Salt Lake City, <em>and everything the water touches.</em></h1>
<p class="lede">Seamless rain gutters made on site in copper, aluminum and steel, by a family-owned exterior contractor that also does the roof, heat cable, leaf guards, soffit, fascia, windows and siding.</p>
<div class="btn-row"><a class="btn" href="@/{QUOTE}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="spec"><p class="label light">Spec sheet</p><dl><div><dt>Profile</dt><dd>K-style, 5&Prime; &amp; 6&Prime;</dd></div><div><dt>Metals</dt><dd>Copper &middot; Aluminum &middot; Steel</dd></div><div><dt>Seams</dt><dd>None. Formed on site</dd></div><div><dt>Small homes</dt><dd>Done in 2&ndash;6 hours</dd></div></dl></div>
</div>
<div class="wrap tiles">
<a class="tile" href="@/about-mm-gutters-exteriors/"><b>1990</b><span>Started as a gutter company. Family-owned ever since.</span></a>
<a class="tile" href="@/services/rain-gutters-installation/"><b>On site</b><span>Gutters formed to the exact length of each run. No seams to leak.</span></a>
<a class="tile" href="@/services/"><b>Roof to ground</b><span>One company for every surface the water touches.</span></a></div>
</section>

<section class="pow"><div class="wrap pow-grid">
<div class="pow-text reveal"><p class="label light">The path of the water</p><h2>Rain hits the roof first. <em>We follow it all the way down.</em></h2>
<p class="lede">Water runs off the roof, past the heat cable, into the gutters, behind the fascia and down the siding. Every one of those is an M&amp;M service, so one company can get the whole path right.</p>
<ol class="wlist">{wl}</ol></div>
<div class="pow-draw reveal">{water_svg()}<p class="cap mono">Section through an eave &middot; not to scale</p></div>
</div></section>

<section class="sec materials"><div class="wrap">
<div class="head row reveal"><div><p class="label">Made on site</p><h2>Seamless gutters, cut to the length of your roofline</h2></div><p class="head-note">We form seamless gutters on site, so every run comes off in one piece, sized to the roof above it.</p></div>
<div class="swatches">
<a class="swatch reveal" href="@/services/rain-gutters-installation/">{img("copper-gutter-6", "Copper gutters and downspouts on a white home")}<div><p class="label light">01 &middot; Metal</p><h3>Copper</h3><p>For homes that want the metal to show: copper gutters and downspouts, alongside aluminum and steel.</p></div></a>
<a class="swatch reveal" href="@/blog/5-inch-vs-6-inch-gutters/">{img("utah-rain-gutters-company-01-1024x683-2", "White seamless K-style gutters and downspout")}<div><p class="label light">02 &middot; K-style</p><h3>5&Prime; or 6&Prime;</h3><p>5-inch is standard on most homes. 6-inch handles bigger, steeper roofs. Here&rsquo;s how to choose.</p></div></a>
<a class="swatch reveal" href="@/services/roof-heat-cable-installation/">{img("heat-cable", "Heat cable installed in a zig-zag along a shingle roof edge")}<div><p class="label light">03 &middot; Winter</p><h3>Heat cable</h3><p>Zig-zag cable along the eaves, so snowmelt has somewhere to go instead of freezing into an ice dam.</p></div></a>
</div></div></section>

<section class="sec work"><div class="wrap"><div class="head row reveal"><div><p class="label light">Our work</p><h2>From copper downspouts to whole exteriors</h2></div><a class="more light" href="@/our-work/">See more work {ARROW}</a></div>
<div class="bento">{bento}</div></div></section>

<section class="winter"><div class="winter-bg">{img("heat-cable1", "Heat cable installed in rows across a shingle roof")}</div><div class="wrap"><div class="winter-card reveal">
<p class="label light">Utah winters</p><h2>Snow melts on a warm roof and freezes again at the cold edge.</h2>
<p>That ridge of ice at the eaves is an ice dam, and the water backed up behind it finds its way under shingles. Heat cable and ice-melting systems keep a channel open so it can drain.</p>
<div class="btn-row"><a class="btn" href="@/services/roof-heat-cable-installation/">Heat cable {ARROW}</a><a class="btn ghost light" href="@/services/ice-melting-systems/">Ice-melting systems</a></div></div></div></section>

<section class="sec story"><div class="wrap story-grid">
<div class="reveal"><p class="label">Since 1990</p><h2>A family business, run by someone who started on the ladder</h2>
<p class="lede">Nate Nuttall still goes out to job sites and meets customers, and the company still employs family.</p>
<a class="more" href="@/about-mm-gutters-exteriors/">About M&amp;M {ARROW}</a></div>
<ol class="timeline reveal"><li><b>1990</b><span>M&amp;M gets its start.</span></li><li><b>2005</b><span>Nate Nuttall joins as an installer, then moves into sales and management.</span></li>
<li><b>2010</b><span>Nate buys the business.</span></li><li><b>Today</b><span>Gutters, heat cable, roofing, soffit, fascia, windows, siding, stucco and stone.</span></li></ol>
</div>
<div class="wrap quotes-row"><figure class="bigquote reveal"><blockquote><p>&ldquo;{STAFF[1][0]}&rdquo;</p></blockquote><figcaption>{STAFF[1][1]}</figcaption></figure>
<figure class="smallquote reveal"><blockquote><p>&ldquo;{STAFF[0][0]}&rdquo;</p></blockquote><figcaption>{STAFF[0][1]}</figcaption></figure></div>
</section>

<section class="sec paper"><div class="wrap split">
<div class="reveal"><p class="label">How it works</p><h2>Three steps to a better-protected home</h2>
<ol class="steps"><li><b>Call</b><span>Reach out for your free consultation. We&rsquo;ll discuss your vision and assess your needs.</span></li>
<li><b>Design</b><span>Our team creates a custom plan for your home. With HOVER, you can see a 3D model of the result before you pay for it.</span></li>
<li><b>Install</b><span>Our crew does the work, and leaves the site clean.</span></li></ol>
<a class="more" href="@/hover/">About HOVER 3D models {ARROW}</a></div>
<div class="reveal">{quote_form()}</div></div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="label">Questions</p><h2>Gutter questions we hear most</h2><p class="lede">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div>
<div class="reveal">{faq_html(faqs)}</div></div></section>''' + cta()
    return {"path": "", "canonical": U, "title": "Gutter Installation Salt Lake City | M&M Gutters & Exteriors",
            "meta": "Seamless gutter installation in Salt Lake City since 1990: copper, aluminum and steel gutters, leaf guards, heat cable, roofing and siding. Free quotes.",
            "body": body, "schema": [crumbs_ld(U, [HOME]), faq_ld(faqs)]}


def gallery_page(r, known, title, h1, lede, names):
    trail = [HOME, (h1, r["path"])]
    intro = clean(r["content"], known) if r["words"] > 150 else ""
    gal = "".join(f'<figure class="reveal"><button type="button" class="zoom" aria-label="Enlarge photo">{img(n, "M&M Gutters & Exteriors project in the Salt Lake Valley")}</button></figure>' for n in names if n in IMG)
    body = phero(trail, h1, lede, "Our work", "copper-gutter-4", "Copper gutters and downspouts installed by M&M", buttons=False) + (f'<section class="sec"><div class="wrap"><div class="prose reveal">{intro}</div></div></section>' if intro else "") + \
        f'<section class="sec dark"><div class="wrap"><div class="masonry">{gal}</div></div></section><dialog class="lightbox"><button type="button" class="lb-close" aria-label="Close">&times;</button></dialog>' + cta()
    return {"path": r["path"], "canonical": U + r["path"], "title": title, "meta": r["meta"] or "Photos of M&M Gutters & Exteriors projects in Salt Lake City and across the valley: gutters, heat cable, soffit and fascia, roofing and siding.",
            "body": body, "full_biz": False, "schema": [crumbs_ld(U + r["path"], trail)], "modified": r.get("modified")}


def simple_page(r, known, label, h1=None, title=None, meta=None, form=False, image=None):
    trail = [HOME, (h1 or strip_title(r["title"]) or r["h1"], r["path"])]
    content = clean(r["content"], known)
    right = f'<div class="reveal sticky">{quote_form()}</div>' if form else side_services()
    body = phero(trail, h1 or r["h1"] or strip_title(r["title"]), "", label, image, "M&M Gutters & Exteriors project", buttons=not form) + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{content}</div>{right}</div></section>''' + ("" if form else cta())
    return {"path": r["path"], "canonical": U + r["path"], "title": title or r["title"], "meta": meta or r["meta"] or first_para(r["content"]),
            "body": body, "full_biz": form, "schema": [crumbs_ld(U + r["path"], trail)], "modified": r.get("modified")}


def notfound():
    body = f'''<section class="phero"><div class="ph-bg plan" aria-hidden="true"></div><div class="wrap"><div class="ph-text"><p class="label light">404</p><h1>This page went down the drain.</h1>
<p class="lede">Try the <a href="@/">home page</a>, <a href="@/services/rain-gutters-installation/">rain gutters</a> or the <a href="@/blog/">blog</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></div></section>'''
    return {"path": "404.html", "canonical": None, "title": "Page Not Found | M&M Gutters & Exteriors", "meta": "This page isn't on the M&M Gutters & Exteriors site. Try the home page, rain gutters or the blog, or call 801.280.2222.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def make_pages(rows):
    R = {r["path"]: r for r in rows}
    known = set(R) | {BLOG[1]}
    posts = [r for r in rows if r["path"].startswith("blog/") and r["path"] != "blog/"]
    pages = [home(known)]
    for p, r in R.items():
        if p == "": continue
        if p.startswith("blog/") and p != "blog/":
            pages.append(post_page(r, known, posts))
        elif p.startswith("services/"):
            pages.append(service_page(r, known))
        elif p in ("blog/", "blog-all/"):
            h1 = "Blog" if p == "blog/" else "All Blog Posts"
            pages.append({"path": p, "canonical": U + p, "title": ("Gutter, Roofing & Siding Blog | M&M Gutters & Exteriors" if p == "blog/" else "All Blog Posts | M&M Gutters & Exteriors"),
                          "meta": "Guides from M&M Gutters & Exteriors in Salt Lake City: rain gutters, leaf guards, heat cable, roofing felt, siding, stucco and window replacement.",
                          "body": blog_index(p, posts, h1), "full_biz": False, "schema": [crumbs_ld(U + p, [HOME, (h1, p)]), {"@type": "Blog", "@id": U + p + "#blog", "url": U + p, "name": "M&M Gutters & Exteriors blog"}]})
        elif p in ("our-work/", "portfolio/", "recent-projects/"):
            o = OVERRIDES.get(p, {})
            names = GALLERY if p == "our-work/" else sorted(IMG)
            names = [n for n in names if n != "mm-gutters-exteriors-logo"]
            pages.append(gallery_page(r, known, o.get("title", r["title"]), o.get("h1", r["h1"] or "Our Work"), o.get("lede", ""), names))
        elif p in ("contact-us/", "request-a-quote/"):
            o = OVERRIDES.get(p, {})
            pages.append(simple_page(r, known, "Contact", o.get("h1"), o.get("title"), o.get("meta"), form=True, image="utah-rainer-gutters-03-2"))
        else:
            o = OVERRIDES.get(p, {})
            pages.append(simple_page(r, known, o.get("label", "M&amp;M Gutters &amp; Exteriors"), o.get("h1"), o.get("title"), o.get("meta"),
                                     image={"about-mm-gutters-exteriors/": "20140530-144851", "hover/": "mg-6540-55"}.get(p)))
    pages += [p_blog.page(), notfound()]
    return pages
