"""Home for armour-crete.com: "Sealed for the desert". All copy is the client's own (condensed); drawings are original."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, AREAS, PHONES, EMAIL
from pagekit import ARROW, PHONE, HOME, cta
from illus import texture, slab, SERVICES
import p_blog

STORY = [("moves", "01", "It moves.", "Concrete expands and contracts with temperature: roughly 5.5 millionths of an inch, per inch, per degree. Swing a 50-foot driveway 100&deg;F between a January night and a July afternoon and that is about a third of an inch of movement. Stress opens hairline cracks; control joints exist to choose where."),
         ("drinks", "02", "It drinks.", "Concrete is porous. Water wicks into the capillary pores and down every crack the movement just opened, and it carries whatever is dissolved in it: salt off the pool, salt out of the softener, salt already in the soil and the hard water."),
         ("breaks", "03", "Then it breaks from the inside.", "Water expands about nine percent when it freezes, and southern Utah nights do drop below freezing. Salt does the same job without the cold: as water evaporates it crystallises, and crystals growing in a confined pore lift the surface off. Scaling, spalling and efflorescence are all the same story."),
         ("sealed", "04", "Sealing starves it.", "Sealing doesn&rsquo;t stop concrete moving. Nothing does. It keeps the pore network from staying saturated, which starves freeze&ndash;thaw and salt crystallisation of the one thing they both need.")]
STEPS = [("Clean", "The slab gets cleaned end to end. Nothing goes down over dirt."), ("Dry", "We wait for it to dry completely. Sealer over moisture is how finishes fail."),
         ("Seal", "Deco product, matched to the surface and its exposure, put down early before the slab takes the day&rsquo;s heat."), ("Cure", "Twenty-four hours before you walk or drive on it. Then it&rsquo;s yours again.")]
PRODUCTS = [("DECO 20 Clear", "Reactive penetrating sealer. Dries 100% transparent, no film."), ("Salt Shield 303", "Penetrating, for pool decks and salt. Doesn&rsquo;t change slip resistance."),
            ("SilaCast BES", "The ICC-approved foundation membrane, for certified applicators."), ("Shine-A-Cast", "High-shine decorative finish."), ("TravaCast", "For travertine and pavers."), ("Bio Blacktop", "Natural oil for asphalt. No asphalt, no tar.")]
FAQ = [("How long before I can walk or drive on it?", "Twenty-four hours. That&rsquo;s the real number. Plan for one day without the surface and you won&rsquo;t be caught out."),
       ("How often does it need doing again?", "It depends on the product and how hard the surface gets used; a shaded patio and a west-facing driveway wear very differently. Our maintenance program runs on a two-year cycle, or just call us when it looks tired."),
       ("Will it make the surface slippery?", "Not on pool decks: Salt Shield 303 soaks in and dries clear with no film, and the manufacturer states it doesn&rsquo;t change skid or slip resistance. High-shine finishes do leave a layer, so we talk that through at the assessment."),
       ("Can you seal brand-new concrete?", "Not immediately. Fresh concrete has to cure and give up its moisture first. If you&rsquo;re mid-build, talk to us at the pour and we&rsquo;ll schedule it."),
       ("What does it cost?", "It depends on the surface, its condition, the prep and the finish, so any number before someone has looked at it is a guess. The on-site assessment is free, with no obligation.")]


def home():
    frames = "".join(f'<div class="sframe{" show" if i == 0 else ""}" data-show="{k}">{slab(k, "hs-" + k)}</div>' for i, (k, n, t, d) in enumerate(STORY))
    steps = "".join(f'<div class="step" data-step="{k}"><p class="s-n">{n} / 04</p><h3>{t}</h3><p>{d}</p></div>' for k, n, t, d in STORY)
    tiles = "".join(f'<a class="ftile reveal-up" href="@/{p}"><span class="ft-tex">{texture(tx, "h-" + tx)}</span><span class="ft-in"><b>{lab}</b><span>{d}</span><em>{ARROW}</em></span></a>' for p, lab, tx, d in SERVICES)
    procs = "".join(f'<li class="reveal-up"><span>{i:02d}</span><b>{t}</b><p>{d}</p></li>' for i, (t, d) in enumerate(STEPS, 1))
    prods = "".join(f'<li class="reveal-up"><b>{n}</b><span>{d}</span></li>' for n, d in PRODUCTS)
    marq = "".join(f"<span>{n}</span>" for n, d in PRODUCTS * 2)
    form = f'''<form class="form" method="post" action="" id="assessment-form"><h3>Request an assessment</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="row"><label for="f-email">Email<input id="f-email" type="email" name="email" autocomplete="email"></label><label for="f-area">Area / neighborhood<input id="f-area" name="area"></label></div>
<label for="f-surf">Surface<select id="f-surf" name="surface"><option>Driveway</option><option>Patio or walkway</option><option>Pool deck</option><option>Garage floor</option><option>Expansion joints</option><option>Asphalt</option><option>Foundation (new build)</option></select></label>
<label for="f-msg">Anything we should know?<textarea id="f-msg" name="message"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''
    body = f'''
<section class="hero-full ac-hero"><div class="hf-bg" data-parallax="0.12">{img("snow-canyon-slickrock", "Red sandstone slickrock in Snow Canyon State Park near St. George", priority=True)}</div>
<div class="wrap"><div class="hf-row"><div><p class="label">St. George &middot; Washington County, Utah</p>
<h1>Concrete sealing in St. George, <em>made for the desert.</em></h1>
<p class="lede">Armour Crete does concrete sealing in St. George and across Washington County: driveways, patios and garage floors, wet-look and decorative finishes, pool decks against salt, expansion joints and asphalt, plus foundation waterproofing for builders. Certified Deco applicator; free on-site assessment.</p>
<div class="btn-row"><a class="btn accent" href="#assessment">Free Assessment {ARROW}</a><a class="btn ghost" href="tel:{PHONES[0][2]}">{PHONE} {PHONES[0][1]}</a></div></div>
<aside class="hf-card"><small>The honest answer</small><b>24 hours.</b><p>That&rsquo;s how long you&rsquo;re off the driveway. We&rsquo;d rather tell you up front.</p></aside></div></div><span class="scroll-cue">Scroll</span></section>
<div class="marquee dark" aria-label="Deco products we apply"><div class="marquee-track">{marq}</div></div>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Why concrete fails here</p><h2>Concrete does not crack <em>because it is weak.</em></h2></div>
<div class="story"><div class="story-visual"><figure class="sheet slabs">{frames}</figure></div><div class="story-steps">{steps}</div></div>
</div></section>

<section class="sec dark finishes"><div class="wrap">
<div class="head reveal-up"><p class="label">What we seal</p><h2>Every way concrete fails here. <em>We handle all of them.</em></h2></div>
<div class="ftiles">{tiles}</div></div></section>

<section class="sec"><div class="wrap">
<div class="split" style="align-items:start"><div class="reveal-up"><p class="label">The process</p><h2>Four steps. <em>No shortcuts.</em></h2><p>In southern Utah the timing is most of the job: sealer goes down early in the morning, before the slab has taken on the day&rsquo;s heat. On a hot surface it flash-dries and leaves whiting and streaks.</p>
<div class="big24"><b data-count="24">24</b><span>hours until you can walk or drive on it</span></div></div>
<ol class="procs">{procs}</ol></div></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.18">{img("snow-canyon-dunes", "")}</div><div class="wrap"><blockquote class="reveal-up">We come back <em>every two years.</em></blockquote><footer>Sealer isn&rsquo;t permanent. On a two-year cycle we clean it and put a fresh coat down, so the slab never gets far enough gone to need restoring.</footer></div></section>

<section class="sec sand"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Products</p><h2>Deco only. <em>Nothing off the truck.</em></h2><p>Deco Products has manufactured in Denver since 1991, water-based and solvent-free from the start. As a certified Deco applicator we can put down the restricted products, including the ICC-approved foundation membrane.</p><a class="tlink" href="@/products/">The products {ARROW}</a></div>
<ul class="prods">{prods}</ul></div></section>

<section class="split-photo ac-split"><div class="sp-img">{img("color-country", "Red rock country in southern Utah")}</div><div class="sp-txt reveal-up">
<p class="label">Homes &amp; builders</p><h2>Driveways, patios, pool decks. <em>And waterproofing, on your calendar.</em></h2>
<p>For homeowners: a private assessment on site, a clear scope, and a finish chosen for how the property actually gets used. For builders: foundation waterproofing and damp proofing for new construction, plus HOA, commercial and municipal flatwork, scheduled to the build.</p>
<ul class="chips">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul><p><a class="tlink light" href="@/contractors/">For contractors {ARROW}</a></p></div></section>

<section class="sec" id="assessment"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up"><p class="label">Free on-site assessment</p><h2>We come out and look.</h2><p>Call Dylan at <a href="tel:{PHONES[0][2]}">{PHONES[0][1]}</a> or Zac at <a href="tel:{PHONES[1][2]}">{PHONES[1][1]}</a>, email <a href="mailto:{EMAIL}">{EMAIL}</a>, or send the form.</p>{form}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Concrete Sealing St. George, UT | Driveway Sealer | Armour Crete", "body_class": "is-home",
            "meta": "Concrete sealing in St. George and Washington County: driveways, wet-look finishes, pool decks, expansion joints and foundation waterproofing. Free assessment.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
