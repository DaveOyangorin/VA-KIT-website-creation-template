"""Premium home (v3) for cleartopsolutions.shop: "Where's the water?".
References (screenshotted 20 Oct 2026): FirstOnsite (navy, safety-orange urgent bar), Hippo (calm home-centred clarity),
Flo (sky gradient, floating cards). Signature: the interactive blueprint cutaway in the hero (tap the room where the water
is to get the right service), plus the 48-hour drying dial (EPA). No reviews, no photos of the client's own: the site leans on
drawings, plain words and the 24/7 line."""
import html, re
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U, ST, EMAIL
from pagekit import ARROW, PHONE, HOME, cta, form
from illus import house, clock48, ZONES
import p_blog

EPA = "https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home"
SPOTS = {  # zone -> (title, client's own one-liner, [(label, path)])
    "attic": ("Attic", "Attic Mold Remediation is the process of identifying, removing, and preventing mold growth in the attic space of homes in St. George.", [("Attic mold remediation", "services/attic-mold-remediation/")]),
    "bath": ("Bathroom", "Toilet Overflow Cleanup addresses and resolves the issues arising from toilet overflows. Sewage cleanup removes contaminated wastewater and restores affected areas to ensure safety and hygiene.", [("Toilet overflow cleanup", "services/toilet-overflow-cleanup/"), ("Sewage cleanup", "services/sewage-cleanup/")]),
    "ceiling": ("Ceiling &amp; leaks", "Ceiling Water Damage Repair involves the assessment and restoration of ceilings affected by water intrusion, ensuring safety and structural integrity.", [("Ceiling water damage repair", "services/ceiling-water-damage-repair/"), ("Water leak restoration", "services/water-leak-restoration/")]),
    "kitchen": ("Kitchen", "Kitchen Water Damage Repair involves the assessment and restoration of water-damaged areas in your kitchen, ensuring safety and functionality.", [("Kitchen water damage repair", "services/kitchen-water-damage-repair/"), ("Emergency water removal", "services/emergency-water-removal/")]),
    "basement": ("Basement", "Basement Flood Cleanup is the professional process of removing water from a flooded basement and restoring the area to a safe and dry condition.", [("Basement flood cleanup", "services/basement-flood-cleanup/"), ("Water extraction", "services/water-extraction/"), ("Flood restoration", "services/flood-restoration-services/")]),
    "crawl": ("Crawl space", "Crawl Space Mold Removal is the process of identifying, treating, and eliminating mold growth in the crawl spaces of homes to ensure a safe living environment.", [("Crawl space mold removal", "services/crawl-space-mold-removal/"), ("Mold remediation after water damage", "services/mold-remediation-after-water-damage/")]),
}
STEPS = [("0h", "Call us anytime", "Reach our 24/7 hotline. Our team responds quickly and helps you schedule water damage restoration or emergency repair."),
         ("first hours", "Assess &amp; remove the water", "We inspect the property to identify the source and extent of the damage, then extract standing water with pumps and vacuums."),
         ("24&ndash;48h", "Dry &amp; dehumidify", "Drying equipment goes in so every affected area is thoroughly dried, inside the window the EPA gives for preventing mold."),
         ("done", "Final inspection", "We check that your property is dry and safe, and confirm everything meets your expectations before we leave.")]
FAQ = [("How quickly should I call for water extraction services?", "You should contact us immediately when you notice water damage to minimize potential damage and mold growth."),
       ("What should I do while waiting for your team to arrive?", "Try to minimize further damage by turning off power to affected areas, but avoid handling electrical appliances yourself."),
       ("Will you help with insurance claims?", "Yes, we assist you with documentation and communication with your insurance provider to facilitate your claim."),
       ("What does water damage restoration cost?", "Costs can vary based on the extent of the damage. We assess the situation on-site, explain what&rsquo;s needed in plain language, and provide an upfront estimate before work begins.")]
CITIES = [("St. George", "st-george/", "virgin-river"), ("Washington", "washington/", "summer-storm"), ("Santa Clara", "santa-clara/", "zion-storm"), ("Ivins", "ivins/", "rain-glass")]


