"""Pages for the rhinofoundationsystems.com redesign: "Down to solid ground".

A rhino doesn't move, and neither should a foundation. Rhino's own pages explain how each soil type (clay, silt, sand, loam)
behaves under a house, and that helical piers anchor the foundation below the frost line. So the site is built as a section
through the ground: the home page's signature lets you drive a pier down through the soil until it bears, and the house levels.
References (screenshotted 20 Oct 2026): Rivian (oversized type on a quiet ground, one hero object), STIHL (one hard brand colour
over working photography), Carhartt (rugged, plain-spoken workwear). Brand: the black rhino logo and Rhino blue #1478A2.
Source: Internet Archive captures (Jul-Sep 2025) of all 30 sitemap and nav pages, same URLs and canonicals; three empty
service-area hub URLs from the sitemap are rebuilt as link hubs. Ad landing pages keep their URLs (noindex, out of the sitemap).
Unconfirmed claims are dropped (CLAIMS)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, EMAIL
from migrate import migrate
from tidy import tidy
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_r
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"40\+?|forty|four decades|since 1985|thousands of|hundreds of|5-star|five-star|certified|warrant|guarantee|no subcontractors|Utah.s leading|leading foundation|a leading|"
                    r"#1|best in|award|case study|the \w+ family|family (solves|avoided|noticed)|Roberts|we.ve seen it all|10 stars", re.I)
STOP = ("Lets Talk", "Let's Talk", "What They Say About Us", "Need help with a project")
BTN = re.compile(r"^(Get a FREE estimate|GET A FREE ESTIMATE|Call Now!?|Learn More|Contact Us|Call For Inspection|Get a Free Estimate)$", re.I)
WRONG = re.compile(r"^Crawl spaces are prone to moisture, mold, pests|^Here.s why encapsulation is essential", re.I)
SVC = [("foundation_repair", "Foundation repair", "brick-stair-crack"), ("helical_piers_push_piers", "Helical &amp; push piers", "helical-piers"),
       ("basement_waterproofing", "Basement waterproofing", "basement-waterproofing-install"), ("crawl_space_encapsulation", "Crawl space encapsulation", None),
       ("french_drains", "French drains", None), ("sump_pumps", "Sump pumps", None), ("commercial_foundation_repair", "Commercial foundation repair", "push-pier-install"),
       ("concrete_lifting", "Concrete lifting", "slab-lip-measured"), ("concrete_leveling", "Concrete leveling", "sidewalk-settled"),
       ("concrete_installation", "Concrete installation", None), ("vuba_stone", "Vuba Stone", None)]
LANDING = [("basement_landing", "Basement waterproofing"), ("concrete_repair_landing", "Concrete repair"), ("vuba_stone_landing", "Vuba Stone"), ("leveling_2", "Concrete leveling")]
CITY = [("service_area_foundation_repair_american_fork", "Foundation repair", "American Fork", "service-area/foundation-repair/"),
        ("service_area_foundation_repair_alpine", "Foundation repair", "Alpine", "service-area/foundation-repair/"),
        ("service_area_basement_waterproofing_american_fork", "Basement waterproofing", "American Fork", "service-area/basement-waterproofing/"),
        ("service_area_basement_waterproofing_basement_waterproofing_i_49f943", "Basement waterproofing", "Alpine", "service-area/basement-waterproofing/"),
        ("service_area_concrete_lifting_american_fork", "Concrete lifting", "American Fork", "service-area/concrete-lifting/"),
        ("service_area_concrete_lifting_alpine", "Concrete lifting", "Alpine", "service-area/concrete-lifting/"),
        ("service_area_concrete_repair_st_george", "Concrete repair", "St. George", "service-area/concrete-repair/")]
HUBS = [("service-area/foundation-repair/", "Foundation repair", "foundation-repair/"), ("service-area/basement-waterproofing/", "Basement waterproofing", "basement-waterproofing/"),
        ("service-area/concrete-lifting/", "Concrete lifting", "concrete-lifting/")]
ART = None  # set in make_pages (drawn soil strip from home_r)


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def listify(s):
    """Runs of two or more one-line <h3> items (the old site's icon lists) become a bulleted list."""
    def rep(m):
        items = re.findall(r"<h3>(.*?)</h3>", m.group(0))
        return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    return re.sub(r"(?:<h3>[^<]{2,70}</h3>\s*){2,}", rep, s)


def mig(k):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x"))
    raw = "\n".join(b for b in raw.split("\n") if not WRONG.search(re.sub(r"<[^>]+>", "", b)))
    raw = raw.replace("St. George", "St․George")
    s = tidy(raw, claims=CLAIMS, stop=STOP, skip=(NAME,)).replace("St․George", "St. George")
    s = re.sub(r"<p>\s*Get a FREE estimate\s*</p>", "", s, flags=re.I)
    s = listify(s)
    s = re.sub(r"<h2>[^<]*</h2>\s*(?=<h2>)", "", s)
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    s = re.sub(r"(?:<h[23]>[^<]*</h[23]>\s*)+$", "", s.strip())
    return s.strip(), faqs


def h1_of(k):
    t = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
    if t.startswith("Rhino Foundation System"): t = html.unescape(EXT[k]["title"]).split(" | ")[-1].strip()
    return t


def title_of(k):
    t = html.unescape(EXT[k]["title"]).strip()
    if "Rhino" not in t and len(t + " | Rhino Foundation Systems") <= 64: t += " | Rhino Foundation Systems"
    return html.escape(t)


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 110 or CLAIMS.search(m): m = fb
    return html.escape(m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "...")


def art(label):
    return f'<div class="art-card">{home_r.strip_art()}<span>{label}</span></div>'


def svc_pages():
    out = []
    for k, lab, im in SVC:
        p = path_of(k); c, f = mig(k)
        h = h1_of(k)
        out.append(K.page(p, lab, html.escape(h), "Free consultations and free estimates &middot; 801-509-5344", "Service", title_of(k),
                          meta_of(k, f"{html.unescape(lab)} from Rhino Foundation Systems in Salt Lake City and across Utah. Free consultations and estimates: call 801-509-5344."),
                          c, image=im, alt=f"{html.unescape(lab)} by Rhino Foundation Systems" if im else "", art=None if im else art(lab),
                          crumbs=[("Services", "services/")], faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, html.unescape(lab), "Utah")))
    return out


