"""New post for swiftrestoreutah.com (the 161 existing posts are built in pages.py from the client's own text).

"A Home Fire Safety Checklist for Northern Utah Winters"
Main phrase: "home fire safety checklist" (informational, prevention). None of the 161 posts covers smoke alarms, heating or
escape basics; the service pages target fire damage restoration (after the fact), so this links to them without competing.
Facts and sources, checked 20 Oct 2026 (both U.S. Fire Administration, FEMA):
- Smoke alarms: https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/ : inside and outside each
  bedroom and sleeping area, on every level including the basement; interconnected so all sound; test monthly; replace 9-volt
  batteries (or the backup battery in hardwired alarms) at least yearly; new alarms every 10 years from the manufacture date;
  you may have less than 2 minutes to get out once an alarm sounds.
- Heating: https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/ : keep anything that can burn at least 3 feet
  from heat sources; turn space heaters off when leaving the room or going to bed; have heating equipment and chimneys cleaned
  and inspected yearly; heating fires were the second leading cause of home fires in 2021 (about 32,200 fires, 190 deaths);
  portable heaters were about 3% of home heating fires but 41% of fatal heating fires (2017-2019).
No prices."""
from engine import faq_html, faq_ld, canon
from cfg import U, NAME, ST

POST = ("A Home Fire Safety Checklist for Northern Utah Winters", "restoration-tips/home-fire-safety-checklist-northern-utah-winters/")
SA = "https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/"
HT = "https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/heating/"
FAQ = [("How often should I test smoke alarms?", "The U.S. Fire Administration says to test them monthly, replace 9-volt batteries (or a hardwired alarm&rsquo;s backup battery) at least once a year, and replace the alarms themselves every 10 years from the manufacture date."),
       ("How far should a space heater be from furniture?", "Keep anything that can burn at least 3 feet from any heat source, including space heaters, fireplaces, wood stoves and radiators, and turn space heaters off when you leave the room or go to bed."),
       ("What should I do after a small house fire?", "Make sure everyone is safe and the fire department has cleared the house. Then call your insurance company and a restoration company. Smoke, soot and the water used to fight the fire keep doing damage, so cleanup should start quickly.")]


