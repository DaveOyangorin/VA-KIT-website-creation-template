"""New blog post for foundationrepairogden.com (no blog on the live site; the post sits at /blog/...).
"Is Your Home Ready for an Earthquake? A Foundation-First Checklist for Ogden Homeowners"
Main phrase: "earthquake ready home ogden" (informational). No service page covers earthquakes (the client's own About page
mentions being prepared for water damage, floods "and even some earthquakes"); the post links to foundation inspection and repair
and the contact page without competing for them.
Facts and sources, fetched and read 20 Oct 2026:
- Ready.gov, "Earthquakes" (https://www.ready.gov/earthquakes): prepare before it happens; secure heavy items (bookcases,
  refrigerators, water heaters, televisions, objects on walls) and store heavy and breakable objects on low shelves; consider
  improvements to fix structural issues that could cause a building to collapse in an earthquake; a standard homeowner's policy
  does not cover earthquake damage; Drop, Cover, Hold On; stay inside and avoid doorways; expect aftershocks; serious hazards
  after a quake include building damage, leaking gas and water lines and downed power lines; don't enter damaged buildings.
- American Red Cross (also: deaths and injuries occur when people fall trying to walk or run during shaking or are hit by falling debris), "Earthquake Safety" (https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/earthquake.html):
  earthquakes can't be predicted; if you live in an area prone to earthquakes, get your building evaluated and consider structural
  improvements; earthquakes are generally not covered by household or renters' insurance; learn how to turn off utilities; go-kit
  of at least 3 days and stay-at-home kit of at least 2 weeks; sturdy shoes because glass is one of the most common injuries.
No fault statistics or probabilities (the USGS pages could not be reached to check). No prices."""
from engine import canon
from cfg import U, NAME

POST = ("Is Your Home Ready for an Earthquake? A Foundation-First Checklist for Ogden Homeowners", "blog/earthquake-ready-home-ogden/")
RG = "https://www.ready.gov/earthquakes"
RC = "https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/earthquake.html"
FAQ = [("Does homeowner&rsquo;s insurance cover earthquake damage?", f'Generally not. <a href="{RG}" rel="noopener">Ready.gov</a> says a standard homeowner&rsquo;s policy does not cover earthquake damage, and the <a href="{RC}" rel="noopener">Red Cross</a> says earthquakes are generally not covered by household or renters&rsquo; insurance. Separate earthquake policies exist; ask your insurer.'),
       ("Should I get my foundation looked at before an earthquake?", f'The <a href="{RC}" rel="noopener">Red Cross</a> advises people in earthquake-prone areas to get their building evaluated and consider structural improvements. Existing foundation cracks, bowed walls or uneven floors are worth having evaluated on their own merits.'),
       ("What should I check after an earthquake?", f'Safety first: <a href="{RG}" rel="noopener">Ready.gov</a> warns of building damage, leaking gas and water lines and downed power lines, and says not to enter damaged buildings. Once it&rsquo;s safe, look for new cracks, doors and windows that suddenly stick, and water where it wasn&rsquo;t before.')]


