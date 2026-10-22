"""New blog post for applianceserviceut.com (22 Oct 2026): clothes dryer fire safety. Informational; it doesn't target appliance repair,
dryer repair or washer repair keywords. Sources: NFPA "Clothes Dryer Safety" tip sheet; NFPA research "Home Fires Involving Clothes Dryers and
Washing Machines" (March 2017); U.S. Fire Administration "Clothes Dryer Fire Safety" flyer and "Clothes Dryer Fires in Residential
Buildings (2008-2010)" (Topical Fire Report Series, Vol. 13, Issue 7)."""
from engine import faq_html, faq_ld, canon

SLUG = "clothes-dryer-fire-safety/"
H1 = "Clothes dryer fire safety: the lint habit that matters most"
FAQ = [("What is the leading cause of dryer fires?", "Failure to clean. NFPA says the leading cause of home clothes dryer fires is failure to clean them, and the U.S. Fire Administration found failure to clean was the leading factor in residential dryer fires (34 percent)."),
       ("How often should I clean the dryer vent?", "NFPA&rsquo;s tip sheet says once a year, or more often if clothes are taking longer than normal to dry, either yourself or with a dryer lint removal service."),
       ("Is plastic or foil vent hose OK?", "NFPA recommends rigid or flexible metal venting material to sustain proper air flow and drying time."),
       ("When do most dryer fires happen?", "According to the U.S. Fire Administration, residential dryer fires are more common in fall and winter, peaking in January.")]
