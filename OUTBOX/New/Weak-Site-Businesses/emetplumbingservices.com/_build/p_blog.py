"""New blog post for emetplumbingservices.com (22 Oct 2026): furnace filters and MERV ratings. Informational; it doesn't target "plumber
taylorsville", drain cleaning or any plumbing service keyword, and doesn't repeat their existing posts. Sources: EPA "What is a MERV rating?"
(updated 14 Jan 2026); EPA "Guide to Air Cleaners in the Home" (updated 1 Oct 2026); ENERGY STAR "Maintenance Checklist"."""
from engine import faq_html, faq_ld, canon

SLUG = "ourblog/furnace-filter-merv-ratings/"
H1 = "Furnace filters and MERV ratings, explained"
FAQ = [("What MERV rating should I use at home?", "EPA suggests choosing a filter rated at least MERV 13, or as high a rating as your system fan and filter slot can accommodate. An HVAC technician can confirm what your system can handle."),
       ("How often should I change my furnace filter?", "ENERGY STAR recommends inspecting, cleaning or changing filters once a month. EPA says to follow the manufacturer&rsquo;s recommendation, often every 60 to 90 days, and sooner if the filter looks heavily soiled."),
       ("Is a higher MERV always better?", "A higher MERV traps more particles of specific sizes, but your system has to be able to move air through it. EPA recommends the highest rating your fan and filter slot can accommodate, not simply the highest number on the shelf."),
       ("Will a better filter fix mold or musty smells?", "No. EPA says furnace and HVAC filters do not address the cause of mold and musty odors. The moisture problem has to be found and fixed.")]
