import re, html
from build import U, S, ARROW, PHONE, CHECK, IMG, IMGMAP, CONTACT, INSPECT, img, faq_html, faq_ld, quotes_html, cta, quote_form
import p_blog

# Main keyword: roofing company west valley city (+ roofers / roofing contractor west valley city), per the 14 Oct report.
# Every fact is from the client's own pages (home, about, services, warranty, FAQ, special offers, contact), 17 Oct 2026.
# Years in business differ across the site ("20 years", "over twenty", "27", "over 27", "over 30"); none is used here.

# Contact-sheet review: the client's photos are house and roof shots that look like stock photography; heroes use those
# without people in them (see notes). Images with people are never used as heroes.
POOL = ["j-and-n-roofing-01", "slide-01", "slide-05", "slide-02", "slide-06", "slide-03", "slide-07", "j-and-n-roofing-maintenance-09",
        "j-and-n-roofing-maintenance-11", "j-and-n-roofing-maintenance-14", "j-and-n-roofing-maintenance-05", "salt-lake-city-roofing"]
NOHERO = {"slide-04", "roofing-salt-lake-city-ut", "roofing-salt-lake-city-ut-2", "utah-roofing-services", "utah-roofing-supplies"}


def HERO_POOL():
    names = [n for n in POOL if n in IMG]
    if not names:
        names = sorted((n for n in IMG if IMG[n][0] >= 900 and IMG[n][0] > IMG[n][1] and "logo" not in n), key=lambda n: -IMG[n][0])
    return names


FAQS = [
    ("What warranty does J &amp; N Roofing offer?",
     "We offer a GAF System Plus Warranty. If you have a problem with your roof, you call the GAF Warranty department; a GAF certified roofing contractor will inspect and repair the roof, and if the repair is covered there&rsquo;s no charge. See <a href=\"@/warranty-support/\">warranty support</a>."),
    ("Do I need to take off my current roof to install a new one?",
     "Not always. A re-roof (overlay) can go over an existing roof where it qualifies. We&rsquo;ll look at your roof in a free consultation and tell you whether a tear-off is needed."),
    ("What&rsquo;s the difference between shingle grades?",
     "Heavier grades of shingles offer more durability and higher wind ratings, up to 110 mph. The 30-year shingle is the most commonly installed; 40- and 50-year shingles last longer and carry better wind ratings."),
    ("Is there someone to call outside business hours?",
     f"Yes. Our office hours are 7am to 5pm, Monday&ndash;Friday, and our 24-hour support line is {S['phone24']}."),
]


def anatomy_svg():
    """Fig. 1: a line drawing of a pitched roof with the parts the handbook talks about, numbered."""
    pts = [(300, 84, "1"), (238, 150, "2"), (425, 168, "3"), (382, 205, "4"), (185, 162, "5"), (528, 246, "6"), (546, 268, "7"), (470, 262, "8")]
    marks = "".join(f'<g class="mk"><circle cx="{x}" cy="{y}" r="12"/><text x="{x}" y="{y + 4}">{n}</text></g>' for x, y, n in pts)
    rows = "".join(f'<path class="sh" d="M{100 + i * 15} {226 - i * 10} L{300 - (6 - i) * 0} {226 - i * 10}"/>' for i in range(0))
    shingles = "".join(f'<path class="sh" d="M{96 + k * 22.6:.1f} {238 - k * 15:.1f} L{300:.1f} {238 - k * 15:.1f}"/>' for k in range(1, 9))
    return f'''<svg class="anatomy" viewBox="0 0 600 430" role="img" aria-labelledby="an-t an-d"><title id="an-t">Fig. 1, the parts of a roof</title>
<desc id="an-d">A line drawing of a house with a pitched roof. Numbered parts: 1 ridge vent, 2 shingles, 3 underlayment, 4 roof deck, 5 flashing at the chimney, 6 drip edge, 7 gutter, 8 soffit intake vents.</desc>
<g class="ln">
<rect x="120" y="240" width="370" height="160"/><rect x="165" y="300" width="60" height="70"/><rect x="380" y="300" width="60" height="70"/><rect x="275" y="320" width="50" height="80"/>
<path d="M195 300 V370 M165 335 H225 M410 300 V370 M380 335 H440"/>
<path class="roof" d="M80 244 L300 84 L520 244"/>
<path d="M92 244 L300 96 L508 244" class="thin"/>
{shingles}
<path class="cut" d="M330 104 L520 244 L470 244 L330 140 Z"/>
<path class="under" d="M336 118 L498 238"/><path class="under" d="M338 132 L484 238"/>
<path class="deckl" d="M332 146 L470 244"/>
<rect class="chim" x="168" y="128" width="34" height="74"/><path class="flash" d="M164 202 L206 172"/>
<path class="ridge" d="M286 84 H314 L318 90 H282 Z"/>
<path class="drip" d="M512 240 L522 247 L522 254"/>
<path class="gut" d="M520 252 V268 H550 Q556 268 554 260 Q552 254 558 250 V246"/>
<path class="vent" d="M455 252 h40 M459 249 v6 M467 249 v6 M475 249 v6 M483 249 v6 M491 249 v6"/>
<path class="ground" d="M40 400 H580"/>
</g>
<g class="marks">{marks}</g>
<text class="figcap" x="40" y="424">Fig. 1 &middot; The parts of a roof, from ridge to gutter</text>
</svg>'''


