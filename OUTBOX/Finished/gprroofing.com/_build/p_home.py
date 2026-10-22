import re, html
from build import U, S, ARROW, PHONE, CHECK, IMG, IMGMAP, CONTACT, img, faq_html, faq_ld, quotes_html, cta, quote_form
import p_blog

# Main keyword: roofing company west valley city (+ roofers / roofing contractor west valley city), per the 14 Oct report.
# Every fact is from the client's own pages and FAQs (home, services, about, metal, asphalt, TPO, repair, replacement), 17 Oct 2026.

POOL = ["6937c156578cc788f4a548a0", "ezy-watermark-12-08-2022-08-31-39pm-heic", "ezy-watermark-25-11-2021-08-31-50am-heic", "ezy-watermark-24-03-2022-07-25-05am-heic",
        "ezy-watermark-18-03-2022-10-52-28pm-heic", "ezy-watermark-02-12-2021-11-02-02pm-heic-1024x768-1", "ezy-watermark-09-12-2021-03-25-26pm-heic",
        "ezy-watermark-10-06-2022-01-35-58pm-heic", "6937c156578cc7aa71a5489f", "ezy-watermark-01-03-2022-09-32-45pm-heic", "6937c156e03e9d0602688906",
        "ezy-watermark-18-12-2021-03-05-00pm-heic"]  # Go Pro's own job photos, from the contact-sheet review


def HERO_POOL():
    names = [n for n in POOL if n in IMG]
    if not names:
        names = sorted((n for n in IMG if IMG[n][0] >= 900 and IMG[n][0] > IMG[n][1] and "logo" not in n), key=lambda n: -IMG[n][0])
    return names


PICK = [("asphalt", "Asphalt shingles", "asphalt-shingle-roofing-west-valley-city-ut/",
         [("Lasts about", "20&ndash;30 years; premium architectural up to 50"), ("Typical cost in Utah", "$8,000&ndash;$15,000 for a new roof"), ("Best for", "Pitched roofs")]),
        ("metal", "Metal", "metal-roofing-contractors-west-valley-city-ut/",
         [("Lasts about", "40&ndash;70 years"), ("Typical cost in Utah", "Higher up front than shingles; often cheaper long term"), ("Best for", "Long life, heavy snow")]),
        ("tpo", "TPO membrane", "tpo-roofing-contractors-salt-lake-city-utah/",
         [("Lasts about", "20&ndash;30 years"), ("Typical cost in Utah", "$5&ndash;$12 per sq. ft. installed"), ("Best for", "Flat and low-slope roofs")])]
WALL = ["ezy-watermark-12-08-2022-08-31-39pm-heic", "ezy-watermark-25-11-2021-08-31-50am-heic", "ezy-watermark-24-03-2022-07-25-05am-heic",
        "ezy-watermark-18-03-2022-10-52-28pm-heic", "ezy-watermark-09-12-2021-03-25-26pm-heic", "ezy-watermark-10-06-2022-01-35-58pm-heic",
        "ezy-watermark-01-03-2022-09-32-45pm-heic", "ezy-watermark-18-12-2021-03-05-00pm-heic"]


