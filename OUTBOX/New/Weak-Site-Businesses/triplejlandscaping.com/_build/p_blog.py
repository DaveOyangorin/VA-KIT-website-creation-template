"""New blog post for triplejlandscaping.com (22 Oct 2026): watering a Utah lawn. Informational; it doesn't target landscaping, sprinkler
repair, sod or hardscape keywords. Sources: Utah State University Extension: "Responsible Water Use for Drought" (Kelly Kopp), "Basic
Turfgrass Care", "Watering the Landscape: Make It Easier With Evapotranspiration (ET)", "Irrigation System Maintenance" and "Reducing
Residential Landscape Water Use in Utah: Technologies and Strategies" (2025)."""
from engine import faq_html, faq_ld, canon

SLUG = "how-much-to-water-your-lawn-in-utah/"
H1 = "How much to water your lawn in Utah: the half-inch rule"
FAQ = [("How much water should I put on my lawn each time?", "USU Extension generally recommends about &frac12; inch of water per irrigation. Its turfgrass guide gives a range of &frac12; to 1 inch each time you irrigate."),
       ("How many times a week should I water?", "It depends on the weather. Utah&rsquo;s Weekly Lawn Watering Guide uses weather-station data to tell you how often to water, assuming &frac12; inch per watering. During drought restrictions, twice a week (about 1 inch total) is enough to keep grass alive, according to USU."),
       ("What time of day should I water?", "Early morning, when it&rsquo;s cool and calm. USU recommends avoiding 10 a.m. to 6 p.m. to cut evaporation losses."),
       ("Why is water running off my lawn?", "Your sprinklers are applying water faster than the soil can absorb it. USU recommends watering in short, repeated cycles with about an hour between them so water can soak in.")]
