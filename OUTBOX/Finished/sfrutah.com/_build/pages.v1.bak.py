"""Pages for the sfrutah.com redesign: "The honest inspection".

Superior Foundation Repair's Google reviews keep saying the same thing: Matt came out, looked, and told them what they *didn't*
need ("determined it was stable and didn't need further intervention", "honest about what we needed and more importantly what we
DIDN'T need", "he essentially got nothing out of it"). So the site leads with that, in the client's customers' own words, and
backs it with the one job they documented in full: the Orem house on Artesian Road that had sunk 11 inches and was lifted on
23 helical piers driven 33 to 43 feet (drawn as an original section). The two offices sit on an accurate map of Utah along I-15,
from Ogden to Kanab. Navy and gold from the logo and their own service icons; red rock for Southern Utah.
Source: the live site is broken today (template 404 page), so text and photos come from the Wayback captures (Mar-Jul 2026).
Same URLs (no trailing slash, underscores), canonicals as captured. Home targets "foundation repair salt lake city" (report).
Left out until confirmed: "over 15 years" (the company was founded in 2019; Matt has "over a decade"), "Utah's premier / best /
most trusted", "certified waterproofing specialists", "strong guarantee", "locally made products", "decades of experience", and
the unsigned testimonials ("John and Mary", "David").
"""
import html, json, os, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
from cfg import S, NAME, SHORT, U, HERE, DOMAIN, CITIES
from migrate import migrate
from sfclean import clean, txt
from illus import utah_map, pier_section
import p_blog

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L10 14.8l-5.2 2.8 1-5.8L1.5 7.7l5.9-.8z" fill="currentColor"/></svg>'
CONTACT = "contact/"
HOME = ("Home", "")
EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
NOTHING = re.compile(r"(?!x)x")

REVIEWS = [("Kristi Richards", "I had some cracks in my block retaining wall. Matt accessed the wall and determined it was stable and didn&rsquo;t need further intervention. I appreciate his honesty and integrity!! However, he did some grading on our lot for preventative maintenance. He was fast, thorough and left our lot clean."),
           ("Cindy Schonberger", "Working with Ryan was a pleasure. Both he and Matt were honest about what we needed and more importantly what we DIDN&rsquo;T need. Ryan went out of his way to make sure we understood the process, and went above and beyond to make an extremely picky person (me) happy."),
           ("Corbin Olsen", "Wow! The owner Matt came to my house and spent an hour looking at my foundation and sinking floor issue. He helped me figure out exactly what is going on even though the framers on site [were] able to do the work and he essentially got nothing out of it! Great guy and VERY knowledgeable!"),
           ("Karen Brown", "Matt was easy to schedule, on time and very easy to work with. He identified an issue that was outside of the foundation and was incredibly knowledgable and helpful. I would call him again in a heartbeat if other basement issues arise.")]

