from build import U, BIZ_ID, S, ARROW, PATINA, CONTACT, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

PATH = "blog/why-does-copper-turn-green/"
MRM = "https://www.metalroofing.org.nz/node/3860"
CC = "https://constructioncanada.net/architects-turn-green-reliable-long-lasting-roofing/2"
KUER = "https://www.kuer.org/health-science-environment/2024-02-05/what-if-utah-isnt-the-2nd-driest-state-we-all-thought-it-was"

# Main keyword: "why does copper turn green" (informational, long-tail). Supporting: how long does it take copper
# to turn green / copper roof patina / copper patina stages.
# Not targeted (owned by service pages, linked only): roofing company salt lake city (home),
# copper roofing utah, copper roofing lehi, custom roofing maintenance utah, lehi custom siding.
# Hard head terms ("copper roofing", "copper roof cost") left alone: national competition, and no client prices.

FAQ = [
    ("Is the green on a copper roof a sign of damage?",
     "No. The green layer is the end stage of copper&rsquo;s natural weathering. It adheres tightly and protects the metal underneath from further weathering. Dark streaks, stains or pooling water are different and worth having checked."),
    ("How long does a copper roof take to turn green?",
     "It depends on the air. Published figures run from about 5 years in marine air and 7 to 10 years in seacoast or industrial air, to 15 to 25 years in rural areas and over 30 years in mild ones. In some dry climates it may never turn green at all."),
    ("Will my copper roof turn green in Utah?",
     "It may take a very long time, or stop at brown or gray. Utah is one of the driest states, and in arid places the green sulfate patina may never form because there isn&rsquo;t enough moisture to finish the reaction. No source we found gives a Utah-specific number."),
    ("Does the purity of the copper change how fast it turns green?",
     "No. The New Zealand Metal Roofing Manufacturers&rsquo; guidance says the strength and purity of the copper don&rsquo;t affect how fast the patina forms. Local air, moisture, pollutants and the slope of the surface do."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> copper turns green because it reacts with the air. First it forms a brown oxide film. Then, over years, moisture and airborne sulfur compounds turn the surface into a blue-green layer of basic copper sulfate (or copper carbonate in cleaner air). That layer protects the metal. In dry climates like Utah&rsquo;s, the green stage can take decades, or never arrive.</div>

<p>Copper goes on a roof looking like a new penny. A few weeks later it&rsquo;s already darker. It&rsquo;s fair to wonder whether that&rsquo;s normal, and when the famous green will show up.</p>
<p>Both questions have good answers. Here&rsquo;s what&rsquo;s happening to the metal, the order the colors come in, how long each stage takes, and why a roof in Lehi or Salt Lake City doesn&rsquo;t follow the same clock as one in Boston or by the sea.</p>

<h2>What&rsquo;s actually happening to the metal</h2>
<p>Copper reacts with its surroundings. Within weeks of installation it forms a thin, even brown film of copper oxide from contact with oxygen in the air. The New Zealand Metal Roofing Manufacturers note that small handling marks often disappear in those first weeks for exactly this reason.</p>
<p>The green comes later and needs more than oxygen. Construction Canada describes it as the result of airborne sulfur compounds slowly attacking the surface until the color change stabilizes. Moisture carries the reaction along.</p>
<p>What the green is made of depends on the air. In urban and industrial areas it&rsquo;s mainly <strong>basic copper sulfate</strong>. Away from cities it&rsquo;s mainly <strong>basic copper carbonate</strong>, according to the same New Zealand guidance.</p>
<p>People often call the green &ldquo;verdigris.&rdquo; Strictly speaking, verdigris is a different copper compound made with acetic acid. On a roof, the green you see is the sulfate or carbonate patina.</p>

<figure>{img("copper-roof-aerial", "Aerial view of a home with a new copper roof")}<figcaption>New copper starts out salmon pink and darkens within weeks.</figcaption></figure>

<h2>The colors copper goes through, in order</h2>
<p>Copper doesn&rsquo;t jump from shiny to green. Construction Canada lays out the sequence for unprotected copper:</p>
<ol class="scale inline">{"".join(f'<li><i style="background:{c}"></i><b>{n}</b></li>' for n, c in PATINA)}</ol>
<ol>
<li><strong>Salmon pink.</strong> The natural color of new copper.</li>
<li><strong>Russet brown.</strong> The first oxide film forms.</li>
<li><strong>Light and dark chocolate brown.</strong> The film thickens. The brown gets deeper with time.</li>
<li><strong>Dull slate gray or dull black.</strong> The darkest stage, just before any green appears.</li>
<li><strong>Blue-green or gray-green.</strong> The final patina emerges from the dark stage.</li>
</ol>
<p>Expect the color to vary. Construction Canada points out that hues can differ from panel to panel, and even within a single panel. That&rsquo;s normal weathering, not a defect.</p>

<h2>How long does it take copper to turn green?</h2>
<p>There isn&rsquo;t one number. The speed depends on how much moisture and sulfur the air carries. Here are the published figures from two industry sources:</p>
<div class="tablebox"><table><thead><tr><th>Environment</th><th>Time to green patina</th><th>Source</th></tr></thead><tbody>
<tr><td>Marine</td><td>About 5 years</td><td>NZ Metal Roofing Manufacturers</td></tr>
<tr><td>Seacoast or industrial</td><td>Generally 7 to 10 years</td><td>Construction Canada</td></tr>
<tr><td>Industrial</td><td>About 10 years</td><td>NZ Metal Roofing Manufacturers</td></tr>
<tr><td>Rural (little sulfur dioxide)</td><td>15 to 25 years to reach a dominant stage</td><td>Construction Canada</td></tr>
<tr><td>Moderate</td><td>About 18 years</td><td>NZ Metal Roofing Manufacturers</td></tr>
<tr><td>Mild</td><td>Over 30 years</td><td>NZ Metal Roofing Manufacturers</td></tr>
<tr><td>Some dry or arid climates</td><td>May never turn green</td><td>Both</td></tr>
</tbody></table></div>
<p>The pattern is simple. Salt and pollution speed it up. Clean, dry air slows it down.</p>

<h2>Why copper turns green slowly in Utah</h2>
<p>Utah is dry, even by Western standards. A 2024 analysis by BYU civil engineering assistant professor Rob Sowby, using NOAA data, ranked Utah the <strong>third-driest state</strong>, behind Nevada and Arizona, with an average of 34.3 cm (about 13.5 inches) of precipitation a year for 1991 to 2020 (<a href="{KUER}" rel="noopener">KUER</a>).</p>
<p>That matters for copper. Construction Canada notes that in arid environments the basic sulfate patina may never form, because there isn&rsquo;t enough moisture to carry the chemical conversion to completion. The New Zealand guidance says the same of some dry environments.</p>
<p>So what should a Utah owner expect? We haven&rsquo;t found a source with a Utah-specific timeline, and we won&rsquo;t invent one. What the sources do support:</p>
<ul>
<li>The brown stages arrive on schedule, within weeks to months.</li>
<li>The roof may spend a long time in the brown and slate-gray stages.</li>
<li>Full green is likely to be slow, and on some roofs it may never fully develop.</li>
</ul>
<p>If you&rsquo;re choosing copper for a Wasatch Front home, choose it because you like the brown and bronze tones too. Those are the colors you&rsquo;ll live with for years.</p>

<figure>{img("copper-chimney-cap", "Copper chimney cap with standing seams on a job site")}<figcaption>Vertical surfaces and roof slopes weather at different speeds.</figcaption></figure>

<h2>What else changes how your copper weathers</h2>
<p>Climate sets the pace, but the roof itself plays a part. The New Zealand guidance lists a few factors:</p>
<ul>
<li><strong>Slope.</strong> The pitch of a roof affects how the patina develops. Vertical surfaces like walls, and sheltered soffits, weather differently from open roof planes.</li>
<li><strong>Handling.</strong> Perspiration from bare hands during installation can mark the surface and affect patination.</li>
<li><strong>Streaks and soiling.</strong> Dirty or streaked areas can weather unevenly.</li>
</ul>
<p>One thing that doesn&rsquo;t matter: the copper itself. Strength and purity don&rsquo;t change the rate of patina formation.</p>
<p>That&rsquo;s why the same house can show three shades at once. A <a href="@/lehi-custom-siding-home-value/">copper-sided wall</a> under an eave, a steep dormer and a low-slope roof section will each move at their own speed.</p>

<h2>Is the green layer good or bad for the roof?</h2>
<p>Good. Construction Canada describes the natural patina as covering the surface, adhering tightly and protecting against weathering. It&rsquo;s a big part of why a properly designed and installed copper roof is a long-term, low-maintenance roof.</p>
<p>What&rsquo;s worth watching is anything that isn&rsquo;t even weathering: dark streaks from runoff, debris holding moisture in one spot, loose panels, or cracked seams. Our <a href="@/custom-roofing-maintenance-utah/">copper roof maintenance</a> visits check the seams, flashing and how the patina is developing.</p>

<h2>Can you control how copper ages?</h2>
<p>To a degree. If you want to steer the process, or bring unevenly weathered areas back into line, Custom Roofing offers specialized cleaning and treatments as part of our patina management service. The goal is a roof that ages evenly while keeping its protective layer.</p>
<p>Regular cleaning also helps. Debris and runoff stains are the usual reason a patina comes in blotchy rather than even.</p>

<h2>Questions owners ask about copper patina</h2>
{faq_html(FAQ)}

<h2>Thinking about copper for your home?</h2>
<p>We specialize in <a href="@/copper-roofing-utah/">copper roofing in Utah</a>, from full roofs to dormers, valleys and chimney caps. Call <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/{CONTACT}">request a quote</a> and we&rsquo;ll talk through how copper will look on your house, now and years from now.</p>

<div class="sources"><h3>Sources</h3><ol>
<li><a href="{MRM}" rel="noopener">Metal Roofing Manufacturers Inc. (New Zealand), guidance on copper patina development</a></li>
<li><a href="{CC}" rel="noopener">Construction Canada, &ldquo;Architects turn green for reliable and long-lasting roofing,&rdquo; 10 Nov 2017, page 2</a></li>
<li><a href="{KUER}" rel="noopener">David Condos, KUER 90.1, &ldquo;What if Utah isn&rsquo;t the 2nd-driest state we all thought it was?&rdquo; 5 Feb 2024</a></li>
</ol></div>
'''


def pages():
    url = U + PATH
    trail = [("Home", ""), ("Copper Guide", "blog/"), ("Why Does Copper Turn Green?", PATH)]
    post = {"path": PATH, "canonical": url, "ogtype": "article", "og": "copper-roof-aerial", "modified": "2026-10-17",
            "title": "Why Does Copper Turn Green? (And Why It's Slow in Utah)",
            "meta": "Why copper turns green, the five color stages it passes through, how long a copper roof takes to patina, and why Utah's dry air slows the change down.",
            "body": phero(trail, "Why Does Copper Turn Green?", "The chemistry, the color stages, the timelines, and why a Utah copper roof may stay brown for a long time.",
                          "copper-roof-ladder-trees", "Copper roof with a domed cupola, seen from above", "Copper guide",
                          extra='<div class="meta-line"><span>By Custom Roofing</span><span>Updated 17 Oct 2026</span><span>8 min read</span></div>')
                    + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side([("Copper roofing in Utah", "copper-roofing-utah/"), ("Copper roof maintenance", "custom-roofing-maintenance-utah/"), ("Copper siding", "lehi-custom-siding-home-value/"), ("Request a quote", CONTACT)])}</div></section>' + cta(),
            "schema": [crumbs_ld(url, trail),
                       {"@type": "BlogPosting", "@id": url + "#article", "headline": "Why Does Copper Turn Green? (And Why It's Slow in Utah)",
                        "description": "Why copper turns green, the color stages, patina timelines by climate, and why Utah's dry air slows the process.",
                        "image": U + "assets/img/copper-roof-aerial.webp", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": url, "inLanguage": "en-US",
                        "about": [{"@type": "Thing", "name": "Patina"}, {"@type": "Thing", "name": "Copper roofing"}],
                        "citation": [MRM, CC, KUER]},
                       faq_ld(FAQ)],
            "full_biz": False}
    iurl = U + "blog/"
    itrail = [("Home", ""), ("Copper Guide", "blog/")]
    card = f'<a class="postcard reveal" href="@/{PATH}">{img("copper-roof-aerial", "Aerial view of a copper roof")}<div class="in"><small>Copper patina</small><b>Why does copper turn green? (And why it&rsquo;s slow in Utah)</b><p style="margin:10px 0 0;color:var(--muted)">The chemistry, the five color stages, published timelines, and what Utah&rsquo;s dry air means for your roof.</p></div></a>'
    index = {"path": "blog/", "canonical": iurl, "og": "copper-roof-aerial",
             "title": "Copper Roofing Guide: Patina, Care & More | Custom Roofing",
             "meta": "Plain answers about copper roofs from Custom Roofing in Lehi, Utah: how copper weathers, how long patina takes, and how to care for a copper roof for decades.",
             "body": phero(itrail, "Copper Roofing Guide", "Plain answers about how copper roofs look, weather and last.", "copper-roofing-panels", "Stack of new copper roofing panels", "Blog")
                     + f'<section class="sec"><div class="wrap"><div class="grid">{card}</div></div></section>' + cta(),
             "schema": [crumbs_ld(iurl, itrail), {"@type": "CollectionPage", "@id": iurl + "#page", "url": iurl, "name": "Copper Roofing Guide",
                                                  "hasPart": [{"@id": url + "#article"}]}],
             "full_biz": False}
    return [index, post]
