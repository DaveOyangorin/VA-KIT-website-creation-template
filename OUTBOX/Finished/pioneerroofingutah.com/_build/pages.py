import re, html, os
from build import (U, BIZ_ID, SLC_ID, S, ARROW, PHONE, CHECK, IMG, IMGMAP, INSPECT, CONTACT, ESTIMATE, img, crumbs_ld, faq_ld,
                   faq_html, quotes_html, cta, side, phero, quote_form)
import p_home, p_blog
from overrides import OVERRIDES

CITY = {"eagle-mountain/", "evanston-wyoming/", "south-jordan/", "taylorsville/", "tooele/", "riverton/", "salt-lake-city/",
        "sandy/", "herriman/"}
NOINDEX = {"thank-you/", "home-2/"}   # form thank-you page and an old copy of the home page: kept, but out of the index


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def kind(p):
    if p == "": return "home"
    if p == "blog/": return "blog-index"
    if p.startswith("blog-"): return "post"
    if p == "areas-we-serve/": return "area-index"
    if p.startswith("areas-") or p in CITY: return "city"
    if p in ("about-2/", "certification-and-warranty/", "project-gallery/"): return "about"
    if p in ("contact-us/", "book-inspection/"): return "quote"
    if p == "privacy/": return "legal"
    if p in NOINDEX: return "promo"
    return "service"


# Stock photos of models (not Pioneer's crew), found on the contact-sheet review: never shown on the new site.
STOCK = {"pexels-brian-haddock-120535352-9876243", "pexels-geladelrosario-3676018", "pexels-joshsorenson-13338736", "pexels-pixabay-48895",
         "pexels-quang-vuong-724225078-30255772", "pexels-redheron-28644107", "pexels-todd-trapani-488382-3546778"}  # Pexels stock scenery
NOHERO = STOCK | {"1-1", "1", "2", "3", "4", "utah", "pioneer-roofing-john-and-linda-stout-4-5-ratio-photo"}  # badges, map, people
# Review cards on the current pages: "Rated 5 out of 5 <h6>Name</h6><p>Quote</p>"
REVIEW = re.compile(r'(?:<img data-src="[^"]+" alt="[^"]*">\s*)?Rated 5 out of 5\s*<h6>(.*?)</h6>\s*<p>(.*?)</p>', re.S)


def pull_reviews(body):
    found = [(plain(q), plain(n)) for n, q in REVIEW.findall(body)]
    body = REVIEW.sub("", body)
    body = re.sub(r"<h2>\s*Our Reviews\s*</h2>\s*<p>\s*See how others have viewed their experience with us\s*</p>", "", body, flags=re.I)
    body = re.sub(r"<h2>\s*What Our Customers Say\.*\s*</h2>", "", body, flags=re.I)
    return body, found


def localize_images(body):
    def rep(m):
        src, alt = html.unescape(m.group(1)), html.unescape(m.group(2))
        name = IMGMAP.get(src)
        if not name or name in STOCK: return ""
        return f'<figure>{img(name, alt or "Roof by Pioneer Roofing in Utah")}</figure>'
    def gal(m):
        figs = []
        for src, alt in re.findall(r'<img data-src="([^"]+)" alt="([^"]*)">', m.group(1)):
            name = IMGMAP.get(html.unescape(src))
            if name and name not in STOCK: figs.append(f'<figure>{img(name, html.unescape(alt) or "Roof by Pioneer Roofing in Utah")}</figure>')
        return '<div class="gallery">' + "".join(figs) + "</div>" if figs else ""
    body = re.sub(r'<div class="gal">(.*?)</div>', gal, body, flags=re.S)
    body = re.sub(r'<a href="[^"]+\.(?:jpe?g|png|webp)">\s*(<img [^>]+>)\s*</a>', r"\1", body)
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"((?:<figure>.*?</figure>\s*){3,})", lambda m: '<div class="gallery">' + m.group(1) + "</div>", body, flags=re.S)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox price-table">\1</div>', body, flags=re.S)
    body = body.replace('href="https://pioneerroofingutah.com/', 'href="@/')
    body = re.sub(r'<a href="@/careers/">(.*?)</a>', r'\1', body, flags=re.S)  # /careers/ is a 404 on the live site
    body = re.sub(r'(<img [^>]*tpo-roof-careers[^>]*>)?\s*<h2>Careers</h2>', '', body)
    body = re.sub(r'href="(?:mailto:)?([\w.+-]+@[\w-]+\.[\w.]+)"', r'href="mailto:\1"', body)
    return body


