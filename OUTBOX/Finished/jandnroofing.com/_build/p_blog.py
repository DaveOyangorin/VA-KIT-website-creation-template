from build import U, BIZ_ID, S, ARROW, INSPECT, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

# Same URL pattern as the client's other posts (/<slug>/ at the site root).
PATH = "how-far-should-shingles-overhang-the-drip-edge/"
TITLE = "How Far Should Shingles Overhang the Drip Edge?"
ARMA = "https://www.asphaltroofing.org/installation-of-drip-edge-at-eaves-and-rakes/"
PACIFIC = "https://pacificmo.gov/DocumentCenter/View/990/Roof-Code"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"

# Main keyword: "how far should shingles overhang the drip edge" (+ shingle overhang drip edge, drip edge eaves vs rakes).
# Ties to the client's own warranty page, which gives the shingle manufacturer's 1/4 inch overhang guidance.
# Not targeted (owned by other pages, linked only): roofing company west valley city (home), roof repair / roofing repairs
# west valley city (services/roofing-repairs/), roof replacement, re-roof (overlay), and the many "roofing salt lake city" posts.

FAQ = [
    ("How far should shingles hang over the drip edge?",
     "For a standard L-shaped (90-degree) drip edge, the Asphalt Roofing Manufacturers Association says starter and field shingles should extend 1/4 to 3/4 inch beyond the drip edge at both eaves and rakes. Always check your shingle manufacturer&rsquo;s instructions too."),
    ("Is drip edge required by code?",
     "Under the International Residential Code&rsquo;s shingle section (R905.2.8.5 in the 2018 edition), a drip edge shall be provided at eaves and rake edges of shingle roofs. Utah adopted the 2021 IRC; your city&rsquo;s building department enforces it."),
    ("Does drip edge go over or under the underlayment?",
     "Under at the eaves and over at the rakes. The code and ARMA both describe it that way: underlayment laps over the drip edge along the eaves and goes under the drip edge along the rakes."),
    ("What happens if shingles don&rsquo;t overhang enough?",
     "J &amp; N&rsquo;s warranty notes put it simply: if the overhang isn&rsquo;t done, water can roll back under the shingles and cause leaks at the eaves and rakes."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> with a standard L-shaped metal drip edge, shingles should overhang it by <strong>1/4 to 3/4 inch</strong> at the eaves and rakes, according to the Asphalt Roofing Manufacturers Association (ARMA). The drip edge itself must extend at least 1/4 inch below the roof sheathing under the residential building code. Too little overhang lets water roll back under the shingles.</div>

<p>It&rsquo;s a small detail, measured in fractions of an inch. It&rsquo;s also one of the first places a roof starts to leak when it&rsquo;s done wrong.</p>
<p>Our own warranty notes mention it for that reason: the shingle manufacturer recommends hanging shingles 1/4 inch over the drip metal at the eaves and at the rakes, and if that isn&rsquo;t done, water can roll back under the shingles and cause leaks at the roof edges.</p>
<p>Here&rsquo;s what the drip edge does, what the industry and the code say about it, and what to look for on your own roof.</p>

<h2>What a drip edge is and why it matters</h2>
<p>A drip edge is the strip of bent metal along the edges of a roof. It covers the edge of the roof deck and gives water a clean line to drip off, away from the fascia and the wood underneath.</p>
<p>The shingles sit on top of it. If they stop short, water can wick back along the underside of the shingle and onto the deck. That&rsquo;s why the industry gives a range, not a single number.</p>

<h2>How far shingles should overhang the drip edge</h2>
<p>ARMA&rsquo;s guidance, published in May 2025, depends on the shape of the drip edge (<a href="{ARMA}" rel="noopener">ARMA: Installation of Drip Edge at Eaves and Rakes</a>):</p>
<div class="tablebox"><table><thead><tr><th>Edge detail</th><th>Eaves</th><th>Rakes</th></tr></thead><tbody>
<tr><td>L-shaped (90&deg;) drip edge</td><td>Starter and field courses extend 1/4&Prime;&ndash;3/4&Prime; beyond the drip edge</td><td>1/4&Prime;&ndash;3/4&Prime; beyond the drip edge</td></tr>
<tr><td>T- or D-shaped drip edge</td><td>Up to 3/4&Prime; past the edge, or trimmed flush</td><td>May be trimmed flush</td></tr>
<tr><td>No drip edge</td><td>3/8&Prime;&ndash;1&Prime; overhang</td><td>3/8&Prime;&ndash;1&Prime; overhang</td></tr>
</tbody></table></div>
<p>ARMA also says shingle manufacturers&rsquo; requirements should be followed, so the product&rsquo;s own instructions have the final say.</p>

<figure>{{IMG1}}<figcaption>The roof edge: drip edge below, shingles overhanging it.</figcaption></figure>

<h2>What the building code says</h2>
<p>Utah adopted the 2021 International Residential Code for homes, effective July 1, 2023 (<a href="{ICC}" rel="noopener">International Code Council</a>). The code&rsquo;s drip edge section, as quoted word for word in a city&rsquo;s published copy of the 2018 edition, reads (<a href="{PACIFIC}" rel="noopener">2018 IRC Section R905, City of Pacific, Missouri</a>):</p>
<ul>
<li>A drip edge shall be provided at eaves and rake edges of shingle roofs.</li>
<li>Adjacent pieces shall be overlapped not less than 2 inches.</li>
<li>Drip edges shall extend not less than 1/4 inch below the roof sheathing and at least 2 inches back onto the roof deck.</li>
<li>They shall be mechanically fastened at not more than 12 inches on center.</li>
<li>Underlayment shall be installed over the drip edge along eaves and under the drip edge along rake edges.</li>
</ul>
<p>Your city&rsquo;s building department enforces the edition it has adopted, so a quick call there settles any local detail.</p>

<h2>Eaves vs. rakes: the underlayment order</h2>
<p>This is the part that trips people up. At the <strong>eaves</strong> (the bottom edges), the drip edge goes on first and the underlayment laps over it, so water running down the underlayment lands on top of the metal. At the <strong>rakes</strong> (the sloped side edges), the underlayment goes down first and the drip edge goes over it, so wind-driven rain can&rsquo;t get behind it.</p>
<p>ARMA notes one variation: some manufacturers or local codes allow the drip edge over the underlayment at the eave, with a 12-inch strip of self-adhering underlayment underneath, so the metal sits between two layers.</p>

<h2>Fastening the drip edge</h2>
<p>The code says fasteners no more than 12 inches apart. ARMA&rsquo;s guidance is tighter: roofing nails every 8 to 10 inches, and never nail into the vertical face of the drip edge.</p>

<h2>Signs your roof edge wasn&rsquo;t done right</h2>
<p>You can check a lot from the ground or a ladder at the eave:</p>
<ul>
<li>Shingles that stop short of the metal, or no drip edge at all</li>
<li>Water stains or soft spots on the fascia board below the edge</li>
<li>Peeling paint or rot right under the roof line</li>
</ul>
<p>Any of these is worth a closer look before the next storm. Our <a href="@/services/roof-inspections-maintenance/">roof inspections and maintenance</a> visits check the edges as a matter of course, and if a <a href="@/services/roofing-repairs/">repair</a> is all you need, we&rsquo;ll tell you.</p>

<h2>Drip edge and your shingle warranty</h2>
<p>Manufacturer warranties depend on the roof being installed to the manufacturer&rsquo;s instructions, and edge details are part of those instructions. J &amp; N Roofing installs GAF systems with the GAF System Plus Warranty; see our <a href="@/warranty-support/">warranty support</a> page for how claims work.</p>

<h2>Questions about drip edge and shingle overhang</h2>
{faq_html(FAQ)}

<h2>Want someone to look at your roof edges?</h2>
<p>Call <a href="tel:{S["tel"]}">{S["phone"]}</a> for a free on-site inspection and estimate, or <a href="@/{INSPECT}">request one online</a>. For something that can&rsquo;t wait, our 24-hour support line is <a href="tel:{S["tel24"]}">{S["phone24"]}</a>.</p>

<div class="sources"><h3>Sources</h3><ol>
<li><a href="{ARMA}" rel="noopener">Asphalt Roofing Manufacturers Association (ARMA), &ldquo;Installation of Drip Edge at Eaves and Rakes,&rdquo; 6 May 2025</a></li>
<li><a href="{PACIFIC}" rel="noopener">City of Pacific, Missouri, &ldquo;2018 IRC Section R905 Requirements for Roof Coverings&rdquo; (Ordinance 3181, 7 April 2020)</a>, quoting IRC R905.2.8.5</li>
<li><a href="{ICC}" rel="noopener">International Code Council, &ldquo;Utah Enhances Building Safety Statewide With Adoption of 2021 International Codes,&rdquo; 21 July 2023</a></li>
<li><a href="@/warranty-support/">J &amp; N Roofing Maintenance, Warranty Support</a> (shingle manufacturer overhang guidance)</li>
</ol></div>
'''


def new_post(hero, inline=None):
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("Shingle Overhang &amp; Drip Edge", PATH)]
    art = ART.replace("{IMG1}", img(inline or hero, "Roof edge with shingles over the drip edge"))
    return {"path": PATH, "canonical": url, "ogtype": "article", "og": hero, "modified": "2026-10-17",
            "title": "How Far Should Shingles Overhang the Drip Edge? | J & N",
            "meta": "How far shingles should overhang the drip edge at eaves and rakes, what the building code requires, and how underlayment goes at each edge. Plain answers.",
            "body": phero(trail, TITLE, "Fractions of an inch that decide whether water drips off your roof or rolls back under it.",
                          hero, "Roof by J & N Roofing Maintenance", "Roof maintenance handbook",
                          extra='<div class="meta-line"><span>By J &amp; N Roofing Maintenance</span><span>Published 17 Oct 2026</span><span>6 min read</span></div>')
                    + f'<section class="sec"><div class="wrap layout"><article class="prose">{art}</article>{side([("Roof inspections &amp; maintenance", "services/roof-inspections-maintenance/"), ("Roofing repairs", "services/roofing-repairs/"), ("Warranty support", "warranty-support/"), ("Roofing glossary", "glossary-of-roofing-terms/"), ("All articles", "blog/")])}</div></section>' + cta(),
            "schema": [crumbs_ld(url, trail),
                       {"@type": "BlogPosting", "@id": url + "#article", "headline": TITLE,
                        "description": "Shingle overhang at the drip edge, IRC drip edge requirements, and underlayment order at eaves and rakes.",
                        "image": U + "assets/img/" + hero + ".webp", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": url, "inLanguage": "en-US",
                        "citation": [ARMA, PACIFIC, ICC]},
                       faq_ld(FAQ)],
            "full_biz": False}
