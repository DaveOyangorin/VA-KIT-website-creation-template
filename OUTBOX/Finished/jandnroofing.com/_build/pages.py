import re, html, os, json
from build import (U, BIZ_ID, S, ARROW, PHONE, CHECK, IMG, IMGMAP, CONTACT, INSPECT, img, crumbs_ld, faq_ld,
                   faq_html, quotes_html, cta, side, phero, quote_form)
import p_home, p_blog
from overrides import OVERRIDES, META_ONLY

HERE = os.path.dirname(os.path.abspath(__file__))
# Post classification (see notes): 41 posts J & N wrote are rebuilt; 411 posts copied from goodshomedesign.com are left out.
CLASSES = json.load(open(os.path.join(HERE, "post_classes.json"), encoding="utf-8"))
OWN_POSTS, COPIED = set(CLASSES["own"]), set(CLASSES["copied"])
NOINDEX = {"thank-you/", "search-archives-template/"}
# thumbnails of copied posts that the old recent-posts widgets put on the services and home pages
COPIED_IMG = {"custom-built-wood-barns", "tiny-house-in-the-wilderness", "waterlovt-by-belvari-marine-1"}


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def kind(p):
    if p == "": return "home"
    if p == "blog/" or p.startswith("category/") or p == "search-archives-template/": return "blog-index"
    if p in OWN_POSTS: return "post"
    if p == "dt_testimonials/" or p == "testimonials/": return "testimonials"
    if p.startswith("dt_testimonials/"): return "testimonial"
    if p in ("about-us/", "j-n-roofing-difference/", "service-areas/", "warranty-support/", "references/", "special-offers/", "gallery/"): return "about"
    if p in ("contact-us/", "free-estimate/"): return "quote"
    if p == "privacy-policy/": return "legal"
    if p == "thank-you/": return "promo"
    if p in ("frequently-asked-questions/", "glossary-of-roofing-terms/"): return "guide"
    return "service"


def clean_name(t):
    t = plain(t.split(" – J &")[0].split(" &#8211; J")[0])
    t = re.sub(r"\s*[–-]\s*\d+\s+[^,]+?(?=\s+(?:Sandy|Salt Lake|Park City))", " –", t)   # drop a street number/name from a reviewer's location
    return re.sub(r"\s+", " ", t).strip(" –")


def localize_images(body):
    def rep(m):
        src, alt = html.unescape(m.group(1)), html.unescape(m.group(2))
        name = IMGMAP.get(src)
        if not name or name in COPIED_IMG: return ""
        return f'<figure>{img(name, alt or "Roofing work by J & N Roofing Maintenance")}</figure>'
    body = re.sub(r'^\s*(?:<a href="@/\d{4}/\d{2}/\d{2}/">[^<]*</a>)?\s*(?:<a href="@/category/[^"]+">[^<]*</a>\s*)*', "", body)  # post date + category line
    body = re.sub(r'<a href="[^"]+\.(?:jpe?g|png|webp)">\s*(<img [^>]+>)\s*</a>', r"\1", body)
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"((?:<figure>.*?</figure>\s*){3,})", lambda m: '<div class="gallery">' + m.group(1) + "</div>", body, flags=re.S)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox">\1</div>', body, flags=re.S)
    body = body.replace('href="https://jandnroofing.com/', 'href="@/')
    body = re.sub(r'href="(?:mailto:)?([\w.+-]+@[\w-]+\.[\w.]+)"', r'href="mailto:\1"', body)
    # old internal links that redirect (or 404) on the live site
    for old, new in FIXLINKS.items():
        body = body.replace(f'href="@/{old}"', f'href="@/{new}"')
    body = re.sub(r'<a href="@/financing/">(.*?)</a>', lambda m: m.group(1), body, flags=re.S)  # 404 on the live site
    # links into the copied posts point at pages that are not part of the new site
    body = re.sub(r'<a href="@/([^"#]+)">(.*?)</a>', lambda m: m.group(2) if m.group(1) in COPIED else m.group(0), body, flags=re.S)
    return body


FIXLINKS = {"services-2/residential-roofing/": "services/residential-roofing/", "services-2/low-slope-roofing/": "services/low-slope-roofing/",
            "services-2/": "services/", "roofing-repairs/": "services/roofing-repairs/", "roof-ventilation/": "services/roof-ventilation/",
            "new-construction/": "services/new-construction/", "gutter-cleaning/": "services/gutter-cleaning/"}


def references_body(body):
    """Keep who the references are; hold back private homeowners' phone numbers until the client confirms they may be public."""
    b = re.sub(r"(Contact:\s*[^<–-]*?)\s*[–-]\s*\(?\d{3}\)?[-. ]?\d{3}[-. ]\d{4}", r"\1", body)
    b = re.sub(r"Contact:\s*\(?\d{3}\)?[-. ]?\d{3}[-. ]\d{4}\s*(or\s*)?", "Contact: ", b)
    b = re.sub(r"\(?\b\d{3}\)?[-. ]\d{3}[-. ]\d{4}\b", "", b)
    return '<p><em>Phone numbers for individual references are available on request.</em></p>' + b


