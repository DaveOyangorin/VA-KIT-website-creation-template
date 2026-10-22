"""All pages for the jemzaroofing.com redesign, on the client's current URLs.
Facts come only from the client's own pages (17 Oct 2026): licensed & insured, 18 years of experience, founded in Millcreek,
residential & commercial, English/Spanish, 50 miles around Salt Lake City 84115, cash/card/Square/check, the service
descriptions on services.php and the four reviews on the home page. The service pages on the live site are photo and
video galleries with no text; the new text explains each service and describes what the client's own photos show.
Report (17 Oct 2026): home page targets "roofing company salt lake city"; every service page names Salt Lake City.
"""
import html
from build import (U, S, ARROW, PHONE, CONTACT, SERVICES, BLOG, REVIEWS, img, video, gallery, phero, cta, quotes_html,
                   faq_html, faq_ld, crumbs_ld, contact_form, BADGE)
import p_blog

HOME = ("Home", "")


def svc_ld(path, name, desc):
    return {"@type": "Service", "@id": U + path + "#service", "name": name, "serviceType": name, "description": desc,
            "provider": {"@id": U + "#organization"},
            "areaServed": {"@type": "City", "name": "Salt Lake City", "containedInPlace": {"@type": "State", "name": "Utah"}}}


def related(cur):
    items = [(l, p, im) for l, p, im, _ in SERVICES if p != cur][:4]
    cards = "".join(f'<a class="rel reveal" href="@/{p}">{img(im, html.unescape(l))}<span>{l}</span></a>' for l, p, im in items)
    return f'<section class="sec stone"><div class="wrap"><div class="head reveal"><p class="label">More from Jemza</p><h2>Other services</h2></div><div class="rels">{cards}</div></div></section>'


WHY = f'''<ul class="facts">
<li><b>18 years</b><span>of experience in roofing</span></li>
<li><b>Licensed &amp; insured</b><span>residential and commercial</span></li>
<li><b>English / Espa&ntilde;ol</b><span>bilingual attention</span></li>
<li><b>50 miles</b><span>around Salt Lake City, Utah 84115</span></li>
</ul>'''


def service_page(path, label, h1, title, meta, hero, hero_alt, lede, body, photos, videos=(), faqs=None, desc=None):
    vids = ""
    if videos:
        vids = ('<section class="sec dark"><div class="wrap"><div class="head reveal"><p class="label light">On the job</p><h2>Job videos</h2>'
                '<p class="lede">Short clips from our own projects.</p></div><div class="vids">' + "".join(video(p, c) for p, c in videos) + "</div></div></section>")
    faq_sec = ""
    if faqs:
        faq_sec = f'<section class="sec"><div class="wrap split top"><div class="reveal"><p class="label">Questions</p><h2>Asked about {label.lower()}</h2></div><div class="reveal">{faq_html(faqs)}</div></div></section>'
    trail = [HOME, ("Services", "services.php"), (label, path)]
    page_body = (phero(trail, h1, lede, hero, hero_alt, "Salt Lake City, Utah") +
                 f'''<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">{body}</div>
<aside class="reveal side">{WHY}<a class="btn" href="@/{CONTACT}">Get a Quote {ARROW}</a><p class="small">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a>. Hablamos espa&ntilde;ol.</p></aside></div></section>
<section class="sec stone"><div class="wrap"><div class="head reveal"><p class="label">Our work</p><h2>{label}: project photos</h2><p class="lede">Every photo here is a Jemza job.</p></div>{gallery(photos)}</div></section>'''
                 + vids + faq_sec + related(path) + cta())
    schema = [crumbs_ld(path, trail), svc_ld(path, html.unescape(h1), desc or meta)]
    if faqs: schema.append(faq_ld(faqs))
    return {"path": path, "title": title, "meta": meta, "body": page_body, "og": hero, "schema": schema, "full_biz": False}


STRIP = [("new-roof-01", "Metal and shingle mountain home"), ("roof-project-15", "Standing-seam roof on a log home"), ("metal-roof-07", "Dark metal roof with dormers"),
         ("roof-project-17", "Copper standing-seam bay roof"), ("new-roof-02", "White farmhouse with a metal dormer"), ("roof-project-12", "Estate with metal and shingle roofs"),
         ("chimney-shroud-14", "Louvered shroud on a stone chimney"), ("roof-project-13", "New home with metal and shingle roofs")]


