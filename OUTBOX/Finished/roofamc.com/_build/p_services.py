from build import (SITE, ARROW, PHONE, img, cta_band, side, page_hero, faq_html, faq_schema,
                   crumbs_schema, service_schema)

NDSU = "https://www.ag.ndsu.edu/news/newsreleases/2023/january/reduce-ice-dam-and-icicle-damage"
UOU = "https://www.inscc.utah.edu/~steenburgh/utah_climo/snowstorms.html"
DOE = "https://www.energy.gov/sites/prod/files/guide_to_cool_roofs.pdf"
BLOG = "blog/how-long-do-roofs-last-in-utah/"


def layout(article, links):
    return f'<section class="sec"><div class="wrap layout"><article class="prose">{article}</article>{side(links)}</div></section>'


# --------------------------------------------------------------------------- roof repair
REPAIR_FAQ = [
    ("How can I fix cracks in my roof?",
     "Small cracks in a shingle or around flashing can often be sealed or the single shingle replaced. Cracks across many shingles usually mean the roof is drying out and aging. Have a roofer look first: a crack you can see from the ground is often a sign of more damage up close."),
    ("What does roof repair mean?",
     "Roof repair means fixing part of a roof instead of replacing all of it: a leak, a few missing or broken shingles, failed flashing, a torn spot in a flat roof membrane, or a damaged gutter. If the roof is sound overall, a repair is usually the smarter spend."),
    ("How fast can you come out for a roof leak?",
     f"We know a leak can't wait, so we respond quickly. Call {SITE['phone']} during business hours, Monday to Saturday from 9 to 5. If water is coming in right now, call our emergency line at {SITE['emerg']} and we'll help you limit the damage."),
    ("Do you repair commercial flat roofs?",
     "Yes. We repair flat and low-slope commercial roofs as well as pitched roofs, and we can set up a maintenance program so small problems get caught before they reach tenant spaces, inventory or equipment. See our commercial roofing page for more on how we work with property owners."),
    ("Should I repair or replace an old roof?",
     "Repair makes sense when the damage is in one area and the rest of the roof is in good shape. If leaks keep showing up in new places, shingles are curling everywhere, or the deck feels soft, replacement is usually cheaper over time. We'll tell you which one we'd pick."),
    ("Is the roof repair estimate free?",
     f"Yes. We'll look at the roof and give you a free estimate. Call {SITE['phone']} or send the quote form with a short description and, if you can, a photo of the problem area."),
]

REPAIR_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control does roof repair in Salt Lake City for homes and commercial buildings: leaks, missing or broken shingles, storm and tree damage, flashing, gutters and drainage. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> for a free estimate, or <a href="tel:{SITE["emerg_tel"]}">{SITE["emerg"]}</a> if water is coming in now.</div>

<p>Roof repairs cover a lot of ground. It can be anything from a slow leak over the kitchen to a broken gutter that dumps snowmelt against the foundation. We're fully licensed, insured and certified to repair both residential and commercial roofs, and our crew carries the tools, equipment and materials to handle the job on the first trip.</p>
<p>A simple leak can turn into a major problem if it isn't handled quickly. Water soaks the deck, then the insulation, then the drywall. So we move fast, and we fix the cause rather than smearing tar over the symptom.</p>

<h2>Roof repairs we handle in Salt Lake City</h2>
<p>Here's what most calls turn out to be. If you don't see your problem, call anyway. Chances are we've fixed it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Repair</th><th>What it usually looks like</th></tr></thead>
<tbody>
<tr><td>Shingle replacement</td><td>Shingles missing after wind, cracked, curled or torn at the tabs</td></tr>
<tr><td>Roof leaks</td><td>Ceiling stains, drips in the attic, wet insulation, peeling paint near the ceiling</td></tr>
<tr><td>Storm and tree damage</td><td>Branches on the roof, dented flashing, punctures, lifted edges</td></tr>
<tr><td>Roof patching</td><td>A damaged area on an otherwise healthy roof, shingle or flat</td></tr>
<tr><td>Roof inspections</td><td>Buying or selling a home, after a big storm, or before winter</td></tr>
<tr><td>Waterproofing</td><td>Recurring leaks on low-slope roofs, balconies and transitions</td></tr>
<tr><td>Gutter repairs</td><td>Sagging runs, leaking seams, downspouts pulling away</td></tr>
<tr><td>Drainage solutions</td><td>Ponding water on flat roofs, ice building up at the eaves</td></tr>
</tbody></table></div>

<figure>{img("rain-dripping-shingle-edge", "Rainwater running off the edge of a dark shingle roof")}<figcaption>Water should leave the roof at the edge, fast. When it doesn't, it finds a way in.</figcaption></figure>

