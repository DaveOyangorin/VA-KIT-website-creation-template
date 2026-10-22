"""New blog post for stgeorgehomeservices.com (their 34 guides live at /guides/...; the new post sits at /blog/... so no guide
URL changes). "What temperature should your water heater be set to? 120, 140, and the trade-off in between"
Main phrase: "water heater temperature setting" (informational). No service page or guide targets it: the water heater service
pages are about installs, flushing and descaling; the guides cover hard water, thermal expansion, strapping and heat pump units.
It links to the hard-water guide, water heater flush, tankless descaling, recirculation pump and expansion tank pages.
Facts and sources, checked 20 Oct 2026 (fetched and read):
- U.S. CPSC, "Avoiding Tap Water Scalds", Publication 5098 (https://www.cpsc.gov/s3fs-public/5098.pdf): CPSC urges lowering water
  heaters to 120°F; most adults suffer third-degree burns from 150°F water in two seconds, 140°F in six seconds, 130°F in thirty
  seconds, and even 120°F with a five-minute exposure; the majority of tap water scald injuries and deaths are to the elderly and
  children under five; electric heaters usually have two thermostats, both set to a common temperature, power off at the breaker
  before opening the access panels; check with a candy or meat thermometer at the faucet first thing in the morning or at least
  two hours after hot water use; set the lowest temperature that satisfies the household's needs; always hand-test before
  bathing infants and young children.
- OSHA, "Legionellosis: Control and Prevention" (https://www.osha.gov/legionnaires-disease/control-prevention): ideal temperature
  range for Legionella growth 68-122°F (20-50°C); water heaters maintained below 140°F (60°C) that contain scale and sediment may
  foster Legionella growth; stagnant dead legs and non-recirculated lines also promote growth; controls include storing hot water
  at a minimum of 140°F and delivering at least 122°F to outlets (OSHA's page covers commercial, industrial and multi-family
  settings), draining tanks periodically to remove scale and sediment, and flushing infrequently used lines.
- WHO, "Legionellosis" fact sheet (6 Sept 2022, https://www.who.int/news-room/fact-sheets/detail/legionellosis): keep hot water
  above 50°C, which requires water leaving the heating unit at or above 60°C, or treat with a biocide, particularly in hospitals,
  health care and aged-care settings; reduce stagnation by flushing unused taps.
- The client's own guide on St. George water (18-22 grains per gallon, very hard) and their water heater service pages.
No prices, no product claims."""
from engine import faq_html, faq_ld, canon, img
from cfg import U, NAME

POST = ("What Temperature Should Your Water Heater Be? 120, 140, and the Trade-Off", "blog/water-heater-temperature-setting/")
CPSC = "https://www.cpsc.gov/s3fs-public/5098.pdf"
OSHA = "https://www.osha.gov/legionnaires-disease/control-prevention"
WHO = "https://www.who.int/news-room/fact-sheets/detail/legionellosis"
FAQ = [("What temperature does the CPSC recommend for a water heater?", f'The U.S. Consumer Product Safety Commission urges lowering residential water heaters to 120°F to reduce the risk of tap water scalds (<a href="{CPSC}" rel="noopener">CPSC Publication 5098</a>).'),
       ("Is 120°F hot enough to prevent Legionella?", f'It is inside the range OSHA describes as ideal for Legionella growth, 68 to 122°F. OSHA and the WHO describe storing hot water at 140°F (60°C) as a control, mainly for larger and shared buildings. For a household with someone at higher risk, it is worth a conversation about storing hotter and limiting the temperature at the tap.'),
       ("How do I check my water temperature?", "CPSC&rsquo;s method: hold a candy or meat thermometer under the hot tap first thing in the morning, or at least two hours after anyone has used hot water, and adjust from there.")]


