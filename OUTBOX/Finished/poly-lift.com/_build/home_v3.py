"""Premium home (v3) for poly-lift.com: "Back to level".
References (screenshotted 20 Oct 2026): Hilti (industrial product tiles, one hard accent), Magnum Piering (their pier supplier:
engineering blue, tinted product photos), Ram Jack (dark, bold foundation brand). Signature: the interactive lift. Drag (or
press Inject) and foam fills the void under a sunken slab; the slab rises and the spirit-level bubble centers. It is a diagram
of the method the client describes (Deep Foamjection), not a measurement."""
import html
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U
from pagekit import ARROW, PHONE, HOME, cta, form
import p_blog

SPEC = [("concrete-leveling-and-lifting/", "Concrete raising", "Deep Foamjection lifts driveways, sidewalks, stairs and garage floors. Repaired areas are ready within minutes.", "pl-raising-concrete-with-trailer-in-background-1150-ox8pj158xij"),
        ("foundation-repair/", "Foundation repair", "Push piers and helical piles, with Magnum Piering, to stop a settling house and lift it back.", "pl-utah-university-piering-project-1"),
        ("concrete-sealing/", "Concrete sealing", "A finish after we raise and level, against frost heave, salt and ice in winter.", "pl-man-spraying-concrete-sealing-finsih-to-driveway-oxdlvoqcufm"),
        ("injection-foam-insulation/", "Core Foam Masonry Foam Insulation&reg;", "Foam-in-place insulation for concrete block walls.", "pl-core-foam-mansonry-insulation-1")]
GARAGE = [(f"pl-lifted-garage-poly-lift-{n}", f"Lifted garage, photo {n} of 5") for n in range(1, 6)]
FAQ = [("How much does concrete lifting cost?", "Usually around 50% or less than replacing."), ("How long does it take to lift concrete?", "Most jobs can be done in less than 1 day and ready to use immediately."),
       ("What causes concrete to sink or become uneven?", "Bad compaction, freeze thaw from winter, poor drainage."), ("Can cracked concrete be leveled?", "Cracked concrete can be leveled."),
       ("Can you live in a house during foundation repair?", "Yes, you can continue to live in your home while the foundation is being repaired.")]


def lift():
    return '''<div class="lift" data-lift>
<div class="lv" aria-hidden="true"><span class="lv-b"></span><i></i><i></i></div>
<svg class="lift-svg" viewBox="0 0 800 380" role="img" aria-label="Diagram: foam injected under a sunken concrete slab lifts it back to level">
<defs><pattern id="soil" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="4" cy="5" r="1.4" class="sd"/><circle cx="12" cy="12" r="1" class="sd"/></pattern></defs>
<rect x="0" y="150" width="800" height="230" class="soil"/><rect x="0" y="150" width="800" height="230" fill="url(#soil)"/>
<path class="lyr" d="M0 250 Q200 240 400 252 T800 246"/><path class="lyr" d="M0 320 Q220 312 420 324 T800 318"/>
<g class="foam-g"><path class="foam" d="M120 152 C 90 175, 110 230, 190 236 C 270 244, 360 228, 420 214 C 470 200, 480 160, 440 152 Z"/><path class="foam f2" d="M190 236 C 220 270, 300 268, 340 236" /></g>
<path class="void" d="M120 152 L560 152 L120 176 Z"/>
<g class="slab-g"><rect x="110" y="110" width="460" height="42" class="slab"/><path class="crack" d="M330 110 l6 14 -4 10 6 18"/></g>
<rect x="570" y="110" width="200" height="42" class="slab ok"/>
<g class="gun"><rect x="200" y="34" width="16" height="60" rx="3"/><rect x="186" y="24" width="44" height="16" rx="4"/><path d="M208 94 V150" class="tube"/></g>
<text x="18" y="140" class="tg">SLAB</text><text x="18" y="200" class="tg">VOID</text><text x="18" y="272" class="tg">BASE / SOIL</text><text x="590" y="100" class="tg">LEVEL REFERENCE</text>
</svg>
<div class="lift-ctl"><button type="button" class="btn accent" data-inject>Inject foam</button><input type="range" min="0" max="100" value="0" aria-label="Foam injected, from none to fully lifted"><span class="lift-read" aria-live="polite">Out of level</span></div>
</div>'''


