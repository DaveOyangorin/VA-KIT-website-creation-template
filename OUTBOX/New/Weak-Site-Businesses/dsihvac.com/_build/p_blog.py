"""New blog post for dsihvac.com (23 Oct 2026): furnace filters and MERV ratings. Informational; it doesn't target "hvac company draper" or a
service keyword. Sources: US EPA, "What is a MERV rating?" (updated 14 Jan 2026); EPA, "Guide to Air Cleaners in the Home" (updated 1 Oct
2026); ENERGY STAR, "Heating & Cooling" and "Maintenance Checklist" (energystar.gov)."""
from engine import faq_html, faq_ld, canon

SLUG = "how-often-to-change-your-furnace-filter/"
H1 = "How often to change your furnace filter (and what MERV rating to buy)"
FAQ = [("How often should I change my furnace filter?", "ENERGY STAR says to check it every month, especially in heavy-use winter and summer months, and to change it at least every 3 months. EPA notes manufacturers typically recommend 60 to 90 days, and sooner if filters come out heavily soiled."),
       ("What MERV rating should I use?", "EPA recommends a filter rated at least MERV 13, or as high a rating as your system fan and filter slot can accommodate. It says most systems can take a MERV 13 without equipment problems, but to check with an HVAC technician first."),
       ("Is a higher MERV always better?", "A higher MERV traps more small particles, but a filter your system can&rsquo;t move enough air through isn&rsquo;t an upgrade. That&rsquo;s why EPA says to ask a technician what your fan and filter slot can handle."),
       ("Does a better filter clean all the air in my house?", "No. EPA says no air cleaner or filter will eliminate all the pollutants in your home; reducing sources and ventilating with clean outdoor air come first.")]
