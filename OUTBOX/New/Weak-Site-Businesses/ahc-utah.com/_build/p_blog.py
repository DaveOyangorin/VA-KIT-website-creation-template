"""New blog post for ahc-utah.com (22 Oct 2026): carbon monoxide safety at home. Informational; it doesn't target furnace repair, AC repair,
HVAC company or other service keywords. Sources: U.S. EPA ("Carbon Monoxide's Impact on Indoor Air Quality", "Protect Your Family and Yourself
from Carbon Monoxide Poisoning") and NFPA ("Carbon monoxide safety", which cites the 2023 NFIRS data and a 2023 CDC study). CDC and CPSC
pages were unreachable (403) on 22 Oct."""
from engine import faq_html, faq_ld, canon

SLUG = "carbon-monoxide-safety/"
H1 = "Carbon monoxide at home: sources, symptoms and where alarms belong"
FAQ = [("Where should carbon monoxide alarms go?", "NFPA says to install CO alarms in a central location outside each sleeping area, on every level of the home, and anywhere else your local codes require. For the best protection, interconnect them so when one sounds, they all sound."),
       ("How often should I test a CO alarm?", "At least once a month, according to NFPA. Replace the alarm on the schedule in the manufacturer&rsquo;s instructions."),
       ("What should I do if the CO alarm goes off?", "Move everyone to fresh air right away, outdoors or by an open window or door, make sure everyone is accounted for, and call for help from the fresh-air location. Stay there until emergency personnel arrive."),
       ("How often should a furnace be checked for carbon monoxide safety?", "EPA recommends having fuel-burning appliances, including furnaces, inspected by a trained professional at the beginning of every heating season, and having central heating systems, flues and chimneys inspected, cleaned and tuned up every year.")]
