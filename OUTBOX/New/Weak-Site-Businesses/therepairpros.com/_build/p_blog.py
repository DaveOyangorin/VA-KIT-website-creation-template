"""New blog post for therepairpros.com (21 Oct 2026): repair vs replace and appliance lifespans. It targets an informational question,
not "dryer repair salt lake city" or any other service keyword. Figures: NAHB / Bank of America Home Equity, Study of Life Expectancy of
Home Components (Feb 2007, Table 1, Appliances; read from the original PDF), and ENERGY STAR's refrigerator page. Prices and warranty are
The Repair Pros' own (home page)."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/repair-or-replace-appliance-lifespan/"
H1 = "Repair or replace? How long appliances actually last"
LIFE = [("Gas range", "15"), ("Range/oven hood", "14"), ("Electric range", "13"), ("Standard refrigerator", "13"), ("Dryer (gas or electric)", "13"),
        ("Food waste disposer", "12"), ("Freezer", "11"), ("Washer", "10"), ("Dishwasher", "9"), ("Microwave oven", "9"), ("Compact refrigerator", "9"), ("Trash compactor", "6")]
FAQ = [("How long does a refrigerator last?", "About 13 years for a standard refrigerator and 9 for a compact one, according to the National Association of Home Builders&rsquo; life-expectancy study. Use and maintenance move that number in both directions."),
       ("Is it worth repairing a 10-year-old washer?", "It depends on the repair. The NAHB puts a washer&rsquo;s typical life at about 10 years, so a big repair on an old machine deserves a second look, while a small part on an otherwise healthy washer usually doesn&rsquo;t."),
       ("How much does a diagnosis cost?", "At The Repair Pros, an on-site service call to diagnose the problem is $125, and the average job runs $150&ndash;$400. A virtual repairman visit costs a fraction of that.")]
BODY = f'''<p class="answer">Most major appliances last about 9 to 15 years. A gas range lasts the longest, at around 15. Dishwashers and microwaves are at the short end, at about 9. Whether to repair one comes down to three numbers: its age, the repair price, and what a replacement would cost you, including the energy it uses.</p>

<p>Every appliance repair call starts with the same question from the homeowner: <em>is it worth fixing?</em> Sometimes the answer is obvious. A five-year-old refrigerator with a failed ice maker is worth fixing, and a 20-year-old one with a dead compressor probably isn&rsquo;t. In between is a wide grey zone. Here&rsquo;s a straightforward way to think it through, based on published lifespan data and the costs you&rsquo;ll actually see.</p>

<h2>How long do appliances last?</h2>
<p>The most cited numbers come from a study by the National Association of Home Builders (NAHB) and Bank of America Home Equity, <i>Study of Life Expectancy of Home Components</i>. NAHB surveyed manufacturers, trade associations and researchers, and lists these typical lifespans for a first owner:</p>
<div class="tbl"><table><thead><tr><th>Appliance</th><th>Typical life (years)</th></tr></thead><tbody>
{"".join(f"<tr><td>{a}</td><td>{y}</td></tr>" for a, y in LIFE)}
</tbody></table></div>
<p>Two caveats come straight from the study. First, these are general guidelines, not guarantees: life expectancy depends heavily on how much an appliance is used and how well it&rsquo;s maintained. Second, NAHB notes that appliances are often replaced long before they wear out, because styling and technology change. A dryer that runs every day for a family of six will reach the end of its life sooner than one that runs twice a week.</p>

<h2>A simple way to decide</h2>
<h3>1. Where is it in its life?</h3>
<p>Compare the appliance&rsquo;s age with the table. In the first half of its expected life, repair is almost always the better value. Most failures at that age are one part: a pump, a belt, a heating element, a control board, a door switch. Past about three-quarters of its expected life, look harder at the repair price, because another part may follow.</p>

<h3>2. What does the repair cost against a replacement?</h3>
<p>Many people use a rough rule: if a repair costs more than about half the price of a comparable new appliance, consider replacing it. It&rsquo;s a starting point, not a law. A $300 repair on a $3,000 built-in refrigerator is an easy call. The same repair on a basic $600 top-freezer model, near the end of its life, is not.</p>
<p>The catch is that you can&rsquo;t know the repair cost until someone has diagnosed the problem. &ldquo;Not cooling&rdquo; can be a $20 fan motor or a sealed-system failure. That&rsquo;s why The Repair Pros charges a flat <strong>$125</strong> for an on-site service call to diagnose the issue, and why our average job lands between <strong>$150 and $400</strong>. Once you have a real number, the repair-or-replace decision is usually easy.</p>

<h3>3. Count the energy, especially for refrigerators</h3>
<p>Refrigerators run around the clock, so their energy use adds up. According to ENERGY STAR, an old refrigerator uses about 20% more energy than a model that has earned the ENERGY STAR, and a refrigerator over 15 years old could be costing you about $95 a year to run. ENERGY STAR estimates that replacing an old unit with a certified model and recycling the old one can save about $150 over the new refrigerator&rsquo;s 12-year life. For a fridge in its teens, that tips the scale toward replacing. For a seven-year-old fridge with a bad defrost heater, it doesn&rsquo;t.</p>

<h3>4. Is it still under warranty?</h3>
<p>Check before you pay for anything. Manufacturer warranties often cover parts, and sometimes labor, for the first year or longer on certain components. A factory-authorized service center can do warranty work on the brands it represents. The Repair Pros is a Samsung branded engineer, a Sharp master service center, a Philips TV authorized service center and a Dacor authorized service center. Our own repairs carry a 90-day parts and labor warranty on the work done.</p>

<h2>When repair is usually the better call</h2>
<ul>
<li>The appliance is within the first half to two-thirds of its typical life.</li>
<li>It&rsquo;s a high-end or built-in model whose replacement would mean new cabinetry, gas or electrical work.</li>
<li>The problem is a single part and the rest of the machine is in good shape.</li>
<li>It&rsquo;s a matching set (a washer and dryer pair, a suite of kitchen appliances) you&rsquo;d rather not break up.</li>
</ul>

<h2>When replacing makes more sense</h2>
<ul>
<li>It&rsquo;s at or past its typical life <em>and</em> needs a major repair, such as a compressor, transmission or main control board.</li>
<li>It has needed several repairs in a short time.</li>
<li>It&rsquo;s an old refrigerator or freezer whose energy use is costing you money every month.</li>
<li>Parts are no longer made for it.</li>
</ul>

<h2>Small habits that add years</h2>
<p>The NAHB study stresses that maintenance has a large effect on lifespan. A few habits help almost every appliance reach the far end of its range:</p>
<ul>
<li><strong>Refrigerators:</strong> keep the condenser coils and the area around the unit free of dust, and keep door gaskets clean so they seal.</li>
<li><strong>Dryers:</strong> clean the lint filter every load and keep the vent duct clear. A clogged vent makes the dryer run longer and hotter.</li>
<li><strong>Washers:</strong> don&rsquo;t overload, check the hoses for bulges or cracks, and leave the door of a front-loader open to dry between loads.</li>
<li><strong>Dishwashers:</strong> clean the filter and scrape plates so food doesn&rsquo;t reach the pump and drain.</li>
<li><strong>Ovens and ranges:</strong> wipe spills before they bake on, and use self-clean sparingly.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Not sure which side of the line your appliance is on? <a href="@/#diagnose">Start a work order</a> or call <a href="tel:+18012686868">(801) 268-6868</a>. A diagnosis gives you the real repair number to decide with.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>National Association of Home Builders and Bank of America Home Equity, <a href="https://standards.nsf.org/higherlogic/ws/public/download/348/NAHB%202007%20StudyUseful%20Life%20of%20Home%20Components.pdf" rel="noopener">Study of Life Expectancy of Home Components</a> (February 2007), Table 1: Appliances</li>
<li>ENERGY STAR, <a href="https://www.energystar.gov/products/refrigerators" rel="noopener">Refrigerators</a></li>
<li>The Repair Pros: service call, average job cost and warranty, from our <a href="@/#pricing">pricing</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Repair or replace?", H1, "From the shop &middot; Oct 21, 2026", "Blog", "Repair or Replace? How Long Appliances Last | Repair Pros",
                  "How long do appliances last? Typical lifespans for fridges, washers, dryers, ovens and dishwashers, and a simple way to decide whether to repair or replace.",
                  BODY, image="rp-fridge", alt="A refrigerator after a repair visit", crumbs=[], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "The Repair Pros"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
