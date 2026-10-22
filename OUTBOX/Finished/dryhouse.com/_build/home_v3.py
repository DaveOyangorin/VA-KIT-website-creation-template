"""Premium home (v3) for dryhouse.com / Rocky Mountain Waterproofing.
References (screenshotted 19 Oct 2026): Tremco Roofing (the brand they install: technical, system-led), Layton Construction
(Utah: editorial serif headline, stat row), Big-D (Utah: dark full-bleed mountain photo, heavy condensed uppercase).
Signature: the sticky wall-section story (each layer lights up as its step scrolls past) and an animated water line in the hero."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import S, U, CITIES
from illus import _defs, _bubble, mil_gauge, head_columns, leak_elevation, SECTION_KEY, LEAKS
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'


def wall_story(p="wst"):
    """The wall section with each system layer in its own <g data-layer> so the scroll story can light it up."""
    L = {
        "1": '<path d="M300 20 V72" class="l-wrb"/><rect x="300" y="20" width="40" height="52" class="f-frame"/><path d="M296 20 V128" class="l-wrb2"/>' + _bubble(212, 52, 1, 296, 52),
        "2": '<rect x="296" y="128" width="4" height="312" class="f-memb"/>' + _bubble(212, 108, 2, 298, 200),
        "3": f'<rect x="282" y="140" width="14" height="300" fill="url(#{p}board)" class="l-thin"/>' + _bubble(150, 300, 3, 288, 300),
        "4": '<rect x="238" y="420" width="12" height="60" class="f-drain"/><path d="M238 432h12M238 444h12M238 456h12M238 468h12" class="l-thin"/>' + _bubble(170, 400, 4, 242, 440),
        "5": '<path d="M340 407 H640" class="l-barrier"/>' + _bubble(560, 452, 5, 520, 407),
        "6": '<path d="M0 150 L282 128" class="l-grade"/><path d="M60 168 L258 152" class="l-dim"/><path d="M60 162v12M258 146v12" class="l-dim"/><text x="70" y="190" class="t-s">6 in. fall in the first 10 ft</text>' + _bubble(40, 120, 6, 120, 143)}
    layers = "".join(f'<g data-layer="{k}">{v}</g>' for k, v in L.items())
    return f'''<svg class="drawing" viewBox="0 0 640 500" role="img" aria-labelledby="{p}t"><title id="{p}t">Section through a basement wall: weather barrier, waterproofing membrane, drainage board, strip drain, under-slab barrier and graded backfill</title>{_defs(p)}
<rect x="0" y="0" width="640" height="500" class="f-sheet"/>
<path d="M0 150 L282 128 L282 500 L0 500Z" fill="url(#{p}soil)"/><rect x="340" y="404" width="300" height="96" fill="url(#{p}soil)"/>
<rect x="250" y="440" width="150" height="40" fill="url(#{p}conc)" class="l-ink"/><rect x="300" y="72" width="40" height="368" fill="url(#{p}conc)" class="l-ink"/><rect x="340" y="384" width="300" height="20" fill="url(#{p}conc)" class="l-ink"/>
<text x="420" y="250" class="t-lab">BASEMENT</text><text x="420" y="268" class="t-s">finished space stays dry</text><text x="18" y="236" class="t-lab">BACKFILL</text>
<text x="604" y="492" text-anchor="end" class="t-s">SECTION A &middot; NOT TO SCALE</text>{layers}</svg>'''


STEPS = [("1", "Above grade", "EnviroDri weather barrier", "A liquid-applied, seamless, vapor-permeable weather-resistive and air barrier on the sheathing. It seals every seam and is code approved under any cladding.", "services/above-grade/envirodri/"),
         ("2", "07 14 00", "Waterproofing membrane", "Rubber-modified waterproofing, 40 mils minimum and up to 80+, that stretches over the cracks every foundation gets. Damp proofing at 10&ndash;20 mils can&rsquo;t.", "services/belowgrade/waterproofing/"),
         ("3", "07 21 00", "Drainage &amp; insulation board", "Warm-N-Dri, Thermal Drain or drainage mat lets water fall straight to the footing instead of pressing on the wall, and protects the membrane from the backfill.", "services/belowgrade/foundation-insulation/"),
         ("4", "33 46 00", "Strip drain at the footing", "An engineered footing drain that replaces pipe and gravel, installed at the base of the wall or the face of the footing.", "services/belowgrade/foundation-drains/"),
         ("5", "Horizontal", "Under-slab barrier", "Paraseal (HDPE and bentonite) for basements deep enough to reach the water table, designed with an engineer.", "services/horizontal-services/under-slab/"),
         ("6", "IRC R401.3", "Grade sloped away", "Six inches of fall in the first ten feet keeps surface water moving away from everything below it.", "blog/before-you-backfill-foundation-checklist/")]
PRODUCTS = ["Tuff-N-Dri QC", "Watchdog H3", "TremProof 260", "TremProof 250 GC", "Warm-N-Dri", "Thermal Drain", "Paraseal", "EnviroDri", "MulSeal", "Strip drain"]
TILES = [("services/belowgrade/", "07 10 00", "Below grade", "Waterproofing, damp proofing, drains and insulation for new foundations.", "foundation-waterproofed", "span-3 row-2"),
         ("services/leak-repair/", "03 01 00", "Leak repair", "Active leaks fixed inside or out.", "honeycomb-wall", "span-3"),
         ("services/horizontal-services/", "07 18 00", "Horizontal", "Suspended slabs, decks, porch caps, under-slab.", "trench-wasatch-truck", "span-3"),
         ("services/above-grade/", "07 25 00", "Above grade", "EnviroDri: a seamless, vapor-permeable weather and air barrier for new homes.", "she-built-sign", "span-6")]
FAQ = [("What is the difference between damp proofing and waterproofing?", "Damp proofing is a thin asphalt coat (10&ndash;20 mils) that slows vapor through the wall and cracks with the foundation. Waterproofing is an asphalt emulsion blended with rubber, at least 40 mils and up to 80+ mils thick, so it stretches over the cracks that form."),
       ("Is damp proofing enough for a basement?", "It is the code minimum for most new homes. If you plan to finish the basement, waterproofing is the better match: damp proofing cracks with the concrete when settling occurs."),
       ("Can you fix a leak in a finished basement?", "Often, yes. We fix active leaks from inside or out: cracks under windows, form ties, honeycomb, cold joints and pipe penetrations. We don&rsquo;t fix plumbing, but we routinely fix where pipes come through the foundation."),
       ("Do you work on commercial projects?", "Yes, from simple additions to complex commercial and government projects. Most work is on Net 30 terms."),
       ("How do I get a bid?", "Send the bid request with plans, spec info or site pictures, or call the office at 801-282-2100.")]


def home(TOWNS):
    steps = "".join(f'<div class="step" data-step="{k}"><p class="s-n">{k} / 6 &middot; {c}</p><h3>{t}</h3><p>{d}</p><a class="tlink" href="@/{p}">More {ARROW}</a></div>' for k, c, t, d, p in STEPS)
    marq = "".join(f"<span>{x}</span>" for x in PRODUCTS * 2)
    bento = "".join(f'<a class="tile {cl} reveal-up" href="@/{p}">{img(i, "")}<span class="t-go">{ARROW}</span><span class="t-in"><small>{c}</small><b>{t}</b><span>{d}</span></span></a>' for p, c, t, d, i, cl in TILES)
    prints = "".join(f'<figure class="print reveal-up" style="--rot:{r}deg">{img(n, cap)}<figcaption>{cap}</figcaption></figure>' for n, cap, r in [
        ("libby-sarah-site", "Libby &amp; Sarah on site", -4), ("crew-in-trench", "Prepping the wall", 3), ("window-well-set", "Setting a window well", -2), ("trench-wasatch-truck", "Footing drain trench", 4), ("she-built-sign", "2021 Parade of Homes", -3)])
    leaks = "".join(f'<li><span class="k-n">{i}</span><a href="@/{p}">{n}</a></li>' for i, (n, p) in enumerate(LEAKS, 1))
    town_list = "".join(f'<li{" class=trip" if t else ""}>{n}</li>' for n, t in TOWNS)
    body = f'''
<section class="hero-full dh-hero"><div class="hf-bg" data-parallax="0.1">{img("foundation-waterproofed", "New foundation coated with black Tuff-N-Dri waterproofing, window wells set", priority=True)}</div>
<div class="waterline" aria-hidden="true"><svg viewBox="0 0 1440 120" preserveAspectRatio="none"><path class="wv1" d="M0 60 C 240 20 480 100 720 60 S 1200 20 1440 60 V120 H0Z"/><path class="wv2" d="M0 70 C 240 100 480 40 720 70 S 1200 100 1440 70 V120 H0Z"/></svg><span>Water stops here &middot; hydrostatic head up to 12 ft</span></div>
<div class="wrap"><div class="hf-row"><div><p class="label">West Jordan, Utah &middot; Est. 1960</p>
<h1>Basement waterproofing in West Jordan, <span><em>done right</em> the first time.</span></h1>
<p class="lede">Rocky Mountain Waterproofing has done basement waterproofing in West Jordan and across Utah since 1960: rubber-modified waterproofing and damp proofing, foundation drains and insulation for new construction, and leak repair for basements that are already finished.</p>
<div class="btn-row"><a class="btn accent" href="@/estimate/">Request a Bid {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<aside class="hf-card"><small>Section 07 14 00</small><b>Fluid-applied waterproofing</b><p>The House That SHE Built, 2020: Tuff-N-Dri on the walls, strip drain at the footing.</p></aside></div></div></section>
<div class="marquee dark" aria-label="Products we apply"><div class="marquee-track">{marq}</div></div>

<section class="sec"><div class="wrap">
<p class="big-intro reveal-up">Damp proofing is the code minimum. It cracks with the concrete. We&rsquo;ve spent sixty years teaching Utah to build with <em>waterproofing</em> instead.</p>
<div class="stats"><div class="stat reveal-up"><b data-count="1960">1960</b><span>Founded as Modern Damp Proofing</span></div><div class="stat reveal-up"><b data-count="1996">1996</b><span>Renamed Rocky Mountain Waterproofing</span></div>
<div class="stat reveal-up"><b>40&ndash;80+</b><span>mils of waterproofing, vs 10&ndash;20 for damp proofing</span></div><div class="stat reveal-up"><b data-count="4">4</b><span>Douglas siblings own it today</span></div></div>
</div></section>

<section class="sec sand"><div class="wrap">
<div class="head reveal-up"><p class="label">Sheet A &middot; Wall section</p><h2>One wall. <em>Every layer</em> we put on it.</h2><p class="lede">Scroll through the system, from the weather barrier above grade to the drain at the footing.</p></div>
<div class="story"><div class="story-visual"><figure class="sheet">{wall_story()}</figure></div><div class="story-steps">{steps}</div></div>
</div></section>

<section class="sec dark-band"><div class="wrap">
<div class="head reveal-up"><p class="label">Product data</p><h2>How much water <em>each coating</em> holds back.</h2></div>
<div class="pd-grid"><figure class="sheet reveal-up">{mil_gauge()}<figcaption>Coating thickness, drawn to scale.</figcaption></figure><figure class="sheet reveal-up">{head_columns()}<figcaption>Hydrostatic head at a crack, from our comparison chart.</figcaption></figure></div>
<p class="pd-more"><a class="tlink light" href="@/services/belowgrade/waterproofing/">Compare the options {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Divisions</p><h2>Four kinds of work, <em>one crew</em> from West Jordan.</h2></div>
<div class="bento dh-bento">{bento}</div></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.18">{img("trench-wasatch-truck", "")}</div><div class="wrap"><blockquote class="reveal-up">&ldquo;Do it right <em>the first time.</em>&rdquo;</blockquote><footer>The Rocky Mountain Waterproofing motto, since McKay and Ellen Douglas</footer></div></section>

<section class="sec"><div class="wrap split" style="align-items:center">
<figure class="sheet reveal-up">{leak_elevation()}</figure>
<div class="reveal-up"><p class="label">Leak repair</p><h2>Already leaking? <em>Inside or out.</em></h2><p>Most basement leaks start at one of six places. Pick yours to see what causes it and how it&rsquo;s sealed.</p><ol class="key">{leaks}</ol><a class="btn" href="@/contact/leak-repair-request/">Leak Repair Request {ARROW}</a></div>
</div></section>

<section class="sec sand"><div class="wrap">
<div class="head reveal-up"><p class="label">Site log &middot; Oct 2020</p><h2>The House That <em>SHE</em> Built.</h2><p class="lede">A home built entirely by women for the 2021 Parade of Homes. Libby and Sarah did the waterproofing, window wells and footing drain.</p></div>
<div class="prints">{prints}</div><p class="center"><a class="tlink" href="@/blog/item/20-the-house-that-she-built/">Read the project story {ARROW}</a></p></div></section>

<section class="split-photo dark-split"><div class="sp-img">{img("libby-shop", "Rocky Mountain Waterproofing team member in the shop")}</div><div class="sp-txt reveal-up">
<p class="label">Since 1960</p><h2>A family business, <em>still in the family.</em></h2>
<ol class="timeline"><li><b>1960</b><span>Modern Damp Proofing starts out, Larry R. as president.</span></li><li><b>Then</b><span>Cecil Douglas, then his brother McKay Douglas.</span></li><li><b>1996</b><span>Renamed Rocky Mountain Waterproofing.</span></li><li><b>Today</b><span>Owned by Chris, Jenn, Tyler and Sam.</span></li></ol>
<div class="team">{img("chris-douglas", "Christopher Douglas")}{img("tyler-douglas", "Tyler Douglas")}{img("sam-douglas", "Sam Douglas")}</div>
<p><a class="tlink light" href="@/about/rmwp-history/">Our history {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}</div>
<div class="reveal-up"><p class="label">Service area</p><h2>Based in West Jordan.</h2><p>Near the yard: {" &middot; ".join(CITIES)}. Our list covers {len(TOWNS)} Utah towns.</p>
<details class="towns"><summary>All {len(TOWNS)} towns we serve</summary><ul>{town_list}</ul><p class="small"><span class="trip-k"></span> Possible trip charge.</p></details>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
'''
    return body, FAQ
