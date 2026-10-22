from build import U, S, ARROW, CONTACT, BLOG, img, faq_html, faq_ld, crumbs_ld, cta, phero

# New post. The site has no blog, so it sits at the root with the same .php naming as the other pages.
# Main keyword: "chimney cap vs chimney shroud" (+ chimney shroud vs cap, what is a chimney shroud, chimney shroud code).
# Ties to the client's ChimneyCap-Shroud.php gallery. Not targeted (owned by other pages, linked only):
# roofing company salt lake city (home), metal roofing salt lake city, chimney services (chimney.php).
TITLE, PATH = BLOG
UP = "https://up.codes/viewer/utah/irc-2021/chapter/10/chimneys-and-fireplaces"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"
INSP = "https://inspectapedia.com/chimneys/Chimney_Shrouds.php"
IMC = "https://rumford.com/code/IMC.html"

FAQ = [
    ("Is a chimney shroud the same as a chimney cap?",
     "No. A cap covers the flue opening to keep out rain, snow, debris and animals. A shroud is a larger decorative cover that wraps the top of the chimney. Some shrouds include a cap; many caps are just a small hood and screen."),
    ("Can I put a decorative shroud on a metal (factory-built) chimney?",
     f"Only a listed one. Utah&rsquo;s residential code (R1005.2) says decorative shrouds can&rsquo;t be installed at the top of factory-built chimneys unless they&rsquo;re listed and labeled for that specific chimney system and installed per the manufacturer&rsquo;s instructions (<a href=\"{UP}\" rel=\"noopener\">2021 Utah Residential Code</a>)."),
    ("Does a masonry chimney need a cap?",
     "Yes, in the code&rsquo;s sense: masonry chimneys need a concrete, metal or stone cap, sloped to shed water, with a drip edge and a caulked bond break around the flue liners (R1003.9.1). A screened flue cover on top is a separate item."),
    ("What size mesh should a chimney spark arrestor have?",
     "Where one is installed on a masonry chimney, the code says openings must stop spheres larger than 1/2 inch but let through spheres smaller than 3/8 inch. The screen must have at least four times the net free area of the flue outlet and be removable for cleaning (R1003.9.2)."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> a <strong>chimney cap</strong> covers the flue opening to keep out rain, snow, debris and animals. A <strong>chimney shroud</strong> is a larger decorative cover that wraps the top of the chimney and becomes part of the look of the house. On a <strong>factory-built (metal) chimney</strong>, Utah&rsquo;s residential code only allows a decorative shroud that&rsquo;s listed and labeled for that specific chimney system.</div>

<p>We build and install both at Jemza Roofing, and you can see dozens of them on our <a href="@/ChimneyCap-Shroud.php">chimney caps and shrouds</a> page: black metal boxes over stone, louvered shrouds, copper bells. People often use the two words for the same thing. They aren&rsquo;t, and on some chimneys the difference is a code issue, not just a style choice.</p>
<p>Here&rsquo;s what each one does, what Utah&rsquo;s code says about them, and how to tell which your chimney needs.</p>

<h2>What a chimney cap does</h2>
<p>A chimney cap is the cover over the top of the flue. Most have a small roof or hood that keeps rain and snow out, and mesh sides that keep out leaves, birds and animals while smoke and gases still get out.</p>
<p>That mesh can also act as a spark arrestor, catching embers before they land on the roof. Where a spark arrestor is installed on a masonry chimney, Utah&rsquo;s residential code sets four rules for it (R1003.9.2, <a href="{UP}" rel="noopener">2021 Utah Residential Code</a>):</p>
<ul>
<li>Its net free area must be at least four times the net free area of the flue outlet, so it doesn&rsquo;t choke the draft.</li>
<li>The screen must resist heat and corrosion at least as well as 19-gauge galvanized steel or 24-gauge stainless steel.</li>
<li>Openings must stop spheres larger than 1/2 inch but let through spheres smaller than 3/8 inch.</li>
<li>It must be reachable for cleaning, and the screen or cap must be removable so the flue can be cleaned.</li>
</ul>

<h3>The other kind of &ldquo;cap&rdquo;</h3>
<p>There&rsquo;s a second meaning, and it causes confusion. In the code, a masonry chimney&rsquo;s &ldquo;cap&rdquo; is the solid top of the chimney itself, what many people call the crown. R1003.9.1 says masonry chimneys must have a concrete, metal or stone cap, a drip edge and a caulked bond break around the flue liners, and the cap must be sloped to shed water.</p>
<p>So a masonry chimney usually has both: a sloped crown that sheds water off the brick or stone, and a screened flue cover on top of the flue itself.</p>

<h2>What a chimney shroud is</h2>
<p>A shroud is a bigger, decorative piece that wraps the top of the chimney. Shrouds are often made of sheet metal or copper, and they come in many forms: a long black box spanning several flues, a louvered band, a framed lantern shape, or a copper bell. On a modern or mountain-style house, the shroud is often what you notice first about the roofline.</p>
<p>A shroud can hide the flue terminations and the cap beneath it. That&rsquo;s exactly where the code steps in.</p>

<figure>{img("chimney-shroud-14", "Louvered black chimney shroud on a stone chimney above a standing-seam roof")}<figcaption>A louvered shroud on one of our jobs, over a stone chimney and a standing-seam roof.</figcaption></figure>

<h2>The rule for shrouds on factory-built chimneys</h2>
<p>Utah adopted the 2021 International Residential Code for homes, effective July 1, 2023 (<a href="{ICC}" rel="noopener">International Code Council</a>). Its section on factory-built chimneys says, in R1005.2 (<a href="{UP}" rel="noopener">2021 Utah Residential Code</a>):</p>
<blockquote><p>&ldquo;Decorative shrouds shall not be installed at the termination of factory-built chimneys except where the shrouds are listed and labeled for use with the specific factory-built chimney system and installed in accordance with the manufacturer&rsquo;s installation instructions.&rdquo;</p></blockquote>
<p>The International Mechanical Code has the same rule, in section 805.6 (<a href="{IMC}" rel="noopener">IMC text reproduced by Buckley Rumford</a>).</p>
<p>In plain terms: on a metal chimney system, the shroud has to be one the chimney&rsquo;s listing allows. A custom sheet-metal shroud that isn&rsquo;t listed for that system doesn&rsquo;t meet the code there, however good it looks.</p>

<h3>Why the rule exists</h3>
<p>It comes from fires. A 1991 report by Baird looked at a series of chimney and house fires in California beginning in 1989, and every one of the fires investigated happened in a chimney chase fitted with a decorative sheet-metal shroud. The shrouds had been installed over the manufacturer&rsquo;s spark arrestor and cap. The report concluded that future installations must not include unlisted attachments to a listed fireplace or chimney assembly (<a href="{INSP}" rel="noopener">InspectApedia: Chimney Shrouds</a>).</p>
<p>The reasoning given for the model-code changes, quoted on the same page, is direct: decorative shrouds &ldquo;often allow for the creation of temperatures in excess of those permitted&rdquo; by the UL standards for factory-built chimneys and fireplaces, and they &ldquo;have been the cause of roof and chase fires.&rdquo; A shroud can trap heat at the top of a chimney that was designed and tested to vent into open air.</p>

<h2>Masonry or factory-built? How to tell</h2>
<p>The shroud rule above applies to factory-built chimneys, so the first question is which kind you have. A few clues:</p>
<ul>
<li><strong>Factory-built</strong> chimneys use a metal flue pipe, usually inside a framed box (a chase) finished with siding, stucco or stone veneer. From the roof you&rsquo;ll often see a round metal pipe and a listed metal cap coming out of a flat chase top.</li>
<li><strong>Masonry</strong> chimneys are solid brick, block or stone, usually with clay tile flue liners and a concrete or stone crown.</li>
</ul>
<p>The outside can fool you. A chimney finished in stone may be a framed chase with stone veneer and a metal flue inside. If you aren&rsquo;t sure, the fireplace or stove&rsquo;s paperwork and the label on the chimney system will tell you, or we can look when we&rsquo;re on the roof.</p>

<h2>Cap vs. shroud at a glance</h2>
<div class="tablebox"><table><thead><tr><th></th><th>Chimney cap</th><th>Chimney shroud</th></tr></thead><tbody>
<tr><td>Main job</td><td>Keep rain, snow, debris and animals out of the flue</td><td>Finish the top of the chimney; often covers several flues and the cap</td></tr>
<tr><td>Size</td><td>Covers the flue opening</td><td>Wraps the top of the chimney or chase</td></tr>
<tr><td>Spark protection</td><td>Mesh can act as a spark arrestor (R1003.9.2 rules apply on masonry chimneys)</td><td>Depends on the design and what&rsquo;s under it</td></tr>
<tr><td>Factory-built chimney</td><td>Use the cap listed for the chimney system</td><td>Must be listed and labeled for that specific system (R1005.2)</td></tr>
<tr><td>Masonry chimney</td><td>Flue cover on top of a sloped crown (R1003.9.1)</td><td>A design choice; still needs a crown that sheds water and room for the flue to vent</td></tr>
</tbody></table></div>

<h2>Two more code points while you&rsquo;re up there</h2>
<p>A new cap or shroud is a good time to check the rest of the chimney top. Two rules in the same chapter of Utah&rsquo;s code (<a href="{UP}" rel="noopener">2021 Utah Residential Code</a>):</p>
<ul>
<li><strong>Height (R1003.9):</strong> chimneys must extend at least 2 feet higher than any part of the building within 10 feet, and at least 3 feet above the highest point where the chimney passes through the roof.</li>
<li><strong>Crickets (R1003.20):</strong> a chimney needs a cricket, a small peaked diverter on the uphill side, where its dimension parallel to the ridgeline is greater than 30 inches and it doesn&rsquo;t intersect the ridgeline. On a wide chimney, that&rsquo;s what keeps water and snow from piling up behind it.</li>
</ul>
<p>Your city&rsquo;s building department enforces the code edition it has adopted, so it has the final word on local details.</p>

<figure>{img("chimney-shroud-12", "Two black chimney shrouds being built in the shop")}<figcaption>Two shrouds being built in the shop before they go up on the roof.</figcaption></figure>

<h2>Which one does your chimney need?</h2>
<p>Every chimney with an open flue needs something keeping water and animals out, and that&rsquo;s the cap. A shroud is optional. It&rsquo;s about how the chimney looks, and on a masonry chimney it can be designed to suit the house. On a factory-built chimney, it has to be a shroud listed for that system.</p>
<p>If you&rsquo;re in the Salt Lake City area and want help choosing, call us at <a href="tel:{S["tel"]}">{S["phone"]}</a> or <a href="@/{CONTACT}">send a message</a>. We speak English and Spanish, and you can browse our <a href="@/ChimneyCap-Shroud.php">caps and shrouds</a> and <a href="@/chimney.php">chimney work</a> first.</p>

<h2>Frequently asked questions</h2>
{faq_html(FAQ)}

<p class="sources"><strong>Sources:</strong> <a href="{UP}" rel="noopener">Utah Residential Code 2021, Chapter 10 (UpCodes)</a> &middot; <a href="{ICC}" rel="noopener">International Code Council: Utah adopts the 2021 I-Codes</a> &middot; <a href="{INSP}" rel="noopener">InspectApedia: Chimney Shrouds (Baird, 1991)</a> &middot; <a href="{IMC}" rel="noopener">IMC 805.6, via Buckley Rumford</a>. Code text checked 17 October 2026.</p>
'''


def page():
    trail = [("Home", ""), ("Guide", PATH)]
    lede = "What each one does, what Utah&rsquo;s code says about shrouds on factory-built chimneys, and how to tell which your chimney needs."
    body = phero(trail, TITLE + ": What&rsquo;s the Difference?", lede, "chimney-shroud-04", "Long black chimney shroud on a stone chimney over a flat roof", "Jemza Roofing guide") + f'''
<section class="sec"><div class="wrap split top post-grid"><article class="prose post reveal">
<p class="byline mono">By Jemza Roofing &middot; Salt Lake City &middot; 17 October 2026</p>{ART}</article>
<aside class="side reveal"><div class="card-cta"><p class="label light">Caps &amp; shrouds</p><h3>Thinking about a new shroud?</h3><p>Call the office or send photos of your chimney.</p>
<a class="phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn light" href="@/{CONTACT}">Get a Quote {ARROW}</a></div>
<ul class="side-links"><li><a href="@/ChimneyCap-Shroud.php">Chimney caps &amp; shrouds</a></li><li><a href="@/chimney.php">Chimney services</a></li><li><a href="@/metal-roofing.php">Metal roofing</a></li></ul></aside>
</div></section>''' + cta()
    import re, html as h
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", h.unescape(re.sub(r"<[^>]+>", " ", ART))))
    return {"path": PATH, "title": "Chimney Cap vs. Chimney Shroud: The Difference | Jemza",
            "meta": "Chimney cap vs. chimney shroud: what each does, Utah's code rule for shrouds on factory-built chimneys, spark arrestor mesh sizes, and how to choose one.",
            "body": body, "og": "chimney-shroud-04", "ogtype": "article", "full_biz": False, "words": words,
            "schema": [crumbs_ld(PATH, trail), faq_ld(FAQ),
                       {"@type": "BlogPosting", "@id": U + PATH + "#article", "headline": TITLE + ": What's the Difference?", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": U + "#organization"}, "publisher": {"@id": U + "#organization"}, "mainEntityOfPage": U + PATH,
                        "image": U + "assets/img/chimney-shroud-04.webp", "wordCount": words, "inLanguage": "en-US",
                        "about": ["Chimney cap", "Chimney shroud"], "citation": [UP, ICC, INSP, IMC]}]}