def landing_pages():
    out = []
    for k, lab in LANDING:
        p = path_of(k); c, f = mig(k)
        out.append(K.page(p, lab, html.escape(h1_of(k)), "Free estimates &middot; 801-509-5344", "Free estimate", title_of(k),
                          meta_of(k, f"{lab} from Rhino Foundation Systems in Utah. Tell us about the problem and get a free estimate, or call 801-509-5344."),
                          c, art=art(lab), faqs=f, canonical=EXT[k]["canon"] or None, form_side=True, robots="noindex, follow", sitemap=False))
    return out


def area_pages():
    out = []
    for k, svc, town, hub in CITY:
        p = path_of(k); c, f = mig(k)
        h = f"{svc} in {town}, UT"
        out.append(K.page(p, town, h, "Free consultations and free estimates &middot; 801-509-5344", "Service area", html.escape(f"{svc} in {town}, UT | Rhino Foundation Systems"),
                          meta_of(k, f"{svc} in {town}, Utah, from Rhino Foundation Systems: inspections, repairs and free estimates. Call 801-509-5344."), c,
                          art=art(town), crumbs=[("Service area", "service-area/"), (svc, hub)], faqs=f, canonical=EXT[k]["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"{svc} in {town}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": town + ", UT"}}]))
    for hp, svc, sp in HUBS:
        towns = [(town, path_of(k)) for k, s, town, hub in CITY if hub == hp]
        links = "".join(f'<li><a href="@/{tp}">{svc} in {t}, UT</a></li>' for t, tp in towns)
        body = f'''<p class="answer">{svc} pages for the towns Rhino Foundation Systems serves. For how the work is done, see the main <a href="@/{sp}">{svc.lower()}</a> page.</p>
<h2>Towns</h2><ul>{links}</ul><p><a class="tlink" href="@/service-area/">The full service area {ARROW}</a></p>'''
        out.append(K.page(hp, svc, f"{svc} by town", "Across Utah &middot; 801-509-5344", "Service area", html.escape(f"{svc} by Town in Utah | Rhino Foundation Systems"),
                          f"{svc} from Rhino Foundation Systems by town in Utah: American Fork, Alpine and more. Free consultations and estimates. Call 801-509-5344.",
                          body, art=art(svc), crumbs=[("Service area", "service-area/")]))
    k = "service_area_concrete_repair"; c, f = mig(k)
    c = (c or "") + '<ul><li><a href="@/service-area/concrete-repair/st-george/">Concrete repair in St. George, UT</a></li><li><a href="@/concrete-installation/">Concrete installation</a></li><li><a href="@/vuba-stone/">Vuba Stone overlays</a></li></ul>'
    out.append(K.page(path_of(k), "Concrete repair", "Concrete Repair", "Across Utah &middot; 801-509-5344", "Service area", title_of(k),
                      "Concrete repair from Rhino Foundation Systems in Utah, including St. George: crack repair, tear-out and replacement, resurfacing and overlays. Free estimates.",
                      c, art=art("Concrete repair"), crumbs=[("Service area", "service-area/")], canonical=EXT[k]["canon"] or None))
    for k, h, lab in (("service_area", "Service Area", "Service area"), ("location", "Foundation Repair Contractor in Salt Lake City, Utah", "Salt Lake City")):
        c, f = mig(k)
        if k == "service_area":
            c += "<h2>Pages by service and town</h2><ul>" + "".join(f'<li><a href="@/{hp}">{s} by town</a></li>' for hp, s, sp in HUBS) + '<li><a href="@/service-area/concrete-repair/">Concrete repair</a></li></ul>'
        out.append(K.page(path_of(k), lab, h, "Across Utah &middot; 801-509-5344", "Service area", title_of(k),
                          meta_of(k, f"Rhino Foundation Systems serves all of Utah: Salt Lake, Utah, Davis, Summit, Wasatch and Washington counties. Free estimates: 801-509-5344."),
                          c, image="rhino-truck" if k == "location" else None, alt="Rhino Foundation Systems truck at a job" if k == "location" else "", art=None if k == "location" else art(lab),
                          crumbs=[] if k == "service_area" else [("Service area", "service-area/")], faqs=f, canonical=EXT[k]["canon"] or None))
    return out


def root_pages():
    info = f'''<p class="answer">Call 801-509-5344 or send the form. Consultations and estimates are free.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+18015095344">801-509-5344</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Service area</dt><dd>All of Utah, from the Wasatch Front to St. George</dd></div></dl>'''
    out = [K.page("contact-us/", "Contact", "Contact Rhino Foundation Systems", "Questions, feedback or a free estimate.", "Contact", title_of("contact_us"),
                  "Contact Rhino Foundation Systems: call 801-509-5344 or email office@rhinofoundationsystems.com for foundation repair and waterproofing estimates in Utah.",
                  info, canonical=EXT["contact_us"]["canon"] or None, form_side=True)]
    c, f = mig("about_us")
    out.append(K.page("about-us/", "About", "About Rhino Foundation Systems", "Residential and commercial foundation repair across Utah.", "About", title_of("about_us"),
                      "About Rhino Foundation Systems: residential and commercial foundation repair, basement waterproofing and concrete work across Utah. Licensed and insured.",
                      c, image="rhino-truck", alt="A Rhino Foundation Systems truck", faqs=f, canonical=EXT["about_us"]["canon"] or None))
    c, f = mig("careers")
    out.append(K.page("careers/", "Careers", "Careers at Rhino Foundation Systems", "Join the crew.", "Careers", title_of("careers"),
                      "Careers at Rhino Foundation Systems: foundation repair, waterproofing and concrete jobs in Utah. Tell us about yourself and apply through the form.",
                      c, art=art("Careers"), canonical=EXT["careers"]["canon"] or None, form_side=True))
    grid = "".join(f'<li><a href="@/{path_of(k)}">{lab}</a></li>' for k, lab, im in SVC)
    c, f = mig("services")
    out.append(K.page("services/", "Services", "Foundation, Waterproofing and Concrete Services", "Everything under and around the house.", "Services", title_of("services"),
                      "Rhino Foundation Systems services: foundation repair, helical and push piers, basement waterproofing, crawl spaces, drains, sump pumps and concrete work in Utah.",
                      (c or "") + f"<h2>All services</h2><ul>{grid}</ul>", image="helical-piers", alt="Helical piers ready for installation", canonical=EXT["services"]["canon"] or None))
    return out


def make_pages():
    out = [home_r.home()] + svc_pages() + area_pages() + landing_pages() + root_pages() + [p_blog.page(K)] + \
          [K.notfound((("Foundation repair", "foundation-repair/"), ("Basement waterproofing", "basement-waterproofing/"), ("Contact", "contact-us/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 801-509-5344.", " Free estimates.")) for x in out]
