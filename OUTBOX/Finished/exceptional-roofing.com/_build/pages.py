"""Pages for the exceptional-roofing.com redesign: "Material specimen board".

Most roofers do shingles. Exceptional Roofing's own photos show copper roofs, hand-split cedar shake on historic-style homes,
standing seam metal on mountain homes, TPO, and architectural shingles, and their pages name the exact products (GAF Timberline
HDZ, CertainTeed Presidential TL, GAF Grand Sequoia, GAF EverGuard TPO, CMG Metals finishes). So the site is built like a
roofing sample board: original drawn swatches of each material with the products they use, their photos as a job file, and the
logo's green and slate with a copper accent. No address is shown (service-area business, per the report).
Same URLs and canonicals as the WordPress site (trailing slash). WordPress leftovers (/hello-world/, /sample-page/, the category
and author archives) are not rebuilt (see notes). Home targets "roofing company salt lake city" (report); service pages name Salt
Lake City in title, H1 and first paragraph.
Left out until confirmed: "For over 30 years ... multiple family run operations" (vague; not a company age), any "best" wording.
"""
import html, json, os, re
from engine import img, crumbs_ld, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, HOURS, EMAIL
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from illus import swatch, MATERIALS
import p_blog
from home_v3 import home

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
STOP = ("Need Quality Roofing Services", "Have a roofing project", "Need Roofing in")
SKIP = ("Get a Free Roofing Estimate", "Get a Free Quote", "Contact Us")
CLAIMS = re.compile(r"over 30 years|the best\b|#1|top[- ]rated", re.I)


def faqs_from(s):
    """Pull '<h3>Question?</h3><p>Answer</p>' pairs out of migrated text as FAQ items."""
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    return s.strip(), faqs


def mig(key, skip=()):
    s = migrate(HERE, key, DOMAIN, re.compile(r"(?!x)x"))
    s = s.replace("@/wb_exceptional-roofing.com/", "@/").replace("https://exceptional-roofing.com/wb_exceptional-roofing.com/", "https://exceptional-roofing.com/")
    s = re.sub(r'href="@/wb_exceptional-roofing\.com/?"', 'href="@/"', s)
    s = tidy(s, claims=CLAIMS, stop=STOP, skip=SKIP + tuple(skip))
    s = re.sub(r"<h3>Get a Free Roofing Estimate</h3>\s*<p>Tell us what you need.*?</p>", "", s, flags=re.S)
    s = re.sub(r"<p>Tell us what you need and Exceptional Roofing will follow up.*?</p>", "", s, flags=re.S)
    return faqs_from(s)


SVC = {"roof-repair/": ("Roof Repair", "copper-roof-crew", "Crew working on a copper and shingle roof"),
       "roof-replacement/": ("Roof Replacement", "shingle-drone", "Drone view of a finished shingle roof replacement"),
       "asphalt-roofing/": ("Asphalt Shingle Roofing", "shingle-mountain-home", "Mountain home with a new architectural shingle roof"),
       "metal-roofing/": ("Metal Roofing", "standing-seam-home", "Modern home with standing seam metal roof accents"),
       "flat-roofing/": ("Flat Roofing", "emergency-tarp", "Crew working on a flat roof membrane"),
       "tpo-roofing/": ("TPO Roofing", None, ""),
       "commercial-roofing/": ("Commercial Roofing", "metal-panel-worker", "Roofer carrying a metal panel above the Salt Lake Valley"),
       "commercial/": ("Commercial Roofing", "metal-panel-worker", "Roofer carrying a metal panel above the Salt Lake Valley"),
       "storm-damage-insurance-claims/": ("Storm Damage &amp; Insurance Claims", "emergency-tarp", "Emergency tarp being secured on a damaged roof"),
       "roof-inspections/": ("Roof Inspections", "shingle-aerial", "Aerial view of a residential shingle roof"),
       "emergency-roofing/": ("Emergency Roofing", "emergency-tarp", "Emergency roof tarp being installed"),
       "preventative-maintenance/": ("Preventative Roof Maintenance", "chimney-cap-after", "New chimney cap and flashing on a shingle roof"),
       "apartment-hoa-roofing/": ("Apartment &amp; HOA Roofing", None, ""),
       "retail-office-roofing/": ("Retail &amp; Office Roofing", None, "")}
