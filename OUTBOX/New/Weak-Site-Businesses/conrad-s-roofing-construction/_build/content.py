"""Conrad's Roofing & Construction (Lehi): "Snow line". Winter navy, ice blue, brass; Fraunces. Signature: a roof snow-load calculator
(fresh snow, packed snow, ice -> pounds per square foot, against IBHS's 20 psf typical-roof estimate, via Maine Emergency Management).
Post: how much snow a roof can hold, with FEMA P-957 warning signs. Banner: Timpanogos and Utah Valley in snow (Ken Lund, CC BY-SA 2.0).
Facts: Google listing only."""
LAYOUT = "low"
CITY = "Lehi"
TRADE = "Roofing contractor"
LABEL = "Lehi, Utah &middot; 1650 Digital Dr"
H1 = "Roofing company in Lehi, <em>ready for winter.</em>"
LEDE = "Conrad&rsquo;s Roofing &amp; Construction is a roofing company in Lehi, Utah, at 1650 Digital Dr. Before the snow piles up, or after it does damage, call and talk it through."
HERO_ALT = "Mount Timpanogos and the snowy floor of Utah Valley seen from the air"
CREDIT = "Mount Timpanogos and Utah Valley &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons"
SIG_BTN = "Check your roof&rsquo;s snow load"
INTRO_LABEL = "Roofing &amp; construction"
INTRO_H2 = "Roofs that carry <em>Utah winters.</em>"
INTRO = ["Snow is weight. A foot of light powder and a foot of old, packed snow can put very different loads on the same roof, and ice is heavier still. Conrad&rsquo;s Roofing &amp; Construction works from Lehi, at the north end of Utah Valley.",
         "The calculator below turns what&rsquo;s on your roof into pounds per square foot, using the rules of thumb emergency managers publish. It&rsquo;s a way to decide when to worry and when to call, not a structural rating."]
SIG_LABEL = "Snow load calculator"
SIG_H2 = "How heavy is <em>the snow up there?</em>"
SIG_LEDE = "Estimate the depth of each layer on your roof. We convert it with the equivalences IBHS uses and compare it with the 20 pounds per square foot IBHS estimates a typical roof can handle."
SIG_HTML = '''<div class="tool-grid snow" data-snow>
<div class="sn-gauge" aria-hidden="true"><div class="sn-col"><i class="sn-fill" data-fill></i><b class="sn-line" style="bottom:33.3%"><span>20 psf typical roof</span></b></div><p class="sn-num"><span data-psf>0</span><small>lb / sq ft</small></p></div>
<div class="tool-in">
<label for="sn-f">Fresh, new snow (inches)</label><input type="number" id="sn-f" inputmode="decimal" min="0" value="12" data-fresh>
<label for="sn-p">Old or packed snow (inches)</label><input type="number" id="sn-p" inputmode="decimal" min="0" value="0" data-packed>
<label for="sn-i">Ice (inches)</label><input type="number" id="sn-i" inputmode="decimal" min="0" value="0" data-ice>
</div>
<div class="tool-out" aria-live="polite" data-out><p class="mono">About 5 lb per square foot</p><h3>Well under a typical roof&rsquo;s estimate.</h3><p></p></div>
<p class="small tool-src">Equivalences from IBHS via Maine Emergency Management Agency, &ldquo;Removing Snow from Roofs&rdquo;: 10&ndash;12 inches of new snow, or 3&ndash;5 inches of old snow, equals about 1 inch of water, about 5 lb per sq ft; 1 inch of ice is about 5 lb per sq ft. We use the middle of each range. Older roofs may handle less than 20 psf. Nothing you type leaves this page.</p>
</div>'''
TIPS_LABEL = "Warning signs"
TIPS_H2 = "When the roof <em>is telling you something</em>"
TIPS_LINK = "How much snow can a roof hold?"
TIPS = [("Sagging", "FEMA lists sagging ceiling boards, sagging roof members and bowing trusses among the warning signs of an overstressed roof."),
        ("Sounds", "Popping, cracking and creaking noises during a heavy snow are on FEMA&rsquo;s list too."),
        ("Sticking doors", "FEMA also lists doors or windows that can no longer be opened or closed."),
        ("Cracks and leaks", "Cracks in walls or masonry, cracked or split wood members, and severe roof leaks. If you see any of these, FEMA says to leave the building and get a professional to inspect it.")]
TIPS_SRC = "Source: FEMA P-957, Snow Load Safety Guidance (2014). Don&rsquo;t climb onto a snowy roof; FEMA says snow removal should only be done by qualified people."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is Conrad&rsquo;s Roofing &amp; Construction?", "<p>1650 Digital Dr, Lehi, UT 84043.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+14353753396">435-375-3396</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("How much snow can a roof hold?", "<p>IBHS estimates a typical roof can handle about 20 pounds per square foot of extra weight, less for older roofs. That&rsquo;s roughly 4 feet of new snow or 2 feet of old, packed snow, by its rules of thumb.</p>"),
       ("Should I shovel my roof?", "<p>FEMA and Maine Emergency Management both warn that snow removal from roofs is dangerous. Use a roof rake from the ground for small amounts, and leave anything that requires climbing to professionals.</p>")]
POST_BLURB = "IBHS&rsquo;s rules of thumb for snow weight, FEMA&rsquo;s warning signs, and how to clear snow safely."
TITLE = "Lehi Roofing Company | Conrad's Roofing &amp; Construction"
META = "Conrad's Roofing &amp; Construction: roofing company at 1650 Digital Dr, Lehi, Utah. Call 435-375-3396. Check your roof's snow load with our free calculator."
CONTACT_LEDE = "Lehi, Utah."
CONTACT_TITLE = "Contact Conrad's Roofing &amp; Construction | Lehi, Utah"
CONTACT_META = "Contact Conrad's Roofing &amp; Construction at 1650 Digital Dr, Lehi, UT 84043. Call 435-375-3396 or send the form about a roof or construction project."
BEFORE = ["If you see sagging, hear cracking or doors start sticking under heavy snow, get everyone out first, as FEMA advises.", "Photos of the roof and any leaks help.", "Know roughly how old the roof is, if you can."]
CTA_TITLE = "Roof questions in Lehi? <em>Call Conrad&rsquo;s.</em>"
CTA_TEXT = "Call Conrad&rsquo;s Roofing &amp; Construction at 435-375-3396. 1650 Digital Dr, Lehi, UT 84043."
SIDE_TITLE = "Roofing in Lehi."
BLURB = "Conrad&rsquo;s Roofing &amp; Construction: a roofing contractor at 1650 Digital Dr in Lehi, Utah."
SVC = [("#tool", "Snow load calculator", None), ("how-much-snow-can-a-roof-hold/", "How much snow can a roof hold?", None)]
NAV = [("Snow load", "#tool"), ("Roof snow guide", "how-much-snow-can-a-roof-hold/"), ("Contact", "contact/")]