def post():
    return f'''<p class="answer">The short answer most homes get is 120°F. That is the setting the U.S. Consumer Product Safety Commission urges, because scalds are the injury that actually happens in houses. The longer answer is that a tank kept cooler, with scale and sediment in the bottom, is better at growing bacteria. Here is what each number protects against, and how to pick.</p>
<p>The dial on a water heater is one of the few settings in a house that trades one risk against another. Turn it up, and the water at the tap can burn. Turn it down too far, and the tank sits at a temperature some bacteria like. St. George adds a third factor: very hard water, which fills tanks with scale faster than most places.</p>
<h2>What 120°F protects against: scalds</h2>
<p>The <a href="{CPSC}" rel="noopener">CPSC&rsquo;s guidance on tap water scalds</a> is blunt about the numbers. Most adults will suffer third-degree burns from water at:</p>
<ul><li><b>150°F</b> in about two seconds,</li><li><b>140°F</b> in about six seconds,</li><li><b>130°F</b> in about thirty seconds,</li><li>and even <b>120°F</b>, with a five-minute exposure.</li></ul>
<p>The CPSC notes that most tap water scald injuries and deaths happen to older adults and to children under five: the people least able to pull away quickly. That is why its recommendation is to set residential water heaters to 120°F, and to use the lowest setting that still meets your household&rsquo;s needs. The same agency says to always hand-test the water before bathing a baby or a young child, whatever the setting.</p>
<h2>What 140°F protects against: bacteria in the tank</h2>
<p>The other side of the trade is Legionella, the bacterium behind Legionnaires&rsquo; disease. <a href="{OSHA}" rel="noopener">OSHA&rsquo;s guidance on Legionella control</a> gives its ideal growth range as 68 to 122°F, and warns that water heaters kept below 140°F that contain scale and sediment may foster its growth. Stagnant water makes it worse: lines that are rarely used, or plumbing that was capped off and left in place.</p>
<p>OSHA lists storing hot water at a minimum of 140°F, and delivering it at no less than 122°F to every outlet, among the controls for domestic hot water systems. The <a href="{WHO}" rel="noopener">World Health Organization</a> says much the same: keep hot water above 50°C (122°F), which means water leaving the heater at 60°C (140°F) or above, particularly in hospitals, care settings and aged-care facilities. Both are written mainly with larger and shared buildings in mind, but the biology inside a home tank is the same.</p>
<h2>The St. George factor: scale</h2>
<p>Here is where local water matters. The City of St. George tells residents to set softeners to 18 grains per gallon, with a maximum of 22, which the U.S. Geological Survey scale classes as very hard. We cover what that does to tanks and tankless units in <a href="@/guides/hard-water-and-water-heaters/">what St. George water does to a water heater</a>. The short version: hard water leaves scale and sediment in the bottom of a tank, and OSHA names scale and sediment as part of what lets bacteria grow in a cooler tank.</p>
<p>So in this valley, the temperature setting and the maintenance belong in the same conversation. A tank that gets <a href="@/services/water-heater-flush/">flushed</a> on schedule, with softened or treated water feeding it, is in a very different state from one that has never been drained.</p>
<h2>How to choose a setting for your house</h2>
<p>There is no single right number for every home. A few honest questions get you most of the way:</p>
<ul><li><b>Who lives here?</b> Young children, or an older adult who might not react quickly in a shower, push the case for 120°F at the tap.</li>
<li><b>Is anyone at higher risk from infection?</b> If someone in the house has a weakened immune system or chronic lung disease, ask your doctor about Legionella risk; it may tip the balance toward storing hotter.</li>
<li><b>How much do you use?</b> A tank in a part-time house, or one serving a bathroom nobody uses, sits stagnant. Running unused taps regularly helps, and a <a href="@/services/recirculation-pump/">recirculation pump</a> changes how water moves through the lines.</li>
<li><b>When was the tank last drained?</b> Scale and sediment matter on either side of this trade.</li></ul>
<p>Some households get both: they store water hotter and fit a tempering (mixing) valve, so water at the taps comes out cooler. Whether that suits your setup depends on the heater, the plumbing and who lives there, so it is worth asking whoever services the heater.</p>
<h2>How to check and adjust it</h2>
<ol><li><b>Measure first.</b> The CPSC&rsquo;s method is the simplest: hold a candy or meat thermometer under the hot tap first thing in the morning, or at least two hours after anyone has used hot water. The dial markings on many heaters are not degrees.</li>
<li><b>Electric tanks: power off.</b> Turn off the breaker before opening the access panels. Most electric tanks have two thermostats, upper and lower, and both should be set to the same temperature.</li>
<li><b>Gas tanks: follow the manual.</b> Thermostats differ between makers; adjust as the manufacturer&rsquo;s instructions say, then measure again after a few hours.</li>
<li><b>Tankless units</b> usually set an output temperature on a control panel. Hard water matters even more for these: see the guide above on manufacturer hardness limits, and <a href="@/services/tankless-descaling/">tankless descaling</a>.</li></ol>
<p>If turning the temperature up makes the tank&rsquo;s pressure relief valve drip, or you hear knocking after a change, don&rsquo;t keep adjusting: that can be a sign of <a href="@/guides/thermal-expansion/">thermal expansion</a> or a failing valve, and it should be looked at.</p>
<h2>What we&rsquo;d tell you on the phone</h2>
<p>If you&rsquo;re not sure what your heater is set to, or what it should be for your household, call us. There&rsquo;s no charge to explain the options. If it needs a visit, you&rsquo;ll be told the diagnostic fee on the call, before anyone is dispatched, and it comes off the job if you hire us. The quote is the number.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<h2>Where this comes from</h2>
<ol class="srcs"><li><a href="{CPSC}" rel="noopener">U.S. Consumer Product Safety Commission, &ldquo;Avoiding Tap Water Scalds,&rdquo; Publication 5098</a>.</li>
<li><a href="{OSHA}" rel="noopener">Occupational Safety and Health Administration, &ldquo;Legionellosis (Legionnaires&rsquo; Disease and Pontiac Fever): Control and Prevention&rdquo;</a>.</li>
<li><a href="{WHO}" rel="noopener">World Health Organization, &ldquo;Legionellosis&rdquo; fact sheet, 6 September 2022</a>.</li>
<li>Our own guide, <a href="@/guides/hard-water-and-water-heaters/">What St. George water does to a water heater</a>, and the City of St. George softener guidance it cites.</li></ol>'''


def pages(K):
    p = K.page(POST[1], "Water heater temperature", POST[0], f"By {NAME} &middot; October 20, 2026", "Blog", "Water Heater Temperature Setting: 120 vs 140°F | St. George",
               "What temperature to set a water heater: CPSC's 120°F for scalds, OSHA and WHO's 140°F for Legionella, St. George's hard water, and how to check and adjust it.",
               post(), image="work-tankless-interior-closet", alt="A wall-hung tankless water heater in a closet", crumbs=[("Blog", "blog/")], ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose doc post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/work-tankless-interior-closet.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    idx = K.page("blog/", "Blog", "Blog", "New notes from St. George Home Services. The long-form guides are in Guides.", "Blog", "Blog | St. George Home Services, St. George, Utah",
                 "New notes from St. George Home Services on plumbing, heating and air in St. George, Utah. For the long-form guides with sources, see the Guides section.",
                 f'<div class="posts one"><a class="post-card" href="@/{POST[1]}">{img("work-tankless-interior-closet", "")}<span class="pc-d">Oct 20, 2026</span><b>{POST[0]}</b><em>Read {K.ARROW}</em></a></div><p><a class="tlink" href="@/guides/">All the guides {K.ARROW}</a></p>')
    return [idx, p]
