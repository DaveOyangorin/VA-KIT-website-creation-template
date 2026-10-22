"""Pages for the davenportfoundationrepair.com redesign: "Below grade".

Foundation repair happens where nobody looks, so the site draws it: every section of the site has an original engineer's
cross-section (grade line, soil layers, depth in feet, the house wall and footing, and the repair: push piers, wall anchors,
interior drainage, crawl space jacks and liner, slab lifting, helical piles). The home page opens on a whole-house section with
five numbered problem spots. Paired with that is the client's own job file: their phone photos from real Utah towns (Grantsville,
Morgan, Lehi, Vernal, Ogden, Draper...), captioned as they captioned them. Davenport yellow and near-black from the logo, drafting
paper, soil ochres. Manufacturer network photos are not used.
All 217 URLs are kept exactly (".html" pages), including the 100 blog posts and blog pagination; canonicals copied from the live
site (three pages point to another page and stay out of the sitemap). Home targets "foundation repair west jordan"; section and
service pages name West Jordan in title, H1 and opening paragraph.
"""
import html, json, os, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, U, HERE, DOMAIN, CITIES
from migrate import migrate
from illus import section, hero, SPOTS
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
EST = "free-estimate.html"
HOME = ("Home", "")
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
DROP = re.compile(r"click each photo|photo to enlarge|below are (?:images|photos|pictures)|images below|\bbest\b|#1|100% customer|600 employees|largest|lifetime|guarantee|top-rated|number one|Get a FREE Quote|Get Your Get|^Free .{0,40} Quote$|"
                  r"Request a FREE|Looking for a price\?|Related Pages:|View Review|View Company|Read Full Article|Click here", re.I)
CTA_P = re.compile(r"^(Get|Schedule|Book|Call|Contact|Request|Learn|See|View|Find|Click|Read)\b[^.]{0,60}!?$", re.I)


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def path_of(k):
    u = EXT[k]["url"]
    return re.sub(r"^https?://(www\.)?davenportfoundationrepair\.com/?", "", u)


KNOWN, REMAP, CANON_FIX = set(), {}, []


def remap(m):
    """Links to live pages that are not rebuilt (CMS item pages: single reviews, photos, before/after items) point to the
    nearest parent page that is; every remapped URL is recorded for the redirect list in the notes."""
    p = m.group(1)
    if not KNOWN or p in KNOWN or not p.endswith(".html"): return f'href="@/{p}"'
    parts = p[:-5].split("/")
    while len(parts) > 1:
        parts = parts[:-1]
        cand = "/".join(parts) + ".html"
        if cand in KNOWN:
            REMAP[p] = cand
            return f'href="@/{cand}"'
    REMAP[p] = ""
    return 'href="@/"'


