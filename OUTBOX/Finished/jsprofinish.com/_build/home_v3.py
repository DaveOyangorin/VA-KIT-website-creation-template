"""Premium home (v3) for jsprofinish.com: "Bare studs to finished".
References (screenshotted 20 Oct 2026): Hammer & Hand (craft photography, labelled tiles, uppercase captions), Sun Design
(warm editorial serif, "a home like yours" room cards), The Basement Sanctuary (basement category: finished-room photography).
Signature: the "same room" stage scrubber. The client photographed the same rooms from the same spot on three visits
(Clinton, July-August 2026); a tape-measure rail cross-fades hung -> textured -> finished. Only the two rooms the client
itself paired are used (bedroom closet wall, stairs from the family room)."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, ST, EMAIL, HOURS
from pagekit import ARROW, PHONE, STAR, HOME, cta
import p_blog

ROOMS = [("Bedroom closet wall", ["drywall-hung-clinton-bedroom-closets", "drywall-textured-clinton-bedroom-closets", "finished-clinton-bedroom-bifold-closets"]),
         ("Stairs from the family room", ["drywall-hung-clinton-rec-room-stairs", "drywall-textured-clinton-rec-room-stairs", "finished-clinton-basement-stairs"])]
STAGES = [("Visit 1", "Drywall hung"), ("Visit 2", "Taped &amp; textured"), ("Visit 3", "Finished")]
ALTS = {0: "drywall hung, screws set, seams ready for tape", 1: "seams taped and floated, ceiling sprayed with texture", 2: "painted, trimmed, doors hung, hardware set"}
TRADES = [("services/basement-remodeling/", "Basement remodeling", "Update an outdated or half-finished basement. New layout, new finishes, or a full re-do.", "finished-basement-wet-bar"),
          ("services/framing/", "Framing", "Basement walls, room additions, and structural framing. Straight, square, and to code.", "basement-framing-open-layout"),
          ("services/drywall/", "Drywall", "Hung, taped, mudded, and textured to match the rest of your house.", "drywall-hung-taped-room"),
          ("services/carpentry/", "Carpentry &amp; trim", "Trim, doors, built-ins, mudroom benches, and the details you see every day.", "mudroom-bench-builtins"),
          ("services/painting/", "Painting", "Walls, ceilings, trim, and cabinets, prepped properly so the finish lasts.", "interior-painting-accent-wall"),
          ("services/flooring/", "Flooring", "LVP, laminate, and carpet, including basement installs over concrete.", "lvp-flooring-wide-plank"),
          ("services/bathroom-remodeling/", "Bathroom remodeling", "Full bathroom remodels and new basement bathrooms, from demo to fixtures.", "bathroom-vanity-remodel")]
ROOMCARDS = [("Family &amp; rec rooms", "Built-ins, a fireplace wall, room for everyone.", "basement3"),
             ("Wet bars &amp; kitchenettes", "Cabinetry, counters, and plumbing for entertaining downstairs.", "basement-kitchenette-bar"),
             ("Guest suites &amp; bedrooms", "Conforming bedrooms with the egress windows code requires.", "finished-basement-bedroom"),
             ("Built-ins &amp; mudrooms", "Benches, cubbies, closets and barn doors, built on site.", "mudroom-bench-builtins"),
             ("Bathrooms", "Full or half baths added as part of your basement finish.", "powder-bathroom-remodel")]
REVIEWS = [("Robert Hansen", "We hired JS ProFinish to finish our basement and couldn&rsquo;t be happier with the results. They handled everything from moving a pre-existing studs while doing the framing to sheetrock, mudding and taping, LVP flooring, and finish carpentry. &hellip;"),
           ("Garret Atkin", "They replaced all of my baseboards and door casing. They also completed some board and batten walls. The work was well done. They were on time each day.")]
FAQ = [("How much does it cost to finish a basement?", 'It depends on the size of your basement and what you want in it. A simple rec room costs a lot less than a full suite with a bathroom. We don&rsquo;t do ballpark guesses. We come out, measure, and give you a written estimate for free, with the price locked in before work starts. <a href="@/basement-finishing-cost/">See typical basement finishing costs in Utah</a>.'),
       ("How long does a basement finish take?", "Timeline depends on the scope of the project, and we&rsquo;ll give you an honest schedule with your estimate before any work begins. Once we start, our crew shows up and keeps the project moving until it&rsquo;s done."),
       ("Do you handle permits and inspections?", "Yes. We handle the necessary permits and inspections so your finished basement meets local building codes in Davis and Weber Counties."),
       ("Are you licensed and insured?", f"Yes. JS ProFinish is a licensed and insured Utah contractor (UT Lic. #{ST['license']}), specializing in basement finishing throughout Davis and Weber Counties. You can verify our license on the Utah DOPL licensee lookup.")]
DAVIS = [("Clearfield", "cities/clearfield/"), ("Layton", "cities/layton/"), ("Kaysville", "cities/kaysville/"), ("Syracuse", "cities/syracuse/"), ("Farmington", "cities/farmington/"), ("Bountiful", "cities/bountiful/")]
WEBER = [("Ogden", "cities/ogden/"), ("Roy", "cities/roy/"), ("North Ogden", None), ("South Ogden", None), ("Pleasant View", None), ("Harrisville", None)]
REVIEWS_URL = "https://www.google.com/maps/place/?q=place_id:ChIJIYKoa5IbU4cRxscxPd43Wog"


def scrubber(compact=False):
    tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-room="{i}">{t}</button>' for i, (t, ims) in enumerate(ROOMS))
    frames = ""
    for r, (t, ims) in enumerate(ROOMS):
        for s, n in enumerate(ims):
            frames += f'<figure class="sc-img{" on" if r == 0 and s == 0 else ""}" data-r="{r}" data-s="{s}">{img(n, f"{t}, Clinton basement: {ALTS[s]}")}</figure>'
    marks = "".join(f'<span class="sc-mark" style="--at:{i * 50}%"><small>{v}</small><b>{l}</b></span>' for i, (v, l) in enumerate(STAGES))
    return f'''<div class="scrub{" compact" if compact else ""}" data-scrub>
<div class="sc-head"><div class="sc-tabs" role="tablist" aria-label="Choose a room">{tabs}</div><p class="sc-now" aria-live="polite"><span>Visit 1</span> Drywall hung</p></div>
<div class="sc-frame">{frames}<span class="sc-stamp">Same spot &middot; 3 visits &middot; no staging</span></div>
<div class="sc-tape"><div class="sc-rule" aria-hidden="true"></div>{marks}<input class="sc-range" type="range" min="0" max="200" value="0" step="1" aria-label="Move from the first visit to the finished room"></div>
</div>'''


def home(jsp_form):
    trades = "".join(f'''<a class="trade reveal-up" href="@/{p}" data-img="{i}"><span class="tr-n">{i + 1:02d}</span><b>{l}</b><span class="tr-d">{d}</span><span class="tr-th">{img(im, "")}</span><em>{ARROW}</em></a>''' for i, (p, l, d, im) in enumerate(TRADES))
    previews = "".join(f'<span class="tp-img{" on" if i == 0 else ""}" data-img="{i}">{img(im, "")}</span>' for i, (p, l, d, im) in enumerate(TRADES))
    rooms = "".join(f'<a class="room-card reveal-up" href="@/gallery/" style="--rot:{r}deg">{img(im, "")}<span><b>{t}</b><em>{d}</em></span></a>' for (t, d, im), r in zip(ROOMCARDS, (-1.5, 1, -0.5, 1.5, -1)))
    marq = "".join(f"<span>{t}</span>" for t in ["Framing", "Drywall", "Tape &amp; mud", "Texture", "Trim", "Doors", "Built-ins", "Paint", "LVP", "Bathrooms"] * 2)
    revs = "".join(f'<blockquote class="rv reveal-up"><div class="stars" aria-label="5 stars">{STAR * 5}</div><p>&ldquo;{t}&rdquo;</p><footer>{n} &middot; Google review, 2025</footer></blockquote>' for n, t in REVIEWS)
    city = lambda l, p: f'<li><a href="@/{p}">{l}</a></li>' if p else f"<li>{l}</li>"
    body = f'''
<section class="jsp-hero"><div class="wrap jh-grid">
<div class="jh-text"><p class="label">Basement specialists &middot; Clearfield, Utah</p>
<h1>Basement finishing in Northern Utah, <em>done right.</em></h1>
<p class="lede">JS ProFinish does basement finishing across Davis and Weber County, from Ogden to Bountiful. Since 2019, we&rsquo;ve been helping Northern Utah families turn unfinished basements into the extra space they need: rec rooms, home theaters, guest suites, play areas. Quality work, fair pricing, no surprises.</p>
<div class="btn-row"><a class="btn accent" href="@/contact-us/">Get a Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{ST["tel"]}">{PHONE} {ST["phone"]}</a></div>
<ul class="jh-facts"><li>Licensed &amp; insured</li><li>UT Lic. #{ST["license"]}</li><li>Davis &amp; Weber Counties</li></ul></div>
<div class="jh-visual"><figure class="jh-main" data-parallax="0.06">{img("basement1", "Family room finished by JS ProFinish with custom built-ins, shiplap fireplace wall, and floating mantel", priority=True)}</figure>
<figure class="jh-before">{img("basement-framing-open-layout", "The same kind of basement at the framing stage: bare studs on a concrete floor")}<figcaption>Where every job starts</figcaption></figure>
<svg class="jh-arrow" viewBox="0 0 120 70" aria-hidden="true"><path d="M6 60 C 40 62, 70 40, 108 12" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="4 7"/><path d="M96 10 L110 10 L106 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg>
<div class="jh-rating"><div class="stars" aria-hidden="true">{STAR * 5}</div><b>4.8</b><span>from 18 Google reviews<br>as of September 2026</span></div></div>
</div></section>
<div class="marquee tape" aria-label="Our trades"><div class="marquee-track">{marq}</div></div>

<section class="sec"><div class="wrap">
<p class="big-intro reveal-up">Most contractor photos are the finished room. Ours show the whole job, <em>so you know what to expect in your own basement.</em></p>
<div class="stats"><div class="stat reveal-up"><b data-count="2019">2019</b><span>Finishing basements since, from our Clearfield shop</span></div>
<div class="stat reveal-up"><b>4.8</b><span>Google rating from 18 reviews (Sept. 2026)</span></div>
<div class="stat reveal-up"><b data-count="7">7</b><span>trades, all our own crew, under one contract</span></div>
<div class="stat reveal-up"><b data-count="12">12</b><span>cities across Davis and Weber County</span></div></div>
</div></section>

<section class="sec scrub-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Clinton basement &middot; 900 sq ft &middot; July&ndash;August 2026</p><h2>Same room. <em>Three visits.</em></h2>
<p>We stood in the same place each visit so the stages line up. Drag along the tape to see what changed.</p></div>
{scrubber()}
<p class="scrub-more"><a class="tlink light" href="@/projects/clinton-basement-finish/">See all 18 photos and who did what {ARROW}</a></p>
</div></section>

<section class="sec"><div class="wrap">
<div class="head split-head reveal-up"><div><p class="label">What we do</p><h2>Seven trades. <em>One crew.</em></h2></div>
<p>Basement finishing is the main job. These are the trades behind it, all done by our own crew, and each one is available on its own.</p></div>
<div class="trades-wrap"><div class="trades">{trades}</div><div class="trade-preview" aria-hidden="true">{previews}</div></div>
<p><a class="tlink" href="@/services/">See all services {ARROW}</a></p>
</div></section>

<section class="sec rooms-sec"><div class="wrap"><div class="head reveal-up"><p class="label">Built into your basement</p><h2>A basement finish is more than <em>four walls.</em></h2></div></div>
<div class="rooms-row">{rooms}</div>
<div class="wrap"><p><a class="tlink" href="@/gallery/">See the full gallery {ARROW}</a></p></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.16">{img("framing-interior-walls", "")}</div><div class="wrap"><blockquote class="reveal-up">&ldquo;When we had the inspection done the inspector praised <em>how nicely the framing had been done.</em>&rdquo;</blockquote><footer>Ash Roberts &middot; Google review, 2025 &middot; &ldquo;They finished our basement and helped us make it into a small apartment.&rdquo;</footer></div></section>

<section class="sec"><div class="wrap rv-wrap">
<div class="rv-sum reveal-up"><p class="label">What homeowners say</p><h2><span class="big">4.8</span> out of 5</h2><p>From 18 Google reviews, as of September 2026.</p><a class="tlink" href="{REVIEWS_URL}" rel="noopener">Read all reviews on Google {ARROW}</a></div>
<div class="rv-grid">{revs}</div></div></section>

<section class="sec process-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">How it works</p><h2>From first walkthrough to finished basement, <em>in three steps.</em></h2></div>
<div class="steps3" role="list"><svg class="chalk" viewBox="0 0 1000 40" preserveAspectRatio="none" aria-hidden="true"><path d="M10 20 C 250 6, 500 34, 990 18" pathLength="1"/></svg>
<div class="st3 reveal-up" role="listitem"><span>1</span><b>Free consultation</b><p>We&rsquo;ll visit your home, take measurements, and talk through what you want. No pressure, just honest advice about what&rsquo;s possible.</p></div>
<div class="st3 reveal-up" role="listitem"><span>2</span><b>Design &amp; planning</b><p>Together we&rsquo;ll create a plan that works for your space and budget. You&rsquo;ll know exactly what to expect before we break ground.</p></div>
<div class="st3 reveal-up" role="listitem"><span>3</span><b>Construction</b><p>Our crew shows up on time, keeps the job site clean, and gets the work done right. We&rsquo;ll keep you updated along the way.</p></div></div>
<a class="cost-card reveal-up" href="@/basement-finishing-cost/"><span class="label">Cost guide</span><b>What does a basement finish cost in Utah?</b><span>Per square foot ranges for basic, mid-range, and custom finishes, what moves the price, and how permits factor in for Davis and Weber County.</span><em>Read the cost guide {ARROW}</em></a>
</div></section>

<section class="split-photo owner-split"><div class="sp-img">{img("crew-framing-prep-overhead", "JS ProFinish crew prepping a framed basement before insulation and drywall")}</div><div class="sp-txt reveal-up">
<p class="label">Who you&rsquo;ll work with</p><h2>Pablo J. Padilla, <em>owner.</em></h2>
<p>Pablo started JS ProFinish in Clearfield in 2019 and still runs the crew on every job. JS ProFinish is a local, owner-operated shop. Not a franchise, not a lead-reselling service. When you call, you talk to the people who will actually be in your basement.</p>
<p>The company holds Utah contractor license #{ST["license"]} for carpentry, flooring, drywall, paint, and plastering. Those are our own trades, not subcontracted work.</p>
<p><a class="tlink" href="@/about-us/">About us {ARROW}</a></p></div></section>

<section class="sec areas-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Where we work</p><h2>Based in Clearfield. <em>Minutes from both counties.</em></h2></div>
<div class="counties"><div class="county reveal-up"><h3>Davis County</h3><p>Based in Clearfield, we&rsquo;re minutes from anywhere in Davis County.</p><ul>{"".join(city(l, p) for l, p in DAVIS)}</ul><a class="tlink" href="@/davis-county/">Basement finishing in Davis County {ARROW}</a></div>
<div class="county reveal-up"><h3>Weber County</h3><p>From Ogden to Pleasant View, we finish basements all over Weber County.</p><ul>{"".join(city(l, p) for l, p in WEBER)}</ul><a class="tlink" href="@/weber-county/">Basement finishing in Weber County {ARROW}</a></div>
<div class="shop reveal-up"><span class="label">The shop</span><b>{ST["street"]}<br>Clearfield, UT {ST["zip"]}</b><span>{HOURS}</span></div></div>
</div></section>

<section class="sec faq-sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Common questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{jsp_form()}<p class="small">Prefer to talk now? <a href="tel:{ST["tel"]}">{ST["phone"]}</a> &middot; {HOURS}</p></div>
</div></section>
'''
    return {"path": "", "canonical": "https://jsprofinish.com", "title": "Basement Finishing in Northern Utah | JS ProFinish, Clearfield", "og": "basement1",
            "meta": "Basement finishing in Northern Utah from JS ProFinish: licensed and insured, based in Clearfield, serving Davis and Weber County since 2019. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
