import html
from build import U, S, ARROW, PHONE, img, faq_html, faq_ld, cta, quote_form

IC = {
    "talk": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/><path d="M8.5 11h7M8.5 14h4"/></svg>',
    "level": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="2.5" y="8" width="19" height="8" rx="1.5"/><circle cx="12" cy="12" r="1.6"/><path d="M6 8v3M18 8v3"/></svg>',
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l8 3v6c0 4.4-3.4 8-8 9-4.6-1-8-4.6-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
    "tag": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M3 12V4h8l10 10-8 8z"/><circle cx="7.5" cy="8" r="1.4"/></svg>',
}


def prop(cls, title, text, links, image, alt):
    ls = " ".join(f'<span class="go">{l} {ARROW}</span>' for l, _ in links)
    return f'''<a class="prop {cls} reveal" href="@/{links[0][1]}">{img(image, alt)}<div class="in"><h3>{title}</h3><p>{text}</p>{ls}</div></a>'''


def build(r, pool, posts):
    faqs = r["faqs"]
    reviews = pool[:3]
    qcards = "".join(
        f'<figure class="quote{" big" if i == 0 else ""} reveal"><div class="stars" aria-hidden="true">★★★★★</div><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>'
        for i, (q, a) in enumerate(reviews))
    latest = [("blog/how-to-prevent-ice-dams-on-a-utah-roof/", "How to Prevent Ice Dams on a Utah Roof", "icicles-snow-overhang-roof", "Winter roofing")]
    pick = ["blog/roof-repair-vs-roof-replacement-how-to-choose/", "blog/should-you-get-metal-roofing-utah/"]
    for p, pr in posts:
        if p in pick: latest.append((p, pr["h1"] or pr["title"], None, "From the blog"))
    cards = []
    from build import IMGMAP
    for p, t, im, lab in latest:
        if im is None:
            rr = [x for x in posts if x[0] == p][0][1]
            im = IMGMAP.get(rr.get("og_image") or "", "roofing-project-utah-residential")
        cards.append(f'<a class="postcard reveal" href="@/{p}">{img(im, t)}<div class="in"><small>{lab}</small><b>{html.escape(t)}</b></div></a>')
    body = f'''
<section class="hero">{img("roof-work-in-utah-winter", "Roofers working on a snow-covered roof on a Utah home in winter", priority=True)}
<div class="wrap hero-in">
<div class="hero-text">
<p class="label light">American Roofing Company &middot; South Salt Lake</p>
<h1>Your Trusted Utah <span>Roofing Company</span></h1>
<p class="lede"><strong style="color:#fff">Since 1954</strong>, we have been a trusted roofing contractor in Salt Lake City and beyond for roof repair, roof replacement, roof restoration and roof maintenance. Protect one of your biggest investments with American Roofing Company.</p>
<div class="btn-row"><a class="btn" href="tel:{S["tel"]}">{PHONE} Call {S["phone"]}</a><a class="btn ghost" href="@/request-free-quote/">Schedule a Free Roof Evaluation {ARROW}</a></div>
<div class="badges">{img("badge-certainteed-shinglemaster", "CertainTeed SELECT ShingleMaster certification", lazy=False)}{img("badge-certainteed-gold-star", "CertainTeed Gold Star contractor", lazy=False)}{img("badge-gephardt", "Gephardt Approved roofing company", lazy=False)}{img("badge-bbb", "BBB Accredited Business", lazy=False)}</div>
</div>
<div class="pin" aria-hidden="true"><svg viewBox="0 0 220 220"><defs><path id="pinc" d="M110,110 m-82,0 a82,82 0 1,1 164,0 a82,82 0 1,1 -164,0"/></defs>
<circle cx="110" cy="110" r="106" class="r1"/><circle cx="110" cy="110" r="96" class="r2"/><circle cx="110" cy="110" r="66" class="r3"/>
<text class="ring-t"><textPath href="#pinc" textLength="510" lengthAdjust="spacing">American Roofing Company &#9733; Salt Lake City, Utah &#9733;</textPath></text></svg>
<span class="pin-in"><small>Est.</small><b>1954</b><i>&#9733; &#9733; &#9733;</i></span></div>
</div></section>

<section class="ruler-sec" aria-label="American Roofing by the numbers"><div class="wrap">
<div class="ruler-head"><p class="label">Seventy-two years on Utah roofs</p><p class="ruler-years"><span>1954</span><span>2026</span></p></div>
<div class="ruler" aria-hidden="true"><span class="fill"></span><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i><i class="big"></i><i class=""></i><i class=""></i></div>
<div class="statrow">
<div class="stat"><b>72<sup>+</sup></b><span>Years serving Utah</span></div>
<div class="stat"><b>10.2<sup>yr</sup></b><span>Average foreman tenure</span></div>
<div class="stat"><b>81<sup>%</sup></b><span>Repeat or referral business since 2024</span></div>
<div class="stat"><b>50<sup>%</sup></b><span>Of projects generate a referral</span></div>
</div></div></section>

<section class="sec stamp-sec"><div class="wrap">
<div class="stamp-row reveal">{img("repair-first-promise", "Our Repair-First Promise: if repairable, we won't sell a replacement")}
<div><p class="label light">The Repair-First Promise</p><p class="stamp-say">If your roof can be repaired, <span>we won&rsquo;t sell you a replacement.</span></p></div></div>
<div class="why reveal">
<div><h2>Why Utah property owners choose American Roofing Company</h2>
<p>Roofing problems often come with more questions than answers. Does the roof need a repair or a full replacement? How much is it going to cost? Could insurance be involved? Can you trust the recommendation you've been given?</p>
<p>We believe every roofing decision starts with understanding the condition of your roof. Our Salt Lake City roofing company provides thorough evaluations, explains your options clearly, and recommends the solution that's right for your property.</p></div>
<div class="pillars">
<div class="pillar"><span class="ic">{IC["talk"]}</span><div><h3>Clear communication</h3><p>We explain your roof's condition, walk you through your options, and keep you informed from start to finish.</p></div></div>
<div class="pillar"><span class="ic">{IC["level"]}</span><div><h3>Quality workmanship</h3><p>Every project is completed using proven installation practices and receives a final quality inspection.</p></div></div>
<div class="pillar"><span class="ic">{IC["shield"]}</span><div><h3>We stand behind our work</h3><p>New roof installations include a 5-year workmanship warranty for added peace of mind.</p></div></div>
<div class="pillar"><span class="ic">{IC["tag"]}</span><div><h3>Cost transparency</h3><p>You get complete project pricing before anything is scheduled.</p></div></div>
</div></div>
</div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label light">How it works</p><h2>Get a straight answer in three steps</h2>
<ol class="steps" style="grid-template-columns:1fr;margin-top:28px">
<li><h3>Schedule a roof evaluation</h3><p>We'll learn about your roof, discuss your concerns, and schedule a convenient time to inspect your property.</p></li>
<li><h3>Review your options</h3><p>We'll explain what we found, answer your questions, recommend the solution that best fits your roof's condition, and give you a clear scope of work and project pricing before scheduling.</p></li>
<li><h3>Complete your roofing project</h3><p>We'll complete your project with quality workmanship, perform a final inspection, and provide applicable warranty information.</p></li>
</ol></div>
<div class="reveal" style="color:var(--ink)">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Roofs we service</p><h2>Roofing solutions for every property</h2></div>
<div class="props">
{prop("f", "Homeowners", "Whether you're dealing with a roof leak, aging shingles, or storm damage, we'll help you understand the condition of your roof and the options available.", [("Residential Roofing", "residential/")], "residential-roofing-utah-home", "Two-story Utah home with a new shingle roof")}
{prop("", "Businesses &amp; commercial", "Inspections, repairs, replacements and maintenance designed to minimize disruptions to your operations.", [("Commercial Roofing", "commercial/")], "commercial-roofing-salt-lake-city", "Roofer working on a flat commercial roof in Salt Lake City")}
{prop("", "Apartments &amp; condos", "Careful planning, clear communication and coordination with communities, associations and property managers.", [("Apartment Roofing", "apartment-roof-repair/")], "multifamily-roof-replacement", "Aerial view of a multifamily building roof replacement")}
{prop("w", "Storm damage &amp; insurance claims", "If wind or hail damaged your roof, we can inspect the damage, document our findings, and give you the information you need for the insurance claim process.", [("Storm Damage Roofing", "services/storm-damage-repair/")], "storm-damage-roofing", "Shingle roof with sections torn off by wind")}
</div>
<p class="reveal" style="margin-top:18px"><a class="tlink" href="@/condo-roof-repair/">Condo roofing {ARROW}</a></p>
</div></section>

<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Our work</p><h2>Roofing projects across Utah</h2><p class="lede">From single-family homes to large commercial buildings and multifamily communities, completed with a commitment to quality workmanship and dependable service.</p></div>
<div class="projects">
<figure class="reveal">{img("roofing-project-utah-main", "Large stone home with a new dark shingle roof")}<figcaption>Residential replacement</figcaption></figure>
<figure class="reveal">{img("roofing-project-utah-blue-home", "Blue-sided home with a gray shingle roof")}<figcaption>Shingle roof, blue home</figcaption></figure>
<figure class="reveal">{img("roofing-project-utah-residential", "Gray home with a new shingle roof and landscaped yard")}<figcaption>Residential roofing</figcaption></figure>
<figure class="reveal">{img("completed-roofing-project-final-inspection", "Aerial view of a completed flat roof on a multi-story building")}<figcaption>Final inspection, commercial</figcaption></figure>
<figure class="reveal">{img("hero-house", "Modern farmhouse with a dark shingle roof at sunset")}<figcaption>New roof, modern farmhouse</figcaption></figure>
<figure class="reveal">{img("hunter-high", "Hunter High School roof project")}<figcaption>Hunter High</figcaption></figure>
<figure class="reveal">{img("hillsdale-elementary1", "Hillsdale Elementary roof project")}<figcaption>Hillsdale Elementary</figcaption></figure>
</div>
<p class="reveal" style="margin-top:18px"><a class="tlink" href="@/case-study/">View case studies {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Where we work</p><h2>Based in Salt Lake City. On roofs across the Wasatch.</h2>
<p>American Roofing Company serves homeowners and property owners throughout the Wasatch, including northern Utah, Park City, Ogden, Provo, Tooele, and many surrounding communities.</p>
<p>From residential homes to commercial and multifamily properties, our certified team has experience with a wide variety of roofing systems and project types.</p>
<div class="chips" style="margin:22px 0 8px"><a href="@/service-area/murray-utah-roofing/">Murray</a><a href="@/service-area/sandy-utah-roofing/">Sandy</a><a href="@/service-area/draper-utah-roofing/">Draper</a><a href="@/service-area/ogden-utah-roofing/">Ogden</a><a href="@/service-area/park-city-utah-roofing/">Park City</a><a href="@/service-area/provo-utah-roofing/">Provo</a><a href="@/service-area/tooele-utah-roofing/">Tooele</a><a href="@/service-area/layton-utah-roofing/">Layton</a></div>
<a class="tlink" href="@/service-area/">See all service areas {ARROW}</a></div>
<div class="stack reveal">{img("utah-roofing-service-areas", "Utah valley neighborhood with mountains and a lake behind")}{img("utah-service-area-map", "Map of the Utah service area from Ogden to Provo, Park City and Tooele", cls="b")}<span class="cap">Northern Utah</span></div>
</div></section>

<section class="band">{img("icicles-snow-overhang-roof", "Thick snow overhang with icicles along a roof edge")}
<div class="wrap"><div class="copy reveal"><p class="label light">Utah winters</p><h2>Icicles look pretty. Ice dams cost money.</h2>
<p class="lede">When heat from the house melts roof snow and it refreezes at the eaves, water backs up under the shingles. Here's how to stop it before the ceiling stains show up.</p>
<a class="btn" href="@/blog/how-to-prevent-ice-dams-on-a-utah-roof/">Read the ice dam guide {ARROW}</a></div></div></section>

<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Reviews</p><h2>What our clients are saying</h2></div>
<div class="quotes">{qcards}</div></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">FAQs</p><h2>Questions we hear every week</h2><p class="lede">Straight answers about choosing a Salt Lake City roofer.</p></div>
<div class="reveal">{faq_html(faqs)}</div>
</div></section>

<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Latest articles</p><h2>From the roofing blog</h2></div>
<div class="grid">{"".join(cards)}</div>
<p class="reveal" style="margin-top:18px"><a class="tlink" href="@/blog/">View more articles {ARROW}</a></p>
</div></section>
''' + cta()
    return {"body": body, "og": "roof-work-in-utah-winter",
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(faqs)] if faqs else []}