def tidy(s):
    s = re.sub(r'(href="@/[^"]+\.html)/"', r'\1"', s)
    s = s.replace('href="@/free-estimate.html/"', 'href="@/free-estimate.html"')
    s = re.sub(r'href="/core/pdf/([^"]+)"', r'href="@root/core/pdf/\1"', s)  # spec PDFs are copied into the site
    s = re.sub(r'href="/(?!/)([^"]*)"', r'href="@/\1"', s)
    s = re.sub(r'href="@/([^"#]*)"', remap, s)
    out = []
    for blk in re.findall(r"<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s, re.S):
        txt = html.unescape(re.sub(r"<[^>]+>", "", blk)).strip()
        if not txt or txt in ("&nbsp;", "\xa0", "Categories:"): continue
        if blk.startswith("<p>") and CTA_P.match(txt): continue
        if "directory[" in blk or "' + " in blk: continue  # leftover script templates on opinion.html
        blk = re.sub(r'<a href="@/[^"]*\.(?:jpe?g|png|webp)[^"]*">(.*?)</a>', r"\1", blk)
        blk = re.sub(r'title="[^"]*">', "", blk)
        out.append(blk)
    def minor(b): return b.startswith("<h3>") or re.fullmatch(r"<p><strong>[^<]{0,70}</strong></p>", b) is not None
    def head(b): return b.startswith("<h2>") or minor(b)
    out = [b for i, b in enumerate(out) if not (i + 1 < len(out) and ((minor(b) and head(out[i + 1])) or (b.startswith("<h2>") and out[i + 1].startswith("<h2>"))))]
    while out and head(out[-1]): out.pop()
    return "\n".join(out)


def mig(k, skip=(), drop=DROP):
    return tidy(migrate(HERE, k, DOMAIN, drop, skip_heads=skip))


# section hubs: prefix, hub path, label, nav label, drawing, photos
GROUPS = [
    ("foundation-repair", "Foundation Repair", "Foundation", "piers", ["push-pier-grantsville", "pier-excavation-south-jordan", "push-pier-morgan-garage", "push-pier-pleasant-grove", "interior-piers-50-plus", "push-pier-salt-lake-city", "stair-step-crack-midvale", "door-frame-crack-saratoga-springs"]),
    ("basement-waterproofing", "Basement Waterproofing", "Waterproofing", "drain", ["cleanspace-waterguard-morgan", "basement-wall-system-draper", "waterproofing-ogden", "cleanspace-waterguard-syracuse", "basement-waterproofing-north-salt-lake", "cold-storage-waterproofing-south-jordan", "basement-repair-lindon", "waterproofing-clearfield"]),
    ("crawl-space-repair", "Crawl Space Repair", "Crawl Space", "crawl", ["smartjack-crawl-salt-lake-city", "crawl-space-vernal", "waterguard-crawl-lehi"]),
    ("concrete-leveling", "Concrete Leveling", "Concrete Leveling", "slab", ["walkway-leveling-ogden", "concrete-after-taylorsville", "polylevel-gap-after", "walkway-leveling-salt-lake-city", "slab-repair-after"]),
    ("concrete-repair", "Concrete Repair", "Concrete Repair", "slab", ["driveway-leveling-ogden", "concrete-before-taylorsville", "polylevel-gap-before", "driveway-void-park-city", "driveway-before-west-valley-city", "sunken-deck-draper"]),
    ("sump-pump", "Sump Pumps", "Sump Pumps", "drain", ["waterproofing-clearfield", "cleanspace-waterguard-syracuse", "waterguard-crawl-lehi"]),
    ("commercial-foundation-contractor", "Commercial Foundations", "Commercial", "helical", ["commercial-retaining-wall-heber-city", "commercial-18-foot-wall", "commercial-polylevel-salt-lake-city", "new-footing-park-city-snow"]),
    ("about-us", "About Us", "About", None, ["davenport-team-photo", "davenport-truck-winter-job"]),
]
GMAP = {g[0]: g for g in GROUPS}
HUBINTRO = {
    "foundation-repair": "Davenport Foundation Repair stabilizes settling, cracking and bowing foundations for homes in West Jordan and across Utah, using engineered steel push piers, helical piers, wall anchors and wall reinforcement. Every job starts with a free inspection and a written estimate.",
    "basement-waterproofing": "Davenport Foundation Repair waterproofs basements in West Jordan and across the Salt Lake Valley with interior drainage, sump pumps, wall vapor barriers and dehumidifiers, so water that reaches the wall is collected and pumped out instead of spreading across the floor.",
    "crawl-space-repair": "Davenport Foundation Repair repairs crawl spaces in West Jordan and across Utah: steel support jacks for sagging floors, sealed vapor barriers, drainage and insulation, turning a damp crawl space into a dry, supported one.",
    "concrete-leveling": "Davenport Foundation Repair lifts and levels sunken concrete in West Jordan and across Utah with PolyLevel foam injection: small holes, a lightweight foam that fills the void under the slab, and concrete you can use the same day.",
    "concrete-repair": "Davenport Foundation Repair repairs driveways, sidewalks, patios and pool decks in West Jordan and across Utah: lifting sunken slabs, filling voids, and sealing cracks and joints so water stays out.",
    "sump-pump": "Davenport Foundation Repair installs, services and repairs sump pumps in West Jordan and across the Salt Lake Valley, including battery backup pumps, crawl space pumps and cast-iron systems from the Basement Systems line.",
    "commercial-foundation-contractor": "Davenport Foundation Repair supports commercial construction and existing commercial buildings in West Jordan and across Utah with helical piles, push piers, helical tiebacks and concrete lifting.",
    "about-us": "Davenport Foundation Repair is a locally owned foundation repair company in West Jordan, Utah, led by owner Ron Davenport, with 30 years of experience in foundation repair, basement waterproofing, crawl space repair and concrete lifting.",
}
KIND_RX = [("anchors", r"bowing|anchor|wall-repair|reinforc|retaining"), ("crack", r"crack|stucco|drywall|window-door"), ("crawl", r"crawl|vapor|sagging|support-beam|joist"),
           ("helical", r"helical|commercial"), ("slab", r"concrete|slab|mudjack|polylevel|sidewalk|driveway|pool|sealant|joint|level"),
           ("drain", r"drain|sump|flood|leak|water|basement|dehumid|iceguard|gutter|downspout"), ("piers", r"pier|settle|sink|heave|chimney|foundation")]
ALT = {"push-pier-grantsville": "Push pier foundation repair in Grantsville, UT", "pier-excavation-south-jordan": "Foundation pier installation and excavation in South Jordan, UT",
       "push-pier-morgan-garage": "Push pier installation and structural stabilization in Morgan, UT", "push-pier-pleasant-grove": "Push pier excavation with support brace in Pleasant Grove, UT",
       "interior-piers-50-plus": "Interior pier installation for severe settlement in Utah", "push-pier-salt-lake-city": "Foundation crack after push pier stabilization in Salt Lake City, UT",
       "stair-step-crack-midvale": "Stair-step foundation crack repair in Midvale, UT", "door-frame-crack-saratoga-springs": "Wall crack above a door frame, Saratoga Springs, UT",
       "cleanspace-waterguard-morgan": "CleanSpace wall liner and WaterGuard drain in Morgan, UT", "basement-wall-system-draper": "Finished basement wall system in Draper, UT",
       "waterproofing-ogden": "Basement waterproofing in Ogden, UT", "cleanspace-waterguard-syracuse": "CleanSpace and WaterGuard in Syracuse, UT",
       "basement-waterproofing-north-salt-lake": "Basement waterproofing in North Salt Lake, UT", "cold-storage-waterproofing-south-jordan": "Waterproofing a cold storage room in South Jordan, UT",
       "basement-repair-lindon": "Basement repair in Lindon, UT", "waterproofing-clearfield": "Waterproofing and sump pump job in Clearfield, UT",
       "smartjack-crawl-salt-lake-city": "SmartJack crawl space support installation in Salt Lake City, UT", "crawl-space-vernal": "Crawl space stabilization and encapsulation in Vernal, UT",
       "waterguard-crawl-lehi": "WaterGuard drain and sump in a Lehi, UT basement", "walkway-leveling-ogden": "Concrete leveling of a front walkway in Ogden, UT",
       "concrete-after-taylorsville": "Concrete after lifting in Taylorsville, UT", "concrete-before-taylorsville": "Concrete before lifting in Taylorsville, UT",
       "polylevel-gap-after": "Entrance slab after PolyLevel lifting", "polylevel-gap-before": "A 5-inch gap at an entrance slab before PolyLevel lifting",
       "walkway-leveling-salt-lake-city": "Concrete leveling of a driveway and walkway in Salt Lake City, UT", "slab-repair-after": "Concrete slab after repair",
       "driveway-leveling-ogden": "Driveway before concrete leveling in Ogden, UT", "driveway-void-park-city": "Driveway void filled in Park City, UT",
       "driveway-before-west-valley-city": "Driveway before repair in West Valley City, UT", "sunken-deck-draper": "Sunken deck shored up in Draper, UT",
       "commercial-retaining-wall-heber-city": "Commercial wall job in Heber City, UT", "commercial-18-foot-wall": "Commercial 18-foot wall",
       "commercial-polylevel-salt-lake-city": "Commercial concrete lifting at North Valley in Salt Lake City, UT", "new-footing-park-city-snow": "Laying new footing in Park City, UT",
       "davenport-team-photo": "The Davenport Foundation Repair team", "davenport-truck-winter-job": "Davenport Foundation Repair truck and yard sign at a winter job"}


def kind_for(path, default):
    for k, rx in KIND_RX:
        if re.search(rx, path): return k
    return default or "piers"


CITYRX = r"\s+(in|for|throughout|serving|across|near)\s+(Utah|UT|Salt Lake|West Valley|Provo|Ogden|Orem|Sandy|Lehi|Layton|the |Northern|Southern).*$"


def label_for(k):
    v = EXT[k]
    t = html.unescape(v["title"]).split("|")[0].strip()
    h = html.unescape(v["heads"][0][1]).strip() if v["heads"] and v["heads"][0][0] == "h1" else ""
    if (not t or t.lower().startswith("davenport") or len(t) < 6) and h: t = h
    t = re.sub(CITYRX, "", t, flags=re.I)
    t = re.sub(r"\s*[-–|]\s*Davenport.*$", "", t)
    t = re.sub(r"^Davenport Foundation Repair\s*[-–:]\s*", "", t)
    return t.strip(" ,-&") or "Davenport Foundation Repair"


def short(t, n=44):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0].rstrip(",:&-") + "…"