<h2>Roof leak repair: find the source, not the stain</h2>
<p>Water rarely comes through the ceiling right under the hole. It lands on the deck, runs along a rafter or the top of the insulation, and shows up several feet away. That's why patching the spot above the stain so often fails.</p>
<p>On Salt Lake City homes the usual culprits are the same few places:</p>
<ul>
<li><strong>Flashing</strong> around chimneys, skylights, plumbing vents and where a roof meets a wall</li>
<li><strong>Ice dams</strong> at the eaves, where meltwater refreezes and backs up under the shingles</li>
<li><strong>Worn sealant and seams</strong> on flat and low-slope roofs</li>
<li><strong>Clogged gutters and drains</strong> that let water and ice build up on the roof</li>
</ul>
<p>We trace the path from the stain back to the entry point, fix that, and check the decking around it for rot. If the leak keeps coming back, it's usually a ventilation or ice-dam issue, and we'll say so. North Dakota State University Extension puts it plainly: <a href="{NDSU}" rel="noopener">heat escaping into the attic melts the snow</a>, and that water freezes again when it reaches the colder eaves.</p>

<h2>Storm and tree damage</h2>
<p>Spring wind, summer hail and heavy wet snow all take a toll. After a storm, start from the ground. Look for shingles in the yard, dents in gutters and flashing, and branches on the roof. Take photos from a safe spot. They'll help us, and they'll help with an insurance claim if you decide to file one.</p>
<p>Please don't climb up on a wet or icy roof. Call us, and we'll check it, secure anything loose and give you a written repair estimate.</p>

<h2>Repair or replace? How we decide</h2>
<p>We'll always tell you which way we'd go and why. This is the rough line we use:</p>
<div class="table-wrap"><table>
<thead><tr><th>Usually a repair</th><th>Usually time to replace</th></tr></thead>
<tbody>
<tr><td>Damage is in one spot (a storm, a branch, one vent)</td><td>Leaks keep showing up in new places</td></tr>
<tr><td>A few shingles are missing or cracked</td><td>Shingles are curling or bald across the whole roof</td></tr>
<tr><td>Flashing or a seal has failed</td><td>The deck feels soft or sags</td></tr>
<tr><td>The roof is well inside its expected life</td><td>The roof is near or past the end of its warranty</td></tr>
</tbody></table></div>
<p>Not sure how old your roof is or how much life it has left? Our guide on <a href="@/{BLOG}">how long roofs last in Utah</a> walks through it, and our <a href="@/residential/">residential roofing</a> page covers new roofs and re-roofing.</p>

<h2>Gutters, drainage and snow</h2>
<p>It's important that your gutters and drainage systems work. If they don't, water, snow and ice build up and cause major problems for you and your roof. A gutter full of leaves in November is an ice dam waiting to happen in January.</p>
<p>We repair and re-hang gutters, fix downspouts and sort out drainage on flat roofs where water sits in low spots. For your peace of mind, let us inspect the whole roof while we're up there and repair anything else we find.</p>

<h2>Commercial roof repairs</h2>
<p>A leak in a commercial building isn't just a stain. It can ruin inventory, shut down a room or damage a tenant's equipment. We repair flat and pitched commercial roofs and work around your hours so your business keeps running. For ongoing care, our <a href="@/commercial/">commercial roofing</a> maintenance program helps property owners stretch the life of their roofs.</p>
<p>A property manager with more than 30 years of experience told us we were "especially responsive when repairs are needed to stop damage to tenant spaces and buildings." That's the standard.</p>

<h2>Why property owners call us for roof repair in Salt Lake City</h2>
<ul class="checks">
<li>Licensed, insured and certified for residential and commercial work</li>
<li>A+ rating with the Better Business Bureau</li>
<li>Quick response on leaks, with an emergency line: {SITE["emerg"]}</li>
<li>Free estimates and written bids</li>
<li>Waterproofing know-how most roofers don't have. It's in our name.</li>
</ul>