def home():
    rows = "".join(f'<a class="idx" href="@/{p}" data-img="{im}"><span class="n">{i+1:02d}</span><b>{l}</b><span class="d">{d}</span><i>{ARROW}</i></a>'
                   for i, (l, p, im, d) in enumerate(SERVICES))
    floats = "".join(f'<figure class="fl" data-img="{im}">{img(im, "")}</figure>' for l, p, im, d in SERVICES)
    strip = "".join(f'<figure class="frame-card"><div class="fc-img">{img(n, c)}</div><figcaption><span class="mono">{i+1:02d} / {len(STRIP):02d}</span>{c}</figcaption></figure>' for i, (n, c) in enumerate(STRIP))
    faqs = [("Is Jemza Roofing licensed and insured?", "Yes. Jemza Roofing is licensed and insured, for both residential and commercial roofing."),
            ("Do you speak Spanish?", "Yes. We offer bilingual attention in English and Spanish. <span lang=\"es\">Hablamos espa&ntilde;ol.</span>"),
            ("How far do you travel?", "We cover 50 miles around Salt Lake City, Utah 84115, measured from our office at 2212 S West Temple."),
            ("How can I pay?", "We take cash, card, Square and check."),
            ("Do you work on commercial buildings?", "Yes. We do residential and commercial roofing. Call the office to talk through your building.")]
    quotes = "".join(f'<figure class="bq reveal"><blockquote><p>&ldquo;{html.escape(q)}&rdquo;</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>' for q, a in REVIEWS)
    body = f'''
<section class="hero"><div class="hero-bg">{img("metal-roof-05", "A Jemza roof on a modern Utah home: standing-seam metal with architectural shingles", priority=True)}</div>
<div class="wrap hero-in"><p class="label light">Jemza Roofing &middot; Salt Lake City, Utah</p>
<h1>Roofing company in Salt Lake City. <em>Quality over quantity, always.</em></h1>
<div class="hero-foot"><p class="lede">Licensed and insured roofing for homes and businesses: standing-seam metal, shingles, chimneys, custom caps and shrouds, gutters and more, within 50 miles of our office.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div></div>
{BADGE}<div class="scroll-cue" aria-hidden="true"><span>Scroll</span></div></section>

<section class="sec statement-sec"><div class="wrap statement-grid">
<p class="label">About Jemza</p>
<p class="big reveal">Founded in Millcreek, Utah, Jemza Roofing has spent <em>18 years</em> on roofs across the Salt Lake Valley, from <a href="@/metal-roofing.php">standing-seam metal</a> and <a href="@/asphalt-shingles.php">shingles</a> to the <a href="@/ChimneyCap-Shroud.php">custom chimney shrouds</a> that finish a house.</p>
<div class="st-pair reveal"><figure>{img("new-roof-04", "A crane lifting roofing materials up to a mountain home with a stone chimney")}<figcaption class="mono">On site &middot; materials going up</figcaption></figure>
<figure>{img("roof-project-17", "Copper standing-seam roof over a bay window")}<figcaption class="mono">Copper standing seam</figcaption></figure></div>
<a class="more" href="@/about.php">More about us {ARROW}</a>
</div></section>

<section class="strip-sec" aria-label="Recent projects"><div class="strip-sticky">
<div class="wrap strip-head"><div><p class="label light">Recent projects</p><h2>Work of excellence, <em>from the air</em></h2></div><a class="more light" href="@/portfolio.php">See the portfolio {ARROW}</a></div>
<div class="strip-track">{strip}</div>
<div class="wrap strip-bar"><i></i></div></div></section>

<section class="sec svc-sec"><div class="wrap"><div class="head row reveal"><div><p class="label">Roofers in Salt Lake City</p><h2>What we do</h2></div><a class="more" href="@/services.php">All services {ARROW}</a></div>
<div class="index-wrap"><div class="index">{rows}</div><div class="floats" aria-hidden="true">{floats}</div></div></div></section>

<section class="sec dark band-split"><div class="wrap split">
<div class="reveal"><p class="label light">Chimney caps &amp; shrouds</p><h2>The detail people notice <em>from the street</em></h2>
<p class="lede">Black metal boxes over stone and cedar, louvered shrouds, copper bells that weather to brown. A chimney cap keeps out rain and animals; a shroud also changes how the whole roofline reads.</p>
<p>Before you pick one, read our guide: <a href="@/{BLOG[1]}">{BLOG[0]}: what&rsquo;s the difference?</a> It covers what each one does and the code rule for shrouds on factory-built chimneys.</p>
<div class="btn-row"><a class="btn" href="@/ChimneyCap-Shroud.php">See caps &amp; shrouds {ARROW}</a></div></div>
<div class="pair reveal"><figure>{img("chimney-shroud-14", "Louvered black chimney shroud on a stone chimney above a standing-seam roof")}</figure><figure>{img("chimney-shroud-09", "Copper bell chimney cap on a stone chimney in winter")}</figure></div>
</div></section>

<section class="nums"><div class="wrap nums-in">
<div class="reveal"><b>18</b><span>years of experience in roofing</span></div><div class="reveal"><b>50</b><span>miles covered around Salt Lake City</span></div>
<div class="reveal"><b>2</b><span>languages: English and Spanish</span></div><div class="reveal"><b>8</b><span>services, roof to chimney to walls</span></div></div></section>

<section class="sec"><div class="wrap"><div class="head reveal"><p class="label">Reviews</p><h2>What customers say about <em>Omar and the crew</em></h2></div><div class="bqs">{quotes}</div></div></section>

<section class="sec stone"><div class="wrap split top">
<div class="reveal"><p class="label">Service area</p><h2>Within 50 miles of Salt Lake City</h2>
<p class="lede">Our office is at {S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}. We cover 50 miles around it, which takes in the Salt Lake Valley and well beyond.</p>
{WHY}
<p class="small"><a href="{S["map"]}" rel="noopener">Find us on Google Maps</a></p></div>
<div class="reveal">{contact_form()}</div></div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="label">Questions</p><h2>Before you call</h2><p class="lede">Anything else? Call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div>
<div class="reveal">{faq_html(faqs)}</div></div></section>
''' + cta()
    return {"path": "", "title": "Roofing Company Salt Lake City, UT | Jemza Roofing",
            "meta": "Jemza Roofing is a licensed and insured roofing company in Salt Lake City: metal roofing, shingles, chimney caps and shrouds, gutters. English/Spanish. Call.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(faqs)]}


def services():
    blocks = [
        ("roof-replacement", "Roof replacement", "roof-tear-off-crew", "Crew stripping and re-roofing a house",
         "If your existing roof is beyond repair or simply outdated, we safely remove and dispose of the old roof and install a high-quality replacement that improves both the look and the function of the building."),
        ("metal-roofing", "Metal roofing", "metal-roof-02", "Standing-seam metal roofs on a new home",
         f'Our team helps you choose the metal roofing that fits your budget and the look you want. Metal roofs are durable, attractive and energy-efficient. <a href="@/metal-roofing.php">Metal roofing &rarr;</a>'),
        ("asphalt-shingles", "Asphalt shingles", "asphalt-shingle-roof-03", "Gray architectural shingle roof",
         f'Durable asphalt shingle roofs in a variety of styles and colors, using top-quality materials for weather resistance. <a href="@/asphalt-shingles.php">Asphalt shingles &rarr;</a>'),
        ("chimney", "Chimney", "chimney-02", "White stone chimneys with black caps above a brown metal roof",
         f'Chimney work from inspection to reconstruction, done to be safe and to look right. <a href="@/chimney.php">Chimney &rarr;</a> &middot; <a href="@/ChimneyCap-Shroud.php">Caps &amp; shrouds &rarr;</a>'),
    ]
    sec = "".join(f'<article class="svc-row reveal" id="{a}">{img(im, alt)}<div><p class="label">{i+1:02d}</p><h2>{t} in Salt Lake City</h2><p>{d}</p></div></article>'
                  for i, (a, t, im, alt, d) in enumerate(blocks))
    more = [("Cedar shingles, treated for resistance against mold, rot and insects", None), ("Presidential shake roof", None), ("Roofing repair", None), ("Roof inspections", None),
            ("Gutter, soffit &amp; fascia installation and repair", "gutter-soffit-fascia.php"), ("Metal wall panels", "wall-panels.php"),
            ("Snow bars", "snow_bars.php"), ("Pavers &amp; ballasted roofs", "pavers_and_ballested.php")]
    more_html = "".join("<li>" + ('<a href="@/' + p + '">' + l + "</a>" if p else l) + "</li>" for l, p in more)
    trail = [HOME, ("Services", "services.php")]
    body = phero(trail, "Roofing Services in Salt Lake City", "Jemza Roofing offers residential and commercial roofing services in Salt Lake City and within 50 miles of it: roof replacement, metal roofing, cedar and asphalt shingles, chimneys, gutters and more. Licensed and insured, with 18 years of experience.",
                 "metal-roof-stone-home", "Metal roof on a stone home with the Wasatch Mountains behind", "Our services") + f'''
<section class="sec"><div class="wrap"><div class="svc-list">{sec}</div></div></section>
<section class="sec stone"><div class="wrap split top"><div class="reveal"><p class="label">More services</p><h2>Also on the list</h2><p class="lede">Ask about any of these when you call.</p></div>
<ul class="ticks reveal">{more_html}</ul></div></section>''' + related("services.php") + cta()
    return {"path": "services.php", "title": "Roofing Services in Salt Lake City, UT | Jemza Roofing",
            "meta": "Roofing services in Salt Lake City from Jemza Roofing: roof replacement, metal roofing, cedar and asphalt shingles, chimneys, gutters. Licensed and insured.",
            "body": body, "og": "metal-roof-stone-home", "full_biz": False,
            "schema": [crumbs_ld("services.php", trail)] + [svc_ld("services.php#" + a, t, html.unescape(d.split(" <a")[0])) for a, t, _, _, d in blocks]}


def metal():
    body = '''<h2>Metal roofs that suit the house</h2>
<p>Jemza Roofing installs metal roofing in Salt Lake City for homes and commercial buildings. We help you choose the metal roofing that fits your budget and the look you want, then install it.</p>
<p>Metal roofs are durable, attractive and energy-efficient, and they give long-lasting protection against the weather. That matters along the Wasatch Front, where a roof deals with heavy snow, spring storms and hard summer sun in the same year.</p>
<h3>What you&rsquo;ll see in our work</h3>
<ul><li><strong>Standing-seam panels</strong> on whole roofs and on porches, bays and lower roofs.</li>
<li><strong>Metal combined with shingles</strong>: shingles on the main roof, metal on the accents. It&rsquo;s one of the most common looks in our photos.</li>
<li><strong>Colors</strong> from charcoal and black to brown and blue-green.</li>
<li><strong>Finishing details</strong> that go with a metal roof: <a href="@/snow_bars.php">snow bars</a>, <a href="@/ChimneyCap-Shroud.php">chimney shrouds</a> and <a href="@/wall-panels.php">metal wall panels</a>.</li></ul>
<h3>Planning a metal roof</h3>
<p>Tell us about the building, the look you&rsquo;re after and your budget. We&rsquo;ll talk through the options in English or Spanish.</p>'''
    photos = [("metal-roof-01", "Charcoal standing-seam and shingle roof with three dormers"), ("metal-roof-02", "Stacked standing-seam roofs over the porches of a new home"),
              ("metal-roof-05", "Metal roof sections on a modern mountain home"), ("metal-roof-08", "Blue-green standing-seam roof, seen from above"),
              ("metal-roof-09", "Dark standing-seam roofs on a new build"), ("roof-project-15", "Standing-seam roof on a log home with a stone chimney"),
              ("roof-project-09", "Dark metal roof on a new build in winter"), ("metal-roof-stone-home", "Metal roof on a stone home with mountain views")]
    vids = [("gallery/metal-roofing/videos/1.mp4", "Metal roofing, clip 1"), ("gallery/metal-roofing/videos/2.mp4", "Metal roofing, clip 2"), ("gallery/metal-roofing/videos/3.mp4", "Metal roofing, clip 3")]
    faqs = [("Are metal roofs energy-efficient?", "Yes, metal roofs are energy-efficient as well as durable and attractive. Ask us how the panel and color you&rsquo;re considering perform."),
            ("Can you combine metal with a shingle roof?", "Yes. Many of our projects use shingles on the main roof and standing-seam metal on porches, bays and accent roofs.")]
    return service_page("metal-roofing.php", "Metal roofing", "Metal Roofing in Salt Lake City", "Metal Roofing in Salt Lake City, UT | Jemza Roofing",
                        "Metal roofing in Salt Lake City from Jemza Roofing: standing-seam roofs and metal accents for homes and businesses. Licensed and insured. Get a quote.",
                        "metal-roof-02", "Standing-seam metal roofs on a new home", "Jemza Roofing installs metal roofing in Salt Lake City for homes and businesses: standing-seam roofs and metal accents chosen to fit your budget and the look of the building.",
                        body, photos, vids, faqs)


def asphalt():
    body = '''<h2>Shingle roofs built for Utah weather</h2>
<p>Jemza Roofing installs asphalt shingle roofs in Salt Lake City. We use top-quality materials for weather-resistant roofs, and there&rsquo;s a variety of styles and colors to choose from, so the roof fits the house.</p>
<p>Asphalt shingles are the most familiar roof in the valley. A good install keeps the house dry, and the right color adds to the home&rsquo;s value and curb appeal.</p>
<h3>From tear-off to clean-up</h3>
<p>For a replacement, we remove and dispose of the old roof before the new one goes on. One customer, Paul, had his old roof stripped and replaced, with ridge vents and all new gutters added. Another, Aspen, mentioned that the crew &ldquo;did a great job cleaning up.&rdquo;</p>
<h3>Shingles with metal accents</h3>
<p>Many of our shingle roofs have <a href="@/metal-roofing.php">standing-seam metal</a> over a porch, bay or entry. It&rsquo;s worth asking about if you&rsquo;re replacing the roof anyway.</p>'''
    photos = [("asphalt-shingle-roof-01", "Gray shingle roof with skylights, seen from above"), ("asphalt-shingle-roof-02", "Complex gray shingle roof, top-down"),
              ("asphalt-shingle-roof-03", "Gray architectural shingles on a two-story home"), ("asphalt-shingle-roof-04", "Shingle roof on a corner-lot home"),
              ("asphalt-shingle-roof-05", "Shingles with standing-seam accents on a white farmhouse"), ("asphalt-shingle-roof-06", "Dark shingle roof with metal sections"),
              ("roof-project-01", "Ridge vent along a new shingle roof"), ("roof-project-03", "New gray shingle roof on a single-story home")]
    vids = [(f"gallery/asphalt-shingles/videos/{i}.mp4", f"Asphalt shingles, clip {i}") for i in range(1, 6)]
    return service_page("asphalt-shingles.php", "Asphalt shingles", "Asphalt Shingle Roofing in Salt Lake City", "Asphalt Shingle Roofing in Salt Lake City | Jemza Roofing",
                        "Asphalt shingle roofs in Salt Lake City from Jemza Roofing: weather-resistant materials, many styles and colors, full replacements. Licensed and insured.",
                        "asphalt-shingle-roof-03", "Gray architectural shingle roof on a two-story home", "Jemza Roofing installs asphalt shingle roofs in Salt Lake City, from full replacements with tear-off to new homes, in a variety of styles and colors.",
                        body, photos, vids)


def chimney():
    body = f'''<h2>Chimney work, from inspection to reconstruction</h2>
<p>Jemza Roofing offers chimney services in Salt Lake City, from inspection to reconstruction. The goal is a chimney that&rsquo;s safe, works well and looks good on the house, using quality materials.</p>
<p>A chimney is also where a roof is most likely to leak. The flashing, the cap and the crown all have to shed water, and the roof around it has to be built to match.</p>
<h3>What a chimney needs on top</h3>
<ul><li><strong>A cap that sheds water.</strong> Utah&rsquo;s residential code requires masonry chimneys to have a sloped concrete, metal or stone cap with a drip edge.</li>
<li><strong>A cricket on wide chimneys.</strong> Where a chimney is more than 30 inches wide (measured along the ridge) and doesn&rsquo;t sit on the ridge, the code calls for a cricket that splits water around it.</li>
<li><strong>A cap or shroud that suits the house.</strong> See our <a href="@/ChimneyCap-Shroud.php">chimney caps and shrouds</a>.</li></ul>
<p>We explain those code rules, and the one for decorative shrouds, in <a href="@/{BLOG[1]}">{BLOG[0]}</a>.</p>'''
    photos = [("chimney-01", "Stone chimney with two copper chimney pots"), ("chimney-02", "White stone chimneys with black metal caps over a brown standing-seam roof"),
              ("chimney-04", "Black chimney boxes with wood panels on a shingle roof"), ("chimney-05", "White chimney with a tapered black metal shroud"),
              ("chimney-06", "Tan chimney with a black cap above a shingle roof"), ("chimney-07", "Stone chimney with a louvered cap, hills behind"),
              ("chimney-08", "Copper cap on a stone chimney"), ("chimney-10", "Stone chimney with a black framed shroud")]
    faqs = [("Do you repair chimneys or only cap them?", "Both. Our chimney services run from inspection to reconstruction, and we also build and install caps and shrouds."),
            ("Does a masonry chimney need a cap?", "Utah&rsquo;s residential code (the 2021 IRC as adopted) requires masonry chimneys to have a concrete, metal or stone cap, sloped to shed water, with a drip edge.")]
    return service_page("chimney.php", "Chimney", "Chimney Services in Salt Lake City", "Chimney Services in Salt Lake City, UT | Jemza Roofing",
                        "Chimney services in Salt Lake City from Jemza Roofing: inspection, repair and reconstruction, flashing, caps and shrouds, done safely. Licensed and insured.",
                        "chimney-02", "White stone chimneys with black caps above a brown standing-seam roof", "Jemza Roofing offers chimney services in Salt Lake City, from inspection to reconstruction, plus the caps and shrouds that finish a chimney.",
                        body, photos, (), faqs)


def caps():
    body = f'''<h2>Custom caps and shrouds</h2>
<p>Jemza Roofing builds and installs chimney caps and shrouds in Salt Lake City. The photos on this page show the range: long black metal boxes over stone chimneys, louvered shrouds, framed shrouds with open sides, and copper bell caps.</p>
<p>Some are fitted on site; others are built ahead in the shop, as two of the photos below show, and lifted into place.</p>
<h3>Cap or shroud?</h3>
<p>A <strong>cap</strong> covers the top of the flue to keep out rain, snow, debris and animals. A <strong>shroud</strong> is a larger decorative cover that wraps the top of the chimney and becomes part of the look of the house.</p>
<p>On a factory-built (metal) chimney, the code only allows a decorative shroud that&rsquo;s listed and labeled for that specific chimney system. Our guide explains why: <a href="@/{BLOG[1]}">{BLOG[0]}</a>.</p>
<h3>Matching the roof</h3>
<p>Many of these shrouds sit on <a href="@/metal-roofing.php">standing-seam metal roofs</a> in matching colors. Copper caps weather over time, from bright copper toward brown.</p>'''
    photos = [("chimney-shroud-01", "Green metal shroud on a stone chimney above a green shingle roof"), ("chimney-shroud-02", "Black framed shroud on a cedar-clad chimney, valley view"),
              ("chimney-shroud-04", "Long black shroud on a stone chimney over a flat roof"), ("chimney-shroud-05", "Black metal shroud on a white brick chimney"),
              ("chimney-shroud-06", "Black metal shroud over a wood-clad chimney, mountains behind"), ("chimney-shroud-08", "Black bell-style cap on a white chimney in snow"),
              ("chimney-shroud-09", "Copper bell cap on a stone chimney"), ("chimney-shroud-11", "Black framed shroud on a standing-seam roof in winter"),
              ("chimney-shroud-12", "Two shrouds being built in the shop"), ("chimney-shroud-14", "Louvered black shroud on a stone chimney"),
              ("chimney-shroud-15", "Louvered shroud above a standing-seam roof"), ("chimney-shroud-17", "Framed shroud on a roof still in underlayment")]
    faqs = [("What&rsquo;s the difference between a chimney cap and a shroud?", f"A cap covers the flue opening to keep out water, debris and animals. A shroud is a bigger decorative cover around the top of the chimney. More in our guide, <a href=\"@/{BLOG[1]}\">{BLOG[0]}</a>."),
            ("Can any shroud go on a metal (factory-built) chimney?", "No. Under Utah&rsquo;s residential code, a decorative shroud on a factory-built chimney must be listed and labeled for that specific chimney system and installed per the manufacturer&rsquo;s instructions.")]
    return service_page("ChimneyCap-Shroud.php", "Chimney caps &amp; shrouds", "Chimney Caps &amp; Shrouds in Salt Lake City", "Chimney Caps & Shrouds in Salt Lake City | Jemza Roofing",
                        "Custom chimney caps and shrouds in Salt Lake City from Jemza Roofing: black metal, louvered and copper designs, built to suit the house and roof. Get a quote.",
                        "chimney-shroud-07", "Black metal chimney shroud over a wood-clad chimney", "Jemza Roofing builds and installs custom chimney caps and shrouds in Salt Lake City: black metal boxes, louvered and framed shrouds, and copper bell caps.",
                        body, photos, (), faqs)


def gutters():
    body = '''<h2>Gutters, soffit and fascia, installed and repaired</h2>
<p>Jemza Roofing installs and repairs gutters, soffit and fascia in Salt Lake City. Our photos include copper half-round gutters with round downspouts, black half-round gutters under wood soffits and new gutters on full re-roofs.</p>
<p>Gutters move water off the roof and away from the walls and foundation. Soffit and fascia close in the roof edge and carry the gutter, so it makes sense to look at all three together.</p>
<h3>In our customers&rsquo; words</h3>
<p>R P had new gutters put on an old, crooked house. They wrote that the crew &ldquo;even let us know about a tricky part of our roof that might need an additional spout&rdquo; and offered to come back and add it if there was any leakage. Aspen&rsquo;s review mentions the roof <em>and</em> the gutters.</p>
<h3>Copper</h3>
<p>Copper gutters start bright and darken with age. They suit stone, brick and timber houses, and several of the photos below show them on all three.</p>'''
    photos = [("gutter-soffit-fascia-01", "Copper gutter and downspout on a barn-wood garage"), ("gutter-soffit-fascia-02", "Copper gutters on a white and stone house"),
              ("gutter-soffit-fascia-03", "Copper gutter along a shingle roof edge"), ("gutter-soffit-fascia-04", "Black half-round gutter under a wood soffit"),
              ("gutter-soffit-fascia-05", "Copper gutter and downspout, with snow bars on the roof above"), ("gutter-soffit-fascia-07", "Copper half-round gutter corner, close up"),
              ("gutter-soffit-fascia-08", "Installing a copper gutter on a brick home"), ("gutter-soffit-fascia-10", "Copper downspout on a brick column by the front door")]
    vids = [(f"gallery/gutter-soffit-fascia/videos/{i}.mp4", f"Gutter, soffit and fascia, clip {i}") for i in range(1, 4)]
    return service_page("gutter-soffit-fascia.php", "Gutter, soffit &amp; fascia", "Gutter, Soffit &amp; Fascia in Salt Lake City", "Gutter Installation in Salt Lake City, UT | Jemza Roofing",
                        "Gutter, soffit and fascia installation and repair in Salt Lake City from Jemza Roofing, including copper half-round gutters. Licensed and insured. Call.",
                        "gutter-soffit-fascia-01", "Copper gutter and downspout on a barn-wood garage", "Jemza Roofing installs and repairs gutters, soffit and fascia in Salt Lake City, from new gutters on a re-roof to copper half-round systems.",
                        body, photos, vids)


def walls():
    body = '''<h2>Metal on the walls, not just the roof</h2>
<p>Jemza Roofing installs metal wall panels in Salt Lake City. The project in our photos shows dark metal panels laid in a shingle-style pattern on the upper walls of a modern home, set against natural stone below and a standing-seam roof above.</p>
<p>Metal wall panels are tough and low-maintenance, and they let the wall and the roof share one material and color. On a house with a metal roof, that gives the whole building one look.</p>
<h3>Roof and wall together</h3>
<p>Because we do the <a href="@/metal-roofing.php">metal roof</a> as well, the details where the wall meets the roof can be planned as one job.</p>'''
    photos = [(f"metal-wall-panels-{i:02d}", c) for i, c in enumerate(["Dark metal wall panels on the upper floor of a modern home", "Metal wall panels and large windows, with the hills behind",
                                                                        "Metal panels above natural stone", "Panel pattern around the windows", "Finished wall with a standing-seam roof", "The finished home from the yard"], 1)]
    vids = [(f"gallery/wall-panels/videos/{i}.mp4", f"Wall panels, clip {i}") for i in range(1, 6)]
    return service_page("wall-panels.php", "Metal wall panels", "Metal Wall Panels in Salt Lake City", "Metal Wall Panels in Salt Lake City, UT | Jemza Roofing",
                        "Metal wall panels in Salt Lake City from Jemza Roofing: dark metal cladding matched to the roof, for modern homes and commercial buildings. Get a quote.",
                        "metal-wall-panels-02", "Dark metal wall panels on a modern home", "Jemza Roofing installs metal wall panels in Salt Lake City, cladding walls in metal that matches the roof.",
                        body, photos, vids)


def snow():
    body = '''<h2>Snow bars for metal roofs</h2>
<p>Jemza Roofing installs snow bars in Salt Lake City. Our photos show them on standing-seam metal roofs over the entries and walkways of mountain homes.</p>
<p>Snow slides off a smooth metal roof far more easily than off shingles. Snow bars run across the panels near the eaves and hold the snow in place, so it melts off gradually instead of dropping in one heavy sheet onto a walkway, a deck, a lower roof or the gutters.</p>
<h3>Where they matter most</h3>
<ul><li>Above doors, paths and driveways.</li><li>Over decks and lower roofs.</li><li>Above gutters, which a sliding sheet of snow can tear off.</li></ul>
<p>If you&rsquo;re putting on a <a href="@/metal-roofing.php">metal roof</a>, it&rsquo;s easiest to plan the snow bars at the same time.</p>'''
    photos = [("snow-bars-01", "Snow bars on a standing-seam roof above a stone and wood home"), ("snow-bars-02", "Snow bars along the eaves of a metal roof"),
              ("gutter-soffit-fascia-06", "Snow bars on a metal roof above a copper gutter"), ("metal-roof-09", "Standing-seam roofs on a new mountain home")]
    faqs = [("Why do metal roofs need snow bars?", "Snow slides off metal much more easily than off shingles. Snow bars hold it on the roof so it melts off gradually instead of falling in one sheet onto people, decks or gutters."),
            ("Can snow bars be added to an existing metal roof?", "Call us with photos of the roof and we&rsquo;ll talk it through.")]
    return service_page("snow_bars.php", "Snow bars", "Snow Bars for Metal Roofs in Salt Lake City", "Snow Bars for Metal Roofs in Salt Lake City | Jemza Roofing",
                        "Snow bars for metal roofs in Salt Lake City from Jemza Roofing: hold snow in place so it melts off instead of sliding onto walkways and decks. Call us.",
                        "metal-roof-09", "Standing-seam metal roofs on a new mountain home", "Jemza Roofing installs snow bars on metal roofs in Salt Lake City, so snow melts off gradually instead of sliding onto walkways, decks and gutters.",
                        body, photos, (), faqs)


def pavers():
    body = '''<h2>Pavers and ballast on flat roofs</h2>
<p>Jemza Roofing does paver and ballasted roof work in Salt Lake City. Our photos show a grid of pavers turning a flat roof into a usable deck, and gravel ballast on a lower flat roof next to a shingle roof.</p>
<p>On a ballasted roof, the weight of loose stone or pavers holds the roof membrane in place instead of fasteners or glue. Pavers also make a walking surface, which is why they&rsquo;re used for rooftop decks.</p>
<h3>Flat roofs with a view</h3>
<p>Rooftop decks often share the roof with a chimney. The long black shroud in the photo below sits right beside a paver deck; see more in <a href="@/ChimneyCap-Shroud.php">chimney caps &amp; shrouds</a>.</p>'''
    photos = [("ballasted-paver-roof-02", "Paver grid on a flat roof deck"), ("ballasted-paver-roof-01", "Gravel ballast on a lower flat roof beside a shingle roof"),
              ("rooftop-chimney-shroud-deck", "Flat roof deck with a long black chimney shroud"), ("chimney-shroud-04", "Stone chimney and shroud over a flat roof")]
    return service_page("pavers_and_ballested.php", "Pavers &amp; ballasted roofs", "Pavers &amp; Ballasted Roofs in Salt Lake City", "Pavers & Ballasted Roofs in Salt Lake City | Jemza Roofing",
                        "Paver and ballasted flat roofs in Salt Lake City from Jemza Roofing: rooftop paver decks and gravel ballast on flat and low-slope roofs. Licensed and insured.",
                        "rooftop-chimney-shroud-deck", "Flat roof deck with a long black chimney shroud", "Jemza Roofing does paver and ballasted roof work in Salt Lake City: rooftop paver decks and gravel ballast on flat and low-slope roofs.",
                        body, photos)


def about():
    trail = [HOME, ("About", "about.php")]
    body = phero(trail, "About Jemza Roofing", "Jemza Roofing is a licensed and insured roofing company based in Salt Lake City, founded in Millcreek, Utah, with 18 years of experience in residential and commercial roofing.",
                 "new-roof-01", "Metal and shingle roof on a new mountain home", "About us") + f'''
<section class="sec"><div class="wrap split top post-grid"><div class="prose reveal">
<h2>Founded in Millcreek</h2>
<p>Founded in Millcreek, Utah, Jemza Roofing has built a strong reputation for reliability in the roofing industry. Our team takes pride in good craftsmanship and in solutions that fit what each client needs.</p>
<p>Whether you&rsquo;re a homeowner improving the curb appeal of your property or a business owner protecting your investment, we work on both: residential and commercial roofing.</p>
<h2>How we work</h2>
<p>Our tagline is &ldquo;Quality over quantity always&rdquo;. Our customers&rsquo; reviews mention the things that tagline is about: Omar being responsive and easy to reach, starting and finishing on schedule, not upselling, and a crew that cleans up after itself.</p>
<p>We offer bilingual attention in English and Spanish, we&rsquo;re licensed and insured, and we stand behind our work with a satisfaction guarantee.</p>
<h2>Where we work</h2>
<p>Our office is at {S["street"]}, {S["city"]}, {S["st"]} {S["zip"]}, and we cover 50 miles around Salt Lake City.</p>
</div><aside class="reveal side">{WHY}<a class="btn" href="@/{CONTACT}">Contact us {ARROW}</a></aside></div></section>
<section class="sec stone"><div class="wrap">{gallery([("roof-project-11", "Gray shingles and a metal porch roof on a large home"), ("roof-project-10", "White stone chimney with a black metal cap"), ("new-roof-04", "Lifting materials to a mountain-home roof"), ("roof-project-13", "Metal and shingle roof on a new home")])}</div></section>
''' + quotes_html("What customers say", 2) + cta()
    return {"path": "about.php", "title": "About Jemza Roofing | Roofers in Salt Lake City, UT",
            "meta": "Jemza Roofing was founded in Millcreek, Utah: 18 years of residential and commercial roofing, licensed and insured, bilingual in English and Spanish. Call us.",
            "body": body, "og": "new-roof-01", "full_biz": True,
            "schema": [crumbs_ld("about.php", trail), {"@type": "AboutPage", "@id": U + "about.php#webpage", "url": U + "about.php", "name": "About Jemza Roofing", "about": {"@id": U + "#organization"}}]}


def portfolio():
    trail = [HOME, ("Portfolio", "portfolio.php")]
    items = ([(f"roof-project-{i:02d}", c) for i, c in [(11, "Gray shingles with a metal porch roof"), (12, "Estate with metal and shingle roofs"), (13, "New home with metal and shingle roofs"),
              (14, "Large home with standing-seam sections"), (15, "Standing-seam roof on a log home"), (16, "Brown roof on a large home"), (17, "Copper standing-seam bay roof"),
              (10, "Stone chimney with a black cap"), (6, "Shingle roof in winter"), (7, "Brick home with a new shingle roof"), (8, "New build sheathed and ready for roofing"),
              (9, "Dark metal roof on a new build"), (5, "Addition framed and sheathed"), (2, "Shingle roof with new vents"), (4, "Roof vent on new shingles")]] +
             [(f"new-roof-{i:02d}", c) for i, c in [(1, "Metal and shingle mountain home"), (2, "White farmhouse with a metal dormer"), (3, "Gray shingle home with stone"), (5, "White home with dark shingles")]] +
             [("snow-covered-new-roof", "New roof under snow"), ("shingle-roof-new-build", "Shingle roof on a new build")])
    vids = [("video/1.mp4", "Project video 1"), ("video/2.mp4", "Project video 2"), ("video/slider.mp4", "Project video 3")]
    body = phero(trail, "Roofing Portfolio: Salt Lake City Projects", "Recent Jemza Roofing projects in and around Salt Lake City: metal and shingle roofs, chimneys, gutters and wall panels, mostly photographed from the air.",
                 "roof-project-12", "Estate with metal and shingle roofs, seen from the air", "Portfolio") + f'''
<section class="sec"><div class="wrap">{gallery(items, "grid masonry")}</div></section>
<section class="sec dark"><div class="wrap"><div class="head reveal"><p class="label light">Video</p><h2>Project videos</h2></div><div class="vids">{"".join(video(p, c) for p, c in vids)}</div></div></section>
<section class="sec stone"><div class="wrap"><div class="head reveal"><p class="label">By service</p><h2>More photos by service</h2></div><div class="chips">{"".join(f'<a href="@/{p}">{l}</a>' for l, p, _, _ in SERVICES)}</div></div></section>''' + cta()
    return {"path": "portfolio.php", "title": "Roofing Portfolio | Salt Lake City Projects | Jemza Roofing",
            "meta": "Photos and videos of Jemza Roofing projects around Salt Lake City: metal and shingle roofs, custom chimney shrouds, copper gutters and metal wall panels.",
            "body": body, "og": "roof-project-12", "full_biz": False,
            "schema": [crumbs_ld("portfolio.php", trail), {"@type": "CollectionPage", "@id": U + "portfolio.php#webpage", "url": U + "portfolio.php", "name": "Jemza Roofing portfolio"}]}


def testimonials():
    trail = [HOME, ("Reviews", "testimonials.php")]
    body = phero(trail, "Jemza Roofing Reviews", "What customers in the Salt Lake City area say about working with Jemza Roofing, Omar and the crew.",
                 "asphalt-shingle-roof-05", "Shingle roof with metal accents on a white farmhouse", "Reviews") + quotes_html(head=False) + f'''
<section class="sec stone"><div class="wrap split top"><div class="reveal"><p class="label">Your turn</p><h2>Worked with us?</h2>
<p class="lede">We&rsquo;d love to hear how it went. Reviews on our Google Business Profile help other homeowners find us.</p></div>
<div class="reveal"><a class="btn" href="{S["map"]}" rel="noopener">Leave a review on Google {ARROW}</a><p class="small">Or call the office at <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></div></section>''' + cta()
    reviews_ld = [{"@type": "Review", "reviewBody": q, "author": {"@type": "Person", "name": a}, "itemReviewed": {"@id": U + "#organization"}} for q, a in REVIEWS]
    return {"path": "testimonials.php", "title": "Jemza Roofing Reviews | Salt Lake City Roofing Company",
            "meta": "Read what Salt Lake City homeowners say about Jemza Roofing: on-time crews, no upselling, clean job sites, new roofs and gutters. Leave your own review.",
            "body": body, "og": "asphalt-shingle-roof-05", "full_biz": False, "schema": [crumbs_ld("testimonials.php", trail)] + reviews_ld}


def contact():
    trail = [HOME, ("Contact", "contact.php")]
    body = phero(trail, "Contact Jemza Roofing in Salt Lake City", f"Call the office at {S['phone']}, email {S['email']} or send a message below. We speak English and Spanish and cover 50 miles around Salt Lake City.",
                 "metal-roof-stone-home", "Metal roof on a stone home with mountains behind", "Contact") + f'''
<section class="sec"><div class="wrap split top">
<div class="reveal contact-card"><h2>Office</h2>
<dl><dt>Address</dt><dd><address>{S["name"]}<br>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</address><a href="{S["map"]}" rel="noopener">Directions on Google Maps</a></dd>
<dt>Phone</dt><dd><a class="big" href="tel:{S["tel"]}">{S["phone"]}</a></dd>
<dt>Email</dt><dd><a href="mailto:{S["email"]}">{S["email"]}</a></dd>
<dt>Language</dt><dd>English / <span lang="es">Espa&ntilde;ol</span></dd>
<dt>Service area</dt><dd>50 miles around Salt Lake City, Utah 84115</dd>
<dt>Payment</dt><dd>Cash, card, Square and check</dd></dl></div>
<div class="reveal">{contact_form("Send a message")}</div></div></section>'''
    return {"path": "contact.php", "title": "Contact Jemza Roofing | Salt Lake City, UT Roofers",
            "meta": "Contact Jemza Roofing at 2212 S West Temple Ste. #38, Salt Lake City, UT 84115. Call (385) 261-2942 or send a message. We speak English and Spanish.",
            "body": body, "og": "metal-roof-stone-home", "full_biz": True,
            "schema": [crumbs_ld("contact.php", trail), {"@type": "ContactPage", "@id": U + "contact.php#webpage", "url": U + "contact.php", "name": "Contact Jemza Roofing", "about": {"@id": U + "#organization"}}]}


def notfound():
    body = f'''<section class="sec"><div class="wrap statement"><p class="label">404</p><h1>That page isn&rsquo;t here.</h1>
<p class="big">Try the <a href="@/">home page</a>, our <a href="@/services.php">services</a> or the <a href="@/portfolio.php">portfolio</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p></div></section>'''
    return {"path": "404.html", "title": "Page Not Found | Jemza Roofing", "meta": "This page isn't on the Jemza Roofing site. Try the home page, services or portfolio, or call the office.",
            "body": body, "robots": "noindex, follow", "sitemap": False, "full_biz": False}


def make_pages():
    return [home(), about(), services(), metal(), asphalt(), chimney(), caps(), gutters(), walls(), snow(), pavers(),
            portfolio(), testimonials(), contact(), p_blog.page(), notfound()]