KIND_PHOTOS = {"piers": ["push-pier-grantsville", "pier-excavation-south-jordan", "push-pier-morgan-garage", "push-pier-pleasant-grove", "interior-piers-50-plus", "push-pier-salt-lake-city"],
               "anchors": ["stair-step-crack-midvale", "push-pier-salt-lake-city", "basement-wall-system-draper"],
               "crack": ["door-frame-crack-saratoga-springs", "stair-step-crack-midvale", "push-pier-salt-lake-city"],
               "drain": ["cleanspace-waterguard-morgan", "waterproofing-clearfield", "waterproofing-ogden", "cleanspace-waterguard-syracuse", "basement-waterproofing-north-salt-lake", "basement-repair-lindon", "cold-storage-waterproofing-south-jordan", "basement-wall-system-draper"],
               "crawl": ["smartjack-crawl-salt-lake-city", "crawl-space-vernal", "waterguard-crawl-lehi"],
               "slab": ["walkway-leveling-ogden", "driveway-leveling-ogden", "concrete-after-taylorsville", "polylevel-gap-after", "walkway-leveling-salt-lake-city", "slab-repair-after", "driveway-void-park-city", "sunken-deck-draper"],
               "helical": ["commercial-retaining-wall-heber-city", "commercial-18-foot-wall", "commercial-polylevel-salt-lake-city", "new-footing-park-city-snow"]}


