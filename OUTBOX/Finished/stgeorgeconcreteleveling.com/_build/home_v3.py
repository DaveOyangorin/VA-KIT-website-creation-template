"""Premium home (v3) for stgeorgeconcreteleveling.com: "Measure the lip".
References (screenshotted 20 Oct 2026): Linear (dark, precise, instrument-like UI), Stripe Press (editorial type), Hilti (one hard
accent). Signature: the lip gauge in the hero. Drag the sunken slab down; a caliper reads the lip in sixteenths of an inch and
the panel names the 2010 ADA Standards rule it falls under (303.2 vertical up to 1/4 in, 303.3 bevel 1/4-1/2 in, 303.4 ramp over
1/2 in). The client's own pages cite the same ADA 2010 rules."""
import html, json, os
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, HERE
from pagekit import ARROW, PHONE, HOME, cta, form
from illus import gauge, surface
import p_blog

ADA = "https://www.access-board.gov/ada/"
SURFS = [("driveway-leveling/", "Driveway", "driveway"), ("sidewalk-leveling/", "Sidewalk", "sidewalk"), ("patio-leveling/", "Patio", "patio"), ("garage-floor-leveling/", "Garage floor", "garage"),
         ("pool-deck-leveling/", "Pool deck", "pool"), ("concrete-step-leveling/", "Steps", "steps"), ("porch-entryway-leveling/", "Porch &amp; entry", "porch"), ("commercial-concrete-leveling/", "Commercial", "slab")]
STEPS = [("On-site assessment", "We inspect your slab, identify causes of settlement, and take laser readings to plan a precise lift."),
         ("Utility locate &amp; prep", "We coordinate Blue Stakes 811 when required, mark injection points, and protect adjacent surfaces."),
         ("Clear proposal", "You get a written estimate with scope, timeline, and options like crack/joint sealing or sealing treatments."),
         ("Precision lifting", "We drill small ports, inject polyurethane in stages, monitor lift with levels, and stabilize soils beneath."),
         ("Seal &amp; clean", "We patch ports, seal key joints, tidy up, and walk the site with you to confirm results before we leave.")]
TOWNS = [("Washington", "washington/"), ("Santa Clara", "santa-clara/"), ("Hurricane", "hurricane/"), ("Ivins", "ivins/"), ("La Verkin", "la-verkin/"), ("Toquerville", "toquerville/"), ("Leeds", "leeds/"),
         ("Springdale", "springdale/"), ("Cedar City", "cedar-city/"), ("Kanab", "kanab/"), ("Entrada", "entrada-st-george/"), ("SunRiver", "sunriver-st-george/"), ("Bloomington", "bloomington/"),
         ("Green Valley", "green-valley/"), ("Dixie Springs", "dixie-springs-st-george/"), ("Pine Valley", "pine-valley/")]
FAQ = [("How small a lip counts as a trip hazard?", f'Under the <a href="{ADA}" rel="noopener">2010 ADA Standards</a>, a change in level up to 1/4 inch may be vertical, 1/4 to 1/2 inch must be beveled no steeper than 1:2, and more than 1/2 inch must be ramped. Use the gauge above to see where your lip falls.'),
       ("How does foam lifting work?", "We drill small ports, inject polyurethane in stages, monitor the lift with levels, and stabilize the soils beneath. Then we patch the ports and seal key joints."),
       ("Do you handle public sidewalks?", "We can handle right-of-way permits for public sidewalks and coordinate utility locates (Blue Stakes 811)."),
       ("What does an estimate cost?", "Quotes are always free. We inspect the slab on site and give you a written estimate with scope, timeline and options.")]


def home():
    surfs = "".join(f'<a class="sf reveal-up" href="@/{p}">{surface(s)}<b>{t}</b><em>{ARROW}</em></a>' for p, t, s in SURFS)
    steps = "".join(f'<li class="reveal-up"><span>{i + 1:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS))
    towns = "".join(f'<li><a href="@/{p}">{t}</a></li>' for t, p in TOWNS)
    body = f'''
<section class="lg-hero"><div class="wrap lg-grid">
<div class="lg-text"><p class="label">St. George &middot; Southern Utah &middot; polyurethane foam lifting</p>
<h1>Concrete leveling in St. George. <span>Measure the lip, then fix it.</span></h1>
<p class="lede">St. George Concrete Leveling does concrete leveling in St. George and across Southern Utah: precision foam injection and slab lifting for sunken driveways, sidewalk trip hazards, patios, garage floors and pool decks. Licensed and insured, with free on-site estimates.</p>
<div class="btn-row"><a class="btn accent" href="tel:+14354665545">{PHONE} 435-466-5545</a><a class="btn ghost" href="@/contact/">Get a free quote {ARROW}</a></div></div>
<div class="lg-gauge"><p class="g-q">How big is your lip? <span>Drag to set it.</span></p>{gauge()}<p class="g-src">Rules: <a href="{ADA}" rel="noopener">2010 ADA Standards</a> &sect;303.2&ndash;303.4. They apply to public places; for a home they&rsquo;re a good yardstick.</p></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head split-head reveal-up"><div><p class="label">What we level</p><h2>Pick the surface <span>that sank.</span></h2></div>
<p>Driveways scrape bumpers and push water toward the garage. Sidewalk lips trip people. Pool decks settle from washouts and irrigation leaks. Each surface has its own page.</p></div>
<div class="sfgrid">{surfs}</div>
<p><a class="tlink" href="@/concrete-slab-lifting/">All concrete slab lifting services {ARROW}</a></p></div></section>

<section class="sec proc-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">How it works</p><h2>Straightforward, safe, <span>and transparent.</span></h2></div>
<ol class="procline">{steps}</ol></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.15">{img("red-rock-st-george", "")}</div><div class="wrap"><blockquote class="reveal-up">Red soils, desert moisture swings, <span>and slabs that move.</span></blockquote><footer>Pool decks in Southern Utah often settle from washouts and irrigation leaks. We lift with water-resistant foam that won&rsquo;t wash out. <a href="@/pool-deck-leveling/">Pool deck leveling</a></footer></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Service area</p><h2>St. George <span>and Southern Utah.</span></h2></div>
<ul class="chips towns">{towns}</ul>
<p><a class="tlink" href="@/washington-county/">Washington County</a> &nbsp; <a class="tlink" href="@/iron-county/">Iron County</a> &nbsp; <a class="tlink" href="@/kane-county/">Kane County</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Get a free quote", msg_label="How can we help?")}</div>
</div></section>
<div class="wrap"><p class="credits">Background photo, for atmosphere only: &ldquo;<a href="https://www.flickr.com/photos/105245699@N08/53126613420" rel="noopener">Snow Canyon State Park</a>&rdquo; by pkinney62 (<a href="https://creativecommons.org/licenses/by/2.0/" rel="noopener">CC BY 2.0</a>).</p></div>
''' + cta()
    return {"path": "", "canonical": "https://stgeorgeconcreteleveling.com/", "title": "Concrete Leveling St. George, UT | St. George Concrete Leveling", "og": "red-rock-st-george",
            "meta": "Concrete leveling in St. George, UT: polyurethane foam lifting for sunken driveways, sidewalk trip hazards, patios, garage floors and pool decks. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
