"""Pages for the everworklandscape.com redesign: "Every season".

Everwork's pitch is that one family crew covers the whole year: sprinklers on in April, mowing all summer, blowouts in October, plows when
the snow hits one to two inches, and somebody answering the phone at 2 a.m. So the home page opens on a full-bleed photo of a lawn they
maintain, and the signature is the season planner: a twelve-month rail with a marker on today's month. Pick a month and the board shows
what Everwork does then, using their own timing (startup "mid to late April", blowouts "early October through early November", plows at
the plan's trigger depth), with links to the service pages. Amber on near-black from their trailer; Archivo, Public Sans, JetBrains Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 41 URLs (no trailing slash) plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL, CITIES
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta
slug = lambda c: re.sub(r"[^a-z]+", "-", c.lower()).strip("-")
SVCS = [("sprinkler-repair", "Sprinkler repair", "ew-night1", "Everwork crew digging out a broken sprinkler line at night"),
        ("sprinkler-installation", "Sprinkler installation", "ew-night2", "Everwork crew member digging a trench for a sprinkler line repair at night"),
        ("sprinkler-startup", "Sprinkler startup", "ew-striped", "Striped lawn and clean sidewalk edge maintained by Everwork"),
        ("sprinkler-winterization", "Sprinkler winterization", "ew-ranch", "Mowed front lawn of a brick ranch home with mature trees"),
        ("lawn-maintenance", "Lawn maintenance", "ew-estate", "Striped lawn maintained by Everwork in front of a stone home"),
        ("yard-cleanup", "Yard cleanup", "ew-ba-side", "Before and after of an overgrown side yard cleaned up by Everwork"),
        ("landscape-installation", "Landscape installation", "ew-ba-bed", "Before and after of a weedy commercial planting bed cleaned up and mulched"),
        ("commercial-maintenance", "Commercial maintenance", "ew-ba-bed2", "Before and after of a commercial landscape bed cleaned up by Everwork"),
        ("hoa-landscape-maintenance", "HOA landscape maintenance", "ew-manuf", "Freshly mowed lawn alongside a sidewalk and a home with a covered porch"),
        ("snow-removal", "Snow removal", "ew-truck", "Everwork truck with a red snow plow and branded trailer parked beside landscaped beds in fall")]
SKIP_H2 = re.compile(r"Quote|Our Reviews|Other Services|Near You|Also Serving|^Services$|^Service Areas$|^Need |^Looking for|^Ready for|FAQs?$|^Contact$", re.I)


def ld_faq(key):
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    for j in re.findall(r'(?s)<script type="application/ld\+json"[^>]*>(.*?)</script>', s):
        try: o = json.loads(j)
        except ValueError: continue
        for x in (o.get("@graph", [o]) if isinstance(o, dict) else o):
            if x.get("@type") == "FAQPage":
                return [(q["name"], "<p>" + html.escape(q["acceptedAnswer"]["text"]) + "</p>") for q in x["mainEntity"]]
    return []


def parse(key):
    """h1 text, intro paragraph, and [(h2, [p or (b, text) items])] for the content between the h1 and the footer."""
    s = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    s = s[s.find("<h1"):]; s = s[:s.find("Everwork was founded")]
    s = re.sub(r"(?s)<(script|style|svg)\b.*?</\1>", "", s)
    h1, intro, secs = "", "", []
    for t, x in re.findall(r"(?s)<(h1|h2|h3|p|li)\b[^>]*>(.*?)</\1>", s):
        segs = [y for y in (re.sub(r"\s+", " ", html.unescape(z)).strip() for z in re.split(r"<[^>]+>", x)) if y]
        if not segs: continue
        if t == "h1": h1 = " ".join(segs).replace(" ,", ","); continue
        if not secs:
            if t == "p" and not intro: intro = " ".join(segs)
            if t == "h2": secs.append([" ".join(segs), []])
            continue
        if t == "h2": secs.append([" ".join(segs), []]); continue
        if segs[-1] == "Learn more": continue
        if re.search(r"5-star|five-star|5\.0", " ".join(segs), re.I): continue
        if t == "li" and len(segs) == 2: secs[-1][1].append(("li2", segs[0], segs[1]))
        elif t == "li": secs[-1][1].append(("li", " ".join(segs)))
        elif t == "h3": secs[-1][1].append(("h3", " ".join(segs)))
        else: secs[-1][1].append(("p", " ".join(segs)))
    return h1, intro, [(h, it) for h, it in secs if not SKIP_H2.search(h)]


def render(secs, drop=()):
    out = []
    for h, items in secs:
        if any(d in h for d in drop): continue
        out.append(f"<h2>{html.escape(h)}</h2>")
        lis, li2 = [], []
        def flush():
            if lis: out.append("<ul class=\"chk\">" + "".join(f"<li>{html.escape(i)}</li>" for i in lis) + "</ul>"); lis.clear()
            if li2: out.append('<div class="ben">' + "".join(f"<div><b>{html.escape(a)}</b><p>{html.escape(b)}</p></div>" for a, b in li2) + "</div>"); li2.clear()
        for it in items:
            if it[0] == "li": lis.append(it[1])
            elif it[0] == "li2": li2.append((it[1], it[2]))
            else:
                flush()
                if it[1] in ("What's included", "Local expertise", "What we do", "Nearby"): continue
                out.append(f"<h3>{html.escape(it[1])}</h3>" if it[0] == "h3" else f"<p>{html.escape(it[1])}</p>")
        flush()
    return "\n".join(out)


REVIEWS = [("Jared was super helpful on the phone. He was quick to show up and did a great job! I would highly recommend.", "Riley Nielsen"),
           ("These guys did excellent work for me at my house! I was very pleased with the service and will use them again.", "John Holling"),
           ("Great experience with Everwork! Fair pricing, quality work, and friendly workers. I'd recommend these guys to anyone.", "Payton Goodman"),
           ("Great company managed by a man who actually cares about his customers and his workers! Would highly recommend.", "Saul Tooele"),
           ("He was super easy to work with! He has really amazing prices and does fantastic work! I'd really recommend him!", "Jacob Faber")]

# the season planner: their own service list and their own timing
MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SEASON = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "fall", "fall", "fall", "winter"]
TASKS = {  # (months 1-12, service slug, label, their wording)
    "snow": ((11, 12, 1, 2, 3), "snow-removal", "Snow removal", "Plows go out once snowfall reaches the trigger depth in your plan, typically one to two inches. Seasonal contracts or per visit."),
    "start": ((4,), "sprinkler-startup", "Sprinkler startup", "Most Salt Lake and Utah County systems start in mid to late April, once overnight freezes have passed and secondary water is on."),
    "clean_s": ((3, 4, 5), "yard-cleanup", "Spring cleanup", "Spring cleanups: leaves, debris and overgrowth cleared."),
    "lawn": ((5, 6, 7, 8, 9), "lawn-maintenance", "Lawn maintenance", "Weekly mowing, edging, trimming, and fertilization."),
    "install": ((4, 5, 6, 7, 8, 9), "landscape-installation", "Landscape &amp; sprinkler installs", "Sod, rock, plants, new landscape projects and efficient new irrigation systems."),
    "blow": ((10, 11), "sprinkler-winterization", "Sprinkler blowout", "Schedule a blowout from early October through early November, before the first hard freeze. You don't need to be home."),
    "clean_f": ((10, 11), "yard-cleanup", "Fall cleanup", "Fall cleanups: leaves, debris and overgrowth cleared."),
    "repair": (tuple(range(1, 13)), "sprinkler-repair", "Sprinkler repair, 24/7", "Same-day and next-day appointments in most of the area, and 24/7 for emergencies like a broken main line."),
}


def planner():
    rail = "".join(f'<button type="button" class="pl-m s-{SEASON[i]}" data-m="{i + 1}" aria-pressed="false"><span>{m}</span></button>' for i, m in enumerate(MONTHS))
    data = {k: {"m": list(v[0]), "href": "@/services/" + v[1] + "/", "t": v[2], "d": v[3]} for k, v in TASKS.items()}
    return f'''<div class="plan" data-plan>
<div class="pl-rail" role="group" aria-label="Choose a month">{rail}</div>
<div class="pl-key"><span class="s-winter">Winter</span><span class="s-spring">Spring</span><span class="s-summer">Summer</span><span class="s-fall">Fall</span></div>
<div class="pl-board" aria-live="polite"><div class="pl-head"><p class="label" data-pl-now>This month</p><h3 data-pl-title>October</h3></div><div class="pl-tasks" data-pl-tasks></div></div>
<script type="application/json" data-pl-data>{json.dumps(data)}</script>
<noscript><p>Sprinkler startup: mid to late April. Blowouts: early October through early November. Snow removal: when snow reaches your plan's trigger depth. Sprinkler repair: 24/7, all year.</p></noscript>
</div>'''


def svc_cards(area=None):
    return '<div class="svc-grid">' + "".join(f'<a class="svc-c" href="@/services/{s}/"><figure>{img(im, alt)}</figure><b>{n}{" in " + area if area else ""}</b><em>{ARROW}</em></a>' for s, n, im, alt in SVCS) + "</div>"


def city_chips(prefix=""):
    return '<div class="chips">' + "".join(f'<a href="@/service-areas/{slug(c)}/">{prefix}{c}</a>' for c in CITIES) + "</div>"


def home():
    body = f'''
<section class="e-hero"><div class="eh-img" data-parallax="0.08">{img("ew-hero", "Thick green lawn maintained by Everwork in front of a Utah brick home", priority=True)}</div>
<div class="wrap eh-in"><div class="eh-txt"><p class="label">Sandy, Utah &middot; Open 24 hours, 7 days</p>
<h1>Landscaping in Sandy &amp; sprinkler repair, <em>every season.</em></h1>
<p class="lede">Everwork is a family-owned landscaping and property maintenance crew based in Sandy. Sprinklers, lawns, cleanups, commercial and HOA grounds, and snow removal for homes and businesses across Salt Lake and Utah County, around the clock.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Get a free quote {ARROW}</a><a class="btn ghost" href="tel:+18018758109">{PHONE} Call or text (801) 875-8109</a></div></div></div>
<div class="eh-strip"><div class="wrap"><span><b>24/7</b> calls &amp; texts answered</span><span><b>10</b> services, one crew</span><span><b>27</b> cities served</span><span><b>1&ndash;2&Prime;</b> typical plow trigger</span></div></div></section>

<section class="sec e-plan" id="planner"><div class="wrap">
<div class="e-head split-h reveal"><div><p class="label">The Everwork year</p><h2>What your yard needs <em>this month.</em></h2></div><p class="lede">Sprinklers on in April, mowing through summer, blowouts before the hard freeze, plows when it snows. Pick a month to see what we&rsquo;re doing then.</p></div>
{planner()}
</div></section>

<section class="sec e-svcs"><div class="wrap">
<div class="e-head split-h reveal"><div><p class="label">What we do</p><h2>Ten services. <em>One crew.</em></h2></div><a class="tlink" href="@/services/">All services {ARROW}</a></div>
{svc_cards()}
</div></section>

<section class="e-night"><div class="wrap e-night-in">
<figure class="reveal">{img("ew-night1", "Everwork crew digging out a broken sprinkler line at night")}</figure>
<div class="reveal"><p class="label">After-hours sprinkler line repair</p><h2>Broken main line at 10&nbsp;p.m.? <em>Call anyway.</em></h2>
<p>Got an emergency or after-hours request? We&rsquo;re open 24/7 to keep your property safe and beautiful. Most sprinkler repairs are same-day or next-day, and you usually don&rsquo;t need to be home: we text you photos and a summary when the work is done.</p>
<a class="btn accent" href="tel:+18018758109">{PHONE} (801) 875-8109</a></div></div></section>

<section class="sec e-work"><div class="wrap">
<div class="e-head reveal"><p class="label">Real jobs by the Everwork crew</p><h2>No stock photos. <em>Just our work.</em></h2></div>
<div class="ba-grid">{"".join(f'<figure class="reveal">{img(n, a)}<figcaption>{c}</figcaption></figure>' for n, a, c in (("ew-ba-park", "Before and after of an overgrown park strip trimmed and edged by Everwork", "Park strip trim &amp; edging"), ("ew-ba-bed", "Before and after of a weedy commercial planting bed cleaned up and mulched", "Commercial bed cleanup"), ("ew-ba-planter", "Before and after of a raised planter box with weeds removed", "Weeding &amp; bed detail"), ("ew-ba-side", "Before and after of a side yard cleanup", "Side yard cleanup")))}</div>
<div class="lawns">{"".join(f'<figure class="reveal">{img(n, a)}</figure>' for n, a in (("ew-estate", "Striped lawn in front of a stone home"), ("ew-striped", "Crisp mowing stripes and clean sidewalk edges"), ("ew-hillside", "Large mowed hillside backyard with a valley view"), ("ew-stucco", "Freshly mowed striped lawn with a clean edged border")))}</div>
</div></section>

<section class="e-band"><div class="band-img" data-parallax="0.1">{img("ew-truck", "Everwork truck with a red snow plow and branded trailer")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Look for the orange &amp; black</p><p>As a local, family-run company, we treat each property as if it were our own.</p></blockquote></div></section>

<section class="sec e-revs"><div class="wrap">
<div class="e-head reveal"><p class="label">Our reviews</p><h2>What clients <em>say.</em></h2></div>
<div class="revs">{"".join(f'<blockquote class="rev reveal"><p>&ldquo;{html.escape(q)}&rdquo;</p><cite>{n}</cite></blockquote>' for q, n in REVIEWS)}</div>
</div></section>

<section class="sec e-areas"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Service areas</p><h2>Based in Sandy. <em>27 cities.</em></h2><p>Serving homes and businesses across Salt Lake County and Utah County. Not sure if we cover your street? Give us a call.</p>
<a class="post-card e-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>Deep, less frequent watering, the half-inch can test, and when to start in spring, from USU Extension and EPA WaterSense.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{city_chips()}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Landscaping Sandy, UT | Sprinkler Repair &amp; Snow | Everwork",
            "meta": "Everwork: family-owned landscaping in Sandy, UT. Sprinkler repair and installation, lawn care, cleanups, HOA and commercial care, 24/7 snow removal.",
            "body": body, "body_class": "is-home", "og": "ew-hero", "schema": [crumbs_ld("", [HOME])]}


SVC_META = {  # title, meta (keyword from the report first where it has one)
    "sprinkler-repair": ("Sprinkler Repair in Sandy &amp; Salt Lake County | Everwork", "Sprinkler repair in Sandy and across Salt Lake and Utah County: broken heads, leaks, valves, lines and controllers. Same or next day, 24/7 for emergencies."),
    "sprinkler-installation": ("Sprinkler System Installation in Sandy &amp; Utah | Everwork", "New sprinkler system installation for Utah yards: efficient zones, valves, lines and controllers designed for your lawn and beds. Free quotes, call or text."),
    "sprinkler-startup": ("Spring Sprinkler Startup &amp; Turn-On in Utah | Everwork", "Spring sprinkler startup in Utah: slow pressurizing, every zone inspected, broken heads and leaks found, controller set for spring. Most start mid-late April."),
    "sprinkler-winterization": ("Sprinkler Winterization &amp; Blowouts in Utah | Everwork", "Sprinkler blowouts in Utah: compressed air through every zone, controller set to winter mode. Book early October to early November; no need to be home."),
    "lawn-maintenance": ("Lawn Care in Sandy &amp; Salt Lake County, Utah | Everwork", "Lawn care and maintenance in Sandy and across Salt Lake and Utah County: weekly mowing, edging, trimming and fertilization from a family-owned local crew."),
    "yard-cleanup": ("Yard Cleanup in Sandy, UT | Spring &amp; Fall | Everwork", "Spring and fall yard cleanup in Sandy and across the Wasatch Front: leaves, debris, overgrowth, beds and hauling, for homes, rentals and commercial sites."),
    "landscape-installation": ("Landscape Installation in Salt Lake &amp; Utah County | Everwork", "Landscape installation across Salt Lake and Utah County: sod, rock, plants, beds and new landscape projects, built by the family-owned Everwork crew."),
    "commercial-maintenance": ("Commercial Landscaping &amp; Maintenance in Utah | Everwork", "Commercial landscaping and property maintenance in Utah: year-round grounds care, irrigation and snow removal for offices, retail centers and HOAs."),
    "hoa-landscape-maintenance": ("HOA Landscape Maintenance in Salt Lake &amp; Utah County", "HOA landscape maintenance across Salt Lake and Utah County: common areas, irrigation and snow removal for HOA communities, from one local crew."),
    "snow-removal": ("Snow Removal in Sandy &amp; Salt Lake County, 24/7 | Everwork", "24/7 snow removal in Sandy and across Salt Lake and Utah County: plowing, shoveling and ice melt for homes and businesses. Seasonal or per-visit service."),
}


def make_pages():
    out = [home()]
    # services hub
    h1, intro, secs = parse("services")
    out.append(K.page("services/", "Services", "Our services", intro, "Everwork", "Landscaping, Irrigation &amp; Snow Removal Services | Everwork",
                      "Everwork services: sprinkler repair, installation, startup and blowouts, lawn maintenance, yard cleanup, landscaping, commercial and HOA care, snow removal.",
                      svc_cards(), image="ew-stucco", alt="Freshly mowed striped lawn", canonical=EXT["services"]["canon"]))
    for s, n, im, alt in SVCS:
        key = "services_" + s.replace("-", "_")
        h1, intro, secs = parse(key)
        faqs = ld_faq(key)
        body = render(secs) + f"<h2>{n} near you</h2><p>Based in Sandy and serving homes and businesses across Salt Lake County and Utah County.</p>" + city_chips()
        t, m = SVC_META[s]
        out.append(K.page(f"services/{s}/", n, h1, "", "Serving Salt Lake &amp; Utah County", t, m, body, image=im, alt=alt, intro=intro, crumbs=[("Services", "services/")], faqs=faqs,
                          canonical=EXT[key]["canon"], schema=[K.svc_schema(f"services/{s}/", n, "Salt Lake County and Utah County, UT")]))
    # areas
    h1, intro, secs = parse("service_areas")
    out.append(K.page("service-areas/", "Service areas", "Service areas", "Salt Lake County &amp; Utah County.", "Everwork", "Service Areas: Salt Lake County &amp; Utah County | Everwork",
                      "Everwork serves 27 cities across Salt Lake County and Utah County, from North Salt Lake to Provo, based in Sandy. Sprinklers, lawns, cleanups and snow.",
                      (f'<p class="answer">{html.escape(intro)}</p>' if intro else "") + render(secs) + city_chips(), image="ew-hillside", alt="Large mowed hillside backyard with a valley view", canonical=EXT["service_areas"]["canon"]))
    pics = ["ew-ranch", "ew-estate", "ew-striped", "ew-manuf", "ew-stucco", "ew-hillside", "ew-hero"]
    for i, c in enumerate(CITIES):
        key = "service_areas_" + slug(c).replace("-", "_")
        h1, intro, secs = parse(key)
        faqs = ld_faq(key)
        body = render(secs, drop=("Our Services",)) + f"<h2>Our services in {c}</h2>" + svc_cards(c)
        t0 = EXT[key]["title"].replace(" | Everwork", "")
        title = (t0 + " | Everwork") if len(t0) <= 49 else t0
        meta = f"{html.unescape(intro)}"
        if len(meta) > 160: meta = meta[:157].rsplit(" ", 1)[0] + "&hellip;"
        out.append(K.page(f"service-areas/{slug(c)}/", c, h1, "", "Service area", title.replace("&", "&amp;"), html.escape(html.unescape(meta)).replace("&amp;hellip;", "&hellip;"), body,
                          image=pics[i % len(pics)], alt=f"A lawn maintained by Everwork", intro=intro, crumbs=[("Service areas", "service-areas/")], faqs=faqs, canonical=EXT[key]["canon"]))
    con = f'''<p class="answer">Tell us what you need and we&rsquo;ll get back to you fast, day or night. Prefer to talk? Call or text us anytime.</p>
<dl class="info"><div><dt>Call or text</dt><dd><a href="tel:+18018758109">(801) 875-8109</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>446 E Mountain View Dr<br>Sandy, UT 84070</address></dd></div><div><dt>Hours</dt><dd>Open 24 hours, 7 days a week</dd></div></dl>
<h2>How booking works</h2><ol><li><b>Select your service.</b> Sprinkler repair, lawn care, yard cleanup, snow removal, and more.</li><li><b>Get your free quote.</b> Fill in a quick form and we&rsquo;ll get back to you with a no-obligation quote.</li>
<li><b>Schedule your visit.</b> Pick a time that works for you. In many cases, you don&rsquo;t even need to be home.</li><li><b>Relax and enjoy.</b> Our crew handles everything.</li></ol>'''
    out.append(K.page("contact/", "Contact", "Get your free quote", "Day or night, call, text or send the form.", "Contact", "Contact Everwork | Free Landscaping Quote, Sandy, UT",
                      "Contact Everwork in Sandy, UT for a free quote: call or text (801) 875-8109, open 24 hours, 7 days a week. Sprinklers, lawns, cleanups and snow removal.",
                      con, canonical=EXT["contact"]["canon"], form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Service areas", "service-areas/"), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Call or text (801) 875-8109.", " Open 24/7.")) for x in out]
