"""Pages for the swiftrestoreutah.com redesign: "From flood to finish".

Swift does two jobs most companies split: emergency restoration (water, fire, mold, sewage) and the rebuild and remodel after
it. Their own photos show the whole arc: air movers and dehumidifiers drying a basement, containment walls, opened-up walls,
framing, then finished bathrooms and bedrooms. So the site tells that arc. References (screenshotted 20 Oct 2026): Belfor
(black, a red diagonal cut, urgent bold type), Paul Davis (dark hero with an emergency phone panel), Bluestem Remodeling
(editorial serif italics over finished interiors). Signature: a pinned horizontal recovery timeline (scrolling down moves
the job sideways from the 24/7 call to the finished room), plus before/after drag sliders.
All 266 live URLs kept (Duda site, no trailing slash) with their own canonicals. Home targets "water damage restoration
ogden" (report); service pages name Ogden in title, H1 and first paragraph.
Left out until confirmed: "BBB accredited" (city pages), any "best / #1" wording; the free carpet-cleaning gift offer is kept
as the client states it on its own page.
"""
import html, json, os, re
from engine import img, crumbs_ld, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, ST
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
BLOGIMG = json.load(open(os.path.join(HERE, "blogimg.json"), encoding="utf-8"))
STOP = ("Call Now for Emergency Water Damage Help", "Restore Now, Pay Over Time", "Our Service Areas", "Get A Free Estimate", "NEED HELP WITH DISASTER", "Loading ", "Share this")
SKIP = ("Blog Layout", "GET A QUOTE", "Get A Quote", "Get a Quote", "Updated On:", "Author:")
CLAIMS = re.compile(r"BBB accredited|the best\b|#1\b|top[- ]rated|number one", re.I)
POOL = ["air-mover", "basement-drying", "containment", "demo-bathroom", "rebuild-bath", "finished-bath", "after-remodel", "dehumidifier-air-movers", "demo-open-wall", "finished-bath-2",
        "living-room-dryout", "bedroom-mitigation", "ceiling-leak", "air-scrubbers", "after-restoration", "kitchen-transformation", "fire-kitchen-rebuilt", "demo-basement", "rebuild-bath-2", "after-remodel-2"]
SVC_IMG = {"water-damage-restoration": "basement-drying", "flooded-basement-cleanup": "demo-basement", "fire-damage-restoration": "fire-kitchen-rebuilt", "ogden-mold-removal": "containment",
           "mold-inspection": "containment-bed", "ogden-sewage-cleanup": "demo-open-wall", "leak-detection": "ceiling-leak", "boardup-services": "demo-bathroom-2", "kitchen-remodeling": "kitchen-transformation",
           "bathroom-remodeling": "finished-bath", "reconstruction": "rebuild-bath", "commercial-damage-restoration": "air-scrubbers", "residential-damage-restoration": "living-room-dryout",
           "insurance-claims-restoration-ogden": "bedroom-mitigation", "remodeling-services": "after-remodel", "restoration-services": "dehumidifier-air-movers", "general-contractor": "rebuild-bath-2",
           "odor-removal": "air-scrubbers", "disinfection": "containment", "contents-cleaning": "containment-bed", "lead-paint-removal": "demo-open-wall", "disaster-cleanup": "demo-basement"}