def home(cards):
    spec = "".join(f'<a class="sp reveal-up" href="@/{p}">{img(im, "")}<span class="sp-in"><b>{t}</b><span>{d}</span><em>Learn more {ARROW}</em></span></a>' for p, t, d, im in SPEC)
    gar = "".join(f'<figure class="gs reveal-up"><span class="gs-n">{i + 1:02d}</span>{img(im, c)}<figcaption>{c}</figcaption></figure>' for i, (im, c) in enumerate(GARAGE))
    posts = "".join(f'<a class="post-card reveal-up" href="@/{p}">{img(im, "")}<b>{html.escape(t)}</b><em>Read {ARROW}</em></a>' for t, p, im in cards[:4])
    body = f'''
<section class="pl-hero"><div class="ph-bg" data-parallax="0.1">{img("pl-raising-concrete-with-trailer-in-background-1150-ox8pj158xij", "Poly-Lift crew raising a concrete sidewalk with the Poly-Lift trailer behind them", priority=True)}</div>
<div class="wrap ph-grid"><div><p class="label">Logan &middot; Cache Valley &middot; Davis County</p>
<h1>Concrete lifting in Logan, <span>with foam, not a jackhammer.</span></h1>
<p class="lede">Poly-Lift does concrete lifting in Logan and across Utah with Deep Foamjection, a polyurethane foam injected under sunken slabs. It is quicker and less expensive than replacing, and repaired areas are ready within minutes. For houses, we install push piers and helical piles.</p>
<div class="btn-row"><a class="btn accent" href="@/contact/">Get a Free Estimate {ARROW}</a><a class="btn ghost" href="tel:+14359999309">{PHONE} (435) 999-9309</a></div></div>
<aside class="ph-card"><b>Less than a day</b><span>Most concrete lifting jobs, ready to use immediately.</span><b>15&ndash;25&times; lighter</b><span>HMI foam, on average, compared with a traditional mud jacking or grout mix.</span></aside></div></section>

<section class="sec lift-sec"><div class="wrap lift-grid">
<div><p class="label">How Deep Foamjection works</p><h2>Fill the void. <span>Lift the slab.</span></h2>
<p>Concrete sinks when the base under it washes out, was never compacted properly, or heaves and settles through freeze and thaw. We drill small holes, inject foam through them, and the foam fills the void and expands, lifting the slab back toward level.</p>
<p>Unlike mud jacking with grout, the material is light, the holes are small and the clean-up is minimal. Press <b>Inject foam</b>, or drag the slider.</p>
<p><a class="tlink" href="@/polyurethane-foam-concrete-lifting/">How effective is polyurethane foam? {ARROW}</a></p></div>
{lift()}
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Our specialties</p><h2>Got concrete problems? <span>We&rsquo;ve got you covered.</span></h2></div>
<div class="specs">{spec}</div></div></section>

<section class="sec case-sec"><div class="wrap">
<div class="head split-head reveal-up"><div><p class="label">Completed project &middot; Utah State University</p><h2>Piering a campus building, <span>bay by bay.</span></h2></div>
<p>Push piers set along the foundation walls inside a Utah State University building, with the floor opened up to reach the footings. We have also worked at the Utah stadium and Weber State University.</p></div>
<div class="case-strip">{"".join(f'<figure class="cs">{img(f"pl-utah-university-piering-project-{n}", "Push pier installation at Utah State University")}</figure>' for n in (3, 6, 1, 7, 5))}</div>
<p><a class="tlink light" href="@/completed-projects/">All completed projects {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">A lifted garage</p><h2>A garage lifted <span>on piers.</span></h2></div>
<div class="gsteps">{gar}</div></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.15">{img("pl-utah-stadium", "")}</div><div class="wrap"><blockquote class="reveal-up">Every time you choose to raise rather than replace, <span>you are saving landfills from massive concrete slabs.</span></blockquote><footer>From how we work &middot; <a href="@/concrete-leveling-and-lifting/">Concrete leveling and lifting</a></footer></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Straight answers.</h2>{faq_html(FAQ)}<p><a class="tlink" href="@/faqs/">All FAQs {ARROW}</a></p></div>
<div class="reveal-up"><div class="locs"><div class="loc"><span class="label">Cache location</span><a class="lp" href="tel:+14359999309">(435) 999-9309</a><span>PolyLiftUtah@gmail.com</span></div><div class="loc"><span class="label">Weber location</span><a class="lp" href="tel:+18015305617">(801) 530-5617</a><span>PolyLiftWeber@gmail.com</span></div></div>
<div class="form-col">{form("Request a free estimate", msg_label="What needs lifting or repairing?")}</div></div>
</div></section>

<section class="sec"><div class="wrap"><div class="head reveal-up"><p class="label">From the blog</p><h2>Concrete and foundations, <span>explained.</span></h2></div><div class="posts">{posts}</div></div></section>
''' + cta()
    return {"path": "", "canonical": "https://www.poly-lift.com/", "title": "Concrete Lifting in Logan, UT | Poly-Lift Foam Lifting & Piering", "og": "pl-poly-lift-crewman-injecting-deepfoam-into-concrete-walkway",
            "meta": "Concrete lifting in Logan, UT with Deep Foamjection polyurethane foam: driveways, sidewalks and garage floors ready in minutes. Push piers and helical piles too.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
