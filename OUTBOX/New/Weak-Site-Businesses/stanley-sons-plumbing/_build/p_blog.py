"""New post (23 Oct 2026): water heater temperature and 120 F. Informational; doesn't target "plumber salt lake city" or water heater
repair. Sources: CPSC Publication 5098, "Avoiding Tap Water Scalds"; U.S. Department of Energy FEMP, "Home Energy Checklist"."""
from engine import faq_html, faq_ld, canon

SLUG = "water-heater-temperature-120-degrees/"
H1 = "What temperature should your water heater be? Why CPSC says 120&deg;F"
FAQ = [("What is the recommended water heater temperature?", "The U.S. Consumer Product Safety Commission urges all users to lower water heaters to 120&deg;F. The Department of Energy&rsquo;s home checklist calls 120&deg;F the warm setting."),
       ("How fast can hot tap water burn?", "CPSC says most adults suffer third-degree burns in 2 seconds at 150&deg;F, 6 seconds at 140&deg;F, 30 seconds at 130&deg;F, and as little as 5 minutes at 120&deg;F."),
       ("How do I check my water temperature?", "CPSC suggests holding a candy or meat thermometer under the faucet, first thing in the morning or at least two hours after hot water use, then adjusting and re-checking."),
       ("Will lowering the temperature save money?", "CPSC says lowering it to 120&deg;F conserves energy and saves money as well as preventing scalds. DOE notes water heating can be 14% to 25% of home energy use."),
       ("Should I wait before adjusting an electric water heater?", "Yes. CPSC says hot water should not be used for at least two hours before setting the thermostat, and the power should be shut off at the breaker or fuse before you open the access panels."),
       ("Will turning down the water temperature affect my heat?", "For homes that heat water through the furnace or boiler, CPSC says reducing the water temperature will not affect the heating capacity of the furnace. Contact your fuel supplier to have it lowered.")]
BODY = f'''<p class="answer">Set your water heater to 120&deg;F. The U.S. Consumer Product Safety Commission (CPSC) urges every household to do so, because hotter water burns fast: most adults suffer third-degree burns in 2 seconds at 150&deg;F and 6 seconds at 140&deg;F. Check the real temperature at the tap with a thermometer, since dial settings aren&rsquo;t precise.</p>

<p>The water heater is easy to forget. It sits in a closet or the basement and quietly does its job, often at whatever temperature it was set to when it was installed. That setting matters for two reasons: safety, especially for young children and older adults, and the energy bill. Here&rsquo;s what CPSC and the U.S. Department of Energy (DOE) say.</p>

<h2>Why 120&deg;F</h2>
<p>CPSC&rsquo;s guidance, &ldquo;Avoiding Tap Water Scalds,&rdquo; is short and direct. It urges all users to lower their water heaters to 120 degrees Fahrenheit, and notes that a thermostat setting of 120&deg;F may be necessary for residential water heaters to reduce or eliminate the risk of most tap water scald injuries. It adds that the lower temperature also conserves energy and saves money.</p>
<p>DOE&rsquo;s Home Energy Checklist makes the same recommendation from the energy side: turn down the temperature of your water heater to the warm setting, 120&deg;F, to save energy and avoid scalding. It notes that water heating can account for 14% to 25% of home energy use.</p>

<h2>How fast hot water burns</h2>
<p>CPSC gives these exposure times for third-degree burns in most adults:</p>
<ul>
<li><strong>150&deg;F:</strong> 2 seconds</li>
<li><strong>140&deg;F:</strong> 6 seconds</li>
<li><strong>130&deg;F:</strong> 30 seconds</li>
<li><strong>120&deg;F:</strong> 5 minutes</li>
</ul>
<p>The difference between 140&deg;F and 120&deg;F is the difference between a few seconds and a few minutes, which is often the time it takes to notice, react or get a child out of a bath. Our <a href="@/#tool">water heater thermometer</a> shows each setting side by side.</p>

<h2>Who is most at risk</h2>
<p>CPSC says the majority of injuries and deaths involving tap water scalds are to the elderly and children under the age of five. Even at 120&deg;F, it reminds parents that a five-minute exposure could result in third-degree burns, and it&rsquo;s blunt about supervision: never take hot water temperature for granted, always hand-test before using, especially when bathing infants and young children, and never leave a child unsupervised in the bathroom, even for a second.</p>

<h2>How to check your temperature</h2>
<p>Most water heater dials don&rsquo;t show exact temperatures, so CPSC&rsquo;s approach is to measure at the faucet:</p>
<ol>
<li>Wait until hot water hasn&rsquo;t been used for a while: first thing in the morning, or at least two hours after the last use.</li>
<li>Run hot water at a faucet and hold a candy or meat thermometer under the stream.</li>
<li>If the reading is too high, adjust the thermostat following the manufacturer&rsquo;s instructions.</li>
<li>Check again with the thermometer after the heater has had time to recover.</li>
</ol>

<h2>Adjusting by heater type</h2>
<h3>Electric water heaters</h3>
<p>CPSC says you can call your local electric company, some of which offer to adjust the thermostat at no charge. To do it yourself, it says to avoid using hot water for at least two hours before setting, then shut off the power by turning off the circuit breaker or removing the fuse that serves the heater. Most electric water heaters have two thermostats, upper and lower, behind access panels, and both must be set to a common temperature for proper operation. Follow the instructions that came with the appliance.</p>
<h3>Gas water heaters</h3>
<p>Because gas thermostats differ, CPSC suggests calling your local gas company for instructions. Where the dial doesn&rsquo;t give precise temperatures, use the thermometer method above and adjust according to the manufacturer&rsquo;s instructions.</p>
<h3>Other systems</h3>
<p>If you don&rsquo;t have a separate electric, gas or oil-fired water heater, CPSC says you probably have a system heated through the furnace or boiler; contact your fuel supplier to have the temperature lowered. Apartment residents should talk to the building manager.</p>

<h2>Small energy savers while you&rsquo;re there</h2>
<p>DOE&rsquo;s checklist suggests checking whether your water heater has an insulating blanket, which it says pays for itself in about a year, and insulating your hot water pipes to prevent heat loss.</p>

<h2>When to call a plumber</h2>
<p>If you can&rsquo;t reach the controls safely, the readings don&rsquo;t match the setting, the water never gets hot or the heater is leaking, it&rsquo;s time for a professional. Don&rsquo;t open electrical access panels with the power on.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Water heater questions on the east side of the Salt Lake Valley? Call Stanley &amp; Sons Plumbing at <a href="tel:+13853337488">385-333-7488</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. Consumer Product Safety Commission, <a href="https://www.cpsc.gov/s3fs-public/5098-Tap-Water-Scalds.pdf" rel="noopener">Avoiding Tap Water Scalds</a> (Publication 5098)</li>
<li>U.S. Department of Energy, Federal Energy Management Program, <a href="https://www.energy.gov/cmei/femp/home-energy-checklist" rel="noopener">Home Energy Checklist</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Big Cottonwood Canyon Road &middot; Famartin, CC BY-SA 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Water heater temperature", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Water Heater Temperature: Why 120&deg;F | Stanley &amp; Sons",
                  "What temperature your water heater should be: CPSC urges 120&deg;F. Burn times at 130, 140 and 150 degrees, and how to check and adjust yours safely at home.",
                  BODY, image="hero", alt="Big Cottonwood Canyon Road", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1.replace("&deg;", "°"), "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