<h2>Roof repair questions</h2>
{faq_html(REPAIR_FAQ)}
'''

REPAIR = {
    "path": "roof-repair/",
    "title": "Roof Repair in Salt Lake City, UT | Advanced Roofing",
    "meta": "Roof repair in Salt Lake City for homes and businesses: leaks, shingles, storm damage, flashing and gutters. Licensed, insured, BBB A+. Free estimates. Call us.",
    "body": page_hero([("Home", ""), ("Roof Repair", "roof-repair/")], "Roof Repair in Salt Lake City",
                      "Leaks, missing shingles, storm damage and worn flashing, fixed at the source by a licensed, insured crew.",
                      "shingle-gable-vent", "Gable vent set into an asphalt shingle roof", "Residential &amp; commercial")
            + layout(REPAIR_ART, [("Residential roofing", "residential/"), ("Commercial roofing", "commercial/"),
                                  ("Waterproofing", "waterproofing/"), ("How long roofs last in Utah", BLOG),
                                  ("Get a free quote", "get-a-quote/")])
            + cta_band("Water coming in?", "Call now. We'll help you stop the damage first and fix the cause after."),
    "og": "shingle-gable-vent",
}
REPAIR["schema"] = service_schema(REPAIR, "Roof Repair", "Residential and commercial roof repair in Salt Lake City: leaks, shingles, storm and tree damage, flashing, gutters and drainage.") + [
    faq_schema(REPAIR_FAQ), crumbs_schema([("Home", ""), ("Roof Repair", "roof-repair/")])]

# --------------------------------------------------------------------------- commercial
COM_FAQ = [
    ("Do you work on flat and pitched commercial roofs?",
     "Yes. We handle most commercial roofing needs, whether it's a flat roof on a strip center or a pitched roof on an office building. We check insulation, reflectivity and drainage at the same time, so the new roof works with the building instead of fighting it."),
    ("Can you re-roof without shutting down my business?",
     "In most cases, yes. We know how important it is to keep your business running, so we plan the work in stages and around your hours. Tell us what can't be disrupted, like a loading dock or a busy entrance, and we'll schedule around it."),
    ("What is a commercial roof maintenance program?",
     "It's a planned schedule of inspections and small repairs. We check seams, flashing, drains and any damage from other trades on the roof, then fix small problems before they turn into leaks. The goal is a longer roof life and fewer surprise repair bills."),
    ("Should we add insulation when we replace the roof?",
     "Often, yes. Re-roofing is the cheapest time to add insulation above the deck because the roof is already open. It can noticeably lower a building's energy costs. We'll look at what's there now and tell you whether an upgrade makes sense."),
    ("Do you help with commercial roofing building codes?",
     "Yes. Commercial roofs in Salt Lake City and nearby cities have to meet local building codes. We're familiar with them and can help you choose materials and a design that meet code from the start."),
]

COM_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control provides commercial roofing in Salt Lake City: new roof construction, re-roofing, repairs and a maintenance program for flat and pitched roofs. We plan each job around insulation, drainage and your business hours. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> for a free quote.</div>

<p>As commercial roofers in Salt Lake City, we have the know-how to respond to most commercial roofing needs, whether it's a flat roof or a pitched one. And we don't look at the roof alone. Your building's thermal needs get sorted out at the same time we decide what the roof needs and which materials we'll use.</p>

<h2>Questions we answer before we quote a commercial roof</h2>
<p>A good commercial roof bid starts with the building, not a price sheet. These are the questions our roofers work through on every job:</p>
<ul class="checks">
<li>Is there enough insulation below and above the deck?</li>
<li>Does the roof need more reflectivity?</li>
<li>Do the existing slopes drain properly, or should they be steepened toward the drains?</li>
<li>Does the drainage system need more primary or secondary drains?</li>
</ul>
<p>Get those right and the roof lasts. Get them wrong and even a brand-new membrane will pond water and fail early.</p>

<figure>{img("white-flat-roof-wasatch-mountains", "White flat commercial roof with the Wasatch Mountains in the distance")}<figcaption>A white flat commercial roof in the Salt Lake Valley, with the Wasatch behind it.</figcaption></figure>

<h2>More than moisture control</h2>
<p>Commercial roofs do more than keep water out. Some clients want a rooftop garden or photovoltaic (PV) panels. Others have HVAC units, satellite dishes and the technicians who service them walking across the roof every month.</p>
<p>As a commercial roofing contractor serving Salt Lake City, we check that work by other trades doesn't damage your roofing system, and we plan for the loads and foot traffic up front.</p>

<h2>Five things to weigh before a new commercial roof</h2>
<p>When we take on any job, we consider these five factors, and we'd encourage you to do the same.</p>
<h3>1. Building construction</h3>
<p>Know what the building and the existing roof structure are made of. That tells you whether the support structure can stay or should be replaced with something better suited to the roofing material you choose. It's often a good idea to upgrade the insulation when you replace the roof, because it can lower the building's energy costs a lot.</p>
<h3>2. Investment objectives</h3>
<p>Commercial property can have any number of goals. Knowing yours sets a budget that makes sense and still earns a return when you sell. Ask yourself: How long do I plan to own the property? What length of warranty do I want? What's my budget, and do I have the capital now?</p>
<h3>3. Property use</h3>
<p>What happens inside affects the roof you choose. Will there be regular roof traffic, or only maintenance workers? What would a leak damage, and what would it cost if it ruined inventory or equipment?</p>
<h3>4. Location</h3>
<p>Here in the valley, that means heavy snow loads, freeze-thaw cycles and strong sun at elevation. Reflectivity matters too: the U.S. Department of Energy's <a href="{DOE}" rel="noopener">Guide to Cool Roofs</a> explains how solar reflectance and thermal emittance decide how hot a roof gets, and notes that many roofs lose reflectivity over time.</p>
<h3>5. Building codes</h3>
<p>Different cities have different codes. You need to know the ones that apply to commercial roofing in Salt Lake City and the surrounding area before you settle on materials or a design. We're familiar with local codes and can help with this step.</p>

<h2>Keeping your business open during the work</h2>
<p>When it comes to commercial roofing, we know how important it is to keep your business running and not be bothered by roof repair or replacement. We plan the work so its impact on your day-to-day is as small as we can make it. Tell us about parking, deliveries and access up front, and we'll plan around them.</p>
<figure>{img("crew-crane-staging-from-above", "Crane staging roofing materials on a commercial job, seen from above")}<figcaption>Staging materials by crane keeps the site tidy and the work moving.</figcaption></figure>

<h2>Commercial roof maintenance program</h2>
<p>Our Salt Lake City commercial roofing maintenance program helps clients get more years out of their roofs and better protect their businesses and investment properties. Regular checks catch split seams, loose flashing and blocked drains while they're cheap to fix. If something does go wrong between visits, our <a href="@/roof-repair/">roof repair</a> crew is a phone call away.</p>

<h2>Commercial roofing clients</h2>
<p>We've worked on roofs for schools, offices, retail and storage across the Wasatch Front. A few names from our list: Challenger Schools in South Jordan, Staker Parson Offices in Draper, the Chase Building and Union Center in Salt Lake, Wonder Bread in Layton, Miracle Bowl in Provo and Cedar Park Office Buildings in Murray.</p>
<p><a href="@/clients/">See the full client list</a> or browse our <a href="@/salt-lake-city-commercial-roofing-and-residential-roofing/">Salt Lake City project gallery</a>.</p>

<h2>Commercial roofing questions</h2>
{faq_html(COM_FAQ)}
'''

