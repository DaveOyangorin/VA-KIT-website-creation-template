"""Pages for the cleartopsolutions.shop redesign: "Where's the water?".

ClearTop's 20 service pages are really a map of the house: the attic, the upstairs bathroom, the ceiling below it, the kitchen,
the basement, the crawl space. So the site is built around a blueprint cutaway of a house. On the home page you click the room
where the water is and get the right service; every service page shows the same house with its room lit. References
(screenshotted 20 Oct 2026): FirstOnsite (navy with a safety-orange urgent call bar, icon grid), Hippo (calm, home-centred
insurance site: plain words, soft cards), Flo (sky gradient with floating cards). Second signature: the 48-hour drying dial
(EPA: dry water-damaged areas within 24-48 hours to prevent mold).
All 30 live URLs kept (trailing slash) with their own canonicals (the live home page canonicalises to /st-george/: kept,
flagged). Service pages name St. George in title, H1 and first paragraph (report). Unverified claims left out (cfg)."""
import html, json, os, re
from engine import img, faq_html, faq_ld, canon
from cfg import U, NAME, HERE, DOMAIN, AREAS, PHONES, ST, EMAIL, HOURS
from migrate import migrate
from tidy import tidy, txt
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
from illus import house
import home_v3
import p_blog

header, footer, cta, side = K.header, K.footer, K.cta, K.side
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
CLAIMS = re.compile(r"98%|100\+|certified|state-of-the-art|cutting-edge|top-notch|years of experience|trusted name|highest level|latest technology|best in", re.I)
STOP = ("Talk To Us", "Ready when you are", "Reach Out Today", "Get in Touch with Us", "Visit Us")
DROP = re.compile(r"^(St\. George, UT|In [A-Z][\w. ]+, UT|Availability|Client Satisfaction|Request an Assessment|Licensed (&|&amp;) Insured|Request a Callback|.*★|Professional Planning|Clear Coordination|Reliable Results|"
                  r"What is Water Damage Restoration in|Simple, Fast|1\. Call Us|2\. Diagnosis|3\. Complete|Why [\w. ]+ Chooses ClearTop|Neighborhoods We Serve|Our Core Values|Who We Are$)", re.I)
DROPP = re.compile(r"^(24/7|98%|100\+|We deliver trusted .*|ClearTop Solutions is committed to restoring your peace of mind\.|Pick a reference point.*|Share your details.*|Protecting Your Home from Water Damage in .*|Comprehensive Solutions for .*|Browse every service .*)$")
CREDITS = {"summer-storm": ("Summer Storm", "A Guy Named Nyal", "CC BY-SA 2.0", "https://www.flickr.com/photos/189326381@N08/51386298981", "https://creativecommons.org/licenses/by-sa/2.0/"),
           "night-lightning": ("Thanks For The Shot Pops!", "A Guy Named Nyal", "CC BY-SA 2.0", "https://www.flickr.com/photos/189326381@N08/52379397605", "https://creativecommons.org/licenses/by-sa/2.0/"),
           "zion-storm": ("Zion Landscape", "Bernard Spragg", "public domain", "https://www.flickr.com/photos/88123769@N02/51386338695", "https://creativecommons.org/publicdomain/mark/1.0/"),
           "virgin-river": ("Virgin River in St. George", "Lindsey Winkel, USDA Forest Service", "public domain", "https://www.flickr.com/photos/107640324@N05/53190080585", "https://creativecommons.org/publicdomain/mark/1.0/"),
           "rain-window": ("Rain On Window", "rawpixel", "CC0", "https://www.rawpixel.com/image/5969935/rain-window", "https://creativecommons.org/publicdomain/zero/1.0/"),
           "rain-glass": ("Rain droplets window background", "rawpixel", "CC0", "https://www.rawpixel.com/image/3298420/free-photo-image-water-droplets-rain-texture", "https://creativecommons.org/publicdomain/zero/1.0/")}


def credit(*names):
    parts = [f'&ldquo;<a href="{CREDITS[n][3]}" rel="noopener">{CREDITS[n][0]}</a>&rdquo; by {CREDITS[n][1]} ({f"<a href=\"{CREDITS[n][4]}\" rel=\"noopener\">{CREDITS[n][2]}</a>"})' for n in names]
    return '<p class="credits">Background photos, for atmosphere only: ' + "; ".join(parts) + ".</p>"