# key, label, H1, icon, image, image alt, title, meta, intro
SVC = [("helical_foundation_repair", "Helical piers", "Helical Pier Foundation Repair in Salt Lake City", "ic-sinking-logo", "helical-bracket", "Helical pier bracket attached to a foundation in an excavated hole",
        "Helical Pier Foundation Repair in Salt Lake City | Superior", "Helical pier foundation repair in Salt Lake City and St. George: steel screw piers advanced to stable soil to stop settlement and lift sinking foundations.",
        "Superior Foundation Repair installs helical piers in Salt Lake City, St. George and across Utah. Helical piers are steel shafts with spiral plates, advanced deep into the ground until they reach stable soil, so they can support and lift a settling foundation."),
       ("crack_repair", "Crack repair", "Foundation Crack Repair in Salt Lake City", "ic-crack-logo", "crack-exterior-wall", "Vertical crack running down a home's exterior foundation wall",
        "Foundation Crack Repair in Salt Lake City | Superior", "Foundation and concrete crack repair in Salt Lake City and St. George: crack injection and structural repairs for foundation walls, basement floors and slabs.",
        "Superior Foundation Repair repairs foundation and concrete cracks in Salt Lake City, St. George and across Utah: crack injection and structural repairs for foundation walls, basement floors and exterior concrete, cosmetic or structural."),
       ("complete_leveling_services", "House leveling", "House Leveling in Salt Lake City", "ic-level-logo", "pier-install-window", "Lifting equipment set up against a home's foundation",
        "House Leveling in Salt Lake City, UT | Superior Foundation", "House leveling in Salt Lake City and St. George: lifting brackets and up to 20-ton jacks to correct sagging floors, settling and the cracks they cause.",
        "Superior Foundation Repair levels houses in Salt Lake City, St. George and across Utah, using a lifting bracket and up to 20-ton jacks to correct settling, sagging floors and the wall cracks that come with them."),
       ("mobile_home_leveling", "Mobile home leveling", "Mobile Home Leveling in Salt Lake City", "ic-mobile-logo", "mobile-home-jack", "Jack and supports under a mobile home",
        "Mobile Home Leveling in Salt Lake City, UT | Superior", "Mobile home leveling in Salt Lake City and St. George: jack adjustments and support systems for manufactured homes with uneven floors and sticking doors.",
        "Superior Foundation Repair levels mobile and manufactured homes in Salt Lake City, St. George and across Utah, with precise jack adjustments and support systems. Flat rates save you time and money over the long term."),
       ("post_and_beam_services", "Post and beam", "Post and Beam Repair in Salt Lake City", "ic-post-logo", "post-beam-2", "New support post set under a beam in a crawl space",
        "Post and Beam Foundation Repair in Salt Lake City | Superior", "Post and beam foundation repair in Salt Lake City and St. George: replacing and adjusting posts and beams in crawl spaces under older Utah homes.",
        "Superior Foundation Repair replaces and adjusts posts and beams in Salt Lake City, St. George and across Utah: the support system under many older homes with crawl spaces."),
       ("encapsulation_services", "Encapsulation", "Crawl Space Encapsulation in Salt Lake City", "ic-liner-logo", "crawl-fans", "Crawl space with a vapor barrier and drying fans",
        "Crawl Space Encapsulation in Salt Lake City | Superior", "Crawl space encapsulation in Salt Lake City and St. George: moisture barriers and climate control that turn a damp crawl space into dry, usable space.",
        "Superior Foundation Repair encapsulates crawl spaces in Salt Lake City, St. George and across Utah: a moisture barrier and climate control that keep the space dry, control odors and protect the structure above."),
       ("crawl_space_cleanings", "Crawl space cleaning", "Crawl Space Cleaning in Salt Lake City", "ic-crawl-logo", "mobile-home-crawl", "Crawl space under a home",
        "Crawl Space Cleaning in Salt Lake City, UT | Superior", "Crawl space cleaning in Salt Lake City and St. George: debris removal and sanitizing for safe utility access, better air quality and a usable crawl space.",
        "Superior Foundation Repair cleans crawl spaces in Salt Lake City, St. George and across Utah: clearing debris for utility access and peace of mind, and sanitizing neglected spaces."),
       ("waterproofing_services", "Waterproofing", "Basement Waterproofing in Salt Lake City", "ic-water-logo", None, "",
        "Basement Waterproofing in Salt Lake City | Superior Foundation", "Basement waterproofing in Salt Lake City and St. George: interior and exterior systems that stop water from entering, for Utah snowmelt and spring rain.",
        "Superior Foundation Repair waterproofs basements in Salt Lake City, St. George and across Utah, with interior and exterior systems that stop water from entering your home during snowmelt and spring storms."),
       ("new_construction_waterproofing", "New construction waterproofing", "New Construction Waterproofing in Salt Lake City", "ic-newbuild-logo", None, "",
        "New Construction Waterproofing in Salt Lake City | Superior", "New construction waterproofing in Salt Lake City and St. George: protect a new foundation from water damage and future structural problems from day one.",
        "Superior Foundation Repair waterproofs new construction in Salt Lake City, St. George and across Utah, so a new foundation is protected from water and the structural damage it causes from day one."),
       ("deck_repair", "Deck repair", "Deck Repair in Salt Lake City", "ic-deck-logo", "deck-framing", "Crew framing a new deck",
        "Deck Repair in Salt Lake City, UT | Superior Foundation Repair", "Deck repair in Salt Lake City and St. George: dry rot repairs to main structures and sub-structures, framing and restoration for outdoor decks and patios.",
        "Superior Foundation Repair repairs decks in Salt Lake City, St. George and across Utah, including main-structure and sub-structure dry rot repairs, which can be troublesome to find and fix.")]
