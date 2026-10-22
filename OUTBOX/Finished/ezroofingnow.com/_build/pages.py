import re, html, os
from build import (U, BIZ_ID, UT_ID, AR_ID, S, ARROW, PHONE, CHECK, IMG, IMGMAP, INSPECT, CONTACT, img, crumbs_ld, faq_ld,
                   faq_html, quotes_html, cta, side, phero, quote_form)
import p_home, p_blog

HERE = os.path.dirname(os.path.abspath(__file__))
POSTS = {l.strip() for l in open(os.path.join(HERE, "posts.txt"), encoding="utf-8") if l.strip()}
TESTS = {"home-test/", "schedule-a-inspection-test/"}     # test copies of live pages: kept, but out of the index
PROMO = {"25free/", "splash-pass-raffle-page/"}


def path_of(r):
    f = r["file"][:-5]
    return "" if f == "home" else f.replace("__", "/") + "/"


def plain(s): return html.unescape(re.sub(r"<[^>]+>", "", s or "")).strip()


def pick(*urls):
    """First image (by its live URL) that exists locally."""
    for u in urls:
        n = IMGMAP.get(u)
        if n: return n
    return None


def kind(p):
    if p == "": return "home"
    if p in ("blog/", "ez-roofing-blog/"): return "blog-index"
    if p in POSTS: return "post"
    if p in ("utah-city/", "arkansas-city/"): return "area-index"
    if p.startswith(("utah-city/", "arkansas-city/")): return "city"
    if p in ("projects/", "project-spotlight/"): return "projects-index"
    if p.startswith("projects/"): return "project"
    if p in ("team/",): return "team-index"
    if p.startswith("team/"): return "member"
    if p == "contact/": return "quote"
    if p in ("about-ez-roofing/", "the-ez-process/", "welcome-home-guarantee/", "built-by-people/", "careers/",
             "work-b2b-with-ez-roofing/", "ez-roofing-team/", "roofing-reviews-salt-lake-city/"): return "about"
    if p in ("privacy-policy-terms-conditions/", "sms-terms/"): return "legal"
    if p in TESTS | PROMO: return "promo"
    if p in ("utah/", "arkansas/"): return "hub"
    return "service"


def is_utah(p): return p.startswith(("utah/", "utah-city/")) or p == "utah/"


def fix_name(s, p):
    """Utah pages on the live site call the company 'EZ Roofing Arkansas'. On Utah pages it is just 'EZ Roofing'."""
    if not is_utah(p) or not s: return s
    return s.replace("EZ Roofing Arkansas", "EZ Roofing").replace("EZ ROOFING ARKANSAS", "EZ ROOFING")


# Stock photos of models (not EZ Roofing's crew), found on the contact-sheet review: never shown on the new site.
STOCK = {"commercial-roofing-system", "door-installation", "evaluating-roofing-companies", "factors-to-consider-when-choosing-a-roofing-system",
         "nnovative-gutter-solutions", "seasonal-factors-and-timing-for-window-replacement-in-cabot", "the-benefits-of-working-with-a-local-roofing-contractor",
         "the-importance-of-professional-installation", "the-process-of-working-with-a-local-roofing-contractor", "what-is-the-best-time-of-year-to-install-windows",
         "what-you-need-to-know", "when-to-call-a-roofing-contractor", "screenshot-at-apr-01-11-43-45", "screenshot-at-apr-01-11-43-53", "screenshot-at-apr-01-11-44-02"}


def localize_images(body):
    def rep(m):
        src, alt = html.unescape(m.group(1)), html.unescape(m.group(2))
        name = IMGMAP.get(src)
        if not name or name in STOCK: return ""
        return f'<figure>{img(name, alt or "EZ Roofing project")}</figure>'
    body = re.sub(r'<a href="[^"]+\.(?:jpe?g|png|webp)">\s*(<img [^>]+>)\s*</a>', r"\1", body)  # lightbox links around thumbnails
    body = re.sub(r'<img data-src="([^"]+)" alt="([^"]*)">', rep, body)
    body = re.sub(r"<li>\s*(<figure>.*?</figure>)\s*</li>", r"\1", body, flags=re.S)
    body = re.sub(r"<ul>\s*((?:<figure>.*?</figure>\s*){2,})</ul>", r'<div class="gallery">\1</div>', body, flags=re.S)
    body = re.sub(r"<p>\s*(<figure>.*?</figure>)\s*</p>", r"\1", body)
    body = re.sub(r"<p>\s*<p>", "<p>", body); body = re.sub(r"</p>\s*</p>", "</p>", body)
    body = re.sub(r"(<table>.*?</table>)", r'<div class="tablebox">\1</div>', body, flags=re.S)
    body = re.sub(r'<a href="#">View Bio</a>\s*X\s*', "", body)
    body = re.sub(r"^\s*<h5>\s*OUR (?:SERVICES|FINANCING SERVICES)\s*</h5>", "", body)  # label repeated on top of service pages
    body = body.replace('href="https://ezroofingnow.com/', 'href="@/')
    body = re.sub(r'href="(?:mailto:)?([\w.+-]+@[\w-]+\.[\w.]+)"', r'href="mailto:\1"', body)
    for old, new in FIXLINKS.items(): body = body.replace(f'href="@/{old}"', f'href="@/{new}"')
    return body


