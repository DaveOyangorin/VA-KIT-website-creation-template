"""New post (23 Oct 2026): what a FORTIFIED roof is. Informational; doesn't target "roofing company millcreek". Sources: IBHS FORTIFIED
program pages fortifiedhome.org/roof/ and fortifiedhome.org (read 23 Oct 2026)."""
from engine import faq_html, faq_ld, canon

SLUG = "what-is-a-fortified-roof/"
H1 = "What is a FORTIFIED roof? A homeowner&rsquo;s guide to the IBHS standard"
FAQ = [("Who created FORTIFIED?", "The Insurance Institute for Business &amp; Home Safety (IBHS). FORTIFIED is described on its site as a program of IBHS."),
       ("Does FORTIFIED only work with shingles?", "No. IBHS says the FORTIFIED Roof approach works with nearly any roof covering, including shingles, metal, tile and low-slope systems."),
       ("Will a FORTIFIED roof lower my insurance?", "IBHS says insurers in some areas offer premium discounts for homes with a FORTIFIED designation, but it doesn&rsquo;t give amounts. Ask your own insurer whether it offers one in Utah."),
       ("How does a home get the designation?", "A FORTIFIED-trained contractor installs the upgrades, an independent certified FORTIFIED Evaluator documents them, and IBHS reviews the documentation and issues the designation.")]
BODY = f'''<p class="answer">A FORTIFIED roof is a re-roof or new roof built to a standard from the Insurance Institute for Business &amp; Home Safety (IBHS). It adds stronger roof edges, a sealed roof deck and ring-shank nails in a tighter pattern, with an optional upgrade to impact-rated shingles. An independent evaluator documents the work, and IBHS issues the designation.</p>

<p>Most people only think about their roof when something goes wrong. But the roof is the part of a house that takes the brunt of wind and hail, and IBHS says its post-storm studies generally find that between 70% and 90% of related insurance claims include damage to the roof. The FORTIFIED program grew out of that research. Here is what it involves, in plain language, from the program&rsquo;s own pages.</p>

<h2>What FORTIFIED is</h2>
<p>IBHS describes FORTIFIED as a voluntary construction and re-roofing program designed to strengthen homes and commercial buildings against severe weather such as high winds, hail, hurricanes and tornadoes. There are three levels for homes: FORTIFIED Roof, FORTIFIED Silver and FORTIFIED Gold. The roof level is the starting point, and the one most homeowners meet when it&rsquo;s time to replace a roof anyway.</p>
<p>According to the program, more than 100,000 families have chosen FORTIFIED. It isn&rsquo;t a brand of shingle. IBHS says the FORTIFIED Roof approach works with nearly any roof covering, including shingles, metal, tile and low-slope systems.</p>

<h2>The four upgrades, explained</h2>
<h3>1. Stronger edges</h3>
<p>FORTIFIED Roof calls for a wider drip edge, the metal flashing along the roof&rsquo;s perimeter, and a fully adhered starter strip, the first course of material at the eaves and rakes. The goal is to keep the edge of the roof covering from peeling up.</p>

<h3>2. A sealed roof deck</h3>
<p>The roof deck is the layer of boards under the shingles. If wind strips the covering off, rain can pour through the gaps between those boards. IBHS testing found that each inch of rain on an exposed deck can equal nine bathtubs of water coming into a home. Sealing the seams of the deck, the program says, can reduce that water intrusion by up to 95%. It&rsquo;s a backup layer for the moment the first layer fails.</p>

<h3>3. Ring-shank nails</h3>
<p>Smooth nails hold the deck to the rafters by friction. Ring-shank nails have ridges along the shank that grip the wood. FORTIFIED replaces smooth nails with ring-shank nails in an enhanced pattern, and IBHS says this nearly doubles the roof&rsquo;s strength against the forces of wind, with tighter spacing able to double the uplift a roof withstands.</p>

<h3>4. Impact-resistant shingles (optional)</h3>
<p>For hail, FORTIFIED offers a Hail Supplement. Under it, asphalt shingles must be rated Good or Excellent on the IBHS Hail Impact-Resistant Shingle Ratings, and the program says qualifying shingles are rated for hail up to 2 inches in diameter.</p>

<h2>How a home gets the designation</h2>
<p>The program describes three steps:</p>
<ol>
<li><strong>Find a contractor and an evaluator.</strong> You need a FORTIFIED-trained contractor and an independent evaluator who will verify that FORTIFIED standards are applied. The program&rsquo;s site has a provider locator.</li>
<li><strong>Apply the standard.</strong> The contractor installs the upgrades while a certified FORTIFIED Evaluator documents the key elements, many of which are hidden once the roof is finished.</li>
<li><strong>Receive the designation.</strong> IBHS experts review the documentation and issue the FORTIFIED designation.</li>
</ol>
<p>That documentation step is the point: a sealed deck and nail pattern can&rsquo;t be checked after the shingles go on, so the evaluator records them during the job.</p>

<h2>Insurance and incentives</h2>
<p>IBHS says insurers in some areas offer discounts on homeowners insurance premiums for homes with a FORTIFIED designation, and some offer FORTIFIED endorsements that may pay to upgrade a roof to the standard if it&rsquo;s replaced after a covered loss. It notes that mitigation grants may be available in some places, naming programs in North Carolina and Alabama. None of that is guaranteed in Utah; ask your insurance agent what applies to your policy before you re-roof.</p>

<h2>Why the hidden parts matter</h2>
<p>Most of what FORTIFIED changes is invisible from the street. Once the shingles are on, nobody can see whether the deck seams were sealed, what nails were used or how closely they were spaced. That is why the program relies on an evaluator during the job rather than an inspection afterward, and why IBHS reviews the documentation before issuing a designation.</p>
<p>It also explains the program&rsquo;s focus on the roof first. IBHS notes that much severe convective storm damage, the kind caused by thunderstorms, hail and high winds, can be prevented by strengthening the vulnerable areas of a home, and the roof is the largest of them.</p>

<h2>Questions to ask before a re-roof</h2>
<ul>
<li>Are you FORTIFIED-trained, and can you work with a FORTIFIED Evaluator?</li>
<li>Will the deck seams be sealed, and what nails and nailing pattern will you use?</li>
<li>What drip edge and starter strip will you install at the eaves and rakes?</li>
<li>If hail is a concern, what is the IBHS hail rating of the shingle you&rsquo;re proposing?</li>
<li>Does my insurer offer a discount or endorsement for a FORTIFIED designation?</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Thinking about a new roof in Millcreek? Call RoofTek at <a href="tel:+18014712054">801-471-2054</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Insurance Institute for Business &amp; Home Safety, <a href="https://fortifiedhome.org/roof/" rel="noopener">FORTIFIED Roof</a> (fortifiedhome.org)</li>
<li>Insurance Institute for Business &amp; Home Safety, <a href="https://fortifiedhome.org/" rel="noopener">FORTIFIED Home</a> (fortifiedhome.org)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Mount Olympus, Utah &middot; Jeff McGrath, CC BY-SA 3.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "FORTIFIED roofs", H1, "From the blog &middot; Oct 23, 2026", "Blog", "What Is a FORTIFIED Roof? IBHS Standard Explained | RoofTek",
                  "What a FORTIFIED roof is: stronger edges, a sealed roof deck, ring-shank nails and impact-rated shingles, and how IBHS designates a home.",
                  BODY, image="hero", alt="Mount Olympus, Utah", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1.replace("&rsquo;", "'"), "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