SVCK = {k: (lab, ic) for k, lab, _, ic, *rest in SVC}


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def links(s):
    """Old absolute and relative links to the client's pages -> @/ links; links to anything else are unwrapped."""
    s = re.sub(r'href="https?://(?:www\.)?sfrutah\.com/?([^"#?]*?)/?"', lambda m: f'href="@/{m.group(1)}/"' if m.group(1) else 'href="@/"', s)
    s = re.sub(r'href="(?!@/|https?://|tel:|mailto:)/?([a-z_]+(?:/post/[a-z0-9\-]+)?)/?"', r'href="@/\1/"', s)
    return s


def mig(key, skip=()):
    c, f = clean(migrate(HERE, key, DOMAIN, NOTHING))
    c = "\n".join(b for b in re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", c)
                  if not (b.startswith(("<h2>", "<h3>")) and any(txt(b).lower() == x.lower() for x in skip)) and not re.fullmatch(r"(?i)contact us now|call now.*|schedule your free inspection today", txt(b)))
    c = re.sub(r"<h2>", "<h3>", c).replace("</h2>", "</h3>")
    return links(c), f


def header():
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{NAME} home">{img("sfr-logo", NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>Services</summary><div class="drop">{"".join(f'<a href="@/{k}/">{img(ic + "", "")}<span>{lab}</span></a>' for k, (lab, ic) in SVCK.items())}<a class="all" href="@/services/">All services</a></div></details></li>
<li><a href="@/all_case_studies/">Case Study</a></li><li><a href="@/coverage_areas/">Areas</a></li><li><a href="@/about/">About</a></li><li><a href="@/blog/">Blog</a></li><li><a href="@/{CONTACT}">Contact</a></li></ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{S["tel"]}">{PHONE}<span>{S["phone"]}</span></a><a class="btn" href="@/{CONTACT}">Free Inspection</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a><a href="@/services/">Services</a><a href="@/helical_foundation_repair/">Helical piers</a><a href="@/crack_repair/">Crack repair</a><a href="@/complete_leveling_services/">House leveling</a>
<a href="@/all_case_studies/">Case study</a><a href="@/coverage_areas/">Areas</a><a href="@/about/">About</a><a href="@/blog/">Blog</a><a href="@/{CONTACT}">Contact</a>
<a class="btn" href="tel:{S["tel"]}">Salt Lake {S["phone"]}</a><a class="btn ghost" href="tel:{S["tel2"]}">St. George {S["phone2"]}</a></div></details>
</div></header>''')


def footer():
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="foot">
<div class="f-brand"><span class="flogo">{img("sfr-logo", NAME + " logo")}</span><p>Locally owned foundation repair, founded in 2019 by Matt Baker. Free inspections across Utah.</p>
<p class="small"><a href="{S["bbb"]}" rel="noopener">BBB profile</a> &middot; <a href="{S["fb"]}" rel="noopener">Facebook</a> &middot; <a href="{S["ig"]}" rel="noopener">Instagram</a> &middot; <a href="{S["yt"]}" rel="noopener">YouTube</a></p></div>
<div><h3>Salt Lake City</h3><address>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><p><a class="fph" href="tel:{S["tel"]}">{S["phone"]}</a></p></div>
<div><h3>St. George</h3><address>{S["street2"]}<br>{S["city2"]}, UT {S["zip2"]}</address><p><a class="fph" href="tel:{S["tel2"]}">{S["phone2"]}</a></p></div>
<div><h3>Office</h3><p><a href="mailto:{S["email"]}">{S["email"]}</a></p><p class="small">{S["hours"]}</p><ul><li><a href="@/services/">Services</a></li><li><a href="@/coverage_areas/">Coverage areas</a></li><li><a href="@/all_case_studies/">Case study</a></li></ul></div>
</div>
<p class="fareas"><b>Serving</b> {" &middot; ".join(f'<a href="@/{k}/">{n}</a>' for n, k in [(c, c.lower().replace(". ", "_").replace(" ", "_")) for c in CITIES])}</p>
<div class="fbottom"><span>&copy; 2026 {NAME}</span><span><a href="@/blog/">Blog</a> &middot; <a href="@/about/">About</a> &middot; <a href="@/{CONTACT}">Contact</a></span></div></div></footer>
<div class="callbar"><a href="tel:{S["tel"]}">{PHONE} SLC</a><a href="tel:{S["tel2"]}">{PHONE} St. George</a><a href="@/{CONTACT}">Inspection</a></div>''')


