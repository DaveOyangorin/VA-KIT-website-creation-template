"""Superior Locksmith (West Jordan, 7679 S Redwood Rd): "Pin stack". Aubergine and violet, steel grey, Syne. Signature: "Rekey, repair or
replace?" a scenario picker that explains each option in plain terms and points to BHMA grades for upgrades. Post: lock grades explained
(BHMA A156.2, A156.39, A156.5 highlights, buildershardware.com). Banner: Redwood Rd crossing near West Jordan City Center (An Errant Knight,
CC BY-SA 4.0). Facts: Google listing only."""
LAYOUT = "split"
CITY = "West Jordan"
TRADE = "Locksmith"
LABEL = "West Jordan, Utah &middot; 7679 S Redwood Rd"
H1 = "Locksmith in West Jordan, <em>on Redwood Road.</em>"
LEDE = "Superior Locksmith is a locksmith in West Jordan, Utah, at 7679 S Redwood Rd. New keys, a new home, a lock that&rsquo;s worn out: call and talk to a locksmith."
HERO_ALT = "Light rail tracks and the Redwood Road crossing near West Jordan City Center, with the Wasatch in the distance"
CREDIT = "Redwood Rd crossing, West Jordan &middot; An Errant Knight, CC BY-SA 4.0, via Wikimedia Commons"
SIG_BTN = "Rekey, repair or replace?"
INTRO_LABEL = "Locksmith"
INTRO_H2 = "The right fix <em>for the lock you have.</em>"
INTRO = ["Superior Locksmith works from Redwood Road in West Jordan. Most lock jobs come down to one question: keep the lock and change the key, fix what&rsquo;s there, or put in something new.",
         "The picker below walks through common situations and what each option means, so you know what to ask for when you call."]
SIG_LABEL = "Rekey, repair or replace?"
SIG_H2 = "What&rsquo;s going on <em>with your lock?</em>"
SIG_LEDE = "Pick the situation closest to yours. We&rsquo;ll explain the option that usually fits and what to ask about."
SIG_HTML = '''<div class="tool-grid pick" data-pick>
<div class="pk-lock" aria-hidden="true"><svg viewBox="0 0 160 200"><path class="pk-shackle" data-sh d="M40 90 V60 a40 40 0 0 1 80 0 V90"/><rect class="pk-body" x="20" y="88" width="120" height="100" rx="14"/><g class="pk-pins" data-pins><rect x="52" y="112" width="8" height="26" rx="3"/><rect x="66" y="112" width="8" height="34" rx="3"/><rect x="80" y="112" width="8" height="20" rx="3"/><rect x="94" y="112" width="8" height="30" rx="3"/></g><circle class="pk-key" cx="80" cy="162" r="8"/></svg></div>
<fieldset class="tool-in"><legend>Your situation</legend><div class="chips pk-chips">
<label class="chip"><input type="radio" name="pk" value="move" checked><span>Just moved in</span></label>
<label class="chip"><input type="radio" name="pk" value="lost"><span>Lost a key</span></label>
<label class="chip"><input type="radio" name="pk" value="many"><span>Too many different keys</span></label>
<label class="chip"><input type="radio" name="pk" value="stiff"><span>Key sticks or won&rsquo;t turn</span></label>
<label class="chip"><input type="radio" name="pk" value="broken"><span>Lock is damaged</span></label>
<label class="chip"><input type="radio" name="pk" value="stronger"><span>Want a stronger lock</span></label></div></fieldset>
<div class="tool-out" aria-live="polite" data-out><p class="mono"></p><h3></h3><p></p></div>
<p class="small tool-src">General guidance, not a quote; a locksmith will look at the actual lock. Grade information: Builders Hardware Manufacturers Association (BHMA) standards A156.2 and A156.39.</p>
</div>'''
TIPS_LABEL = "Lock grades"
TIPS_H2 = "What the <em>grade on the box means</em>"
TIPS_LINK = "Lock grades explained"
TIPS = [("BHMA sets the tests", "The Builders Hardware Manufacturers Association publishes the ANSI/BHMA standards that locks are graded against."),
        ("Grade 1: a million cycles", "Under A156.2, a Grade 1 bored lock must pass one million opening-and-closing cycles with a 10 lbf load."),
        ("Residential Grade A", "A156.39 covers residential locksets: Grade A must pass 400,000 cycles and eleven strength and security tests."),
        ("Check the listing", "BHMA keeps a Certified Products Directory, so you can confirm a specific product&rsquo;s grade.")]
TIPS_SRC = "Source: BHMA, A156.2-2022 Locks and Latches and A156.39-2025 Residential Locksets and Latches highlights (buildershardware.com)."
FAQ_H2 = "Good <em>to know</em>"
FAQ = [("Where is Superior Locksmith?", "<p>7679 S Redwood Rd, West Jordan, UT 84084.</p>"),
       ("How do I reach you?", '<p>Call <a href="tel:+18015650226">801-565-0226</a>, or send the form on the <a href="@/contact/">contact page</a>.</p>'),
       ("What&rsquo;s the difference between rekeying and replacing?", "<p>Rekeying changes the inside of the lock so old keys stop working and a new key does, while you keep the lock itself. Replacing swaps the whole lock, which makes sense when it&rsquo;s damaged or you want a different grade or style.</p>"),
       ("What does a BHMA grade mean?", "<p>It means the lock was tested to an ANSI/BHMA standard. For example, Grade 1 locks under A156.2 must pass one million cycles; residential Grade A locks under A156.39 must pass 400,000.</p>")]
POST_BLURB = "What BHMA grades test, from cycle counts to strength, and how to check a lock&rsquo;s rating."
TITLE = "Locksmith in West Jordan, Utah | Superior Locksmith"
META = "Superior Locksmith: locksmith at 7679 S Redwood Rd, West Jordan, Utah. Call 801-565-0226. Not sure whether to rekey, repair or replace? Use our quick guide."
CONTACT_LEDE = "West Jordan, Utah."
CONTACT_TITLE = "Contact Superior Locksmith | Locksmith in West Jordan, Utah"
CONTACT_META = "Contact Superior Locksmith at 7679 S Redwood Rd, West Jordan, UT 84084. Call 801-565-0226 or send the form about keys, rekeying or any lock problem at home."
BEFORE = ["Say what kind of lock it is (front door, deadbolt, mailbox, vehicle) and how many you need done.", "A photo of the lock and key helps.", "Ask for the full price before work starts."]
CTA_TITLE = "Keys or locks in West Jordan? <em>Call Superior.</em>"
CTA_TEXT = "Call Superior Locksmith at 801-565-0226. 7679 S Redwood Rd, West Jordan, UT 84084."
SIDE_TITLE = "Locksmith in West Jordan."
BLURB = "Superior Locksmith: a locksmith at 7679 S Redwood Rd in West Jordan, Utah."
SVC = [("#tool", "Rekey, repair or replace?", None), ("lock-grades-explained/", "Lock grades explained", None)]
NAV = [("Rekey or replace", "#tool"), ("Lock grades", "lock-grades-explained/"), ("Contact", "contact/")]