CASE_IMG = {"from-water-damage-to-full-remodel-a-kitchen-and-bathroom-reconstruction-in-hyrum-ut": "case-hyrum", "full-sewage-cleanup-and-reconstruction-for-a-millcreek-utah-condo": "case-millcreek",
            "kaysville-basement-flood-emergency-storm-water-cleanup-and-mold-mitigation": "case-kaysville-flood", "kaysville-home-remodel-new-kitchen-custom-storage-and-a-total-refresh": "case-kaysville-remodel",
            "kaysville-multi-room-water-damage-restoration": "case-kaysville-rooms", "new-roof-and-garage-build-for-a-farmington-ut-homeowner": "case-farmington-garage",
            "transforming-a-90s-basement-into-a-modern-family-space-in-layton-ut": "case-layton-basement", "when-water-damage-strikes-a-complete-basement-restoration-in-farmington-ut": "case-farmington-basement",
            "a-full-exterior-remodel-and-attic-conversion": "attic-conversion", "a-complete-transformation-after-fire-damage-recovery": "kitchen-transformation", "full-remodel-of-a-fire-damaged-house": "fire-kitchen-rebuilt",
            "multi-room-transformation-in-ogden-ut": "after-remodel"}


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    p = re.sub(r"/+", "/", p)
    return (p.strip("/") + "/") if p.strip("/") else ""


def meta_line(k, fallback):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    m = re.sub(r"\s*-?\s*\(385\)\s*412-8633\s*-?\s*", " ", m).strip()
    if len(m) < 110: m = fallback
    return m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "..."


def clean_title(k):
    t = html.unescape(EXT[k]["title"]).replace("–", "-")
    t = re.sub(r"\s*-\s*\(385\)\s*412-8633\s*", " ", t)
    t = re.sub(r"\s*[|-]\s*Swift Restoration (?:and|&) Remodel\w*.*$", "", t).strip(" -|")
    return t


def mig(k, skip=()):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x"))
    meta = {}
    m = re.search(r"Updated On:</p>\s*<h3>([^<]+)</h3>\s*<p>Author:</p>\s*(?:<h3>([^<]+)</h3>)?", raw)
    if m: meta = {"date": m.group(1).strip(), "author": (m.group(2) or "").strip()}
    raw = re.sub(r"<p>id=\"dmRoot\".*?</p>", "", raw)
    raw = re.sub(r"Updated On:</p>\s*<h3>[^<]+</h3>\s*<p>Author:</p>\s*(?:<h3>[^<]+</h3>)?", "</p>", raw)
    s = tidy(raw, claims=CLAIMS, stop=STOP, skip=SKIP + tuple(skip))
    s = s.replace("Odgen", "Ogden").replace("The trailhead is located just outside of Park City, Utah.", "")
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    return s.strip(), faqs, meta


def pool(i): return POOL[i % len(POOL)]


def svc_pages():
    out = []
    keys = [k for k in EXT if k.startswith("services_")]
    for i, k in enumerate(keys):
        p = path_of(k); parts = p.strip("/").split("/")
        slug = parts[1] if len(parts) > 1 else parts[0]
        c, f, meta = mig(k)
        t0 = clean_title(k)
        if len(parts) == 2:
            lab = re.sub(r"(?i)\b(ogden|in ogden ut|ogden ut|services?|swift)\b", "", t0).strip(" -|,") or t0
            lab = re.sub(r"\s{2,}", " ", lab).strip()
            h1 = f"{lab} in Ogden"
            t = f"{lab} in Ogden, UT | Swift Restoration"
            intro = f"Swift Restoration and Remodeling provides {html.unescape(lab).lower()} in Ogden and across Weber and Davis counties, 24/7, from our office on Pennsylvania Avenue."
            crumbs = [("Services", "services/water-damage-restoration/")] if slug != "water-damage-restoration" else []
            im = SVC_IMG.get(slug, pool(i))
            tag = "Service"
        else:
            h1 = t0; t = f"{t0} | Swift Restoration"; intro = ""; im = SVC_IMG.get(parts[1], pool(i)) if parts[1] in SVC_IMG else pool(i)
            pk = "services_" + parts[1].replace("-", "_")
            crumbs = [(clean_title(pk).split(" in ")[0][:30] if pk in EXT else "Services", parts[0] + "/" + parts[1] + "/")]
            tag = "Guide"
        if len(t) > 64: t = t[:61].rsplit(" ", 1)[0]
        m = meta_line(k, f"{html.unescape(h1)}: 24/7 water, fire and mold restoration and remodeling from Swift Restoration and Remodeling in Ogden, Utah.")
        out.append(K.page(p, h1.split(" in Ogden")[0][:36], h1, None, tag, t, m, c, image=im, alt=f"{html.unescape(h1)}: Swift Restoration job photo", intro=intro, crumbs=crumbs, faqs=f,
                          canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, html.unescape(h1), "Ogden, UT") if tag == "Service" else None))
    return out


