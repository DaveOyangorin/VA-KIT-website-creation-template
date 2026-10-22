import html
from build import U, S, ARROW, PHONE, IMG, img, faq_html, faq_ld, cta, quote_form

IC = {
    "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3l8 3v6c0 4.4-3.4 8-8 9-4.6-1-8-4.6-8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "steps": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M4 18h4v-4h4v-4h4V6h4"/></svg>',
}

# The client's own FAQ answers from their current home page.
FAQ = [
    ("What areas do you serve?",
     "We operate exclusively across Northern Utah, serving the following counties: Utah, Salt Lake, Tooele, Wasatch, Summit, Morgan, Davis, Weber, Box Elder, Cache, and Rich. We also work in major cities, including South Jordan, Salt Lake City, Ogden, Orem, and Tooele. Not sure if we cover your area? Get in touch and we'll let you know."),
    ("What services do you offer?",
     "We provide replacement, repair, storm damage restoration, maintenance, health reports, and gutter replacement for residential and commercial properties throughout Northern Utah. If your situation doesn't fit a clear category, a free Roof Health Report is the right starting point."),
    ("What warranties do you offer?",
     "As a GAF Master Elite contractor, we can offer enhanced manufacturer warranties. These include long-term material protection when systems are installed to GAF specifications, along with a workmanship warranty on our installation. The exact coverage depends on the product and package you select."),
    ("How much does it cost to replace a roof?",
     "Roof replacement cost is shaped by your home's square footage, roof pitch, existing layer count, and the material system you choose. For most single-family homes, full replacements fall in the low to mid tens of thousands of dollars. Every project receives a detailed estimate upfront, including three priced options and payment options."),
    ("Do you offer free roof inspections in Utah?",
     "Yes. We provide a free Roof Health Report to homeowners throughout our Northern Utah service area. A certified inspector will examine your roof, provide a clear summary of findings, and outline your current options for repair or replacement."),
    ("Do you assist with insurance claims?",
     "Yes. For storm-damaged roofs, we offer an optional insurance concierge service. Our team inspects the roof, documents all findings with photos, prepares a complete file, and coordinates with your adjuster on the roofing portion if needed. All coverage and payment decisions rest with your insurer. Our role is to make sure your file is thorough and accurate."),
    ("Do you offer financing?",
     "Yes. Both roof repair and full replacement projects are eligible for financing, so you can spread payments over time or defer them instead of paying everything upfront. We walk you through available options after your Roof Health Report, and our team will help you identify what fits your situation."),
    ("How quickly can you replace my roof?",
     "Most residential roof replacements are finished in a single day, including cleanup. We back every project with an On-Time Start Guarantee: once you approve your proposal, we begin within 14 calendar days (weather permitting), or we credit 20% of your project cost back to you."),
]


def prop(cls, title, text, href, image, alt):
    return f'''<a class="prop {cls} reveal" href="@/{href}">{img(image, alt)}<div class="in"><h3>{title}</h3><p>{text}</p><span class="go">Learn more {ARROW}</span></div></a>'''


def mat(href, title, text, image, alt):
    return f'<a class="linkcard reveal" href="@/{href}" style="padding:0;overflow:hidden">{img(image, alt)}<div style="padding:20px 22px 22px;display:grid;gap:6px"><b>{title}</b><span>{text}</span></div></a>'


