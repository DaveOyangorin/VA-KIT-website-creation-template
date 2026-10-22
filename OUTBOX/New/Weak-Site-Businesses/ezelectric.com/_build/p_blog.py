"""New blog post for ezelectric.com (21 Oct 2026): winter electrical safety. Informational; doesn't compete with any service page.
Sources: NFPA "Home Fires Involving Heating Equipment" (2011-2015 data, as reported by OH&S, Jan 2018); CPSC news release
"Put Safety at the Top of Your List When Decorating this Holiday Season" (Dec 2017). No claims about EZ Electric beyond its own pages."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/winter-electrical-safety-utah/"
H1 = "Winter electrical safety in Utah: space heaters, holiday lights and extension cords"
FAQ = [("Can I plug a space heater into an extension cord or power strip?", "No. Plug a space heater straight into a wall outlet, and plug only one heat-producing appliance into an outlet at a time. That&rsquo;s standard fire-safety guidance from the NFPA."),
       ("How far should a space heater be from furniture and curtains?", "At least three feet from anything that can burn: bedding, curtains, furniture, paper, clothes. Keep kids and pets out of that three-foot zone too."),
       ("Do outdoor holiday lights need a GFCI?", "The CPSC says to plug outdoor lights only into a GFCI-protected outlet or a portable GFCI, and to use lights labeled for outdoor use."),
       ("Why does my breaker trip when I run a space heater?", "Space heaters draw a lot of current. If the heater shares a circuit with other loads, the breaker may trip to protect the wiring. Don&rsquo;t keep resetting it: move the heater to another circuit, or have an electrician look at the circuit.")]
BODY = f'''<p class="answer">Heating fires peak in December, January and February, and space heaters cause most of the deaths. Keep heaters three feet from anything that can burn, plug them straight into the wall, and turn them off when you leave the room. For holiday lights, inspect every strand, use outdoor-rated lights on a GFCI outside, and don&rsquo;t overload cords.</p>

<p>Utah winters bring two things that put extra load on a home&rsquo;s wiring: space heaters in cold basements and drafty rooms, and strings of lights along rooflines and porches. Both are safe when they&rsquo;re used the right way, and both cause fires every year when they aren&rsquo;t. Here&rsquo;s what national fire and product-safety agencies recommend.</p>

<h2>Space heaters: the biggest winter risk</h2>
<p>The National Fire Protection Association (NFPA) tracks home fires involving heating equipment. In its report covering 2011 through 2015, portable and stationary space heaters were involved in <strong>43% of home heating fires</strong>, but <strong>85% of home heating fire deaths</strong>. December, January and February are the leading months for heating fires. The most common factor in fatal heating fires was simple: the heater was too close to something that could burn. That factor alone was behind <strong>53% of home heating fire deaths</strong>.</p>

<h3>The NFPA&rsquo;s space heater rules</h3>
<ul>
<li><strong>Three feet of clearance.</strong> Keep anything that can burn (bedding, curtains, sofas, paper, laundry) at least three feet from a space heater. Keep children and pets out of that zone.</li>
<li><strong>Turn it off</strong> when you leave the room or go to sleep.</li>
<li><strong>One heater per outlet.</strong> Plug only one heat-producing appliance into an outlet at a time.</li>
<li><strong>Never heat the house with the oven.</strong></li>
<li><strong>Carbon monoxide alarms.</strong> Install and maintain CO alarms, especially if you have any fuel-burning heater, furnace or fireplace.</li>
<li><strong>Yearly inspection.</strong> Have heating equipment and chimneys cleaned and inspected every year by a qualified professional.</li>
</ul>

<h3>Why the outlet matters</h3>
<p>A typical space heater draws close to the full capacity of a standard 15-amp household circuit. That&rsquo;s why the cord and plug can get warm, and why plugging a heater into a power strip or a light-duty extension cord is a bad idea: the strip or cord can overheat long before a breaker reacts. Plug the heater directly into a wall outlet. If the plug, cord or outlet ever feels hot, or the outlet is discolored, stop using it and have it checked.</p>

<h2>Holiday lights and decorations</h2>
<p>The U.S. Consumer Product Safety Commission (CPSC) estimates that holiday decorating sends about <strong>14,700 people</strong> to emergency rooms each season, an average of about 240 a day across November and December. Many of those are falls from ladders and roofs. The CPSC also counted, on average, about <strong>100 Christmas tree fires</strong> a year from 2012 to 2014. The CPSC&rsquo;s electrical advice:</p>
<ul>
<li><strong>Use tested lights.</strong> Only use lights tested for safety by a nationally recognized testing laboratory.</li>
<li><strong>Inspect every set</strong>, new or old, for broken or cracked sockets, frayed or bare wires and loose connections. Throw out damaged sets rather than taping them.</li>
<li><strong>Outdoor lights outdoors.</strong> Use lights labeled for outdoor use, and plug them only into a GFCI-protected receptacle or a portable GFCI.</li>
<li><strong>No electric lights on a metallic tree.</strong></li>
<li><strong>Check extension cords.</strong> Make sure each cord is rated for how you&rsquo;re using it and is in good condition, with no cuts or fraying.</li>
</ul>

<h3>Don&rsquo;t overload the circuit</h3>
<p>Big outdoor displays add up. Several strands of older incandescent lights, an inflatable or two and a fountain heater can easily overload one outdoor circuit. That&rsquo;s when breakers trip on the coldest night of the year. LED strands use a fraction of the power, so switching saves load as well as electricity. If you light up every year, a dedicated outdoor circuit or a few weather-resistant GFCI outlets where you actually need them beats a web of extension cords across the lawn. EZ Electric installs outdoor-rated outlets and circuits; see <a href="@/outdoor-specialty-electrical-services/">outdoor &amp; specialty services</a>.</p>

<h2>Extension cords: temporary means temporary</h2>
<ul>
<li>Use cords rated for the load and the location. Outdoor cords are marked for outdoor use.</li>
<li>Don&rsquo;t run cords under rugs or through doorways, where they get crushed and overheat unseen.</li>
<li>Don&rsquo;t daisy-chain cords or power strips.</li>
<li>If you use the same extension cord in the same spot every winter, that&rsquo;s a sign you need an outlet there.</li>
</ul>

<h2>Signs your wiring needs attention this winter</h2>
<p>Winter load exposes weak spots. Call an electrician if you notice:</p>
<ul>
<li>Breakers that trip repeatedly, or a circuit that only trips when a heater runs</li>
<li>Lights that dim or flicker when something turns on</li>
<li>Outlets or switch plates that are warm to the touch, buzz or are discolored</li>
<li>A burning smell with no obvious source</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Questions about a circuit, an outlet or adding power for the season? Call EZ Electric at <a href="tel:+13852840394">(385) 284-0394</a> for a free quote, Monday to Friday, 8 AM to 6 PM.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>National Fire Protection Association, <i>Home Fires Involving Heating Equipment</i> (2011&ndash;2015 data), as reported in <a href="https://ohsonline.com/articles/2018/01/11/nfpa-releases-report-on-home-fires-involving-heating-equipment.aspx" rel="noopener">&ldquo;Space Heaters Account for 43 Percent of U.S. Home Heating Fires, NFPA Reports&rdquo;</a>, Occupational Health &amp; Safety (January 2018)</li>
<li>U.S. Consumer Product Safety Commission, <a href="https://cpsc.gov/Newsroom/News-Releases/2018/Put-Safety-at-the-Top-of-Your-List-When-Decorating-this-Holiday-Season" rel="noopener">Put Safety at the Top of Your List When Decorating this Holiday Season</a> (December 2017)</li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Winter electrical safety", H1, "From the blog &middot; Oct 21, 2026", "Blog", "Winter Electrical Safety in Utah: Heaters &amp; Lights | EZ",
                  "Heating fires peak in winter. Space heater rules, holiday light and extension cord safety from the NFPA and CPSC, and the warning signs to call an electrician.",
                  BODY, image="ez-landscape-lighting", alt="Outdoor lighting glowing at dusk in Utah", crumbs=[], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "EZ Electric"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
