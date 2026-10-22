"""Blog for cleartopsolutions.shop (the live site has none): a blog index and one new post.

"Summer Storm Season in St. George: How to Get Your Home Ready for Monsoon Water"
Main phrase: "monsoon season st george home" / storm-season preparation (informational). None of the 20 service pages targets
preparation or insurance timing; the post links to basement flood cleanup, water extraction, mold remediation and leak pages
without competing for their keywords.
Facts and sources, checked 20 Oct 2026 (fetched):
- Ready.gov, "Floods" (https://www.ready.gov/floods): homeowner's insurance policies do not cover flooding; it typically takes up
  to 30 days for a flood policy to go into effect; get coverage under the NFIP; where it rains it can flood (flooding doesn't follow
  lines on a map); FEMA's Flood Map Service Center; declutter drains and gutters, install check valves, consider a sump pump with a
  battery, move valuables to higher levels, keep documents in a waterproof container with password-protected digital copies;
  after: wear gloves, boots, masks when cleaning mold; people with asthma/lung conditions/immune suppression should not enter
  buildings with visible or smelled mold; children should not take part in cleanup; don't touch wet electrical equipment; turn
  off electricity if safe; floodwater can be contaminated.
- National Weather Service, "Turn Around Don't Drown" (https://www.weather.gov/safety/flood-turn-around-dont-drown): 6 inches of
  fast-moving flood water can knock over an adult; 12 inches can carry away most cars; 2 feet can carry away SUVs and trucks.
- EPA, "A Brief Guide to Mold, Moisture and Your Home" (https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home): dry
  water-damaged areas and items within 24-48 hours to prevent mold growth; moldy areas under about 10 sq ft can usually be
  handled yourself, larger areas or a lot of water damage call for professional guidance.
- The client's own text: monsoon season leaks and flooding affect outdoor living spaces; rainfall is infrequent but significant
  when it comes; red rock and desert terrain.
No monsoon start/end dates (no official source reached); no prices."""
from engine import faq_html, faq_ld, canon, img
from cfg import U, NAME, ST

POST = ("Summer Storm Season in St. George: How to Get Your Home Ready for Monsoon Water", "blog/monsoon-season-st-george-home-prep/")
READY = "https://www.ready.gov/floods"
NWS = "https://www.weather.gov/safety/flood-turn-around-dont-drown"
EPA = "https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home"
FAQ = [("Does homeowners insurance cover monsoon flooding?", f'According to <a href="{READY}" rel="noopener">Ready.gov</a>, homeowner&rsquo;s insurance policies do not cover flooding. Flood coverage is a separate policy, for example through the National Flood Insurance Program, and it typically takes up to 30 days to go into effect. A leak from a pipe or appliance inside the house is a different situation from flood water coming in from outside, so check your own policy with your agent.'),
       ("How fast does mold start after a storm leak?", f'The <a href="{EPA}" rel="noopener">EPA</a> advises drying water-damaged areas and items within 24 to 48 hours to prevent mold growth. That&rsquo;s the clock that matters after a storm.'),
       ("Can I clean up a small leak myself?", "Often, yes: stop the water, dry the area fast, and keep an eye on it. The EPA says mold patches under about 10 square feet can usually be handled yourself. If there was a lot of water, it came from outside or a sewer line, or it has soaked into walls, floors or the ceiling, get it assessed.")]


