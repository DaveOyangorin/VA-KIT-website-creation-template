import re, html, os
from build import (U, BIZ_ID, S, ARROW, PHONE, CHECK, IMG, IMGMAP, CONTACT, img, crumbs_ld, faq_ld,
                   faq_html, quotes_html, cta, side, phero, quote_form)
import p_home, p_blog
from overrides import OVERRIDES, META_ONLY

POSTS = {"dont-wait-for-the-storm-5-signs-your-roof-needs-attention/", "popular-owens-corning-shingle-colors/", "who-to-call-for-roof-leak/",
         "who-to-call-for-leaking-roof/", "average-cost-to-install-metal-roof/", "most-common-roof-repair/",
         "what-time-of-year-is-cheapest-to-replace-a-roof/", "what-to-do-if-your-roof-is-damaged-in-a-storm/",
         "how-cool-roofs-help-you-save-up-to-30-on-summer-comfort-with-a-salt-lake-city-roofing-company-2/",
         "will-homeowners-insurance-pay-for-a-new-roof/"}
EMPTY_LEGAL = {"privacy-policy/", "terms-of-service/"}   # empty on the live site: kept, but out of the index until real text exists


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def kind(p):
    if p == "": return "home"
    if p == "blog/" or p.startswith("category/"): return "blog-index"
    if p in POSTS: return "post"
    if p in ("about-go-pro-roofing-west-valley-city/", "reviews/", "gallery/"): return "about"
    if p == "contact/": return "quote"
    if p in EMPTY_LEGAL: return "legal"
    if p == "sitemap/": return "sitemap"
    return "service"


# Contact-sheet review: only images that are clearly Go Pro Roofing's own (watermarked job photos, WhatsApp job photos, the crew in
# GPR hoodies, the annotated inspection photo) plus certification badges and the Owens Corning color chart are kept. Everything
# else on the current site looks like stock or AI imagery and is left off (list in real_photos.txt).
REAL = {l.strip() for l in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "real_photos.txt"), encoding="utf-8") if l.strip()}
STOCK = {n for n in IMG if n not in REAL and "logo" not in n}
NOHERO = STOCK | {"1", "2-2", "3", "3-2", "4", "4-2", "5", "5-2", "gaf-master-elite-1-1", "gaf-master-elite-1-1-2", "gaf-master-elite1", "gaf-master-elite1-2",
                  "img-20240122-wa0092", "img-20240122-wa0092-2", "owens-corning-shingle-color-comparison", "official-inspection-reports-for-selling-purchasing-homes"}
REVIEW = re.compile(r"Posted on Google\s+(.{2,40}?)\s+Trustindex verifies that the original source of the review is Google\.\s+(.*?)(?=Posted on Google|$)", re.S)


def pull_reviews(body):
    txt = plain(body)
    found = [(re.sub(r"\s+", " ", q).strip(), n.strip()) for n, q in REVIEW.findall(txt)]
    return [(q, n) for q, n in found if len(q) > 40]


def localize_images(body):
    def rep(m):
        src, alt = html.unescape(m.group(1)), html.unescape(m.group(2))
        name = IMGMAP.get(src)
        if not name or name in STOCK: return ""
        return f'<figure>{img(name, alt or "Roof by Go Pro Roofing in Utah")}</figure>'
    body = re.sub(r'^\s*<ul><li><a href="#">\s*Home\s*</a></li>.*?</ul>', "", body, flags=re.S)  # old breadcrumb
    body = re.sub(r"^\s*Home\s+(?:Services|About)\s+", "", body)
    body = re.sub(r'<a href="[^"]+\.(?:jpe?g|png|webp)">\s*(<img [^>]+>)\s*</a>', r"\1", body)
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"((?:<figure>.*?</figure>\s*){3,})", lambda m: '<div class="gallery">' + m.group(1) + "</div>", body, flags=re.S)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox">\1</div>', body, flags=re.S)
    body = body.replace('href="https://gprroofing.com/', 'href="@/')
    body = body.replace('href="@/residential-roof-installation-uta/"', 'href="@/residential-roof-installation-utah/"')  # typo link on the live site
    body = re.sub(r'<a href="@/why-weather-resilient-roofing-is-becoming-essential-for-todays-homeowners/">(.*?)</a>', lambda m: m.group(1), body, flags=re.S)  # 404 on the live site
    body = re.sub(r'href="(?:mailto:)?([\w.+-]+@[\w-]+\.[\w.]+)"', r'href="mailto:\1"', body)
    body = re.sub(r"<h2>\s*What Our (?:Utah )?(?:Roofing )?Customers (?:are|Are) Saying\s*</h2>.*?(?=<h[23]|$)", "", body, flags=re.S)
    body = re.sub(r"Wanna know what people think about us\? Check out our Review\.", "", body)
    return body