def auto_meta(r, h1):
    txt = re.sub(r"\s+", " ", plain(" ".join(re.findall(r"<p>(.*?)</p>", r["body"])[:3])))
    if len(txt) < 60: txt = f"{h1}. J & N Roofing Maintenance: residential roofing and maintenance in West Valley City and the Salt Lake City metro. Free estimates."
    if len(txt) > 158: txt = txt[:155].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return txt


RELATED = {
    "service": [("Roofing repairs", "services/roofing-repairs/"), ("Roof replacement", "services/roof-replacement/"), ("Roof inspections &amp; maintenance", "services/roof-inspections-maintenance/"), ("Warranty support", "warranty-support/"), ("Free estimate", INSPECT)],
    "post": [("Roofing repairs", "services/roofing-repairs/"), ("Roof replacement", "services/roof-replacement/"), ("Roofing glossary", "glossary-of-roofing-terms/"), ("All articles", "blog/")],
    "about": [("About us", "about-us/"), ("The J &amp; N difference", "j-n-roofing-difference/"), ("Testimonials", "testimonials/"), ("Warranty support", "warranty-support/"), ("Service areas", "service-areas/")],
    "guide": [("Roofing FAQ", "frequently-asked-questions/"), ("Glossary of roofing terms", "glossary-of-roofing-terms/"), ("Blog", "blog/"), ("Free estimate", INSPECT)],
}
LABEL = {"service": "Roofing services", "post": "J &amp; N Roofing blog", "about": "About J &amp; N", "legal": "Legal", "quote": "Contact",
         "guide": "Roof maintenance handbook", "testimonial": "Testimonial", "testimonials": "Testimonials", "promo": "J &amp; N Roofing"}


def trail_for(p, h1, k):
    t = [("Home", "")]
    if k == "post": t.append(("Blog", "blog/"))
    elif k == "service" and p != "services/": t.append(("Services", "services/"))
    elif k == "testimonial": t.append(("Testimonials", "testimonials/"))
    t.append((html.escape(h1), p))
    return t


def hero_for(p, k, r, i, pool):
    own = [IMGMAP[u] for u in r["images"] if u in IMGMAP and IMG[IMGMAP[u]][0] >= 900 and IMG[IMGMAP[u]][0] > IMG[IMGMAP[u]][1] and IMGMAP[u] not in p_home.NOHERO]
    if own: return own[0]
    return pool[i % len(pool)]