def home():
    spots = ""
    for z, (t, d, links) in SPOTS.items():
        x, y = ZONES[z][1]
        spots += f'<button type="button" class="hs" data-z="{z}" style="left:{x / 8:.2f}%;top:{y / 6:.2f}%" aria-label="Water in the {html.unescape(t).lower()}"><span></span></button>'
    panels = "".join(f'<div class="hp" data-z="{z}"{"" if i == 0 else " hidden"}><p class="label">{t}</p><p>{d}</p><div class="hp-links">' +
                     "".join(f'<a href="@/{p}">{l} {ARROW}</a>' for l, p in links) + "</div></div>" for i, (z, (t, d, links)) in enumerate(SPOTS.items()))
    tiles = "".join(f'''<a class="zt reveal-up" href="@/{SPOTS[z][2][0][1]}"><span class="zt-art">{house(z, uid="zt" + z, crop=True)}</span><span class="zt-in"><b>{SPOTS[z][0]}</b><span>{" &middot; ".join(l for l, p in SPOTS[z][2])}</span></span></a>''' for z in ("basement", "bath", "ceiling", "kitchen", "attic", "crawl"))
    steps = "".join(f'<li class="d-step" data-at="{i}"><span class="ds-t">{h}</span><b>{t}</b><p>{d}</p></li>' for i, (h, t, d) in enumerate(STEPS))
    cities = "".join(f'<a class="city reveal-up" href="@/{p}">{img(im, "")}<span><b>{c}</b><em>{ARROW}</em></span></a>' for c, p, im in CITIES)
    marq = "".join(f"<span>{t}</span>" for t in ["Water extraction", "Flood cleanup", "Sewage cleanup", "Ceiling leaks", "Toilet overflows", "Mold remediation", "Drying &amp; dehumidifying", "Kitchen water damage"] * 2)
    body = f'''
<section class="ct-hero"><div class="ch-bg" data-parallax="0.1">{img("summer-storm", "", priority=True)}</div><div class="wrap ch-grid">
<div class="ch-text"><p class="label"><span class="live"></span>St. George &middot; 24/7 emergency line</p>
<h1>Water damage restoration in St. George. <em>Start with where the water is.</em></h1>
<p class="lede">ClearTop Solutions provides water damage restoration in St. George, Washington, Santa Clara and Ivins: water extraction, drying, flood and sewage cleanup, leak and ceiling repair, and mold remediation. Licensed &amp; insured, with a 24/7 emergency line.</p>
<div class="btn-row"><a class="btn accent big-call" href="tel:{ST["tel"]}">{PHONE} Call {ST["phone"]}</a><a class="btn ghost" href="@/contact/">Request an Assessment {ARROW}</a></div></div>
<div class="ch-house"><p class="ch-hint">Tap the room where the water is</p><div class="hmap" data-hmap>{house(None, uid="hero")}{spots}</div><div class="hpanel" aria-live="polite">{panels}</div></div>
</div></section>
<div class="urgent"><div class="wrap ur-in"><b>Standing water right now?</b><span>Turn off power to affected areas if it&rsquo;s safe, don&rsquo;t handle wet electrical appliances, and call.</span><a href="tel:{ST["tel"]}">{PHONE} {ST["phone"]}</a></div></div>
<div class="marquee" aria-label="Services"><div class="marquee-track">{marq}</div></div>

<section class="sec dial-sec" data-dial><div class="wrap dial-grid">
<div class="dial-vis">{clock48()}<p class="dial-note">The EPA&rsquo;s guidance: <a href="{EPA}" rel="noopener">dry water-damaged areas and items within 24&ndash;48 hours</a> to prevent mold growth.</p></div>
<div><p class="label">The first 48 hours</p><h2>Water keeps working <em>after the leak stops.</em></h2>
<p class="dial-lede">It soaks into drywall, under flooring and into cabinets. The longer it sits, the greater the damage and the harder it is to put right. Here&rsquo;s how a job runs.</p>
<ol class="d-steps">{steps}</ol></div></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Where it starts</p><h2>Six rooms. <em>Twenty ways water gets in.</em></h2><p>Every service, grouped by the part of the house it fixes.</p></div>
<div class="ztiles">{tiles}</div>
<p><a class="tlink" href="@/services/">See all 20 services {ARROW}</a></p></div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.16">{img("rain-window", "")}</div><div class="wrap"><blockquote class="reveal-up">&ldquo;It is important to dry water-damaged areas and items <em>within 24&ndash;48 hours</em> to prevent mold growth.&rdquo;</blockquote><footer>U.S. Environmental Protection Agency, <a href="{EPA}" rel="noopener">A Brief Guide to Mold, Moisture and Your Home</a></footer></div></section>

<section class="sec sky-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">When you call</p><h2>Simple, fast, <em>and straightforward.</em></h2></div>
<div class="floats"><div class="fl" data-float="0.04"><span>1</span><b>Call us anytime</b><p>Reach our 24/7 hotline. Our team responds quickly and helps you schedule restoration or emergency repair.</p></div>
<div class="fl" data-float="0.08"><span>2</span><b>Diagnosis &amp; quote</b><p>We assess the situation on-site, explain what&rsquo;s needed in plain language, and provide an upfront estimate before work begins.</p></div>
<div class="fl" data-float="0.12"><span>3</span><b>Complete the job</b><p>Our technicians complete the work efficiently and confirm everything meets your expectations before we leave.</p></div></div>
<div class="ins reveal-up"><b>Insurance</b><p>We assist with documentation and communication with your insurance provider, and coordinate with insurance companies and other parties to streamline the process.</p></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Where we work</p><h2>St. George <em>and its neighbors.</em></h2></div>
<div class="cities">{cities}</div></div></section>

<section class="sec faq-sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Request a callback", fields=[("zip", "ZIP code (optional)")], msg_label="What happened? (optional)")}<p class="small">Faster: call the 24/7 line, <a href="tel:{ST["tel"]}">{ST["phone"]}</a>.</p></div>
</div></section>
<div class="wrap"><p class="credits">Background photos, for atmosphere only: &ldquo;<a href="https://www.flickr.com/photos/189326381@N08/51386298981" rel="noopener">Summer Storm</a>&rdquo; and &ldquo;<a href="https://www.flickr.com/photos/189326381@N08/52379397605" rel="noopener">Thanks For The Shot Pops!</a>&rdquo; by A Guy Named Nyal (<a href="https://creativecommons.org/licenses/by-sa/2.0/" rel="noopener">CC BY-SA 2.0</a>); &ldquo;<a href="https://www.flickr.com/photos/88123769@N02/51386338695" rel="noopener">Zion Landscape</a>&rdquo; by Bernard Spragg and the Virgin River in St. George by Lindsey Winkel, USDA Forest Service (public domain); rain on window and rain on glass by rawpixel (CC0).</p></div>
''' + cta()
    return {"path": "", "canonical": "https://cleartopsolutions.shop/st-george/", "sitemap": False, "title": "Water Damage Restoration St. George, UT | ClearTop Solutions",
            "meta": "Water damage restoration in St. George, UT: water extraction, drying, flood and sewage cleanup, leak and ceiling repair, mold remediation. 24/7 emergency line.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
