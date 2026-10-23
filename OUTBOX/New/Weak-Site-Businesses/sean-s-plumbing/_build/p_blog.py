"""New post (23 Oct 2026): hard water explained. Informational; doesn't target "plumber south jordan". Source: U.S. Geological Survey,
Water Science School, "Hardness of Water" (updated 24 Aug 2026). Unit conversion: 1 grain per gallon = 17.1 mg/L (arithmetic)."""
from engine import faq_html, faq_ld, canon

SLUG = "hard-water-explained/"
H1 = "Hard water explained: what the numbers mean for your home"
FAQ = [("What makes water hard?", "Dissolved calcium and magnesium, picked up as water moves through soil and rock, according to the U.S. Geological Survey."),
       ("What counts as hard water?", "USGS classes water with 121 to 180 mg/L as calcium carbonate as hard, and over 180 mg/L as very hard. Soft is 0 to 60, and moderately hard is 61 to 120."),
       ("Is hard water bad for my health?", "USGS says hardness is not a health concern, but it can be a nuisance. It also notes the WHO view that drinking water may contribute some calcium and magnesium to the diet."),
       ("Why does my water heater get scale?", "USGS explains that heating hard water forms solid calcium carbonate deposits, which can shorten equipment life, raise heating costs and lower the efficiency of electric water heaters."),
       ("Does hard water affect my clothes?", "USGS says hard water means you need more detergent for laundry, and that it can shorten the life of fabrics and clothes."),
       ("How do I clean mineral buildup out of a coffee maker?", "USGS notes that coffee makers build up the same minerals, and that running vinegar through them helps dissolve the deposits."),
       ("Why is hard water so common in the West?", "USGS links hard water in the east-central and western United States to carbonate aquifers and aquifers with high dissolved-solids concentrations. Check your own water report for local numbers.")]
BODY = f'''<p class="answer">Hard water is water with a lot of dissolved calcium and magnesium. The U.S. Geological Survey (USGS) classes it by milligrams per liter as calcium carbonate: soft is 0 to 60, moderately hard 61 to 120, hard 121 to 180, and very hard above 180. It isn&rsquo;t a health concern, USGS says, but it leaves soap scum and spots, and it builds scale in water heaters and pipes.</p>

<p>If you&rsquo;ve ever scrubbed white crust off a faucet, wondered why glasses come out of the dishwasher spotted, you&rsquo;ve met hard water. Here&rsquo;s what it is, how it&rsquo;s measured and what it does in a home, from the USGS Water Science School.</p>

<h2>What hardness is</h2>
<p>USGS defines water hardness as the amount of dissolved calcium and magnesium in the water. Other dissolved metals can contribute, but those two are the main players.</p>
<p>They come from the ground. As rain and snowmelt move through soil and rock, USGS explains, water dissolves small amounts of naturally occurring minerals and carries them into groundwater. Water is a strong solvent for calcium and magnesium, so where those minerals are present, the water picks them up.</p>

<h2>Where hard water is common</h2>
<p>USGS mapped hardness at national monitoring sites in the 1970s and found hard water in the east-central and western United States, a pattern it ties to carbonate aquifers and aquifers with high dissolved-solids concentrations. It cautions that the national data are for regional patterns only and aren&rsquo;t meant for decisions about an individual property. For your own home, use your water provider&rsquo;s annual water quality report or a test.</p>

<h2>How it&rsquo;s measured</h2>
<p>USGS expresses hardness in milligrams per liter (mg/L) as calcium carbonate. Its general guidelines:</p>
<ul>
<li><strong>Soft:</strong> 0 to 60 mg/L</li>
<li><strong>Moderately hard:</strong> 61 to 120 mg/L</li>
<li><strong>Hard:</strong> 121 to 180 mg/L</li>
<li><strong>Very hard:</strong> more than 180 mg/L</li>
</ul>
<p>Water reports and test kits sometimes give hardness in grains per gallon instead. One grain per gallon equals 17.1 mg/L, so multiply by 17.1 to compare with the USGS scale. For example, 10 grains per gallon is about 171 mg/L, which lands in the hard range. Our <a href="@/#tool">hardness converter</a> does it for you.</p>

<h2>What hard water does in a home</h2>
<h3>Soap, skin and laundry</h3>
<p>USGS explains that calcium in hard water reacts with soap to form soap scum, the film you feel on your hands after washing. Because some of the soap is used up that way, you need more soap or detergent to get hands, hair and laundry clean. USGS adds that hard water can shorten the life of fabrics and clothes.</p>
<h3>Dishes and glassware</h3>
<p>The spots and film left on dishes and glasses are hard-water residue. USGS calls them unsightly but not dangerous.</p>
<h3>Water heaters and appliances</h3>
<p>This is where hardness costs money. When hard water is heated, as in a water heater, calcium carbonate can come out of solution and form solid deposits called scale. USGS says scale can shorten the life of equipment, raise the cost of heating water, lower the efficiency of electric water heaters and clog pipes. Coffee makers build up the same minerals; USGS notes that running vinegar through them helps dissolve the deposits.</p>
<h3>Pipes</h3>
<p>Over many years, scale can build up inside pipes, narrowing them and reducing water flow and pressure, according to USGS. Industries in hard-water areas sometimes pay to soften water for the same reason: it can damage equipment.</p>

<h2>Is hard water a health problem?</h2>
<p>No, says USGS: hardness is not a health concern, but it can be a nuisance. It also points out that people need minerals to stay healthy, and that the World Health Organization notes drinking water may contribute calcium and magnesium to the diet, which could matter for people whose intake is marginal.</p>

<h2>What you can do</h2>
<ul>
<li><strong>Find your number.</strong> Check your water provider&rsquo;s water quality report, or use a test kit.</li>
<li><strong>Clean fixtures regularly.</strong> Mineral deposits on faucet aerators and shower heads are easier to remove before they build up.</li>
<li><strong>Ask about the water heater.</strong> Since USGS says scale shortens water heater life, ask a plumber what maintenance makes sense for your unit.</li>
<li><strong>Compare treatment options.</strong> USGS points to local water-softening vendors as a source of local information; ask what any system needs for maintenance before you buy.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Scale, low pressure or water heater trouble in South Jordan? Call Sean&rsquo;s Plumbing at <a href="tel:+14358506314">435-850-6314</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. Geological Survey, Water Science School, <a href="https://www.usgs.gov/special-topics/water-science-school/science/hardness-water" rel="noopener">Hardness of Water</a> (updated August 24, 2026)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Oquirrh Lake, Daybreak &middot; Dean Derhak, CC BY-SA 3.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Hard water", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Hard Water Explained: What the Numbers Mean | Sean's",
                  "Hard water explained: the USGS hardness scale, converting grains per gallon to mg/L, and what calcium and magnesium do to fixtures and water heaters at home.",
                  BODY, image="hero", alt="Oquirrh Lake in Daybreak, South Jordan", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