BODY = f'''<p class="answer">Most dryer fires are preventable. NFPA says the leading cause of home clothes dryer fires is failure to clean them. Clean the lint filter before or after every load, never run the dryer without it, clean the vent pipe at least once a year, use metal venting, and turn the dryer off when you leave home or go to bed.</p>

<p>The clothes dryer is one of the hardest-working appliances in the house, and one of the easiest to forget about. It just runs. But it also pushes hot air through a tumbling drum full of fabric, and that produces lint, a highly combustible material. The National Fire Protection Association (NFPA) and the U.S. Fire Administration (USFA) both point to the same simple fact: most dryer fires come down to cleaning that didn&rsquo;t happen.</p>

<h2>How big is the problem?</h2>
<p>NFPA research found that from 2010 to 2014, U.S. fire departments responded to an estimated <strong>15,970 home fires a year involving clothes dryers or washing machines</strong>, causing an estimated 13 civilian deaths, 440 civilian injuries and $238 million in direct property damage each year. Dust, fiber or lint was the item most often first ignited in fires involving dryers.</p>
<p>A USFA report focused on dryers found an estimated <strong>2,900 clothes dryer fires in residential buildings each year</strong>, causing about 5 deaths, 100 injuries and $35 million in property loss annually. Its key finding: <strong>failure to clean (34 percent) was the leading factor</strong> contributing to these fires.</p>

<h2>Why lint is dangerous</h2>
<p>USFA explains how it happens. A dryer works by forcing hot air through a turning drum, and a full load of wet clothes can hold as much as a gallon and a half of water. As clothes tumble, they shed small fibers. Much of that lint is caught by the filter, but some travels into the vent with the moist air. Lint is highly combustible, and as it builds up in the dryer and the vent, airflow drops. Vents can also be blocked by bird or animal nests or by crushed or damaged ducting. When the dryer can&rsquo;t exhaust properly, it can overheat, and a fire can start.</p>

<h2>The habits that prevent dryer fires</h2>
<h3>Every load</h3>
<ul>
<li><strong>Clean the lint filter</strong> before or after each load (NFPA); USFA says before and after each cycle.</li>
<li><strong>Never use the dryer without a lint filter.</strong></li>
<li><strong>Remove lint that collects around the drum</strong>, and don&rsquo;t forget the back of the dryer, where USFA notes lint can build up.</li>
<li><strong>Don&rsquo;t overload the dryer</strong>, and follow the manufacturer&rsquo;s operating instructions.</li>
<li><strong>Turn the dryer off</strong> if you leave home or when you go to bed.</li>
</ul>

<h3>At least once a year</h3>
<ul>
<li><strong>Clean the vent pipe.</strong> NFPA says to clean lint out of the vent pipe once a year, or more often if clothes are taking longer than normal to dry, or have a dryer lint removal service do it.</li>
<li><strong>Check the venting system</strong> behind the dryer to make sure it isn&rsquo;t damaged, crushed or restricted (USFA).</li>
<li><strong>Check the outdoor vent flap</strong> opens when the dryer is running, and isn&rsquo;t covered by snow in winter (NFPA).</li>
</ul>

<h3>Installation and setup</h3>
<ul>
<li><strong>Have your dryer installed and serviced by a professional</strong>, as both NFPA and USFA recommend.</li>
<li><strong>Use metal venting.</strong> NFPA recommends rigid or flexible metal venting material to keep proper airflow and drying time.</li>
<li><strong>Gas dryers</strong> should be inspected by a qualified professional to make sure the gas line and connection are intact and free of leaks.</li>
<li><strong>Electrical:</strong> dryers should be properly grounded, with the right plug and outlet, and connected properly.</li>
</ul>
<p>USFA&rsquo;s report also notes that many newer homes put laundry in upstairs bedrooms, hallways or closets, which can mean longer vent runs to reach an outside wall. Long or winding vents collect more lint, so they deserve extra attention.</p>

<h3>Around the dryer</h3>
<ul>
<li>Keep the area clear of things that can burn, like boxes, cleaning supplies and clothing.</li>
<li>Clothes that have touched flammable substances such as gasoline, paint thinner or similar solvents should be laid outside to dry first, then washed and dried as usual.</li>
</ul>

<h2>Warning signs</h2>
<p>NFPA&rsquo;s clearest warning sign is a load that&rsquo;s <strong>taking longer than normal to dry</strong>. That usually means air isn&rsquo;t moving through the vent the way it should, and it&rsquo;s time to clean the vent pipe. A dryer that has slowed down isn&rsquo;t just wasting energy; it&rsquo;s telling you lint has built up somewhere.</p>

<h2>Winter matters most</h2>
<p>USFA found residential dryer fires happen more often in fall and winter, peaking in January. More laundry, heavier clothes and longer drying times add up, and in Utah, snow can block an outdoor vent flap. A winter check of the vent flap and a vent cleaning before the cold months are cheap insurance.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>Clean the lint filter every load, and never run the dryer without one.</li>
<li>Clean the vent pipe at least once a year, or whenever drying slows down.</li>
<li>Use metal venting, and check that the outside flap opens and isn&rsquo;t snowed in.</li>
<li>Turn the dryer off when you leave or go to bed.</li>
</ul>

<p>ASI Appliance Service repairs and maintains dryers and other major appliances across metro Salt Lake City, Ogden, Provo and Tooele. Call <a href="tel:+18014878591">(801) 487-8591</a> for same or next-day service.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>National Fire Protection Association, <a href="https://www.nfpa.org/-/media/project/storefront/catalog/files/safety-tip-sheets/dryersafetytips.pdf" rel="noopener">Clothes Dryer Safety</a> (tip sheet)</li>
<li>NFPA Research, <a href="https://content.nfpa.org/-/media/Project/Storefront/Catalog/Files/Research/NFPA-Research/US-Fire-Problem/Fire-causes/oswashersdryers.pdf" rel="noopener">Home Fires Involving Clothes Dryers and Washing Machines</a> (March 2017)</li>
<li>U.S. Fire Administration, <a href="https://www.usfa.fema.gov/downloads/pdf/publications/clothes_dryer_fire_safety_flyer.pdf" rel="noopener">Clothes Dryer Fire Safety</a> (flyer)</li>
<li>U.S. Fire Administration, <a href="https://www.usfa.fema.gov/downloads/pdf/statistics/v13i7.pdf" rel="noopener">Clothes Dryer Fires in Residential Buildings (2008&ndash;2010)</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Dryer fire safety", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Clothes Dryer Fire Safety: Clean the Lint | ASI Appliance",
                  "Failure to clean is the leading cause of dryer fires. NFPA and U.S. Fire Administration tips on lint filters, vent pipes, metal venting and winter checks.",
                  BODY, image="asi-mtn", alt="Salt Lake City in winter", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "Clothes dryer fire safety: the lint habit that matters most", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "ASI Appliance Service, Inc."}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
