"""New blog post for whitepineplumbingut.com (22 Oct 2026): hard water and your plumbing. Informational; it doesn't target "plumber south
jordan", drain cleaning, water heater or emergency keywords. Sources: USGS Water Science School, "Hardness of Water" (updated 24 Aug 2026);
EPA, "Consumer Confidence Report (CCR) Information for Consumers" and the CCR home page (updated 9 Sep 2026)."""
from engine import faq_html, faq_ld, canon

SLUG = "hard-water-and-your-plumbing/"
H1 = "Hard water and your plumbing: what it does and how to check yours"
FAQ = [("What makes water hard?", "USGS defines water hardness as the amount of dissolved calcium and magnesium in the water."),
       ("Is hard water bad for my health?", "USGS says hardness is not a health concern, but it can be a nuisance. It notes the World Health Organization says drinking water may contribute calcium and magnesium to the diet."),
       ("How hard is &ldquo;hard&rdquo;?", "USGS classifies water as soft at 0&ndash;60 mg/L (as calcium carbonate), moderately hard at 61&ndash;120, hard at 121&ndash;180, and very hard above 180 mg/L."),
       ("How do I find out how hard my water is?", "Check your water supplier&rsquo;s Consumer Confidence Report, the annual drinking water quality report community water systems must deliver by July 1, or ask your local water utility. USGS suggests contacting your local health agency, utility or a water-softener vendor for local information.")]