# ---------- layout ----------
def header():
    def col(prefix):
        hub = prefix + ".html"
        kids = [c for c in CHILD.get(prefix, []) if c["path"].count("/") == 1][:9]
        return f'<div class="mcol"><a class="mh" href="@/{hub}">{GMAP[prefix][2]}</a>' + "".join(f'<a href="@/{c["path"]}">{c["short"]}</a>' for c in kids) + "</div>"
    mega = "".join(col(g[0]) for g in GROUPS[:7])
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("davenport-logo", NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details class="megad"><summary>Services</summary><div class="drop mega">{mega}</div></details></li>
<li><a href="@/foundation-repair/foundation-problems.html">Problems</a></li><li><a href="@/about-us/reviews.html">Reviews</a></li><li><a href="@/about-us/our-blog.html">Blog</a></li><li><a href="@/about-us.html">About</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{PHONE}<span>{S["phone"]}</span></a><a class="btn" href="@/{EST}">Free Estimate</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{"".join(f'<a href="@/{g[0]}.html">{g[1]}</a>' for g in GROUPS[:7])}
<a href="@/foundation-repair/foundation-problems.html">Foundation problems</a><a href="@/about-us/reviews.html">Reviews</a><a href="@/about-us/our-blog.html">Blog</a><a href="@/service-area.html">Service area</a><a href="@/about-us.html">About</a>
<a class="btn" href="tel:{S["tel"]}">Call {S["phone"]}</a></div></details>
</div></header>''')


def footer():
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top"><p class="foot-say">Fixed from<br><span>the ground down.</span></p><div class="foot-call"><a class="fphone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{EST}">Get a Free Estimate {ARROW}</a></div></div>
<div class="foot">
<div><span class="flogo">{img("davenport-logo", NAME + " logo")}</span><p>Locally owned foundation repair in West Jordan, Utah: foundations, basements, crawl spaces and concrete. A certified Foundation Supportworks dealer.</p>
<p class="soc"><a href="{S["fb"]}" rel="noopener">Facebook</a> &middot; <a href="{S["ig"]}" rel="noopener">Instagram</a> &middot; <a href="{S["yt"]}" rel="noopener">YouTube</a> &middot; <a href="{S["li"]}" rel="noopener">LinkedIn</a></p></div>
<div><h3>Services</h3><ul>{"".join(f'<li><a href="@/{g[0]}.html">{g[1]}</a></li>' for g in GROUPS[:7])}</ul></div>
<div><h3>Company</h3><ul><li><a href="@/about-us.html">About us</a></li><li><a href="@/about-us/meet-the-team.html">Meet the team</a></li><li><a href="@/about-us/reviews.html">Reviews</a></li><li><a href="@/about-us/case-studies.html">Case studies</a></li><li><a href="@/about-us/financing.html">Financing</a></li><li><a href="@/about-us/job-opportunities.html">Jobs</a></li><li><a href="@/about-us/our-blog.html">Blog</a></li></ul></div>
<div><h3>West Jordan office</h3><address>{NAME}<br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p><a href="tel:{S["tel2"]}">{S["phone2"]}</a></p><p><a href="@/service-area.html">Service area</a> &middot; <a href="@/schedule-service.html">Schedule service</a></p></div>
</div><div class="fbottom"><span>&copy; 2026 {NAME}</span><span>{" &middot; ".join(CITIES)}</span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} Call</a><a href="@/{EST}">Free Estimate</a></div>''')


