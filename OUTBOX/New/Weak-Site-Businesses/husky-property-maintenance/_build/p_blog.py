"""New post (23 Oct 2026): smoke and carbon monoxide alarm basics. Informational; doesn't target "handyman midvale". Sources: U.S. Fire
Administration, "Smoke alarms" (last reviewed 13 Oct 2026) and "Carbon Monoxide Poisoning Prevention" (last reviewed 21 Sep 2026); CPSC,
"Carbon Monoxide Fact Sheet"."""
from engine import faq_html, faq_ld, canon

SLUG = "smoke-and-co-alarm-basics/"
H1 = "Smoke and carbon monoxide alarms: where they go and how to keep them working"
FAQ = [("How many smoke alarms do I need?", "The U.S. Fire Administration says to put smoke alarms inside and outside each bedroom and sleeping area, and on every level of the home."),
       ("How often should I replace smoke alarms?", "USFA says to replace the entire smoke alarm every 10 years, test it monthly, and replace 9-volt or backup batteries at least once a year."),
       ("Where should a CO alarm go?", "USFA says to install CO alarms in a central location outside each separate sleeping area and on every level of your home. CPSC adds that plug-in or hardwired alarms should have battery backup."),
       ("What should I do if the CO alarm goes off?", "CPSC says never ignore it: move outside to fresh air, call 911, and don&rsquo;t go back in until emergency responders say it&rsquo;s safe."),
       ("Do smoke alarms need to be interconnected?", "The U.S. Fire Administration recommends choosing interconnected smoke alarms, so that when one sounds, they all sound."),
       ("Does the CO alarm&rsquo;s test button check the sensor?", "No. CPSC says the test button checks whether the circuitry is operating correctly, not the accuracy of the sensor."),
       ("What does carbon monoxide poisoning feel like?", "CPSC says early symptoms of low to moderate CO poisoning are similar to the flu but without the fever. Higher exposure can cause confusion, vomiting and loss of consciousness.")]
BODY = f'''<p class="answer">Put smoke alarms inside and outside every bedroom and on every level of your home, test them monthly, replace batteries at least yearly, and replace each alarm every 10 years. Install carbon monoxide (CO) alarms outside each sleeping area and on every level. If a CO alarm sounds, get everyone outside and call 911.</p>

<p>Smoke and carbon monoxide alarms are cheap, quiet and easy to forget, right up until the moment they matter. The U.S. Fire Administration (USFA) is blunt about it: a smoke alarm with a dead or missing battery is the same as having no alarm at all. Here&rsquo;s what USFA and the U.S. Consumer Product Safety Commission (CPSC) recommend.</p>

<h2>Smoke alarms</h2>
<h3>Where to put them</h3>
<p>USFA&rsquo;s placement guidance is simple:</p>
<ul>
<li>Inside each bedroom and sleeping area.</li>
<li>Outside each bedroom and sleeping area.</li>
<li>On every level of the home.</li>
</ul>
<p>It also recommends interconnected smoke alarms, so that when one sounds, they all sound. That matters in a house where a fire in the basement might not be heard from an upstairs bedroom.</p>

<h3>Testing and batteries</h3>
<ul>
<li><strong>Test monthly.</strong> Press the test button on each alarm once a month.</li>
<li><strong>Replace batteries yearly.</strong> For alarms with 9-volt batteries, replace them at least once every year. For hardwired alarms, replace the backup battery at least once a year.</li>
</ul>

<h3>Replace the alarm every 10 years</h3>
<p>Smoke alarms don&rsquo;t last forever. USFA says to replace the entire smoke alarm every 10 years. If you don&rsquo;t know how old an alarm is, check the label on it or the manufacturer&rsquo;s instructions.</p>

<h2>Carbon monoxide alarms</h2>
<h3>Why they matter</h3>
<p>USFA calls carbon monoxide the invisible killer because it is a colorless, odorless, poisonous gas. People can&rsquo;t sense it, so they may not know they&rsquo;re being exposed. CO poisoning can happen when a fuel-burning appliance, such as a furnace, heater or generator, isn&rsquo;t working or vented properly.</p>
<p>CPSC notes that the early symptoms of low to moderate CO poisoning are similar to the flu, but without the fever. Higher exposure brings more severe symptoms, including mental confusion, vomiting and loss of consciousness.</p>

<h3>Where to put them</h3>
<p>USFA says to install CO alarms in a central location outside each separate sleeping area and on every level of your home. CPSC&rsquo;s fact sheet says to use battery-operated alarms or alarms with battery backup, so plug-in and hardwired units keep working in a power outage.</p>

<h3>Testing and replacing</h3>
<p>CPSC points out that the test button checks whether the alarm&rsquo;s circuitry is working, not the accuracy of the sensor. It also notes that CO alarms have a recommended replacement age, which you can find in the product literature or from the manufacturer, and that newer alarms have an end-of-life signal to tell you when to replace them.</p>

<h3>If a CO alarm sounds</h3>
<p>CPSC&rsquo;s instruction: never ignore an alarming CO alarm, because it is warning you of a potentially deadly hazard. Move outside to fresh air, call 911, and don&rsquo;t go back inside until emergency responders say it&rsquo;s safe.</p>

<h2>Preventing CO in the first place</h2>
<ul>
<li><strong>Service the heating system.</strong> CPSC recommends having it professionally inspected and serviced every year.</li>
<li><strong>Keep vents clear.</strong> USFA says to make sure vents for the dryer, furnace, stove and fireplace are clear of snow and other debris.</li>
<li><strong>Use generators outside.</strong> USFA says to use portable generators outdoors in well-ventilated areas, away from doors, windows and vents. CPSC adds never to operate a generator or other gasoline engine-powered tool in or near an enclosed space.</li>
<li><strong>Never idle a car in the garage.</strong> CPSC: never leave a car running in an attached garage, even with the garage door open.</li>
</ul>

<h2>A quick household routine</h2>
<ol>
<li>Walk the house once and count: is there a smoke alarm in every bedroom, outside every sleeping area and on every level? A CO alarm outside each sleeping area and on every level?</li>
<li>Find out how old each smoke alarm is.</li>
<li>Pick a day each month to press every test button.</li>
<li>Pick a day each year for new batteries, and put the heating system service on the calendar.</li>
</ol>
<p>Our <a href="@/#tool">home safety checklist</a> keeps the monthly and yearly items in one place.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Need alarms mounted, replaced or interconnected in Midvale? Call Husky Property Maintenance at <a href="tel:+18017425282">801-742-5282</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. Fire Administration, <a href="https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/" rel="noopener">Smoke alarms</a> (last reviewed October 13, 2026)</li>
<li>U.S. Fire Administration, <a href="https://www.usfa.fema.gov/prevention/life-safety-hazards/carbon-monoxide/" rel="noopener">Carbon Monoxide Poisoning Prevention</a> (last reviewed September 21, 2026)</li>
<li>U.S. Consumer Product Safety Commission, <a href="https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet" rel="noopener">Carbon Monoxide Fact Sheet</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Midvale and Murray from the air &middot; Famartin, CC BY-SA 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Smoke &amp; CO alarms", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Smoke and CO Alarm Basics: Placement &amp; Testing | Husky",
                  "Smoke and carbon monoxide alarm basics from USFA and CPSC: where to install them, test monthly, batteries yearly, replace smoke alarms every 10 years.",
                  BODY, image="hero", alt="Midvale from the air", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