def auto_meta(r, h1):
    txt = re.sub(r"\s+", " ", plain(" ".join(re.findall(r"<p>(.*?)</p>", r["body"])[:3])))
    if len(txt) < 60: txt = f"{h1}. Pioneer Roofing: family run roofing company in Salt Lake City since 1980. Repairs, replacements and inspections."
    if len(txt) > 158: txt = txt[:155].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return txt


RELATED = {
    "service": [("Roof repairs", "roofing-repairs/"), ("Roof inspections", "roof-inspections/"), ("Pricing", "pricing/"), ("New roof estimator", ESTIMATE), ("Contact", CONTACT)],
    "city": [("Roofing in Salt Lake City", "salt-lake-city/"), ("Roof repairs", "roofing-repairs/"), ("Residential roofing", "residential-roofing/"), ("All areas we serve", "areas-we-serve/")],
    "post": [("Roof repairs", "roofing-repairs/"), ("Roof inspections", "roof-inspections/"), ("Pricing", "pricing/"), ("All articles", "blog/")],
    "about": [("About Pioneer", "about-2/"), ("Certification &amp; warranty", "certification-and-warranty/"), ("Project gallery", "project-gallery/"), ("Areas we serve", "areas-we-serve/")],
}
LABEL = {"service": "Roofing services", "city": "Areas we serve", "post": "Pioneer Roofing blog", "about": "About Pioneer Roofing", "legal": "Legal",
         "quote": "Contact", "promo": "Pioneer Roofing", "area-index": "Areas we serve"}


def city_name(p, r):
    t = plain(r["h1"] or r["title"].split(" - ")[0])
    return t