def post():
    return f'''<p class="answer">Earthquakes can&rsquo;t be predicted. That&rsquo;s the first thing both <a href="{RG}" rel="noopener">Ready.gov</a> and the <a href="{RC}" rel="noopener">American Red Cross</a> say, and it&rsquo;s why both put the work up front: what you do to a house before the ground moves matters more than anything you can do while it&rsquo;s moving. For a home in Ogden, that list starts with the structure itself and works outward to the things inside it.</p>
<p>We think about this from the bottom up, because the foundation is where a house meets the ground. As our own About page puts it, foundations have to stand up to water damage, floods and even some earthquakes; even though the region isn&rsquo;t famous for those, it&rsquo;s still best to be prepared. Here is a practical checklist, built on what the federal and Red Cross guidance actually says.</p>

<h2>1. Know the state of your foundation</h2>
<p>The <a href="{RC}" rel="noopener">Red Cross</a> is direct about this: if you live in an area prone to earthquakes, get your building evaluated and consider structural improvements. <a href="{RG}" rel="noopener">Ready.gov</a> says the same in different words: consider making improvements to your building to fix structural issues that could cause it to collapse during an earthquake.</p>
<p>For most homeowners, &ldquo;get your building evaluated&rdquo; starts with things you can see. Walk the basement and the outside of the house and note:</p>
<ul>
<li>Cracks in foundation or basement walls, and whether they&rsquo;re growing</li>
<li>Walls that bow inward or lean</li>
<li>Floors that slope, sag or have heaved</li>
<li>Doors and windows that stick or no longer latch</li>
<li>Water in the basement after rain or snowmelt</li>
</ul>
<p>None of these means a house will fail in an earthquake. They mean the foundation has already been moving or taking on water, which is worth knowing before anything shakes it. An on-site <a href="@/services/">foundation inspection</a> is the way to find out what they mean for your house.</p>

<h2>2. Fix what an evaluation finds</h2>
<p>Hard, compact clay swells when it gets wet, like a dry sponge, and that movement can heave floors and open cracks over the years. A foundation that is already cracked or out of level is a weaker starting point than one that isn&rsquo;t. Repairing cracks, stabilizing walls and dealing with water are good for the house every single day, and they&rsquo;re the kind of structural issues the guidance tells you to address.</p>
<p>Be wary of anyone who promises a particular repair makes a house &ldquo;earthquake proof&rdquo;. The honest version is simpler: a sound foundation is better than an unsound one, and the details depend on your house, which is why the evaluation comes first.</p>

<h2>3. Secure what can fall</h2>
<p>The <a href="{RC}" rel="noopener">Red Cross</a> notes that injuries happen when people fall trying to walk or run during shaking, or are hit by falling debris. <a href="{RG}" rel="noopener">Ready.gov</a> lists the usual suspects: bookcases, refrigerators, water heaters, televisions and objects that hang on walls. It recommends securing heavy items and storing heavy and breakable objects on low shelves.</p>
<p>The <a href="{RC}" rel="noopener">Red Cross</a> suggests a useful exercise: imagine the room picked up and shaken up and down and side to side, and ask what could fall and hurt someone. Straps, hooks, latches and other safety devices are widely available.</p>
<p>Pay special attention to the water heater: it&rsquo;s heavy, it&rsquo;s often in the basement, and it&rsquo;s connected to water and often gas.</p>

<h2>4. Learn your shut-offs</h2>
<p>After the shaking stops, <a href="{RG}" rel="noopener">Ready.gov</a> warns of serious hazards: damage to the building, leaking gas and water lines, and downed power lines. The <a href="{RC}" rel="noopener">Red Cross</a> recommends learning how to turn off the utilities in your home before you need to. Find the main water valve, the electrical panel and, if you have gas, the gas meter, and make sure more than one person in the house knows where they are.</p>

<h2>5. Check your insurance</h2>
<p>This one surprises people. <a href="{RG}" rel="noopener">Ready.gov</a> says a standard homeowner&rsquo;s insurance policy does not cover earthquake damage, and the <a href="{RC}" rel="noopener">Red Cross</a> says earthquakes are generally not covered by household or renters&rsquo; insurance. Earthquake policies may be available; ask your insurer what yours covers and what a separate policy would.</p>

<h2>6. Build your kits</h2>
<p>The <a href="{RC}" rel="noopener">Red Cross</a> recommends a go-kit with at least three days of supplies you can carry, and a stay-at-home kit with at least two weeks of supplies. It also suggests keeping sturdy shoes by the bed, since glass is one of the most common earthquake injuries, along with a flashlight, glasses, a dust mask and a whistle. <a href="{RG}" rel="noopener">Ready.gov</a> adds a family communications plan with an out-of-state contact and a place to meet if you get separated.</p>

<h2>7. Practice Drop, Cover and Hold On</h2>
<p>Both sources teach the same three steps. <strong>Drop</strong> onto your hands and knees. <strong>Cover</strong> your head and neck, under a sturdy table or desk if one is close, or next to an interior wall away from windows. <strong>Hold on</strong> until the shaking stops. <a href="{RG}" rel="noopener">Ready.gov</a> adds: if you&rsquo;re inside, stay inside and don&rsquo;t run outside, and avoid doorways. Expect aftershocks, and be ready to do it again.</p>

<h2>After the shaking: what to look for</h2>
<p>Once everyone is safe, and only once it&rsquo;s safe, walk the house again with the same list from step 1. Don&rsquo;t enter a building that looks damaged; <a href="{RG}" rel="noopener">Ready.gov</a> is clear on that. Things worth noting afterward:</p>
<ul>
<li>New cracks, or old ones that have widened</li>
<li>Doors and windows that suddenly stick</li>
<li>Water on the basement floor that wasn&rsquo;t there before</li>
<li>Gaps where floors meet walls</li>
</ul>
<p>Photograph them with something for scale. If something has changed, have the foundation looked at. Call (385) 213-2324, any day from 7 a.m. to 11 p.m., or <a href="@/contact/">send the form</a> for a free estimate.</p>

<div class="sources"><h3>Sources</h3><ul>
<li>Ready.gov (U.S. Department of Homeland Security), <a href="{RG}" rel="noopener">Earthquakes</a></li>
<li>American Red Cross, <a href="{RC}" rel="noopener">Earthquake Safety</a></li>
</ul><p>This article is general information. For emergencies, call 911.</p></div>'''


def page(K):
    p = POST[1]
    schema = [{"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
               "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p)}]
    import home_o
    return K.page(p, "Earthquake-ready home", POST[0], "Published 20 October 2026 &middot; Sources: Ready.gov, American Red Cross", "Blog",
                  "Earthquake-Ready Home Checklist for Ogden, UT | Fortified Foundations",
                  "How to get an Ogden home ready for an earthquake, foundation first: evaluate and fix structural issues, secure heavy items, utilities, insurance and kits.",
                  post() + f'<p class="v-credit">{home_o.CREDIT}</p>', image="og-canyon-tall", alt="Ogden Canyon in a photograph from the 1870s (U.S. National Archives)", faqs=FAQ, schema=schema, ogtype="article")