def build(r):
    body = f'''
<section class="hero">{img("aerial-new-roof-neighborhood", "Aerial view of a new dark shingle roof on a home in a Northern Utah neighborhood", priority=True)}
<div class="wrap">
<p class="label light">South Jordan, UT &middot; GAF Master Elite&reg; contractor</p>
<h1>South Jordan&rsquo;s roofing company. <span>New roof in a day.</span></h1>
<p class="lede">Aesthetic Roofing is a GAF Master Elite&reg; roofing company in South Jordan, Utah, replacing and repairing roofs for homeowners across Northern Utah. Honest recommendations, premium materials, and most replacements finished in a single day.</p>
<div class="btn-row"><a class="btn" href="@/contact/">Book a Free Roof Health Report {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
<div class="rating"><span class="stars" aria-hidden="true">★★★★★</span><span><strong>4.8</strong> Google rating &middot; 350+ reviews</span></div>
<div class="badges">{img("gaf-master-elite", "GAF Master Elite residential roofing contractor", lazy=False)}{img("bbb-logo", "Better Business Bureau", lazy=False)}</div>
<div class="ticket" role="note"><small>On-Time Start Guarantee</small><b>Start in 14 days or 20% back.</b>
<p>Once you approve your proposal, we begin within 14 calendar days (weather permitting), or we credit 20% of your project cost back to you.</p></div>
</div></section>

<section class="statband" aria-label="Aesthetic Roofing by the numbers"><div class="wrap">
<div class="stat"><b>1<sup>day</sup></b><span>Most residential replacements, including cleanup</span></div>
<div class="stat"><b>14<sup>days</sup></b><span>From approved proposal to start, or 20% back</span></div>
<div class="stat"><b>3<sup>options</sup></b><span>Priced options on every estimate</span></div>
<div class="stat"><b>495<sup>+</sup></b><span>Roofs installed last year</span></div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Roofers in South Jordan</p><h2>A Northern Utah roofing company you can trust</h2>
<p>Your roof protects everything underneath it, which is why choosing the right roofing company matters. We help homeowners in South Jordan and across Northern Utah make confident decisions with honest recommendations, premium materials, and quality workmanship.</p>
<p>As a GAF Master Elite&reg; roofing contractor, we meet some of the industry&rsquo;s highest standards for training, installation quality and customer service. Whether you need a minor repair or a complete roof replacement, our team focuses on doing the job right while keeping the whole process straightforward.</p>
<p>If your roof can be repaired, we&rsquo;ll tell you. If replacement makes more sense, we&rsquo;ll explain why.</p>
<a class="tlink" href="@/about/">Meet the team {ARROW}</a></div>
<div class="stack reveal">{img("aerial-home-mountains", "Drone view of a two-story Utah home with a new roof and the Wasatch Mountains behind")}{img("aesthetic-team", "The Aesthetic Roofing team in branded shirts", cls="b")}<span class="cap">Drone shot, Northern Utah</span></div>
</div></section>

<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Roofing services</p><h2>Roofing services for every home</h2><p class="lede">Every home has different roofing needs. Pick the one you&rsquo;ve got.</p></div>
<div class="props">
{prop("f", "Roof Replacement", "When repairs are no longer cost-effective, a full replacement gives you a durable, attractive roof, usually finished in a single day.", "services/roof-replacement/", "aerial-new-roof-yard", "Aerial view of a freshly replaced shingle roof on a Utah home")}
{prop("", "Roof Repair", "Leaks, missing shingles, damaged flashing and other problems, fixed before they turn into bigger ones.", "services/roof-repair/", "aerial-new-shingle-roof", "Close aerial view of a shingle roof")}
{prop("", "Storm Damage", "Wind and hail damage repaired fast, with an optional insurance concierge to document your claim.", "services/storm-damage-roof-repair/", "aerial-gray-roof-solar", "Aerial view of a gray shingle roof with solar panels")}
{prop("w", "Roof Inspection &amp; Roof Health Report", "A certified inspector examines your roof and gives you a clear summary of findings and your options. Free across our service area.", "services/roof-inspection/", "top-down-new-roof", "Top-down drone photo of a complete new roof")}
</div>
<p class="reveal" style="margin-top:18px"><a class="tlink" href="@/services/gutter-replacement/">Gutter replacement {ARROW}</a> &nbsp; <a class="tlink" href="@/services/">All services {ARROW}</a></p>
</div></section>

<section class="band">{img("top-down-new-roof", "Top-down drone photo of a new roof showing ridge lines and vents")}
<div class="wrap"><div class="copy reveal"><p class="label light">Engineered roofing systems</p><h2>A roof is more than the shingles you can see.</h2>
<p class="lede">We install full roofing systems: shingles, underlayment, ice and water protection, flashing and ventilation, working together. Our crews follow GAF manufacturer specifications on every job.</p>
<a class="btn" href="@/roof-types/">Compare roof types {ARROW}</a></div></div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label light">Structured execution</p><h2>What to expect when you work with us</h2>
<p class="lede">A clear, step-by-step process, and a named person responsible at every stage.</p>
<ol class="steps" style="margin-top:28px">
<li><h3>Free Roof Health Report</h3><p>A certified inspector examines your roof and walks you through what they found.</p></li>
<li><h3>A proposal with three priced options</h3><p>Fixed price and schedule, plus financing choices if you want them.</p></li>
<li><h3>Installation, usually in one day</h3><p>Your install coordinator manages materials and crews; your project manager is on site.</p></li>
<li><h3>Final inspection and walkthrough</h3><p>We check the work against GAF specifications and leave the site clean.</p></li>
</ol></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Roof types</p><h2>Roofing materials we install</h2><p class="lede">Choosing the right material is just as important as choosing the right roofer. We&rsquo;ll help you compare durability, looks, upkeep and budget.</p></div>
<div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,240px),1fr))">
{mat("roof-types/asphalt-shingle/", "Asphalt Shingle", "The most popular choice in Northern Utah: performance, value and curb appeal.", "material-asphalt-shingles", "Asphalt shingle roof")}
{mat("roof-types/metal-roofing/", "Standing Seam Metal", "A clean, modern look with decades of protection and little upkeep.", "material-metal", "Standing seam metal roof")}
{mat("roof-types/flat-roofing/", "Flat Roofing", "Low-slope systems installed with the specialized techniques they need.", "material-flat", "Flat roof system")}
{mat("roof-types/designer-asphalt-roofing/", "Designer Asphalt", "Architectural shingles that add dimension and character.", "aerial-new-roof-yard", "Designer asphalt shingle roof seen from above")}
</div></div></section>

<section class="sec white"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Reviews</p><h2>What homeowners say</h2>
<div class="reviews-live"><span class="stars" aria-hidden="true">★★★★★</span><b>4.8</b><span>Google rating from 350+ reviews</span>@@REVIEWS_WIDGET@@</div></div>
<div class="reveal"><p class="label">Our work</p><h2>Recent projects</h2>
<div class="projects mini">
<figure>{img("aerial-roofs-street", "Aerial view of new roofs along a Utah street")}<figcaption>Northern Utah</figcaption></figure>
<figure>{img("aerial-new-shingle-roof", "Aerial view of a new shingle roof")}<figcaption>Shingle replacement</figcaption></figure>
<figure>{img("crew-on-roof-utah-county", "Roofing crew working on a home with snowy mountains behind")}<figcaption>Utah County</figcaption></figure>
<figure>{img("aerial-gray-roof-solar", "Gray shingle roof with solar panels from above")}<figcaption>Roof with solar</figcaption></figure>
</div><p style="margin-top:14px"><a class="tlink" href="@/projects/">View the project gallery {ARROW}</a></p></div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Service area</p><h2>Roofing across Northern Utah</h2>
<p>Based in South Jordan, we work in 11 Northern Utah counties and in major cities including South Jordan, Salt Lake City, Ogden, Orem and Tooele.</p>
<div class="chips" style="margin:20px 0"><a href="@/service-areas/salt-lake-county-ut/">Salt Lake County</a><a href="@/service-areas/utah-county-ut/">Utah County</a><span>Tooele</span><span>Wasatch</span><span>Summit</span><span>Morgan</span><span>Davis</span><span>Weber</span><span>Box Elder</span><span>Cache</span><span>Rich</span></div>
<a class="tlink" href="@/service-areas/">See service areas {ARROW}</a></div>
<div class="reveal"><div style="background:var(--paper);border-radius:var(--r);padding:24px;border:1px solid var(--line)">{img("service-area-map", "Map of the Northern Utah counties served by Aesthetic Roofing")}</div></div>
</div></section>

<section class="sec white"><div class="wrap" style="max-width:960px">
<div class="head reveal"><p class="label">FAQ</p><h2>Clear answers about our process</h2></div>
{faq_html(FAQ)}
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">From the blog</p><h2>What causes roof leaks?</h2>
<p class="lede">The usual suspects on Utah homes, how to spot them from inside, and when a handyman patch is enough.</p>
<a class="btn navy" href="@/blog/what-causes-roof-leaks/">Read the guide {ARROW}</a></div>
<div class="reveal">{img("crew-on-roof-utah-county", "Roofer working on a home roof in Utah County")}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company in South Jordan, UT | Aesthetic Roofing",
            "meta": "Aesthetic Roofing is a GAF Master Elite roofing company in South Jordan, UT. New roofs in a day, honest repairs and a free Roof Health Report. Call today.",
            "body": body, "og": "aerial-new-roof-neighborhood",
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(FAQ)]}