def make_pages(ex):
    pages, rec = [], {}
    for r in ex:
        p = path_of(r)
        if p in COPIED: continue
        rec[p] = r
    pool = p_home.HERO_POOL()
    tests = []
    for p, r in sorted(rec.items()):
        if p.startswith("dt_testimonials/") and p != "dt_testimonials/":
            body = r["body"]; m = re.match(r"\s*<h\d>(.*?)</h\d>", body)
            q = plain(body[m.end():] if m else body)
            tests.append([re.sub(r"\s+", " ", q), clean_name(r["title"])])
    posts = sorted([(p, r) for p, r in rec.items() if kind(p) == "post"], key=lambda x: x[1].get("published") or "", reverse=True)

    for i, (p, r) in enumerate(sorted(rec.items())):
        k = kind(p)
        h1 = plain(r["h1"] or r["title"].split(" – ")[0].split(" &#8211; ")[0])
        url = U + p
        page = {"path": p, "title": r["title"], "meta": r["meta"] or auto_meta(r, h1), "canonical": r.get("canonical") or url,
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
        body = localize_images(r["body"])
        if p == "references/": body = references_body(body)
        body = lead + body
        trail = trail_for(p, h1, k)
        main = body
        extra = ""
        if k == "post" and r.get("published"):
            d = r["published"][:10]
            extra = f'<div class="meta-line"><span>By J &amp; N Roofing Maintenance</span><span>Published <time datetime="{d}">{d}</time></span></div>'
        if k == "blog-index":
            cat = "" if p in ("blog/", "search-archives-template/") else re.sub(r"^category/|/$", "", p).replace("-", " ").title()
            h1 = "Roof Maintenance Handbook" if not cat else f"{cat} Articles"
            trail = [("Home", ""), ("Blog", "blog/")] + ([(cat, p)] if cat else [])
            listing = [(p_blog.PATH, {"h1": p_blog.TITLE, "images": [], "title": "", "published": "2026-10-17"})] + posts
            cards = "".join(f'<a class="postcard reveal" href="@/{pp}">{img(hero_for(pp, "post", pr, j, pool), plain(pr["h1"] or pp))}<div class="in"><small>{(pr.get("published") or "")[:10]}</small><b>{html.escape(plain(pr["h1"] or pr["title"].split(" – ")[0]))}</b></div></a>'
                            for j, (pp, pr) in enumerate(listing))
            if p not in META_ONLY:
                page["title"] = f"{cat} Articles | J & N Roofing Blog" if cat else "Roof Maintenance Handbook | J & N Roofing Blog"
                page["meta"] = "Roof maintenance guides and articles from J & N Roofing Maintenance in West Valley City, UT: repairs, replacement, re-roofing, shingles and flat roofs."
            if p in NOINDEX: page["robots"] = "noindex, follow"; page["sitemap"] = False
            page["body"] = phero(trail, h1, "Plain-spoken roofing advice for homeowners in West Valley City and the Salt Lake metro.", hero, "Roof", "Blog") + \
                f'<section class="sec"><div class="wrap"><div class="postgrid">{cards}</div></div></section>' + cta()
            page["schema"] = [crumbs_ld(url, trail), {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": plain(h1)}]
            page["canonical"] = url; page["full_biz"] = False; pages.append(page); continue
        if k == "testimonials":
            main = '<p>What J &amp; N Roofing customers in Salt Lake City, Sandy and Park City have said about working with Norm and the crew.</p>'
            h1 = "Testimonials"; trail = trail_for(p, h1, k)
            if p == "dt_testimonials/": page["title"] = "Customer Testimonials | J & N Roofing Maintenance"
        if k == "testimonial":
            q = next((t for t in tests if t[1] == clean_name(r["title"])), None)
            h1 = clean_name(r["title"]); trail = trail_for(p, h1, k)
            main = (f'<blockquote class="pull"><p>{html.escape(q[0])}</p><footer>{html.escape(q[1])}</footer></blockquote>' if q else body) + '<p><a href="@/testimonials/">Read all testimonials</a></p>'
            page["title"] = f"{h1} | J & N Roofing Testimonial"
            page["meta"] = auto_meta({"body": f"<p>{html.escape(q[0]) if q else ''}</p>"}, h1)
        if p == "gallery/":
            h1 = "Roofing Gallery"; trail = trail_for(p, h1, k)
            main = '<p>Roofs J &amp; N Roofing Maintenance has completed across the Salt Lake City metro area.</p>' + body
        if k == "promo" or p in NOINDEX:
            page["robots"] = "noindex, follow"; page["sitemap"] = False
        rel = RELATED.get(k) or RELATED["service"]
        if k == "post":
            rel = RELATED["post"] + [(plain(pr["h1"] or pr["title"].split(" – ")[0])[:60], pp) for pp, pr in posts if pp != p][:3]
        layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        if k == "quote":
            h1 = "Contact J &amp; N Roofing" if p == "contact-us/" else "Request a Free Estimate"; trail = trail_for(p, h1, k)
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<p>Fill out the form with your contact information and the best phone number to reach you, plus a brief description of what you&rsquo;re looking for. One of our certified roofing contractors will call you back with a free estimate.</p>
<div class="pillars" style="grid-template-columns:1fr;margin-top:18px">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Phone</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a><br>Business hours: 7am to 5pm, Monday&ndash;Friday</p></div></div>
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>24-hour support</h3><p><a href="tel:{S["tel24"]}">{S["phone24"]}</a></p></div></div>
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Service area</h3><p>All of the Salt Lake City metro area, from {S["city"]}, {S["st"]}</p></div></div>
</div><p style="margin-top:16px"><a href="mailto:{S["email"]}">{S["email"]}</a></p></div>
<div>{quote_form()}</div></div></section>'''
        faqs = r["faqs"]
        extra_secs = ""
        if faqs:
            extra_secs += f'<section class="sec tight"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Frequently asked questions</h2></div>{faq_html(faqs)}</div></section>'
        if (k in ("service",) or k == "testimonials") and tests:
            j = i % len(tests)
            extra_secs += quotes_html(tests if k == "testimonials" else tests[j:] + tests[:j], "What customers say" if k == "testimonials" else "What customers say about Norm and the crew", limit=99 if k == "testimonials" else 4)
        page["body"] = phero(trail, h1, "", hero, plain(h1), LABEL.get(k, "J &amp; N Roofing"), extra) + layout + extra_secs + cta()
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        if k == "service":
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": page["meta"], "url": url, "provider": {"@id": BIZ_ID},
                        "areaServed": [{"@type": "City", "name": "West Valley City"}, {"@type": "City", "name": "Salt Lake City"}]})
        elif k == "post":
            sch.append({"@type": "BlogPosting", "@id": url + "#article", "headline": plain(h1)[:110], "description": page["meta"], "url": url,
                        "mainEntityOfPage": url, "image": U + "assets/img/" + hero + ".webp",
                        "datePublished": r.get("published") or None, "dateModified": r.get("modified") or None,
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"})
            page["ogtype"] = "article"
        elif k in ("about", "testimonials"):
            sch.append({"@type": "AboutPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "quote":
            sch.append({"@type": "ContactPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "guide" and p == "glossary-of-roofing-terms/":
            sch.append({"@type": "DefinedTermSet", "@id": url + "#glossary", "name": "Glossary of Roofing Terms", "url": url})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "quote", "service", "testimonials")
        pages.append(page)

    pages.append(p_blog.new_post(pool[1] if len(pool) > 1 else pool[0]))
    pages.append({"path": "404.html", "title": "Page Not Found | J & N Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn&rsquo;t here", "Try the home page, or call for a free estimate.",
                                pool[0], "Roof", "Error 404")})
    return pages, {}
