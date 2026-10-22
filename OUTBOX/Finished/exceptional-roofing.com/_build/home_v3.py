"""Premium home (v3) for exceptional-roofing.com. Imported by pages.py: home() replaces the v1 layout.
References: Copper X (full-bleed hero on the roof itself), Baker Roofing (tilted photo prints, heritage voice), Strike Group
(condensed uppercase display, diagonal photo cut). Signature: the material selector, drawn swatch + their own photo per material."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, AREAS, PHONES
from pagekit import ARROW, PHONE, HOME, cta
from illus import swatch, MATERIALS
import p_blog

HOME_FAQ = [("Do you provide free roofing estimates?", "Yes. Free quotes on any project, and most quotes are given the same day or week. Call or text 801-680-6499, or send the estimate form."),
            ("Should I repair or replace my roof?", "If the issue is limited to one area and the rest of the roof is serviceable, repair may be enough. Repeated leaks, widespread wear, storm damage in several areas, or aging materials usually point to replacement."),
            ("What roofing systems do you work on?", "Asphalt shingle, standing seam and corrugated metal, copper, wood shake and wood shingle, flat and low-slope, TPO and PVC, for homes and businesses."),
            ("Do you offer financing?", "Yes, through Acorn Finance. You can pre-qualify online and review payment options; approval, rates and terms are set by the lenders, not by us."),
            ("Do you work outside Salt Lake County?", "Our core area runs from Salt Lake City to Park City, Heber, Kamas and Santaquin. For the right project we also take work elsewhere in Utah, southern Idaho and southwest Wyoming.")]

SWAPS = [("asphalt", "shingle-drone", "Architectural shingles from the drone"), ("metal", "standing-seam-home", "Standing seam metal on a modern home"),
         ("shake", "wood-shake-historic", "Wood shake on a historic-style home"), ("copper", "copper-roof-crew", "Custom copper roof, crew on site"), ("tpo", "emergency-tarp", "Flat roof membrane work")]
TILES = [("roof-repair/", "Roof repair", "Leaks, flashing, pipe boots, storm damage, skylights.", "chimney-cap-after", "span-2 row-2"),
         ("roof-replacement/", "Roof replacement", "Tear-off, deck, underlayment, flashing, cleanup and a final inspection.", "shingle-mountain-home", "span-4"),
         ("metal-roofing/", "Metal roofing", "Standing seam, corrugated, copper, CMG finishes.", "metal-panel-worker", "span-2"),
         ("flat-roofing/", "Flat &amp; TPO", "TPO, PVC and low-slope roofs.", "emergency-tarp", "span-2"),
         ("roof-inspections/", "Inspections", "A clear read on the roof you have.", "shingle-aerial", "span-2"),
         ("commercial-roofing/", "Commercial", "Repair, replacement and maintenance for businesses.", "metal-roof-project", "span-2"),
         ("storm-damage-insurance-claims/", "Storm &amp; insurance", "Storm damage, emergency tarps and claims.", "winter-new-build", "span-2")]
PRINTS = [("wood-shake-home", "Wood shake, historic home", -5), ("standing-seam-home", "Standing seam accents", 3), ("cedar-shake-detail", "Cedar shake detail", -2),
          ("winter-new-build", "New build, in the snow", 4), ("shingle-front", "Architectural shingles", -3)]
PRODUCTS = ["GAF Timberline HDZ", "CertainTeed Presidential TL", "GAF Grand Sequoia", "CertainTeed Landmark", "CMG Metals finishes", "GAF EverGuard TPO", "Hand-split cedar shake", "Custom copper"]


def home():
    sel = "".join(f'<button class="mat{" on" if i == 0 else ""}" type="button" data-swap="{k}"><span class="mat-sw">{swatch(k, "ms-" + k)}</span><span class="mat-t"><small>No. {i + 1:02d}</small><b>{n}</b><span>{d}</span></span></button>'
                  for i, (k, n, d, p) in enumerate(MATERIALS))
    pics = "".join(f'<figure class="mat-img{" show" if i == 0 else ""}" data-swap-img="{k}">{img(im, alt)}<figcaption>{alt}</figcaption></figure>' for i, (k, im, alt) in enumerate(SWAPS))
    bento = "".join(f'<a class="tile {c} reveal-up" href="@/{p}">{img(i, "")}<span class="t-go">{ARROW}</span><span class="t-in"><small>{n:02d}</small><b>{t}</b><span>{d}</span></span></a>' for n, (p, t, d, i, c) in enumerate(TILES, 1))
    prints = "".join(f'<figure class="print reveal-up" style="--rot:{r}deg">{img(n, c)}<figcaption>{c}</figcaption></figure>' for n, c, r in PRINTS)
    marq = "".join(f"<span>{x}</span>" for x in PRODUCTS * 2)
    chips = "".join(f"<li>{a}</li>" for a in AREAS)
    body = f'''
<section class="hero-full"><div class="hf-bg" data-parallax="0.12">{img("metal-roof-project", "Mountain home with a new standing seam and shingle roof by Exceptional Roofing", priority=True)}</div>
<div class="wrap"><div class="hf-row"><div><p class="label">Salt Lake City &middot; Park City &middot; Heber</p>
<h1>Roofing company in Salt Lake City <span>for every material.</span></h1>
<p class="lede">Exceptional Roofing is a roofing company in Salt Lake City for asphalt shingles, standing seam metal, copper, wood shake and flat TPO roofs: repairs, replacements and new roofs for homes and businesses, from the Salt Lake Valley to Park City and Heber.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Get a Free Estimate {ARROW}</a><a class="btn ghost" href="tel:{PHONES[0][2]}">{PHONE} {PHONES[0][1]}</a></div></div>
<aside class="hf-card"><small>Call or text</small><b>{PHONES[0][1]}</b><p>Estimator line, open from 6:30 AM on weekdays. Most quotes the same day or week.</p></aside></div></div>
<span class="scroll-cue">Scroll</span></section>
<div class="marquee" aria-label="Products we install"><div class="marquee-track">{marq}</div></div>

<section class="sec"><div class="wrap">
<p class="big-intro reveal-up">Most homes get shingles, and we install the good ones. But mountain homes, historic houses and flat commercial roofs need <em>something else</em>, and we do those too.</p>
<div class="stats" style="--stat-n:4"><div class="stat reveal-up"><b data-count="5">5</b><span>roofing systems, installed by one crew</span></div><div class="stat reveal-up"><b data-count="16">16</b><span>towns in our core service area</span></div>
<div class="stat reveal-up"><b>6:30</b><span>AM, when the phone lines open on weekdays</span></div><div class="stat reveal-up"><b data-count="3">3</b><span>states for larger and specialty roofs</span></div></div>
</div></section>

<section class="sec matsec"><div class="wrap">
<div class="head reveal-up"><p class="label">The sample board</p><h2>Pick a material.</h2><p class="lede">Every swatch is drawn from the real surface. Every photo is one of our roofs.</p></div>
<div class="matbox" data-swap-group><div class="mat-list">{sel}</div><div class="mat-view">{pics}</div></div>
</div></section>

<section class="sec sand"><div class="wrap">
<div class="head reveal-up"><p class="label">Services</p><h2>Repair to full replacement.</h2></div>
<div class="bento">{bento}</div>
<p class="more"><a class="tlink" href="@/services/">All services {ARROW}</a></p></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.18">{img("cedar-shake-detail", "")}</div><div class="wrap"><blockquote class="reveal-up">Roofing is <em>our passion.</em></blockquote><footer>Exceptional Roofing &middot; it&rsquo;s on the logo</footer></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Job file</p><h2>Our roofs, not stock photos.</h2></div>
<div class="prints">{prints}</div>
<div class="compare reveal-up"><div class="cmp-stage" data-compare>{img("chimney-cap-after", "New chimney cap and flashing, after")}<div class="cmp-before">{img("chimney-cap-before", "Rusted chimney cap, before")}</div><span class="cmp-handle" aria-hidden="true"></span>
<span class="cmp-tag l">Before</span><span class="cmp-tag r">After</span><input class="cmp-range" type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>
<div class="cmp-txt"><p class="label">Drag to compare</p><h3>A chimney cap, done properly.</h3><p>Chimney caps, flashing, trim, valleys and transitions are where roofs leak, and where a roof looks finished or not. Custom metal details are part of every job.</p><a class="tlink" href="@/gallery/">The full gallery {ARROW}</a></div></div>
</div></section>

<section class="split-photo dark-split"><div class="sp-img">{img("winter-new-build", "New construction roof in the snow")}</div><div class="sp-txt reveal-up">
<p class="label">Where we work</p><h2>The Salt Lake Valley, and up the canyons.</h2>
<p>Our core area runs from Salt Lake City and the east bench to Park City, Heber, Kamas, Oakley and Alta. For larger and specialty roofs we also review projects across Utah, southern Idaho and southwest Wyoming.</p>
<ul class="chips">{chips}</ul><p><a class="tlink light" href="@/service-areas/">Service areas {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal-up"><div class="fin"><p class="label">Financing</p><h3>Pay over time, through Acorn Finance.</h3><p>Pre-qualify online and review payment options before the work starts. Financing is provided by Acorn Finance and its lending partners.</p><a class="tlink" href="@/financing/">Financing {ARROW}</a></div>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company Salt Lake City | Exceptional Roofing", "body_class": "is-home",
            "meta": "Roofing company in Salt Lake City for asphalt, metal, copper, wood shake and flat TPO roofs: repair, replacement and new roofs. Free estimates, same week.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}
