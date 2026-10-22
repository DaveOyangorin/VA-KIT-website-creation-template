import re, html
from build import (U, BIZ_ID, S, ARROW, PHONE, IMG, IMGMAP, img, crumbs_ld, faq_ld, faq_html, cta, side, phero, quote_form)
import p_home, p_blog

# links on the current site that point at pages that don't exist
FIXLINKS = {"roof-types/asphalt-shingle-roofing/": "roof-types/asphalt-shingle/",
            "roof-types/standing-seam-metal-roofing/": "roof-types/metal-roofing/",
            "services/storm-damage/": "services/storm-damage-roof-repair/"}
# pages that should not be rebuilt (recommend a 301 instead)
SKIP = {"sample-page/": ""}

# Per the 5 Oct audit: name South Jordan in the title, H1 and first paragraph of every service page.
# (title, meta or None to keep the client's, H1, answer-first intro written from the client's own facts)
OVERRIDES = {
    "services/roof-repair/": ("Roof Repair in South Jordan, UT | Aesthetic Roofing", None, "Roof Repair in South Jordan, UT",
        "Aesthetic Roofing repairs roof leaks, missing and damaged shingles, flashing and storm damage on homes in South Jordan and across Northern Utah. Every repair starts with a careful assessment, and if your roof can be repaired instead of replaced, we'll tell you."),
    "services/roof-replacement/": ("Roof Replacement in South Jordan, UT | Aesthetic Roofing", None, "Roof Replacement in South Jordan, UT",
        "Aesthetic Roofing replaces roofs in South Jordan and across Northern Utah, and most residential replacements are finished in a single day, including cleanup. Every proposal includes three priced options, and our On-Time Start Guarantee means we start within 14 days of approval or credit 20% back."),
    "services/storm-damage-roof-repair/": ("Storm Damage Roof Repair in South Jordan, UT | Aesthetic", None, "Storm Damage Roof Repair in South Jordan, UT",
        "Aesthetic Roofing repairs hail, wind, tree and debris damage on roofs in South Jordan and across Northern Utah. For storm-damaged roofs we offer an optional insurance concierge service: we document the damage with photos and coordinate with your adjuster on the roofing portion."),
    "services/roof-inspection/": ("Roof Inspection in South Jordan, UT | Aesthetic Roofing", None, "Roof Inspection in South Jordan, UT",
        "Aesthetic Roofing offers a free Roof Health Report to homeowners in South Jordan and across our Northern Utah service area. A certified inspector examines your roof, gives you a clear summary of findings, and outlines your options for repair or replacement."),
    "services/gutter-replacement/": ("Gutter Replacement in South Jordan, UT | Aesthetic Roofing",
        "Gutter replacement in South Jordan, UT. We remove failing gutters and install a sealed new system that moves water away from your home. Get a free quote.",
        "Gutter Replacement in South Jordan, UT",
        "Aesthetic Roofing replaces gutters on homes in South Jordan and across Northern Utah. We remove the damaged or failing system and install new gutters aligned to carry water away from your roof, walls and foundation, with every section secured and sealed."),
    "services/gutter-services/": ("Gutter Installation in South Jordan, UT | Aesthetic Roofing", None, "Gutter Installation in South Jordan, UT",
        "Aesthetic Roofing installs gutters for homes in South Jordan and across Northern Utah, as part of a roofing project or on their own. A properly sized gutter system moves rain and snowmelt away from your roofline and foundation."),
    "roof-types/metal-roofing/": ("Metal Roofing in South Jordan, UT | Aesthetic Roofing", None, "Metal Roofing in South Jordan, UT",
        "Aesthetic Roofing installs standing seam metal roofing on homes in South Jordan and across Northern Utah. Metal roofs are built to handle harsh weather for decades with little maintenance, and they give a home a clean, modern look."),
    "roof-types/": ("Roof Types for South Jordan Homes | Aesthetic Roofing", None, "Roof Types for South Jordan Homes", None),
    "service-areas/": ("Roofing Service Areas in Northern Utah | Aesthetic Roofing",
        "Aesthetic Roofing serves 11 Northern Utah counties from South Jordan, including Salt Lake and Utah County. See where we work and book a free Roof Health Report.",
        None, None),
}


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def kind(p):
    if p == "": return "home"
    if p in ("services/", "roof-types/", "service-areas/"): return "hub"
    if p.startswith("services/"): return "service"
    if p.startswith("roof-types/"): return "material"
    if p.startswith("service-areas/"): return "area"
    if p == "contact/": return "contact"
    if p == "projects/": return "projects"
    if p == "about/": return "about"
    if p == "financing/": return "service"
    if p == "thank-you/": return "thanks"
    return "legal"