COMMERCIAL = {
    "path": "commercial/",
    "title": "Commercial Roofing Salt Lake City, UT | Advanced Roofing",
    "meta": "Commercial roofing in Salt Lake City: flat and pitched roof installation, re-roofing, repairs and maintenance plans that keep your business open. Free quotes.",
    "body": page_hero([("Home", ""), ("Commercial Roofing", "commercial/")], "Commercial Roofing in Salt Lake City",
                      "Flat and pitched roofs for offices, schools, retail and storage, planned around insulation, drainage and your business hours.",
                      "corrugated-metal-roof-vents", "Rooftop ventilation units on a corrugated metal commercial roof", "For property owners &amp; managers")
            + layout(COM_ART, [("Roof repair", "roof-repair/"), ("Waterproofing", "waterproofing/"),
                               ("Our clients", "clients/"), ("Salt Lake City projects", "salt-lake-city-commercial-roofing-and-residential-roofing/"),
                               ("Get a free quote", "get-a-quote/")])
            + cta_band("Planning a re-roof?", "Get a written bid with the materials, the method and a schedule that works around your business."),
    "og": "white-flat-roof-wasatch-mountains",
}
COMMERCIAL["schema"] = service_schema(COMMERCIAL, "Commercial Roofing", "Commercial roof installation, re-roofing, repair and maintenance for flat and pitched roofs in Salt Lake City, Utah.") + [
    faq_schema(COM_FAQ), crumbs_schema([("Home", ""), ("Commercial Roofing", "commercial/")])]

# --------------------------------------------------------------------------- residential
RES_FAQ = [
    ("Which roofing material is best for a Utah home?",
     "Asphalt shingles are the most common and cost the least. Metal lasts longest, sheds snow well and may carry a lifetime warranty. Concrete or clay tile lasts like metal but is heavy. Wood shakes look great but are less common because of fire concerns. Your budget and house style decide it."),
    ("What's the difference between re-roofing and a new roof?",
     "A new roof installation is for new construction or an addition, starting from bare framing. Re-roofing means replacing the covering on an existing roof. We check the deck underneath and repair or replace damaged sections, so the new roof sits on a sound base."),
    ("Why does attic ventilation matter so much?",
     "Good ventilation keeps the roof deck cold in winter and lets heat escape in summer. That helps prevent ice dams, keeps shingles from cooking and can make rooms more comfortable. One client found a room they'd heated with a space heater for 20 years didn't need it after we vented their new roof."),
    ("Will a new roof disrupt my family's routine?",
     "We plan the work so it doesn't get in the way of your daily routine. You'll know when the crew is coming and where materials will go, and we clean up when the job is done."),
    ("Do you do roof repairs as well as replacements?",
     "Yes. Plenty of roofs only need a repair. We'll tell you honestly whether a repair will do the job or whether the roof is ready to be replaced. See our roof repair page for the kinds of repairs we handle."),
]

RES_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control installs, replaces and repairs residential roofing in Salt Lake City and Park City. We work in asphalt shingles, metal, concrete or clay tile and wood shakes, and we check the deck and ventilation on every job. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> for a free quote.</div>

<p>Every home is someone's castle, and we've found that homeowners' roofing needs in Salt Lake City can be quite demanding. For one thing, the roof has to look right with the rest of the house. So the challenge for our residential roofers is to make it look right and also perform the way it should, protecting what's usually your biggest investment.</p>
<p>As a residential roofing contractor in Salt Lake City, we help you choose high-quality materials, we make sure the deck underneath is sound before we build on it, and we make sure the ventilation meets every requirement. We also plan the work so it doesn't interrupt you or your family's routine.</p>