BODY = f'''<p class="answer">Hard water is water with a lot of dissolved calcium and magnesium. According to USGS, it isn&rsquo;t a health concern, but when it&rsquo;s heated it can leave calcium carbonate scale that clogs pipes, lowers water pressure, cuts water heater efficiency and shortens equipment life. To know how hard your own water is, check your water supplier&rsquo;s annual drinking water quality report.</p>

<p>If you&rsquo;ve noticed white crust on faucets, spots on glasses or a water heater that doesn&rsquo;t seem to keep up the way it used to, hard water may be part of the story. USGS notes that hard water is common in the east-central and western United States. Here&rsquo;s what hardness actually is, what it does inside a home&rsquo;s plumbing, and how to find reliable numbers for your own tap.</p>

<h2>What &ldquo;hard water&rdquo; means</h2>
<p>The U.S. Geological Survey defines hardness simply: <strong>the amount of dissolved calcium and magnesium in the water</strong>. Those minerals come from the ground the water passes through, and some other metals can contribute too. USGS explains that hard water was prevalent in the east-central and western U.S., reflecting carbonate aquifers and aquifers with high dissolved solids.</p>

<h2>How hardness is measured</h2>
<p>USGS reports hardness in milligrams per liter (mg/L) as calcium carbonate and uses four classes:</p>
<div class="tbl"><table><thead><tr><th>Classification</th><th>Hardness (mg/L as calcium carbonate)</th></tr></thead><tbody>
<tr><td>Soft</td><td>0 to 60</td></tr><tr><td>Moderately hard</td><td>61 to 120</td></tr><tr><td>Hard</td><td>121 to 180</td></tr><tr><td>Very hard</td><td>More than 180</td></tr></tbody></table></div>
<p>You&rsquo;ll also see hardness given in &ldquo;grains per gallon&rdquo; on water softener labels and some utility reports. It&rsquo;s a different unit for the same thing, so check which unit a report uses before comparing numbers.</p>

<h2>What hard water does to plumbing</h2>
<p>USGS lists several effects, and most of them show up in a home&rsquo;s plumbing and appliances:</p>
<ul>
<li><strong>Scale when water is heated.</strong> Heated hard water can leave solid deposits of calcium carbonate. USGS says these deposits can reduce the life of equipment, raise heating costs and lower the efficiency of water heaters.</li>
<li><strong>Clogged pipes and lower pressure.</strong> Scale can build up inside pipes, narrowing them and reducing water pressure.</li>
<li><strong>Soap scum and more detergent.</strong> Soap reacts with calcium to form soap scum, so you need more soap or detergent to get things clean.</li>
<li><strong>Spots and worn fabrics.</strong> Hard water can leave spots or a film on dishes and glassware, and can shorten the life of clothes and fabrics.</li>
</ul>
<p>The water heater is where scale tends to matter most, because heating is what drives the minerals out of solution. That&rsquo;s why the efficiency and lifespan points above are worth taking seriously if you know your water is hard.</p>

<h2>Is it a health problem?</h2>
<p>No. USGS is clear that <strong>hardness is a property of water that is not a health concern, but it can be a nuisance</strong>. It also notes that the World Health Organization says drinking water may contribute calcium and magnesium to the diet, which can matter for people who get little of these minerals elsewhere. Treating hard water is usually about protecting plumbing and appliances, and about comfort, not safety.</p>

<h2>How to find out how hard your water is</h2>
<p>National maps give the big picture, but USGS cautions that its national hardness map uses 1975 data that is not designed for local decisions. For your own home, go local:</p>
<ol>
<li><strong>Read your Consumer Confidence Report (CCR).</strong> EPA explains that community water systems must deliver this annual drinking water quality report to their customers each year by July 1. It covers where your water comes from, contaminants detected, and contact information. Many utilities include hardness in the report or will tell you if you ask.</li>
<li><strong>Use EPA&rsquo;s CCR search.</strong> EPA&rsquo;s &ldquo;Find Your Consumer Confidence Report&rdquo; tool can help you locate your supplier&rsquo;s report.</li>
<li><strong>Ask your water utility</strong>, your local health agency, or a water-softener vendor, the sources USGS suggests for local information.</li>
</ol>
<p>If you&rsquo;re on a private well, there&rsquo;s no utility report, so testing is the way to know.</p>

<h2>Signs hard water may be affecting your home</h2>
<p>Based on the effects USGS describes, these are the clues worth noticing:</p>
<ul>
<li>White, chalky buildup on faucets and showerheads</li>
<li>Spots or film on dishes and glassware</li>
<li>Soap that doesn&rsquo;t lather well, or soap scum that keeps coming back</li>
<li>Water pressure that seems lower than it used to be</li>
<li>A water heater that seems less efficient or doesn&rsquo;t last as long as expected</li>
</ul>
<p>None of these alone proves your water is hard, but together with a hardness number from your CCR, they help you decide whether it&rsquo;s worth doing something about.</p>

<h2>What you can do</h2>
<ul>
<li><strong>Know your number.</strong> Start with your water supplier&rsquo;s report so you&rsquo;re working from real data, not guesses.</li>
<li><strong>Consider a water softener.</strong> If your water is hard and the effects above are bothering you, a softener is the usual whole-home answer. A plumber can help size and install one properly.</li>
<li><strong>Keep an eye on the water heater.</strong> Since heating is what creates scale, the water heater deserves attention in hard-water homes.</li>
<li><strong>Watch for pressure changes.</strong> A slow drop in pressure can be a sign of buildup somewhere in the system and is worth having checked.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Thinking about a water softener, or worried about your water heater? White Pine Plumbing handles water softeners, water heaters and plumbing repairs in South Jordan. Call or text <a href="tel:+14353575862">435-357-5862</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. Geological Survey, Water Science School, <a href="https://www.usgs.gov/special-topics/water-science-school/science/hardness-water" rel="noopener">Hardness of Water</a> (updated August 24, 2026)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/ccr/ccr-information-consumers" rel="noopener">Consumer Confidence Report (CCR) Information for Consumers</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/ccr" rel="noopener">Consumer Confidence Reports (CCR)</a> (updated September 9, 2026)</li>
</ul></div>
<p class="small photo-credit">Banner photo: South Jordan &middot; Jeremy Taylor, CC BY 2.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Hard water &amp; your plumbing", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Hard Water and Your Plumbing: What It Does | White Pine",
                  "Hard water explained: what USGS says it does to pipes, pressure and water heaters, how hardness is measured, and how to find your own water's numbers.",
                  BODY, image="wp-hero", alt="Sunset over South Jordan", crumbs=[("Blog", "blank/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "White Pine Plumbing"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
