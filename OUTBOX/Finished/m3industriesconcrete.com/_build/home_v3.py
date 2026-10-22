"""Premium home (v3) for m3industriesconcrete.com: "From red dirt to finished slab".
References (screenshotted 20 Oct 2026): Holcim (photo-tiled grid, dark), The Concrete Collective (photo hero, serif, dark
services band), Hilti (industrial tiles, one hard accent). Signature: the exploded slab. As you scroll, a cross-section of a
slab separates into its layers (native red dirt, compacted base, steel, concrete, finish and seal) and each layer shows the
client's own job photo and the client's own words about it."""
import html
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U
from pagekit import ARROW, PHONE, HOME, cta, form
import p_blog

LAYERS = [("ground", "Native ground", "Red dirt, graded", "Every project starts with proper grading, compaction, and base preparation.", "m3-foundation-forms", "A graded red-dirt site with a new foundation and excavators"),
          ("base", "Compacted base", "Where jobs are won", "We don&rsquo;t cut corners underground. That&rsquo;s what separates a 5-year concrete job from a 30-year one.", "m3-sidewalk-forms", "Forms set and base prepared for a sidewalk"),
          ("steel", "Steel reinforcement", "The backbone", "We use rebar and wire mesh where needed to give your concrete the structural backbone to resist cracking, shifting, and heavy loads.", "m3-footing", "Rebar set in footing forms along a building"),
          ("pour", "The pour", "Quality mix, honest pour", "We use the right concrete mix for the application. No watering down, no shortcuts. Every yard of concrete is placed with care.", "m3-pour-crew", "M3 Industries crew placing and screeding concrete"),
          ("finish", "Finish &amp; seal", "Straight edges, proper joints", "Straight edges, consistent textures, and proper control joints. The finished look matters just as much as what&rsquo;s underneath.", "m3-stained-driveway", "A finished, stained concrete driveway")]
SVCS = [("concrete-driveway-patio/", "Driveways &amp; patios", "m3-driveway-cones"), ("retaining-walls/", "Retaining walls", "m3-retaining-wall"), ("stamped-decorative-concrete/", "Stamped &amp; decorative", "m3-stained-steps"),
        ("concrete-pads-slabs/", "Pads &amp; slabs", "m3-slab-flag"), ("concrete-foundations/", "Foundations", "m3-foundation-wall"), ("concrete-coatings-st-george/", "Coatings &amp; sealing", "m3-stained-driveway"),
        ("concrete-sidewalks-walkways/", "Sidewalks &amp; walkways", "m3-sidewalk-forms"), ("concrete-cleaning-st-george/", "Concrete cleaning", "m3-driveway-side")]
REVIEWS = [("Merrill and his crew were awesome to work with and did an excellent job on a couple of projects I had them do. I couldn&rsquo;t be happier and strongly recommend them for any concrete needs you may have.", "Scott Later"),
           ("M3 put in a concrete guest parking driveway for us. They did a great job. Neighbors have complimented on the appearance, especially the flat top curb. Would recommend M3 Industries for any hard surface projects.", "Tom Penne"),
           ("Seriously the best company I have worked with! Very prompt scheduling with fair pricing. Communicated well through the whole process. Exceptional crew.!! Will definitely use them again for future projects!!", "Amy Adams")]
FAQ = [("Do you provide free estimates?", "Yes. Contact us online or call (435) 701-0081 to schedule a free, no-obligation quote."),
       ("What areas do you serve?", "We serve St. George, Washington, Santa Clara, Ivins, Hurricane, and surrounding Southern Utah communities."),
       ("Are you licensed and insured?", "Yes, M3 Industries is fully licensed and insured in the State of Utah."),
       ("How far in advance should I schedule?", "Spring and summer fill quickly, so contact us a few weeks in advance when possible."),
       ("Do you handle demolition or removal of old concrete?", "Yes, we can remove existing concrete before installation.")]


def slab_svg():
    return '''<svg class="xslab" viewBox="0 0 520 440" aria-hidden="true">
<g class="ly ly-ground" data-l="ground"><path class="ft" d="M60 330 L260 410 L460 330 L260 250Z"/><path class="sd" d="M60 330 L260 410 L260 432 L60 352Z"/><path class="sd2" d="M460 330 L260 410 L260 432 L460 352Z"/></g>
<g class="ly ly-base" data-l="base"><path class="ft" d="M70 300 L260 376 L450 300 L260 224Z"/><path class="sd" d="M70 300 L260 376 L260 394 L70 318Z"/><path class="sd2" d="M450 300 L260 376 L260 394 L450 318Z"/><g class="dots"><circle cx="200" cy="300" r="3"/><circle cx="260" cy="280" r="3"/><circle cx="320" cy="304" r="3"/><circle cx="240" cy="330" r="3"/><circle cx="300" cy="260" r="3"/><circle cx="350" cy="290" r="3"/><circle cx="180" cy="280" r="3"/></g></g>
<g class="ly ly-steel" data-l="steel"><path class="grid" d="M110 270 L260 330 M140 258 L290 318 M170 246 L320 306 M200 234 L350 294 M230 222 L380 282 M260 210 L410 270 M110 270 L260 210 M140 282 L290 222 M170 294 L320 234 M200 306 L350 246 M230 318 L380 258 M260 330 L410 270"/></g>
<g class="ly ly-pour" data-l="pour"><path class="ft" d="M80 230 L260 302 L440 230 L260 158Z"/><path class="sd" d="M80 230 L260 302 L260 336 L80 264Z"/><path class="sd2" d="M440 230 L260 302 L260 336 L440 264Z"/></g>
<g class="ly ly-finish" data-l="finish"><path class="ft" d="M80 170 L260 242 L440 170 L260 98Z"/><path class="jt" d="M170 134 L350 206 M170 206 L350 134"/><g class="beads"><circle cx="230" cy="160" r="5"/><circle cx="250" cy="172" r="4"/><circle cx="290" cy="150" r="5"/><circle cx="310" cy="176" r="3.5"/></g></g>
</svg>'''


