"""Stanley & Sons Plumbing (Salt Lake City, Fort Union Blvd): "Hot line". Warm oxblood, tap-red and cool blue, Playfair Display: a family
name set like an old shop sign. Signature: a water-heater temperature thermometer with CPSC's time-to-burn figures (120/130/140/150 F).
Post: why 120 F (CPSC publication 5098, DOE/FEMP). Banner: Big Cottonwood Canyon Road, Cottonwood Heights (Famartin, CC BY-SA 4.0).
Facts: Google listing only."""
LAYOUT = "overlay"
CITY = "Salt Lake City"
TRADE = "Plumber"
LABEL = "Salt Lake City &middot; Fort Union Blvd"
H1 = "Plumber in Salt Lake City, <em>Stanley &amp; Sons.</em>"
LEDE = "Stanley &amp; Sons Plumbing is a plumber in Salt Lake City, at 2346 E Fort Union Blvd #7100. A leak, a clog, a water heater that&rsquo;s too hot or not hot enough: call and talk to the family."
HERO_ALT = "Big Cottonwood Canyon Road heading toward the mountains east of Cottonwood Heights"
CREDIT = "Big Cottonwood Canyon Road &middot; Famartin, CC BY-SA 4.0, via Wikimedia Commons"
SIG_BTN = "Check your water heater setting"
INTRO_LABEL = "Plumber"
INTRO_H2 = "A family name <em>on the business.</em>"
INTRO = ["Stanley &amp; Sons Plumbing works from Fort Union Boulevard, on the east side of the Salt Lake Valley, with a family name on the business.",
         "One of the simplest things in a house to get right is also one of the most overlooked: how hot the water heater is set. The thermometer below shows what the U.S. Consumer Product Safety Commission says each setting means for scalds."]
SIG_LABEL = "Water heater thermometer"
SIG_H2 = "How hot is <em>too hot?</em>"
SIG_LEDE = "Slide to your water heater&rsquo;s temperature. CPSC recommends 120&deg;F and gives the exposure times that cause third-degree burns at hotter settings."
SIG_HTML = '''<div class="tool-grid therm" data-therm>
<div class="th-wrap" aria-hidden="true"><div class="th-tube"><i data-merc></i><b style="bottom:0%">120&deg;</b><b style="bottom:33.3%">130&deg;</b><b style="bottom:66.6%">140&deg;</b><b style="bottom:100%">150&deg;</b></div><div class="th-bulb"></div></div>
<div class="tool-in"><label for="th-t">Water heater temperature: <b data-tv>120</b>&deg;F</label><input type="range" id="th-t" min="120" max="150" step="10" value="120" data-t>
<div class="th-scale"><span>120&deg;F</span><span>130&deg;</span><span>140&deg;</span><span>150&deg;F</span></div>
<p class="th-time"><span data-time>5 minutes</span><small>exposure for a third-degree burn, per CPSC</small></p></div>
<div class="tool-out" aria-live="polite" data-out><p class="mono">120&deg;F &middot; CPSC&rsquo;s recommendation</p><h3>The setting CPSC urges for every home.</h3><p></p></div>
<p class="small tool-src">Figures: U.S. Consumer Product Safety Commission, &ldquo;Avoiding Tap Water Scalds&rdquo; (Publication 5098): most adults suffer third-degree burns from 150&deg;F water in 2 seconds, 140&deg;F in 6 seconds, 130&deg;F in 30 seconds, and 120&deg;F in 5 minutes. Dial markings aren&rsquo;t precise; CPSC suggests checking at the tap with a thermometer.</p>
</div>'''
TIPS_LABEL = "Set it right"
TIPS_H2 = "Four steps <em>from CPSC and DOE</em>"
TIPS_LINK = "Why 120&deg;F is the number"
TIPS = [("Measure at the tap", "CPSC suggests holding a candy or meat thermometer under the faucet, first thing in the morning or at least two hours after hot water use."),
        ("Aim for 120&deg;F", "CPSC urges lowering water heaters to 120&deg;F; the Department of Energy&rsquo;s checklist calls it the warm setting and says it saves energy and prevents scalding."),
        ("Electric: two thermostats", "CPSC notes most electric water heaters have two thermostats, both set to the same temperature, behind access panels. Shut off the power at the breaker first."),
        ("Gas: follow the maker", "Gas thermostats differ, so CPSC says to follow the manufacturer&rsquo;s instructions or call your gas company, then re-check with the thermometer.")]
TIPS_SRC = "Sources: CPSC Publication 5098; U.S. Department of Energy, FEMP Home Energy Checklist."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is Stanley &amp; Sons Plumbing?", "<p>2346 E Fort Union Blvd #7100, Salt Lake City, UT 84121.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+13853337488">385-333-7488</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("What temperature should my water heater be?", "<p>The U.S. Consumer Product Safety Commission urges 120&deg;F. Even then, it says a five-minute exposure could cause third-degree burns, so always hand-test bath water for children.</p>"),
       ("Who is most at risk from scalds?", "<p>CPSC says most tap water scald injuries and deaths involve older adults and children under five.</p>")]
POST_BLURB = "What CPSC and the Department of Energy say about water heater settings, and how to check yours."
TITLE = "Plumber in Salt Lake City, UT | Stanley &amp; Sons Plumbing"
META = "Stanley &amp; Sons Plumbing: plumber at 2346 E Fort Union Blvd, Salt Lake City. Call 385-333-7488. See what your water heater temperature means for scalds."
CONTACT_LEDE = "Salt Lake City, Utah."
CONTACT_TITLE = "Contact Stanley &amp; Sons Plumbing | Salt Lake City, Utah"
CONTACT_META = "Contact Stanley &amp; Sons Plumbing at 2346 E Fort Union Blvd #7100, Salt Lake City, UT 84121. Call 385-333-7488 or send the form about a plumbing problem."
BEFORE = ["If water is actively leaking, turn off the main water shutoff first.", "For water heater problems, note whether it&rsquo;s gas or electric and roughly how old it is.", "A photo of the label on the water heater helps."]
CTA_TITLE = "Plumbing trouble? <em>Call Stanley &amp; Sons.</em>"
CTA_TEXT = "Call Stanley &amp; Sons Plumbing at 385-333-7488. 2346 E Fort Union Blvd #7100, Salt Lake City, UT 84121."
SIDE_TITLE = "Plumbing in Salt Lake City."
BLURB = "Stanley &amp; Sons Plumbing: a plumber at 2346 E Fort Union Blvd in Salt Lake City, Utah."
SVC = [("#tool", "Water heater thermometer", None), ("water-heater-temperature-120-degrees/", "Why 120&deg;F", None)]
NAV = [("Water heater temp", "#tool"), ("Why 120&deg;F", "water-heater-temperature-120-degrees/"), ("Contact", "contact/")]
