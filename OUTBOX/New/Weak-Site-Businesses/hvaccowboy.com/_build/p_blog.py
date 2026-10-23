"""New blog post for hvaccowboy.com (22 Oct 2026): carbon monoxide and your furnace. Informational; it doesn't target "hvac company lehi",
furnace repair or AC keywords. Sources: EPA "Carbon Monoxide's Impact on Indoor Air Quality" (updated 15 Jul 2026); NFPA "Carbon Monoxide
Safety" tip sheet (c2017, as distributed by Liberty County, GA)."""
from engine import faq_html, faq_ld, canon

SLUG = "carbon-monoxide-and-your-furnace/"
H1 = "Carbon monoxide and your furnace: what to know before winter"
FAQ = [("Can a furnace cause carbon monoxide?", "Yes. EPA lists leaking chimneys and furnaces, and backdrafting from furnaces, gas water heaters, wood stoves and fireplaces, among the sources of carbon monoxide in homes."),
       ("Where should CO alarms go?", "NFPA says to install CO alarms in a central location outside each sleeping area and on every level of the home, and to interconnect them so that when one sounds, they all sound."),
       ("How often should a furnace be inspected?", "EPA recommends having a trained professional inspect, clean and tune up the central heating system every year, and repairing any leaks promptly. NFPA says to have fuel-burning heating equipment inspected every year before cold weather sets in."),
       ("What do I do if the CO alarm goes off?", "NFPA says to move immediately to fresh air, outdoors or by an open window or door, make sure everyone is accounted for, and call for help from the fresh-air location. Stay there until emergency personnel say it is safe to go back in.")]
