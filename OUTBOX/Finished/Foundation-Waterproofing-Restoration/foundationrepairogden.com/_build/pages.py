"""Pages for the foundationrepairogden.com redesign: "Fortified".

The name is a fortification and the town is old Ogden: cut stone, iron and Weber clay. The client's own FAQ says heaving comes
from hard clay that "expands whenever it gets wet" like a dry sponge, and that heaving is often misdiagnosed as settlement, so
the signature (home_o.py) shows both: wet the clay and the floor heaves; switch to settlement and one side drops. References
(screenshotted 20 Oct 2026): Filson (heritage serif and condensed caps on warm canvas), Heath Ceramics (editorial serif, earthy
clay palette), Red Wing Heritage (plain-spoken craft). Everything is drawn: the live template's images are stock.
Source: Internet Archive (home Dec 2024, the other pages Sep 2020), same URLs (no trailing slash). The template's spun copy is
cleaned and its unverifiable claims dropped (CLAIMS)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, AREAS, PHONES, HOURS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import home_o
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"certified|licensed, insured|geotechnical|structural and|latest equipment|master of the craft|no other company|good reputation|24/7|day or night|"
                    r"guarantee|the best|#1|most professional|\$\s?\d|only hire|seasoned in the industry|we.ve unfortunately seen|national and local standards|permanent solution|years of experience|not insulated|skills, expertise", re.I)
STOPH = ("Services", "F.A.Q.", "Reviews", "Contact Us Today!", "Zips Codes", "Cities Near", "Business Hours", "City Facts", "Brands We Use")
TOWNS = [("foundation_repair_roy_weber_county", "Roy"), ("layton_84040_concrete_company", "Layton"), ("clearfield_foundation", "Clearfield"),
         ("foundation_kaysville_ut", "Kaysville"), ("foundation_experts_syracuse_utah", "Syracuse"), ("hooper_ut_foundationservice", "Hooper"),
         ("foundation_companies_hill_afb", "Hill AFB"), ("eden_ut_foundationservices", "Eden")]
SERVICES = ["Foundation repair", "Foundation cracks", "Basement waterproofing", "Emergency water removal", "Wall cracks", "Uneven floors", "Concrete",
            "Block foundations", "Flooded basements", "Foundation inspection", "Foundation forms"]
SENT = re.compile(r"(?<=[.!?])\s+")
CREDIT = f'<p class="v-credit">{home_o.CREDIT}</p>'


def path_of(k):
    p = EXT[k]["url"].replace(U, "")
    return p + "/" if p else ""


def blocks(k):
    """The template's article: every block after the H1 up to the template's service/FAQ/review furniture."""
    t = open(os.path.join(HERE, "src", "pages", k + ".html"), encoding="utf-8", errors="replace").read()
    t = re.sub(r"<(script|style).*?</\1>", "", t, flags=re.S)
    i = t.find("<h1")
    out = []
    for m in re.finditer(r"<(h2|h3|p)[^>]*>(.*?)</\1>", t[i:], re.S):
        x = " ".join(html.unescape(re.sub(r"<[^>]+>", " ", m.group(2))).split())
        if not x or len(x) < 3: continue
        if m.group(1) == "h2" and x in STOPH: break
        if x.startswith(("Serving all of Utah", "Call Today", "(385)")): break
        if m.group(1) == "h2" and x in ("Expert Foundation",): continue
        sents = [s for s in SENT.split(x) if not CLAIMS.search(s)]
        if not sents: continue
        x = " ".join(sents)
        tag = m.group(1) if m.group(1) != "h3" else "h3"
        out.append(f"<{tag}>{html.escape(x, quote=False)}</{tag}>")
    while out and out[-1].startswith("<h"): out.pop()
    return "\n".join(out)


def facts(town):
    sv = "".join(f"<li>{s}</li>" for s in SERVICES)
    near = "".join(f"<li>{a}</li>" for a in AREAS if a != town)
    return f'''<h2>What we work on</h2><ul class="cols">{sv}</ul>
<h2>Hours</h2><p>{HOURS}. Call <a href="tel:+13852132324">(385) 213-2324</a>.</p>
<h2>Nearby towns</h2><ul class="chips">{near}</ul>'''


def town_pages():
    out = []
    for i, (k, town) in enumerate(TOWNS):
        p = path_of(k)
        t0 = html.unescape(EXT[k]["title"]).split(" - ")[0].strip()
        h1 = f"Foundation repair &amp; waterproofing in {town}, UT"
        out.append(K.page(p, town, h1, f"Foundation repair, basement waterproofing and concrete in {town} &middot; (385) 213-2324", "Near Ogden",
                          html.escape(EXT[k]["title"]), f"Foundation repair, basement waterproofing, concrete and inspections in {town}, Utah, from Fortified Foundations. Call (385) 213-2324, 7 a.m. to 11 p.m.",
                          blocks(k) + facts(town) + CREDIT, image=("og-canyon-river", "og-canyon-road")[i % 2], alt="Ogden Canyon in a photograph from the 1870s (U.S. National Archives)", crumbs=[("Services", "services/")],
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Foundation repair in {town}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": town + ", UT"}}]))
    return out


def root_pages():
    sv = "".join(f"<li>{s}</li>" for s in SERVICES)
    towns = "".join(f'<li><a href="@/{path_of(k)}">{t}</a></li>' for k, t in TOWNS)
    services = K.page("services/", "Services", "Foundation, Concrete and Waterproofing Services", "In Ogden and nearby towns &middot; (385) 213-2324", "Services",
                      "Foundation Repair, Concrete &amp; Waterproofing Services | Ogden, UT",
                      "Fortified Foundations services in Ogden, UT: foundation repair, cracks, basement waterproofing, water removal, uneven floors, concrete and inspections.",
                      f'<p class="answer">Fortified Foundations works on foundations, basements and concrete in Ogden and the towns around it.</p><h2>What we work on</h2><ul class="cols">{sv}</ul><h2>By town</h2><ul class="chips">{towns}</ul>' + CREDIT,
                      image="og-canyon-road", alt="Ogden Canyon in a photograph from the 1870s (U.S. National Archives)")
    about = K.page("about/", "About", "About Fortified Foundations", "Foundation work in Ogden, Utah.", "About", "About Fortified Foundations | Foundation Repair in Ogden, UT",
                   "About Fortified Foundations: foundation repair, concrete and basement waterproofing in Ogden, Utah. Call (385) 213-2324 to have your foundation looked at.",
                   blocks("about") + CREDIT, image="og-hero", alt="The Wasatch Mountains above Ogden in a photograph from the 1870s (U.S. National Archives)")
    info = f'''{blocks("contact")}
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13852132324">(385) 213-2324</a></dd></div><div><dt>Hours</dt><dd>{HOURS}</dd></div>
<div><dt>Area</dt><dd>Ogden and nearby: {", ".join(AREAS[1:])}</dd></div></dl>'''
    contact = K.page("contact/", "Contact", "Contact Fortified Foundations", "Call (385) 213-2324 or send the form.", "Contact", "Contact Fortified Foundations | Ogden, UT Foundation Repair",
                     "Contact Fortified Foundations in Ogden, UT: call (385) 213-2324, every day from 7 a.m. to 11 p.m., or send the form for a free estimate on your foundation.",
                     info, form_side=True)
    opt = K.page("opt-out/", "Do not sell my info", "Do Not Sell My Info", "Privacy request.", "Privacy", "Do Not Sell My Info | Fortified Foundations",
                 "Ask Fortified Foundations not to sell or share your personal information. Send the form with your details and the request, or call (385) 213-2324.",
                 "<p>Use the form to ask us not to sell or share your personal information.</p>", form_side=True, robots="noindex, follow", sitemap=False)
    return [services, about, contact, opt]


def make_pages():
    out = [home_o.home()] + town_pages() + root_pages() + [p_blog.page(K)] + \
          [K.notfound((("Services", "services/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call (385) 213-2324.", " Free estimates.")) for x in out]