def trail_for(p, h1, k):
    t = [("Home", "")]
    if k == "post": t.append(("Blog", "blog/"))
    elif k == "city": t.append(("Areas we serve", "areas-we-serve/"))
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
    for p in sorted(rec):
        rec[p]["body"], found = pull_reviews(rec[p]["body"])
        for q, a in found:
            if q not in seen and len(q) > 40: seen.add(q); tests.append([q, a])
    posts = sorted([(p, r) for p, r in rec.items() if kind(p) == "post"], key=lambda x: x[1].get("published") or x[1].get("modified") or "", reverse=True)

    for i, (p, r) in enumerate(sorted(rec.items())):
        k = kind(p)
        h1 = plain(r["h1"] or r["title"].split(" - ")[0])
        url = U + p
        meta = r["meta"] or auto_meta(r, h1)
        page = {"path": p, "title": r["title"], "meta": meta, "canonical": r.get("canonical") or url,
                "modified": (r.get("modified") or "")[:10] or None, "auto_meta": not r["meta"]}
        lead = ""
        if p in OVERRIDES:
            page["title"], h1, page["meta"], lead = OVERRIDES[p]; page["auto_meta"] = False
            lead = f'<div class="answer">{lead}</div>'
        if k == "home":
            page.update(p_home.build(r, rec, posts, tests)); pages.append(page); continue
        hero = hero_for(p, k, r, i, pool)
        body = lead + localize_images(r["body"])
        trail = trail_for(p, h1, k)
        main = body
        extra = ""
        if k == "post":
            d = (r.get("published") or r.get("modified") or "")[:10]
            if d: extra = f'<div class="meta-line"><span>By Pioneer Roofing</span><span>Updated <time datetime="{d}">{d}</time></span></div>'
        if k == "blog-index":
            cards = "".join(f'<a class="postcard reveal" href="@/{pp}">{img(hero_for(pp, "post", pr, j, pool), plain(pr["h1"] or pp))}<div class="in"><small>Pioneer Roofing blog</small><b>{html.escape(plain(pr["h1"] or pr["title"].split(" - ")[0]))}</b></div></a>'
                            for j, (pp, pr) in enumerate([(p_blog.PATH, {"h1": "What Is the 25% Rule for Roofing?", "images": [], "title": ""})] + posts))
            page["body"] = phero(trail, "Pioneer Roofing Blog", "Straight answers about roofs in Utah, from a family roofing company working since 1980.", hero, "Roof", "Blog") + \
                f'<section class="sec"><div class="wrap"><div class="postgrid">{cards}</div></div></section>' + cta()
            page["schema"] = [crumbs_ld(url, trail), {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": "Pioneer Roofing Blog"}]
            page["full_biz"] = False; pages.append(page); continue
        if k == "area-index":
            cities = sorted([(cp, cr) for cp, cr in rec.items() if kind(cp) == "city"], key=lambda x: city_name(*x))
            chips = "".join(f'<a href="@/{cp}">{html.escape(city_name(cp, cr))}</a>' for cp, cr in cities)
            main = body + f'<h2>Cities we serve</h2><div class="chips">{chips}</div>'
        if k == "city":
            sibs = sorted(cp for cp in rec if kind(cp) == "city" and cp != p)
            j = i % max(1, len(sibs)); near = (sibs[j:] + sibs[:j])[:6]
            main = body + '<h2>More areas we serve</h2><div class="chips">' + "".join(f'<a href="@/{cp}">{html.escape(city_name(cp, rec[cp]))}</a>' for cp in near) + "</div>"
        if p == "new-roof-estimator/":
            main = ('<p>Answer a few questions about your home and get an instant estimate for a new roof, powered by Roofr. For an exact price, <a href="@/book-inspection/">book an inspection</a>.</p>'
                    '<div class="embed-live"><iframe src="https://app.roofr.com/instant-estimator/1f8d907e-dd77-4116-8f18-b40e42bf3f6a/PioneerRoofingCoLLC" title="Pioneer Roofing instant roof estimator" loading="lazy"></iframe></div>')
            h1 = "New Roof Estimator"; trail = trail_for(p, h1, k)
        if p == "book-inspection/":
            body = ('<p>Pick a time for your roof inspection below. Prefer to talk first? Call John at <a href="tel:' + S["tel"] + '">' + S["phone"] + '</a>.</p>'
                    '<div class="embed-live"><div class="tidycal-embed" data-path="mason2/roof-inspection"></div><script src="https://asset-tidycal.b-cdn.net/js/embed.js" async></script></div>')
            h1 = "Book a Roof Inspection"; trail = trail_for(p, h1, k)
        if k == "promo":
            page["robots"] = "noindex, follow"; page["sitemap"] = False
        rel = RELATED.get(k) or RELATED["service"]
        if k == "post":
            rel = RELATED["post"] + [(plain(pr["h1"] or pp)[:60], pp) for pp, pr in posts if pp != p][:3]
        layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        if k == "quote":
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">{body}
<div class="pillars" style="grid-template-columns:1fr;margin-top:18px">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Call John</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br>Our service number goes directly to the owner.</p></div></div>
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Offices</h3><p>{S["slc"]["street"]}, {S["slc"]["city"]}, {S["slc"]["st"]} {S["slc"]["zip"]}<br>{S["price"]["street"]}, {S["price"]["city"]}, {S["price"]["st"]} {S["price"]["zip"]}</p></div></div>
</div><p style="margin-top:16px"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div>{quote_form()}</div></div></section>'''
        faqs = r["faqs"]
        extra_secs = ""
        if faqs:
            extra_secs += f'<section class="sec tight"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Frequently asked questions</h2></div>{faq_html(faqs)}</div></section>'
        if k in ("service", "about") and tests:
            extra_secs += quotes_html(tests[i % len(tests):] + tests[:i % len(tests)])
        page["body"] = phero(trail, html.escape(h1), "", hero, h1, LABEL.get(k, "Pioneer Roofing"), extra) + layout + extra_secs + cta()
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        prov = {"@id": SLC_ID}
        if k == "service":
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": page["meta"], "url": url, "provider": prov,
                        "areaServed": {"@type": "State", "name": "Utah"}})
        elif k == "city":
            cn = city_name(p, r)
            sch.append({"@type": "Service", "@id": url + "#service", "name": f"Roofing in {cn}", "description": page["meta"], "url": url, "provider": prov,
                        "areaServed": {"@type": "City", "name": cn}})
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
        elif k == "area-index":
            sch.append({"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": plain(h1)})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "quote", "city", "area-index")
        pages.append(page)

    pages.append(p_blog.new_post(pool[1] if len(pool) > 1 else pool[0]))
    pages.append({"path": "404.html", "title": "Page Not Found | Pioneer Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn&rsquo;t here", "Try the home page, or call John.",
                                pool[0], "Roof", "Error 404")})
    return pages, {}
