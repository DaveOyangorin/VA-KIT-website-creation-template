"""New blog post for acs-hoa.com (21 Oct 2026): a winter checklist for HOA boards. It doesn't target "hoa management lehi" or other
service keywords. Sources: Ready.gov "Winter Weather"; American Red Cross frozen-pipe guidance (as reported by WRFA-LP). ACS's own
services for the HOA-specific steps."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/hoa-winter-checklist-utah/"
H1 = "The HOA board&rsquo;s winter checklist for Utah communities"
FAQ = [("When should an HOA blow out its sprinkler system?", "Before the first hard freeze. The Red Cross lists sprinkler supply lines among the pipes most likely to freeze, and recommends draining sprinkler systems before winter. For a common-area system, schedule it with your landscape vendor in the fall."),
       ("Who handles snow removal in an HOA?", "It depends on your governing documents. Many associations contract snow removal for common areas, private roads and walkways. Check your CC&amp;Rs, and get the contract in place before the first storm."),
       ("How should we tell owners about a water shutoff?", "Directly and early. A broadcast email or text to all owners, plus a calendar and website notice, reaches people far better than a notice on a mailbox."),
       ("What should owners do if they leave for the winter?", "The Red Cross advises leaving the heat on, set no lower than 55&deg;F, when you&rsquo;ll be away in cold weather. Owners should also tell the HOA how to reach them, and who has a key, in case of a leak.")]
BODY = f'''<p class="answer">Before winter, an HOA board should blow out common-area sprinklers, lock in a snow removal contract, check exterior lighting and walkways, remind owners how to prevent frozen pipes, and make sure there&rsquo;s a fast way to reach every owner about shutoffs and storms.</p>

<p>Winter in Utah is hard on shared property. Sprinkler lines crack, walkways ice over, roofs carry heavy snow, and a single frozen pipe in one unit can flood the one below. Most of these problems are predictable, which means most are preventable with a little planning in October and November. Here&rsquo;s a checklist for HOA boards, built on emergency-preparedness guidance from Ready.gov and the American Red Cross.</p>

<h2>1. Shut down and blow out irrigation</h2>
<p>According to the American Red Cross, the pipes most likely to freeze include outdoor hose bibs, swimming pool supply lines and <strong>water sprinkler lines</strong>, along with pipes in unheated spaces and pipes running along exterior walls. Red Cross guidance is to drain sprinkler systems and outdoor hoses before winter.</p>
<p>For an HOA, that means scheduling the common-area irrigation blowout with your landscape contractor before the first hard freeze, and confirming it&rsquo;s done. If owners maintain their own yard systems, send a reminder with a date.</p>

<h2>2. Get the snow removal contract in writing</h2>
<p>Check your governing documents to confirm what the association is responsible for: private roads, common walkways, mailbox areas, clubhouse entrances. Then make sure the contract spells out:</p>
<ul>
<li>The snowfall depth that triggers service</li>
<li>Which areas get cleared, and in what order</li>
<li>Whether walkways get ice melt, and how often</li>
<li>Response times after a storm ends</li>
<li>Who the board or manager calls when something&rsquo;s missed</li>
</ul>
<p>Getting quotes in late summer or early fall gives you time to compare. ACS provides custom quotes for snow removal, lawn care and sprinkler maintenance for the communities it manages.</p>

<h2>3. Walk the property before the snow flies</h2>
<p>A fall inspection catches problems while they&rsquo;re still cheap to fix. Look for:</p>
<ul>
<li>Exterior lighting that&rsquo;s out along walkways and parking areas</li>
<li>Trip hazards: lifted sidewalk panels and broken steps that become dangerous under snow</li>
<li>Gutters and downspouts clogged with leaves, which can lead to ice buildup</li>
<li>Exposed pipes in unheated common areas such as garages, crawl spaces and clubhouse utility rooms</li>
<li>Tree limbs hanging over roofs, walkways or parking that heavy snow could bring down</li>
</ul>

<h2>4. Remind owners how to prevent frozen pipes</h2>
<p>In condos and townhomes, one owner&rsquo;s frozen pipe can become several owners&rsquo; insurance claim. Send owners the Red Cross&rsquo;s basic advice before the first cold snap:</p>
<ul>
<li>Keep garage doors closed if there are water supply lines in the garage.</li>
<li>Open kitchen and bathroom cabinet doors so warmer air can circulate around the plumbing.</li>
<li>On very cold nights, let cold water drip from faucets served by exposed pipes. Running water, even at a trickle, helps keep pipes from freezing.</li>
<li>Keep the thermostat at the same temperature day and night.</li>
<li>If you&rsquo;ll be away, leave the heat on, set no lower than 55&deg;F.</li>
</ul>
<p>The Red Cross also warns never to thaw a frozen pipe with an open flame.</p>

<h2>5. Plan how you&rsquo;ll reach every owner, fast</h2>
<p>Winter brings messages owners need right away: a water shutoff for a repair, a power outage, a parking ban for plowing, an icy-walkway warning. A notice on a door or mailbox isn&rsquo;t enough. Make sure the association has current email addresses and phone numbers for every owner and a way to broadcast to all of them at once. ACS&rsquo;s communication tools include broadcasts for power outages, water shutoffs and other urgent news, alongside a community calendar and newsletters.</p>

<h2>6. Share basic winter-safety reminders</h2>
<p>A short note in the fall newsletter helps owners and residents stay safe. Ready.gov&rsquo;s winter guidance includes:</p>
<ul>
<li>Prepare homes to keep out the cold with insulation, caulking and weather stripping.</li>
<li>Install and test smoke alarms and carbon monoxide detectors with battery backups.</li>
<li>Use generators and fuel only outdoors, at least 20 feet from windows, doors and attached garages.</li>
<li>Gather supplies in case you need to stay home for several days without power.</li>
<li>Know the signs of frostbite (numbness; white or grayish-yellow skin; firm or waxy skin) and hypothermia (shivering, exhaustion, confusion, fumbling hands, memory loss, slurred speech or drowsiness). A body temperature below 95&deg;F is an emergency.</li>
</ul>

<h2>7. Review the reserves before the bills come</h2>
<p>Winter is when deferred maintenance shows up: an old boiler gives out, a roof leaks under snow load, a parking lot heaves. A board that knows what&rsquo;s coming can plan for it. ACS begins work with a community with a reserve analysis that makes clear the maintenance and growth issues to plan for now, and presents a transparent financial report at each board meeting.</p>

<h2>A one-page version for your next meeting</h2>
<ol>
<li>Common-area sprinklers blown out (date: ____ )</li>
<li>Snow removal contract signed, with triggers and areas listed</li>
<li>Fall walk-through done: lights, trip hazards, gutters, exposed pipes, trees</li>
<li>Frozen-pipe reminder sent to owners</li>
<li>Owner contact list current, and broadcast tested</li>
<li>Winter-safety note in the newsletter</li>
<li>Reserve items reviewed for winter risk</li>
</ol>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Want help running the checklist? ACS manages HOAs across Utah, Washington, Idaho and Arizona. <a href="@/request-a-quote.html">Request a bid</a> or call <a href="tel:+18778444227">1-877-844-4227</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Ready.gov (U.S. Department of Homeland Security), <a href="https://www.ready.gov/winter-weather" rel="noopener">Winter Weather</a></li>
<li>American Red Cross frozen-pipe guidance, as reported in <a href="https://www.wrfalp.com/red-cross-offers-tips-to-prevent-pipes-from-freezing-in-subzero-temps" rel="noopener">&ldquo;Red Cross offers tips to prevent pipes from freezing in subzero temps&rdquo;</a> (WRFA-LP)</li>
<li>Advanced Community Services, <a href="@/management-services.html">Management</a>, <a href="@/online-services.html">Online</a> and <a href="@/professional-services.html">Professional</a> services</li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "HOA winter checklist", H1, "For boards &middot; Oct 21, 2026", "Blog", "Winter Checklist for Utah HOA Boards | ACS HOA Management",
                  "A winter checklist for Utah HOA boards: sprinkler blowouts, snow contracts, fall walk-throughs, frozen-pipe reminders, owner broadcasts and reserve reviews.",
                  BODY, crumbs=[], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "The HOA board's winter checklist for Utah communities", "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "Advanced Community Services"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
