import re, html, json
from build import (U, BIZ_ID, S, ARROW, PHONE, IMG, IMGMAP, img, crumbs_ld, faq_ld, faq_html, quotes_html, cta, side,
                   phero, quote_form, crumbs_html)
import p_home, p_blog


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


CITY_IMGS = ["utah-roofing-service-areas", "hero-house", "roofing-project-utah-main", "residential-roofing-utah-home",
             "roofing-project-utah-blue-home", "roofing-project-utah-residential", "snowy-house-evergreens"]


def hero_for(path, i):
    p = path
    rules = [(r"storm|hail|insurance", "storm-damage-roofing"), (r"metal", "metal-roof-chimney-dusk"),
             (r"commercial|flat-roof|single-ply|built-up|low-slope|coating", "commercial-roofing-salt-lake-city"),
             (r"apartment|condo|essex", "multifamily-roof-replacement"),
             (r"repair|leak|maintenance|emergency|historic", "shingle-damage-closeup"),
             (r"gutter|soffit", "roofing-project-utah-residential"),
             (r"residential|asphalt|shingle|replacement", "roofing-project-utah-main"),
             (r"dumpster|financing|estimate|quote", "roof-condition-options-review"),
             (r"about|team|case-study|certified|mission|why-choose", "completed-roofing-project-final-inspection"),
             (r"glossary", "roofing-services-menu-img")]
    for rx, name in rules:
        if re.search(rx, p): return name
    return CITY_IMGS[i % len(CITY_IMGS)]


def kind(path):
    if path == "": return "home"
    if path == "blog/": return "blog-index"
    if path.startswith("blog/"): return "post"
    if path == "glossary/": return "glossary-index"
    if path.startswith("glossary/"): return "term"
    if path == "service-area/": return "area-index"
    if path.startswith("service-area/"): return "city"
    if path in ("request-free-quote/",): return "quote"
    if path.startswith(("about-us", "meet-the-team", "case-study", "essex-court")): return "about"
    if path.startswith("privacy-policy"): return "legal"
    return "service"


# iStock photos of models posing as workers: never shown as if they were the client's crew
STOCK_PEOPLE = {"clear-communication-photo", "cost-transparency-photo", "quality-workmanship-photo", "workmanship-warranty-photo"}


def localize_images(body):
    def rep(m):
        src, alt = html.unescape(m.group(1)), html.unescape(m.group(2))
        name = IMGMAP.get(src)
        if not name or name in STOCK_PEOPLE: return ""
        return f'<figure>{img(name, alt or "Roofing project in Utah")}</figure>'
    def gal(m):
        figs = []
        for src, alt in re.findall(r'<img data-src="([^"]+)" alt="([^"]*)">', m.group(1)):
            name = IMGMAP.get(html.unescape(src))
            if not name or name in STOCK_PEOPLE: continue
            cap = html.unescape(alt).title() if alt else ""
            if re.match(r"(?i)^(img|dsc|image|photo|pic|screenshot|untitled|wp)\b", cap) or re.fullmatch(r"[\d\s]*", cap):
                cap = ""  # camera file names are not captions
            figs.append(f'<figure>{img(name, (cap + " roofing project") if cap else "American Roofing project in Utah")}'
                        + (f'<figcaption>{html.escape(cap)}</figcaption>' if cap else "") + '</figure>')
        return '<div class="gallery">' + "".join(figs) + "</div>" if figs else ""
    body = re.sub(r'<div class="gal">(.*?)</div>', gal, body, flags=re.S)
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox">\1</div>', body, flags=re.S)
    return fix_links(body)


# Old internal links that 301 on the live site: point them straight at the final page.
FIXLINKS = {"apartment-condo/": "apartment-roof-repair/", "contact-us/": "request-free-quote/",
            "can-you-replace-roof-without-hoa-approval/": "blog/can-you-replace-roof-without-hoa-approval/",
            "how-to-identify-wind-damage-to-a-roof-american-roofing/": "blog/how-to-identify-wind-damage-to-a-roof-american-roofing/",
            "seasonal-roof-maintenance-checklist/": "blog/seasonal-roof-maintenance-checklist/",
            "residential-roof-repair/": "residential/", "products/pitched-roof-materials/": "",
            "blog/when-will-insurance-pay-for-a-new-roof/ar-infographic-insurance-cover-ver01-resized/": "blog/when-will-insurance-pay-for-a-new-roof/",
            "services/roof-repairs/ar-infographic-newroof-ver01/": "services/roof-repairs/"}


