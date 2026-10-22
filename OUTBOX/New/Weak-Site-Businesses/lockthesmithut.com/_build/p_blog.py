"""New blog post for lockthesmithut.com (21 Oct 2026): children and pets locked in hot cars. Public-safety content; it doesn't target
car lockout or key keywords. Sources: NoHeatStroke.org (Jan Null, CCM, San Jose State University; data updated 28 Sep 2026); NHTSA and
Kids and Car Safety guidance as reported by ABC7 (18 Jun 2024)."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/hot-car-safety-utah/"
H1 = "Hot cars and locked doors: what every Utah driver should know"
FAQ = [("A child is locked in a hot car. Should I call a locksmith or 911?", "Call 911 first, right away. Emergency responders can get inside faster than anyone else, and they bring medical help. Don&rsquo;t wait for a locksmith or a spare key when a child is alone in a hot car."),
       ("How hot does a car get inside?", "NHTSA says a car&rsquo;s interior can climb past 100&deg;F even when it&rsquo;s only in the 70s outside, and most of the rise happens in the first 10 minutes. Cracking the windows or parking in shade does little to change that."),
       ("How many children die in hot cars?", "According to NoHeatStroke.org, 1,070 U.S. children have died of vehicular heatstroke since 1998, an average of 37 a year. Two of the 2026 cases were in Utah: American Fork and Vernal, both in late July."),
       ("How do kids get trapped in cars?", "Safety groups describe two common ways: a caregiver forgets a child in the back seat, or a child climbs into an unlocked car and can&rsquo;t get out. That&rsquo;s why safety groups say to keep cars locked all the time, with keys out of reach.")]
BODY = f'''<p class="answer">If a child or pet is locked in a hot car, call 911 immediately. Don&rsquo;t wait for a locksmith. A car can pass 100&deg;F inside on a 70-degree day, and children overheat fast. To prevent it, check the back seat every time, keep your car locked, and keep keys and remotes out of kids&rsquo; reach.</p>

<p>Keys locked in the car are usually just an inconvenience. But when a child or a pet is inside, it&rsquo;s an emergency that can turn deadly in minutes, and the right first call isn&rsquo;t to us. This guide covers what happens inside a hot car, what to do in the first minutes, and the simple habits that prevent it.</p>

<h2>How fast a car becomes dangerous</h2>
<p>The National Highway Traffic Safety Administration (NHTSA) warns that temperatures inside a car can climb to over 100&deg;F even when it&rsquo;s only in the 70s outdoors. Most of the increase happens in the first ten minutes. NHTSA also notes that rolling the windows down or parking in the shade does little to change the interior temperature.</p>
<p>Children are far more vulnerable than adults. According to NHTSA, heatstroke can begin when a body&rsquo;s temperature reaches 104&deg;F, and a child can die when their internal temperature reaches 107&deg;F, the point where the body can no longer regulate its own heat. Utah&rsquo;s summers regularly bring afternoons in the 90s and above, with intense high-altitude sun.</p>

<h2>The numbers</h2>
<p>Jan Null, a meteorologist at San Jose State University, tracks every U.S. child death from vehicular heatstroke at NoHeatStroke.org. As of late September 2026, <strong>1,070 children</strong> have died in hot cars since 1998, an <strong>average of 37 a year</strong>. Twenty-five children died in 2026 alone, and two of them were in Utah: a 4-year-old girl in American Fork on a 100-degree day, and a 7-month-old girl in Vernal on a 94-degree day, both in late July.</p>
<p>These deaths happen to careful, loving families. Safety guidance focuses on two ways it happens: a child is forgotten in the back seat, or a child climbs into an unlocked car to play and can&rsquo;t get out.</p>

<h2>If you see a child or pet alone in a hot car</h2>
<ol>
<li><strong>Call 911 immediately.</strong> This is the most important step. Dispatchers can send police and fire crews, who can get into the car fastest and bring medical help.</li>
<li><strong>Stay with the car</strong> and keep watching the child or animal. Tell the dispatcher how they look and whether they&rsquo;re responding.</li>
<li><strong>Follow the dispatcher&rsquo;s instructions.</strong> If the child is in distress, they may tell you how to get them out.</li>
<li><strong>Once the child is out,</strong> get them into shade or air conditioning and cool them quickly, as ABC7 reported from NHTSA and Kids and Car Safety guidance, while help is on the way.</li>
</ol>
<p>A locksmith is the right call when no one is in danger: the keys are on the seat, the engine is off and everyone is safely outside. If anyone is inside on a warm day, call 911 first.</p>

<h2>Habits that prevent it</h2>
<h3>Look before you lock</h3>
<p>Check the back seat every time you get out of the car, even on a short errand. Safety groups suggest putting something you can&rsquo;t leave without (a phone, a bag, your employee badge, even your left shoe) in the back seat next to the child. Some parents put a stuffed animal in the car seat when it&rsquo;s empty, then move it to the front seat when the child is buckled in, as a visual reminder.</p>

<h3>Keep your car locked, all the time</h3>
<p>Kids and Car Safety&rsquo;s advice is to keep cars locked 100% of the time, even if you don&rsquo;t have kids, and to keep keys and remote fobs out of children&rsquo;s reach. Teach children that a car is not a play area. If a child goes missing, check the floorboards and trunks of nearby vehicles right away, even locked ones.</p>

<h3>Ask for a call</h3>
<p>Ask your child care provider or school to call you if your child doesn&rsquo;t arrive as scheduled. It&rsquo;s one of the simplest backstops there is.</p>

<h3>Pets count too</h3>
<p>The same heat applies to dogs, which cool themselves mainly by panting. A &ldquo;quick&rdquo; stop with the dog in the car can turn dangerous on a warm Utah afternoon. If you can&rsquo;t take your pet inside with you, leave it at home.</p>

<h2>When it&rsquo;s just your keys</h2>
<p>Locking your keys in the car with no one inside is stressful but not dangerous. Stay in the shade, don&rsquo;t try to force a window or door, and call a locksmith. Lockthesmith&rsquo;s mobile service runs seven days a week, 8 AM to 8 PM, across Salt Lake, Davis, Utah, Weber and Summit counties: <a href="tel:+18014624094">801-462-4094</a>.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<div class="sources"><p class="label">Sources</p><ul>
<li>Jan Null, CCM, Department of Meteorology &amp; Climate Science, San Jose State University, <a href="https://www.noheatstroke.org/" rel="noopener">NoHeatStroke.org: Pediatric Vehicular Heatstroke</a> (updated September 28, 2026)</li>
<li>ABC7, <a href="https://abc7.com/post/sweltering-heat-approaches-experts-share-hot-car-safety/14970828/" rel="noopener">&ldquo;As sweltering heat approaches, experts share hot car safety tips&rdquo;</a> (June 18, 2024), citing NHTSA and Kids and Car Safety</li>
<li>National Highway Traffic Safety Administration, <a href="https://www.nhtsa.gov/campaign/heatstroke" rel="noopener">Heatstroke campaign</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Hot car safety", H1, "Safety &middot; Oct 21, 2026", "Blog", "Hot Car Safety in Utah: Kids &amp; Locked Doors | Lockthesmith",
                  "A car can pass 100&deg;F inside on a 70-degree day. What to do if a child or pet is locked in a hot car (call 911 first) and the habits that prevent it.",
                  BODY, art=None, crumbs=[], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "Lockthesmith"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