<h2>Residential roofing services</h2>
<div class="table-wrap"><table>
<thead><tr><th>Service</th><th>When you need it</th></tr></thead>
<tbody>
<tr><td>New roof installation</td><td>New builds and additions, starting from bare framing</td></tr>
<tr><td>Roof replacement and re-roofing</td><td>The old roof is worn out; we tear off, check the deck and install new</td></tr>
<tr><td>Roof repairs and leak repairs</td><td>Storm damage, missing shingles, failed flashing (see <a href="@/roof-repair/">roof repair</a>)</td></tr>
<tr><td>Roof maintenance</td><td>Keeping a healthy roof that way, especially before winter</td></tr>
<tr><td>Waterproofing</td><td>Low-slope sections, balconies and problem transitions (see <a href="@/waterproofing/">waterproofing</a>)</td></tr>
<tr><td>Drainage and gutter options</td><td>Water and ice building up at the eaves</td></tr>
</tbody></table></div>

<h2>Top residential roofing materials for Salt Lake City homes</h2>
<p>Several roofing materials work well here. These are the four we're asked about most.</p>

<figure>{img("material-asphalt-shingles", "Close-up of asphalt shingles on a sloped roof")}</figure>
<h3>Composition or asphalt shingles</h3>
<p>By far the most common roofing material for homes in the United States. Asphalt shingles come in about a dozen colors, solid and blended, and go with almost any home design. They're generally guaranteed for 20 to 30 years and cost a lot less than the other options, which is a big reason they're so popular.</p>

<h3>Metal panels or tiles</h3>
<p>Metal has been standard on farm and commercial buildings for decades, and it's now the fastest-growing type of home roofing. Metal roofs last a long time and may come with a lifetime warranty. Panels go up quickly and need little upkeep. Metal tiles need a bit more care but can be made to look like wood or slate. Expect a metal roof to cost a bit more than double an asphalt roof, with far better durability.</p>

<h3>Concrete or clay tile</h3>
<p>You'll still find some clay tile roofs in Salt Lake City. Concrete and clay are comparable to metal in price and lifespan, though a little more expensive on average. They can mimic other materials like wood shakes or slate. They're also heavier than anything else used in Utah, so the structure has to be able to carry the weight.</p>

<h3>Wood shakes and shingles</h3>
<p>Wood roofs look amazing, but they're less popular now, partly because of fire safety concerns. Shakes are thick and tough and stand up well to hail. Wood shingles are thinner and take weather damage more easily. Both cost about the same as concrete, clay or metal.</p>

<p>Want to know how long each one really lasts here? Read <a href="@/{BLOG}">how long roofs last in Utah</a>.</p>

<h2>Ventilation: the part of your roof you can't see</h2>
<p>A roof that looks perfect can still fail early if the attic can't breathe. Trapped heat cooks shingles from below in summer and melts snow in winter, which leads straight to ice dams. Moisture from the house condenses on a cold deck and rots it.</p>
<p>That's why we check intake and exhaust venting on every job. One homeowner wrote that after we replaced and vented their roof, it was "the first winter we did not need to use a space heater in one particular room of the house." They'd used one in that room for 20 years.</p>
<figure>{img("roof-layers-diagram", "Sketch of a house roof cut away to show the deck, underlayment, insulation and shingle layers")}<figcaption>A roof is a system: deck, underlayment, flashing, venting and the covering you see.</figcaption></figure>

<h2>We'll waterproof your residential roof</h2>
<p>Our residential roofers also provide waterproofing that can lower your energy costs and add years to your roof. Whether you need roof repair, replacement, re-roofing, waterproofing or maintenance, we're the Salt Lake City residential roofing contractor to call for high-quality work, every time.</p>

<h2>What install day looks like</h2>
<p>You'll know when the crew is coming and where the materials will go. We keep the site tidy and clean up when the job is done. One client noted the crew "left the yard clean," and that one of the owners came by several times during the install to check progress and talk with the crew.</p>
<p>See the work for yourself in our <a href="@/park-city-commercial-roofing-and-waterproofing-solutions/">Park City project gallery</a>.</p>