ANAT = [("Ridge vent", "Lets warm, moist attic air out at the peak."), ("Shingles", "The weather surface; heavier grades carry higher wind ratings."),
        ("Underlayment", "The water-shedding layer beneath the shingles."), ("Roof deck", "The sheathing everything is nailed to."),
        ("Flashing", "Metal that seals the joint where the roof meets a chimney or wall."), ("Drip edge", "Metal at the eave that sends water into the gutter."),
        ("Gutter", "Carries the water off the roof and away from the house."), ("Soffit vents", "Intake air that pairs with the ridge vent.")]


def build(r, rec, posts, tests):
    pool = HERO_POOL()
    hero = pool[0]
    services = [("Roofing repairs", "services/roofing-repairs/", "Have a leak? Repairs big and small, with honest advice on whether a repair will do."),
                ("Roof replacement", "services/roof-replacement/", "GAF roofing systems with the GAF System Plus Warranty."),
                ("Roof tear off", "services/roof-tear-off/", "Old layers removed down to the deck before the new roof goes on."),
                ("Re-roof (overlay)", "services/re-roof-overlay/", "New shingles over an existing roof, where it qualifies."),
                ("Inspections &amp; maintenance", "services/roof-inspections-maintenance/", "Small problems caught before they turn into leaks."),
                ("Low slope roofing", "services/low-slope-roofing/", "PVC and TPO for roofs with a pitch under 3:12."),
                ("Roof ventilation", "services/roof-ventilation/", "Intake and exhaust that keep attic moisture off the roof deck."),
                ("Gutter cleaning", "services/gutter-cleaning/", "Avoid water damage with clean gutters.")]
    toc = "".join(f'<a class="toc-row reveal" href="@/{p}"><span class="ch">Chapter {i+1:02d}</span><span class="tt"><b>{n}</b><span>{d}</span></span><span class="dots" aria-hidden="true"></span><i>{ARROW}</i></a>' for i, (n, p, d) in enumerate(services))
    guides = [(p_blog.PATH, p_blog.TITLE, "Fractions of an inch at the roof edge, and why they matter.", "Guide")]
    guides += [("glossary-of-roofing-terms/", "Glossary of roofing terms", "Plain definitions, from algae discoloration to valleys.", "Reference"),
               ("frequently-asked-questions/", "Roofing FAQ", "Shingle grades, warranties, re-roofing and flat roofs.", "Q&amp;A"),
               ("warranty-support/", "How warranty claims work", "The GAF System Plus Warranty, step by step.", "Warranty")]
    books = "".join(f'<a class="book reveal" href="@/{p}"><span class="spine">{k}</span><b>{t}</b><span>{d}</span><em>Read {ARROW}</em></a>' for p, t, d, k in guides)
    coupons = "".join(f'<div class="coupon reveal"><span class="c-k">With a GAF system &amp; warranty</span><b>${a}</b><span class="c-off">off</span><p>{t}</p><span class="c-cut" aria-hidden="true">&#9986;</span></div>'
                      for a, t in [("70", "a complete re-shingle over an existing roof"), ("130", "a complete tear-off and re-shingle over existing sheathing"), ("200", "a complete tear-off, re-sheath and re-shingle")])
    anat = "".join(f'<li><span class="n">{i + 1}</span><b>{t}</b><span>{d}</span></li>' for i, (t, d) in enumerate(ANAT))
    areas = ["Salt Lake", "West Valley", "Cottonwood Heights", "West Jordan", "South Jordan", "Riverton", "Herriman", "Park City", "Tooele",
             "Magna", "Grantsville", "Sandy", "Murray", "Taylorsville", "Centerville", "Ogden"]
    quotes = ""
    picked = tests[:5]
    if picked:
        short = min(picked, key=lambda t: len(t[0])); picked = [short] + [t for t in picked if t is not short]
    for i, (q, a) in enumerate(picked):
        quotes += f'<figure class="pq{" lead" if i == 0 else ""} reveal"><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
    body = f'''
<section class="cover"><div class="wrap cover-grid">
<div class="cover-text"><p class="issue"><span>The roof maintenance handbook</span><span>West Valley City edition</span></p>
<h1>The roofing company West Valley City counts on for <em>quality and upkeep.</em></h1>
<p class="lede">J &amp; N Roofing Maintenance is a residential roofing company in West Valley City, serving the whole Salt Lake City metro area with roof repairs, replacements, tear-offs, re-roofing and maintenance. When quality counts, count on us.</p>
<div class="btn-row"><a class="btn" href="@/{INSPECT}">Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<ul class="cover-facts"><li>GAF certified roofing contractor</li><li>Free consultations</li><li>24-hour support line</li></ul></div>
<figure class="fig reveal">{anatomy_svg()}<ol class="anat">{anat}</ol></figure>
</div></section>

<section class="note-sec"><div class="wrap note-grid">
<div class="letter reveal"><p class="kicker">A note from the J &amp; N team</p>
<p class="dropcap">J &amp; N Roofing Maintenance takes extreme pride in the work we provide for our customers.</p>
<p>We like to help you understand what needs to be done on your home. Our trained staff will explain the best type of roofing material for your house based on its roof pitch and ventilation needs, and we&rsquo;ll answer your questions before, during and after the work.</p>
<p>Many people call us asking for a whole new roof. Sometimes, after we inspect it, all it needs is quality repair work to keep it going strong for years. When that&rsquo;s the case, we&rsquo;ll tell you.</p>
<p class="sig">{img("j-n-roofing-logo", "J & N Roofing Maintenance", cls="sig-logo")}</p></div>
<div class="reveal why"><p class="kicker">Why homeowners call us</p><ol class="checklist">
<li><i>{CHECK}</i><div><b>GAF certified roofing contractor</b><small>Roofs backed by the GAF System Plus Warranty</small></div></li>
<li><i>{CHECK}</i><div><b>Free consultations</b><small>An honest look at whether you need a repair or a replacement</small></div></li>
<li><i>{CHECK}</i><div><b>Yearly training</b><small>Technicians, managers and foremen all go through regular yearly training</small></div></li>
<li><i>{CHECK}</i><div><b>24-hour support</b><small>{S["phone24"]}, for anything that can&rsquo;t wait</small></div></li>
</ol></div></div></section>

<section class="sec contents"><div class="wrap">
<div class="head row reveal"><div><p class="kicker">Contents &middot; roofers in West Valley City</p><h2>The services, <em>chapter by chapter</em></h2></div><p class="head-note">As a roofing contractor in West Valley City, we cover new roofs, old roofs and everything that keeps a roof working.</p></div>
<div class="toc-list">{toc}</div>
</div></section>

<section class="sec shelf"><div class="wrap">
<div class="head row reveal"><div><p class="kicker">The roof maintenance handbook</p><h2>Plain answers <em>before you call</em></h2></div><p class="head-note">Guides from J &amp; N for homeowners who want to understand their roof.</p></div>
<div class="books">{books}</div>
</div></section>

<section class="sec offers-sec"><div class="wrap">
<div class="head row reveal"><div><p class="kicker light">Special offers</p><h2>Save on your next roofing project</h2></div><p class="head-note">With the purchase of a GAF system and warranty. Refer a friend or family member and share the savings. <a href="@/special-offers/">Offer details &rarr;</a></p></div>
<div class="coupons">{coupons}</div>
</div></section>

<section class="sec quotes-sec"><div class="wrap"><div class="head reveal"><p class="kicker">Testimonials</p><h2>What customers say about <em>Norm and the crew</em></h2></div><div class="pqs">{quotes}</div></div></section>

<section class="sec areas"><div class="wrap split top">
<div class="reveal"><p class="kicker">Service areas</p><h2>West Valley City and the Salt Lake metro</h2>
<p class="lede">From our base at {S["street"]} in West Valley City, we serve homeowners across the Salt Lake City metro area.</p>
<p class="area-list">{" &middot; ".join(areas)}</p></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="kicker">Questions</p><h2>Frequently asked</h2><p class="lede">More on the <a href="@/frequently-asked-questions/">FAQ page</a>.</p>
<a class="btn ghost" href="@/{CONTACT}">Contact us {ARROW}</a></div>
<div class="reveal">{faq_html(FAQS)}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company West Valley City, UT | J & N Roofing",
            "meta": "J & N Roofing Maintenance is a roofing company in West Valley City, UT: repairs, replacement, tear-offs and maintenance across the Salt Lake metro. Call us.",
            "body": body, "og": hero,
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(FAQS)],
            "full_biz": True}