HEROES = {"services/roof-repair/": "aerial-new-shingle-roof", "services/roof-replacement/": "aerial-new-roof-yard",
          "services/storm-damage-roof-repair/": "aerial-gray-roof-solar", "services/roof-inspection/": "top-down-new-roof",
          "services/gutter-replacement/": "aerial-home-mountains", "services/gutter-services/": "aerial-roofs-street",
          "roof-types/metal-roofing/": "aerial-home-mountains", "roof-types/flat-roofing/": "top-down-new-roof",
          "roof-types/asphalt-shingle/": "aerial-new-shingle-roof", "roof-types/designer-asphalt-roofing/": "aerial-new-roof-yard",
          "service-areas/salt-lake-county-ut/": "aerial-roofs-street", "service-areas/utah-county-ut/": "crew-on-roof-utah-county",
          "about/": "aesthetic-team", "financing/": "aerial-new-roof-yard", "projects/": "aerial-new-roof-neighborhood",
          "contact/": "aerial-home-mountains"}
FALLBACK = ["aerial-new-roof-neighborhood", "aerial-roofs-street", "aerial-gray-roof-solar", "aerial-new-shingle-roof"]

RELATED = {
    "service": [("Roof Replacement", "services/roof-replacement/"), ("Roof Repair", "services/roof-repair/"),
                ("Storm Damage Roof Repair", "services/storm-damage-roof-repair/"), ("Roof Inspection", "services/roof-inspection/"),
                ("Financing", "financing/")],
    "material": [("All Roof Types", "roof-types/"), ("Roof Replacement", "services/roof-replacement/"), ("Asphalt Shingle", "roof-types/asphalt-shingle/"),
                 ("Metal Roofing", "roof-types/metal-roofing/"), ("Financing", "financing/")],
    "area": [("Roof Replacement", "services/roof-replacement/"), ("Roof Repair", "services/roof-repair/"), ("All Service Areas", "service-areas/"),
             ("Projects", "projects/"), ("Contact", "contact/")],
    "about": [("Projects", "projects/"), ("Services", "services/"), ("Financing", "financing/"), ("Contact", "contact/")],
}
LABEL = {"service": "Roofing services", "material": "Roof types", "area": "Service area", "about": "About us", "hub": "Aesthetic Roofing",
         "legal": "Legal", "projects": "Our work", "contact": "Contact", "thanks": "Thank you"}


def localize(body):
    def one(src, alt):
        name = IMGMAP.get(html.unescape(src))
        # 3D renders are not photos; decorative shapes and the logo mark are not content
        if name and re.search(r"roofing-types-|light-blk-btm|aesthetic-a-yellow", name): return None
        return name
    def gal(m):
        figs = []
        for src, alt in re.findall(r'<img data-src="([^"]+)" alt="([^"]*)">', m.group(1)):
            name = one(src, alt)
            if name: figs.append(f'<figure>{img(name, html.unescape(alt) or "Roof installed by Aesthetic Roofing in Northern Utah")}</figure>')
        return '<div class="gallery">' + "".join(figs) + "</div>" if figs else ""
    body = re.sub(r'<div class="gal">(.*?)</div>', gal, body, flags=re.S)
    def rep(m):
        name = one(m.group(1), m.group(2))
        return f'<figure>{img(name, html.unescape(m.group(2)) or "Roof installed by Aesthetic Roofing in Northern Utah")}</figure>' if name else ""
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox">\1</div>', body, flags=re.S)
    for a, b in FIXLINKS.items(): body = body.replace("@/" + a, "@/" + b)
    return body


def tidy(body, h1):
    # the old pages repeat the page title as loose text above the first paragraph, and use the first photo as a banner
    body = re.sub(r'^\s*(<img data-src="[^"]+" alt="[^"]*">\s*)+', "", body)
    body = re.sub(r"^\s*[^<]{1,80}(?=<(?:p|h2|ul)>)", "", body)
    body = re.sub(r"<p>(?:Testmonials|Testimonials|Our Recent Projects|Project Showcase|View More|Projects)</p>", "", body)
    return body