<h2>Residential roofing questions</h2>
{faq_html(RES_FAQ)}
'''

RESIDENTIAL = {
    "path": "residential/",
    "title": "Residential Roofing Salt Lake City | Advanced Roofing",
    "meta": "Residential roofing in Salt Lake City and Park City: new roofs, re-roofing and repairs in shingle, metal, tile or wood, with ventilation done right. Free quote.",
    "body": page_hero([("Home", ""), ("Residential Roofing", "residential/")], "Residential Roofing in Salt Lake City",
                      "New roofs, re-roofing and repairs that look right on your home and hold up to Utah winters.",
                      "shingle-roof-homes", "Gabled asphalt shingle roofs on two-story homes", "For homeowners")
            + layout(RES_ART, [("Roof repair", "roof-repair/"), ("Waterproofing", "waterproofing/"),
                               ("How long roofs last in Utah", BLOG), ("Park City projects", "park-city-commercial-roofing-and-waterproofing-solutions/"),
                               ("Get a free quote", "get-a-quote/")])
            + cta_band("Thinking about a new roof?", "We'll inspect the one you have, tell you honestly if it can be repaired, and give you a written quote if it can't."),
    "og": "shingle-roof-homes",
}
RESIDENTIAL["schema"] = service_schema(RESIDENTIAL, "Residential Roofing", "Residential roof installation, replacement, re-roofing and repair in Salt Lake City and Park City, Utah.",
                                       area=[{"@type": "City", "name": "Salt Lake City, UT"}, {"@type": "City", "name": "Park City, UT"}]) + [
    faq_schema(RES_FAQ), crumbs_schema([("Home", ""), ("Residential Roofing", "residential/")])]

# --------------------------------------------------------------------------- waterproofing
WP_FAQ = [
    ("What does roof waterproofing do?",
     "Waterproofing adds a continuous barrier that keeps water out of the roof system. It stops leaks, protects the deck and insulation, and can reduce maintenance caused by thermal shock, the stress of a roof heating and cooling fast. It also helps a roof last longer."),
    ("Is waterproofing only for flat roofs?",
     "No. Flat and low-slope roofs need it most, but balconies, decks over living space, valleys and wall transitions on pitched roofs benefit too. We look at where water actually collects on your building and waterproof those areas."),
    ("Can waterproofing save energy?",
     "Yes. Wet insulation doesn't insulate well, so keeping it dry helps your heating and cooling work as designed. Some waterproofing systems are also reflective, which can cut heat gain in summer. We'll explain the options that fit your roof."),
    ("How do I know if my roof needs waterproofing?",
     "Common signs are leaks that return after a patch, water stains near walls or balconies, ponding water on a flat roof that's still there two days after a storm, and blistered or cracked roof coatings. If you see any of these, have the roof looked at before winter freeze-thaw makes them worse."),
    ("Do you waterproof homes and commercial buildings?",
     "Both. We waterproof residential and commercial roofs in Salt Lake City and Park City, from a single leaking balcony over a garage to a full commercial flat roof. Every roof, large or small, needs maintenance and repair at some point."),
]

WP_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control provides waterproofing in Salt Lake City and Park City for residential and commercial roofs. Waterproofing stops leaks, protects insulation, cuts energy loss and can extend your roof's life. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> and we'll check where water is getting in.</div>

<p>Moisture control is half our name for a reason. Our residential and commercial roofers in Salt Lake City have the knowledge and experience to find a waterproofing solution that fits each roof. Done right, waterproofing brings real benefits: lower roof costs over time, better energy efficiency, a longer roof life, and less maintenance caused by thermal shock.</p>
<p>Because we understand how all the roofing parts work together, we can respond to each roof's needs without overspending.</p>

<h2>Where water gets into a roof</h2>
<p>Most leaks start at a change: where two roof planes meet, where the roof meets a wall, or where something pokes through it. On flat roofs, water that sits in low spots will eventually find a seam.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trouble spot</th><th>Why it leaks</th></tr></thead>
<tbody>
<tr><td>Flat and low-slope roofs</td><td>Ponding water, aging seams, worn membrane</td></tr>
<tr><td>Balconies and decks over rooms or garages</td><td>Water runs toward the house wall or through the deck surface</td></tr>
<tr><td>Wall and chimney transitions</td><td>Flashing pulls away or the sealant dries out</td></tr>
<tr><td>Valleys and eaves</td><td>Ice dams push meltwater up under the covering</td></tr>
<tr><td>Penetrations (vents, HVAC, skylights)</td><td>Boots and curbs crack in the sun and cold</td></tr>
</tbody></table></div>

<figure>{img("ceiling-water-damage", "Ceiling with a hole torn open by water damage, exposing the framing above")}<figcaption>This is what a slow leak does when nobody catches it.</figcaption></figure>

<h2>Why waterproofing pays for itself</h2>
<h3>Lower roof costs</h3>
<p>A dry roof deck doesn't rot, and dry insulation doesn't need replacing. Catching water early is far cheaper than replacing sheathing and drywall later.</p>
<h3>Energy efficiency</h3>
<p>Wet insulation loses much of its value. Keeping it dry keeps your heating bill where it should be in January. Some systems also reflect sunlight; the Department of Energy's <a href="{DOE}" rel="noopener">Guide to Cool Roofs</a> explains how reflectance and emittance affect roof temperature.</p>
<h3>Longer roof life</h3>
<p>Every Utah winter puts a roof through one freeze-thaw cycle after another. Waterproofing keeps water out of the cracks where that cycle does the most damage.</p>
<h3>Less damage from thermal shock</h3>
<p>A dark roof can go from icy at dawn to hot by afternoon in spring. That fast swing stresses seams and flashing. The right waterproofing layer helps the roof move without opening up.</p>

<h2>Waterproofing for homes and businesses</h2>
<p>No matter how large or small, all roofs need maintenance and repair. Our crew covers every part of it, from <a href="@/roof-repair/">roof repair</a> to full restoration on all roof types. We can turn your workplace or home into a dry, comfortable space without leaks.</p>
<p>One homeowner had a leak around a balcony that ran into their garage. We came back and fixed it at no charge, in their words "in a professional, no-hassle manner." That's the kind of follow-through you should expect.</p>
<p>We also work with the same membrane materials on water features. Our <a href="@/ponds/">pond liner</a> work uses EPDM, PVC and other membranes, so we understand how they behave in Utah's climate.</p>
<figure>{img("roof-layers-diagram", "Sketch of a house roof cut away to show its layers")}<figcaption>Waterproofing works as part of the whole roof system, not as a coat of paint on top.</figcaption></figure>

<h2>How we approach a waterproofing job</h2>
<p>Waterproofing only works if it goes where the water actually is. So we start by finding the path, not by picking a product.</p>
<ol>
<li><strong>Trace the water.</strong> We follow stains, wet insulation and soft decking back to the point where water gets in.</li>
<li><strong>Check what's underneath.</strong> Wet or rotten decking and soaked insulation get replaced first. Sealing over them just traps the moisture.</li>
<li><strong>Match the system to the roof.</strong> A balcony, a flat commercial roof and a valley on a shingle roof each need a different approach.</li>
<li><strong>Detail the transitions.</strong> Walls, curbs, drains and penetrations get the most attention, because that's where most leaks start.</li>
<li><strong>Stand behind it.</strong> If something isn't right afterwards, call us and we'll come back and make it right.</li>
</ol>
<p>Some leaks turn out to be a ventilation or ice-dam problem rather than a waterproofing one. If that's the case, we'll tell you, and fix the cause instead of selling you a coating.</p>

<h2>Waterproofing questions</h2>
{faq_html(WP_FAQ)}
'''