BODY = f'''<p class="answer">Carbon monoxide (CO) is an odorless, colorless gas made whenever fuel burns. In a home, the usual sources are furnaces, water heaters, gas stoves, fireplaces and cars in attached garages. Protect your family with CO alarms outside every sleeping area and on every level, test them monthly, and have fuel-burning appliances inspected at the start of every heating season.</p>

<p>Salt Lake winters mean furnaces running for months, windows shut tight, and cars warming up on cold mornings. That&rsquo;s exactly the season when carbon monoxide becomes a real household risk. You can&rsquo;t see it, taste it or smell it, and its early symptoms feel like the flu. Here&rsquo;s what the U.S. Environmental Protection Agency (EPA) and the National Fire Protection Association (NFPA) say about where CO comes from, how to recognize it, and how to keep it out of your home.</p>

<h2>What carbon monoxide is</h2>
<p>EPA describes carbon monoxide as an odorless, colorless and toxic gas. It&rsquo;s produced whenever any fuel, such as gas, oil, kerosene, wood or charcoal, is burned. NFPA adds that it forms when fuels burn incompletely, and calls it the &ldquo;invisible killer.&rdquo;</p>
<p>When fuel-burning appliances are maintained and used properly, EPA says, the amount of CO they produce is usually not hazardous. The danger comes when equipment isn&rsquo;t working properly or is used incorrectly. Because it&rsquo;s impossible to see, taste or smell, EPA warns that CO can kill before you are aware it is in your home.</p>

<h2>How big a problem is it?</h2>
<p>NFPA reports that in 2023, U.S. fire departments responded to 82,245 carbon monoxide incidents. It also cites a 2023 study by the Centers for Disease Control and Prevention, which found that unintentional, non-fire-related CO poisoning was responsible each year (2005 to 2018) for about 101,847 emergency department visits, 14,365 hospitalizations and at least 430 deaths.</p>

<h2>Where CO comes from in a home</h2>
<p>EPA lists these common sources:</p>
<ul>
<li>Leaking chimneys and furnaces</li>
<li>Back-drafting from furnaces, gas water heaters, wood stoves and fireplaces</li>
<li>Gas stoves and gas ranges that aren&rsquo;t properly adjusted</li>
<li>Unvented kerosene and gas space heaters</li>
<li>Generators and other gasoline-powered equipment</li>
<li>Car exhaust from attached garages</li>
<li>Worn or poorly adjusted and maintained combustion devices, such as boilers and furnaces</li>
<li>A furnace flue that is improperly sized, blocked, disconnected or leaking</li>
</ul>
<p>For context, EPA notes that average CO levels in homes without gas stoves run from 0.5 to 5 parts per million (ppm). Near properly adjusted gas stoves, levels are often 5 to 15 ppm; near poorly adjusted stoves they may be 30 ppm or higher.</p>

<h2>Symptoms to know</h2>
<p>EPA explains that the effects of CO vary from person to person, depending on age, overall health, the concentration and how long the exposure lasts:</p>
<ul>
<li><strong>Low levels:</strong> shortness of breath, mild nausea and mild headaches. EPA notes low levels may have longer-term health effects, and can cause fatigue in healthy people and chest pain in people with heart disease.</li>
<li><strong>Moderate levels:</strong> severe headaches, dizziness, mental confusion, nausea or fainting.</li>
<li><strong>High levels:</strong> impaired vision and coordination, and death. NFPA says high levels can be fatal within minutes.</li>
</ul>
<p>The tricky part is that these symptoms look like the flu or food poisoning. EPA points to one telling clue: <strong>flu-like symptoms that clear up after you leave home.</strong> If everyone in the house feels ill at the same time, and better when they&rsquo;re away, take it seriously.</p>
<p>Some people are more vulnerable. EPA names fetuses, infants, elderly people, and people with anemia or a history of heart or respiratory disease. NFPA adds pregnant women and people with conditions like emphysema or asthma.</p>

<h2>If you suspect CO poisoning</h2>
<ol>
<li><strong>Get fresh air immediately.</strong> EPA says to open doors and windows, turn off combustion appliances and leave the house.</li>
<li><strong>Get medical help.</strong> EPA advises going to an emergency room and telling the physician you suspect CO poisoning. It can often be diagnosed with a blood test done soon after exposure.</li>
<li><strong>Answer the doctor&rsquo;s questions.</strong> Do symptoms happen only at home? Do they fade when you leave? Is anyone else sick, and did it start at the same time? Which fuel-burning appliances do you use, and when were they last inspected?</li>
</ol>

<h2>CO alarms: where they go and how to keep them working</h2>
<p>NFPA&rsquo;s guidance on carbon monoxide alarms:</p>
<ul>
<li>Install CO alarms in a <strong>central location outside each sleeping area</strong> and on <strong>every level of the home</strong>, plus anywhere local laws, codes or standards require.</li>
<li>For the best protection, <strong>interconnect</strong> them, so when one sounds, they all sound.</li>
<li>Follow the manufacturer&rsquo;s instructions for placement and mounting height.</li>
<li>Choose an alarm that carries the label of a recognized testing laboratory.</li>
<li><strong>Test CO alarms at least once a month</strong>, and replace them according to the manufacturer&rsquo;s instructions.</li>
<li>If the trouble signal sounds, check the battery and replace it if it&rsquo;s low. If it still sounds, call the fire department.</li>
<li>If the CO alarm sounds, move to fresh air right away, outdoors or by an open window or door. Make sure everyone is accounted for, call for help from there, and stay until emergency personnel arrive.</li>
<li>Call your local fire department&rsquo;s non-emergency number ahead of time to find out what number to call if your CO alarm sounds.</li>
</ul>

<h2>Prevention: the habits that matter most</h2>
<h3>Get appliances inspected every heating season</h3>
<p>EPA&rsquo;s first prevention step is to have your fuel-burning appliances inspected by a trained professional <strong>at the beginning of every heating season</strong>: oil and gas furnaces, gas water heaters, gas ranges and ovens, gas dryers, space heaters, fireplaces and wood stoves. Make sure flues and chimneys are connected, in good condition and not blocked. EPA also recommends having a trained professional inspect, clean and tune up the central heating system, including furnaces, flues and chimneys, every year, and repairing any leaks promptly.</p>

<h3>Vent to the outside</h3>
<p>EPA recommends choosing appliances that vent their fumes outdoors whenever possible, having them properly installed, and maintaining them according to the manufacturer&rsquo;s instructions. Install and use an exhaust fan vented outdoors over gas stoves, and open the flue when the fireplace is in use.</p>

<h3>Winter habits for a Utah home</h3>
<ul>
<li><strong>Don&rsquo;t idle the car in the garage.</strong> EPA says not to idle a car inside a garage, and NFPA says never to run a vehicle or other fueled engine indoors, even with the garage door open. If you warm up the car, pull it out right after starting it.</li>
<li><strong>Clear vents after a snowstorm.</strong> NFPA reminds homeowners to make sure vents for the dryer, furnace, stove and fireplace are clear of snow, and that a running car&rsquo;s exhaust pipe isn&rsquo;t covered with snow.</li>
<li><strong>Keep generators outside.</strong> EPA warns never to use a portable generator inside homes, garages, crawlspaces or sheds. Deadly CO levels can build quickly and linger for hours after the generator shuts off.</li>
<li><strong>Be careful with space heaters.</strong> EPA suggests a vented space heater when replacing an unvented one. If you must use an unvented gas or kerosene heater, use the proper fuel, follow its cautions, keep doors to the rest of the house open and crack a window for ventilation.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>CO is invisible and odorless. An alarm is the only way to know it&rsquo;s there.</li>
<li>Put CO alarms outside every sleeping area and on every level; test them monthly.</li>
<li>Flu-like symptoms that ease when you leave home are a warning sign.</li>
<li>Have your furnace, water heater and other fuel-burning appliances inspected every heating season.</li>
<li>Never run cars or generators indoors, and clear snow from vents.</li>
</ul>

<p>Affordable Heating &amp; Cooling inspects, tunes up, repairs and installs furnaces in the Salt Lake Valley, all makes and models. To schedule a heating-season check, call <a href="tel:+18012610924">801.261.0924</a> or <a href="@/Contact/">request a free estimate</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/carbon-monoxides-impact-indoor-air-quality" rel="noopener">Carbon Monoxide&rsquo;s Impact on Indoor Air Quality</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/protect-your-family-and-yourself-carbon-monoxide-poisoning" rel="noopener">Protect Your Family and Yourself from Carbon Monoxide Poisoning</a></li>
<li>National Fire Protection Association, <a href="https://www.nfpa.org/education-and-research/home-fire-safety/carbon-monoxide" rel="noopener">Carbon Monoxide Safety</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Carbon monoxide safety", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Carbon Monoxide at Home: Symptoms &amp; CO Alarms | AHC Blog",
                  "Where carbon monoxide comes from in a home, the symptoms that look like the flu, where CO alarms belong, and the winter habits that keep CO out.",
                  BODY, image="ahc-winter", alt="Sugar House Park in snow", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "Carbon monoxide at home: sources, symptoms and where alarms belong", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Affordable Heating & Cooling, Inc."}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
