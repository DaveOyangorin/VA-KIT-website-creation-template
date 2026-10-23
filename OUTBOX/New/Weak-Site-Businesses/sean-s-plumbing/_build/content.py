"""Sean's Plumbing (South Jordan): "Hard water". Lake teal on deep blue, chalk-white scale, Outfit. Signature: a water hardness converter
(grains per gallon or mg/L -> USGS class, with a scale ring that thickens). Post: hard water explained (USGS Water Science School).
Banner: Oquirrh Lake in Daybreak, South Jordan (Dean Derhak, CC BY-SA 3.0). Facts: Google listing only."""
LAYOUT = "low"
CITY = "South Jordan"
TRADE = "Plumber"
LABEL = "South Jordan, Utah &middot; Redwood Rd"
H1 = "Plumber in South Jordan, <em>Sean&rsquo;s Plumbing.</em>"
LEDE = "Sean&rsquo;s Plumbing is a plumber in South Jordan, Utah, at 10330 S Redwood Rd #5230. Drips, clogs, scale and everything in between: call and talk to Sean&rsquo;s."
HERO_ALT = "Oquirrh Lake and the homes of Daybreak in South Jordan below snow-capped mountains"
CREDIT = "Oquirrh Lake, Daybreak &middot; Dean Derhak, CC BY-SA 3.0, via Wikimedia Commons"
SIG_BTN = "Check your water hardness"
INTRO_LABEL = "Plumber"
INTRO_H2 = "What&rsquo;s in <em>the water.</em>"
INTRO = ["Sean&rsquo;s Plumbing works from Redwood Road in South Jordan. When you call, a little detail goes a long way: where the problem is, how long it&rsquo;s been happening, and what you see.",
         "White crust on faucets and shower heads, spots on glasses and scale in the water heater all come from the same thing: hard water. Your water report or a test strip gives you a number. The converter below tells you what it means."]
SIG_LABEL = "Water hardness converter"
SIG_H2 = "How hard <em>is your water?</em>"
SIG_LEDE = "Enter the hardness from your water report or a test kit, in grains per gallon or milligrams per liter. We&rsquo;ll place it on the U.S. Geological Survey&rsquo;s scale."
SIG_HTML = '''<div class="tool-grid hard" data-hard>
<div class="hd-pipe" aria-hidden="true"><svg viewBox="0 0 200 200"><circle class="hd-wall" cx="100" cy="100" r="88"/><circle class="hd-scale" data-scale cx="100" cy="100" r="80"/><circle class="hd-water" data-water cx="100" cy="100" r="76"/></svg><p class="hd-cls" data-cls>Hard</p></div>
<div class="tool-in"><label for="hd-v">Hardness</label><input type="number" id="hd-v" inputmode="decimal" min="0" value="10" data-v>
<div class="chips" role="radiogroup" aria-label="Units"><label class="chip"><input type="radio" name="hd-u" value="gpg" checked><span>grains per gallon</span></label><label class="chip"><input type="radio" name="hd-u" value="mgl"><span>mg/L (ppm)</span></label></div>
<div class="hd-bar" aria-hidden="true"><i style="--w:25%">Soft</i><i style="--w:25%">Moderate</i><i style="--w:25%">Hard</i><i style="--w:25%">Very hard</i><b data-pin></b></div></div>
<div class="tool-out" aria-live="polite" data-out><p class="mono">171 mg/L as calcium carbonate</p><h3>Hard</h3><p></p></div>
<p class="small tool-src">USGS classes (mg/L as calcium carbonate): soft 0&ndash;60, moderately hard 61&ndash;120, hard 121&ndash;180, very hard over 180. Conversion: 1 grain per gallon = 17.1 mg/L. Nothing you type leaves this page.</p>
</div>'''
TIPS_LABEL = "What hardness does"
TIPS_H2 = "Four signs <em>of hard water</em>"
TIPS_LINK = "Hard water, explained"
TIPS = [("Soap scum", "USGS: calcium reacts with soap to form soap scum, so you need more soap and detergent for hands, hair and laundry."),
        ("Spots on dishes", "Spots and film on glassware are hard-water residue. USGS calls them unsightly but not dangerous."),
        ("Scale in the water heater", "Heating hard water forms calcium carbonate deposits that USGS says can shorten equipment life, raise heating costs and lower the efficiency of electric water heaters."),
        ("Narrowing pipes", "Over time, USGS says scale can build up inside pipes, reducing water flow and pressure.")]
TIPS_SRC = "Source: U.S. Geological Survey, Water Science School, &ldquo;Hardness of Water&rdquo; (updated August 24, 2026). USGS: hardness is not a health concern, but it can be a nuisance."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is Sean&rsquo;s Plumbing?", "<p>10330 S Redwood Rd #5230, South Jordan, UT 84095.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+14358506314">435-850-6314</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("Is hard water safe to drink?", "<p>The U.S. Geological Survey says hardness is not a health concern, but it can be a nuisance, mainly through soap scum and scale.</p>"),
       ("How do I convert grains per gallon to mg/L?", "<p>Multiply by 17.1. For example, 10 grains per gallon is about 171 mg/L, which USGS classes as hard.</p>")]
POST_BLURB = "What USGS says hardness is, how it&rsquo;s measured, and what it does to fixtures and water heaters."
TITLE = "Plumber in South Jordan, Utah | Sean's Plumbing, Redwood Rd"
META = "Sean's Plumbing: plumber at 10330 S Redwood Rd, South Jordan, Utah. Call 435-850-6314. Find out how hard your water is with our free USGS hardness converter."
CONTACT_LEDE = "South Jordan, Utah."
CONTACT_TITLE = "Contact Sean's Plumbing | Plumber in South Jordan, Utah"
CONTACT_META = "Contact Sean's Plumbing at 10330 S Redwood Rd #5230, South Jordan, UT 84095. Call 435-850-6314 or send the form about a plumbing problem at your home."
BEFORE = ["If water is actively leaking, turn off the main water shutoff first.", "Note where the problem is and how long it&rsquo;s been happening.", "A photo of the problem helps."]
CTA_TITLE = "A plumbing problem? <em>Call Sean&rsquo;s.</em>"
CTA_TEXT = "Call Sean&rsquo;s Plumbing at 435-850-6314. 10330 S Redwood Rd #5230, South Jordan, UT 84095."
SIDE_TITLE = "Plumbing in South Jordan."
BLURB = "Sean&rsquo;s Plumbing: a plumber at 10330 S Redwood Rd in South Jordan, Utah."
SVC = [("#tool", "Water hardness converter", None), ("hard-water-explained/", "Hard water, explained", None)]
NAV = [("Hardness converter", "#tool"), ("Hard water", "hard-water-explained/"), ("Contact", "contact/")]
