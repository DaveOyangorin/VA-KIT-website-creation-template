"""Home (v3) for swiftrestoreutah.com: "From flood to finish".
Hero after Belfor (black ground, a flame-red diagonal slash, urgent heavy type) with a Paul Davis-style 24/7 phone panel and two
tilted job photos ("Day 1" drying, "Finished" bath). Signature: the pinned horizontal recovery timeline. Remodel half set in
Bluestem's editorial serif italics. Every photo is the client's own."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, AREAS, ST
from pagekit import ARROW, PHONE, HOME, cta
import p_blog

STAGES = [("00", "The call", "24/7, any hour", "A real person answers (385) 412-8633, day or night, and a crew heads out.", "swift-van"),
          ("01", "Extract &amp; dry", "Day 1", "Standing water out, then air movers, air scrubbers and dehumidifiers set to pull moisture out of the structure.", "dehumidifier-air-movers"),
          ("02", "Contain", "Days 1&ndash;3", "Plastic containment walls keep dust, spores and moisture out of the rest of the house.", "containment"),
          ("03", "Open it up", "Days 2&ndash;5", "Wet drywall, insulation and flooring come out so the framing can dry and nothing is hidden behind the wall.", "demo-bathroom"),
          ("04", "Rebuild", "Week 2 onward", "Framing, plumbing and new drywall. We&rsquo;re a general contractor, so the rebuild stays with the same crew.", "rebuild-bath"),
          ("05", "Finish", "The good part", "Tile, vanities, paint and floors. Often the room comes back better than it was before the water.", "finished-bath")]
RESTORE = [("services/water-damage-restoration/", "Water damage", "basement-drying"), ("services/flooded-basement-cleanup/", "Flooded basements", "demo-basement"), ("services/fire-damage-restoration/", "Fire &amp; smoke", "fire-kitchen-rebuilt"),
           ("services/ogden-mold-removal/", "Mold removal", "containment-bed"), ("services/ogden-sewage-cleanup/", "Sewage cleanup", "demo-open-wall"), ("services/leak-detection/", "Leak detection", "ceiling-leak")]
REMODEL = [("services/kitchen-remodeling/", "Kitchens", "kitchen-transformation"), ("services/bathroom-remodeling/", "Bathrooms", "finished-bath-2"), ("services/reconstruction/", "Reconstruction", "rebuild-bath-2"), ("services/general-contractor/", "General contracting", "after-remodel-2")]
CASES = [("case-studies/kaysville-basement-flood-emergency-storm-water-cleanup-and-mold-mitigation/", "Kaysville basement flood", "case-kaysville-flood"),
         ("case-studies/from-water-damage-to-full-remodel-a-kitchen-and-bathroom-reconstruction-in-hyrum-ut/", "Hyrum: water damage to full remodel", "case-hyrum"),
         ("case-studies/transforming-a-90s-basement-into-a-modern-family-space-in-layton-ut/", "Layton: a 90s basement, modernized", "case-layton-basement"),
         ("case-studies/full-sewage-cleanup-and-reconstruction-for-a-millcreek-utah-condo/", "Millcreek condo sewage cleanup", "case-millcreek")]
FAQ = [("Do you really answer at night?", "Yes. Emergency service is 24/7 from our Ogden office at (385) 412-8633. Water keeps spreading while you wait, so call as soon as you find it."),
       ("Can you help with my insurance claim?", "Yes. We document the damage and work with your insurance company through the claim, from the first moisture readings to the rebuild."),
       ("Do you do the rebuild too, or just the cleanup?", "Both. We&rsquo;re a licensed general contractor (license 4853926-5501), so the same company handles the drying, the tear-out, the rebuild and the finishes, and can remodel while the walls are open."),
       ("Which areas do you cover?", "Ogden and Weber and Davis counties: Layton, Kaysville, Farmington, Bountiful, North Salt Lake, Roy, Harrisville, Huntsville, West Haven, Plain City and up to Brigham City."),
       ("Can I finance the work?", "Yes. You can restore now and pay over time through Hearth, and see options before work starts.")]


def home(tip_cards):
    track = "".join(f'<article class="tl-card"><figure>{img(im, t)}</figure><div class="tl-txt"><span class="tl-n">{n}</span><small>{when}</small><h3>{t}</h3><p>{d}</p></div></article>' for n, t, when, d, im in STAGES)
    rest = "".join(f'<a class="rs-item reveal-up" href="@/{p}">{img(i, "")}<span>{t}</span><em>{ARROW}</em></a>' for p, t, i in RESTORE)
    remo = "".join(f'<a class="rm-item reveal-up" href="@/{p}">{img(i, "")}<span><i>{t}</i></span></a>' for p, t, i in REMODEL)
    cases = "".join(f'<a class="tile span-3 reveal-up" href="@/{p}">{img(i, "")}<span class="t-go">{ARROW}</span><span class="t-in"><small>Case study</small><b>{t}</b></span></a>' for p, t, i in CASES)
    tips = "".join(f'<a class="tip reveal-up" href="@/{p}"><span>{d or "Restoration tips"}</span><b>{t}</b></a>' for t, p, im, d in tip_cards[:4])
    marq = "".join(f"<span>{x}</span>" for x in ["24/7 emergency response", "Water damage", "Flooded basements", "Fire &amp; smoke", "Mold", "Sewage", "Rebuild", "Kitchens", "Bathrooms", "IICRC certified"] * 2)
    body = f'''
<section class="sw-hero"><div class="slash" aria-hidden="true"></div><div class="wrap sw-in">
<div class="sw-text"><p class="label">Ogden &middot; Weber &amp; Davis counties &middot; since 2009</p>
<h1>Water damage restoration in Ogden. <span>From flood <i>to finish.</i></span></h1>
<p class="lede">Swift Restoration and Remodeling does water damage restoration in Ogden around the clock: extraction, drying, mold and sewage cleanup, fire and smoke, and then the rebuild and remodel, with one local crew from the first call to the final finish.</p>
<div class="btn-row"><a class="btn accent" href="tel:{ST["tel"]}">{PHONE} Call {ST["phone"]}</a><a class="btn ghost" href="@/contact/">Get a Quote {ARROW}</a></div></div>
<div class="sw-art"><figure class="sw-p p1">{img("basement-drying", "Air movers drying a water-damaged basement in Ogden", priority=True)}<figcaption>Day 1 &middot; drying</figcaption></figure>
<figure class="sw-p p2">{img("finished-bath", "Finished bathroom after Swift rebuilt it")}<figcaption>Finished</figcaption></figure>
<div class="sw-phone"><small>24/7 emergency line</small><a href="tel:{ST["tel"]}">{ST["phone"]}</a><span>Licensed &middot; IICRC certified &middot; locally owned</span></div></div>
</div></section>
<div class="marquee" aria-label="What we do"><div class="marquee-track">{marq}</div></div>

<section class="hscroll" data-hscroll><div class="hs-pin"><div class="wrap hs-head"><p class="label">The recovery timeline</p><h2>What happens after <i>you call.</i></h2><div class="hs-bar"><span></span></div></div>
<div class="hs-track">{track}<article class="tl-card tl-end"><div class="tl-txt"><h3>That&rsquo;s the whole job.</h3><p>Water, fire or mold today. A finished room at the end. One company the whole way.</p><a class="btn accent" href="tel:{ST["tel"]}">{PHONE} {ST["phone"]}</a></div></article></div></div></section>

<section class="sec duo"><div class="wrap duo-in">
<div class="restore reveal-up"><p class="label">Restoration &middot; 24/7</p><h2>When it&rsquo;s an emergency.</h2><div class="rs-list">{rest}</div><p><a class="tlink light" href="@/services/restoration-services/">All restoration services {ARROW}</a></p></div>
<div class="remodel reveal-up"><p class="label">Remodeling</p><h2>When it&rsquo;s <i>a fresh start.</i></h2><p>Plenty of our remodels start as water damage. If the walls are already open, it&rsquo;s the best time to change the room.</p><div class="rm-grid">{remo}</div><p><a class="tlink" href="@/services/remodeling-services/">Remodeling {ARROW}</a></p></div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:center">
<div class="compare reveal-up"><div class="cmp-stage" data-compare>{img("after-remodel", "Bedroom after the remodel")}<div class="cmp-before">{img("before-remodel", "The same bedroom before the remodel")}</div><span class="cmp-handle" aria-hidden="true"></span><span class="cmp-tag l">Before</span><span class="cmp-tag r">After</span><input class="cmp-range" type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div></div>
<div class="reveal-up"><p class="label">Drag to compare</p><h2>Same room. <i>New life.</i></h2><p>Bare walls and old floors before; a finished bedroom after. Restoration gets the house dry and safe. Remodeling is what makes it feel like home again.</p><a class="tlink" href="@/case-studies/">See our work {ARROW}</a></div>
</div></section>

<section class="sec sand"><div class="wrap"><div class="head reveal-up"><p class="label">Our work</p><h2>Jobs from across <i>Northern Utah.</i></h2></div><div class="bento">{cases}</div></div></section>

<section class="split-photo dark-split"><div class="sp-img">{img("darin-jenks", "Darin Jenks of Swift Restoration and Remodeling")}</div><div class="sp-txt reveal-up">
<p class="label">Locally owned</p><h2>Ogden&rsquo;s neighbors since 2009.</h2>
<p>Swift Restoration and Remodeling is locally owned and operated in Ogden, with over 13 years in restoration and over 30 years in construction. Our office is on Pennsylvania Avenue, and our crews work across Weber and Davis counties.</p>
<ul class="chips">{"".join(f"<li>{a}</li>" for a in AREAS)}</ul><p><a class="tlink light" href="@/about-us/">About us {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}</div>
<div class="reveal-up"><p class="label">Restoration tips</p><h2>From our blog.</h2><div class="tips">{tips}</div>
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label">New</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Water Damage Restoration Ogden UT | Swift Restoration 24/7", "body_class": "is-home",
            "meta": "Water damage restoration in Ogden, 24/7: extraction, drying, mold, sewage and fire cleanup, then the rebuild and remodel, from a locally owned crew since 2009.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
