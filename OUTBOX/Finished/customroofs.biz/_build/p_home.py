import html
from build import U, S, ARROW, PHONE, PATINA, CONTACT, img, faq_html, faq_ld, quotes_html, cta, quote_form, patina_bar

# Main keyword: roofing company salt lake city (+ roofers / roofing contractor salt lake city).
# Truthful framing: the client is located in Lehi and serves Salt Lake City and the Wasatch Front (their own words).

# Reviews copied word for word from the client's home page. "Sega Nintendo" left out (looks like a placeholder name; see notes).
TESTS = [
    ("I had a great experience with Jaime. He was on top of every detail. The work was done in a timely manner. On a very complex roof, he brought in a crew that quickly accomplished the tear-off and then sealed it well while the shingles were installed. Given the complexity, installing shingles took awhile. But the look of the finished roof was worth it.", "Scott Summers"),
    ("Custom roofing llc, so far one of the best roofing companies out there. If not the BEST! The staff was always on time very respectful and profesional. Did meet deadline on time job was done when it was said to be. I really think highly of custom roofing and i surely recommend this company!!!", "Gama Garcia"),
    ("Jaime and his team are fantastic and did a great job on updating the roof on our old shed! Very professional and quick to respond.", "Shane Reeves"),
    ("Jaime did a beautiful job re-roofing and fixing up our shed. He does a high quality work!", "Lacey Reeves"),
]

SNAPS = [("copper-roof-aerial", "Aerial view of a large home with a full copper roof", "Full copper roof, seen from above"),
         ("copper-arched-roof-building", "Arched building covered in copper shingles", "Copper shingles on an arched roof"),
         ("copper-chimney-cap", "Copper chimney cap with standing seams", "Copper chimney cap"),
         ("copper-siding-detail", "Copper roof edge on a modern building with dark siding", "Copper edge on a modern build"),
         ("red-black-metal-siding-barn-sunset", "Barn with red and black metal siding at sunset", "Red and black siding, newest work"),
         ("copper-standing-seam-over-old-roof", "Copper standing-seam panels going on beside existing shingles", "Copper panels during install")]

FAQS = [
    ("Do you only work with copper?",
     "No. Copper is our specialty, but we also handle general roofing, siding, gutters, and roof repair and maintenance for homes and businesses."),
    ("Can I add copper without replacing my whole roof?",
     "Yes. We install copper accents such as valleys, dormers and chimney caps on existing roofs, and copper gutters to go with them."),
    ("Where are you located, and do you work in Salt Lake City?",
     "Custom Roofing is located in Lehi, Utah. We serve customers throughout Utah, with a primary focus on the Wasatch Front, including Salt Lake City."),
    ("How do I get started?",
     "Call 801-889-4220 or send us a message. We&rsquo;ll set up a free consultation, build a project plan, and get your approval before any work starts."),
]


