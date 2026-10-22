"""Pages for the poly-lift.com redesign: "Back to level".

Poly-Lift's specialty is polyurethane foam concrete lifting (their Deep Foamjection method), with push piers and helical piles
for foundations. The reviewer's note: make the foam specialty clear. So the site is built around the moment a sunken slab comes
back to level. References (screenshotted 20 Oct 2026): Hilti (industrial, product-led tiles, one hard accent colour), Magnum Piering
(their own pier supplier: engineering blue, tinted product photography), Ram Jack (dark, bold foundation-repair brand).
HMI (their foam maker) was behind a bot check; Alchatek showed a security wall.
Signature: the interactive lift on the home page (inject foam, the slab rises, the spirit-level bubble centers).
All 42 live URLs kept (trailing slash) with their own canonicals; one new blog post. Service and city pages name Logan in the
title, H1 and first paragraph (report)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, EMAIL, HOURS
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
FMAP = json.load(open(os.path.join(HERE, "fmap.json"), encoding="utf-8"))
META = json.load(open(os.path.join(HERE, "imgmeta.json"), encoding="utf-8"))
CLAIMS = re.compile(r"\bthe best\b|no one does it better|state-of-the-art|highly skilled|unlike other companies|top-of-the-line|superior service|year after year|on the market|the experts in|exponentially|leading durability", re.I)
STOP = ("Discover the Best Concrete or Foundation", "What People Are Saying About Us Online", "Get In Touch!", "Request a FREE Estimate", "Services Concrete Leveling")
CARD = re.compile(r"cost|need-to-be-sealed|piles-for-foundation-repair|homeowners-guide|how-effective|concrete-block-insulation$|why-do-foundation|magnumpiering", re.I)
SVCS = {"concrete_leveling_and_lifting": "Concrete Leveling &amp; Lifting", "concrete_sealing": "Concrete Sealing", "foundation_repair": "Foundation Repair",
        "foundation_repair_push_piering": "Push Piers", "foundation_repair_helical_piles": "Helical Piles", "injection_foam_insulation": "Core Foam Masonry Foam Insulation&reg;"}
POSTS = ["sinking_foundation_repair", "foundation_repair_cost", "concrete_block_insulation", "polyurethane_foam_concrete_lifting", "push_piers_homeowners_guide", "what_are_helical_piles", "does_concrete_need_to_be_sealed"]
CITY = [k for k in EXT if k.startswith(("concrete_contractors_", "concrete_contractor_", "foundation_repair_")) and k.endswith("_ut")]
DEFAULT = ["pl-poly-lift-crewman-injecting-deepfoam-into-concrete-walkway", "pl-lifted-garage-poly-lift-3", "pl-utah-university-piering-project-6", "pl-residential-poly-lift-jobs-2",
           "pl-raising-concrete-with-trailer-in-background-1150-ox8pj158xij", "pl-finished-driveway-with-concrete-sealant", "pl-piering-landscape"]


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def page_imgs(k):
    out = []
    for u in EXT[k]["imgs"]:
        f = u.split("?")[0].split("/")[-1]
        n = FMAP.get(f)
        if n and n in META and n not in out and not n.startswith("pl-logo"): out.append(n)
    return sorted(out, key=lambda n: bool(CARD.search(n)))


def mig(k, skip=()):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x"))
    raw = raw.replace("harsh Pacific Northwest seasons", "harsh winters").replace("Pacific Northwest", "Northern Utah")
    s = tidy(raw, claims=CLAIMS, stop=STOP, skip=skip)
    s = s.replace("&#39;", "&rsquo;")
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    return s.strip(), faqs


def strip_imgs(names):
    names = [n for n in names if not CARD.search(n)][:6]
    if len(names) < 2: return ""
    return '<h2>From our jobs</h2><div class="pstrip">' + "".join(f'<figure class="ps-f">{img(n, "")}</figure>' for n in names) + "</div>"


def title_of(k): return html.escape(html.unescape(EXT[k]["title"]))


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 110: m = fb
    return html.escape(m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "...")


def svc_pages():
    out = []
    for k, lab in SVCS.items():
        p = path_of(k); c, f = mig(k); ims = page_imgs(k) or DEFAULT[:1]
        h1 = f"{lab} in Logan, UT"
        lab_t = html.unescape(lab).replace("®", "")
        intro = f"Poly-Lift provides {lab_t.lower() if 'Core' not in lab else 'Core Foam Masonry Foam Insulation&reg;'} in Logan, across Cache Valley and in Davis County, from our Logan office. Call the Cache location at (435) 999-9309 or the Weber location at (801) 530-5617."
        t = f"{lab} in Logan, UT | Poly-Lift"
        if len(html.unescape(t)) > 62: t = f"{lab_t[:30]} in Logan, UT | Poly-Lift"
        crumbs = [("Foundation Repair", "foundation-repair/")] if k.startswith("foundation_repair_") else [("Services", "services/")]
        out.append(K.page(p, lab, h1, None, "Service", t, meta_of(k, f"{lab_t} in Logan, Utah from Poly-Lift. Free estimates."), c + strip_imgs(ims[1:]), image=ims[0], alt="",
                          intro=intro, crumbs=crumbs, faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, f"{lab_t} in Logan, UT", "Logan, UT")))
    return out


def city_pages():
    out = []
    for i, k in enumerate(CITY):
        p = path_of(k); c, f = mig(k); ims = page_imgs(k)
        ims = [n for n in ims if not CARD.search(n)] or [DEFAULT[i % len(DEFAULT)]]
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        place = re.sub(r"^.*? in ", "", t0).replace(", UT", "").strip()
        kind = "Foundation Repair &amp; Concrete Lifting" if k.startswith("foundation_repair_") else "Concrete Leveling &amp; Lifting"
        h1 = f"{kind} in {html.escape(place)}, UT"
        out.append(K.page(p, html.escape(place), h1, None, "Service area", title_of(k), meta_of(k, f"{html.unescape(kind)} in {place}, Utah from Poly-Lift, based in Logan."),
                          c + strip_imgs(ims[1:]), image=ims[0], alt="", crumbs=[("Service Areas", "service-areas/")], faqs=f, canonical=EXT[k]["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"{html.unescape(kind)} in {place}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "Place", "name": place + ", UT"}}]))
    return out


def post_pages():
    out, cards = [], []
    for i, k in enumerate(POSTS):
        p = path_of(k); c, f = mig(k); ims = page_imgs(k)
        hero = next((n for n in ims if not CARD.search(n)), DEFAULT[(i + 2) % len(DEFAULT)])
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        pg = K.page(p, html.escape(t0[:36]), html.escape(t0), f"From the {NAME} blog", "Blog", title_of(k), meta_of(k, f"{t0}: from the Poly-Lift blog, Logan, Utah."), c + strip_imgs([n for n in ims if n != hero]),
                    image=hero, alt="", crumbs=[("Blog", "blog/")], faqs=f, canonical=EXT[k]["canon"] or None, ogtype="article")
        pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
        pg["schema"].append({"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": t0, "image": U + f"assets/img/{hero}.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)})
        out.append(pg); cards.append((t0, p, hero))
    return out, cards


def gallery_projects():
    raw = open(os.path.join(HERE, "src", "pages", "completed_projects.html"), encoding="utf-8").read()
    cats = {"weber-state-university": "Weber State University", "utah-state-university": "Utah State University", "residential": "Residential", "lifted-garage": "Lifted Garage", "utah-stadium": "Utah Stadium"}
    items = re.findall(r'class="uabb-masonary-item ([a-z\-]+) uabb-photo-item".*?<img[^>]*src="([^"]+)"', raw, re.S)
    chips = '<button type="button" class="on" data-filter="all">All</button>' + "".join(f'<button type="button" data-filter="{c}">{l}</button>' for c, l in cats.items())
    grid = ""
    for c, u in items:
        n = FMAP.get(u.split("?")[0].split("/")[-1])
        if n and n in META: grid += f'<figure class="m-f" data-cat="{c}">{img(n, cats[c] + " project photo")}<figcaption>{cats[c]}</figcaption></figure>'
    body = f'''<p class="answer">Commercial and residential jobs from our own crews: piering under a Utah State University building and at the stadium, Weber State University, a garage lifted back to level, and driveways and walkways across Cache Valley.</p>
<div class="g-chips" role="group" aria-label="Filter projects">{chips}</div><div class="masonry" data-gallery>{grid}</div>'''
    return K.page("completed-projects/", "Completed Projects", "Completed Projects", "Foundation and concrete jobs, photographed by our crews.", "Our work", title_of("completed_projects"),
                  meta_of("completed_projects", "Completed foundation repair and concrete lifting projects by Poly-Lift: Utah State University, Weber State University, the Utah stadium, residential and a lifted garage."),
                  body, image="pl-utah-university-piering-project-6", alt="Push piers installed along a foundation wall at Utah State University", canonical=EXT["completed_projects"]["canon"] or None)


def photo_gallery():
    ims = [n for n in page_imgs("photo_gallery") if not CARD.search(n)]
    grid = "".join(f'<figure class="m-f">{img(n, "")}</figure>' for n in ims)
    return K.page("photo-gallery/", "Photo Gallery", "Photo Gallery", "Concrete lifting, sealing and foundation repair photos.", "Our work", title_of("photo_gallery"),
                  meta_of("photo_gallery", "Photos of Poly-Lift concrete lifting, concrete sealing and foundation repair jobs in Logan, Cache Valley and across Utah."),
                  f'<div class="masonry">{grid}</div><p><a class="tlink" href="@/completed-projects/">Completed projects {ARROW}</a></p>', image=ims[0] if ims else DEFAULT[1], alt="", canonical=EXT["photo_gallery"]["canon"] or None)


def faqs_page():
    raw = open(os.path.join(HERE, "src", "pages", "faqs.html"), encoding="utf-8").read()
    main = raw[raw.find("Frequently Asked Questions</h1>"):]
    blocks = re.split(r"<h2[^>]*>(.*?)</h2>", main, flags=re.S)
    body, allq = "", []
    for i in range(1, len(blocks) - 1, 2):
        head = txt(blocks[i]); seg = blocks[i + 1]
        qs = re.findall(r"<h4[^>]*>(.*?)</h4>(.*?)(?=<h4|$)", seg, re.S)
        qa = []
        for q, a in qs:
            at = txt(re.sub(r"<(script|style)[^>]*>.*?</\1>", "", a, flags=re.S))
            at = re.split(r"\s(?:Services Concrete Leveling|Discover the Best|What People Are Saying)", at)[0].strip()
            if at and len(at) < 900: qa.append((html.escape(txt(q)), html.escape(at)))
        if qa:
            body += f"<h2>{html.escape(head)}</h2>" + faq_html(qa, open_first=False); allq += qa
    pg = K.page("faqs/", "FAQs", "Frequently Asked Questions", "Concrete lifting, sealing, foundation lifting, push piers and helical piles.", "FAQs", title_of("faqs"),
                meta_of("faqs", "Answers to common questions about concrete lifting, concrete sealing, foundation lifting, push piers and helical piles from Poly-Lift in Logan, Utah."),
                body, image="pl-lifted-garage-poly-lift-4", alt="", canonical=EXT["faqs"]["canon"] or None)
    if allq: pg["schema"].append(faq_ld(allq))
    return pg


def contact_page():
    info = f'''<p class="answer">Two locations, one crew standard. Call the location nearest you, Monday to Friday, 7 a.m. to 5 p.m., or send the form for a free estimate.</p>
<div class="locs"><div class="loc"><span class="label">Cache location</span><a class="lp" href="tel:+14359999309">(435) 999-9309</a><a href="mailto:PolyLiftUtah@gmail.com">PolyLiftUtah@gmail.com</a></div>
<div class="loc"><span class="label">Weber location</span><a class="lp" href="tel:+18015305617">(801) 530-5617</a><a href="mailto:PolyLiftWeber@gmail.com">PolyLiftWeber@gmail.com</a></div></div>
<dl class="info"><div><dt>Address</dt><dd>715 W 1725 N<br>Logan, UT 84341</dd></div><div><dt>Hours</dt><dd>{HOURS}</dd></div></dl>'''
    return K.page("contact/", "Contact", "Contact Poly-Lift", "Free estimates for concrete lifting and foundation repair.", "Contact", title_of("contact"),
                  meta_of("contact", "Contact Poly-Lift in Logan, UT: Cache location (435) 999-9309, Weber location (801) 530-5617. Free estimates for concrete lifting and foundation repair."),
                  info, canonical=EXT["contact"]["canon"] or None, form_side=True)


def reviews_page():
    body = f'''<blockquote>&ldquo;Your satisfaction exemplifies the level of service and commitment we strive to deliver to all of our clients. Reviews not only help our online reputation, but they help others make a more informed decision about doing business with Poly-Lift.&rdquo;<footer>Clay Ogden, Poly-Lift</footer></blockquote>
<p>If we&rsquo;ve worked on your concrete or foundation, a review on Google helps your neighbors decide. Thank you.</p>
<p><a class="btn" href="https://www.google.com/search?q=Poly-Lift+Logan+UT+reviews" rel="noopener">Find us on Google {ARROW}</a></p>'''
    return K.page("reviews/", "Reviews", "Satisfaction Means More to Us Than a Job Well Done", None, "Reviews", title_of("reviews"),
                  meta_of("reviews", "Reviews and testimonials for Poly-Lift, concrete lifting and foundation repair in Logan, Utah. Leave us a review on Google."), body,
                  image="pl-residential-poly-lift-jobs-3", alt="", canonical=EXT["reviews"]["canon"] or None)


def generic(k, h1=None, tag="", image=None, extra=""):
    c, f = mig(k)
    t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
    return K.page(path_of(k), html.escape(t0[:36]), html.escape(h1 or t0), None, tag, title_of(k), meta_of(k, f"{t0}: Poly-Lift, concrete lifting and foundation repair in Logan, Utah."),
                  c + extra, image=image, alt="", faqs=f, canonical=EXT[k]["canon"] or None)


def make_pages():
    posts, cards = post_pages()
    cards.insert(0, (p_blog.POST[0], p_blog.POST[1], "pl-sidewalk-concrete-raised-before-and-after"))
    blog_cards = "".join(f'<a class="post-card" href="@/{p}">{img(im, "")}<b>{html.escape(t)}</b><em>Read {ARROW}</em></a>' for t, p, im in cards)
    blog = K.page("blog/", "Blog", "Blog", "Concrete lifting, foundation repair and sealing, explained.", "Blog", title_of("blog"),
                  meta_of("blog", "The Poly-Lift blog: concrete lifting, foundation repair, push piers, helical piles, concrete sealing and foam insulation, explained by a Logan, Utah contractor."),
                  f'<div class="posts">{blog_cards}</div>', canonical=EXT["blog"]["canon"] or None)
    cat = {"category_foundation_repair": ["sinking_foundation_repair", "foundation_repair_cost", "push_piers_homeowners_guide", "what_are_helical_piles"],
           "category_concrete_leveling_lifting": ["polyurethane_foam_concrete_lifting", "does_concrete_need_to_be_sealed"], "category_core_foam_masonry": ["concrete_block_insulation"]}
    cats = []
    for ck, ks in cat.items():
        lst = "".join(f'<a class="post-card" href="@/{path_of(k)}">{img(next(im for t, p, im in cards if p == path_of(k)), "")}<b>{html.escape(html.unescape(EXT[k]["title"]).split(" | ")[0])}</b><em>Read {ARROW}</em></a>' for k in ks)
        t0 = html.unescape(EXT[ck]["title"]).split(" | ")[0]
        cats.append(K.page(path_of(ck), html.escape(t0[:30]), html.escape(t0), "Articles from the Poly-Lift blog.", "Blog", title_of(ck), meta_of(ck, f"{t0}: articles from Poly-Lift in Logan, Utah."),
                           f'<div class="posts">{lst}</div>', crumbs=[("Blog", "blog/")], canonical=EXT[ck]["canon"] or None))
    roots = [generic("services", "Our Services", "Services", "pl-raising-concrete-with-trailer-in-background-1150-ox8pj158xij"),
             generic("service_areas", "Service Areas", "Service areas", "pl-poly-lift-trailer-by-uneven-concrete", '<ul class="chips">' + "".join(f'<li><a href="@/{path_of(k)}">{html.escape(re.sub(r"^.*? in ", "", html.unescape(EXT[k]["title"]).split(" | ")[0]).replace(", UT", ""))}</a></li>' for k in CITY) + "</ul>"),
             generic("video", "Videos", "Videos", "pl-foamgun2"), generic("foundation_repair_technical", "Technical Information", "Resources", "pl-magnum-steel-piering-opt"),
             generic("concrete_leveling_and_lifting_downloads", "Case Studies and Downloads", "Resources", "pl-3d-graphic-foamlift-scaled-1"),
             generic("ukraine_aid", "Ukraine Aid", "Community"), generic("privacy_policy", "Privacy Policy", "Legal"), generic("accessibility", "Accessibility Statement", "Legal"), generic("sitemap", "Sitemap", "Sitemap")]
    out = [home_v3.home(cards)] + svc_pages() + city_pages() + posts + [p_blog.page(K)] + [blog] + cats + [gallery_projects(), photo_gallery(), faqs_page(), contact_page(), reviews_page()] + roots + \
          [K.notfound((("Concrete lifting", "concrete-leveling-and-lifting/"), ("Foundation repair", "foundation-repair/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (435) 999-9309.", " Free estimates.")) for x in out]