LEDE = {"roof-repair/": "Leaks, flashing, storm damage, missing shingles, skylights and vents, on asphalt, metal and flat roofs.",
        "roof-replacement/": "Full tear-off, deck inspection, underlayment, flashing, installation, cleanup and a final inspection.",
        "asphalt-roofing/": "Architectural and designer shingles: GAF Timberline HDZ, CertainTeed Landmark and Presidential TL, GAF Grand Sequoia.",
        "metal-roofing/": "Standing seam, custom corrugated and copper, with CMG Metals colors and finishes.",
        "flat-roofing/": "Low-slope roofs for homes, additions, apartments and commercial buildings.",
        "tpo-roofing/": "TPO and PVC membranes, including GAF EverGuard TPO, for flat and low-slope roofs.",
        "commercial-roofing/": "Repair, replacement, TPO, maintenance and flat roofing for Utah businesses.",
        "commercial/": "Repair, replacement, TPO, maintenance and flat roofing for Utah businesses."}
INTRO = "Exceptional Roofing provides {s} in Salt Lake City and across the Salt Lake Valley, Park City and Heber, for homes and businesses."


CITY_IMG = [("shingle-mountain-home", "Mountain home with a new shingle roof"), ("standing-seam-home", "Standing seam metal roof"), ("wood-shake-home", "Wood shake roof"), ("shingle-drone", "Shingle roof from the drone"), ("metal-roof-project", "Metal and shingle mountain home"), ("winter-new-build", "New build in winter"), ("mountain-home-roof", "Mountain home roof"), ("cedar-shake-detail", "Cedar shake detail")]


def material_board(link=True, small=False):
    cards = "".join(f'<a class="spec reveal" href="@/{p}"><span class="sw">{swatch(k)}</span><span class="sp-k">No. {i + 1:02d}</span><b>{n}</b><span class="sp-p">{d}</span></a>' for i, (k, n, d, p) in enumerate(MATERIALS))
    return f'<div class="board{" small" if small else ""}">{cards}</div>'


HOME_FAQ = [("Do you provide free roofing estimates?", "Yes. Free quotes on any project, and most quotes are given the same day or week. Call or text 801-680-6499, or send the estimate form."),
            ("Should I repair or replace my roof?", "If the issue is limited to one area and the rest of the roof is serviceable, repair may be enough. Repeated leaks, widespread wear, storm damage in several areas, or aging materials usually point to replacement."),
            ("What roofing systems do you work on?", "Asphalt shingle, standing seam and corrugated metal, copper, wood shake and wood shingle, flat and low-slope, TPO and PVC, for homes and businesses."),
            ("Do you offer financing?", "Yes, through Acorn Finance. You can pre-qualify online and review payment options; approval, rates and terms are set by the lenders, not by us."),
            ("Do you work outside Salt Lake County?", "Our core area runs from Salt Lake City to Park City, Heber, Kamas and Santaquin. For the right project we also take work elsewhere in Utah, southern Idaho and southwest Wyoming.")]


