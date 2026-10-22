"""New blog post for thedisasterrepairteam.com (/blog/...).
"Frozen Pipes in a Utah Winter: How to Prevent Them, Thaw Them, and What to Do When One Bursts"
Main phrase: "frozen pipes utah" (informational, seasonal). Their six posts cover insurance, cost, hidden water damage, spring
storms, spring water damage and what to do right after water damage; none covers freezing. It links to the water damage page,
the insurance post and the "what to do immediately" post without competing for "water damage restoration".
Facts and sources, checked 20 Oct 2026 (fetched and read):
- American Red Cross, "Preventing & Thawing Frozen Pipes" (https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-
  of-emergencies/winter-storm/frozen-pipes.html): water expands as it freezes and can break metal or plastic pipes; pipes that
  freeze most often (outdoor hose bibs, pool and sprinkler supply lines, pipes in unheated basements, crawl spaces, attics, garages,
  kitchen cabinets, pipes on exterior walls with little insulation); prevention (drain sprinkler lines, remove hoses, close inside
  valves to hose bibs and leave the outside bib open, insulate attics/basements/crawl spaces, pipe sleeves or UL-listed heat tape,
  keep garage doors closed, open cabinet doors, let cold water drip, keep the thermostat the same day and night, no lower than
  55°F when away); thawing (a trickle means suspect a frozen pipe, keep the faucet open, heat with a heating pad, hair dryer,
  space heater kept away from flammables or hot towels, never a blowtorch, kerosene or propane heater or open flame, call a
  licensed plumber if you can't find or reach it, check other faucets).
- EPA, "A Brief Guide to Mold, Moisture and Your Home": dry water-damaged areas within 24-48 hours to prevent mold growth.
- The client's own text: burst pipes and frozen-line failures are among common water emergencies; documentation for insurance;
  moisture travels under flooring, behind baseboards and into insulation; available 24/7.
No prices, no coverage promises."""
from engine import faq_html, faq_ld, canon
from cfg import U, NAME

POST = ("Frozen Pipes in a Utah Winter: Prevent Them, Thaw Them, and What to Do When One Bursts", "blog/frozen-pipes-utah-winter/")
RC = "https://www.redcross.org/get-help/how-to-prepare-for-emergencies/types-of-emergencies/winter-storm/frozen-pipes.html"
EPA = "https://www.epa.gov/mold/brief-guide-mold-moisture-and-your-home"
FAQ = [("What temperature should I leave the heat at when I travel in winter?", f'The <a href="{RC}" rel="noopener">American Red Cross</a> says to leave the heat on, set no lower than 55°F, if you will be away during cold weather.'),
       ("Should I let my faucets drip?", "When it is very cold, letting the cold water drip from a faucet served by exposed pipes helps: running water through the pipe, even at a trickle, helps prevent it from freezing."),
       ("Can I use a torch to thaw a frozen pipe?", "No. Use an electric heating pad, a hair dryer, a space heater kept away from anything flammable, or towels soaked in hot water. Never a blowtorch, kerosene or propane heater, or any open flame.")]