def build():
    snaps = "".join(f'<figure class="snap reveal">{img(n, a)}<figcaption><span>Specimen {i + 1:02d}</span>{c}</figcaption></figure>' for i, (n, a, c) in enumerate(SNAPS))
    stages = "".join(f'<li data-c="{c}"><i style="background:{c}"></i><span>Stage {i + 1}</span><b>{n}</b></li>' for i, (n, c) in enumerate(PATINA))
    CHIPS = [("copper-roofing-utah/", "Copper roofs", "Installation, replacement and full overhauls", "#e59a7a", "#b5652f"),
             ("copper-roofing-utah/#accents", "Copper accents", "Valleys, dormers, chimney caps", "#c8794a", "#8a4a24"),
             ("lehi-custom-siding-home-value/", "Copper siding", "Installation, repair and replacement", "#8a5232", "#4f2c18"),
             ("custom-roofing-maintenance-utah/", "Repair &amp; maintenance", "Inspections, cleaning, seam and panel repair", "#8cc7b7", "#4c8c7d")]
    chips = "".join(f'<a class="chip reveal" style="--a:{a1};--b:{b1};--r:{(i - 1.5) * 4:.0f}deg" href="@/{p}"><span class="face"><span class="hole"></span><span class="no">No. {i + 1:02d}</span></span><span class="txt"><b>{t}</b><small>{s}</small><em>View {ARROW}</em></span></a>' for i, (p, t, s, a1, b1) in enumerate(CHIPS))
    q0, a0 = TESTS[0]
    rest = "".join(f'<figure class="q reveal"><blockquote><p>{html.escape(q)}</p></blockquote><figcaption>{html.escape(a)}</figcaption></figure>' for q, a in TESTS[1:])
    body = f'''
<section class="hero">{img("copper-roof-ladder-trees", "Copper standing-seam roof with a domed cupola and copper dormers, seen from above", priority=True)}
<div class="wrap hero-in">
<div class="hero-text">
<p class="label light">Custom Roofing LLC &middot; Lehi &middot; Salt Lake City &middot; Wasatch Front</p>
<h1>A roofing company for Salt Lake City homes, <em>built around copper.</em></h1>
<p class="lede">Custom Roofing is a roofing company serving Salt Lake City and the Wasatch Front from Lehi. We specialize in copper roofs, copper accents and copper siding, and we handle the repairs, maintenance and general roofing that keep any home protected.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Request a Quote {ARROW}</a><a class="btn ghost" href="tel:{S["tel"]}">{PHONE} {S["phone"]}</a></div>
</div>
<div class="element" aria-hidden="true"><span class="z">29</span><span class="w">63.546</span><b>Cu</b><span class="n">Copper</span><span class="stage">Stage 1 &middot; <span>Salmon pink</span></span></div>
</div>{patina_bar("hero-patina")}</section>

<section class="ring-sec" aria-label="What we do"><div class="wrap">
<div class="ring-head reveal"><p class="label">The sample ring</p><h2>Four things we do, <em>in copper and beyond</em></h2></div>
<div class="ring"><span class="rod" aria-hidden="true"></span>{chips}</div>
</div></section>

<section class="sec"><div class="wrap split">
<div class="reveal"><p class="label">Roofers in Salt Lake City</p><h2>Every roof should fit <em>the house it&rsquo;s on</em></h2>
<p>Every home has its own character, and its roof should reflect that. As roofers serving Salt Lake City and the Wasatch Front, we build copper roofing around your home&rsquo;s architecture and your style, from a single copper dormer to a full roof.</p>
<p>Not every job is copper. We also take on repairs, replacements and new installations, big or small, for homes and businesses. One of our clients put it simply: on a very complex roof, Jaime &ldquo;was on top of every detail.&rdquo;</p>
<a class="tlink" href="@/home/roofing-services-lehi-quality-guaranteed/">See all services and our newest work {ARROW}</a></div>
<figure class="arch reveal">{img("copper-roof-home", "Two-story stucco home with a copper roof and curved copper dormers")}<figcaption>Copper roof and curved dormers</figcaption></figure>
</div></section>

<section class="strip-sec patina-run" aria-label="The patina scale"><div class="strip-sticky"><div class="wrap pr-grid">
<div class="pr-text"><p class="label light">The patina scale</p><h2>New copper doesn&rsquo;t stay penny-bright. <em>That&rsquo;s the point.</em></h2>
<p class="lede">Left to weather, copper moves from salmon pink through russet and chocolate browns to a dull slate gray, and finally to blue-green. That surface layer protects the metal underneath.</p>
<p>In a dry place like Utah, the last stage can take far longer than people expect, or never fully arrive.</p>
<a class="tlink" href="@/blog/why-does-copper-turn-green/">Why does copper turn green? {ARROW}</a></div>
<div class="pr-swatch"><div class="sheet-cu"><span class="sheen"></span><span class="cap">Cu &middot; <span class="cap-n">Salmon pink</span></span></div><ol class="stages">{stages}</ol></div>
</div><p class="wrap src">Color stages as described by Construction Canada (2017). Screen colors are approximate.</p></div></section>

<section class="sec white"><div class="wrap">
<div class="head reveal"><p class="label">Residential &amp; commercial</p><h2>What we build <em>and look after</em></h2><p class="lede">Copper is the specialty. Protection is the job.</p></div>
<div class="props">
<a class="prop f reveal" href="@/copper-roofing-utah/">{img("copper-dome-roof-installer", "Custom Roofing installer standing on top of a copper dome under construction")}<div class="in"><h3>Copper roofing in Utah</h3><p>Installation, replacement and complete copper roof overhauls, starting with a detailed inspection of the roof you have.</p><span class="go">Copper roofing {ARROW}</span></div></a>
<a class="prop w reveal" href="@/lehi-custom-siding-home-value/">{img("copper-siding-install", "Copper siding panels being installed around a window")}<div class="in"><h3>Copper siding</h3><p>Panels installed one by one, with finishes from new copper&rsquo;s shine to a weathered look.</p><span class="go">Siding {ARROW}</span></div></a>
<a class="prop w reveal" href="@/custom-roofing-maintenance-utah/">{img("copper-standing-seam-over-old-roof", "Copper standing-seam roof panels with tools on the roof")}<div class="in"><h3>Repair &amp; maintenance</h3><p>Inspections, debris removal, resealing, and fixing panels and seams before small issues turn into leaks.</p><span class="go">Repair &amp; maintenance {ARROW}</span></div></a>
</div></div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">From our projects</p><h2>Copper, <em>up close</em></h2><p class="lede">Roofs, accents and siding from Custom Roofing jobs in Utah.</p></div>
<div class="snaps">{snaps}</div>
</div></section>

<section class="sec dark"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label light">How it works</p><h2>Three steps from first call <em>to finished roof</em></h2>
<ol class="steps" style="margin-top:24px">
<li><h3>Fill out the form</h3><p>It takes about two minutes. Tell us where the project is and what you have in mind, and our team will be in touch.</p></li>
<li><h3>We build your plan</h3><p>After a free consultation we create the project plan, then get your approval before we start.</p></li>
<li><h3>We do the work</h3><p>You sit back while our crew takes care of the project.</p></li>
</ol></div>
<div class="reveal sticky-form">{quote_form()}</div>
</div></section>

<section class="sec white reviews"><div class="wrap">
<p class="label reveal">Reviews</p>
<figure class="bigq reveal"><blockquote><p>{html.escape(q0)}</p></blockquote><figcaption>{html.escape(a0)}</figcaption></figure>
<div class="qrow">{rest}</div>
</div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before <em>you call</em></h2><p class="lede">Short answers to what people ask us first.</p>
<a class="btn navy" href="@/{CONTACT}">Contact us {ARROW}</a></div>
<div class="reveal">{faq_html(FAQS)}</div>
</div></section>
''' + cta()
    return {"title": "Roofing Company Salt Lake City | Copper Roofing Specialists",
            "meta": "Custom Roofing is a roofing company serving Salt Lake City and the Wasatch Front from Lehi, specializing in copper roofs, siding and repairs. Call 801-889-4220.",
            "body": body, "og": "copper-roof-ladder-trees", "es": True,
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]},
                       faq_ld(FAQS)],
            "full_biz": True}