def cta(title="Find out what&rsquo;s happening below grade.", text="A free inspection and a written estimate. We look at the whole house, explain the cause, and show you the options."):
    return f'''<section class="cta"><div class="wrap cta-in"><div><p class="label">Free inspection</p><h2>{title}</h2><p class="lede">{text}</p></div>
<div class="cta-side"><a class="cta-phone" href="tel:{S["tel"]}"><small>Call</small><b>{S["phone"]}</b></a><a class="btn" href="@/{EST}">Request a Free Estimate {ARROW}</a></div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", buttons=True, drawing=None):
    art = f'<figure class="ph-img">{img(image, alt, priority=True)}<figcaption class="mono">{html.escape(alt)}</figcaption></figure>' if image else ""
    btn = f'<div class="btn-row"><a class="btn" href="@/{EST}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>' if buttons else ""
    return f'''<section class="phero{" has-img" if image else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}{btn}</div>{art}</div></section>'''


def side(prefix=None, cur=None):
    rel = ""
    if prefix and prefix in CHILD:
        kids = [c for c in CHILD[prefix] if c["path"] != cur][:10]
        rel = f'<div class="side-rel"><p class="label dark">{GMAP[prefix][1]}</p><ul><li><a href="@/{prefix}.html">Overview</a></li>{"".join(f"<li><a href=@/{c["path"]}>{c["short"]}</a></li>" for c in kids)}</ul></div>'
    return f'''<aside class="sv-side"><div class="side-card"><p class="label">Free inspection</p><h3>Talk to a design specialist</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{EST}">Free Estimate {ARROW}</a><p class="small">{S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}</p></div>{rel}</aside>'''