def build(r, rec, posts, tests):
    pool = HERO_POOL()
    hero = pool[0]
    tiles = [("Roof repair", "roof-repair-west-valley-city/", "Leaks, storm and weather damage, and emergency roof repair. Most repairs $300&ndash;$1,500."),
             ("Roof replacement", "roof-replacement-services-utah/", "Asphalt, metal, TPO, tile and flat roofs. Most replacements take 1&ndash;3 days."),
             ("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/", "Residential and commercial metal roofs, installed and repaired."),
             ("Asphalt shingles", "asphalt-shingle-roofing-west-valley-city-ut/", "Shingle roofs from an Owens Corning Preferred Contractor."),
             ("TPO flat roofs", "tpo-roofing-contractors-salt-lake-city-utah/", "Installation, repair and replacement of TPO membrane roofs."),
             ("Roof installation", "residential-roof-installation-utah/", "New roofs for home builds and additions. Most homes done in 1&ndash;2 days."),
             ("Inspections &amp; reports", "services/", "Free roof inspections, plus official inspection reports for buying or selling a home."),
             ("Swamp cooler removal", "services/", "Swamp cooler removal and roof patching, along with general roof repairs.")]
    tile_html = "".join(f'<a class="tool reveal" href="@/{p}"><span class="model">GPR&middot;{i+1:02d}</span><b>{n}</b><span class="d">{d}</span><em>Learn more {ARROW}</em></a>' for i, (n, p, d) in enumerate(tiles))
    tabs = "".join(f'<button type="button" role="tab" aria-selected="{"true" if i == 0 else "false"}" data-k="{k}"{"" if i == 0 else " tabindex=\"-1\""}><span>0{i+1}</span>{n}</button>' for i, (k, n, p, rows) in enumerate(PICK))
    panels = "".join(f'''<div class="pick-panel" data-k="{k}"{"" if i == 0 else " hidden"}><p class="pick-name">{n}</p><dl>{"".join(f"<div><dt>{a}</dt><dd>{b}</dd></div>" for a, b in rows)}</dl><a class="btn" href="@/{p}">{n} {ARROW}</a></div>''' for i, (k, n, p, rows) in enumerate(PICK))
    chart = '''<div class="tablebox chooser"><table><caption>Three roof types side by side</caption><thead><tr><th>Roof type</th><th>Lasts about</th><th>Typical cost in Utah</th><th>Best for</th></tr></thead><tbody>
<tr><td><a href="@/asphalt-shingle-roofing-west-valley-city-ut/">Asphalt shingles</a></td><td>20&ndash;30 years; premium architectural up to 50</td><td>$8,000&ndash;$15,000 for a new roof</td><td>Pitched roofs</td></tr>
<tr><td><a href="@/metal-roofing-contractors-west-valley-city-ut/">Metal</a></td><td>40&ndash;70 years</td><td>Higher up front than shingles; often cheaper long term</td><td>Long life, heavy snow</td></tr>
<tr><td><a href="@/tpo-roofing-contractors-salt-lake-city-utah/">TPO membrane</a></td><td>20&ndash;30 years</td><td>$5&ndash;$12 per sq. ft. installed</td><td>Flat and low-slope roofs</td></tr>
</tbody></table></div>'''
    wall = "".join(f'<figure class="snap reveal">{img(n, "Finished roof by Go Pro Roofing in the Salt Lake Valley")}<figcaption>Job {i+1:02d}</figcaption></figure>' for i, n in enumerate([w for w in WALL if w in IMG]))
    hf = r.get("faqs") or []
    latest = [(p_blog.PATH, "How Are Valleys Done on a Metal Roof?")] + [(pp, re.sub(r"<[^>]+>", "", pr["h1"] or pr["title"].split(" – ")[0])) for pp, pr in posts[:2]]
    post_html = "".join(f'<li><a href="@/{pp}">{html.escape(t)} {ARROW}</a></li>' for pp, t in latest)
    certs = [("Owens Corning Preferred Contractor", "Certified to install Owens Corning roofing systems"),
             ("Master Roofer Certified", "Recognized by Owens Corning, CertainTeed and GAF"),
             ("Licensed &amp; insured", "Serving Salt Lake and Utah counties"),
             ("Latino-owned &amp; locally operated", "Excelencia revolucionaria")]
    cert_html = "".join(f'<li><span class="n">{i+1:02d}</span><div><b>{a}</b><small>{b}</small></div></li>' for i, (a, b) in enumerate(certs))
    body = f'''
<section class="hero"><div class="hero-bg">{img(hero, "Go Pro Roofing crew tearing off and re-roofing a brick home", priority=True)}</div><div class="hero-slash" aria-hidden="true"></div>
<div class="wrap hero-in">
<div class="hero-text"><p class="tag">Free estimates &middot; 24/7 emergency service</p>
<h1>Roofing company in West Valley City. <span>Pro-grade roofs.</span></h1>
<p class="lede">Go Pro Roofing is a roofing company in West Valley City, Utah, serving homeowners across Salt Lake and Utah counties with roof repair, roof replacement and metal roofing. Licensed, insured, and an Owens Corning Preferred Contractor.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div></div>
<dl class="plate"><div class="plate-h"><span>Spec plate</span><span>GPR</span></div>
<div><dt>Workmanship warranty</dt><dd>5 yr</dd></div><div><dt>Material warranties</dt><dd>up to 50 yr</dd></div>
<div><dt>Most replacements</dt><dd>1&ndash;3 days</dd></div><div><dt>Estimate &amp; inspection</dt><dd>$0</dd></div></dl>
</div></section>

<section class="sec lineup"><div class="wrap">
<div class="head row reveal"><div><p class="tag dark">The lineup</p><h2>Roofers in West Valley City, <span>for every kind of roof</span></h2></div><p class="head-note">As a roofing contractor in West Valley City, we handle everything from a single leak to a full tear-off, for homes and businesses across the Salt Lake Valley.</p></div>
<div class="tools">{tile_html}</div>
</div></section>

<section class="sec picker"><div class="wrap">
<div class="head row reveal"><div><p class="tag">Pick the right roof</p><h2>Pick the right roof <span>for the job</span></h2></div><p class="head-note">Three roof types we install most. Figures come from our own service pages; your roof&rsquo;s size, pitch and materials set the real price.</p></div>
<div class="pick reveal"><div class="pick-tabs" role="tablist" aria-label="Roof type">{tabs}</div><div class="pick-out">{panels}</div></div>
<details class="chart-toggle"><summary>Compare all three in a table</summary>{chart}</details>
<p class="tlink-row"><a class="tlink" href="@/{p_blog.PATH}">Going metal? See how metal roof valleys are built {ARROW}</a></p>
</div></section>

<section class="sec dark creds"><div class="wrap split">
<div class="reveal"><p class="tag">Certified &amp; local</p><h2>Credentials that come <span>with every roof</span></h2>
<ol class="certs">{cert_html}</ol></div>
<div class="reveal proof"><p class="tag">Photo-documented</p><h3>See every step, even the parts that get covered</h3>
<blockquote>&ldquo;They took tons of photos before/during/after that were shared with me on a Google link which made it easy to share with my insurance company. My roof took one day which was glorious!&rdquo;</blockquote><p class="who">Misty Jensen, Google review</p>
<figure class="proof-img">{img("official-inspection-reports-for-selling-purchasing-homes", "Inspection photo with blown ridge caps circled in red")}<figcaption>From a Go Pro inspection report: blown ridge caps, circled</figcaption></figure></div>
</div></section>

<section class="sec jobs"><div class="wrap">
<div class="head row reveal"><div><p class="tag dark">Job site wall</p><h2>Roofs across <span>the Salt Lake Valley</span></h2></div><p class="head-note">Bluffdale, Sandy, Provo, Taylorsville, West Jordan and right here in West Valley City. <a href="@/gallery/">See the gallery</a>.</p></div>
<div class="wall">{wall}</div>
</div></section>
''' + quotes_html(tests, "What homeowners say about Jos&eacute;&rsquo;s team") + f'''
<section class="sec white"><div class="wrap split top">
<div class="reveal"><p class="tag dark">Where we work</p><h2>West Valley City <span>and the whole valley</span></h2>
<p class="lede">Based at {S["street"]} in West Valley City, we serve homeowners across Salt Lake and Utah counties, including West Valley City, Sandy, Draper, Murray, Herriman and Riverton.</p>
<div class="chips"><span>West Valley City</span><span>Salt Lake City</span><span>Sandy</span><span>Draper</span><span>Murray</span><span>Herriman</span><span>Riverton</span><span>Taylorsville</span><span>West Jordan</span><span>Utah County</span></div></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap split top">
<div class="reveal"><p class="tag dark">Questions</p><h2>Common questions</h2><p class="lede">From the blog:</p><ul class="blog-links">{post_html}</ul>
<a class="btn navy" href="@/{CONTACT}">Contact us {ARROW}</a></div>
<div class="reveal">{faq_html(hf[:6])}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company in West Valley City, UT | Go Pro Roofing",
            "meta": "Go Pro Roofing is a roofing company in West Valley City, UT: roof repair, replacement and metal roofs across Salt Lake and Utah counties. Free estimates.",
            "body": body, "og": hero,
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]}]
                      + ([faq_ld(hf[:6])] if hf else []),
            "full_biz": True}