WATERPROOFING = {
    "path": "waterproofing/",
    "title": "Waterproofing Salt Lake City | Roofs & Moisture Control",
    "meta": "Roof waterproofing in Salt Lake City and Park City for homes and commercial buildings. Stop leaks, protect insulation and add years to your roof. Call today.",
    "body": page_hero([("Home", ""), ("Waterproofing", "waterproofing/")], "Roof Waterproofing in Salt Lake City",
                      "Leaks stopped, insulation kept dry and years added to the roof you already have.",
                      "gutter-storm-clouds", "Metal gutter and downspout under dark storm clouds", "Moisture control is in our name")
            + layout(WP_ART, [("Roof repair", "roof-repair/"), ("Commercial roofing", "commercial/"),
                              ("Residential roofing", "residential/"), ("Ponds &amp; water features", "ponds/"),
                              ("Get a free quote", "get-a-quote/")])
            + cta_band("A leak that keeps coming back?", "That's usually a waterproofing problem, not a shingle problem. Let's find it."),
    "og": "gutter-storm-clouds",
}
WATERPROOFING["schema"] = service_schema(WATERPROOFING, "Roof Waterproofing", "Residential and commercial roof waterproofing in Salt Lake City and Park City, Utah.",
                                         area=[{"@type": "City", "name": "Salt Lake City, UT"}, {"@type": "City", "name": "Park City, UT"}]) + [
    faq_schema(WP_FAQ), crumbs_schema([("Home", ""), ("Waterproofing", "waterproofing/")])]

# --------------------------------------------------------------------------- ponds
PONDS_LIST = [("Assey Pond", "Orem", 100000), ("Dave Checket Pond", "Wolf Creek", 60000),
              ("Wally Joiner Ponds", "Mapleton", 20000), ("Huntsman fishing pond", "Emery County", 4000),
              ("Lagoon Pond", "Farmington", 2000), ("Fear Factory", "Salt Lake", 1000)]
bars = "".join(
    f'<li style="display:grid;gap:8px;padding:16px 0;border-bottom:1px solid var(--line)"><div style="display:flex;justify-content:space-between;gap:12px"><b style="font:600 1.2rem/1.2 var(--display);text-transform:uppercase">{n} <span class="muted" style="font:400 .95rem var(--body);text-transform:none">· {c}</span></b><span style="font:700 1.1rem var(--display)">{s:,} sq ft</span></div><span style="display:block;height:8px;background:var(--stone-2);border-radius:4px"><span style="display:block;height:8px;width:{max(2, s/1000):.0f}%;background:var(--green);border-radius:4px"></span></span></li>'
    for n, c, s in PONDS_LIST)

PONDS_FAQ = [
    ("What pond liner materials do you install?",
     "We work with thermosets, including EPDM, neoprene and butyl, and with thermoplastics such as CSPE and PVC, plus other copolymers on the market. The right one depends on the size of the pond, what it holds and how it will be used."),
    ("Do you install liners for large commercial or agricultural ponds?",
     "Yes. Our listed projects run from a 1,000 square foot feature to the 100,000 square foot Assey Pond in Orem. We install liners for architectural, industrial and commercial uses, including catchments and reservoirs."),
    ("Why would a roofing company install pond liners?",
     "A pond liner and a flat roof membrane solve the same problem: keeping water exactly where you want it. We understand these membranes, how they're joined and how they behave in heat and cold, so the skills carry straight over."),
]