def cta(title="Get the honest answer first.", text="A free inspection tells you what&rsquo;s going on, and whether you need a repair at all. Call the office nearest you, or send the form."):
    return f'''<section class="cta"><div class="wrap cta-in">
<div><p class="label">Free inspection</p><h2>{title}</h2><p class="lede">{text}</p><a class="btn gold" href="@/{CONTACT}">Request a Free Inspection {ARROW}</a></div>
<div class="offices"><a class="office" href="tel:{S["tel"]}"><small>Salt Lake City</small><b>{S["phone"]}</b><span>{S["street"]}</span></a>
<a class="office" href="tel:{S["tel2"]}"><small>St. George</small><b>{S["phone2"]}</b><span>{S["street2"]}</span></a></div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", icon=None):
    art = f'<figure class="ph-img">{img(image, alt, priority=True)}</figure>' if image else (f'<div class="ph-icon">{img(icon, "")}</div>' if icon else "")
    return f'''<section class="phero{" has-art" if art else ""}"><div class="wrap ph-in"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>{art}</div></section>'''


def side(extra=""):
    q = REVIEWS[1]
    return f'''<aside class="sv-side"><div class="card-insp"><p class="label">Free inspection</p><p class="ci-t">Honest about what you <em>don&rsquo;t</em> need.</p>
<blockquote><p>&ldquo;{q[1][:150].rsplit(" ", 1)[0]}&hellip;&rdquo;</p><footer>{q[0]} &middot; Google review</footer></blockquote>
<a class="btn" href="@/{CONTACT}">Request an Inspection {ARROW}</a>
<dl><div><dt>Salt Lake</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a></dd></div><div><dt>St. George</dt><dd><a href="tel:{S["tel2"]}">{S["phone2"]}</a></dd></div><div><dt>Hours</dt><dd>{S["hours"]}</dd></div></dl></div>{extra}</aside>'''


def form(title="Request a free inspection"):
    return f'''<form class="form" method="post" action=""><h3>{title}</h3>
<div class="row"><label for="f-name">Full name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone number *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email address *<input id="f-email" type="email" name="email" autocomplete="email" required></label>
<label for="f-city">City or town the property is near *<input id="f-city" name="city" required></label>
<label for="f-msg">Message<textarea id="f-msg" name="message" placeholder="What are you seeing? Cracks, sticking doors, sloping floors, water..."></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