# Old internal links that redirect on the live site: point them straight at the final page.
FIXLINKS = {"arkansas-city/conway/": "arkansas-city/conway-arkansas/"}


def auto_meta(r, h1):
    """Pages with no meta description get one from their own first paragraph (marked in the notes)."""
    txt = plain(" ".join(re.findall(r"<p>(.*?)</p>", r["body"])[:3]))
    txt = re.sub(r"\s+", " ", txt)
    if len(txt) < 60: txt = f"{h1}. EZ Roofing: roof repair, replacement and free roof inspections in Salt Lake City, Utah and Cabot, Arkansas."
    if len(txt) > 158: txt = txt[:155].rsplit(" ", 1)[0].rstrip(",;:") + "..."
    return txt


RELATED = {
    "service": [("Our free inspection", INSPECT), ("Storm damage", "roof-storm-damage/"), ("New roof", "get-a-new-roof/"), ("Financing", "financing/"), ("Contact", CONTACT)],
    "ut": [("Roof repair in Salt Lake City", "utah/salt-lake-city-roof-repair/"), ("Roof replacement in Salt Lake City", "utah/salt-lake-city-roof-replacement/"),
           ("Free roof inspection in Salt Lake City", "utah/salt-lake-city-free-roof-inspection/"), ("Roofing in Salt Lake City", "utah-city/salt-lake-city/"), ("All Utah cities", "utah-city/")],
    "ar": [("Roof repair in Cabot", "arkansas/cabot-roof-repair/"), ("Roof replacement in Cabot", "arkansas/cabot-roof-replacement/"),
           ("Free roof inspection in Cabot", "arkansas/cabot-free-roof-inspection/"), ("Roofing in Cabot", "arkansas-city/cabot/"), ("All Arkansas cities", "arkansas-city/")],
    "post": [("Our free inspection", INSPECT), ("Storm damage", "roof-storm-damage/"), ("New roof", "get-a-new-roof/"), ("All articles", "blog/")],
    "about": [("About EZ Roofing", "about-ez-roofing/"), ("Our process", "the-ez-process/"), ("Meet our team", "ez-roofing-team/"), ("Welcome Home Guarantee", "welcome-home-guarantee/"), ("Customer reviews", "roofing-reviews-salt-lake-city/")],
}
LABEL = {"service": "Roofing services", "city": "Service area", "post": "Roofing blog", "about": "About EZ Roofing", "legal": "Legal",
         "project": "Project spotlight", "member": "Our team", "promo": "Free inspection", "hub": "Locations", "quote": "Contact"}


def state_of(p):
    if p.startswith(("utah/", "utah-city/")) or p == "utah/": return "ut"
    if p.startswith(("arkansas/", "arkansas-city/")) or p == "arkansas/": return "ar"
    return None


def trail_for(p, h1, k):
    t = [("Home", "")]
    st = state_of(p)
    if k == "post": t.append(("Blog", "blog/"))
    elif k == "city": t.append(("Utah cities" if st == "ut" else "Arkansas cities", "utah-city/" if st == "ut" else "arkansas-city/"))
    elif k == "service" and st: t.append(("Utah" if st == "ut" else "Arkansas", "utah/" if st == "ut" else "arkansas/"))
    elif k == "project": t.append(("Projects", "projects/"))
    elif k == "member": t.append(("Our team", "ez-roofing-team/"))
    t.append((html.escape(h1), p))
    return t