def gallery_body(body):
    """Gallery page: each photo is followed by 'UTAH UTAH <city>' on the live site; keep the city as a caption."""
    figs = []
    for src, alt, city in re.findall(r'<img data-src="([^"]+)" alt="([^"]*)">\s*(?:<h4>UTAH</h4>\s*)*<p>\s*([^<]+?)\s*</p>', body):
        name = IMGMAP.get(html.unescape(src))
        if not name or name in STOCK: continue
        c = city.strip().title()
        figs.append(f'<figure>{img(name, f"Roofing project by Go Pro Roofing in {c}, Utah")}<figcaption>{html.escape(c)}</figcaption></figure>')
    return '<p>Recent roofing projects by Go Pro Roofing across the Salt Lake Valley and Utah County.</p><div class="gallery captioned">' + "".join(figs) + "</div>"


def auto_meta(r, h1):
    txt = re.sub(r"\s+", " ", plain(" ".join(re.findall(r"<p>(.*?)</p>", r["body"])[:3])))
    if len(txt) < 60: txt = f"{h1}. Go Pro Roofing: licensed roofing contractor in West Valley City, Utah. Free estimates and free roof inspections."
    if len(txt) > 158: txt = txt[:155].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return txt


RELATED = {
    "service": [("Roof repair", "roof-repair-west-valley-city/"), ("Roof replacement", "roof-replacement-services-utah/"), ("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/"), ("Reviews", "reviews/"), ("Free quote", CONTACT)],
    "post": [("Roof repair", "roof-repair-west-valley-city/"), ("Roof replacement", "roof-replacement-services-utah/"), ("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/"), ("All articles", "blog/")],
    "about": [("About Go Pro Roofing", "about-go-pro-roofing-west-valley-city/"), ("Reviews", "reviews/"), ("Gallery", "gallery/"), ("Services", "services/")],
}
LABEL = {"service": "Roofing services", "post": "Go Pro Roofing blog", "about": "About Go Pro Roofing", "legal": "Legal", "quote": "Contact",
         "sitemap": "Sitemap", "blog-index": "Blog"}


def trail_for(p, h1, k):
    t = [("Home", "")]
    if k == "post": t.append(("Blog", "blog/"))
    elif k == "service" and p != "services/": t.append(("Services", "services/"))
    t.append((html.escape(h1), p))
    return t


def hero_for(p, k, r, i, pool):
    own = [IMGMAP[u] for u in r["images"] if u in IMGMAP and IMGMAP[u] not in NOHERO and IMG[IMGMAP[u]][0] >= 900 and IMG[IMGMAP[u]][0] > IMG[IMGMAP[u]][1]]
    if own: return own[0]
    return pool[i % len(pool)]