def page(path, label, h1, lede, tag, title, meta, content, image=None, alt="", icon=None, intro="", crumbs=None, faqs=None, form_side=False, schema=None, canonical=None, sitemap=True, robots=None):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    faqs = faqs or []
    main = (f'<p class="answer">{intro}</p>' if intro else "") + content + (f"<h2>Common questions</h2>{faq_html(faqs)}" if faqs else "")
    right = f'<div class="form-col">{form()}</div>' if form_side else side()
    body = phero(trail, h1, lede, tag, image, alt, icon) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{main}</article>{right}</div></section>''' + ("" if form_side else cta())
    pg = {"path": path, "canonical": canonical or canon(path), "title": title, "meta": meta, "body": body, "og": image, "schema": [crumbs_ld(path, trail)] + (schema or []) + ([faq_ld(faqs)] if faqs else [])}
    if not sitemap: pg["sitemap"] = False
    if robots: pg["robots"] = robots
    return pg


def svc_schema(path, name, area="Salt Lake City, UT"):
    return [{"@type": "Service", "@id": canon(path) + "#service", "name": name, "provider": {"@id": U + "#business"}, "areaServed": {"@type": "State", "name": "Utah"}}]


HOME_FAQ = [("Is the inspection really free?", "Yes. We inspect the foundation, explain what we find, and give you a detailed, no-pressure estimate if a repair is needed. Sometimes the honest answer is that it isn&rsquo;t."),
            ("What signs should I look for?", "Inside: cracks in drywall, floors and ceilings, sticking or misaligned doors and windows, sloping floors. Outside: gaps around windows and doors, foundation cracks, leaning chimneys, soil separating from the foundation, water pooling. In a basement: bowed walls, leaks, cracked floors or walls, water stains."),
            ("Do you work on commercial buildings?", "Yes. We install helical pile systems for everything from residential decks to multi-story commercial properties."),
            ("Where do you work?", "We have offices in Salt Lake City and St. George and work across Utah, including Ogden, Park City, Provo, Herriman, Price, Cedar City, Kanab and Duck Creek Village."),
            ("Can you work in winter?", "Ask us about your project. Utah weather affects some exterior work, but interior repairs and many pier installations can go ahead year-round.")]


def home():
    revs = "".join(f'<blockquote class="rev reveal"><div class="stars" aria-label="5 stars">{STAR * 5}</div><p>&ldquo;{t}&rdquo;</p><footer><b>{n}</b><span>Google review</span></footer></blockquote>' for n, t in REVIEWS)
    svcs = "".join(f'<a class="svc reveal" href="@/{k}/">{img(ic, "")}<b>{lab}</b><em>{ARROW}</em></a>' for k, lab, _, ic, *r in SVC)
    case_photos = [("orem-excavation", "Excavation along the sunken corner"), ("orem-brackets", "Pier brackets on the foundation"), ("orem-crew-gasline", "Gas line dug out by hand before the lift"), ("orem-interior-crack", "Interior damage before the lift")]
    cps = "".join(f'<figure class="reveal">{img(n, c)}<figcaption>{c}</figcaption></figure>' for n, c in case_photos)
    body = f'''
