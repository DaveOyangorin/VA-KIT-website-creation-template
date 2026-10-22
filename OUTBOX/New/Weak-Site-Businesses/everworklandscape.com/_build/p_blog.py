"""New blog post for everworklandscape.com (22 Oct 2026): how to water a Utah lawn. Informational; it doesn't target "landscaping sandy",
"lawn care sandy" or any sprinkler service keyword. Sources: USU Extension, "Training Turfgrass for Drought Resilience" (Kopp and Goodspeed,
April 2026); USU Extension CWEL news, "Why wait to water your lawn" (23 Apr 2025); USU Extension Juab County, "Watering Smarter: Lawn Care
During Drought"; EPA WaterSense, "Watering Tips" (updated 11 Mar 2026); Utah Division of Water Resources Weekly Lawn Watering Guide."""
from engine import faq_html, faq_ld, canon

SLUG = "utah-lawn-watering-guide/"
H1 = "How to water a Utah lawn: deeper, less often"
FAQ = [("How much water does a lawn need each week?", "EPA WaterSense says a landscape typically needs about one inch of water a week, including rainfall. In Utah, the state&rsquo;s Weekly Lawn Watering Guide gives a county-by-county number of waterings per week based on recent weather."),
       ("When should I start watering in spring?", "Utah water managers advised in April 2025 that most Utahns didn&rsquo;t need to water until mid-May at the earliest, around Mother&rsquo;s Day or when highs regularly reach the 70s. USU Extension notes that watering too early can hinder root growth."),
       ("What time of day should I water?", "Early morning. USU Extension says early-morning watering reduces evaporation losses, and recommends calm, low-wind periods. EPA advises avoiding the middle of the day."),
       ("Is a brown lawn dead?", "Not necessarily. USU Extension explains that turfgrass naturally goes dormant during extended drought and that drought-stressed grass is usually dormant and capable of recovery.")]
