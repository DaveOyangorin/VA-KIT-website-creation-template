from build import U, BIZ_ID, S, ARROW, INSPECT, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

# Same URL pattern as the client's other posts (/<slug>/ at the site root).
PATH = "how-to-do-valleys-on-a-metal-roof/"
ATAS = "https://www.buildsite.com/pdf/atas/ATAS-Metal-Roofing-Field-Lok-Installation-Guide-Installation-Instructions-1283402.pdf"
HPM = "https://www.hpmhawaii.com/files/pages/manufacturing/CMR/resources/Exposed-Fasten-Panels-Install-Guide-March-2023.pdf"

# Main keyword: "how do you do valleys with metal roofing" (a real Google question from the 14 Oct report) / "metal roof valley".
# Not targeted (owned by other pages, linked only): roofing company west valley city (home), metal roofing west valley city and
# metal roofing contractors west valley city (metal-roofing-contractors-west-valley-city-ut/), roof repair west valley city,
# and the client's post on metal roof cost (average-cost-to-install-metal-roof/).

FAQ = [
    ("Do metal roof valleys leak?",
     "A valley carries water from two roof planes, so it&rsquo;s one of the places a roof is most likely to leak if it&rsquo;s done poorly. Manufacturers&rsquo; details call for underlayment under the valley, a valley pan or flashing, sealed closures and the right laps. One guide warns that valleys must drain and be kept free of debris so water doesn&rsquo;t back up under the panels."),
    ("What is a valley pan on a metal roof?",
     "It&rsquo;s the metal flashing that sits in the bottom of the valley and carries the water. On the standing seam system we looked at, the pan is laid in the valley center and the panels lock to a cleat set 4 to 6 inches from that center line, so their edges never sit in the water stream."),
    ("How much should valley trim overlap?",
     "On the exposed-fastener system we looked at, the manufacturer requires a 9-inch lap for valley trim, compared with 3 inches for its other trims, set with two beads of butyl sealant. Always follow the lap your panel&rsquo;s manufacturer specifies."),
    ("Can exposed-fastener metal panels go on a low-slope roof?",
     "One manufacturer&rsquo;s guide says its exposed-fastened panels should be installed at a minimum slope of 3:12, and to ask before going lower. Low-slope roofs usually call for a different panel, so check the product&rsquo;s own minimum."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> a metal roof valley is built in layers. First, a self-adhered underlayment runs up both sides of the valley. Then a metal valley pan or valley flashing goes in the center. The roof panels are cut to the valley angle and either lock onto a cleat (standing seam) or seal to the flashing with closures and sealant (exposed fastener). The goal is to keep panel edges and fasteners out of the main water path.</div>

<p>Valleys are where two roof slopes meet, and they carry more water than any other part of a roof. That makes them one of the details that separates a metal roof that lasts from one that leaks.</p>
<p>Here&rsquo;s how valleys are built on the two main types of metal roofs, using the manufacturers&rsquo; own installation details, and what to ask your installer.</p>

<h2>Why valleys are the hard part of a metal roof</h2>
<p>A roof plane sheds water straight down. A valley collects water from two planes and channels it down one line. In Utah, that includes snowmelt as well as rain.</p>
<p>Metal panels can&rsquo;t simply be bent into a valley. They have to be cut at an angle, which creates cut edges and panel ends right where the water runs. The valley detail exists to protect those edges.</p>
<p>One manufacturer puts the basic rules plainly: valley dimensions must be the proper width for the slope and rain conditions, valleys must have positive slope for drainage, and they must be kept free of debris so water doesn&rsquo;t back up and get under the panels (<a href="{HPM}" rel="noopener">HPM Exposed Fasten Design &amp; Detail Guide</a>).</p>

<h2>Standing seam valleys: the cleat method</h2>
<p>Standing seam panels have raised, interlocking seams and hidden fasteners. The ATAS Field-Lok installation guide lays out its valley detail in five steps (<a href="{ATAS}" rel="noopener">ATAS installation guide</a>):</p>
<ol>
<li><strong>Underlayment first.</strong> Install a self-adhered underlayment (ATA-Shield) about 18 inches up both sides of the valley line.</li>
<li><strong>Shim.</strong> Place a 3/8-inch shim as shown in the detail.</li>
<li><strong>Valley pan.</strong> Lay the valley pan in the valley center, and locate a &ldquo;joggle&rdquo; cleat 4 to 6 inches from the valley center.</li>
<li><strong>Fasten the cleat.</strong> Fasten it 6 inches on center through butyl tape and the pan, into the shim and the roof deck.</li>
<li><strong>Lock the panels.</strong> Turn the edge of each panel under so it slides into the cleat, and fasten it with clips at 2 feet on center.</li>
</ol>
<p>Notice what that achieves. The panel edges hook onto a cleat that sits away from the center of the valley, and the only fasteners near the water go through butyl tape. The middle of the valley is a clean metal channel.</p>

<h2>Exposed-fastener valleys: flashing, closures and sealant</h2>
<p>Exposed-fastener panels (often called ribbed or corrugated panels) are screwed through the face of the panel. Their valleys work differently. HPM&rsquo;s March 2023 guide shows the parts of its valley detail:</p>
<ul>
<li>Underlayment over the roof deck</li>
<li>Valley flashing in the center of the valley</li>
<li>Inside closures, set in sealant top and bottom, that fill the gaps under the panel ribs</li>
<li>Fasteners through the panel, placed as the guide specifies for each panel type</li>
</ul>
<p>The laps matter too. The same guide says all its trims need a 3-inch lap, except valley trim, which needs a <strong>9-inch lap</strong>, set with two 3/8-inch beads of butyl sealant (<a href="{HPM}" rel="noopener">HPM guide, trim lap detail</a>). That triple-length overlap tells you how much water a valley handles compared with other trims.</p>
<p>Slope matters as well. HPM says its exposed-fastened panels should go on a minimum slope of 3:12, and to ask before going lower.</p>

<h2>Open vs. closed metal valleys</h2>
<p>You&rsquo;ll hear roofers talk about open and closed valleys. In an open valley, the metal valley flashing stays visible down the center, and the panels stop short of it. In a closed valley, roofing covers the valley.</p>
<p>Both details above are open-style: the valley pan or flashing is exposed in the middle, and panel edges are held back from the water channel. Both keep cut panel edges out of the heaviest flow.</p>

<h2>What to ask your installer about valleys</h2>
<p>You don&rsquo;t need to install a valley yourself to judge whether it&rsquo;s being done right. A few questions go a long way:</p>
<ul>
<li><strong>Whose installation details are you following?</strong> The panel manufacturer&rsquo;s guide should be the rulebook.</li>
<li><strong>What goes under the valley?</strong> Ask about self-adhered underlayment up both sides.</li>
<li><strong>How are the panel edges secured?</strong> Cleats for standing seam; closures and sealant for exposed fastener.</li>
<li><strong>What lap does the valley trim get?</strong> Compare the answer with the manufacturer&rsquo;s number.</li>
<li><strong>Will you photograph the valley before it&rsquo;s covered?</strong> Photos of the underlayment and flashing prove what you can&rsquo;t see later.</li>
</ul>
<p>That last one matters to us. Customers have mentioned the photos we take before, during and after a job. One wrote that the before, during and after photos we shared on a Google link made it easy to share with their insurance company.</p>

<h2>Metal roof valleys and Utah snow</h2>
<p>In the Salt Lake Valley, valleys handle snowmelt as well as rain. That&rsquo;s one more reason to ask about the underlayment under each valley and how it drains, and to keep valleys clear of debris, as the manufacturer guidance above recommends.</p>

<h2>Questions about metal roof valleys</h2>
{faq_html(FAQ)}

<h2>Thinking about a metal roof?</h2>
<p>Go Pro Roofing installs and repairs metal roofs across the Salt Lake Valley. See our <a href="@/metal-roofing-contractors-west-valley-city-ut/">metal roofing services</a>, read what a <a href="@/average-cost-to-install-metal-roof/">metal roof costs to install</a>, or call José at <a href="tel:{S["tel"]}">{S["phone"]}</a> for a free estimate.</p>

<div class="sources"><h3>Sources</h3><ol>
<li><a href="{ATAS}" rel="noopener">ATAS International, Field-Lok standing seam installation guide: Valley Detail</a></li>
<li><a href="{HPM}" rel="noopener">HPM (Hawaii), Exposed Fasten Design &amp; Detail Guide, March 2023</a>: general notes (valleys, minimum slope), Valley detail, Trim Lap detail</li>
</ol></div>
'''


def new_post(hero):
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("Metal Roof Valleys", PATH)]
    return {"path": PATH, "canonical": url, "ogtype": "article", "og": hero, "modified": "2026-10-17",
            "title": "How Are Valleys Done on a Metal Roof? | Go Pro Roofing",
            "meta": "How valleys are done on a metal roof: standing seam cleats, exposed-fastener flashing and laps, straight from the manufacturers' own installation details.",
            "body": phero(trail, "How Are Valleys Done on a Metal Roof?", "Standing seam and exposed-fastener valleys, straight from the manufacturers&rsquo; installation details.",
                          hero, "Metal roofing project by Go Pro Roofing", "Go Pro Roofing blog",
                          extra='<div class="meta-line"><span>By Go Pro Roofing</span><span>Published 17 Oct 2026</span><span>7 min read</span></div>')
                    + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side([("Metal roofing", "metal-roofing-contractors-west-valley-city-ut/"), ("Metal roof cost", "average-cost-to-install-metal-roof/"), ("Roof repair", "roof-repair-west-valley-city/"), ("All articles", "blog/")])}</div></section>' + cta(),
            "schema": [crumbs_ld(url, trail),
                       {"@type": "BlogPosting", "@id": url + "#article", "headline": "How Are Valleys Done on a Metal Roof?",
                        "description": "Standing seam and exposed-fastener metal roof valley details, from manufacturers' installation guides.",
                        "image": U + "assets/img/" + hero + ".webp", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": url, "inLanguage": "en-US",
                        "citation": [ATAS, HPM]},
                       faq_ld(FAQ)],
            "full_biz": False}
