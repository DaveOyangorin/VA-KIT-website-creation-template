"""Pages for the triplejlandscaping.com redesign: "Grounded".

Triple J does every layer of a yard: design, sod, beds, sprinklers, pavers, flagstone, walls, concrete. So the home page opens on a full-bleed
photo of one of their own paver jobs with the Wasatch behind it, and the signature is a yard plan: tap a zone (lawn, beds, path, patio,
wall, sprinklers, drive) and the panel shows the service that builds it, in their words, with a photo from one of their own jobs.
Deep moss and their teal-to-lime leaf gradient, Cormorant Garamond to sit with their script logo.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same 7 URLs (no trailing slash) and canonicals."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE, EMAIL
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
header, footer = K.header, K.footer
cta = K.cta

GROUPS = [("design", "Landscape design &amp; installation", [("Landscape design", "Custom outdoor plans that reflect your style and property needs."), ("Zeroscape", "Rock and mulch landscaping that reduces watering and keeps your yard clean and modern."),
            ("Xeriscape", "Drought-tolerant landscaping that saves water while maintaining natural beauty."), ("New sod installation", "Fresh, healthy grass installed with proper soil prep for long-lasting results."),
            ("Artificial grass", "Low-maintenance turf that stays green year-round without watering.")]),
          ("lawn", "Lawn care &amp; yard maintenance", [("Lawn service", "Regular mowing, edging and lawn upkeep to keep your yard tidy."), ("Mulching &amp; bed care", "Mulch application that enhances soil health and improves appearance."),
            ("General clean up", "Comprehensive yard cleanup: debris removal, seasonal tidying and more."), ("Tree trimming and removal", "Professional trimming and safe tree removal when needed to protect your property.")]),
          ("irrigation", "Irrigation &amp; sprinkler services", [("Sprinkler installation", "Custom irrigation systems designed for efficient coverage and long-lasting performance."), ("Sprinkler repair", "Repairs for leaks, broken heads, controller issues and system upgrades.")]),
          ("hardscape", "Hardscape &amp; outdoor features", [("Paver installation", "Custom patios and walkways built for lasting durability and clean, polished curb appeal."), ("Flagstone &amp; stone work", "Natural stone patios and pathways that add beauty, texture and timeless character."),
            ("Retaining walls", "Engineered walls that control elevation changes and improve structure and stability."), ("Fire pits &amp; outdoor features", "Custom fire pits and features designed for comfort and year-round enjoyment."),
            ("Concrete work", "Professional concrete installation for driveways, walkways, patios and flat areas.")]),
          ("seasonal", "Seasonal &amp; miscellaneous", [("Snow removal", "Winter snow clearing for driveways and walkways."), ("Junk removal", "Removal of yard debris and unwanted materials.")])]
ZONES = [("lawn", "Lawn", "New sod installation", "Fresh, healthy grass installed with proper soil prep for long-lasting results. Prefer no mowing? Artificial grass stays green year-round without watering.", "tj-sod", "Fresh sod along a white vinyl fence", "design"),
         ("beds", "Beds", "Xeriscape &amp; bed care", "Drought-tolerant plantings, rock and mulch that save water while keeping natural beauty, plus mulching that improves soil health and appearance.", "tj-xeri", "A xeriscaped slope with gravel and a cedar fence at sunset", "design"),
         ("path", "Path", "Flagstone &amp; stone work", "Natural stone patios and pathways that add beauty, texture and timeless character.", "tj-flag", "A flagstone path curving through new sod", "hardscape"),
         ("patio", "Patio", "Paver installation", "Custom patios and walkways built for lasting durability and clean, polished curb appeal.", "tj-paver-path", "A curved paver walkway between new planting beds", "hardscape"),
         ("wall", "Wall", "Retaining walls", "Engineered walls that control elevation changes and improve structure and stability.", "tj-wall", "A stone retaining wall beside a paver patio", "hardscape"),
         ("water", "Sprinklers", "Sprinkler installation &amp; repair", "Custom irrigation systems designed for efficient coverage, and repairs for leaks, broken heads, controller issues and upgrades.", "tj-sprinkler", "A new sprinkler valve manifold in a trench", "irrigation"),
         ("drive", "Drive", "Concrete work", "Professional concrete installation for driveways, walkways, patios and flat areas.", "tj-concrete", "New concrete pavers in a checker pattern", "hardscape")]
FAQ = [("Do you offer free estimates?", "<p>Yes. Request a quote online or call 385-227-5475, and we&rsquo;ll get back to you with an estimate.</p>"),
       ("What areas do you serve?", "<p>Homeowners and businesses throughout Salt Lake County. Our office is in West Valley City.</p>"),
       ("What are your hours?", "<p>Monday through Saturday, 7 am to 6 pm.</p>"),
       ("Are you licensed and insured?", "<p>Yes. We&rsquo;re licensed, insured and locally owned, and we stand behind our work.</p>")]


def yard():
    svg = '''<svg class="yd" viewBox="0 0 640 440" aria-hidden="true"><rect x="0" y="0" width="640" height="440" rx="14" class="yd-ground"/>
<rect x="40" y="30" width="230" height="150" rx="6" class="yd-house"/><text x="155" y="112" text-anchor="middle" class="yd-hl">HOUSE</text>
<rect class="z" data-z="patio" x="40" y="180" width="230" height="70" rx="4"/><path class="z" data-z="path" d="M150 250 C 170 300, 250 320, 300 380 L 345 380 C 300 320, 215 290, 195 250 Z"/>
<rect class="z" data-z="lawn" x="300" y="40" width="300" height="250" rx="10"/><path class="z" data-z="beds" d="M40 270 L 140 270 C 150 330, 230 360, 280 420 L 40 420 Z"/>
<rect class="z" data-z="wall" x="300" y="300" width="300" height="22" rx="3"/><rect class="z" data-z="drive" x="380" y="335" width="220" height="85" rx="4"/>
<g class="z sprk" data-z="water"><circle cx="340" cy="80" r="7"/><circle cx="560" cy="80" r="7"/><circle cx="340" cy="250" r="7"/><circle cx="560" cy="250" r="7"/><circle cx="450" cy="165" r="7"/></g>
<text x="450" y="170" text-anchor="middle" class="yd-l" dy="-18">LAWN</text><text x="155" y="220" text-anchor="middle" class="yd-l">PATIO</text><text x="95" y="380" class="yd-l">BEDS</text>
<text x="490" y="383" text-anchor="middle" class="yd-l">DRIVE</text><text x="450" y="316" text-anchor="middle" class="yd-l yd-ls">WALL</text></svg>'''
    btns = "".join(f'<button type="button" class="zb" data-zone="{k}" aria-pressed="{"true" if i == 0 else "false"}">{n}</button>' for i, (k, n, *_r) in enumerate(ZONES))
    panels = "".join(f'''<div class="zp" data-panel="{k}"{"" if i == 0 else " hidden"}><figure>{img(im, alt)}</figure><div><p class="label">{n} zone</p><h3>{t}</h3><p>{d}</p><a class="tlink" href="@/services/#{g}">See the service {ARROW}</a></div></div>''' for i, (k, n, t, d, im, alt, g) in enumerate(ZONES))
    return f'''<div class="yard" data-yard><div class="yd-wrap">{svg}<div class="zbs" role="group" aria-label="Choose a part of the yard">{btns}</div></div><div class="zps" aria-live="polite">{panels}</div></div>'''


def home():
    body = f'''
<section class="g-hero"><div class="gh-img" data-parallax="0.08">{img("tj-hero", "A new paver walkway and planting beds beside a home, with the Wasatch Range behind, by Triple J Landscaping", priority=True)}</div>
<div class="wrap gh-in"><div class="gh-txt"><p class="label">Salt Lake County &middot; Locally owned &middot; Licensed &amp; insured</p>
<h1>Landscaping in Salt Lake City, <em>built to last every season.</em></h1>
<p class="lede">Design, lawn care, irrigation, hardscaping and maintenance for homeowners and businesses. From full landscape installs to sprinkler service and seasonal yard care.</p>
<div class="btn-row"><a class="btn accent" href="@/get-a-quote/">Get a free quote {ARROW}</a><a class="btn ghost" href="tel:+13852275475">{PHONE} 385-227-5475</a></div></div>
<ul class="gh-tags"><li>Design</li><li>Lawn care</li><li>Irrigation</li><li>Hardscaping</li><li>Maintenance</li></ul></div></section>

<section class="sec g-yard" id="yard"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Your yard, zone by zone</p><h2>Tap the yard. <em>See how we&rsquo;d build it.</em></h2></div><p class="lede">Every photo here is from a Triple J job. Pick a zone to see the service behind it.</p></div>
{yard()}
</div></section>

<section class="sec g-svc"><div class="wrap">
<div class="g-head reveal"><p class="label">Our services</p><h2>Everything outside, <em>under one crew.</em></h2></div>
<div class="svc5">{"".join(f'<a class="sv reveal" href="@/services/#{k}"><span class="sv-n">{i + 1:02d}</span><b>{t}</b><ul>{"".join(f"<li>{n}</li>" for n, d in items)}</ul></a>' for i, (k, t, items) in enumerate(GROUPS))}</div>
</div></section>

<section class="g-band"><div class="band-img" data-parallax="0.1">{img("tj-squares", "Large concrete pavers with black river rock joints beside new turf")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">Our approach</p><p>Great outdoor spaces should be beautiful and functional, built to last through every season. Our goal is simple: make your yard better, without headaches for you.</p></blockquote></div></section>

<section class="sec g-work"><div class="wrap">
<div class="g-head split-h reveal"><div><p class="label">Recent projects</p><h2>We build projects <em>that last.</em></h2></div><a class="tlink" href="@/projects/">All projects {ARROW}</a></div>
<div class="gal">{"".join(f'<figure class="g{i} reveal">{img(n, a)}</figure>' for i, (n, a) in enumerate([("tj-path", "A paver path with river rock and planting beds along a cedar fence"), ("tj-flag2", "A flagstone walkway beside a new lawn"), ("tj-xeri2", "Xeriscape terraces beside a modern home"), ("tj-sod", "New sod along a white fence"), ("tj-wall", "A stone wall and patio")]))}</div>
</div></section>

<section class="sec g-acc"><div class="wrap g-acc-in">
<div class="reveal"><p class="label">Accountability you can count on</p><h2>No surprises, <em>start to finish.</em></h2>
<p>Strong communication and reliability matter as much as quality workmanship. From the first consultation through completion, we keep you informed and involved at every stage. We respect your property, stand behind our work, and stay committed to results that earn your trust.</p>
<ul class="ticks"><li>Licensed &amp; insured</li><li>Locally owned</li><li>Free estimates</li><li>Quality guaranteed</li></ul></div>
<div class="reveal"><p class="label">Questions</p>{faq_html(FAQ)}<a class="post-card g-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>USU Extension&rsquo;s half-inch rule, run times by sprinkler type, and the habits that grow deeper roots.</p><em>Read it {ARROW}</em></a></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Landscaping Salt Lake City | Triple J Landscaping, LLC",
            "meta": "Triple J Landscaping: locally owned landscaping in Salt Lake County. Design, sod, xeriscape, sprinklers, pavers, retaining walls and concrete. Free estimates.",
            "body": body, "body_class": "is-home", "og": "tj-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home()]
    sv = '<p class="answer">A range of services tailored to your needs, for homeowners and businesses throughout Salt Lake County. Every project starts with a free estimate.</p>' + \
         "".join(f'<h2 id="{k}">{t}</h2><dl class="svl">' + "".join(f"<div><dt>{n}</dt><dd>{d}</dd></div>" for n, d in items) + "</dl>" for k, t, items in GROUPS)
    out.append(K.page("services/", "Services", "Landscaping Services", "Design, lawn care, irrigation, hardscaping and more.", "Services", "Landscaping Services in Salt Lake County | Triple J",
                      "Triple J Landscaping services: design, xeriscape, sod and artificial grass, lawn care, sprinkler installation and repair, pavers, walls, concrete, snow removal.",
                      sv, image="tj-paver-path", alt="A curved paver walkway", canonical=EXT["services"]["canon"], faqs=FAQ[:2],
                      schema=K.svc_schema("services/", "Landscaping", "Salt Lake City, UT")))
    ab = '''<p class="answer">Triple J Landscaping is a locally owned and operated landscaping company serving homeowners and businesses throughout Salt Lake County.</p>
<p>From custom landscape design and irrigation installation to lawn maintenance and hardscape construction, we bring craftsmanship, care and reliable results to every project. Our goal is simple: make outdoor spaces more beautiful, functional and enjoyable, without headaches for you.</p>
<h2>Our services</h2><p>Complete landscaping solutions, from custom design and installation to lawn maintenance, irrigation systems and hardscape features. Whether you need a small upgrade or a full outdoor transformation, we tailor each project to your space, style and long-term goals.</p>
<h2>Experience</h2><p>With years of hands-on experience in outdoor construction and property care, our team brings skill and efficiency to every job. We&rsquo;ve refined our process so projects stay organized, on schedule and built to last, and we apply the same precision to simple lawn improvements and complete renovations.</p>
<h2>Accountability you can count on</h2><p>Strong communication and reliability are as important as quality workmanship. From the first consultation through completion, we keep you informed and involved at every stage so there are no surprises. We respect your property and stand behind our work.</p>'''
    out.append(K.page("about-us/", "About", "About Triple J Landscaping", "Local experts creating outdoor spaces in Utah.", "About", "About Triple J Landscaping | Locally Owned, Salt Lake County",
                      "Triple J Landscaping is a locally owned landscaping company serving Salt Lake County homes and businesses with design, irrigation, lawn care and hardscapes.",
                      ab, image="tj-flag", alt="A flagstone path through a lawn", canonical=EXT["about_us"]["canon"]))
    pj = '<p class="answer">We build projects that last. A few recent Triple J jobs around Salt Lake County.</p><div class="pgal">' + "".join(f"<figure>{img(n, a)}<figcaption>{c}</figcaption></figure>" for n, a, c in (
        ("tj-hero", "Pavers and beds with the Wasatch behind", "Pavers &amp; planting beds"), ("tj-squares", "Large concrete pavers with river rock joints", "Concrete pavers &amp; turf"),
        ("tj-paver-path", "A curved paver walkway", "Curved paver walkway"), ("tj-path", "A paver path with river rock", "Stepping-stone path"), ("tj-flag", "A flagstone path through sod", "Flagstone &amp; sod"),
        ("tj-flag2", "A flagstone walkway", "Flagstone walkway"), ("tj-sod", "New sod along a fence", "New sod"), ("tj-xeri", "A xeriscaped slope at sunset", "Xeriscape slope"),
        ("tj-xeri2", "Xeriscape terraces", "Xeriscape terraces"), ("tj-wall", "A stone wall and patio", "Retaining wall &amp; patio"), ("tj-concrete", "New concrete pavers", "Concrete work"),
        ("tj-sprinkler", "A new sprinkler valve manifold", "Sprinkler install"), ("tj-tree", "A tree being taken down", "Tree removal"), ("tj-truck", "The Triple J dump truck", "On the job"))) + "</div>"
    out.append(K.page("projects/", "Projects", "Our Projects", "We build projects that last.", "Projects", "Landscaping Projects &amp; Gallery | Triple J Landscaping, Utah",
                      "See recent Triple J Landscaping projects in Salt Lake County: pavers, flagstone, sod, xeriscape, retaining walls, concrete work and sprinkler installs.",
                      pj, image="tj-squares", alt="Concrete pavers and turf", canonical=EXT["projects"]["canon"]))
    con = f'''<p class="answer">Request a quote for your next project and we&rsquo;ll get back to you with an estimate.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13852275475">385-227-5475</a></dd></div><div><dt>Email</dt><dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd></div>
<div><dt>Address</dt><dd><address>4558 West 3170 South<br>West Valley City, Utah 84120</address></dd></div><div><dt>Office hours</dt><dd>Monday&ndash;Saturday: 7AM&ndash;6PM</dd></div></dl>'''
    out.append(K.page("get-a-quote/", "Get a quote", "Get a Free Quote", "Request a quote for your next project.", "Contact", "Get a Free Landscaping Quote | Triple J Landscaping, Utah",
                      "Request a free landscaping quote from Triple J Landscaping: call 385-227-5475, email, or send the form. Serving all of Salt Lake County, Monday to Saturday.",
                      con, canonical=EXT["get_a_quote"]["canon"], form_side=True))
    for path, k, h1, title, meta in (("privacy-policy/", "privacy_policy", "Privacy Policy", "Privacy Policy | Triple J Landscaping, LLC, Salt Lake County",
                                      "Triple J Landscaping privacy policy: what information we collect through our website and forms, how we use it, cookies, third-party services and your choices."),
                                     ("accessibility-statement/", "accessibility_statement", "Accessibility Statement", "Accessibility Statement | Triple J Landscaping, LLC, Utah",
                                      "Triple J Landscaping is committed to an accessible website for everyone. Our accessibility measures, ongoing efforts and how to contact us for help today.")):
        t = EXT[k]["text"]; t = t[t.find(h1) + len(h1):].strip()
        sents = re.split(r"(?<=[.!?])\s+", t)
        body = "".join(f"<p>{html.escape(' '.join(sents[j:j + 4]))}</p>" for j in range(0, len(sents), 4))
        out.append(K.page(path, h1, h1, "", "Legal", title, meta, body, canonical=EXT[k]["canon"]))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Services", "services/"), ("Projects", "projects/"), ("Get a quote", "get-a-quote/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (" Free estimates.", " Call 385-227-5475.")) for x in out]