def hero_for(p, k, r, i, pool):
    if k == "post" and r.get("og_image") in IMGMAP and IMGMAP[r["og_image"]] not in STOCK: return IMGMAP[r["og_image"]]
    own = [IMGMAP[u] for u in r["images"] if u in IMGMAP and IMGMAP[u] not in STOCK and IMG[IMGMAP[u]][0] >= 900]
    if own: return own[0]
    return pool[i % len(pool)]


def make_pages(ex):
    pages, rec = [], {}
    for r in ex:
        rec[path_of(r)] = r
    posts = sorted([(p, r) for p, r in rec.items() if kind(p) == "post"], key=lambda x: x[1].get("published") or "", reverse=True)
    pool = p_home.HERO_POOL()
    pools = {"ut": p_home.HERO_POOL("ut"), "ar": p_home.HERO_POOL("ar")}
    # real reviews quoted on the current site (reviews page)
    tests = []
    for q, a in re.findall(r"<blockquote><p>(.*?)</p>(.*?)</blockquote>", rec.get("roofing-reviews-salt-lake-city/", {"body": ""})["body"], re.S):
        tests.append([plain(q), plain(a)])

    for i, (p, r) in enumerate(sorted(rec.items())):
        k = kind(p)
        h1 = fix_name(plain(r["h1"] or r.get("entry_title") or r["title"].split("|")[0]), p)
        if k in ("project",) and not r["h1"]:
            m = re.search(r"<h2>(.*?)</h2>", r["body"]); h1 = plain(m.group(1)) if m else plain(r["title"].split("|")[0])
        if h1.lower() in ("quality roofing services", "our services", "") or k in ("hub",):
            h1 = plain(r["title"].split("|")[0])
        url = U + p
        title = fix_name(r["title"], p)
        meta = fix_name(r["meta"], p) or auto_meta(r, h1)
        page = {"path": p, "title": title, "meta": meta, "canonical": r.get("canonical") or url, "modified": (r.get("modified") or "")[:10] or None,
                "auto_meta": not r["meta"]}
        if k == "home":
            page.update(p_home.build(r, rec, posts, tests)); pages.append(page); continue
        hero = hero_for(p, k, r, i, pools.get(state_of(p), pool))
        st = state_of(p)
        body = fix_name(localize_images(r["body"]), p)
        if k == "post" and body.startswith("<figure>"):
            body = re.sub(r"^<figure>.*?</figure>", "", body, count=1, flags=re.S)  # same photo as the hero
        lede = ""
        extra = ""
        if k == "post" and r.get("published"):
            d = r["published"][:10]
            extra = f'<div class="meta-line"><span>By EZ Roofing</span><span>Published <time datetime="{d}">{d}</time></span></div>'
        trail = trail_for(p, h1, k)
        main = body
        if k == "blog-index":
            cards = "".join(f'<a class="postcard reveal" href="@/{pp}">{img(hero_for(pp, "post", pr, j, pool), plain(pr["h1"] or pp))}<div class="in"><small>{(pr.get("published") or "")[:10]}</small><b>{html.escape(plain(pr["h1"] or pp))}</b></div></a>'
                            for j, (pp, pr) in enumerate([(p_blog.PATH, {"h1": "The Best Time of Year to Replace a Roof in Utah", "published": "2026-10-17", "og_image": None, "images": []})] + posts))
            page["body"] = phero(trail, "EZ Roofing Blog", "Roofing advice for homeowners in Utah and Arkansas.", hero, "Roof project", "Roofing blog") + \
                f'<section class="sec"><div class="wrap"><div class="postgrid">{cards}</div></div></section>' + cta()
            page["schema"] = [crumbs_ld(url, trail), {"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": "EZ Roofing Blog"}]
            page["full_biz"] = False; pages.append(page); continue
        if k == "area-index":
            pref = p
            cities = sorted([(cp, cr) for cp, cr in rec.items() if cp.startswith(pref) and cp != pref])
            chips = "".join(f'<a href="@/{cp}">{html.escape(plain(cr["h1"] or cp).replace("Roofing Company in ", ""))}</a>' for cp, cr in cities)
            stn = "Utah" if p.startswith("utah") else "Arkansas"
            L = S["ut" if stn == "Utah" else "ar"]
            h1 = f"{stn} Service Areas"
            main = f'<p>EZ Roofing serves homeowners and businesses across {stn} from our office at {L["street"]}, {L["city"]}, {L["st"]} {L["zip"]}. Choose your city:</p><div class="chips">{chips}</div>'
            trail = [("Home", ""), (h1, p)]
            if not r["meta"]: page["meta"] = f"EZ Roofing service areas in {stn}: roof repair, roof replacement and free roof inspections from our {L['city']} office. Find your city and call {L['phone']}."
            page["title"] = f"{stn} Service Areas | EZ Roofing"
        if k == "projects-index":
            projs = sorted([(pp, pr) for pp, pr in rec.items() if kind(pp) == "project"])
            cards = ""
            for pp, pr in projs:
                ph = hero_for(pp, "project", pr, 0, pool)
                nm = re.search(r"<h2>(.*?)</h2>", pr["body"]); nm = plain(nm.group(1)) if nm else plain(pr["title"].split("|")[0])
                loc = re.search(r"<h5>(.*?)</h5>", pr["body"]); loc = plain(loc.group(1)) if loc else ""
                cards += f'<a class="postcard reveal" href="@/{pp}">{img(ph, nm)}<div class="in"><small>{html.escape(loc)}</small><b>{html.escape(nm)}</b></div></a>'
            main = (body if k == "projects-index" and p == "project-spotlight/" and len(plain(body)) > 200 else "") + f'<div class="postgrid">{cards}</div>'
            if p == "projects/": h1 = "Projects"; trail = [("Home", ""), ("Projects", p)]
            if not r["meta"]: page["meta"] = "Roofing projects by EZ Roofing in Utah and Arkansas: residential roofs, a subdivision and a commercial plaza, with photos and the upgrades on each roof."
            page["title"] = page["title"] if r["meta"] else "Projects | EZ Roofing Utah & Arkansas"
        if k == "team-index":
            members = sorted([(mp, mr) for mp, mr in rec.items() if kind(mp) == "member"])
            main = '<p>Meet the people behind EZ Roofing on our <a href="@/ez-roofing-team/">team page</a>.</p><div class="chips">' + "".join(
                f'<a href="@/{mp}">{html.escape(plain(mr.get("entry_title") or mr["h1"] or mp).title())}</a>' for mp, mr in members) + "</div>"
            h1 = "Our Team"; trail = [("Home", ""), ("Our team", p)]
            page["title"] = "Team | EZ Roofing Utah & Arkansas"; page["meta"] = "The EZ Roofing team in Utah and Arkansas. Meet the people who inspect, plan and manage your roofing project, from the owner to our project managers."
        if k == "member":
            nm = plain(r.get("entry_title") or r["h1"]).title()
            h1 = nm
            main = f'<p>{html.escape(nm)} is part of the EZ Roofing team. Read more about our people on the <a href="@/ez-roofing-team/">Meet Our Team</a> page.</p>'
            page["robots"] = "noindex, follow"; page["sitemap"] = False
            page["title"] = f"{nm} | EZ Roofing Team"; page["meta"] = f"{nm}, EZ Roofing team member. Meet the EZ Roofing team in Utah and Arkansas."
        if k == "promo" and p in TESTS:
            page["robots"] = "noindex, follow"; page["sitemap"] = False
        if k == "city":
            sibs = sorted([cp for cp in rec if cp.startswith(p.split("/")[0] + "/") and cp != p.split("/")[0] + "/" and cp != p])
            j = i % max(1, len(sibs)); near = (sibs[j:] + sibs[:j])[:6]
            main = body + '<h2>Nearby service areas</h2><div class="chips">' + "".join(f'<a href="@/{cp}">{html.escape(plain(rec[cp]["h1"] or cp).replace("Roofing Company in ", ""))}</a>' for cp in near) + "</div>"
        rel = RELATED.get(k) or RELATED.get(st or "", None) or RELATED["service"]
        if k in ("service", "city", "hub") and st: rel = RELATED[st]
        if k == "post":
            rel = RELATED["post"] + [(plain(pr["h1"] or pp)[:60], pp) for pp, pr in posts if pp != p][:3]
        layout = f'<section class="sec"><div class="wrap layout"><article class="prose">{main}</article>{side(rel)}</div></section>'
        if k == "quote":
            layout = f'''<section class="sec"><div class="wrap split" style="align-items:start"><div class="prose">
<p>We offer a free annual inspection to assess the wear and tear of your roof from year to year. If you have an immediate situation from storm damage or another concern, we&rsquo;ll inspect your roof for free. Request an appointment, or call us.</p>
<div class="pillars" style="grid-template-columns:1fr;margin-top:18px">
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>{S["ar"]["name"]} &middot; Headquarters</h3><p>{S["ar"]["street"]}<br>{S["ar"]["city"]}, {S["ar"]["st"]} {S["ar"]["zip"]}<br><a href="tel:{S["ar"]["tel"]}">{S["ar"]["phone"]}</a></p></div></div>
<div class="pillar"><span class="ic">{PHONE}</span><div><h3>{S["ut"]["name"]}</h3><p>{S["ut"]["street"]}<br>{S["ut"]["city"]}, {S["ut"]["st"]} {S["ut"]["zip"]}<br><a href="tel:{S["ut"]["tel"]}">{S["ut"]["phone"]}</a></p></div></div>
</div><p style="margin-top:16px"><a href="mailto:{S["email"]}">{S["email"]}</a> &middot; {S["hours"]}</p>
<p>Emergency? Call or text <a href="tel:{S["emergency_tel"]}">{S["emergency"]}</a> for 24-hour emergency service.</p></div>
<div>{quote_form()}</div></div></section>'''
            h1 = "Contact EZ Roofing"; trail = [("Home", ""), ("Contact", p)]
        faqs = r["faqs"]
        extra_secs = ""
        if faqs:
            extra_secs += f'<section class="sec tight"><div class="wrap" style="max-width:900px"><div class="head reveal"><p class="label">FAQs</p><h2>Frequently asked questions</h2></div>{faq_html(faqs)}</div></section>'
        if k == "about" and p == "roofing-reviews-salt-lake-city/":
            extra_secs += quotes_html(tests)
        page["body"] = phero(trail, html.escape(h1), html.escape(lede), hero, h1, LABEL.get(k, "EZ Roofing"), extra) + layout + extra_secs + cta()
        page["og"] = hero
        sch = [crumbs_ld(url, trail)]
        prov = {"@id": UT_ID if st == "ut" else AR_ID if st == "ar" else BIZ_ID}
        if k in ("service", "hub"):
            sch.append({"@type": "Service", "@id": url + "#service", "name": plain(h1), "description": page["meta"], "url": url, "provider": prov,
                        "areaServed": {"@type": "State", "name": {"ut": "Utah", "ar": "Arkansas"}.get(st, "Utah")} if st else [{"@type": "State", "name": "Utah"}, {"@type": "State", "name": "Arkansas"}]})
        elif k == "city":
            city = re.sub(r"^(Roofing Company in )", "", plain(r["h1"] or "")).strip()
            sch.append({"@type": "Service", "@id": url + "#service", "name": f"Roofing in {city}", "description": page["meta"], "url": url, "provider": prov,
                        "areaServed": {"@type": "City", "name": city}})
        elif k == "post":
            sch.append({"@type": "BlogPosting", "@id": url + "#article", "headline": plain(h1)[:110], "description": page["meta"], "url": url,
                        "mainEntityOfPage": url, "image": U + "assets/img/" + hero + ".webp",
                        "datePublished": r.get("published") or None, "dateModified": r.get("modified") or r.get("published") or None,
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "inLanguage": "en-US"})
            page["ogtype"] = "article"
        elif k in ("about",):
            sch.append({"@type": "AboutPage", "@id": url + "#page", "url": url, "name": plain(h1), "about": {"@id": BIZ_ID}})
        elif k == "quote":
            sch.append({"@type": "ContactPage", "@id": url + "#page", "url": url, "name": "Contact EZ Roofing", "about": {"@id": BIZ_ID}})
        elif k in ("projects-index", "area-index", "team-index"):
            sch.append({"@type": "CollectionPage", "@id": url + "#page", "url": url, "name": plain(h1)})
        if faqs: sch.append(faq_ld(faqs))
        page["schema"] = sch
        page["full_biz"] = k in ("about", "quote", "city", "area-index", "hub")
        pages.append(page)

    pages.append(p_blog.new_post())
    pages.append({"path": "404.html", "title": "Page Not Found | EZ Roofing", "meta": "That page doesn't exist.", "canonical": None,
                  "robots": "noindex, follow", "sitemap": False, "full_biz": False, "schema": [],
                  "body": phero([("Home", ""), ("Not found", "404.html")], "This page isn&rsquo;t here", "Try the home page, or schedule a free inspection.",
                                pool[0], "Roof", "Error 404")})
    return pages, {}
