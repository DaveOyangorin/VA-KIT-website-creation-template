import re, html
from build import U, S, ARROW, PHONE, CHECK, IMG, IMGMAP, INSPECT, CONTACT, img, faq_html, faq_ld, quotes_html, cta, quote_form
import p_blog

# Main keyword: roofing company salt lake city (+ roofers / roofing contractor salt lake city), per the 14 Oct report.
# Every fact below is from the client's own pages (home, about, process, free inspection, financing, contact), 17 Oct 2026.
W = "https://ezroofingnow.com/wp-content/uploads/"
HOME_IMGS = {"crow": W + "2026/03/DJI_20260219105641_0157_D.jpg", "nolen": W + "2026/01/DJI_20260116134648_0009_D.jpg",
             "camily": W + "2024/10/DJI_0957.jpg"}


def _n(url):
    return IMGMAP.get(url)


UT_POOL = ["sotorbani-3", "sotorbani-2", "king-2-1", "sotorbani-4", "the-mackerel-residence-3", "waldron-1", "sotorbani-1", "salk-5", "the-mackerel-residence-4", "king-3"]
AR_POOL = ["dji-20260219105641-0157-d", "dji-0957", "dji-0209", "dji-0572", "dji-0218", "img-6057", "dji-20260116134648-0009-d"]


def HERO_POOL(state=None):
    """Wide project photos from the client's own site, picked on the contact-sheet review.
    Utah pages only show Utah projects (Sandy, Draper, Holladay, Woods Cross); Arkansas pages only Arkansas ones."""
    names = UT_POOL if state == "ut" else AR_POOL if state == "ar" else UT_POOL[:4] + AR_POOL[:3] + UT_POOL[4:] + AR_POOL[3:]
    return [n for n in names if n in IMG]


SHIELD = [("Synthetic felt", "Underlayment across the deck"), ("Ice &amp; water barrier", "Protection where water collects"),
          ("Full perimeter drip edge", "Metal edging around the whole roof"), ("Real starter strip", "A sealed first course at the eaves"),
          ("6-nail high-wind pattern", "Nailing pattern rated for 130 MPH"), ("Hail-resistant ridge cap", "Along every ridge"),
          ("Flashing at walls &amp; penetrations", "Comprehensive flashing at every wall and penetration")]

EVAL = [("Shingles &amp; slope wear", "Wear-and-tear across every slope"), ("Overall roof condition", "Deterioration, potential leak areas, storm damage"),
        ("Soffit &amp; fascia", "The edges under and along the roofline"), ("Gutters", "Condition and attachment"),
        ("Windows", "Exterior condition"), ("Siding", "Exterior condition")]

FAQS = [
    ("Is the roof inspection really free?",
     "Yes. All of our roof inspections are free, including a free annual inspection to track wear from year to year, and free inspections after storm damage or another urgent concern."),
    ("Do you help with insurance claims?",
     "Yes. If storm damage is found, we can help you decide whether to file a claim, file it with you, and meet the insurance adjuster on the roof during their inspection."),
    ("Do you offer financing?",
     "Yes. Financing is provided by Foundation Finance Company. Ask us which options are available for your project, or see our <a href=\"@/financing/\">financing page</a>."),
    ("What warranty comes with a new roof?",
     "We provide a 5-year workmanship warranty and extended 25-year warranties, plus a 24/7 warranty hotline: your call is answered and a workman scheduled the same day."),
    ("Where are your offices?",
     f"EZ Roofing Utah is at {S['ut']['street']}, Salt Lake City, UT {S['ut']['zip']}, and EZ Roofing Arkansas is at {S['ar']['street']}, Cabot, AR {S['ar']['zip']}. Both offices are staffed locally."),
]