BODY = f'''<p class="answer">MERV (Minimum Efficiency Reporting Value) tells you how well a furnace or AC filter traps particles between 0.3 and 10 microns; the higher the number, the better it traps them. EPA suggests at least MERV 13, or the highest rating your system fan and filter slot can handle. Check the filter monthly, change it as the manufacturer recommends (often every 60 to 90 days), and make sure it fits snugly.</p>

<p>Utah furnaces work hard from fall through spring, and the filter is the one part of the system most homeowners can take care of themselves. It&rsquo;s also the part people forget. Here&rsquo;s what the numbers on the package mean and how to choose and look after a filter, based on guidance from the U.S. Environmental Protection Agency and ENERGY STAR.</p>

<h2>What MERV means</h2>
<p>According to EPA, MERV stands for <strong>Minimum Efficiency Reporting Values</strong>. The rating reports a filter&rsquo;s ability to capture particles between 0.3 and 10 microns, and it comes from a test method developed by ASHRAE, the American Society of Heating, Refrigerating and Air-Conditioning Engineers.</p>
<p>The scale runs from MERV 1&ndash;4 at the low end up to MERV 16. EPA&rsquo;s summary is simple: <em>the higher the MERV rating, the better the filter is at trapping specific sizes of particles.</em> HEPA filters are a separate category and are not rated on the MERV system.</p>

<h2>Which rating to choose</h2>
<p>EPA&rsquo;s recommendation, if you&rsquo;re upgrading, is to choose a filter rated <strong>at least MERV 13</strong>, or as high a rating as your system fan and filter slot can accommodate.</p>
<p>That second half matters. A filter has to let enough air through for the system to work. EPA notes that many systems can use a MERV 13 filter if it&rsquo;s changed often, but that you may need to consult a professional HVAC technician to find the most efficient filter your particular system can handle. If you&rsquo;re not sure, ask during your next tune-up; it takes a technician a minute to check.</p>

<h2>How often to check and change it</h2>
<p>Two official sources, one practical routine:</p>
<ul>
<li><strong>ENERGY STAR</strong> recommends that you <em>inspect, clean, or change air filters once a month</em> in your central air conditioner, furnace and/or heat pump. It&rsquo;s the one maintenance task ENERGY STAR lists for homeowners to do themselves, and it notes that a dirty filter can raise energy costs and lead to early equipment failure.</li>
<li><strong>EPA</strong> says to replace filters according to the manufacturer&rsquo;s recommendations, which typically suggest every 60 to 90 days, and to change them sooner if they look heavily soiled when you pull them out.</li>
</ul>
<p>In practice: look at the filter every month, and replace it on the manufacturer&rsquo;s schedule or whenever it looks dirty, whichever comes first. Writing the date on the filter frame makes this easy to track.</p>

<h2>Fit matters as much as rating</h2>
<p>A high-rated filter that doesn&rsquo;t fit does little good. EPA advises making sure the filter <strong>fits snugly so air does not leak around it</strong>, and that it fits without being bent or crushed. Check the size printed on the old filter, and check the airflow arrow so the new one faces the right way.</p>

<h2>What a filter can and can&rsquo;t do</h2>
<p>Filters help, but EPA is clear about their limits:</p>
<ul>
<li><strong>They only filter when the system runs.</strong> EPA notes that HVAC filters work only when the system is operating, and systems usually run less than 25% of the time during heating and cooling seasons. Getting more filtration means running the system longer, which EPA points out can raise electricity costs and may make humidity control less reliable in cooling season.</li>
<li><strong>No filter removes everything.</strong> In EPA&rsquo;s words, no air cleaner or filter will eliminate all of the air pollutants in your home.</li>
<li><strong>Filters don&rsquo;t fix mold.</strong> EPA says portable air cleaners and furnace/HVAC filters do not address the cause of mold and musty odors.</li>
<li><strong>Filtration isn&rsquo;t ventilation.</strong> EPA adds that filtration does not replace the need to control pollutant sources and ventilate.</li>
</ul>
<p>EPA also notes that it does not certify or recommend specific brands or models of air filters, so treat brand claims on the package with care and go by the MERV rating and fit.</p>

<h2>Pair the filter with a yearly checkup</h2>
<p>Changing the filter is your job; the rest of the system benefits from a professional look. ENERGY STAR recommends yearly contractor checkups, and advises that it&rsquo;s best to check the cooling system in the spring and the heating system in the fall. A pre-season visit is also a good time to confirm which filter rating your system can handle.</p>

<h2>A simple filter routine</h2>
<ol>
<li>Find your filter slot and note the size printed on the current filter.</li>
<li>Buy the highest MERV your system can handle, aiming for MERV 13 if your technician confirms it&rsquo;s compatible.</li>
<li>Install it snugly with the airflow arrow pointing the right way, and write the date on the frame.</li>
<li>Check it once a month; replace it on the manufacturer&rsquo;s schedule (often 60 to 90 days) or sooner if it&rsquo;s dirty.</li>
<li>Book a heating check in the fall and a cooling check in the spring.</li>
</ol>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Not sure what filter your furnace takes, or due for a fall heating check? Emet Plumbing Heating &amp; Air services heating and air systems across the Salt Lake Valley. Call or text <a href="tel:+18014337354">(801) 433-7354</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/what-merv-rating" rel="noopener">What is a MERV rating?</a> (updated January 14, 2026)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/indoor-air-quality-iaq/guide-air-cleaners-home" rel="noopener">Guide to Air Cleaners in the Home</a> (updated October 1, 2026)</li>
<li>ENERGY STAR, <a href="https://www.energystar.gov/saveathome/heating-cooling/maintenance-checklist" rel="noopener">Maintenance Checklist</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Furnace filters &amp; MERV", H1, "Emet Insights &middot; Oct 22, 2026", "Emet Insights", "Furnace Filters &amp; MERV Ratings, Explained | Emet Plumbing",
                  "What MERV ratings mean, which furnace filter EPA suggests, how often to check and change it, and what filters can't do, from EPA and ENERGY STAR guidance.",
                  BODY, image="em-tech", alt="An Emet technician at the back of a service van", crumbs=[("Blog", "ourblog/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Emet Plumbing Heating & Air"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
