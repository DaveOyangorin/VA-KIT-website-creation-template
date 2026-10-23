"""RoofTek (Millcreek): "Pitch". Charcoal and safety orange, Archivo Black. Signature: a roof pitch calculator (rise over 12 -> angle, slope
factor, roof area and squares from a footprint). Pure geometry, no prices. Tips and post: IBHS FORTIFIED Roof upgrades (fortifiedhome.org).
Banner: Mount Olympus above Millcreek (Jeff McGrath, CC BY-SA 3.0). Facts: Google listing only."""
LAYOUT = "overlay"
CITY = "Millcreek"
TRADE = "Roofing contractor"
LABEL = "Millcreek, Utah &middot; 4080 S W Temple St"
H1 = "Roofing company in Millcreek, <em>built on pitch.</em>"
LEDE = "RoofTek is a roofing company in Millcreek, Utah, at 4080 S W Temple St. Leaks, storm damage, a roof that&rsquo;s seen better days: call and talk to a roofer."
HERO_ALT = "Mount Olympus rising above the Millcreek area of the Salt Lake Valley"
CREDIT = "Mount Olympus, Utah &middot; Jeff McGrath, CC BY-SA 3.0, via Wikimedia Commons"
SIG_BTN = "Work out your roof pitch"
INTRO_LABEL = "Roofing contractor"
INTRO_H2 = "The roof over <em>Millcreek.</em>"
INTRO = ["A roof is a system: the deck, the edges, the fasteners and the covering all have to hold together when wind and weather hit it. RoofTek is a roofing contractor based on S W Temple in Millcreek.",
         "When you call, it helps to know roughly how steep your roof is, how big the house is, and what you&rsquo;re seeing: missing shingles, a stain on a ceiling, water in the attic. The pitch calculator below gives you the first two in a couple of minutes."]
SIG_LABEL = "Roof pitch calculator"
SIG_H2 = "How steep <em>is your roof?</em>"
SIG_LEDE = "Roofers describe slope as rise over a 12-inch run: a 6/12 roof climbs 6 inches for every foot across. Set yours, add the home&rsquo;s footprint, and see the angle and roughly how much roof that really is."
SIG_HTML = '''<div class="tool-grid pitch" data-pitch>
<div class="pt-fig"><svg viewBox="0 0 320 200" role="img" aria-label="Roof profile at the chosen pitch"><line class="pt-base" x1="20" y1="170" x2="300" y2="170"/><polygon class="pt-roof" data-poly points="20,170 160,100 300,170"/><line class="pt-rise" data-rise x1="160" y1="170" x2="160" y2="100"/><text class="pt-lbl" data-plbl x="160" y="190" text-anchor="middle">6 / 12</text></svg></div>
<div class="tool-in">
<label for="pt-r">Rise per 12 inches of run: <b data-rv>6</b> inches</label><input type="range" id="pt-r" min="1" max="18" step="1" value="6" data-r>
<div class="pt-scale"><span>Low slope</span><span>Steep</span></div>
<label for="pt-f">Home footprint, square feet (optional)</label><input type="number" id="pt-f" inputmode="numeric" min="0" placeholder="e.g. 1800" data-f>
</div>
<div class="tool-out" aria-live="polite" data-out><p class="mono">6/12 pitch</p><h3>26.6&deg; roof angle</h3><p>Slope factor 1.118: every square foot of floor below is about 1.12 square feet of roof.</p></div>
<p class="small tool-src">Geometry only: angle = arctan(rise &divide; 12); slope factor = &radic;(rise&sup2; + 12&sup2;) &divide; 12. Real roofs add overhangs, valleys, dormers and waste, so a roofer measures before quoting. Nothing you type leaves this page.</p>
</div>'''
TIPS_LABEL = "What makes a roof stronger"
TIPS_H2 = "Four upgrades <em>from IBHS research</em>"
TIPS_LINK = "What a FORTIFIED roof is"
TIPS = [("Stronger edges", "The FORTIFIED Roof standard calls for a wider drip edge and a fully adhered starter strip, to help keep the edge of the roof covering from peeling up."),
        ("A sealed roof deck", "Sealing the seams of the roof deck can reduce water intrusion by up to 95% if the shingles blow off, according to IBHS."),
        ("Ring-shank nails", "IBHS says ring-shank nails in an enhanced pattern nearly double a roof&rsquo;s strength against wind compared with smooth nails."),
        ("Impact-rated shingles", "FORTIFIED&rsquo;s optional hail supplement requires asphalt shingles rated Good or Excellent in IBHS&rsquo;s hail impact ratings.")]
TIPS_SRC = "Source: Insurance Institute for Business &amp; Home Safety, FORTIFIED Roof (fortifiedhome.org). Ask any roofer whether they are FORTIFIED-trained."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is RoofTek?", "<p>4080 S W Temple St, Millcreek, UT 84107.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+18014712054">801-471-2054</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("What does 6/12 pitch mean?", "<p>The roof rises 6 inches for every 12 inches of horizontal run, an angle of about 26.6 degrees. The calculator above converts any pitch.</p>"),
       ("What is a FORTIFIED roof?", "<p>A roofing standard from the Insurance Institute for Business &amp; Home Safety (IBHS) that adds stronger edges, a sealed deck and ring-shank nails, verified by an independent evaluator.</p>")]
POST_BLURB = "What IBHS&rsquo;s FORTIFIED Roof standard adds to a re-roof, and how a home earns the designation."
TITLE = "Roofing Company in Millcreek, Utah | RoofTek Roofing"
META = "RoofTek: roofing company at 4080 S W Temple St, Millcreek, Utah. Call 801-471-2054. Work out your roof pitch, angle and roof area with our free calculator."
CONTACT_LEDE = "Millcreek, Utah."
CONTACT_TITLE = "Contact RoofTek | Roofing Contractor in Millcreek, Utah"
CONTACT_META = "Contact RoofTek at 4080 S W Temple St, Millcreek, UT 84107. Call 801-471-2054 or send the form about a roof leak, storm damage or a new roof."
BEFORE = ["If water is coming in, move valuables and put a bucket under the drip; don&rsquo;t climb onto a wet or icy roof.", "Photos of the damage and the ceiling stains help.", "Know roughly how old the roof is, if you can."]
CTA_TITLE = "Roof trouble in Millcreek? <em>Call RoofTek.</em>"
CTA_TEXT = "Call RoofTek at 801-471-2054. 4080 S W Temple St, Millcreek, UT 84107."
SIDE_TITLE = "Roofing in Millcreek."
BLURB = "RoofTek: a roofing contractor at 4080 S W Temple St in Millcreek, Utah."
SVC = [("#tool", "Roof pitch calculator", None), ("what-is-a-fortified-roof/", "What a FORTIFIED roof is", None)]
NAV = [("Pitch calculator", "#tool"), ("FORTIFIED roofs", "what-is-a-fortified-roof/"), ("Contact", "contact/")]