# service key -> (zone in the cutaway, short label)
SVCZONE = {"services_water_extraction": "basement", "services_rapid_water_extraction": "basement", "services_water_extraction_company": "basement", "services_emergency_water_removal": "kitchen",
           "services_emergency_water_cleanup": "all", "services_24_hour_water_restoration_near_me": "all", "services_water_damage_restoration_near_me": "all", "services_water_cleanup_services": "all",
           "services_water_damage_mitigation": "all", "services_flood_restoration_services": "basement", "services_basement_flood_cleanup": "basement", "services_ceiling_water_damage_repair": "ceiling",
           "services_water_leak_restoration": "ceiling", "services_kitchen_water_damage_repair": "kitchen", "services_toilet_overflow_cleanup": "bath", "services_sewage_cleanup": "bath",
           "services_attic_mold_remediation": "attic", "services_crawl_space_mold_removal": "crawl", "services_mold_remediation_after_water_damage": "crawl", "services_water_damage_remediation_after_fire": "all"}
SVC_KEYS = [k for k in EXT if k.startswith("services_")]


def path_of(k):
    u = EXT[k]["url"]
    p = u.split(".shop/", 1)[1] if ".shop/" in u else ""
    return (p.strip("/") + "/") if p.strip("/") else ""


def label_of(k): return html.unescape(EXT[k]["title"]).split(" | ")[0].strip()


def summary(k):
    """The client's one-line definition of each service (from the services hub, falling back to the page's quick answer)."""
    hub = SUMS.get(label_of(k))
    return hub or ""


def drop_blocks(s):
    out, skip = [], False
    for b in re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s):
        t = txt(b)
        if b.startswith(("<h2>", "<h3>")):
            skip = bool(DROP.match(t))
            if skip: continue
        if skip or DROPP.match(t): continue
        if b.startswith("<ul>") and "Prompt response" in b: continue
        out.append(b)
    return "\n".join(out)


def mig(k):
    raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")).replace("&#39;", "&rsquo;")
    raw = re.sub(r'<a href="[^"]*email-protection[^"]*">(?:[^<]*</a>|</p>\s*<p>\[email(?:&#160;| )protected\]</p>)', f'<a href="mailto:{EMAIL}">{EMAIL}</a>.</p>', raw)
    raw = re.sub(r'<a href="[^"]*email-protection[^"]*">', "", raw).replace("[email&#160;protected]", EMAIL).replace("[email protected]", EMAIL)
    raw = re.sub(r"<h3>Our Services</h3>.*", "", raw, flags=re.S)
    s = drop_blocks(tidy(raw, claims=CLAIMS, stop=STOP))
    s = re.sub(r"<p><strong>Quick answer:</strong>\s*", '<p class="qa"><strong>Quick answer:</strong> ', s)
    s = s.replace("stress-included", "stress-free")
    faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
    else: faqs = []
    while re.search(r"<h3>[^<]*</h3>\s*$", s): s = re.sub(r"<h3>[^<]*</h3>\s*$", "", s)
    return s.strip(), faqs


SUMS = {}
_hub = tidy(migrate(HERE, "services", DOMAIN, re.compile(r"(?!x)x")))
for t, d in re.findall(r"<h3>(?:<a [^>]*>)?([^<]+)(?:</a>)?</h3>\s*<p>(.*?)</p>", _hub):
    d = d.replace("&#39;", "&rsquo;").strip()
    if d.endswith("..."):
        d = d[:-3].rsplit(" ", 1)[0].rstrip(",")
        d = re.sub(r"\s+(in|of|to|and|the|a|for|from|with|thoro\w*|cruci\w*)$", "", d)
        d = re.sub(r"\s+(in|of|to|and|the|a|for|from|with)$", "", d) + "."
    d = re.sub(r",?\s+ensuring(?: a safe)?\.$", ".", d).replace("located in St..", "located in St. George.")
    SUMS[html.unescape(t).strip()] = d


def svc_cards(exclude=None, limit=None):
    keys = [k for k in SVC_KEYS if k != exclude][:limit]
    return '<div class="svc-cards">' + "".join(f'<a class="svc-card" href="@/{path_of(k)}" data-z="{SVCZONE[k]}"><span class="sz">{SVCZONE[k] if SVCZONE[k] != "all" else "whole home"}</span><b>{html.escape(label_of(k))}</b><em>{ARROW}</em></a>' for k in keys) + "</div>"