def pages_main():
    out = []
    sv = [("Services", "services/")]
    for p, (lab, im, alt) in SVC.items():
        key = p.strip("/").replace("-", "_")
        c, f = mig(key, skip=(lab, html.unescape(lab)))
        h1 = f"{lab} in Salt Lake City"
        t = f"{lab} in Salt Lake City | Exceptional Roofing"
        if len(html.unescape(t)) > 62: t = f"{lab} Salt Lake City | Exceptional Roofing"
        m = html.unescape(EXT[key]["meta"] or "")
        if "Salt Lake" not in m: m = f"{html.unescape(lab)} in Salt Lake City from Exceptional Roofing: " + (LEDE.get(p, "repair, replacement and installation for homes and businesses.")[0].lower() + LEDE.get(p, "repair, replacement and installation for homes and businesses.")[1:])
        if len(m) > 160: m = m[:157].rsplit(" ", 1)[0] + "."
        art = None if im else f'<div class="board small one">{"".join(f"<span class=sw>{swatch(k)}</span>" for k in (["tpo"] if "tpo" in p or "retail" in p else ["asphalt", "metal"]))}</div>'
        canonical = canon("commercial-roofing/") if p == "commercial/" else (EXT[key]["canon"] or None)
        out.append(K.page(p, html.unescape(lab) if False else lab, h1, LEDE.get(p), "Service", t, m, c, image=im, alt=alt, art=art,
                          intro=INTRO.format(s=html.unescape(lab).lower().replace("&", "and")), crumbs=sv, faqs=f, canonical=canonical, sitemap=p != "commercial/",
                          schema=K.svc_schema(p, html.unescape(lab), "Salt Lake City, UT")))
    # city pages
    for key, v in EXT.items():
        if key in ("sandy", "murray", "draper", "holladay", "cottonwood_heights", "south_jordan", "west_jordan", "riverton", "park_city", "salt_lake_city_avenues", "kearns", "kamas", "oakley", "heber",
                   "emigration_canyon", "alpine", "alta", "santaquin"):
            city = html.unescape(v["title"]).split(" – ")[0].split(" – ")[0].replace("Salt Lake City / Avenues", "Salt Lake City & the Avenues").strip()
            p = v["url"].replace(U, "")
            c, f = mig(key, skip=(f"Roofing Services in {city}",))
            t = f"Roofing in {city}, UT | Exceptional Roofing"
            if len(t) > 62: t = f"Roofing {city} | Exceptional Roofing"
            m = f"Roofing in {city}, Utah: roof repair, replacement, asphalt, metal, wood shake, flat and commercial roofing from Exceptional Roofing. Free estimates."
            if len(m) > 160: m = f"Roofing in {city}, Utah: repair, replacement, asphalt, metal, shake, flat and commercial roofs from Exceptional Roofing. Free estimates."
            ci = CITY_IMG[sum(1 for o in out if o.get("_city")) % len(CITY_IMG)]
            out.append(K.page(p, city, f"Roofing in {city}, Utah", None, "Service area", t, m, c, image=ci[0], alt=ci[1],
                              crumbs=[("Service Areas", "service-areas/")], faqs=f, canonical=v["canon"] or None,
                              schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Roofing in {city}, Utah", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": city + ", UT"}}]))
            out[-1]["_city"] = True
    def simple(key, p, lab, h1, lede, tag, t, m, image=None, alt="", pre="", post="", form_side=False, crumbs=None, art=None, intro=""):
        c, f = mig(key, skip=(lab, h1))
        out.append(K.page(p, lab, h1, lede, tag, t, m, pre + c + post, image=image, alt=alt, art=art, crumbs=crumbs, faqs=f, form_side=form_side, canonical=EXT[key]["canon"] or None, intro=intro))
    simple("services", "services/", "Services", "Roofing Services in Salt Lake City", "Repair, replacement, every material, homes and businesses.", "Services",
           "Roofing Services in Salt Lake City | Exceptional Roofing", "Roofing services in Salt Lake City: repair, replacement, asphalt, metal, flat and TPO, commercial, storm damage, inspections, emergency and maintenance.",
           pre=material_board(small=True) + '<ul class="svc-index">' + "".join(f'<li><a href="@/{p}">{l}</a><span>{LEDE.get(p, "")}</span></li>' for p, l, ic in K.C.SVC) + "</ul>",
           intro="Exceptional Roofing offers roofing services in Salt Lake City, across the Salt Lake Valley and up to Park City and Heber, on every common roofing material.")
    simple("service_areas", "service-areas/", "Service Areas", "Roofing Service Areas in Utah", "Salt Lake Valley, Park City, Heber and the Wasatch Back.", "Service areas",
           "Roofing Service Areas | Exceptional Roofing, Salt Lake City", "Exceptional Roofing serves Salt Lake City, Sandy, Draper, Murray, Holladay, South Jordan, Park City, Heber, Kamas, Oakley, Alpine and more.",
           pre='<ul class="chips">' + "".join(f'<li><a href="@/{v["url"].replace(U, "")}">{html.unescape(v["title"]).split(" – ")[0]}</a></li>' for k2, v in EXT.items() if k2 in ("sandy", "murray", "draper", "holladay", "cottonwood_heights", "south_jordan", "west_jordan", "riverton", "park_city", "salt_lake_city_avenues", "kearns", "kamas", "oakley", "heber", "emigration_canyon", "alpine", "alta", "santaquin")) +
               f'</ul><p><a class="tlink" href="@/regional-service-area/">Regional projects: Utah, southern Idaho, southwest Wyoming {ARROW}</a></p>',
           intro="Exceptional Roofing is based in the Salt Lake Valley and serves homeowners, businesses, builders and property managers across the Wasatch Front and Wasatch Back.")
    simple("regional_service_area", "regional-service-area/", "Regional service area", "Regional Roofing: Utah, Southern Idaho &amp; Wyoming", "Larger and specialty roofs beyond the Salt Lake Valley.", "Service areas",
           "Regional Roofing Service Area | Exceptional Roofing, Utah", "For the right project, Exceptional Roofing reviews roofing work across Utah, southern Idaho and southwest Wyoming: replacements, metal, flat and specialty roofs.",
           crumbs=[("Service Areas", "service-areas/")])
    gal = [("copper-roof-crew", "Custom copper roof work"), ("wood-shake-historic", "Historic wood shake roofing"), ("cedar-shake-detail", "Cedar shake detail"), ("standing-seam-home", "Standing seam metal"),
           ("metal-roof-project", "Metal and asphalt mountain home"), ("metal-panel-worker", "Metal panel work, valley view"), ("shingle-drone", "Architectural shingles from the drone"), ("shingle-mountain-home", "Premium asphalt, custom home"),
           ("shingle-front", "Finished shingle roof, front view"), ("mountain-home-roof", "Mountain home roof"), ("winter-new-build", "New construction in winter"), ("emergency-tarp", "Emergency tarp"),
           ("chimney-cap-before", "Chimney cap, before"), ("chimney-cap-after", "Chimney cap, after"), ("shingle-aerial", "Residential shingle roof")]
    simple("gallery", "gallery/", "Gallery", "Roofing Gallery: Salt Lake City Projects", "Copper, shake, metal, shingle and flat roofs by our crew.", "Gallery",
           "Roofing Gallery | Exceptional Roofing, Salt Lake City Projects", "Photos of Exceptional Roofing projects in the Salt Lake area: custom copper, historic wood shake, standing seam metal, architectural shingles and more.",
           post='<div class="pgal">' + "".join(f"<figure>{img(n, c)}<figcaption>{c}</figcaption></figure>" for n, c in gal) + "</div>")
    simple("financing", "financing/", "Financing", "Roof Financing Through Acorn Finance", "Pre-qualify online and review payment options.", "Financing",
           "Roof Financing | Exceptional Roofing, Salt Lake City", "Roof financing for Salt Lake City projects through Acorn Finance: pre-qualify online for roof replacement, repair, storm damage, metal, flat and commercial roofing.")
    simple("about", "about/", "About", "About Exceptional Roofing", "A Salt Lake Valley roofing company. Roofing is our passion.", "About",
           "About Exceptional Roofing | Salt Lake Valley Roofers", "About Exceptional Roofing: a Salt Lake Valley roofer working from trailers and sheds to apartment complexes, mansions and business multiplexes, in every material.",
           image="metal-panel-worker", alt="Exceptional Roofing crew member carrying a metal panel")
    simple("faq", "faq/", "FAQ", "Roofing FAQ", "Repair, replacement, inspections, materials, timelines and estimates.", "FAQ",
           "Roofing FAQ | Exceptional Roofing, Salt Lake City", "Answers to common roofing questions from Exceptional Roofing in Salt Lake City: repair vs replacement, materials, inspections, timelines and free estimates.")
    simple("reviews", "reviews/", "Reviews", "Reviews", "What customers say about Exceptional Roofing.", "Reviews",
           "Reviews | Exceptional Roofing, Salt Lake City Roofing Company", "Exceptional Roofing has worked throughout Salt Lake City, Park City, Heber Valley, Farmington, Bountiful and the east bench. Read reviews and request a free quote.",
           post="<p>See our reviews on Google, and ask us for references from recent projects near you.</p>")
    simple("contact", "contact/", "Contact", "Contact Exceptional Roofing", "Free quotes on any project. Call, text, email or send the form.", "Contact",
           "Contact Exceptional Roofing | Free Roofing Estimates, SLC", "Contact Exceptional Roofing for a free roofing estimate in Salt Lake City: estimator 801-680-6499, production 801-809-8535, ExceptionalroofingUT@gmail.com.",
           pre=f'''<dl class="info"><div><dt>Estimator</dt><dd><a href="tel:{PHONES[0][2]}">{PHONES[0][1]}</a> (call or text)</dd></div><div><dt>Production</dt><dd><a href="tel:{PHONES[1][2]}">{PHONES[1][1]}</a></dd></div>
<div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div><div><dt>Best hours</dt><dd>Mon&ndash;Fri 6:30 AM&ndash;7:00 PM; Sat 9:00 AM&ndash;5:00 PM; Sun closed</dd></div></dl>''', form_side=True)
    return out


def make_pages():
    p_blog.setup(K, img)
    out = [home()] + pages_main() + p_blog.pages() + [K.notfound((("Services", "services/"), ("Gallery", "gallery/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.", " Call 801-680-6499.")) for x in out]