<section class="hero"><div class="wrap hero-in">
<div class="hero-text"><p class="label">Salt Lake City &middot; St. George &middot; all of Utah</p>
<h1>Foundation repair in Salt Lake City, <span>starting with an honest inspection.</span></h1>
<p class="lede">Superior Foundation Repair does foundation repair in Salt Lake City, St. George and across Utah: helical piers, house and mobile home leveling, crack repair, waterproofing and crawl space work. Every job starts with a free inspection, and sometimes the honest answer is that you don&rsquo;t need a repair.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Request a Free Inspection {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<p class="hero-note">Southern Utah? Call St. George: <a href="tel:{S["tel2"]}">{S["phone2"]}</a></p></div>
<div class="hero-case"><figure>{img("orem-excavation", "Excavation along the sunken corner of the Orem home before the lift", priority=True)}</figure>
<div class="case-tag"><span>Case 01 &middot; Orem</span><b>11 in.</b><span>corner lifted back on 23 helical piers</span></div></div>
</div></section>

<section class="sec reviews"><div class="wrap">
<div class="head reveal"><p class="label">In their words</p><h2>&ldquo;What we <em>didn&rsquo;t</em> need.&rdquo;</h2><p class="lede">Three of these four customers say the same thing: Matt looked, and told them the truth, even when it meant less work for us.</p></div>
<div class="revs">{revs}</div></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Services</p><h2>Ten ways we fix a house.</h2></div>
<div class="svcs">{svcs}</div></div></section>

<section class="sec navy"><div class="wrap split">
<div class="reveal"><p class="label gold">Case study &middot; Artesian Road, Orem</p><h2>A house the city planned to condemn.</h2>
<p>A 1995 split-level: 5 bedrooms, 3 baths, 2,100 square feet. Years of shifting had sunk one corner 11 inches. When we dug, the soil smelled like a swamp: lake-bed sediment, a natural spring under the front of the property, and a high water table across the street at Springwater Park.</p>
<p>We installed 23 helical piers, 33 to 40 feet deep and some to 43 feet, to reach load-bearing soil, then lifted the house evenly on brackets along all four walls. Gas lines were dug out by hand first so they could move with the house. An independent structural engineer inspected the finished work, the home passed, and the condemnation plans were canceled.</p>
<a class="tlink light" href="@/all_case_studies/">Read the full case study {ARROW}</a></div>
<figure class="sheet reveal">{pier_section()}</figure>
</div><div class="wrap"><div class="case-strip">{cps}</div></div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Two offices</p><h2>From Ogden to Kanab.</h2>
<p>We work out of two offices: Salt Lake City for the Wasatch Front and St. George for Southern Utah. The soils change a lot along the way, from wet lake-bed clays up north to the sandy and expansive soils of the south, so we size each repair to the ground under that house.</p>
<div class="two-off"><div><b>Salt Lake City</b><span>{S["street"]}, {S["city"]}, UT {S["zip"]}</span><a href="tel:{S["tel"]}">{S["phone"]}</a></div><div><b>St. George</b><span>{S["street2"]}, {S["city2"]}, UT {S["zip2"]}</span><a href="tel:{S["tel2"]}">{S["phone2"]}</a></div></div>
<a class="tlink" href="@/coverage_areas/">All coverage areas {ARROW}</a></div>
<figure class="map-wrap reveal">{utah_map()}</figure>
</div></section>

<section class="sec sand"><div class="wrap split">
<figure class="tv reveal">{img("kutv-matt-garage", "Matt Baker of Superior Foundation Repair Utah interviewed on KUTV 2News This Morning")}<figcaption>2News This Morning (KUTV): &ldquo;Homeowners finally get help&rdquo;</figcaption></figure>
<div class="reveal"><p class="label">On KUTV 2News</p><h2>&ldquo;A safe home for my children to live in.&rdquo;</h2>
<p>KUTV&rsquo;s 2News This Morning covered homeowners in Utah and Salt Lake County who finally got help with their foundations. One of them, Amber, said: &ldquo;I&rsquo;m forever grateful to him &amp; his crew and what they&rsquo;ve done. If it wasn&rsquo;t for him, I wouldn&rsquo;t have a safe home for my children to live in.&rdquo;</p>
<a class="tlink" href="{S["kutv"]}" rel="noopener">Watch on YouTube {ARROW}</a></div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">The owner</p><h2>Meet Matt Baker.</h2>
<p>Matt founded Superior Foundation Repair in 2019, after more than a decade in foundation repair, to raise the standard he saw in the industry. He&rsquo;s a hands-on owner: you&rsquo;ll often find him in the field with the crews, making sure every repair meets the standard. Off the job he&rsquo;s with his wife and kids, or out hunting.</p>
<a class="tlink" href="@/about/">About us {ARROW}</a>
<figure class="matt">{img("matt-pier-install", "Matt Baker installing a helical pier")}</figure></div>
<div class="reveal"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(HOME_FAQ)}
<a class="guide" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Foundation Repair Salt Lake City | Superior Foundation Repair",
            "meta": "Foundation repair in Salt Lake City and St. George: helical piers, house leveling, crack repair and waterproofing, starting with a free, honest inspection.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(HOME_FAQ)]}


def city_pages():
    out = []
    names = {"st_george": "St. George", "cedar_city": "Cedar City", "kanab": "Kanab", "duck_creek_village": "Duck Creek Village", "provo": "Provo", "salt_lake_city": "Salt Lake City",
             "ogden": "Ogden", "park_city": "Park City", "price": "Price", "herriman": "Herriman"}
    for k, n in names.items():
        v = EXT[k]
        c, f = mig(k)
        h1 = f"Foundation Repair in {n}, Utah"
        office = "St. George" if k in ("st_george", "cedar_city", "kanab", "duck_creek_village") else "Salt Lake City"
        ph = S["phone2"] if office == "St. George" else S["phone"]
        t = f"Foundation Repair {n}, UT | Superior Foundation Repair"
        if len(t) > 62: t = f"Foundation Repair {n} | Superior Foundation"
        m = f"Foundation repair in {n}, Utah: helical piers, crack repair, leveling and waterproofing from our {office} office. Free, honest inspections."
        out.append(page(f"{k}/", n, h1, f"Served from our {office} office: {ph}.", "Coverage area", t, html.unescape(m).replace("’", "'"), c,
                        intro=f"Superior Foundation Repair provides foundation repair in {n}, Utah, from our {office} office: helical piers, house leveling, crack repair, waterproofing and crawl space work, starting with a free inspection.",
                        crumbs=[("Coverage areas", "coverage_areas/")], faqs=f, canonical=v["canon"] or None,
                        schema=[{"@type": "Service", "@id": canon(f"{k}/") + "#service", "name": f"Foundation repair in {n}, Utah", "provider": {"@id": U + "#business"}, "areaServed": {"@type": "City", "name": n + ", UT"}}]))
    return out


