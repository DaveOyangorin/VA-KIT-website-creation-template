"""Premium home (v3) for sfrutah.com / Superior Foundation Repair Utah.
References (screenshotted 19 Oct 2026): Ram Jack (foundation repair: dark, bold, high contrast), Big-D (Utah: map of offices,
dark condensed type), Mortenson (full-bleed photo hero, DIN-style condensed caps).
Signature: the sticky Orem case story (their own photos cross-fade step by step, ending on the drawn pier section)."""
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import S, U
from illus import utah_map, pier_section
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L10 14.8l-5.2 2.8 1-5.8L1.5 7.7l5.9-.8z" fill="currentColor"/></svg>'

CASE = [("1", "orem-door-gap", "Door frame out of square before the lift", "The house", "A 1995 split-level on Artesian Road in Orem: 5 bedrooms, 3 baths, 2,100 square feet. Doors out of square, walls cracked."),
        ("2", "orem-wall-crack", "Wall crack inside the Orem home", "11 inches", "Years of shifting had sunk one corner 11 inches. The city planned to condemn the building."),
        ("3", "orem-excavation", "Excavation along the sunken corner", "A swamp underneath", "When we dug, the soil smelled like a swamp: lake-bed sediment, a natural spring under the front of the property, a high water table across the street."),
        ("4", "orem-brackets", "Helical pier brackets on the foundation", "23 helical piers", "Driven 33 to 40 feet, some to 43, to reach load-bearing soil. Brackets on all four walls let the house rise evenly."),
        ("5", "orem-crew-gasline", "Crew digging out the gas line by hand", "Gas lines by hand", "Pipes move when a house moves, so the gas lines were dug out by hand first to give them room."),
        ("6", None, "", "Passed", "Void fills under the lifted sections, then an independent structural engineer&rsquo;s inspection. The home passed, and the condemnation plans were canceled.")]
CITIES = ["Ogden", "Park City", "Salt Lake City", "Herriman", "Provo", "Price", "Cedar City", "Duck Creek Village", "Kanab", "St. George"]


