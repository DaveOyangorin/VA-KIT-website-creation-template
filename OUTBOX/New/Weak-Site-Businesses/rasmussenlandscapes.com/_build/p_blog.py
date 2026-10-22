"""New blog post for rasmussenlandscapes.com (21 Oct 2026): when to start watering a Utah lawn and how much. Informational: it doesn't
target sprinkler repair, lawn care or any service keyword. Sources: Utah Division of Water Resources / Slow the Flow (Weekly Lawn
Watering Guide, USU Center for Water Efficient Landscaping cycle chart); KSL.com, 22 Apr 2025 (Candice Hasenyager, Utah Division of
Water Resources; Kelly Kopp, USU). Rasmussen's own seasonal practice from its sprinkler pages."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/when-to-water-your-lawn-utah/"
H1 = "When should you start watering your lawn in Utah?"
CYCLE = [("Spray heads", "1.3&ndash;2.0 in/hr", "15&ndash;23 min", "3 cycles of 5&ndash;8 min"), ("Rotors", "0.4&ndash;1.0 in/hr", "30&ndash;75 min", "3 cycles of 10&ndash;25 min"),
         ("Multi-stream rotary nozzles", "0.4&ndash;0.8 in/hr", "38&ndash;75 min", "3 cycles of 17&ndash;25 min")]
FAQ = [("When should I turn on my sprinklers in Utah?", "Having the system turned on and tested in April or May is fine. Rasmussen&rsquo;s crews do most turn-ons then. But the Utah Division of Water Resources says most lawns don&rsquo;t need watering until about Mother&rsquo;s Day, or when daytime highs regularly reach the 70s."),
       ("How many times a week should I water?", "It changes with the weather. The state&rsquo;s Weekly Lawn Watering Guide gives a recommended number of watering cycles for each county every week of the season. Check it weekly, or use a smart controller."),
       ("How long should each watering run?", "It depends on your sprinkler type. USU&rsquo;s chart puts half an inch of water at about 15&ndash;23 minutes for spray heads and 30&ndash;75 minutes for rotors, split into three shorter cycles so water soaks in instead of running off."),
       ("My lawn is turning yellow. Does it need more water?", "Not always. USU&rsquo;s Kelly Kopp has noted that discoloration often calls for fertilizer, not more water. Check soil moisture first, and look for dry spots caused by a sprinkler head that isn&rsquo;t covering its area.")]
BODY = f'''<p class="answer">Most Utah lawns don&rsquo;t need watering until about mid-May. The state&rsquo;s water managers suggest waiting until about Mother&rsquo;s Day, or until daytime highs regularly reach the 70s. After that, let the Utah Division of Water Resources&rsquo; weekly guide tell you how many times to water, and split each watering into short cycles so it soaks in.</p>

<p>Every spring the same thing happens across the Salt Lake Valley. The first warm weekend arrives, sprinklers come on, and lawns get watered every day whether they need it or not. Utah is the second-driest state in the nation, so that habit costs a lot of water. It also costs your lawn: grass watered early and often grows shallow roots, and shallow roots are the first to fail in July.</p>

<h2>Wait for the lawn to need it</h2>
<p>In April 2025, KSL reported the state&rsquo;s advice for the season. Candice Hasenyager, director of the Utah Division of Water Resources, said residents should wait until about Mother&rsquo;s Day, or until high temperatures regularly reach the 70s, before irrigating. Water managers said most Utahns don&rsquo;t need to water until mid-May at the earliest. The point, in Hasenyager&rsquo;s words, is to hold off on irrigating until your landscape needs it.</p>
<p>Why wait? Kelly Kopp, a Utah State University professor and director of USU&rsquo;s Center for Water Efficient Landscaping, explained that most grass is still recovering from winter and has moisture left from spring storms and the soil. Watering too early and too often can hinder root growth, which leaves the lawn more prone to drought stress later. Kopp also noted that many residents use about twice as much water as they need, and that a lawn that looks discolored in spring often needs fertilizer, not water.</p>

<h2>Turn the system on, but don&rsquo;t start the schedule</h2>
<p>There&rsquo;s a difference between turning your sprinkler system on and starting to water. Spring is the right time to bring the system back to life and check it, before you need it. When Rasmussen&rsquo;s crews do spring turn-ons (mostly in April and May), they open the stop-and-waste valve slowly while listening for leaks. Then they run every zone, walk each one to flag heads that don&rsquo;t work or spray the wrong way, and make repairs. They set the clock for the season but leave it off. The homeowner turns it on when the weather warms up.</p>
<p>That sequence lets you find a broken head or a leaking valve in April, not in the middle of a July heat wave, without wasting water in the meantime.</p>

<h2>How many times a week? Let the weekly guide decide</h2>
<p>Lawns need different amounts of water in May than in July. The Utah Division of Water Resources publishes a <strong>Weekly Lawn Watering Guide</strong> that recommends how many irrigation cycles to run that week in each Utah county, based on the forecast and local conditions. Slow the Flow, the state&rsquo;s water conservation program, suggests bookmarking it and checking it weekly. During the season the division posts it every week.</p>
<p>A smart (weather-based) irrigation controller does the same job automatically. If you have an older clock, the habit to build is simple: check the guide, then adjust the number of watering days.</p>

<h2>How long each time? It depends on your sprinkler heads</h2>
<p>Different sprinkler heads put down water at very different rates, so &ldquo;15 minutes per zone&rdquo; means very different things. Slow the Flow shares this chart from USU&rsquo;s Center for Water Efficient Landscaping for applying about half an inch of water:</p>
<div class="tbl"><table><thead><tr><th>Sprinkler type</th><th>Precipitation rate</th><th>Runtime for 0.5&Prime;</th><th>Suggested cycles</th></tr></thead><tbody>
{"".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in CYCLE)}
</tbody></table></div>
<p>Notice the last column: the total time is split into <strong>three shorter cycles</strong>. That&rsquo;s cycle-and-soak watering. Spray heads in particular put water down faster than many Utah soils can absorb it. Three short runs with a break between each let the water soak in instead of running down the gutter.</p>

<h2>Summer: watch for dry spots, not just the calendar</h2>
<p>By July, the heat changes everything. Rasmussen&rsquo;s summer sprinkler tune-up, offered from July and sometimes through September, starts with a walk around the yard looking for dry spots, pooling water and other signs of watering trouble. A brown patch in an otherwise green lawn usually isn&rsquo;t a sign that the whole yard needs more water. It&rsquo;s a sign that one head is clogged, tilted, blocked by a plant that grew in front of it, or not getting enough pressure. Fix the head, and you can often water less overall.</p>
<p>Other clues that something in the system is wrong: water pooling when the sprinklers aren&rsquo;t running, soggy grass that never dries out, or dry spots where coverage doesn&rsquo;t reach. Those usually point to a broken line or a valve problem rather than a schedule problem.</p>

<h2>Fall: taper off, then shut down before the freeze</h2>
<p>As days shorten and temperatures fall, lawns need less water, and the weekly guide will show fewer cycles. Keep watering through the fall growth spurt, but don&rsquo;t let the system sit full of water into a hard freeze. Starting in October, Rasmussen&rsquo;s sprinkler teams shut systems off at the stop-and-waste valve, then push compressed air through every zone to clear out remaining water so pipes and valves don&rsquo;t crack over the winter.</p>

<h2>A simple Utah watering checklist</h2>
<ul>
<li><strong>April&ndash;May:</strong> turn the system on and test every zone. Leave the clock off.</li>
<li><strong>Around Mother&rsquo;s Day, or when highs reach the 70s:</strong> start watering.</li>
<li><strong>Every week:</strong> check the state&rsquo;s Weekly Lawn Watering Guide for your county and adjust.</li>
<li><strong>Every watering:</strong> run three short cycles, timed for your sprinkler type.</li>
<li><strong>July:</strong> walk the yard for dry spots and fix heads before adding minutes.</li>
<li><strong>October:</strong> shut off and blow out the system before a hard freeze.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Want your system turned on, tuned up or blown out the right way? Call Rasmussen Landscapes at <a href="tel:+18014660303">(801) 466-0303</a> for a quote over the phone, or read how we handle <a href="@/sprinklers/">sprinkler turn-ons, tune-ups and shut-offs</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Slow the Flow (Utah Division of Water Resources), <a href="https://slowtheflow.org/tools-and-resources/weekly-watering/" rel="noopener">Weekly Watering Guide</a>, including the cycle-length chart from Utah State University&rsquo;s Center for Water Efficient Landscaping</li>
<li>Utah Division of Water Resources, <a href="https://wateringindex.utah.gov/traditional-wlwg.html" rel="noopener">Weekly Lawn Watering Guide</a></li>
<li>KSL.com, <a href="https://www.ksl.com/article/51299176/why-should-you-wait-to-water-your-lawn-according-to-these-utah-experts" rel="noopener">&ldquo;Why should you wait to water your lawn, according to these Utah experts&rdquo;</a> (April 22, 2025)</li>
<li>Rasmussen Landscapes, <a href="@/sprinklers/">Sprinklers</a> and <a href="@/sprinkler-maintenance/">Sprinkler Maintenance</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "When to water", H1, "From the blog &middot; Oct 21, 2026", "Blog", "When to Start Watering Your Lawn in Utah | Rasmussen",
                  "Most Utah lawns don't need water until mid-May. When to start, how often to water with the state's weekly guide, and how long to run each sprinkler type.",
                  BODY, image="ras-sprinkler-spray", alt="A sprinkler watering a lawn in morning light", crumbs=[("Blog", "blog/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "Rasmussen Landscapes"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