def post():
    return f'''<p class="answer">In St. George, rain is rare, and that&rsquo;s exactly why late-summer storms catch houses out. When a monsoon thunderstorm does arrive, a lot of water lands at once on hard desert ground, roofs and patios that spend most of the year bone-dry. Here&rsquo;s how to get your home ready before the storms, what to do while one is overhead, and what to do in the hours after.</p>
<p>We restore water-damaged homes across St. George, Washington, Santa Clara and Ivins, and storm season brings a particular kind of call: water through a roof or a window that has never leaked before, runoff across a patio and under a door, a backed-up drain, a basement or crawl space taking on water. Most of it is preventable, and most of the rest gets much smaller if it&rsquo;s dealt with fast.</p>
<h2>Why storms hit desert homes hard</h2>
<p>Three things work against a house here. First, the ground: hard, dry soil and rock don&rsquo;t soak up a sudden downpour, so water runs off fast and goes wherever the grade sends it, including toward your foundation. Second, the house itself: roof seals, window seals and drains that sit dry for months crack, shrink or fill with debris, and nobody notices until the first heavy rain. Third, the lifestyle: outdoor living spaces, patios and pool decks are built to shed water in a light shower, not a cloudburst.</p>
<p>And flooding doesn&rsquo;t only happen in flood zones. As <a href="{READY}" rel="noopener">Ready.gov</a> puts it, flooding doesn&rsquo;t follow lines on a map: where it rains, it can flood. You can check the official flood risk for your address on FEMA&rsquo;s Flood Map Service Center, but treat it as a starting point, not a guarantee.</p>
<h2>Before storm season: a walk-around checklist</h2>
<p>Pick a dry morning and walk the property with these in mind. Most of the list is free or cheap.</p>
<ul><li><b>Gutters, downspouts and roof drains.</b> Clear them out. Ready.gov&rsquo;s flood checklist starts with decluttering drains and gutters. Make sure downspouts discharge well away from the foundation, not against it.</li>
<li><b>The grade around the house.</b> Soil, rock and pavers should slope away from the walls. Low spots by the foundation are where runoff collects and finds a way in.</li>
<li><b>Patio and yard drains.</b> Pour a bucket of water into each one. If it doesn&rsquo;t drain freely, it won&rsquo;t cope with a storm.</li>
<li><b>Roof and window seals.</b> Look for cracked caulk around windows, doors and roof penetrations. Sun and heat age seals fast here.</li>
<li><b>Basement and crawl space.</b> If you have one, look for old water stains and check vents and window wells. Ready.gov suggests considering a sump pump with a battery backup, and check valves to stop sewer lines backing up into the house.</li>
<li><b>Valuables and documents.</b> Move anything precious off basement floors to higher levels, and keep important documents in a waterproof container with password-protected digital copies.</li></ul>
<h2>Check your insurance before you need it</h2>
<p>This is the step people skip, and it&rsquo;s the one with a deadline. According to Ready.gov, homeowner&rsquo;s insurance policies do not cover flooding, and a flood policy typically takes up to 30 days to go into effect. If you want flood coverage for storm season, the time to buy it is well before the first storm, not when one is on the forecast.</p>
<p>It&rsquo;s also worth knowing how your policy treats different kinds of water: a leak from a supply line or a failed appliance, water through a damaged roof, and flood water from outside are often handled very differently. A ten-minute call to your agent now saves a lot of confusion later. When a claim does happen, we help with documentation and communication with your insurance provider.</p>
<h2>While a storm is overhead</h2>
<ul><li><b>Stay out of moving water.</b> The <a href="{NWS}" rel="noopener">National Weather Service</a> warns that just 6 inches of fast-moving flood water can knock over an adult, 12 inches can carry away most cars, and 2 feet can carry away SUVs and trucks. Washes and low crossings around St. George can go from dry to dangerous fast.</li>
<li><b>Don&rsquo;t mix water and electricity.</b> If water is coming in near outlets or appliances, turn off power to the affected area if it&rsquo;s safe to do so, and don&rsquo;t touch electrical equipment while it&rsquo;s wet or you&rsquo;re standing in water.</li>
<li><b>Slow the water if you safely can.</b> Towels at a door, a bucket under a drip, moving furniture and rugs off a wet floor. Take photos and video as you go: they help with the claim later.</li></ul>
<h2>After the storm: the first 48 hours</h2>
<p>Once the rain stops, the clock starts. The <a href="{EPA}" rel="noopener">EPA</a> advises drying water-damaged areas and items within 24 to 48 hours to prevent mold growth. Water that soaks into drywall, under flooring or into cabinets keeps doing damage after the storm has passed.</p>
<ol><li><b>Find where it came in.</b> Roof, window, door, drain, or up from below. Fixing the entry point comes first, or the next storm repeats the job.</li>
<li><b>Get standing water out.</b> Small amounts can be mopped and vacuumed with a wet-vac. Larger amounts need <a href="@/services/water-extraction/">water extraction</a> with pumps and commercial vacuums.</li>
<li><b>Dry it properly.</b> Fans and open windows help with a small spill. Soaked walls, floors and ceilings need drying equipment and dehumidifiers, and moisture checks to confirm they&rsquo;re actually dry, not just dry on the surface.</li>
<li><b>Treat outside water with caution.</b> Ready.gov notes floodwater can be contaminated and carry dangerous debris. Wear heavy gloves, boots and protective clothing for cleanup, and a mask around mold. People with asthma, other lung conditions or a weakened immune system should not enter buildings with indoor water leaks or mold they can see or smell, and children should not take part in cleanup.</li></ol>
<h2>When to call a professional</h2>
<p>The EPA&rsquo;s rule of thumb for mold is a useful one for water too: a patch under about 10 square feet is usually something you can handle yourself, while a lot of water damage or a larger area calls for professional help. Call if water has reached a <a href="@/services/basement-flood-cleanup/">basement</a> or crawl space, if a <a href="@/services/ceiling-water-damage-repair/">ceiling</a> is sagging or stained, if the water came from a sewer line or from outside, or if you can smell mustiness days later (see <a href="@/services/mold-remediation-after-water-damage/">mold remediation after water damage</a>).</p>
<p>Our 24/7 emergency line is <a href="tel:{ST["tel"]}">{ST["phone"]}</a>. We assess on site, explain what&rsquo;s needed in plain language, and give you an upfront estimate before work begins.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{READY}" rel="noopener">Ready.gov, &ldquo;Floods&rdquo;</a>; <a href="{NWS}" rel="noopener">National Weather Service, &ldquo;Turn Around Don&rsquo;t Drown&rdquo;</a>; <a href="{EPA}" rel="noopener">U.S. EPA, &ldquo;A Brief Guide to Mold, Moisture and Your Home&rdquo;</a>. Insurance terms vary by policy: confirm your coverage with your agent.</p>'''