def make_pages(ex):
    pages, rec = [], {}
    for r in ex:
        rec[path_of(r)] = r
    pool = p_home.HERO_POOL()
    tests, seen = [], set()
    for q, a in pull_reviews(rec.get("reviews/", {"body": ""})["body"]):
        if q not in seen: seen.add(q); tests.append([q, a])
    posts = sorted([(p, r) for p, r in rec.items() if kind(p) == "post"], key=lambda x: x[1].get("published") or x[1].get("modified") or "", reverse=True)

    for i, (p, r) in enumerate(sorted(rec.items())):
        k = kind(p)
        h1 = plain(r["h1"] or r["title"].split(" – ")[0])
        url = U + p
        meta = r["meta"] or auto_meta(r, h1)
        page = {"path": p, "title": r["title"], "meta": meta, "canonical": r.get("canonical") or url,
                "modified": (r.get("modified") or "")[:10] or None, "auto_meta": not r["meta"]}
        lead = ""
        if p in OVERRIDES:
            page["title"], h1, page["meta"], lead = OVERRIDES[p]; page["auto_meta"] = False
            lead = f'<div class="answer">{lead}</div>'
        if p in META_ONLY:
            page["title"], page["meta"] = META_ONLY[p]; page["auto_meta"] = False
        if k == "home":
            page.update(p_home.build(r, rec, posts, tests)); pages.append(page); continue
        hero = hero_for(p, k, r, i, pool)
        body = lead + localize_images(r["body"])
        trail = trail_for(p, h1, k)
        main = body
        extra = ""
        if k == "post":
            d = (r.get("published") or r.get("modified") or "")[:10]
            if d: extra = f'<div class="meta-line"><span>By Go Pro Roofing</span><span>Updated <time datetime="{d}">{d}</time></span></div>'
            if not r["h1"]: h1 = plain(r["title"].split(" – ")[0]); trail = trail_for(p, h1, k)
        if k == "blog-index":
            cat = "" if p == "blog/" else re.sub(r"^category/|/$", "", p).replace("-", " ").title()
            h1 = "Roofing Resources &amp; News" if p == "blog/" else f"{cat} Articles"
            trail = [("Home", ""), ("Blog", "blog/")] + ([] if p == "blog/" else [(cat, p)])
            listing = [(p_blog.PATH, {"h1": "How Are Valleys Done on a Metal Roof?", "images": [], "title": ""})] + posts
            cards = "".join(f'<a class="postcard reveal" href="@/{pp}">{img(hero_for(pp, "post", pr, j, pool), plain(pr["h1"] or pp))}<div class="in"><small>Go Pro Roofing blog</small><b>{html.escape(plain(pr["h1"] or pr["title"].split(" – ")[0]))}</b></div></a>'
                            for j, (pp, pr) in enumerate(listing))
            if not r["meta"] and p not in META_ONLY:
                page["meta"] = "Roofing articles from Go Pro Roofing in West Valley City: roof repair, replacement, metal roofs, storm damage and insurance, written for Utah homeowners."
            if p != "blog/": page["title"] = f"{cat} Articles | Go Pro Roofing Blog"
            page["body"] = phero(trail, h1, "Straight answers for Utah homeowners from a West Valley City roofing contractor.", hero, "Roof", "Blog") + \
                f'<section class="sec"><div class="wrap"><div class="postgrid">{cards}</div></div></section>' + cta()
            page["schema"] = [crumbs_ld(url, trail), {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": plain(h1)}]
            page["canonical"] = url
            page["full_biz"] = False; pages.append(page); continue
        if p == "gallery/":
            main = gallery_body(r["body"]); h1 = "Recent Roofing Projects"; trail = trail_for(p, h1, k)
        if p == "reviews/":
            main = '<p>Real Google reviews from Go Pro Roofing customers, shown on our site through Trustindex.</p>'
            h1 = "Reviews &amp; Testimonials"; trail = trail_for(p, h1, k)
        if k == "sitemap":
            items = "".join(f'<li><a href="@/{pp}">{html.escape(plain(rr["h1"] or rr["title"].split(" – ")[0]))}</a></li>'
                            for pp, rr in sorted(rec.items()) if pp not in ("sitemap/",) and kind(pp) not in ("legal",) and pp)
            main = f'<ul class="sitemap-list"><li><a href="@/">Home</a></li><li><a href="@/{p_blog.PATH}">How Are Valleys Done on a Metal Roof?</a></li>{items}</ul>'
            h1 = "Sitemap"; trail = trail_for(p, h1, k)
            page["meta"] = "Every page on the Go Pro Roofing website: roofing services in West Valley City, blog articles, reviews, gallery and contact details."
        if k == "legal":
            page["robots"] = "noindex, follow"; page["sitemap"] = False
            main = f'<p>[[NEEDS: {html.escape(h1)} text from the client. The current page is empty.]]</p><p>Questions? Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or email <a href="mailto:{S["email"]}">{S["email"]}</a>.</p>'
        rel = RELATED.get(k) or RELATED["service"]
        if k == "post":
            rel = RELATED["post"] + [(plain(pr["h1"] or pr["title"].split(" – ")[0])[:60], pp) for pp, pr in posts if pp != p][:3]
        layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        if k == "quote":
            h1 = "Contact Go Pro Roofing"; trail = trail_for(p, h1, k)
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<p>Free estimates and free roof inspections across Salt Lake and Utah counties. Call, text or send a message, and José&rsquo;s team will get back to you.</p>
<div class="pillars" style="grid-template-columns:1fr;margin-top:18px">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Call or text</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br>24/7 emergency service</p></div></div>
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Office</h3><p>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</p></div></div>
</div><p style="margin-top:16px"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div>{quote_form()}</div></div></section>'''
        faqs = r["faqs"]
        extra_secs = ""
        if faqs:
            extra_secs += f'<section class="sec tight"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Frequently asked questions</h2></div>{faq_html(faqs)}</div></section>'
        if (k in ("service",) or p == "reviews/") and tests:
            j = i % len(tests)
            extra_secs += quotes_html(tests if p == "reviews/" else tests[j:] + tests[:j], "Google reviews" if p == "reviews/" else "What West Valley homeowners say", limit=99 if p == "reviews/" else 6)
        page["body"] = phero(trail, h1, "", hero, plain(h1), LABEL.get(k, "Go Pro Roofing"), extra) + layout + extra_secs + cta()
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        if k == "service":
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": page["meta"], "url": url, "provider": {"@id": BIZ_ID},
                        "areaServed": [{"@type": "City", "name": "West Valley City"}, {"@type": "AdministrativeArea", "name": "Salt Lake County"}]})
        elif k == "post":
            sch.append({"@type": "BlogPosting", "@id": url + "#article", "headline": plain(h1)[:110], "description": page["meta"], "url": url,
                        "mainEntityOfPage": url, "image": U + "assets/img/" + hero + ".webp",
                        "datePublished": r.get("published") or r.get("modified") or None, "dateModified": r.get("modified") or None,
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"})
            page["ogtype"] = "article"
        elif k == "about":
            sch.append({"@type": "AboutPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "quote":
            sch.append({"@type": "ContactPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "quote", "service")
        pages.append(page)

    pages.append(p_blog.new_post(pool[1] if len(pool) > 1 else pool[0]))
    pages.append({"path": "404.html", "title": "Page Not Found | Go Pro Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn&rsquo;t here", "Try the home page, or call for a free quote.",
                                pool[0], "Roof", "Error 404")})
    return pages, {}