def fix_links(body):
    return re.sub(r'href="@/([^"#]*)', lambda m: 'href="@/' + FIXLINKS.get(m.group(1), m.group(1)), body)


RELATED = {
    "service": [("Roof Repairs", "services/roof-repairs/"), ("Roof Replacements", "services/roof-replacements/"),
                ("Storm Damage Repair", "services/storm-damage-repair/"), ("Insurance Claim Process", "services/roof-insurance-claim-process/"),
                ("Free Roofing Estimates", "free-roofing-estimates/")],
    "city": [("Residential Roofing", "residential/"), ("Commercial Roofing", "commercial/"), ("Roof Repairs", "services/roof-repairs/"),
             ("All Service Areas", "service-area/"), ("Request a Free Quote", "request-free-quote/")],
    "post": [("Roof Repairs", "services/roof-repairs/"), ("Roof Replacements", "services/roof-replacements/"),
             ("Storm Damage Repair", "services/storm-damage-repair/"), ("All Articles", "blog/")],
    "about": [("Why Choose Us", "about-us/why-choose-us/"), ("Meet the Team", "meet-the-team/"), ("Certifications", "about-us/certified-roofing-contractor/"),
              ("Case Studies", "case-study/"), ("Service Areas", "service-area/")],
    "term": [("Glossary", "glossary/"), ("Asphalt Shingles", "services/asphalt-shingles/"), ("Roof Replacements", "services/roof-replacements/"),
             ("Blog", "blog/")],
}
LABEL = {"service": "Roofing services", "city": "Service area", "post": "Roofing blog", "about": "About American Roofing",
         "term": "Roofing glossary", "legal": "Legal", "glossary-index": "Roofing glossary", "area-index": "Where we work"}


def trail_for(path, h1, k):
    t = [("Home", "")]
    if k == "post": t.append(("Blog", "blog/"))
    elif k == "term": t.append(("Glossary", "glossary/"))
    elif k == "city": t.append(("Service Areas", "service-area/"))
    elif path.startswith("about-us/") and path != "about-us/": t.append(("About Us", "about-us/"))
    t.append((html.escape(h1), path))
    return t