def quote_form(title="Request a free estimate"):
    return f'''<form class="form" method="post" action="">
<h3>{title}</h3>
<label for="f-svc">How can we help? *<select id="f-svc" name="service" required><option value="">Choose a service</option><option>Water in my basement/crawl space</option><option>Bowing walls or settling foundation</option><option>Cracked or sinking concrete</option><option>Crawlspace problems</option></select></label>
<div class="row"><label for="f-first">First name *<input id="f-first" name="first_name" autocomplete="given-name" required></label><label for="f-last">Last name *<input id="f-last" name="last_name" autocomplete="family-name" required></label></div>
<div class="row"><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label><label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label></div>
<div class="row"><label for="f-addr">Property address *<input id="f-addr" name="address" autocomplete="street-address" required></label><label for="f-zip">Zip code *<input id="f-zip" name="zip" inputmode="numeric" autocomplete="postal-code" required></label></div>
<label for="f-msg">What&rsquo;s going on? (optional)<textarea id="f-msg" name="message" placeholder="A short sentence is best"></textarea></label>
<label class="check"><input type="checkbox" name="sms_consent"><span>I agree to receive transactional SMS from Davenport Foundation Repair about appointments and customer care. Message frequency may vary; data rates may apply; reply STOP to opt out.</span></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


# ---------- page index ----------
PAGES = []
for k, v in EXT.items():
    if k in ("feeds_xml", "google_kml", "sitemap_html") or k.startswith("about_us_our_blog_"): continue
    PAGES.append({"key": k, "path": "" if k == "home" else path_of(k)})
CHILD = {}
for p in PAGES:
    pre = p["path"].split("/")[0].replace(".html", "")
    if "/" in p["path"] and pre in GMAP:
        p["short"] = short(label_for(p["key"]))
        CHILD.setdefault(pre, []).append(p)
for lst in CHILD.values(): lst.sort(key=lambda c: (c["path"].count("/"), c["path"]))

QUOTES = [("Chase and his crew were excellent and we were very satisfied with their attention to detail.", "Susan H.", "North Ogden, UT"),
          ("so far the products are working great and everyone has been a pleasure to work with.", "Nick E.", "West Jordan, UT"),
          ("Very friendly and helpful", "Rod", "Orem, UT")]
JOBLOG = ["push-pier-grantsville", "cleanspace-waterguard-morgan", "smartjack-crawl-salt-lake-city", "walkway-leveling-ogden", "pier-excavation-south-jordan", "basement-wall-system-draper",
          "crawl-space-vernal", "commercial-retaining-wall-heber-city", "push-pier-pleasant-grove", "cold-storage-waterproofing-south-jordan", "concrete-after-taylorsville", "new-footing-park-city-snow"]
HOME_FAQ = [("What are the signs of a foundation problem?", "Uneven, sagging or cracked floors; cracks in drywall or foundation walls; chimneys pulling away from the house; bowing or leaning basement walls; and doors or windows that start to stick."),
            ("Is it better to fix foundation cracks early?", "Yes. A crack is a symptom. Finding the cause while the movement is small usually means a simpler, less disruptive repair than waiting until walls bow or floors drop further."),
            ("How do you fix a crack in a basement wall?", "It depends on the cause. Settling is stopped with piers under the footing; inward pressure is handled with wall anchors or wall reinforcement; and leaking cracks are sealed and paired with drainage. The inspection tells us which."),
            ("Do you charge for an inspection?", "No. We offer a free home inspection and a no-obligation, written cost estimate."),
            ("What areas do you serve?", "We are based in West Jordan and work throughout Utah, including Salt Lake City, West Valley City, Provo, Orem, Ogden, Sandy, South Jordan, Lehi, Layton and nearby cities.")]


def home():
    legend = "".join(f'<li><a href="@/{p}"><span class="n">{n}</span>{t}</a></li>' for n, t, p, x, y in SPOTS)
    plates = "".join(f'''<a class="plate reveal" href="@/{g[0]}.html"><span class="pl-x">{section(g[3])}</span><span class="pl-t"><span class="mono">{i + 1:02d}</span><b>{g[1]}</b><em>{ARROW}</em></span></a>''' for i, g in enumerate(GROUPS[:7]))
    plates += f'''<a class="plate plate-q reveal" href="@/{EST}"><span class="pq-in"><span class="mono">08 &middot; Not sure?</span><b>We&rsquo;ll find the cause first.</b><span>A free inspection and a written estimate, whatever the problem turns out to be.</span><em class="btn">Free Estimate {ARROW}</em></span></a>'''
    log = "".join(f'<figure class="reveal">{img(n, ALT[n])}<figcaption><span class="mono">{ALT[n].split(" in ")[-1] if " in " in ALT[n] else "Utah"}</span>{ALT[n].split(" in ")[0]}</figcaption></figure>' for n in JOBLOG)
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div class="hero-text"><p class="label">West Jordan, Utah &middot; locally owned &middot; 30 years</p>
<h1>Foundation repair in West Jordan, <span>fixed from the ground down.</span></h1>
<p class="lede">Davenport Foundation Repair handles foundation repair in West Jordan and across Utah: stabilizing settling and bowing foundations, waterproofing basements, repairing crawl spaces, and lifting and sealing concrete. Start with a free home inspection and a written estimate.</p>
<div class="btn-row"><a class="btn" href="@/{EST}">Get a Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<div class="hero-art"><p class="mono hx-k">SECTION A&ndash;A &middot; TYPICAL UTAH HOME &middot; TAP A NUMBER</p>{hero()}<ol class="hx-legend">{legend}</ol></div>
</div></section>
<section class="strip" aria-label="At a glance"><div class="wrap strip-in"><span>Locally owned</span><span>30 years</span><span>Foundation Supportworks dealer</span><span>Basement Systems dealer</span><span>Written warranties</span><span>Free inspections</span></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label dark">Our services</p><h2>Seven ways we fix <span>what&rsquo;s underneath.</span></h2>
<p class="lede">There&rsquo;s no one-size-fits-all fix. Each repair is matched to the cause: soil, water, pressure or settlement.</p></div>
<div class="plates">{plates}</div>
</div></section>

<section class="sec dark"><div class="wrap">
<div class="head reveal"><p class="label">From the job file</p><h2>Real jobs, <span>real Utah towns.</span></h2><p class="lede">Photos from our crews&rsquo; own jobs, captioned the way they filed them.</p></div>
<div class="joblog">{log}</div>
<p class="more reveal"><a class="tlink light" href="@/foundation-repair/photo-gallery.html">More job photos {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label dark">Why it lasts</p><h2>Engineered steel, <span>installed by our own crews.</span></h2>
<p>As a certified Foundation Supportworks dealer, we install professionally engineered piers, anchors and wall systems, with ongoing training and written warranties. As a Basement Systems dealer, our waterproofing and sump systems come from the same network of specialists.</p>
<ul class="ticks"><li>Tested and patented foundation products</li><li>Professionally trained technicians</li><li>Written warranties</li><li>A free inspection and written estimate</li></ul>
<a class="tlink" href="@/about-us.html">About Davenport {ARROW}</a></div>
<figure class="reveal fig-truck">{img("davenport-truck-winter-job", ALT["davenport-truck-winter-job"])}<figcaption class="mono">On a winter job</figcaption></figure>
</div></section>

<section class="sec paper2"><div class="wrap">
<div class="head reveal"><p class="label dark">Customer reviews</p><h2>In their words.</h2></div>
<div class="quotes">{"".join(f'<blockquote class="reveal"><p>&ldquo;{q}&rdquo;</p><footer><b>{n}</b><span>{w}</span></footer></blockquote>' for q, n, w in QUOTES)}</div>
<p class="more reveal"><a class="tlink" href="@/about-us/reviews.html">Read the reviews {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label dark">Questions</p><h2>Foundation questions, <span>answered.</span></h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec tight"><div class="wrap"><a class="guide reveal" href="@/{p_blog.POST[1]}"><span class="g-x">{section("piers")}</span><span><span class="label dark">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></span></a></div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Foundation Repair West Jordan, UT | Davenport Foundation Repair",
            "meta": "Davenport Foundation Repair: foundation repair in West Jordan and across Utah, plus basement waterproofing, crawl space repair and concrete lifting. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def fit_meta(m, label):
    m = html.unescape(re.sub(r"\s+", " ", m or "")).strip()
    if not m: m = f"{label} in West Jordan and across Utah from Davenport Foundation Repair. Free inspection and written estimate."
    if len(m) > 160: m = m[:157].rsplit(" ", 1)[0].rstrip(",;:.") + "..."
    for add in (" Davenport Foundation Repair, West Jordan, Utah.", " Free inspection and written estimate.", " Free estimates.", " Serving West Jordan, UT."):
        if len(m) < 150 and len(m + add) <= 160 and add.strip(" .") not in m: m += add
    return html.escape(m, quote=False)


def page(p):
    k, path = p["key"], p["path"]
    v = EXT[k]
    pre = path.split("/")[0].replace(".html", "")
    g = GMAP.get(pre)
    is_hub = path == pre + ".html" and g
    label = g[1] if is_hub else label_for(k)
    service = pre not in ("about-us", "free-estimate", "schedule-service", "service-area", "privacy-policy", "terms-of-use", "opinion", "sitemap")
    h1 = (f"{label} in West Jordan, UT" if service and "west jordan" not in label.lower() else label)
    cands = ([f"{label} in West Jordan, UT | Davenport", f"{label} in West Jordan, UT", f"{label} | West Jordan, UT"] if service else
             [f"{label} | Davenport Foundation Repair", f"{label} | Davenport Foundation Repair, UT", f"{label} | Davenport, West Jordan UT", f"{label} | Davenport"])
    fits = [c for c in cands if 50 <= len(c) <= 60]
    title = fits[0] if fits else min((c for c in cands if len(c) <= 60), key=lambda c: 60 - len(c), default=short(label, 58))
    trail = [HOME] + ([(g[1], pre + ".html")] if g and not is_hub else []) + [(label, path)]
    photos = g[4] if g else ["davenport-truck-winter-job"]
    kp = KIND_PHOTOS.get(kind_for(path, g[3] if g else None)) if service else None
    photos = kp or photos
    im = photos[sum(map(ord, path)) % len(photos)]
    intro = HUBINTRO.get(pre) if is_hub else ((f"{html.escape(html.unescape(v.get('meta') or ''))} Davenport Foundation Repair is based in West Jordan and serves homes across Utah.") if service and v.get("meta") else "")
    kind = kind_for(path, g[3] if g else None) if service else None
    draw = section(kind) if kind else ""
    kids = ""
    if is_hub and pre in CHILD:
        kids = '<h2>In this section</h2><div class="kids">' + "".join(f'<a href="@/{c["path"]}"><b>{c["short"]}</b>{ARROW}</a>' for c in CHILD[pre]) + "</div>"
    content = (f'<p class="answer">{intro}</p>' if intro else "") + (draw if is_hub else "") + mig(k, skip=(html.unescape(v["heads"][0][1]) if v["heads"] else "",)) + ("" if is_hub else draw) + kids
    form = path in (EST, "schedule-service.html")
    right = f'<div class="reveal">{quote_form("Request a free estimate" if path == EST else "Schedule service")}</div>' if form else side(pre if g else None, path)
    body = phero(trail, h1, None, g[1] if g else "Davenport Foundation Repair", im, ALT.get(im, "")) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{content}</article>{right}</div></section>''' + ("" if form else cta())
    can = v.get("canon") or canon(path)
    tgt = re.sub(r"^https?://(www\.)?davenportfoundationrepair\.com/", "", can)
    if can.rstrip("/") != canon(path).rstrip("/") and tgt not in KNOWN and tgt != "":
        CANON_FIX.append((path, tgt)); can = canon(path)  # live canonical points at a duplicate URL not in this build
    pg = {"path": path, "canonical": can, "title": html.escape(title, quote=False), "meta": fit_meta(v.get("meta"), label), "body": body, "og": im,
          "schema": [crumbs_ld(path, trail)] + ([{"@type": "Service", "@id": canon(path) + "#service", "name": label, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": "West Jordan, UT"}}] if service else [])}
    if can.rstrip("/") != canon(path).rstrip("/"): pg["sitemap"] = False
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "Try a service below or call the office.", "404") + f'<section class="sec"><div class="wrap"><div class="kids">{"".join(f"<a href=@/{g[0]}.html><b>{g[1]}</b>{ARROW}</a>" for g in GROUPS[:7])}</div></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Davenport Foundation Repair", "meta": "This page was not found. See Davenport Foundation Repair services in West Jordan, Utah, or call 1-801-569-2302 for a free foundation inspection and estimate.",
            "body": body, "robots": "noindex, follow", "sitemap": False}


def html_sitemap(out):
    trail = [HOME, ("Sitemap", "sitemap.html")]
    groups = {}
    for pg in out:
        if not pg.get("path") or pg["path"] == "404.html" or pg.get("robots"): continue
        groups.setdefault(pg["path"].split("/")[0].replace(".html", ""), []).append(pg)
    cols = "".join(f'<div class="smap-col"><h2>{GMAP[g][1] if g in GMAP else g.replace("-", " ").title()}</h2><ul>' +
                   "".join(f'<li><a href="@/{pg["path"]}">{re.split(r" [|] ", html.unescape(pg["title"]))[0]}</a></li>' for pg in sorted(lst, key=lambda x: x["path"])) + "</ul></div>"
                   for g, lst in sorted(groups.items()))
    body = phero(trail, "Sitemap", "Every page on the Davenport Foundation Repair website.", "Sitemap", buttons=False) + f'<section class="sec"><div class="wrap smap">{cols}</div></section>'
    return {"path": "sitemap.html", "canonical": EXT.get("sitemap_html", {}).get("canon") or canon("sitemap.html"), "title": "Sitemap | Davenport Foundation Repair, West Jordan, UT",
            "meta": "The Davenport Foundation Repair sitemap: every page on foundation repair, basement waterproofing, crawl space repair, concrete lifting, sump pumps and our blog.",
            "body": body, "schema": [crumbs_ld("sitemap.html", trail)]}


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, EST, tidy, section)
    KNOWN.update(p["path"] for p in PAGES)
    KNOWN.update(p_blog.paths())
    KNOWN.update({"sitemap.html", EST})
    out = [home()] + [page(p) for p in PAGES if p["path"] and p["key"] != "about_us_our_blog_html"] + p_blog.pages() + [notfound()]
    out.append(html_sitemap(out))
    return [dict(x, body=Q(x["body"])) for x in out]