def home(REVIEWS, SVC, HOME_FAQ, CONTACT):
    steps = "".join(f'<div class="step" data-step="{k}"><p class="s-n">Case 01 &middot; {k} / 6</p><h3>{t}</h3><p>{d}</p></div>' for k, im, alt, t, d in CASE)
    frames = "".join((f'<figure class="cframe{" show" if k == "1" else ""}" data-show="{k}">{img(im, alt)}<figcaption>{alt}</figcaption></figure>' if im else
                      f'<figure class="cframe cdraw" data-show="{k}">{pier_section("hp")}</figure>') for k, im, alt, t, d in CASE)
    marq = "".join(f"<span>{c}</span>" for c in CITIES * 2)
    lead, rest = REVIEWS[1], [REVIEWS[0], REVIEWS[2], REVIEWS[3]]
    revs = "".join(f'<blockquote class="rv reveal-up"><div class="stars" aria-label="5 stars">{STAR * 5}</div><p>&ldquo;{t}&rdquo;</p><footer>{n} &middot; Google review</footer></blockquote>' for n, t in rest)
    photo = {"helical_foundation_repair": "helical-bracket", "crack_repair": "crack-exterior-wall", "complete_leveling_services": "pier-install-window", "mobile_home_leveling": "mobile-home-jack",
             "post_and_beam_services": "post-beam-2", "encapsulation_services": "crawl-fans", "crawl_space_cleanings": "mobile-home-crawl", "deck_repair": "deck-framing"}
    lay = {"helical_foundation_repair": "span-3 row-2", "crack_repair": "span-3", "complete_leveling_services": "span-2", "mobile_home_leveling": "span-1", "post_and_beam_services": "span-2",
           "encapsulation_services": "span-2", "crawl_space_cleanings": "span-2", "deck_repair": "span-2", "waterproofing_services": "span-2", "new_construction_waterproofing": "span-2"}
    tiles = ""
    for k, lab, h1, ic, im, alt, t, m, intro in SVC:
        bg = img(photo[k], "") if k in photo else ""
        tiles += f'<a class="tile {lay[k]}{" icon-tile" if not bg else ""} reveal-up" href="@/{k}/">{bg}<span class="t-ic">{img(ic, "")}</span><span class="t-go">{ARROW}</span><span class="t-in"><b>{lab}</b></span></a>'
    body = f'''
<section class="hero-full sf-hero"><div class="hf-bg" data-parallax="0.12">{img("pier-rig-desert", "Pier installation rig at a Southern Utah home at golden hour", priority=True)}</div>
<div class="wrap"><div class="hf-row"><div><p class="label">Salt Lake City &middot; St. George &middot; all of Utah</p>
<h1>Foundation repair in Salt Lake City, <span>starting with the truth.</span></h1>
<p class="lede">Superior Foundation Repair does foundation repair in Salt Lake City, St. George and across Utah: helical piers, house and mobile home leveling, crack repair, waterproofing and crawl space work. Every job starts with a free inspection, and sometimes the honest answer is that you don&rsquo;t need a repair.</p>
<div class="btn-row"><a class="btn accent" href="@/{CONTACT}">Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<aside class="hf-card"><small>Google review</small><b>&ldquo;Honest about what we didn&rsquo;t need.&rdquo;</b><p>Cindy Schonberger, on Matt and Ryan</p></aside></div></div><span class="scroll-cue">Scroll</span></section>
<div class="marquee" aria-label="Cities we serve"><div class="marquee-track">{marq}</div></div>

<section class="sec"><div class="wrap">
<p class="big-intro reveal-up">Three of our four Google reviews say the same thing: Matt looked at the house and told them the truth, <em>even when it meant less work for us.</em></p>
<div class="stats"><div class="stat reveal-up"><b data-count="2019">2019</b><span>Founded by owner Matt Baker</span></div><div class="stat reveal-up"><b data-count="2">2</b><span>offices: Salt Lake City and St. George</span></div>
<div class="stat reveal-up"><b data-count="23">23</b><span>helical piers under one Orem house</span></div><div class="stat reveal-up"><b data-count="43" data-suffix=" ft">43 ft</b><span>deepest pier on that job</span></div></div>
</div></section>

<section class="sec reviews-sec"><div class="wrap">
<blockquote class="rv-lead reveal-up"><div class="stars" aria-label="5 stars">{STAR * 5}</div><p>&ldquo;{lead[1]}&rdquo;</p><footer>{lead[0]} &middot; Google review</footer></blockquote>
<div class="rv-grid">{revs}</div></div></section>

<section class="sec case-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Case 01 &middot; Artesian Road, Orem</p><h2>A house the city planned to condemn.</h2></div>
<div class="story"><div class="story-visual"><div class="frames">{frames}</div></div><div class="story-steps">{steps}<p class="step-cta"><a class="tlink light" href="@/all_case_studies/">Read the full case study {ARROW}</a></p></div></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Services</p><h2>Ten ways we fix a house.</h2></div>
<div class="bento sf-bento">{tiles}</div></div></section>

<section class="split-photo map-split"><div class="sp-txt reveal-up"><p class="label">Two offices</p><h2>From Ogden to Kanab.</h2>
<p>Salt Lake City for the Wasatch Front, St. George for Southern Utah. The ground changes a lot along I-15, from wet lake-bed clay up north to the sandy and expansive soils of the south, so each repair is sized to the ground under that house.</p>
<div class="two-off"><div><b>Salt Lake City</b><span>{S["street"]}, {S["city"]}, UT {S["zip"]}</span><a href="tel:{S["tel"]}">{S["phone"]}</a></div><div><b>St. George</b><span>{S["street2"]}, {S["city2"]}, UT {S["zip2"]}</span><a href="tel:{S["tel2"]}">{S["phone2"]}</a></div></div>
<a class="tlink light" href="@/coverage_areas/">All coverage areas {ARROW}</a></div><div class="sp-map reveal-up">{utah_map()}</div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.18">{img("orem-excavation", "")}</div><div class="wrap"><blockquote class="reveal-up">&ldquo;If it wasn&rsquo;t for him, I wouldn&rsquo;t have <em>a safe home</em> for my children to live in.&rdquo;</blockquote><footer>Amber, on KUTV 2News This Morning &middot; <a href="{S["kutv"]}" rel="noopener">Watch the segment</a></footer></div></section>

<section class="split-photo owner-split"><div class="sp-img">{img("matt-pier-install", "Matt Baker installing a helical pier")}</div><div class="sp-txt reveal-up">
<p class="label">The owner</p><h2>Meet Matt Baker.</h2>
<p>Matt founded Superior Foundation Repair in 2019, after more than a decade in foundation repair, to raise the standard he saw in the industry. You&rsquo;ll often find him in the field with the crews. Off the job he&rsquo;s with his wife and kids, or out hunting.</p>
<figure class="tv">{img("kutv-matt-garage", "Matt Baker interviewed on KUTV 2News This Morning")}<figcaption>On KUTV 2News This Morning: &ldquo;Homeowners finally get help&rdquo;</figcaption></figure>
<p><a class="tlink" href="@/about/">About us {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(HOME_FAQ)}</div>
<div class="reveal-up"><a class="guide" href="@/{p_blog.POST[1]}">{img("pier-rig-desert", "")}<span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
'''
    return body