def svc_pages():
    out = []
    for k in SVC_KEYS:
        p = path_of(k); lab = label_of(k); c, f = mig(k)
        lab_h = html.escape(lab)
        h1 = f"{lab_h} in St. George, UT"
        intro = f"ClearTop Solutions provides {lab_h.lower().replace('near me', 'in St. George')} in St. George, Washington, Santa Clara and Ivins, with a 24/7 emergency line at {ST['phone']}."
        intro = intro.replace("in St. George in St. George", "in St. George")
        t = f"{lab_h} in St. George, UT | ClearTop Solutions"
        if len(html.unescape(t)) > 60: t = f"{lab_h} in St. George, UT | ClearTop"
        if len(html.unescape(t)) > 60: t = f"{lab_h} | St. George, UT"
        sm = html.unescape(re.sub(r"<[^>]+>", "", summary(k)))
        m = f"{lab} in St. George, UT: {sm[0].lower() + sm[1:] if sm else ''}"
        if len(m) > 150: m = m[:147].rsplit(" ", 1)[0].rstrip(",") + "."
        body = c + f'<h2>Related services</h2>{svc_cards(exclude=k, limit=6)}'
        out.append(K.page(p, lab_h, h1, "24/7 emergency line &middot; St. George, Washington, Santa Clara, Ivins", "Service", t, html.escape(m), body, art=house(SVCZONE[k], uid="p" + str(len(out))),
                          intro=intro, crumbs=[("Services", "services/")], faqs=f, canonical=EXT[k]["canon"] or None, schema=K.svc_schema(p, f"{lab} in St. George, UT", "St. George, UT")))
    return out


CITYIMG = {"st_george": "virgin-river", "washington": "summer-storm", "santa_clara": "zion-storm", "ivins": "rain-glass"}