def make_pages(ex):
    pages, recs = [], {}
    for r in ex:
        p = path_of(r)
        if p in SKIP: continue
        recs[p] = r
    hubs = {"services/": [x for x in recs if kind(x) == "service" and x.startswith("services/")],
            "roof-types/": [x for x in recs if kind(x) == "material"],
            "service-areas/": [x for x in recs if kind(x) == "area"]}
    for i, (p, r) in enumerate(sorted(recs.items())):
        k = kind(p)
        url = U + p
        h1 = r["h1"] or plain(r["title"]).split("|")[0].strip()
        if h1.isupper(): h1 = h1.title()
        page = {"path": p, "title": r["title"], "meta": r["meta"] or "", "canonical": r.get("canonical") or url,
                "modified": (r.get("modified") or "")[:10] or None}
        if k == "home":
            page.update(p_home.build(r)); pages.append(page); continue
        faqs = [f for f in r["faqs"] if plain(f[1]) and f[0] not in ("Services", "Roof Types")]
        hero = HEROES.get(p, FALLBACK[i % len(FALLBACK)])
        body = localize(tidy(r["body"], h1))
        intro = None
        if p in OVERRIDES:
            t, m, h, intro = OVERRIDES[p]
            page["title"] = t
            if m: page["meta"] = m
            if h: h1 = h
        if intro:
            body = f'<div class="answer">{html.escape(intro)}</div>' + body
        trail = [("Home", "")]
        if "/" in p.rstrip("/"):
            parent = p.split("/")[0] + "/"
            trail.append(({"services/": "Services", "roof-types/": "Roof Types", "service-areas/": "Service Areas"}.get(parent, parent), parent))
        trail.append((html.escape(h1), p))
        lede = r["meta"] if r["meta"] and len(r["meta"]) < 240 else ""
        main = body
        if k == "hub":
            cards = "".join(f'<a class="linkcard" href="@/{c}"><b>{html.escape(recs[c]["h1"] or c)}</b><span>{html.escape((recs[c]["meta"] or "")[:120])}</span></a>' for c in sorted(hubs[p]))
            main = f'<div class="grid" style="margin-bottom:40px">{cards}</div>' + body
        if k == "projects":
            main = '<p class="lede" style="color:var(--steel)">Drone and ground photos of roofs we\'ve installed across Northern Utah.</p>' + body
        rel = [x for x in RELATED.get(k, RELATED["service"]) if x[1] != p]
        if k == "contact":
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<h2>Talk to our team</h2><p>Have questions about roof repair, replacement, storm damage, or our Roof Health Report? Call us or fill out the form and our team will get back to you as soon as possible.</p>
<div class="pillars" style="grid-template-columns:1fr">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>Phone</h3><p><a href="tel:{S["tel"]}">{S["phone"]}</a></p></div></div>
<div class="pillar"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></span><div><h3>Email</h3><p><a href="mailto:{S["email"]}">{S["email"]}</a></p></div></div>
<div class="pillar"><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s7-6.2 7-12a7 7 0 1 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg></span><div><h3>Office</h3><p>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</p></div></div>
</div></div><div>{quote_form()}</div></div></section>'''
        elif k == "thanks":
            layout = f'<section class="sec"><div class="wrap prose"><p class="lede">Thanks for reaching out. Our team will contact you shortly.</p><p><a class="btn navy" href="@/">Back to home {ARROW}</a></p></div></section>'
        else:
            layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        extra = ""
        if faqs:
            extra = f'<section class="sec tight white"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Common questions</h2></div>{faq_html(faqs)}</div></section>'
        page["body"] = phero(trail, html.escape(h1), html.escape(lede), hero, h1, LABEL.get(k, "Aesthetic Roofing")) + layout + extra + (cta() if k not in ("legal", "thanks") else "")
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        if k in ("service", "material"):
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": r["meta"], "url": url,
                        "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "AdministrativeArea", "name": "Northern Utah"}})
        elif k == "area":
            county = "Salt Lake County, UT" if "salt-lake" in p else "Utah County, UT"
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": r["meta"], "url": url,
                        "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "AdministrativeArea", "name": county}})
        elif k == "about":
            sch.append({"@type": "AboutPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "contact":
            sch.append({"@type": "ContactPage", "@id": url + "#page", "url": url, "name": "Contact Aesthetic Roofing", "about": {"@id": BIZ_ID}})
        elif k in ("projects", "hub"):
            sch.append({"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "contact", "area", "hub")
        if k == "thanks":
            page["robots"] = "noindex, follow"; page["sitemap"] = False
        pages.append(page)

    pages += p_blog.pages()
    pages.append({"path": "404.html", "title": "Page Not Found | Aesthetic Roofing", "meta": "That page doesn't exist.",
                  "canonical": None, "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn't on the roof", "Try one of these instead.",
                                "top-down-new-roof", "Top-down drone view of a new roof", "Error 404")})
    return pages, SKIP