def build(r, rec, posts, tests):
    crow, nolen, camily = (_n(HOME_IMGS[k]) for k in ("crow", "nolen", "camily"))
    pool = HERO_POOL()
    hero = "sotorbani-3" if "sotorbani-3" in IMG else pool[0]
    ev = "".join(f'<li><i>{CHECK}</i><div><b>{a}</b><small>{b}</small></div></li>' for a, b in EVAL)
    sh = "".join(f'<li><i>{CHECK}</i><div><b>{a}</b><small>{b}</small></div></li>' for a, b in SHIELD)
    stack = "".join(f'<li class="card" style="--i:{i}"><span class="n">{i + 1:02d}<small>/07</small></span><div><b>{a}</b><p>{b}</p></div><i aria-hidden="true">{CHECK}</i></li>' for i, (a, b) in enumerate(SHIELD))
    svcs = [("Roof repair", "Salt Lake City", "utah/salt-lake-city-roof-repair/", "Leaks, missing shingles, flashing and storm damage, found and fixed before they spread."),
            ("Roof replacement", "Salt Lake City", "utah/salt-lake-city-roof-replacement/", "When a roof is beyond repair: tear-off and a new roof installed to the EZ Shield standard."),
            ("Storm damage", "Utah &amp; Arkansas", "roof-storm-damage/", "Wind and hail damage is often invisible from the street. We document it and work with your insurer."),
            ("Shingle repair", "Utah &amp; Arkansas", "shingle-roof-repair-in-utah-and-arkansas/", "Most roofs can be patched. We tell you honestly whether yours is truly repairable."),
            ("Stone coated steel", "Utah &amp; Arkansas", "stone-coated-steel-roofing/", "Is it time to upgrade? We walk you through costs, long-term savings and what to expect from installation."),
            ("Commercial roofing", "Salt Lake City", "utah/salt-lake-city-commercial-roofing/", "Roofing for businesses and multifamily buildings, including single-ply systems."),
            ("Siding", "Salt Lake City", "utah/salt-lake-city-siding-services/", "Siding repair and replacement, checked as part of every property evaluation."),
            ("Windows &amp; doors", "Salt Lake City", "utah/salt-lake-city-windows-services/", "Window replacement and door installation from the same local team."),
            ("Free roof inspection", "Salt Lake City", "utah/salt-lake-city-free-roof-inspection/", "A 26-point inspection of your roof and exterior. No cost, no obligation.")]
    cards = "".join(f'<a class="svc reveal" href="@/{p}"><small>{loc}</small><b>{n}</b><span>{d}</span><em>Learn more &rarr;</em></a>' for n, loc, p, d in svcs)
    projs = [("projects/the-king-residence/", "king-2-1" if "king-2-1" in IMG else None, "The King Residence", ""), ("projects/the-mackerel-residence/", "the-mackerel-residence-4" if "the-mackerel-residence-4" in IMG else None, "The Mackerel Residence", ""),
             ("projects/the-crow-residence/", crow, "The Crow Residence", "")]
    proj_html = ""
    for p, n, nm, loc in projs:
        if not n: continue
        pr = rec.get(p)
        if pr and not loc:
            m = re.search(r"<h5>(.*?)</h5>", pr["body"]); loc = re.sub(r"<[^>]+>", "", m.group(1)) if m else ""
        proj_html += f'<a class="postcard reveal" href="@/{p}">{img(n, nm + " roof by EZ Roofing")}<div class="in"><small>{html.escape(loc)}</small><b>{nm}</b></div></a>'
    latest = [(p_blog.PATH, "The Best Time of Year to Replace a Roof in Utah")] + [(pp, re.sub(r"<[^>]+>", "", pr["h1"] or pp)) for pp, pr in posts[:2]]
    post_html = "".join(f'<li><a href="@/{pp}">{html.escape(t)}</a></li>' for pp, t in latest)
    ut_img = "the-mackerel-residence-3" if "the-mackerel-residence-3" in IMG else pool[1]; ar_img = camily or pool[2]
    body = f'''
<section class="hero"><div class="hero-bg">{img(hero, "Aerial view of the Shotorbani residence roof by EZ Roofing in Holladay, Utah", priority=True)}</div>
<div class="wrap hero-in">
<div class="hero-text"><p class="label light">EZ Roofing &middot; Salt Lake City, UT &middot; Cabot, AR</p>
<h1>Roofing company in Salt Lake City, <span>done the EZ way.</span></h1>
<p class="lede">EZ Roofing is a family owned roofing company in Salt Lake City, Utah and Cabot, Arkansas. We specialize in roof repair and replacement, and every project starts with a free, in-person property evaluation.</p>
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Schedule a Free Inspection {ARROW}</a><a class="btn ghost light" href="tel:{S["ut"]["tel"]}">{PHONE} {S["ut"]["phone"]}</a></div></div>
<div class="sheet"><div class="clip" aria-hidden="true"></div><header><span>Free property evaluation</span><span>26-point</span></header><ol class="checklist ticks">{ev}</ol><div class="sign"><span>No cost &middot; no obligation</span><span>EZ Roofing</span></div></div>
</div></section>

<section class="specs-band" aria-label="EZ Roofing at a glance"><div class="wrap spec-row">
<div class="stat reveal"><b>2017</b><span>Founded in Salt Lake City and Cabot. Family owned and operated.</span></div>
<div class="stat reveal"><b>5&ndash;25<sup>yr</sup></b><span>5-year workmanship warranty, extended 25-year warranties</span></div>
<div class="stat reveal"><b>$2M<sup>policy</sup></b><span>Insurance coverage, $1M+ above the state requirement</span></div>
<div class="stat reveal"><b>A+</b><span>Better Business Bureau accredited rating</span></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Roofers in Salt Lake City</p><h2>Roof repair, replacement and the rest of your exterior</h2><p class="lede">As a roofing contractor in Salt Lake City, we handle everything from a few missing shingles to a full replacement, plus the siding, windows and doors around them.</p></div>
<div class="services">{cards}</div>
</div></section>

<section class="sec dark shield-sec"><div class="wrap shield-grid">
<div class="shield-head"><p class="label light">The EZ Shield Roofing System</p><h2>Seven details we don&rsquo;t <span>compromise on</span></h2>
<p class="lede">Every installation follows our EZ Shield Roofing System, from the felt on the deck to the cap on the ridge. We&rsquo;re a Preferred Contractor with Owens Corning.</p>
<a class="tlink light" href="@/about-ez-roofing/">How we work {ARROW}</a></div>
<ol class="stack">{stack}</ol>
</div></section>

<section class="sec scan-sec"><div class="wrap split rev">
<div class="reveal"><p class="label">Our free inspection</p><h2>We call it a property evaluation, <span>not a roof inspection</span></h2>
<p>We do a physical evaluation of every part of your roof: shingle and slope wear-and-tear and overall condition. Then we check the soffit, fascia, gutters, windows and siding too.</p>
<p>Some roofing contractors charge $75&ndash;$200 for an inspection, depending on location, roof size and materials. At EZ Roofing, all roof inspections are free, and we recommend one every year. If your roof is healthy, we save the data so next year&rsquo;s check can track how it&rsquo;s aging.</p>
<a class="btn navy" href="@/{INSPECT}">About our free inspection {ARROW}</a></div>
<figure class="reveal scan">{img("dji-0057", "Top-down drone view of a hip roof during an EZ Roofing evaluation") if "dji-0057" in IMG else img(pool[3], "EZ Roofing project")}<span class="scanline" aria-hidden="true"></span><figcaption class="scan-tag">Evaluation in progress</figcaption></figure>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Two locations</p><h2>Local teams in Utah and Arkansas</h2><p class="lede">We operate with local staff in both of our service areas.</p></div>
<div class="twostate">
<a class="state reveal" href="@/utah-city/salt-lake-city/">{img(ut_img, "The Mackerel residence, an EZ Roofing project in Draper, Utah")}<div class="in"><h3>EZ Roofing Utah</h3><address>{S["ut"]["street"]}, {S["ut"]["city"]}, {S["ut"]["st"]} {S["ut"]["zip"]}<br>{S["ut"]["phone"]}</address><span class="go" style="display:inline-block;margin-top:12px;font-weight:700">Salt Lake City roofing &rarr;</span></div></a>
<a class="state reveal" href="@/arkansas-city/cabot/">{img(ar_img, "Roofing project by EZ Roofing in Arkansas")}<div class="in"><h3>EZ Roofing Arkansas</h3><address>{S["ar"]["street"]}, {S["ar"]["city"]}, {S["ar"]["st"]} {S["ar"]["zip"]}<br>{S["ar"]["phone"]}</address><span class="go" style="display:inline-block;margin-top:12px;font-weight:700">Cabot roofing &rarr;</span></div></a>
</div>
<div class="chips" style="margin-top:22px"><a href="@/utah-city/">All Utah cities</a><a href="@/arkansas-city/">All Arkansas cities</a></div>
</div></section>

<section class="team"><div class="team-img">{img("thumbnail-img-2510-1", "The EZ Roofing team in their red company shirts")}</div><div class="wrap"><div class="team-card reveal"><p class="label light">Family owned &amp; operated</p><h2>Local people, <span>since 2017</span></h2><p>We operate with local staff in both of our service areas: a licensed general contractor with a dedicated project manager on every full replacement.</p></div></div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label light">Peace of mind</p><h2>The business practices we follow</h2>
<ol class="checklist" style="margin-top:20px">
<li><i>{CHECK}</i><div><b>Licensed general contractor</b><small>A fully licensed general contracting company, not just a roofing contractor</small></div></li>
<li><i>{CHECK}</i><div><b>Highly qualified</b><small>Owens Corning Preferred Contractor and Certified Member of the Roofing &amp; Solar Reform Alliance</small></div></li>
<li><i>{CHECK}</i><div><b>Additional insurance</b><small>A $2M policy, $1M+ higher than the state requires</small></div></li>
<li><i>{CHECK}</i><div><b>24/7 warranty hotline</b><small>Your call is answered and a workman scheduled the same day</small></div></li>
<li><i>{CHECK}</i><div><b>Dedicated project manager</b><small>On site for every full replacement, with a Live Digital Timeline of photos and updates</small></div></li>
<li><i>{CHECK}</i><div><b>Catch-All System</b><small>Heavy-duty tarps and full perimeter protection before a shingle is touched</small></div></li>
</ol></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Project spotlight</p><h2>Recent roofs</h2><p class="lede">A few projects from our gallery. <a href="@/projects/">See all projects</a>.</p></div>
<div class="postgrid">{proj_html}</div>
</div></section>
''' + quotes_html(tests, "What customers say") + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before you book</h2><p class="lede">From the blog:</p><ul class="checks" style="padding-left:1.1em">{post_html}</ul>
<a class="btn navy" href="@/{CONTACT}">Contact us {ARROW}</a></div>
<div class="reveal">{faq_html(FAQS)}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company Salt Lake City | EZ Roofing Utah & Arkansas",
            "meta": "EZ Roofing is a family owned roofing company in Salt Lake City, UT and Cabot, AR: roof repair, replacement and free 26-point inspections. Call (888) 575-3025.",
            "body": body, "og": hero,
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(FAQS)],
            "full_biz": True}