BODY = f'''<p class="answer">Check your furnace filter every month and change it at least every three months, more often when it looks dirty or the system is running hard in winter and summer. If you&rsquo;re upgrading, EPA recommends a filter rated at least MERV 13, or the highest rating your system&rsquo;s fan and filter slot can handle, and a snug fit so air can&rsquo;t sneak around it.</p>

<p>The filter is the cheapest part of a heating and air system and the one homeowners touch most often. It&rsquo;s also the one that gets forgotten. A clogged filter makes the blower work harder, and a filter that doesn&rsquo;t fit lets dust go straight into the equipment. Here&rsquo;s what the US Environmental Protection Agency (EPA) and ENERGY STAR say about choosing and changing one.</p>

<h2>Why the filter matters</h2>
<p>Your furnace or air handler pulls air from the house through return vents, passes it through the filter, heats or cools it and sends it back out. The filter has two jobs: protecting the equipment from dust and debris, and catching some of the particles floating in your home&rsquo;s air.</p>
<p>ENERGY STAR is blunt about what happens when it&rsquo;s neglected: a dirty filter can increase energy costs and damage your equipment, leading to early failure. EPA adds that a filter that is dirty and overloaded won&rsquo;t work well. Either way you pay for it, in the utility bill or in a repair.</p>

<h2>How often to check and change it</h2>
<p>ENERGY STAR&rsquo;s advice is to check your filter every month, especially during the heavy-use months of winter and summer, and to change it at least every three months. Its maintenance checklist puts it as inspecting, cleaning or changing the filters in your central air conditioner, furnace or heat pump once a month.</p>
<p>EPA points to the manufacturer&rsquo;s instructions, noting that manufacturers typically recommend replacement every 60 to 90 days, and that if a filter looks heavily soiled when you replace it, you should change it more often.</p>
<p>In practice, homes with pets, construction dust, a lot of foot traffic or long runtimes during a cold snap or a heat wave tend to load filters faster. The monthly check is how you find your home&rsquo;s real interval: pull the filter, hold it up to the light, and if you can&rsquo;t see through it, it&rsquo;s time.</p>

<h2>What MERV means</h2>
<p>MERV stands for Minimum Efficiency Reporting Value. EPA describes it as a rating of a filter&rsquo;s ability to capture particles between 0.3 and 10 microns. The scale on EPA&rsquo;s chart runs from 1 to 16, and the higher the MERV rating, the better the filter is at trapping specific sizes of particles. HEPA filters are a separate category and aren&rsquo;t rated on the MERV scale.</p>
<p>EPA notes that filters rated MERV 13 and above are required to demonstrate at least 50% removal efficiency for the smallest particles.</p>

<h3>EPA&rsquo;s recommendation: MERV 13 if your system can take it</h3>
<p>If you&rsquo;re upgrading, EPA recommends choosing a filter rated at least MERV 13, or as high a rating as your system fan and filter slot can accommodate. It says most furnaces and HVAC systems can use a MERV 13 filter without creating equipment problems, but it also advises consulting a professional HVAC technician to find the highest-efficiency filter that will work best for your system.</p>
<p>The reason for the caution is airflow. A denser filter can make it harder for some blowers to move air through the system. A technician can look at your equipment, your filter slot and how the system is running before you commit to a case of filters.</p>

<h2>Fit matters as much as the rating</h2>
<p>A high-MERV filter that leaves gaps around the edges filters less air than you think, because air takes the easy path around it. EPA&rsquo;s guidance:</p>
<ul>
<li>Make sure the filter fits snugly so air does not leak around it.</li>
<li>You shouldn&rsquo;t have to bend or crush the filter to make it fit.</li>
<li>Check the size printed on the frame of the old filter and buy that size.</li>
<li>Install it with the airflow arrow pointing in the direction the air moves, toward the furnace or air handler.</li>
</ul>

<h2>What a filter can&rsquo;t do</h2>
<p>EPA points out that furnace and HVAC filters only filter the air while the system is running, which during heating and cooling seasons is usually less than 25% of the time. Running the fan longer gets more air through the filter, but longer run times also increase electricity costs.</p>
<p>And no filter does everything. In EPA&rsquo;s words, no air cleaner or filter will eliminate all of the air pollutants in your home. The most effective ways to improve indoor air are to reduce or remove the sources of pollutants and to ventilate with clean outdoor air. Filtration helps, but it doesn&rsquo;t replace those steps.</p>

<h2>A five-minute filter routine</h2>
<ol>
<li><strong>Find the slot.</strong> It&rsquo;s usually beside or under the furnace, or behind a large return grille.</li>
<li><strong>Turn the system off</strong> at the thermostat before you pull the old filter.</li>
<li><strong>Read the frame.</strong> Note the size and the airflow arrow.</li>
<li><strong>Look at it.</strong> If it&rsquo;s gray and you can&rsquo;t see light through it, replace it now and check sooner next time.</li>
<li><strong>Slide the new one in</strong> with the arrow toward the equipment, snug and without bending.</li>
<li><strong>Write the date</strong> on the frame so next month&rsquo;s check is easy.</li>
</ol>

<h2>Filters and the yearly tune-up</h2>
<p>A clean filter is the homeowner&rsquo;s half of maintenance. The other half is a yearly tune-up, which ENERGY STAR recommends for HVAC equipment. Its checklist for a contractor visit includes tightening electrical connections, lubricating moving parts, checking the condensate drain, cleaning the cooling coils, checking refrigerant, and on the heating side, checking gas connections, burner combustion and the heat exchanger.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Not sure what filter your system can take, or due for a tune-up? Proformance Heating and Air serves Draper and the south Salt Lake Valley with free quotes. Call <a href="tel:+13852267667">385-226-7667</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>US EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/what-merv-rating" rel="noopener">What is a MERV rating?</a> (updated January 14, 2026)</li>
<li>US EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home" rel="noopener">Guide to Air Cleaners in the Home</a> (updated October 1, 2026)</li>
<li>ENERGY STAR, <a href="https://www.energystar.gov/saveathome/heating-cooling" rel="noopener">Heating &amp; Cooling</a></li>
<li>ENERGY STAR, <a href="https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist" rel="noopener">Maintenance Checklist</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Corner Canyon area, Draper, Utah &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Furnace filters", H1, "From the blog &middot; Oct 23, 2026", "Blog", "How Often to Change Your Furnace Filter | Proformance",
                  "How often to change a furnace filter, what MERV rating to buy and why fit matters, from EPA and ENERGY STAR guidance. Check monthly, change every 3 months.",
                  BODY, image="pf-hero", alt="Corner Canyon area, Draper", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": "Proformance Heating and Air"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