def page(K, img):
    A = K.ARROW
    body = f'''<p class="answer">A home fire safety checklist covers the things that keep a small fire small: working smoke alarms in the right places, heaters and chimneys kept safe, and a plan everyone in the house knows. In a Northern Utah winter, with furnaces, fireplaces and space heaters running for months, it&rsquo;s worth walking through every year.</p>
<p>We see the other side of this. Our crews handle fire, smoke and soot damage across Weber and Davis counties, and the water used to put a fire out often does as much damage as the flames. The best outcome is the one where we never get the call. Here&rsquo;s the checklist we&rsquo;d give our own families, built on guidance from the U.S. Fire Administration.</p>
<h2>1. Smoke alarms where they matter</h2>
<p>The <a href="{SA}" rel="noopener">U.S. Fire Administration</a> recommends smoke alarms inside and outside each bedroom and sleeping area, and on every level of the home, including the basement. Mount them on the ceiling or high on a wall, following the manufacturer&rsquo;s instructions.</p>
<p>If you&rsquo;re replacing alarms anyway, choose <b>interconnected</b> alarms, so when one sounds they all sound. In a two-story house or a home with a finished basement, that&rsquo;s the difference between hearing a fire that starts downstairs and sleeping through it.</p>
<h2>2. Test, change, replace</h2>
<ul><li><b>Test every alarm monthly.</b> Battery-powered and hardwired alarms both.</li><li><b>Batteries at least once a year.</b> For 9-volt alarms, and for the backup battery in hardwired alarms.</li><li><b>New alarms every 10 years.</b> Alarms don&rsquo;t last forever; the 10 years count from the manufacture date printed on the back.</li></ul>
<p>The reason it matters: the USFA notes that once an alarm sounds, you may have less than two minutes to get everyone outside. An alarm with a dead battery gives you none of that time.</p>
<h2>3. Give heat sources room</h2>
<p>Heating is a big part of the winter risk. According to the <a href="{HT}" rel="noopener">USFA&rsquo;s heating fire data</a>, heating fires were the second leading cause of home fires in 2021, with about 32,200 reported fires and an estimated 190 deaths. Portable heaters stand out: from 2017 to 2019 they were only about 3% of home heating fires but 41% of the fatal ones.</p>
<ul><li>Keep anything that can burn (blankets, curtains, furniture, laundry, boxes) at least <b>3 feet</b> from heat sources: space heaters, fireplaces, wood stoves, radiators and candles.</li><li>Turn space heaters off when you leave the room or go to bed.</li><li>Plug space heaters directly into the wall, and follow the manufacturer&rsquo;s instructions for the model you have.</li></ul>
<h2>4. Chimneys and heating equipment, once a year</h2>
<p>The USFA recommends having heating equipment and chimneys cleaned and inspected every year by a professional. Creosote builds up inside chimneys that see regular use, and a furnace that hasn&rsquo;t been looked at in years is a furnace nobody has checked. Early fall, before the first cold snap, is the easy time to schedule it.</p>
<p>If you burn wood, let ashes cool completely and store them in a metal container with a lid, outside and away from the house, not in a paper bag by the back door.</p>
<h2>5. Know your way out</h2>
<p>Walk through the house with everyone who lives there and agree on two ways out of each room where you can, and a meeting spot outside, in front of the house, where firefighters can see you. Practice it, including at night. Kids and anyone who needs help getting out should know exactly who is helping them.</p>
<p>Keep bedroom doors closed at night; a closed door slows smoke and heat. If there&rsquo;s smoke, stay low on the way out. Once you&rsquo;re out, stay out and call 911 from outside.</p>
<h2>6. Kitchens and everyday habits</h2>
<p>Most of fire safety is habits. Stay in the kitchen while you&rsquo;re frying or boiling. Keep a lid nearby to smother a pan fire. Don&rsquo;t overload outlets or run extension cords under rugs. Charge devices on hard surfaces, not on beds or couches. Blow out candles when you leave a room. None of it is complicated, and all of it is easy to let slide in a busy house.</p>
<h2>7. A walk-around before the first cold snap</h2>
<p>Pick a fall weekend and walk the house with this list in hand. Check the date on every smoke alarm and press the test button. Look at where the space heaters will live this winter and clear three feet around each spot. Book the chimney sweep and the furnace service if they&rsquo;re due. Clear the dryer lint screen and look behind the dryer, where lint collects. Move anything stored against the furnace or water heater. Then sit down with everyone in the house and walk the escape plan, so the first time anyone thinks about it isn&rsquo;t at 3 a.m.</p>
<h2>A five-minute checklist</h2>
<div class="checklist"><ol><li><span>Smoke alarm inside and outside every sleeping area, on every level</span></li><li><span>Every alarm tested this month</span></li><li><span>Batteries changed this year; alarms less than 10 years old</span></li><li><span>Three feet of clear space around every heater, stove and fireplace</span></li><li><span>Chimney and heating equipment inspected this year</span></li><li><span>Two ways out and a meeting spot everyone knows</span></li></ol></div>
<h2>If a fire does happen</h2>
<p>Get everyone out and let the fire department do its job. Once the house is cleared, call your insurance company, and call us at <a href="tel:{ST["tel"]}">{ST["phone"]}</a>, 24/7. Smoke and soot keep etching surfaces, and the water used to fight the fire starts its own damage within hours. We can <a href="@/services/boardup-services/">board up</a> openings, start <a href="@/services/fire-damage-restoration/">fire damage restoration</a> and <a href="@/services/odor-removal/">odor removal</a>, deal with the water, and then <a href="@/services/reconstruction/">rebuild</a> what was lost.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{SA}" rel="noopener">U.S. Fire Administration, Smoke alarms</a>; <a href="{HT}" rel="noopener">U.S. Fire Administration, Heating fire safety</a>.</p>'''
    pg = K.page(POST[1], "Home fire safety", POST[0], f"By {NAME} &middot; October 20, 2026", "Restoration tips", "Home Fire Safety Checklist for Utah Winters | Swift",
                "A home fire safety checklist for Northern Utah winters: smoke alarm placement and testing, space heater clearance, chimney inspections and an escape plan.",
                body, image="fire-kitchen-rebuilt", alt="Kitchen Swift rebuilt after a fire", crumbs=[("Restoration tips", "restoration-tips/")], ogtype="article")
    pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    pg["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                   "image": U + "assets/img/fire-kitchen-rebuilt.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    return pg
