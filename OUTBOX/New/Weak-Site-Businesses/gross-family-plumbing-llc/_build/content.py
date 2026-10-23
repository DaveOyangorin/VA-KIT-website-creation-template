"""Gross Family Plumbing LLC (Salt Lake City, Research Way): "Every flush". Field green on deep green, Sora; clean, numeric. Signature:
a toilet water calculator (household size, flushes, current gallons per flush vs a WaterSense 1.28 gpf model -> gallons a year), plus
WaterSense's 10-minute dye test. Post: when to replace a toilet (EPA WaterSense residential toilets + Fix a Leak Week).
Banner: Salt Lake City skyline and the Wasatch (Invictus323, CC BY 4.0). Facts: Google listing only."""
LAYOUT = "split"
CITY = "Salt Lake City"
TRADE = "Plumber"
LABEL = "Salt Lake City &middot; Research Way"
H1 = "Plumber in Salt Lake City, <em>the Gross family.</em>"
LEDE = "Gross Family Plumbing LLC is a plumber in Salt Lake City, at 1750 Research Way #3600. A running toilet, a slow drain, a leak under the sink: call and talk to the family."
HERO_ALT = "The Salt Lake City skyline in front of the snow-capped Wasatch Range"
CREDIT = "Salt Lake City skyline &middot; Invictus323, CC BY 4.0, via Wikimedia Commons"
SIG_BTN = "See what your toilet uses"
INTRO_LABEL = "Plumber"
INTRO_H2 = "Small leaks, <em>big numbers.</em>"
INTRO = ["Gross Family Plumbing LLC works from Research Way on Salt Lake City&rsquo;s west side, with a family name on the business.",
         "Toilets are the biggest water user inside a typical home, nearly 30 percent of indoor use according to EPA WaterSense. Older ones can use as much as 6 gallons a flush. The calculator below shows what that adds up to in your house."]
SIG_LABEL = "Toilet water calculator"
SIG_H2 = "What does <em>every flush cost?</em>"
SIG_LEDE = "Pick your toilet&rsquo;s gallons per flush (it&rsquo;s often stamped behind the seat), set your household, and compare with a WaterSense-labeled toilet at 1.28 gallons."
SIG_HTML = '''<div class="tool-grid flush" data-flush>
<div class="fl-tank" aria-hidden="true"><div class="fl-col"><i data-a></i><span>Now</span></div><div class="fl-col ws"><i data-b></i><span>WaterSense</span></div></div>
<div class="tool-in">
<fieldset><legend>Your toilet</legend><div class="chips">
<label class="chip"><input type="radio" name="fl-g" value="6"><span>Older: up to 6 gpf</span></label><label class="chip"><input type="radio" name="fl-g" value="3.5" checked><span>3.5 gpf</span></label><label class="chip"><input type="radio" name="fl-g" value="1.6"><span>1.6 gpf (federal standard)</span></label></div></fieldset>
<label for="fl-p">People in the home</label><input type="number" id="fl-p" inputmode="numeric" min="1" max="20" value="4" data-p>
<label for="fl-f">Flushes per person per day (your estimate)</label><input type="number" id="fl-f" inputmode="numeric" min="0" max="30" value="5" data-f>
</div>
<div class="tool-out" aria-live="polite" data-out><p class="mono"></p><h3></h3><p></p></div>
<p class="small tool-src">Figures: EPA WaterSense, &ldquo;Residential Toilets&rdquo; (updated May 29, 2026): older toilets can use as much as 6 gallons per flush; the federal standard is 1.6; WaterSense-labeled toilets use 1.28 or less. Flushes per day are your own estimate. Nothing you type leaves this page.</p>
</div>'''
TIPS_LABEL = "The 10-minute dye test"
TIPS_H2 = "Is your toilet <em>leaking right now?</em>"
TIPS_LINK = "When to replace a toilet"
TIPS = [("Add color", "WaterSense: put a few drops of food coloring in the toilet tank."),
        ("Don&rsquo;t flush", "Wait 10 minutes without using the toilet."),
        ("Check the bowl", "If any color shows up in the bowl, the toilet is leaking from the tank."),
        ("Flush after", "Flush right away when the test is done so the coloring doesn&rsquo;t stain the tank.")]
TIPS_SRC = "Source: EPA WaterSense, Fix a Leak Week (updated March 13, 2026): the average household&rsquo;s leaks can waste more than 9,300 gallons a year."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is Gross Family Plumbing?", "<p>1750 Research Way #3600, Salt Lake City, UT 84119.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+13853311988">385-331-1988</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("How much water does a toilet use?", "<p>EPA WaterSense says older toilets can use as much as 6 gallons per flush, the federal standard is 1.6, and WaterSense-labeled toilets use 1.28 gallons or less.</p>"),
       ("How much could a new toilet save?", "<p>WaterSense estimates replacing old toilets with labeled models could cut toilet water use by 20 to 60 percent, nearly 13,000 gallons a year for a home.</p>")]
POST_BLURB = "What WaterSense says about old toilets, the 1.28-gallon label, and the dye test for leaks."
TITLE = "Plumber in Salt Lake City, UT | Gross Family Plumbing LLC"
META = "Gross Family Plumbing LLC: plumber at 1750 Research Way, Salt Lake City. Call 385-331-1988. See how much water your toilet uses with our WaterSense calculator."
CONTACT_LEDE = "Salt Lake City, Utah."
CONTACT_TITLE = "Contact Gross Family Plumbing LLC | Salt Lake City, Utah"
CONTACT_META = "Contact Gross Family Plumbing LLC at 1750 Research Way #3600, Salt Lake City, UT 84119. Call 385-331-1988 or send the form about any plumbing problem at home."
BEFORE = ["If water is actively leaking, turn off the main water shutoff, or the valve behind the toilet.", "Note where the problem is and how long it&rsquo;s been happening.", "A photo of the problem helps."]
CTA_TITLE = "A plumbing problem? <em>Call the Gross family.</em>"
CTA_TEXT = "Call Gross Family Plumbing LLC at 385-331-1988. 1750 Research Way #3600, Salt Lake City, UT 84119."
SIDE_TITLE = "Plumbing in Salt Lake City."
BLURB = "Gross Family Plumbing LLC: a plumber at 1750 Research Way in Salt Lake City, Utah."
SVC = [("#tool", "Toilet water calculator", None), ("when-to-replace-a-toilet/", "When to replace a toilet", None)]
NAV = [("Toilet calculator", "#tool"), ("Replacing a toilet", "when-to-replace-a-toilet/"), ("Contact", "contact/")]