def area_pages():
    out = []
    for i, k in enumerate([k for k in EXT if k.startswith("service_areas_")]):
        p = path_of(k); parts = p.strip("/").split("/")
        c, f, meta = mig(k)
        t0 = clean_title(k)
        if len(parts) == 2:
            city = re.sub(r"(?i)water damage restoration|water damage|restoration|in|-|mold|fire|&|ut$|utah", " ", t0)
            city = re.sub(r"\s{2,}", " ", city).strip(" ,|") or t0
            h1 = f"Water Damage Restoration in {city}, UT"
            t = f"Water Damage Restoration {city}, UT | Swift"
            m = meta_line(k, f"Water damage restoration in {city}, Utah: 24/7 water extraction, drying, mold, fire and rebuild from Swift Restoration and Remodeling in Ogden.")
            out.append(K.page(p, city, h1, None, "Service area", t, m, c, image=pool(i + 3), alt=f"Swift Restoration job photo", crumbs=[("Service Areas", "service-areas/")], faqs=f, canonical=EXT[k]["canon"] or None,
                              schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Water damage restoration in {city}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": city + ", UT"}}]))
        else:
            out.append(local_page(k, p, c, f, i, crumbs=[("Service Areas", "service-areas/")]))
    return out


def local_page(k, p, c, f, i, crumbs=None):
    t0 = clean_title(k)
    return K.page(p, t0[:36], t0, "A local guide from Swift Restoration and Remodeling in Ogden.", "Local guide", f"{t0} | Swift Restoration, Ogden"[:64],
                  meta_line(k, f"{t0}: a local guide to Northern Utah from Swift Restoration and Remodeling, Ogden's 24/7 water, fire and mold restoration and remodeling team."),
                  c, image=pool(i + 7), alt="Swift Restoration job photo", crumbs=crumbs, faqs=f, canonical=EXT[k]["canon"] or None)


def case_pages():
    out = []
    keys = [k for k in EXT if k.startswith("case_studies_")]
    for i, k in enumerate(keys):
        p = path_of(k); slug = p.strip("/").split("/")[-1]
        c, f, meta = mig(k)
        t0 = clean_title(k)
        im = CASE_IMG.get(slug, pool(i + 2))
        out.append(K.page(p, t0[:36], t0, f"Case study{(' &middot; ' + meta['date']) if meta.get('date') else ''}", "Our work", f"{t0} | Swift Restoration"[:64],
                          meta_line(k, f"{t0}: a Swift Restoration and Remodeling project from first call to finished rebuild, with photos from the job."),
                          c, image=im, alt=t0, crumbs=[("Our work", "case-studies/")], faqs=f, canonical=EXT[k]["canon"] or None, ogtype="article"))
    return out


def tip_pages():
    out, cards = [], []
    keys = [k for k in EXT if k.startswith("restoration_tips_")]
    for i, k in enumerate(keys):
        p = path_of(k)
        c, f, meta = mig(k)
        t0 = clean_title(k)
        im = BLOGIMG.get(k) or pool(i)
        by = " &middot; ".join(x for x in (meta.get("author"), meta.get("date")) if x)
        pg = K.page(p, t0[:36], t0, by or None, "Restoration tips", f"{t0} | Swift Restoration"[:64], meta_line(k, f"{t0}: restoration tips for Northern Utah homeowners from Swift Restoration and Remodeling in Ogden, available 24/7."),
                    c, image=im, alt=t0, crumbs=[("Restoration tips", "restoration-tips/")], faqs=f, canonical=EXT[k]["canon"] or None, ogtype="article")
        pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
        pg["schema"].append({"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t0, "image": U + f"assets/img/{im}.webp", "author": {"@type": "Person", "name": meta.get("author") or "Darin Jenks"},
                             "publisher": {"@id": U + "#business"}, "mainEntityOfPage": EXT[k]["canon"] or canon(p)})
        out.append(pg); cards.append((t0, p, im, meta.get("date", "")))
    return out, cards


def root_pages(tip_cards, case_keys):
    out = []
    def r(k, h1, lede, tag, t, mfb, pre="", post="", image=None, form_side=False, extra_skip=()):
        c, f, meta = mig(k, skip=extra_skip)
        out.append(K.page(path_of(k), h1[:36], h1, lede, tag, t, meta_line(k, mfb), pre + c + post, image=image, alt=h1, faqs=f, form_side=form_side, canonical=EXT[k]["canon"] or None))
    r("about_us", "About Swift Restoration and Remodeling", "Locally owned in Ogden since 2009.", "About", "About Swift Restoration and Remodeling | Ogden, UT",
      "Swift Restoration and Remodeling is locally owned and has served Ogden since 2009, with over 13 years in restoration and over 30 years in construction.", image="darin-jenks", extra_skip=("About Us",))
    r("contact", "Contact Swift Restoration and Remodeling", "24/7 emergency service from our Ogden office.", "Contact", "Contact Swift Restoration and Remodeling | Ogden 24/7",
      "Contact Swift Restoration and Remodeling, 2900 Pennsylvania Ave, Unit C, Ogden, UT 84401. Call (385) 412-8633, 24/7 emergency service. License 4853926-5501.",
      pre=f'''<dl class="info"><div><dt>Office</dt><dd>{ST["street"]}, Ogden, UT {ST["zip"]}</dd></div><div><dt>Phone</dt><dd><a href="tel:{ST["tel"]}">{ST["phone"]}</a></dd></div><div><dt>Hours</dt><dd>24/7 emergency service</dd></div><div><dt>License</dt><dd>Contractor license numbers {ST["license"]}</dd></div></dl>''',
      form_side=True, extra_skip=("Contact", "Contact Swift Restoration and Remodeling"))
    for k, h1, tag, t, mfb in [("reviews", "Reviews", "Reviews", "Reviews | Swift Restoration and Remodeling, Ogden", "Reviews of Swift Restoration and Remodeling, Ogden's 24/7 water, fire and mold restoration and remodeling company. IICRC certified, locally owned since 2009."),
                               ("financing", "Restoration Financing", "Financing", "Restoration Financing | Swift Restoration, Ogden UT", "Restore now, pay over time: financing for water, fire and mold restoration and remodeling in Ogden through Hearth, from Swift Restoration and Remodeling."),
                               ("gift", "A Free Gift for You", "Offer", "Free Gift | Swift Restoration and Remodeling, Ogden", "A free gift from Swift Restoration and Remodeling in Ogden: one room of free carpet cleaning and a free 15-minute carpet inspection for new customers."),
                               ("consumer_report", "Consumer's Insider Guide to Carpet Cleaning", "Guide", "Carpet Cleaning Consumer Report | Swift Restoration", "Special report: a consumer's insider guide to carpet cleaning from Swift Restoration and Remodeling in Ogden, Utah, plus a free 15-minute carpet inspection."),
                               ("social_wall", "Social Wall", "Social", "Social Wall | Swift Restoration and Remodeling, Ogden", "Follow Swift Restoration and Remodeling on social media: water, fire and mold restoration and remodeling projects across Ogden and Northern Utah."),
                               ("spotting_guide", "Spotting Guide", "Guide", "Carpet Spotting Guide | Swift Restoration and Remodeling", "A carpet spotting guide from Swift Restoration and Remodeling in Ogden: how to treat common spots and stains, and when to call in a professional cleaner."),
                               ("press_releases", "Press Releases", "News", "Press Releases | Swift Restoration and Remodeling, Ogden", "Press releases and news from Swift Restoration and Remodeling, Ogden's locally owned water, fire and mold restoration and remodeling company since 2009."),
                               ("privacy_policy", "Privacy Policy", "Legal", "Privacy Policy | Swift Restoration and Remodeling", "The privacy policy for swiftrestoreutah.com: what Swift Restoration and Remodeling collects through its forms and website, how it is used and your choices."),
                               ("terms_of_service", "Terms of Service", "Legal", "Terms of Service | Swift Restoration and Remodeling", "The terms of service for swiftrestoreutah.com, the website of Swift Restoration and Remodeling in Ogden, Utah: use of the site, content and limitations."),
                               ("kitchen_bathroom_remodeling", "Kitchen &amp; Bathroom Remodeling in Ogden", "Remodeling", "Kitchen &amp; Bathroom Remodeling in Ogden | Swift", "Kitchen and bathroom remodeling in Ogden from Swift Restoration and Remodeling: design, demolition, rebuild and finishes from a local licensed contractor."),
                               ("how_to_prevent_mold_during_utah_s_humid_summer_months", "How to Prevent Mold During Utah's Humid Summer Months", "Restoration tips", "Preventing Mold in Utah Summers | Swift Restoration", "How to prevent mold during Utah's humid summer months: ventilation, humidity control and leak checks from Swift Restoration and Remodeling in Ogden.")]:
        r(k, h1, None, tag, t, mfb, extra_skip=(h1,), image="finished-bath" if "remodel" in k else None)
    # listings
    tips = "".join(f'<a class="post-card reveal-up" href="@/{p}">{img(im, "")}<span class="pc-d">{d}</span><b>{t}</b><em>Read {ARROW}</em></a>' for t, p, im, d in tip_cards)
    out.append(K.page("restoration-tips/", "Restoration tips", "Restoration Tips", "Water, fire, mold and remodeling advice for Northern Utah homeowners.", "Blog", "Restoration Tips | Swift Restoration and Remodeling",
                      "Restoration tips from Swift Restoration and Remodeling in Ogden: water damage, flooded basements, fire and smoke, mold, insurance claims and remodeling advice.",
                      f'<div class="posts">{tips}</div>', canonical=EXT["restoration_tips"]["canon"] or None))
    cases = "".join(f'<a class="post-card reveal-up" href="@/{path_of(k)}">{img(CASE_IMG.get(path_of(k).strip("/").split("/")[-1], pool(i + 2)), "")}<b>{clean_title(k)}</b><em>See the job {ARROW}</em></a>' for i, k in enumerate(case_keys))
    out.append(K.page("case-studies/", "Our work", "Our Work: Case Studies", "Water, fire and remodeling jobs across Northern Utah, start to finish.", "Our work", "Case Studies | Swift Restoration and Remodeling, Ogden",
                      "Case studies from Swift Restoration and Remodeling: water damage, sewage, fire and full remodels in Ogden, Layton, Kaysville, Farmington, Roy, Hyrum and more.",
                      f'<div class="posts">{cases}</div>', image="after-remodel", alt="Bedroom after a Swift remodel", canonical=EXT["case_studies"]["canon"] or None))
    c, f, meta = mig("service_areas")
    areas = "".join(f'<li><a href="@/{path_of(k)}">{re.sub(r"(?i)water damage restoration|water damage|restoration| in |-|mold|fire|&| ut$|utah", " ", clean_title(k)).strip()}</a></li>' for k in EXT if k.startswith("service_areas_") and path_of(k).count("/") == 2)
    out.append(K.page("service-areas/", "Service Areas", "Our Service Areas", "Ogden, Weber and Davis counties, and up to Brigham City.", "Service areas", "Service Areas | Swift Restoration and Remodeling, Ogden",
                      "Swift Restoration and Remodeling serves Ogden, Layton, Kaysville, Farmington, Bountiful, North Salt Lake, Roy, Harrisville, Huntsville, West Haven, Plain City and Brigham City.",
                      f'<figure class="sheet map-fig">{img("swift-map", "Map of Northern Utah with Ogden marked")}</figure><ul class="chips">{areas}</ul>' + c, canonical=EXT["service_areas"]["canon"] or None))
    c, f, meta = mig("author_darin_jenks")
    out.append(K.page("author/darin-jenks/", "Darin Jenks", "Darin Jenks", "Swift Restoration and Remodeling, Ogden.", "Author", "Darin Jenks | Swift Restoration and Remodeling",
                      "Darin Jenks of Swift Restoration and Remodeling in Ogden writes about water damage, fire and mold restoration, insurance claims and remodeling in Northern Utah.",
                      c, image="darin-jenks", alt="Darin Jenks", canonical=EXT["author_darin_jenks"]["canon"] or None))
    for i, k in enumerate(["urban_air_trampoline_and_adventure_park", "the_hive_winery_and_brandy_company", "layton_city_vietnam_memorial_wall", "heritage_museum_of_layton", "ogden_nature_center", "mount_ogden",
                           "waterfall_canyon_trail", "ogden_s_george_s_eccles_dinosaur_park", "hill_aerospace_museum", "nordic_valley_ski_resort"]):
        c, f, meta = mig(k)
        out.append(local_page(k, path_of(k), c, f, i))
    return out


REMAP = {"cleaning/carpet-cleaning-ogden": "services/contents-cleaning", "contact-us": "contact", "hiring-a-mold-removal-company-after-water-damage": "restoration-tips/7-things-to-know-before-hiring-a-mold-remediation-company",
         "restoration-tips/6-ways-to-avoid-a-flooded-basement": "restoration-tips", "restoration-tips/how-to-clean-up-water-after-an-appliance-leak": "services/water-damage-restoration/appliance-leak",
         "restoration-tips/how-to-detect-water-damage-in-your-ogden-home-before-it-s-too-late": "restoration-tips", "restoration-tips/water-damage-insurance-claim": "restoration-tips/how-to-document-water-damage-for-insurance-claims-in-northern-utah",
         "service-areas/layton-ut": "service-areas/water-damage-layton-ut", "services/flood-damage-restoration": "services/flooded-basement-cleanup", "services/mold-removal": "services/ogden-mold-removal",
         "services/mold-removal/mold-growth-from-water-damage": "restoration-tips/mold-growth-from-water-damage", "services/reconstruction/choosing-the-right-flooring-for-your-basement-renovation": "restoration-tips/choosing-flooring-for-your-basement-renovation",
         "services/smoke-damage-repair": "services/fire-damage-restoration", "services/water-damage-restoration/the-difference-between-water-mitigation-and-water-restoration": "restoration-tips/the-difference-between-water-mitigation-and-water-restoration",
         "services/water-damage-restoration/water-damage-insurance-claim": "restoration-tips/how-to-document-water-damage-for-insurance-claims-in-northern-utah", "water-heater-burst": "restoration-tips/water-heater-burst"}


def remap(body):
    def fix(m):
        p = m.group(1).strip("/")
        return f'href="@/{REMAP[p]}/"' if p in REMAP else m.group(0)
    return re.sub(r'href="@/([^"#]*)"', fix, body)


def make_pages():
    tips, cards = tip_pages()
    cards.insert(0, (p_blog.POST[0], p_blog.POST[1], "fire-kitchen-rebuilt", "Oct 20, 2026"))
    tips.insert(0, p_blog.page(K, img))
    cases = case_pages()
    out = [home_v3.home(cards)] + svc_pages() + area_pages() + cases + tips + root_pages(cards, [k for k in EXT if k.startswith("case_studies_")]) + [K.notfound((("Water damage", "services/water-damage-restoration/"), ("Our work", "case-studies/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=remap(Q(x["body"]))), (" Call (385) 412-8633.", " 24/7 in Ogden.")) for x in out]