def city_pages():
    out = []
    for k, img_ in CITYIMG.items():
        city = {"st_george": "St. George", "washington": "Washington", "santa_clara": "Santa Clara", "ivins": "Ivins"}[k]
        raw = migrate(HERE, k, DOMAIN, re.compile(r"(?!x)x")).replace("&#39;", "&rsquo;")
        hoods = []
        m = re.search(r"<h3>Neighborhoods We Serve</h3>(.*?)<h3>(?:Reliable|Expert)", raw, re.S)
        if m: hoods = [h for h in re.findall(r"<h3>([^<]+)</h3>", m.group(1))]
        raw = re.sub(r"<h3>Neighborhoods We Serve</h3>.*?(?=<h3>(?:Reliable|Expert))", "", raw, flags=re.S)
        raw = re.sub(r"<h3>Why [\w. ]+ Chooses ClearTop.*", "", raw, flags=re.S)
        s = drop_blocks(tidy(raw, claims=CLAIMS, stop=STOP))
        faqs = [(q, a) for q, a in re.findall(r"<h3>([^<]{8,160}\?)</h3>\s*(<p>.*?</p>)", s, re.S)]
        if len(faqs) >= 2: s = re.sub(r"<h3>[^<]{8,160}\?</h3>\s*<p>.*?</p>", "", s, flags=re.S)
        else: faqs = []
        chips = ('<h2>Places we know in ' + city + '</h2><ul class="chips hoods">' + "".join(f"<li>{h}</li>" for h in hoods) + "</ul>") if hoods else ""
        body = s + chips + f"<h2>Services in {city}</h2>" + svc_cards() + credit(img_)
        p = path_of(k)
        h1 = f"Water Damage Restoration in {city}, UT"
        out.append(K.page(p, city, h1, "24/7 emergency line &middot; (435) 288-1334", "Service area", f"Water Damage Restoration {city}, UT | ClearTop"[:60],
                          html.escape(f"Water damage restoration in {city}, Utah from ClearTop Solutions: extraction, drying, mold, sewage and leak repair, with a 24/7 emergency line."),
                          body, image=img_, alt="", crumbs=[] if k == "st_george" else [("St. George", "st-george/")], faqs=faqs, canonical=EXT[k]["canon"] or None,
                          schema=[{"@type": "Service", "@id": canon(p) + "#service", "name": f"Water damage restoration in {city}, UT", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": city + ", UT"}}]))
    return out


def services_hub():
    groups = [("Where it starts", ["attic", "bath", "ceiling", "kitchen", "basement", "crawl"]), ("Anywhere in the home", ["all"])]
    zl = {"attic": "Attic", "bath": "Bathroom", "ceiling": "Ceilings &amp; leaks", "kitchen": "Kitchen", "basement": "Basement &amp; extraction", "crawl": "Crawl space &amp; mold", "all": "Whole-home water, drying &amp; mitigation"}
    blocks = ""
    for z in ["basement", "bath", "ceiling", "kitchen", "attic", "crawl", "all"]:
        ks = [k for k in SVC_KEYS if SVCZONE[k] == z]
        items = "".join(f'<li><a href="@/{path_of(k)}"><b>{html.escape(label_of(k))}</b><span>{summary(k)}</span></a></li>' for k in ks)
        blocks += f'<div class="hub-z"><div class="hz-art">{house(z, uid="hz" + z, crop=z != "all")}</div><div><h2>{zl[z]}</h2><ul class="hub-list">{items}</ul></div></div>'
    body = f'<p class="answer">Every service ClearTop Solutions provides in St. George, UT, grouped by where the water is. Not sure which one you need? Call the 24/7 line at <a href="tel:{ST["tel"]}">{ST["phone"]}</a> and describe what you see.</p>' + blocks
    return K.page("services/", "Services", "Water Damage Services in St. George", "Grouped by where the water is.", "Services", "Water Damage Services in St. George, UT | ClearTop",
                  "Every water damage service ClearTop Solutions provides in St. George, UT: extraction, flood and basement cleanup, leaks, ceilings, kitchens, sewage and mold.",
                  body, art=house(None, uid="hub"), canonical=EXT["services"]["canon"] or None)


def about():
    c, f = mig("about")
    c = re.sub(r"<h3>(Integrity|Professionalism|Customer-Centric Approach|Quality Assurance)</h3>", "", c)
    vals = '<h2>What we hold to</h2><ul class="ticks"><li>Integrity</li><li>Professionalism</li><li>A customer-centric approach</li><li>Quality assurance</li></ul>'
    return K.page("about/", "About", "About ClearTop Solutions", "Water damage restoration for St. George homes and businesses.", "About", "About ClearTop Solutions | Water Damage, St. George UT",
                  "About ClearTop Solutions: water damage restoration for homes and businesses in St. George, Utah, with a 24/7 emergency line and clear communication throughout.",
                  c + vals + credit("rain-window"), image="rain-window", alt="", canonical=EXT["about"]["canon"] or None)


def contact():
    info = f'''<p class="answer">If you are facing water damage, call the 24/7 emergency line at <a href="tel:{ST["tel"]}">{ST["phone"]}</a>, or send your details and the team will follow up with clear next steps.</p>
<dl class="info"><div><dt>24/7 emergency line</dt><dd><a href="tel:{ST["tel"]}">{ST["phone"]}</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Office</dt><dd>{ST["street"]}<br>St. George, UT {ST["zip"]}</dd></div><div><dt>Serving</dt><dd>St. George, Washington, Santa Clara, Ivins</dd></div></dl>
<h2>What happens when you call</h2><ul class="ticks"><li><b>Quick response.</b> We aim to arrive as soon as possible to assess the situation.</li><li><b>Open communication.</b> We keep you informed about each step, so you know what to expect.</li><li><b>Coordination.</b> We coordinate with insurance companies and other parties to streamline the process.</li></ul>
<p><a class="tlink" href="https://www.google.com/maps/search/?api=1&amp;query=ClearTop+Solutions+2505+S+River+Rd+St.+George+UT" rel="noopener">Find us on the map {ARROW}</a></p>'''
    pg = K.page("contact/", "Contact", "Contact ClearTop Solutions", "24/7 emergency line for water damage in St. George.", "Contact", "Contact ClearTop Solutions | 24/7 Water Damage, St. George",
                "Contact ClearTop Solutions in St. George, UT: 24/7 emergency line (435) 288-1334, info@cleartopsolutions.shop, 2505 S River Road, Ste 2.", info,
                canonical=EXT["contact"]["canon"] or None, form_side=True)
    pg["body"] = pg["body"].replace("How can we help?", "What happened? (optional)")
    return pg


def legal(k, h1, t, m):
    c, f = mig(k)
    return K.page(path_of(k), h1, h1, None, "Legal", t, m, c, canonical=EXT[k]["canon"] or None)


def make_pages():
    out = [home_v3.home()] + svc_pages() + city_pages() + [services_hub(), about(), contact(),
           legal("privacy_policy", "Privacy Policy", "Privacy Policy | ClearTop Solutions, St. George UT", "The privacy policy for cleartopsolutions.shop: what ClearTop Solutions collects through its forms and website, how it is used, and your choices."),
           legal("terms_and_conditions", "Terms and Conditions", "Terms and Conditions | ClearTop Solutions", "The terms and conditions for cleartopsolutions.shop, the website of ClearTop Solutions, water damage restoration in St. George, Utah.")] + \
          p_blog.pages(K) + [K.notfound((("Services", "services/"), ("St. George", "st-george/"), ("Contact", "contact/")))]
    return [K.fit(dict(x, body=Q(x["body"])), (" 24/7: (435) 288-1334.", " Call 24/7.")) for x in out]