BODY = f'''<p class="answer">Water a Utah lawn deeply and less often, not a little every day. Aim for moisture about 6 inches down, check with a screwdriver, and stretch the days between waterings gradually. Water early in the morning, keep spray off the pavement, and follow the state&rsquo;s Weekly Lawn Watering Guide for how many times a week your county needs.</p>

<p>Most lawn problems we see along the Wasatch Front aren&rsquo;t caused by too little water. They come from water applied the wrong way: short daily cycles, midday runs, heads spraying the sidewalk, and controllers still set for August in October. Utah State University Extension and the EPA&rsquo;s WaterSense program both point to the same handful of habits. Here they are in plain language.</p>

<h2>1. Water deeply, then wait</h2>
<p>Grass roots grow where the water is. USU Extension&rsquo;s April 2026 fact sheet <em>Training Turfgrass for Drought Resilience</em> explains that frequent, shallow watering keeps moisture near the surface, so roots stay shallow. Extending the time between waterings and watering deeper lets moisture move lower in the soil, and the roots follow.</p>
<p>USU Extension&rsquo;s advice is to apply water &ldquo;deeply enough to wet the active root zone&rdquo; and to avoid frequent, shallow irrigation, especially during drought. A USU Extension drought handout from Juab County puts a number on it: rather than focusing on minutes, aim for moisture about <strong>6 inches</strong> into the soil.</p>

<h2>2. Check the depth with a screwdriver</h2>
<p>You don&rsquo;t need special tools. USU Extension suggests a simple screwdriver or soil probe: either one moves easily through moist soil but not through dry soil. Push it in the day after watering. If it stops after an inch or two, the water isn&rsquo;t getting deep enough.</p>
<p>As a starting point, the Juab County handout suggests running pop-up spray heads for about 15 minutes and gear-driven (rotary) heads for about 30 minutes, then probing the next day and adjusting.</p>

<h2>3. Stretch the days between waterings gradually</h2>
<p>Don&rsquo;t go from daily watering to once a week overnight. USU Extension notes that reducing frequency over time lets the grass adapt without severe stress, and that even in sandy soils, step-by-step changes can condition turf to handle longer intervals.</p>
<p>How do you know when it&rsquo;s time? USU Extension says slight leaf wilting or a dull, bluish-gray color can signal that soil moisture is running low, and that these early symptoms don&rsquo;t mean permanent damage.</p>

<h2>4. Measure what your sprinklers put down</h2>
<p>EPA WaterSense says a landscape typically needs about <strong>one inch of water a week, including rainfall</strong>. To learn how long your system takes, EPA suggests the can test:</p>
<ol>
<li>Set a few empty, straight-sided cans (tuna cans work) around one zone.</li>
<li>Run the zone and time how long it takes to fill them with a half inch of water.</li>
<li>Try watering that length of time twice a week, then adjust for weather and how your lawn responds.</li>
</ol>
<p>Uneven cans tell you something too: one zone getting much more water than another usually means a tilted, clogged or mismatched head.</p>

<h2>5. Use Utah&rsquo;s Weekly Lawn Watering Guide</h2>
<p>National rules of thumb are a start, but Utah weather swings fast. The Utah Division of Water Resources publishes a <strong>Weekly Lawn Watering Guide</strong> with a recommended number of waterings per week for each county, based on recent weather and evapotranspiration (how much water the grass is actually losing). According to the state, it publishes every Friday and assumes about half an inch of water per watering, which lines up neatly with the can test above. There is also a separate guide for lawns intentionally planted with low-water-use grass.</p>

<h2>6. Don&rsquo;t start too early in spring</h2>
<p>Green-up doesn&rsquo;t mean your lawn is thirsty. In April 2025, after a good winter for most of the state, Utah water managers said most Utahns didn&rsquo;t need to water until mid-May at the earliest. The guidance from Candice Hasenyager, director of the Utah Division of Water Resources, was to wait until around Mother&rsquo;s Day or until highs regularly reach the 70s. USU Extension&rsquo;s summary: watering too early can hinder root growth and increase drought stress later.</p>
<p>That&rsquo;s different from turning your system on. A spring startup checks every zone for freeze damage before you need the water. Most Salt Lake and Utah County systems are started in mid to late April, and then you water only as the lawn needs it.</p>

<h2>7. Water early in the morning, and keep it on the grass</h2>
<ul>
<li><strong>Morning.</strong> USU Extension says early-morning watering reduces evaporation losses, and recommends choosing calm, low-wind periods. EPA advises avoiding the middle of the day, when the sun evaporates much of the water.</li>
<li><strong>On the lawn, not the sidewalk.</strong> EPA&rsquo;s advice is to set sprinklers to keep water on the landscape and off the pavement.</li>
<li><strong>Stop runoff.</strong> If water begins to pool, EPA says to turn the sprinkler off. On clay or slopes, split run times into shorter cycles with breaks so the water can soak in.</li>
<li><strong>Adjust with the seasons.</strong> EPA notes that irrigation schedules should change with the seasons, and suggests checking monthly for leaks and broken or clogged heads.</li>
</ul>

<h2>8. Mow higher and feed the soil</h2>
<p>Watering isn&rsquo;t the only lever. USU Extension notes that a higher mowing height shades the soil, reduces evaporation and supports deeper roots. It also recommends returning grass clippings when you mow, adding compost or organic amendments, and aeration to relieve compaction, all of which help roots grow deeper.</p>

<h2>9. Brown isn&rsquo;t always dead</h2>
<p>If a dry spell gets ahead of you, don&rsquo;t panic. USU Extension explains that turfgrass naturally goes dormant during extended drought, and drought-stressed grass is usually dormant and capable of recovery. A June 2026 episode of USU Extension&rsquo;s <em>The Green Thumb</em> on Utah Public Radio added that the cool-season grasses in most Utah lawns recover when cooler conditions return.</p>

<h2>Quick checklist</h2>
<ul>
<li>Water to about 6 inches deep; check with a screwdriver the next day.</li>
<li>Fewer, longer waterings; stretch the gap gradually.</li>
<li>Watch for wilting or a bluish-gray color before you water again.</li>
<li>Do the half-inch can test on each zone.</li>
<li>Follow Utah&rsquo;s Weekly Lawn Watering Guide for your county.</li>
<li>Wait until about mid-May to start regular watering in a normal year.</li>
<li>Water in the early morning, off the pavement, with no runoff.</li>
<li>Mow higher, leave the clippings, aerate compacted soil.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Heads spraying the street, dry spots that never green up, or a controller you can&rsquo;t make sense of? Everwork fixes and tunes sprinkler systems across Salt Lake and Utah County. Call or text <a href="tel:+18018758109">(801) 875-8109</a>, day or night.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Kelly Kopp and Jerry Goodspeed, USU Extension, <a href="https://extension.usu.edu/cwel/research/training-turfgrass-for-drought-resilience" rel="noopener">Training Turfgrass for Drought Resilience</a> (April 2026)</li>
<li>USU Extension Center for Water-Efficient Landscaping, <a href="https://extension.usu.edu/cwel/news/why-wait-to-water-lawn" rel="noopener">Why should you wait to water your lawn</a> (April 23, 2025)</li>
<li>USU Extension, Juab County, <a href="https://extension.usu.edu/juab/files/WateringSmarterLawnCareDuringDrought.pdf" rel="noopener">Watering Smarter: Lawn Care During Drought</a></li>
<li>Utah Public Radio, <a href="https://www.upr.org/show/the-green-thumb/2026-06-19/green-thumb-training-your-lawn" rel="noopener">The Green Thumb: Training your lawn to become more self-sufficient</a> (June 19, 2026)</li>
<li>U.S. EPA WaterSense, <a href="https://www.epa.gov/watersense/watering-tips" rel="noopener">Watering Tips</a> (updated March 11, 2026)</li>
<li>Utah Division of Water Resources, <a href="https://conservewater.utah.gov/weekly-lawn-watering-guide/" rel="noopener">Weekly Lawn Watering Guide</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Utah lawn watering guide", H1, "From the blog &middot; Oct 22, 2026", "Blog", "How to Water a Utah Lawn: Deeper, Less Often | Everwork",
                  "How to water a Utah lawn: deep, less frequent watering, the screwdriver and can tests, when to start in spring and the state's weekly watering guide.",
                  BODY, image="ew-striped", alt="Crisp mowing stripes and clean sidewalk edges on a front lawn", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Everwork Property Maintenance & Landscaping"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