def pages_main():
    out = []
    sv = [("Services", "services/")]
    for k, lab, h1, ic, im, alt, t, m, intro in SVC:
        c, f = mig(k, skip=(h1,))
        out.append(page(f"{k}/", lab, h1, None, "Service", t, m, c, image=im, alt=alt, icon=ic, intro=intro, crumbs=sv, faqs=f, canonical=EXT[k]["canon"] or None, schema=svc_schema(f"{k}/", lab)))
    c, f = mig("services", skip=("Superior Foundation Repair Services", "Get Your Free Foundation Inspection"))
    grid = '<div class="svc-list">' + "".join(f'<a href="@/{k}/">{img(ic, "")}<b>{lab}</b></a>' for k, lab, _, ic, *r in SVC) + "</div>"
    out.append(page("services/", "Services", "Foundation Repair Services in Salt Lake City &amp; Utah", "Ten services, two offices, one free inspection to start.", "Services",
                    "Foundation Repair Services in Salt Lake City | Superior", "Foundation repair services in Salt Lake City, St. George and across Utah: helical piers, crack repair, leveling, waterproofing, crawl spaces, post and beam, decks.",
                    grid + c, image="pier-install-yard", alt="Helical pier installation at a Utah home",
                    intro="Superior Foundation Repair offers foundation repair services in Salt Lake City, St. George and across Utah, for homes and commercial buildings, starting with a free inspection.", faqs=f, canonical=EXT["services"]["canon"] or None))
    c, f = mig("about", skip=("About US", "Our Company's Story", "Our Team", "What Our Customers Say?"))
    c = re.split(r"<h3>What Our Customers Say\?</h3>|<p>“We were impressed", c)[0]
    c = re.sub(r"<p>Superior At Superior", "<p>At Superior", c)
    out.append(page("about/", "About", "About Superior Foundation Repair Utah", "Founded in 2019 by Matt Baker. Offices in Salt Lake City and St. George.", "About us",
                    "About Superior Foundation Repair Utah | Founded by Matt Baker", "Superior Foundation Repair Utah was founded in 2019 by Matt Baker, a hands-on owner with over a decade in foundation repair. Offices in Salt Lake City and St. George.",
                    c + '<h2>What customers say</h2><div class="revs small-revs">' + "".join(f'<blockquote><p>&ldquo;{t}&rdquo;</p><footer><b>{n}</b> &middot; Google review</footer></blockquote>' for n, t in REVIEWS) + "</div>",
                    image="kutv-matt-closeup", alt="Matt Baker, owner of Superior Foundation Repair Utah, on KUTV 2News", faqs=f, canonical=EXT["about"]["canon"] or None))
    c, f = mig("all_case_studies", skip=("11 inches",))
    c = re.sub(r"<p>(Read the entire Case Study below|Click Here Full Case Study)</p>", "", c)
    c = c.replace("<h3>Common questions</h3>", "")
    gal = '<div class="pgal">' + "".join(f"<figure>{img(n, cap)}<figcaption>{cap}</figcaption></figure>" for n, cap in [("orem-excavation", "Excavating along the sunken corner"), ("orem-brackets", "Brackets connecting the piers to the foundation"),
                                                                                                                   ("orem-crew-gasline", "Gas line dug out by hand"), ("orem-excavator", "Excavator on site"), ("orem-door-gap", "Door frame out of square before the lift"), ("orem-wall-crack", "Wall crack inside")]) + "</div>"
    out.append(page("all_case_studies/", "Case study", "Case Study: Orem Home Lifted 11 Inches", "Artesian Road, Orem: 23 helical piers, 33 to 43 feet deep.", "Case study 01",
                    "Case Study: Orem Home Lifted 11 Inches | Superior Foundation", "Case study: a 1995 Orem split-level sunk 11 inches over a natural spring, lifted on 23 helical piers 33 to 43 feet deep. It passed an engineer's inspection.",
                    f'<figure class="sheet">{pier_section("cs")}</figure>' + c + gal, image="orem-brackets", alt="Helical pier brackets on the Orem home's foundation",
                    intro="One property on Artesian Road in Orem shows how the right approach can restore stability when shifting soils threaten a home: one corner had sunk 11 inches, and the city planned to condemn the house.",
                    faqs=f, canonical=EXT["all_case_studies"]["canon"] or None))
    c, f = mig("coverage_areas")
    out.append(page("coverage_areas/", "Coverage areas", "Foundation Repair Coverage Areas in Utah", "Two offices along I-15: Salt Lake City and St. George.", "Coverage areas",
                    "Foundation Repair Coverage Areas in Utah | Superior Foundation", "Superior Foundation Repair covers Utah from Salt Lake City and St. George offices: Ogden, Park City, Provo, Herriman, Price, Cedar City, Kanab and Duck Creek Village.",
                    f'<figure class="map-wrap">{utah_map("ca")}</figure>' + '<ul class="city-links">' + "".join(f'<li><a href="@/{k}/">{n}</a></li>' for n, k in [(c2, c2.lower().replace(". ", "_").replace(" ", "_")) for c2 in CITIES]) + "</ul>" + c,
                    intro="Superior Foundation Repair covers all of Utah from two offices, Salt Lake City and St. George, with city pages for the places we work most.", faqs=f, canonical=EXT["coverage_areas"]["canon"] or None))
    c, f = mig("contact", skip=("Contact with Superior Foundation Repair Utah", "Contact Information", "Over Service Areas"))
    c = re.sub(r"(?s)<p>We’re happy to assist.*?</ul>", "", c)
    out.append(page(CONTACT, "Contact", "Contact Superior Foundation Repair Utah", "Two offices, one email, free inspections.", "Contact",
                    "Contact Superior Foundation Repair Utah | SLC &amp; St. George", "Contact Superior Foundation Repair Utah: Salt Lake City 801-970-1473, St. George 435-668-0734, office@sfrutah.com. Mon to Fri, 9 AM to 5 PM. Free inspections.",
                    f'''<dl class="info"><div><dt>Salt Lake City</dt><dd><a href="tel:{S["tel"]}">{S["phone"]}</a><br>{S["street"]}, {S["city"]}, UT {S["zip"]}</dd></div>
<div><dt>St. George</dt><dd><a href="tel:{S["tel2"]}">{S["phone2"]}</a><br>{S["street2"]}, {S["city2"]}, UT {S["zip2"]}</dd></div><div><dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd></div><div><dt>Hours</dt><dd>{S["hours"]}; Saturday &amp; Sunday closed</dd></div></dl>''' +
                    "<h2>What to expect</h2><ul><li>A quick response to your request</li><li>A free inspection and a detailed, no-pressure estimate</li><li>Honest advice, including when a repair isn&rsquo;t needed</li></ul>",
                    intro="We&rsquo;re happy to answer questions, give advice, or schedule a free inspection. Call the office nearest you or send the form.", form_side=True, canonical=EXT["contact"]["canon"] or None))
    return out


def make_pages():
    p_blog.setup(phero, cta, side, ARROW, HOME, CONTACT, mig)
    out = [home()] + pages_main() + city_pages() + p_blog.pages() + [notfound()]
    return [_fit(dict(x, body=Q(x["body"]))) for x in out]


def _fit(pg):
    for add in (" Free inspections.", " Call 801-970-1473."):
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound():
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", "Try our services, the case study, or call the office.", "404") + f'<section class="sec"><div class="wrap"><p><a class="tlink" href="@/services/">Services {ARROW}</a> &nbsp; <a class="tlink" href="@/blog/">Blog {ARROW}</a></p></div></section>'
    return {"path": "404.html", "title": "Page Not Found | Superior Foundation Repair Utah", "meta": "This page was not found. See Superior Foundation Repair services and the Orem case study, or call 801-970-1473 for a free foundation inspection in Utah.",
            "body": body, "robots": "noindex, follow", "sitemap": False}