PONDS_ART = f'''
<div class="answer">Advanced Roofing and Moisture Control installs pond liners and water features in Utah, from backyard ponds to 100,000 square foot reservoirs. We work with EPDM, neoprene, butyl, CSPE, PVC and other membranes, and pick the right system for each installation. Call <a href="tel:{SITE["tel"]}">{SITE["phone"]}</a> to talk through your project.</div>

<p>With ponds, catchments, reservoirs and other water features, we understand what each installation needs and what each product can handle. It's the same moisture control we bring to roofs, just pointed the other way: keeping water in instead of out.</p>
<p>Pond liners can be architectural, industrial or commercial. We know the products and adapt to each installation with the proper membrane system.</p>

<h2>Pond liner materials we install</h2>
<div class="table-wrap"><table>
<thead><tr><th>Family</th><th>Materials</th><th>Good to know</th></tr></thead>
<tbody>
<tr><td>Thermosets</td><td>EPDM, neoprene, butyl</td><td>Rubber membranes that stay flexible in the cold</td></tr>
<tr><td>Thermoplastics</td><td>CSPE, PVC</td><td>Seams can be heat-welded into one continuous sheet</td></tr>
<tr><td>Other copolymers</td><td>Various</td><td>Chosen for specific chemical or project needs</td></tr>
</tbody></table></div>

<h2>Pond projects on our list</h2>
<p>These are real ponds we've lined, by size. There are many more.</p>
<ul style="list-style:none;padding:0;margin:0 0 1.6em;border-top:1px solid var(--line)">{bars}</ul>

<figure>{img("pond-waterfall-garden", "Garden pond with a small waterfall surrounded by shrubs and trees")}<figcaption>A finished water feature starts with a liner nobody will ever see.</figcaption></figure>

<h2>Architectural, industrial and commercial installations</h2>
<p>A decorative garden pond and an irrigation reservoir need very different liners. We look at size, depth, what the water will touch, sun exposure and how the site is accessed before we recommend a membrane. Then we install it with the seams and edges done properly, because that's where liners fail.</p>
<p>Already have a liner that's leaking? The same skills we use for <a href="@/waterproofing/">roof waterproofing</a> apply. We can often find and repair the problem.</p>
<figure>{img("water-lilies-pond", "White water lilies blooming on a pond")}</figure>

<h2>Planning a pond liner project</h2>
<p>A liner is only as good as the ground under it and the way it's sized and joined. Here's what we look at before we order material.</p>
<h3>Size and depth</h3>
<p>A common rule of thumb for sizing a flexible liner is the pond's length plus twice its deepest depth, plus extra at each edge for anchoring, and the same for the width. Shelves, waterfalls and streams add more. We measure the finished excavation, not the plan, so there are no short edges.</p>
<h3>What goes under the liner</h3>
<p>Rocks, roots and sharp gravel will puncture a liner from below over time. The base gets cleared and smoothed, and a protective underlayment goes down before the membrane.</p>
<h3>What the water touches</h3>
<p>Fish and plants, irrigation water and industrial catchments all put different demands on a membrane. That's one of the biggest factors in choosing between rubber and thermoplastic liners.</p>
<h3>Seams and edges</h3>
<p>On large ponds the liner is made from several panels. Seams and the anchored edges are where liners fail, so that's where we spend the most care.</p>
<p>Already have a pond that's losing water? Tell us how fast the level drops and where the liner is visible. Leaks are often at the edges, around a waterfall or at a seam, and many can be repaired.</p>

<h2>Pond and liner questions</h2>
{faq_html(PONDS_FAQ)}
'''

PONDS = {
    "path": "ponds/",
    "title": "Pond Liner Installation Utah | Advanced Moisture Control",
    "meta": "Pond liner and water feature installation in Utah with EPDM, butyl, neoprene, CSPE and PVC. Backyard ponds to 100,000 sq ft reservoirs. Call for a quote.",
    "body": page_hero([("Home", ""), ("Ponds &amp; Water Features", "ponds/")], "Pond Liners &amp; Water Features",
                      "Liners for ponds, catchments and reservoirs across Utah, from a backyard feature to 100,000 square feet.",
                      "pond-waterfall-garden", "Garden pond with a small waterfall", "Residential &amp; commercial ponds")
            + layout(PONDS_ART, [("Waterproofing", "waterproofing/"), ("Our clients", "clients/"),
                                 ("Commercial roofing", "commercial/"), ("Get a free quote", "get-a-quote/")])
            + cta_band("Planning a pond?", "Tell us the size and what it's for. We'll recommend a liner and give you a quote."),
    "og": "pond-waterfall-garden",
}
PONDS["schema"] = service_schema(PONDS, "Pond Liner Installation", "Pond liner and water feature installation in Utah using EPDM, neoprene, butyl, CSPE and PVC membranes.",
                                 area=[{"@type": "State", "name": "Utah"}]) + [
    faq_schema(PONDS_FAQ), crumbs_schema([("Home", ""), ("Ponds & Water Features", "ponds/")])]

PAGES = [REPAIR, COMMERCIAL, RESIDENTIAL, WATERPROOFING, PONDS]