BODY = f'''<p class="answer">For most Utah lawns, USU Extension recommends about &frac12; inch of water each time you irrigate, early in the morning, with the number of waterings per week set by the weather. Check Utah&rsquo;s Weekly Lawn Watering Guide for how often, find out how long your sprinklers take to put down &frac12; inch, and split run times into short cycles if water runs off.</p>

<p>Utah is a dry place with a thirsty habit. According to Utah State University Extension, Utah is the second driest state in the nation by average precipitation, yet among the top states in water use per person, and urban landscape irrigation accounts for as much as 65% of annual municipal water use, much of it applied beyond what plants need. The good news: watering correctly saves water and grows a healthier, more drought-tolerant lawn. Here&rsquo;s how USU&rsquo;s turf and water specialists say to do it.</p>

<h2>The half-inch rule</h2>
<p>USU water conservation and turfgrass specialist Kelly Kopp puts it simply: <strong>&ldquo;We generally recommend putting out &frac12; inch of water with each irrigation.&rdquo;</strong> USU&rsquo;s turfgrass care guide gives a range of &frac12; to 1 inch each time you water. Utah&rsquo;s Weekly Lawn Watering Guide is built on the same assumption of &frac12; inch per irrigation.</p>
<p>Deep, less frequent watering matters because it encourages roots to grow deeper, which USU notes makes a lawn healthier and more drought tolerant. Frequent shallow watering keeps roots near the surface, where they dry out first.</p>

<h2>How often: let the weather decide</h2>
<p>A lawn&rsquo;s water needs change with the weather. USU explains this through evapotranspiration (ET), the water lost through evaporation from soil and transpiration from plants. As temperatures rise, ET rises and lawns need more frequent watering; when it cools, they need less. Summer needs more irrigation than spring or fall.</p>
<p>That&rsquo;s why USU recommends not watering on a fixed schedule all season. Instead:</p>
<ul>
<li><strong>Use the Weekly Lawn Watering Guide.</strong> Utah&rsquo;s Division of Water Resources publishes a weekly guide, based on weather-station data from across the state, that tells you how many times to water that week.</li>
<li><strong>Adjust your controller with the seasons.</strong> USU&rsquo;s irrigation maintenance guide reminds homeowners that spring and fall need less water than midsummer.</li>
<li><strong>Consider a smart controller.</strong> USU lists smart irrigation controllers among the most useful tools for cutting residential landscape water use.</li>
</ul>
<p>During drought, USU&rsquo;s advice is that watering twice a week, about 1 inch total, is plenty to keep grass alive. It may go dormant and turn golden for a while, but dormancy is normal, and the lawn recovers when temperatures cool.</p>

<h2>How long to run your sprinklers</h2>
<p>To put down &frac12; inch, you need to know how fast your sprinklers apply water. USU&rsquo;s drought guidance gives typical figures by head type:</p>
<div class="tbl"><table><thead><tr><th>Sprinkler head</th><th>Precipitation rate</th><th>Run time for &frac12;&Prime;</th><th>Suggested cycling</th></tr></thead><tbody>
<tr><td>Spray head</td><td>1.3&ndash;2.0&Prime;/hr</td><td>23&ndash;15 min</td><td>3 cycles (8 or 5 min)</td></tr>
<tr><td>Rotor head</td><td>0.4&ndash;1.0&Prime;/hr</td><td>75&ndash;30 min</td><td>3 cycles (25 or 10 min)</td></tr>
<tr><td>Multi-stream, multi-trajectory (MSMT)</td><td>0.4&ndash;0.6&Prime;/hr</td><td>75&ndash;50 min</td><td>3 cycles (25 or 17 min)</td></tr>
</tbody></table></div>
<p>Your system may differ. USU&rsquo;s Water Check program can measure exactly how long your system takes to apply &frac12; inch and how evenly it waters: technicians set catch cups across the lawn, run the sprinklers for a few minutes, and calculate your precipitation rate and uniformity. You can do a simpler version yourself with straight-sided cans spread around the lawn.</p>

<h2>Water early, and in cycles</h2>
<ul>
<li><strong>Early morning.</strong> USU recommends irrigating in the early morning when it&rsquo;s cool and the wind isn&rsquo;t blowing, and avoiding 10 a.m. to 6 p.m. to minimize evaporation.</li>
<li><strong>Cycle and soak.</strong> If puddles form or water runs off, water in short, repeated cycles, allowing about an hour between them so water can move into the soil. USU&rsquo;s maintenance guide gives the same advice for slopes and sandy or clay soils.</li>
<li><strong>Treat sun and shade differently.</strong> Shady areas need much less water than sunny ones.</li>
<li><strong>Spot-water brown patches.</strong> Small areas can brown in hot weather because of uneven sprinklers. Rather than running the whole system longer, USU suggests hand-watering or using a hose-end sprinkler on those spots.</li>
</ul>

<h2>Keep the system in shape</h2>
<p>A sprinkler system that wastes water can&rsquo;t follow any schedule well. USU recommends checking your system monthly for leaks and for damaged or clogged heads. At spring start-up, its maintenance checklist covers cleaning out the controller, replacing the battery, checking wiring and rain or frost sensors, flushing lines, and running each valve to look for tilted, buried or misaligned heads, clogged nozzles, and misting that can signal high water pressure. USU&rsquo;s 2025 water-use fact sheet also points to efficient nozzles, drip irrigation for beds, and drought-tolerant grass varieties as ways to cut water use further.</p>

<h2>Mow higher, water smarter</h2>
<p>Watering and mowing work together. USU recommends mowing Utah lawns at 2 to 4 inches, and around 3 inches to improve heat and drought tolerance, because taller grass grows deeper roots that can reach water deeper in the soil. Follow the one-third rule: don&rsquo;t cut off more than a third of the blade at once, and leave the clippings on the lawn to return nitrogen and reduce evaporation. Aerating improves water infiltration and reduces compaction and thatch.</p>

<h2>Beds, trees and shrubs</h2>
<p>Lawn rules don&rsquo;t apply to everything. USU recommends hand-watering or drip irrigation for flower beds, vegetable gardens and shrub beds, with water reaching about 6 inches deep for flowers and vegetables and 2 feet for established trees and shrubs. Cover bare soil in beds with 2 to 3 inches of mulch to save water and cut weeding.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>About &frac12; inch per watering; let the weekly guide and the weather set how often.</li>
<li>Water early in the morning, never 10 a.m.&ndash;6 p.m.</li>
<li>Know your sprinklers&rsquo; run time for &frac12; inch, and cycle-and-soak if water runs off.</li>
<li>Check heads and leaks monthly; mow at about 3 inches.</li>
</ul>

<p>Triple J Landscaping installs and repairs sprinkler systems and builds water-wise yards across Salt Lake County. For a free estimate, call <a href="tel:+13852275475">385-227-5475</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>USU Extension, <a href="https://extension.usu.edu/drought/news-articles/responsible-water-use" rel="noopener">Responsible Water Use for Drought</a></li>
<li>USU Extension, <a href="https://extension.usu.edu/yardandgarden/research/basic-turfgrass-care" rel="noopener">Basic Turfgrass Care</a></li>
<li>USU Extension, <a href="https://extension.usu.edu/cwel/research/watering-the-landscape-make-it-easier-with-et" rel="noopener">Watering the Landscape: Make It Easier With Evapotranspiration (ET)</a></li>
<li>USU Extension, <a href="https://extension.usu.edu/yardandgarden/research/irrigation-system-maintenance" rel="noopener">Irrigation System Maintenance</a></li>
<li>USU Extension, <a href="https://extension.usu.edu/climate/research/reducing-residential-landscape-water-use-in-utah-technologies-and-strategies" rel="noopener">Reducing Residential Landscape Water Use in Utah: Technologies and Strategies</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Watering your lawn", H1, "From the blog &middot; Oct 22, 2026", "Blog", "How Much to Water Your Lawn in Utah | Triple J Landscaping",
                  "USU Extension's half-inch rule for Utah lawns: how often to water, sprinkler run times by head type, early-morning cycles and mowing higher for deeper roots.",
                  BODY, image="tj-sod", alt="A healthy new lawn", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "How much to water your lawn in Utah: the half-inch rule", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Triple J Landscaping"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