def post():
    return f'''<p class="answer">A frozen pipe is one of the most common ways a Utah winter turns into a water damage call. Water expands as it freezes, and that pressure can break a metal or plastic pipe. The break often isn&rsquo;t obvious until the ice thaws and water starts running into a wall, a ceiling or a basement. Here is how to prevent it, how to thaw a pipe safely, and what to do in the first hours if one bursts.</p>
<p>Burst pipes and frozen-line failures are among the emergencies we see most every winter across Northern Utah. Most of them start in the same few places, and most can be prevented with an hour of work in the fall.</p>
<h2>Which pipes freeze</h2>
<p>The <a href="{RC}" rel="noopener">American Red Cross</a> lists the pipes that freeze most often:</p>
<ul><li>Pipes exposed to severe cold: <b>outdoor hose bibs, swimming pool supply lines and sprinkler lines</b>.</li>
<li>Supply pipes in <b>unheated interior spaces</b>: basements, crawl spaces, attics, garages and kitchen cabinets.</li>
<li>Pipes that run along <b>exterior walls</b> with little or no insulation.</li></ul>
<p>In a lot of Utah homes that means the sprinkler system, the hose bib on the north side of the house, the line through the garage, and the kitchen sink on an outside wall.</p>
<h2>Before the first hard freeze</h2>
<ul><li><b>Sprinkler and pool lines.</b> Drain them following the manufacturer&rsquo;s or installer&rsquo;s directions. Don&rsquo;t put antifreeze in them unless you&rsquo;re told to.</li>
<li><b>Hoses and hose bibs.</b> Remove, drain and store hoses. Close the inside valve that feeds each outdoor hose bib, then open the outside bib to let it drain, and leave it open so any water left in the pipe has room to expand.</li>
<li><b>Insulation.</b> Add insulation to attics, basements and crawl spaces. Look in the garage and under kitchen and bathroom cabinets for supply lines in unheated areas, and insulate both hot and cold pipes there. Pipe sleeves, or UL-listed heat tape or heat cable, are made for this.</li>
<li><b>Know your main shutoff.</b> Find the main water shutoff before you need it, and make sure everyone in the house knows where it is. If a pipe bursts, it is the first thing you will want.</li></ul>
<h2>On the coldest nights</h2>
<ul><li>Keep the garage door closed if there are water lines in the garage.</li>
<li>Open kitchen and bathroom cabinet doors so warm air reaches the plumbing, and move cleaners out of children&rsquo;s reach while they are open.</li>
<li>Let the cold water drip from faucets served by exposed pipes. Even a trickle helps keep a pipe from freezing.</li>
<li>Keep the thermostat at the same temperature day and night. A higher heating bill for a few nights costs far less than a burst pipe.</li>
<li>If you will be away, leave the heat on, set no lower than 55°F. For a second home or a long trip, it is worth having someone check the house.</li></ul>
<h2>If a pipe freezes</h2>
<p>If you turn on a faucet and only a trickle comes out, suspect a frozen pipe. The Red Cross advice for thawing it:</p>
<ol><li><b>Keep the faucet open.</b> As the ice melts, running water helps melt the rest.</li>
<li><b>Apply gentle heat</b> to the frozen section: an electric heating pad, a hair dryer, a space heater kept well away from anything flammable, or towels soaked in hot water.</li>
<li><b>Never use an open flame.</b> No blowtorch, kerosene or propane heater, or charcoal stove.</li>
<li><b>Keep heating until full water pressure returns,</b> then check every other faucet in the house. If one pipe froze, others may have too.</li>
<li>If you can&rsquo;t find the frozen section, can&rsquo;t reach it, or can&rsquo;t thaw it, call a licensed plumber.</li></ol>
<h2>Signs a pipe has burst where you can&rsquo;t see it</h2>
<p>Not every break floods a floor. A pipe inside a wall or above a ceiling can leak for hours before anyone notices. Watch for:</p>
<ul><li>A ceiling that sags or bulges, or paint that bubbles. Water collects above the surface before it comes through; the photo at the top of this page is exactly that.</li>
<li>Stains spreading on drywall or along a baseboard, or flooring that lifts or feels soft.</li>
<li>Water pressure that drops at some faucets, or a water meter that keeps moving when nothing in the house is running.</li>
<li>The sound of running water in a wall after a cold night.</li></ul>
<p>Any of those after a freeze is a reason to shut off the water and get it looked at, because the damage you can see is usually only part of it.</p>
<h2>If a pipe bursts</h2>
<p>A burst usually shows itself when the pipe thaws. Act in this order:</p>
<ol><li><b>Shut off the water</b> at the main valve.</li>
<li><b>Stay safe around electricity.</b> If water is near outlets, appliances or the panel, don&rsquo;t walk into it; turn off power to the area only if you can do so safely.</li>
<li><b>Take photos and video</b> of the water, the pipe and anything damaged before you move things. It helps the insurance claim.</li>
<li><b>Move what you can</b> out of the water and get rugs and furniture off wet floors.</li>
<li><b>Call for help with the water.</b> What you can see is usually only part of it: water travels under flooring, behind baseboards and into insulation.</li></ol>
<p>Time matters because of mold. The <a href="{EPA}" rel="noopener">EPA</a> advises drying water-damaged areas and items within 24 to 48 hours to prevent mold growth, and a wall cavity or subfloor won&rsquo;t dry that fast on its own. That is why our <a href="@/water-damage-cleanup-restoration/">water damage</a> work includes moisture readings, not just extraction: the job isn&rsquo;t finished until the hidden moisture is gone.</p>
<h2>Insurance</h2>
<p>Whether a burst pipe is covered depends on your policy and the circumstances, so call your agent early. Good documentation helps: photos, moisture readings and a clear scope of what was affected. See <a href="@/blog/does-home-insurance-cover-water-damage-in-utah/">does insurance cover water damage in Utah</a> and <a href="@/blog/what-to-do-immediately-after-water-damage-in-your-utah-home/">what to do immediately after water damage</a>.</p>
<p>If a pipe has burst, call 385-287-6344 in Northern Utah or 435-619-9594 in St. George. We&rsquo;re available 24/7.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{RC}" rel="noopener">American Red Cross, &ldquo;Preventing &amp; Thawing Frozen Pipes&rdquo;</a>; <a href="{EPA}" rel="noopener">U.S. EPA, &ldquo;A Brief Guide to Mold, Moisture and Your Home&rdquo;</a>.</p>'''


def page(K):
    p = K.page(POST[1], "Frozen pipes", POST[0], f"From the {NAME} blog &middot; October 20, 2026", "Blog", "Frozen Pipes in Utah: Prevent, Thaw, Burst | Disaster Repair Team",
               "Frozen pipes in a Utah winter: which pipes freeze, how to prevent it, how to thaw a pipe safely, and the first steps when one bursts. Red Cross and EPA sources.",
               post(), image="drt-ceiling", alt="A ceiling bulging with water from a leak above", crumbs=[("Blog", "blog/")], ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/drt-ceiling.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    return p