BODY = f'''<p class="answer">A furnace that leaks or backdrafts can put carbon monoxide (CO), an odorless, colorless, toxic gas, into your home. EPA recommends a professional inspection, cleaning and tune-up of your heating system every year, and CO alarms on every level outside each sleeping area. If an alarm sounds, NFPA says to get to fresh air first and call for help from there.</p>

<p>Utah Valley furnaces run hard from fall to spring, and that&rsquo;s when carbon monoxide matters most. CO is a byproduct of burning fuel, and it&rsquo;s dangerous precisely because you can&rsquo;t notice it. Here&rsquo;s what the U.S. Environmental Protection Agency (EPA) and the National Fire Protection Association (NFPA) say every homeowner should know before heating season.</p>

<h2>What carbon monoxide is</h2>
<p>EPA describes carbon monoxide as <strong>an odorless, colorless and toxic gas</strong>. Because you can&rsquo;t see, taste or smell it, it can harm you before you know it&rsquo;s there. NFPA calls it the &ldquo;invisible killer&rdquo; and explains that it&rsquo;s created when fuels such as gasoline, wood, coal, natural gas, propane, oil and methane burn incompletely. In the home, heating and cooking equipment that burn fuel can be sources of CO.</p>
<p>NFPA adds that a person can be poisoned by a small amount of CO over a longer period of time, or by a large amount over a shorter time.</p>

<h2>Where it comes from in a home</h2>
<p>EPA lists the common sources of carbon monoxide indoors:</p>
<ul>
<li>Leaking chimneys and furnaces</li>
<li>Backdrafting from furnaces, gas water heaters, wood stoves and fireplaces</li>
<li>Unvented kerosene and gas space heaters</li>
<li>Gas stoves</li>
<li>Car exhaust from attached garages</li>
<li>Tobacco smoke</li>
</ul>
<p>&ldquo;Backdrafting&rdquo; is worth understanding: it&rsquo;s when combustion gases that should go up and out the flue flow back into the house instead. Keeping vents and flues working properly is one reason the annual inspection matters.</p>

<h2>Symptoms to take seriously</h2>
<p>According to EPA, at low concentrations CO can cause fatigue in healthy people and chest pain in people with heart disease. At higher concentrations it can cause impaired vision and coordination, headaches, dizziness, confusion and nausea, flu-like symptoms that may clear up after leaving the home. At very high concentrations it is fatal.</p>
<p>That last detail, symptoms that ease when you leave, is a clue. If everyone in the house feels unwell at home and better elsewhere, take it seriously.</p>

<h2>Step 1: Get the heating system inspected every year</h2>
<p>EPA&rsquo;s first recommendation for reducing exposure is to have a trained professional <strong>inspect, clean and tune up your central heating system every year</strong>, and to repair any leaks promptly. NFPA gives the same advice with a deadline: have fuel-burning heating equipment and chimneys inspected by a professional every year <strong>before cold weather sets in</strong>.</p>
<p>EPA also advises keeping gas appliances properly adjusted, using an exhaust fan vented to the outdoors over gas stoves, and choosing a vented space heater when replacing an unvented one.</p>

<h2>Step 2: Put CO alarms in the right places</h2>
<p>NFPA&rsquo;s guidance on carbon monoxide alarms:</p>
<ul>
<li><strong>Location:</strong> install CO alarms in a central location outside each sleeping area and on every level of the home, plus anywhere local laws, codes or standards require. EPA cites the Consumer Product Safety Commission&rsquo;s matching recommendation: CO alarms on each level, outside each sleeping area.</li>
<li><strong>Interconnect them</strong> so that when one sounds, they all sound.</li>
<li><strong>Follow the manufacturer&rsquo;s instructions</strong> for placement and mounting height.</li>
<li><strong>Choose a listed alarm</strong>, one listed by a qualified testing laboratory.</li>
<li><strong>Test monthly</strong>, and replace alarms according to the manufacturer&rsquo;s instructions.</li>
<li><strong>If the trouble signal chirps</strong>, check the battery and replace it if low. If it still sounds, call the fire department.</li>
</ul>

<h2>Step 3: Know what to do if the alarm sounds</h2>
<ol>
<li><strong>Get to fresh air immediately</strong>, outdoors or by an open window or door.</li>
<li><strong>Account for everyone</strong> in the home.</li>
<li><strong>Call for help from the fresh-air location</strong>, and stay there until emergency personnel say it&rsquo;s safe to go back in.</li>
</ol>
<p>NFPA also suggests calling your local fire department&rsquo;s non-emergency number ahead of time to find out what number to call if your CO alarm sounds.</p>

<h2>Winter habits that matter in Utah</h2>
<p>A few of NFPA&rsquo;s tips are especially relevant along the Wasatch Front:</p>
<ul>
<li><strong>Clear the vents after a storm.</strong> During and after a snowstorm, make sure vents for the dryer, furnace, stove and fireplace are clear of snow.</li>
<li><strong>Don&rsquo;t warm up the car in the garage.</strong> Remove it immediately after starting, even if the garage door is open, and make sure the exhaust pipe isn&rsquo;t covered with snow.</li>
<li><strong>Never heat the house with the oven.</strong></li>
<li><strong>Open the flue</strong> when using a fireplace.</li>
<li><strong>Generators and grills stay outside</strong>, well away from windows, doors and vents.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Due for a furnace check before the cold sets in? Cowboy Heating &amp; Air does furnace repair, installation and maintenance across Utah Valley, with 24/7 emergency service. Call <a href="tel:+18019400420">801-940-0420</a>. If a CO alarm is sounding, get outside and call for help first.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/carbon-monoxides-impact-indoor-air-quality" rel="noopener">Carbon Monoxide&rsquo;s Impact on Indoor Air Quality</a> (updated July 15, 2026)</li>
<li>National Fire Protection Association, Carbon Monoxide Safety tip sheet (&copy;2017), as distributed by <a href="https://libertycountyga.gov/DocumentCenter/View/629/Carbon-Monoxide-Safety-PDF" rel="noopener">Liberty County, Georgia</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Carbon monoxide &amp; your furnace", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Carbon Monoxide and Your Furnace: Before Winter | Cowboy",
                  "Carbon monoxide and your furnace: where CO comes from, symptoms, yearly heating inspections, where CO alarms go and what to do if one sounds. EPA and NFPA.",
                  BODY, image="cb-furnace", alt="Furnace diagnostics with a meter", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Cowboy Heating & Air"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
