"""Pages for the armour-crete.com redesign: "Sealed for the desert".

Armour Crete's own copy is the best explanation of concrete failure on any St. George site: the slab moves with a 100-degree
swing, drinks water and salt, and breaks from the inside. So the site draws it. References (screenshotted 20 Oct 2026): SUNDEK
(dark full-bleed dusk hero over decorative concrete), Euclid's Increte line (a catalog of finishes and colours), Layton
Construction (editorial serif headline, stat row). Signature: the sticky slab story (moves, drinks, breaks, sealed) and drawn
finish textures in place of photos the client doesn't have. Red rock and sandstone from Snow Canyon (openly licensed, credited).
Same URLs and canonicals (trailing slash). Home targets "concrete sealing st george" (report); every page names St. George.
"""
import html, json, os, re
from engine import img, crumbs_ld, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, EMAIL
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from illus import texture, slab, SERVICES
import home_v3, p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
STOP = ("Request an assessment", "Request an\nassessment")
SKIP = ("24h", "2yr", "hours", "years")
CREDITS = '<p class="credits">Landscape photos: Snow Canyon State Park by pkinney62 (<a href="https://creativecommons.org/licenses/by/2.0/" rel="noopener">CC BY 2.0</a>, Flickr); Color Country and Pine Valley Mountains, BLM Utah and U.S. Forest Service (public domain). Service drawings are original.</p>'
CITY_IMG = {"concrete_sealing_washington_ut": "snow-canyon-ridge", "concrete_sealing_hurricane_ut": "color-country", "concrete_sealing_ivins_ut": "snow-canyon-dunes", "concrete_sealing_santa_clara_ut": "snow-canyon-flats"}


def mig(k, skip=()):
    s = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x"))
    s = tidy(s, stop=STOP, skip=SKIP + tuple(skip))
    s = re.sub(r"<h3>\d+\s*(?:h|yr|hours|years)?</h3>", "", s)
    s = re.sub(r"<li>0\d\s*", "<li>", s)
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>(?:\s*<p>.*?</p>)?)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>(?:\s*<p>.*?</p>)?", "", s, flags=re.S)
    else: faqs = []
    return s.strip(), faqs


def svc_pages():
    out = []
    for p, lab, tex, short in SERVICES:
        k = p.strip("/").replace("-", "_")
        c, f = mig(k)
        t0 = html.unescape(EXT[k]["title"]).split(" | ")[0].strip()
        h1 = f"{lab} in St. George"
        t = f"{html.unescape(lab)} in St. George, UT | Armour Crete"
        if len(t) > 62: t = f"{html.unescape(lab)} St. George | Armour Crete"
        m = html.unescape(EXT[k]["meta"] or "")
        art = f'<div class="tex-hero">{texture(tex, "ph-" + tex)}<span>{html.unescape(lab)}</span></div>'
        out.append(K.page(p, lab, h1, short, "Service", t, m, c, art=art, intro=f"Armour Crete provides {html.unescape(lab).lower().replace('&', 'and')} in St. George and across Washington County, Utah. {short}",
                          crumbs=[("Services", "")], faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, html.unescape(lab), "St. George, UT")))
    return out


def city_pages():
    out = []
    for k, im in CITY_IMG.items():
        v = EXT[k]; p = v["url"].replace(U, "").replace("https://armour-crete.com/", "")
        p = (p.strip("/") + "/")
        t0 = html.unescape(v["title"]).split(" | ")[0].strip()
        c, f = mig(k, skip=(t0,))
        city = t0.replace("Concrete Sealing in ", "").replace(", UT", "")
        out.append(K.page(p, city, t0, "Driveways, patios, pool decks, expansion joints and foundation waterproofing.", "Service area", f"{t0} | Armour Crete"[:62], html.unescape(v["meta"]), c,
                          image=im, alt=f"Red rock landscape near {city}, Utah", crumbs=[("Service area", "")], faqs=f, canonical=v["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": t0, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "Place", "name": city + ", UT"}}]))
    return out


def other_pages():
    out = []
    for k, p, h1, lede, tag, t, art in [("products", "products/", "The Deco Sealers We Use", "Six Deco products, matched to the surface and the exposure it lives in.", "Products", "Deco Concrete Sealers We Use | St. George, UT | Armour Crete", "wetlook"),
                                        ("contractors", "contractors/", "Concrete Sealing for Contractors &amp; Builders", "Foundation waterproofing and flatwork sealing on your build calendar.", "For contractors", "Concrete Sealing for Builders in St. George | Armour Crete", "aggregate"),
                                        ("privacy", "privacy/", "Privacy Policy", None, "Legal", "Privacy Policy | Armour Crete", None),
                                        ("terms", "terms/", "Terms of Use", None, "Legal", "Terms of Use | Armour Crete", None)]:
        c, f = mig(k, skip=(h1,))
        a = f'<div class="tex-hero">{texture(art, "ph-o-" + art)}</div>' if art else None
        out.append(K.page(p, h1, h1, lede, tag, t, html.unescape(EXT[k]["meta"]), c, art=a, faqs=f, canonical=EXT[k]["canon"] or None))
    return out


def make_pages():
    out = [home_v3.home()] + svc_pages() + city_pages() + other_pages() + p_blog.pages(K, img) + [K.notfound((("Driveway sealing", "driveway-sealing/"), ("Products", "products/")))]
    pages = [K.fit(dict(x, body=Q(x["body"])), (" Free on-site assessment.", " Call 435-994-5235.")) for x in out]
    for pg in pages:
        if "hf-bg" in pg["body"] or "pf-bg" in pg["body"] or "qb-bg" in pg["body"]:
            pg["body"] += f'<div class="wrap">{CREDITS}</div>'
    return pages
