"""Pages for the stgeorgeconcreteleveling.com redesign: "Measure the lip".

The question every visitor has is "is this bad enough to fix?". The 2010 ADA Standards answer it in fractions of an inch, and
the client's own text cites them. So the site is built around a measurement: the home page gauge lets you set a lip height and
reads back the rule it falls under. Everything else is drawn (the live site has no photos of its own). References (screenshotted
20 Oct 2026): Stripe Press and Linear for precise, instrument-like typography; Hilti for one hard accent on a quiet ground.
All 63 live pages kept (trailing slash) with their own canonicals; one new blog post. Unverified claims and the customer
anecdotes written into the pages are left out (cfg)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, HOURS
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from illus import surface
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
EXT = {k: v for k, v in EXT.items() if not k.startswith("favicon")}
CLAIMS = re.compile(r"thousands of|family.owned|15\+|\d+\+? years|years serving|years in business|certified|S260|warranty|guarantee|Example:|client had|customer had|homeowner had|we recently|last (month|year|summer|spring)|backed by|award|best in|#1", re.I)
STOP = ("Get a Fast, Free Leveling Quote", "Get a Quote (it's free!)", "Ready When You Are", "Contact Information")
SKIP = ("St. George Concrete Leveling",)
SURFACE = {"driveway": "driveway", "sidewalk": "sidewalk", "patio": "patio", "garage": "garage", "warehouse": "garage", "pool": "pool", "step": "steps", "porch": "porch"}
SVCKEYS = ["polyurethane_foam_injection", "mudjacking_services", "driveway_leveling", "sidewalk_leveling", "patio_leveling", "garage_floor_leveling", "pool_deck_leveling", "concrete_slab_lifting",
           "foundation_slab_leveling", "concrete_settlement_repair", "sunken_concrete_repair", "trip_hazard_removal", "concrete_void_filling", "soil_stabilization_for_concrete_slabs",
           "concrete_crack_repair", "concrete_resurfacing", "concrete_joint_repair", "commercial_concrete_leveling", "warehouse_floor_leveling", "hoa_community_concrete_repairs",
           "concrete_step_leveling", "porch_entryway_leveling", "retaining_wall_stabilization"]
ROOT = ["contact", "thank_you", "terms", "privacy"]


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".com/", 1)[1] if ".com/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def surf_of(k):
    for key, s in SURFACE.items():
        if key in k: return s
    return "slab"


def mig(k):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")).replace("&#39;", "&rsquo;").replace("St. George", "St․George")
    s = tidy(raw, claims=CLAIMS, stop=STOP, skip=SKIP).replace("St․George", "St. George")
    s = re.sub(r"<ul>(?:<li>(?:Licensed and insured|Always FREE Quotes)</li>)+</ul>", "", s)
    s = re.sub(r"<ul></ul>", "", s)
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    while re.search(r"<h3>[^<]*</h3>\s*$", s): s = re.sub(r"<h3>[^<]*</h3>\s*$", "", s)
    return s.strip(), faqs


def title_of(k): return html.escape(html.unescape(EXT[k]["title"]))


def meta_of(k, fb):
    m = html.unescape(EXT[k]["meta"] or "").strip()
    if len(m) < 110 or CLAIMS.search(m): m = fb
    return html.escape(m if len(m) <= 160 else m[:157].rsplit(" ", 1)[0] + "...")


def svc_pages():
    out = []
    for k in SVCKEYS:
        if k not in EXT: continue
        p = path_of(k); c, f = mig(k)
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        lab = re.sub(r"\s*St\. George,? UT$", "", t0).strip()
        h1 = f"{html.escape(lab)} in St. George, UT"
        out.append(K.page(p, html.escape(lab[:36]), h1, "Free on-site estimate &middot; 435-466-5545", "Service", title_of(k),
                          meta_of(k, f"{lab} in St. George, UT: polyurethane foam lifting for sunken concrete. Free on-site estimate and written proposal. Call 435-466-5545."),
                          c, art=f'<div class="art-card">{surface(surf_of(k))}<span>{html.escape(lab)}</span></div>', crumbs=[("Services", "concrete-slab-lifting/")] if k != "concrete_slab_lifting" else [],
                          faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, f"{lab} in St. George, UT", "St. George, UT")))
    return out


def area_pages():
    out = []
    for k in [k for k in EXT if k not in SVCKEYS and k not in ROOT and k != "home"]:
        p = path_of(k); c, f = mig(k)
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        place = re.sub(r"^Concrete Leveling\s*(in)?\s*", "", t0).replace(", UT", "").strip() or t0
        county = "county" in k
        out.append(K.page(p, html.escape(place[:36]), html.escape(t0), "Free on-site estimate &middot; 435-466-5545", "Service area", title_of(k),
                          meta_of(k, f"Concrete leveling in {place}, Utah: polyurethane foam lifting for driveways, sidewalks, patios and pool decks. Free estimate: 435-466-5545."),
                          c, art=f'<div class="art-card">{surface("sidewalk")}<span>{html.escape(place)}</span></div>', crumbs=[] if county else [("Washington County", "washington-county/")],
                          faqs=f, canonical=EXT[k]["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Concrete leveling in {place}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "Place", "name": place + ", UT"}}]))
    return out


def root_pages():
    info = f'''<p class="answer">Call 435-466-5545, Monday to Friday, 8 a.m. to 5 p.m., or send the form for a free quote.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+14354665545">435-466-5545</a></dd></div><div><dt>Address</dt><dd>169 W 2710 S Cir Suite 202-A<br>St. George, UT 84790</dd></div>
<div><dt>Service area</dt><dd>St. George &amp; Southern Utah</dd></div><div><dt>Hours</dt><dd>{HOURS}</dd></div></dl>'''
    contact = K.page("contact/", "Contact", "Contact St. George Concrete Leveling", "Free quotes for concrete leveling in Southern Utah.", "Contact", title_of("contact"),
                     "Contact St. George Concrete Leveling: 435-466-5545, 169 W 2710 S Cir Suite 202-A, St. George, UT 84790. Monday to Friday, 8 a.m. to 5 p.m. Free quotes.",
                     info, canonical=EXT["contact"]["canon"] or None, form_side=True)
    thanks = K.page("thank-you/", "Thank you", "Thank you", "We&rsquo;ll be in touch soon.", "Contact", title_of("thank_you"), "Thank you for contacting St. George Concrete Leveling. We&rsquo;ll be in touch soon. For anything urgent, call 435-466-5545, Monday to Friday.",
                    f'<p>Your request was sent. If it&rsquo;s urgent, call <a href="tel:+14354665545">435-466-5545</a>.</p><p><a class="tlink" href="@/">Back to home {ARROW}</a></p>', canonical=EXT["thank_you"]["canon"] or None, robots="noindex, follow", sitemap=False)
    legal = []
    for k, h in (("terms", "Terms"), ("privacy", "Privacy Policy")):
        c, f = mig(k)
        legal.append(K.page(path_of(k), h, h, None, "Legal", title_of(k), meta_of(k, f"{h} for stgeorgeconcreteleveling.com, the website of St. George Concrete Leveling in St. George, Utah. How the site and its forms work."), c, canonical=EXT[k]["canon"] or None))
    return [contact, thanks] + legal


def make_pages():
    out = [home_v3.home()] + svc_pages() + area_pages() + root_pages() + [p_blog.page(K)] + \
          [K.notfound((("Driveway leveling", "driveway-leveling/"), ("Trip hazard removal", "trip-hazard-removal/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 435-466-5545.", " Free estimates.")) for x in out]