def home(cards):
    steps = "".join(f'<div class="step" data-step="{k}"><p class="s-n">Layer {i + 1} of 5 &middot; {t}</p><h3>{sub}</h3><p>{d}</p></div>' for i, (k, t, sub, d, im, a) in enumerate(LAYERS))
    frames = "".join(f'<figure class="lframe{" show" if i == 0 else ""}" data-show="{k}">{img(im, a)}<figcaption>{t}</figcaption></figure>' for i, (k, t, sub, d, im, a) in enumerate(LAYERS))
    tiles = "".join(f'<a class="sv reveal-up" href="@/{p}">{img(im, "")}<b>{t}</b><em>{ARROW}</em></a>' for p, t, im in SVCS)
    revs = "".join(f'<blockquote class="rv reveal-up"><p>&ldquo;{t}&rdquo;</p><footer>{n} &middot; St. George, UT</footer></blockquote>' for t, n in REVIEWS)
    posts = "".join(f'<a class="post-card reveal-up" href="@/{p}">{img(im, "")}<b>{html.escape(t)}</b><em>Read {ARROW}</em></a>' for t, p, im in cards[:3])
    body = f'''
<section class="m3-hero"><div class="mh-bg" data-parallax="0.1">{img("m3-pour-crew", "M3 Industries crew placing concrete on a St. George job", priority=True)}</div>
<div class="wrap mh-grid"><div><p class="label">Southern Utah concrete &middot; licensed &amp; insured</p>
<h1>Concrete coatings and concrete work in St. George, <span>poured right from the dirt up.</span></h1>
<p class="lede">M3 Industries is a St. George concrete contractor for driveways, patios, stamped concrete, retaining walls, pads, foundations, and concrete coatings and sealing. Locally owned, serving all of Washington County, with free estimates.</p>
<div class="btn-row"><a class="btn accent" href="@/inquiry-services-page/">Request a Free Estimate {ARROW}</a><a class="btn ghost" href="tel:+14357010081">{PHONE} (435) 701-0081</a></div></div>
<div class="mh-stamp"><b>20+</b><span>years of hands-on concrete experience</span></div></div></section>
<div class="marquee m3m" aria-label="Services"><div class="marquee-track">{"".join(f"<span>{t}</span>" for t in ["Driveways", "Patios", "Stamped", "Retaining walls", "RV pads", "Foundations", "Coatings", "Sealing", "Sidewalks"] * 2)}</div></div>

<section class="sec layer-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">What&rsquo;s under the surface</p><h2>A slab is five layers. <span>Four of them you&rsquo;ll never see.</span></h2></div>
<div class="layers" data-layers><div class="l-vis">{slab_svg()}<div class="lframes">{frames}</div></div><div class="l-steps">{steps}</div></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head split-head reveal-up"><div><p class="label">What we do</p><h2>Every phase, <span>new pours to protective coatings.</span></h2></div><p>From new pours to protective coatings, M3 Industries handles every phase of your concrete project. On time and on budget.</p></div>
<div class="svgrid">{tiles}</div></div></section>

<section class="sec work-sec"><div class="wrap"><div class="head reveal-up"><p class="label">Our work</p><h2>Concrete projects <span>across Southern Utah.</span></h2></div>
<div class="wgrid">{"".join(f'<figure class="wf reveal-up">{img(n, "M3 Industries concrete job in St. George")}</figure>' for n in ["m3-slab-house", "m3-driveway-curve", "m3-screed", "m3-stained-steps", "m3-slab-home", "m3-foundation-wall"])}</div></div></section>

<section class="sec rv-sec"><div class="wrap"><div class="head reveal-up"><p class="label">What customers say</p><h2>Straight edges. <span>Straight answers.</span></h2></div><div class="rvs">{revs}</div></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Get a free estimate", msg_label="Tell us about your project")}<p class="small">Or call <a href="tel:+14357010081">(435) 701-0081</a>.</p></div>
</div></section>

<section class="sec"><div class="wrap"><div class="head reveal-up"><p class="label">From the blog</p><h2>Concrete in Southern Utah, <span>explained.</span></h2></div><div class="posts">{posts}</div></div></section>
''' + cta()
    return {"path": "", "canonical": "https://www.m3industriesconcrete.com", "title": "Concrete Coatings & Concrete Contractor St. George, UT | M3", "og": "m3-pour-crew",
            "meta": "Concrete coatings and concrete work in St. George, UT: driveways, patios, stamped concrete, retaining walls, pads and foundations. Licensed and insured. Free estimates.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