def make_pages(ex):
    redirects, pages, rec = {}, [], {}
    for r in ex:
        p = path_of(r)
        canon = r.get("canonical")
        own = U + p
        if canon and canon.rstrip("/") != own.rstrip("/"):
            redirects[p] = canon.replace(U, "")
            continue
        rec[p] = r
    posts = sorted([(p, r) for p, r in rec.items() if kind(p) == "post"], key=lambda x: x[1].get("published") or "", reverse=True)
    cities = sorted([(p, r) for p, r in rec.items() if kind(p) == "city"], key=lambda x: x[0])
    terms = sorted([(p, r) for p, r in rec.items() if kind(p) == "term"], key=lambda x: x[0])
    # testimonials pooled from all pages (real client reviews shown on the current site)
    pool, seen = [], set()
    for r in ex:
        for q, a in r["testimonials"]:
            if q not in seen and len(q) > 60: seen.add(q); pool.append([q, a])

    for i, (p, r) in enumerate(sorted(rec.items())):
        k = kind(p)
        h1 = r["h1"] or plain(r["title"]).split("|")[0].strip()
        url = U + p
        page = {"path": p, "title": r["title"], "meta": r["meta"] or "", "canonical": r.get("canonical") or url,
                "modified": (r.get("modified") or "")[:10] or None}
        if k == "home":
            page.update(p_home.build(r, pool, posts)); pages.append(page); continue
        if k == "blog-index":
            page.update(p_blog.index(r, posts)); pages.append(page); continue
        hero = hero_for(p, i)
        if k == "post" and r.get("og_image") in IMGMAP: hero = IMGMAP[r["og_image"]]
        lede = r["meta"] if r["meta"] and len(r["meta"]) < 240 and k != "post" else ""
        extra = ""
        if k == "post" and r.get("published"):
            d = r["published"][:10]
            extra = f'<div class="meta-line"><span>By American Roofing Company</span><span>Published <time datetime="{d}">{d}</time></span></div>'
        body = localize_images(r["body"])
        trail = trail_for(p, h1, k)
        main = body
        if k == "area-index":
            chips = "".join(f'<a href="@/{cp}">{html.escape((cr["h1"] or cp).replace("Roofing", "").strip())}</a>' for cp, cr in cities)
            main = body + f'<h2>Cities we serve</h2><div class="chips">{chips}</div>'
        if k == "glossary-index":
            items = "".join(f'<a class="linkcard" href="@/{tp}"><b>{html.escape(tr["h1"] or tp)}</b><span>{html.escape(tr["meta"][:110])}</span></a>' for tp, tr in terms)
            main = body + f'<h2>Glossary terms</h2><div class="grid">{items}</div>'
        rel = RELATED.get(k, RELATED["service"])
        if k == "city":
            cname = lambda cp: "Roofing in " + re.sub(r"-utah-roofing/?$", "", cp.split("/")[1]).replace("-", " ").title()
            others = [cp for cp, cr in cities if cp != p]
            j = i % max(1, len(others))
            rel = RELATED["city"][:3] + [(cname(o), o) for o in (others[j:] + others[:j])[:2]] + RELATED["city"][3:]
        if k == "post":
            rel = RELATED["post"] + [(pr["h1"] or pp, pp) for pp, pr in posts if pp != p][:3]
        layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        if k == "quote":
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">{body or "<p>Tell us about your roof and we'll set up a free evaluation.</p>"}
<ol class="steps" style="margin-top:28px;grid-template-columns:1fr"><li style="background:var(--navy);color:#fff"><h3>Schedule a roof evaluation</h3><p>We'll learn about your roof and set a convenient time to inspect it.</p></li>
<li style="background:var(--navy);color:#fff"><h3>Review your options</h3><p>A clear scope of work and project pricing before anything is scheduled.</p></li>
<li style="background:var(--navy);color:#fff"><h3>Complete your project</h3><p>Quality workmanship, a final inspection and applicable warranty information.</p></li></ol></div>
<div>{quote_form()}</div></div></section>'''
        faqs = r["faqs"]
        extra_secs = ""
        if faqs:
            extra_secs += f'<section class="sec tight"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Frequently asked questions</h2></div>{faq_html(faqs)}</div></section>'
        extra_secs += quotes_html(r["testimonials"])
        page["body"] = phero(trail, html.escape(h1), html.escape(lede), hero, h1, LABEL.get(k, "American Roofing"), extra) + layout + extra_secs + cta()
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        if k == "service":
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": r["meta"], "url": url,
                        "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "State", "name": "Utah"}})
        elif k == "city":
            city = re.sub(r"-utah-roofing/?$", "", p.split("/")[1]).replace("-", " ").title()
            sch.append({"@type": "Service", "@id": url + "#service", "name": f"Roofing in {city}, UT", "description": r["meta"], "url": url,
                        "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "City", "name": f"{city}, UT"}})
        elif k == "post":
            sch.append({"@type": "BlogPosting", "@id": url + "#article", "headline": plain(h1)[:110], "description": r["meta"], "url": url,
                        "mainEntityOfPage": url, "image": U + "assets/img/" + hero + ".webp",
                        "datePublished": r.get("published") or None, "dateModified": r.get("modified") or r.get("published") or None,
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"})
            page["ogtype"] = "article"
        elif k == "term":
            sch.append({"@type": "DefinedTerm", "@id": url + "#term", "name": plain(h1), "description": r["meta"], "url": url,
                        "inDefinedTermSet": U + "glossary/"})
        elif k == "glossary-index":
            sch.append({"@type": "DefinedTermSet", "@id": U + "glossary/", "name": "Roofing Glossary", "url": url})
        elif k == "about":
            sch.append({"@type": "AboutPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "quote":
            sch.append({"@type": "ContactPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "quote", "city", "area-index")
        pages.append(page)

    # the new blog post
    pages.append(p_blog.ice_dams())
    pages.append({"path": "404.html", "title": "Page Not Found | American Roofing Company", "meta": "That page doesn't exist.",
                  "canonical": None, "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page blew off the roof", "Try one of these instead.",
                                "icicles-snow-overhang-roof", "Icicles on a snowy roof edge", "Error 404")})
    return pages, redirects