def pages(K):
    p = K.page(POST[1], "Monsoon prep", POST[0], f"By {NAME} &middot; October 20, 2026", "Blog", "Monsoon Season Home Prep in St. George, UT | ClearTop",
               "Getting a St. George home ready for monsoon storms: a walk-around checklist, flood insurance timing, storm safety, and the first 48 hours after water gets in.",
               post() + '<p class="credits">Photo: &ldquo;<a href="https://www.flickr.com/photos/189326381@N08/52379397605" rel="noopener">Thanks For The Shot Pops!</a>&rdquo; by A Guy Named Nyal (<a href="https://creativecommons.org/licenses/by-sa/2.0/" rel="noopener">CC BY-SA 2.0</a>), for atmosphere only.</p>',
               image="night-lightning", alt="Lightning over a desert town at night", crumbs=[("Blog", "blog/")], ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/night-lightning.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    idx = K.page("blog/", "Blog", "Water Damage Blog", "Plain-English notes on water, storms and mold in St. George homes.", "Blog", "Water Damage Blog | ClearTop Solutions, St. George UT",
                 "Notes from ClearTop Solutions on water damage in St. George homes: storm season prep, insurance timing, drying, mold, and when to call for help.",
                 f'<div class="posts one"><a class="post-card" href="@/{POST[1]}">{img("night-lightning", "")}<span class="pc-d">Oct 20, 2026</span><b>{POST[0]}</b><em>Read {K.ARROW}</em></a></div>')
    return [idx, p]
