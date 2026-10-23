"""New post (23 Oct 2026): how to hire a locksmith without getting scammed. Informational; doesn't target "locksmith salt lake city".
Sources: BBB, "BBB Scam Alert: Locked out? Don't fall for a locksmith scam" (24 Jul 2020); FTC press release "FTC Urges Consumers to Use
Caution When Seeking a Locksmith" (30 May 2008); FTC Consumer Advice, "How To Avoid a Scam"."""
from engine import faq_html, faq_ld, canon

SLUG = "how-to-hire-a-locksmith/"
H1 = "How to hire a locksmith without getting scammed"
FAQ = [("When should I find a locksmith?", "Before you need one. The FTC suggests researching a locksmith the same way you would a plumber or electrician, then saving the number in your phone."),
       ("What&rsquo;s the most common locksmith scam?", "The BBB describes a very low quote on the phone, sometimes as low as $15, followed by reasons on site to raise the price, often by hundreds of dollars."),
       ("How should I pay a locksmith?", "The BBB recommends paying by credit card for added security and insisting on an itemized invoice listing parts, labor, mileage and service charges."),
       ("What if the price changes when they arrive?", "The BBB says if the on-site estimate doesn&rsquo;t match the phone quote, have someone else do the job."),
       ("How can I tell if a locksmith ad is fake?", "The BBB suggests checking whether the specific business name is clearly identified, and whether the same ad appears under other names. Scammers often borrow a reputable locksmith&rsquo;s name and logo."),
       ("Should a locksmith show ID?", "Yes. The BBB says most legitimate locksmiths arrive in a clearly marked vehicle and provide identification."),
       ("Where do I report a locksmith scam?", "The FTC takes reports at ReportFraud.ftc.gov. You can also check and report businesses through the BBB."),
       ("Is there a risk after the job is done?", "The BBB warns that once a scammer has been to your home or workplace, they know where it is and may be able to get back in later, which is one more reason to vet a locksmith first.")]
BODY = f'''<p class="answer">Find a locksmith before you need one and save the number. When you call, ask for the business&rsquo;s name and the full price, including the service call, mileage and parts. When they arrive, expect a marked vehicle and ID, be wary of anyone who insists on drilling the lock, get an itemized invoice, and pay by card. If the price changes on site, the Better Business Bureau says to have someone else do the job.</p>

<p>Most people look for a locksmith at the worst possible moment: standing outside a locked door, late, cold or in a hurry. Scammers count on that. Both the Better Business Bureau (BBB) and the Federal Trade Commission (FTC) have warned about locksmiths who advertise as local, quote a low price and then charge far more. Here&rsquo;s what they say to watch for, and how to protect yourself.</p>

<h2>How the scam works</h2>
<p>The BBB&rsquo;s scam alert describes a pattern:</p>
<ul>
<li><strong>Borrowed identity.</strong> Many locksmith scammers use the name and logo of a reputable locksmith in their advertising.</li>
<li><strong>A generic greeting.</strong> When you call, you may hear something like &ldquo;Hello, locksmith services&rdquo; instead of a business name.</li>
<li><strong>A lowball quote.</strong> The caller quotes a very low price, as low as $15 in the BBB&rsquo;s example.</li>
<li><strong>The upsell on site.</strong> Once there, the locksmith finds reasons to raise the price. The BBB says victims often pay much more than they were quoted.</li>
<li><strong>Drilling and &ldquo;security&rdquo; upgrades.</strong> Scammers may claim the lock can&rsquo;t be opened without drilling and replacing it with an expensive lock, sometimes one that is cheap and not actually secure.</li>
</ul>
<p>There&rsquo;s a further risk the BBB points out: once a scammer has been to your home or workplace, they know where it is, and may be able to get back in later.</p>
<p>The FTC raised similar concerns as far back as 2008, warning that some locksmiths advertising in local listings may not be local at all, and that others may not have professional training.</p>

<h2>Before you&rsquo;re locked out</h2>
<p>The FTC&rsquo;s first piece of advice is the simplest: do the research before you need a locksmith, the same way you would choose a plumber, electrician or other professional, and then program the number into your phone. A calm afternoon is a much better time to compare businesses than a dark parking lot.</p>
<ul>
<li>Look at the advertising. The BBB suggests checking whether the specific name of the business is clearly identified, and whether the same ad appears under different names.</li>
<li>Look the business up on BBB.org.</li>
<li>Save the number of the one you choose.</li>
</ul>

<h2>On the phone</h2>
<p>The BBB&rsquo;s advice for the call itself:</p>
<ul>
<li><strong>Ask for the business name.</strong> If the person answering won&rsquo;t give one, that&rsquo;s a warning sign.</li>
<li><strong>Ask about all costs first.</strong> That includes the service call, mileage and parts, before you agree to the work.</li>
<li><strong>Get an estimate before work begins,</strong> including for emergency service.</li>
</ul>
<p>Our <a href="@/#tool">locksmith call checklist</a> puts these questions in one place so you can tick them off as you go.</p>

<h2>When the locksmith arrives</h2>
<ul>
<li><strong>Check identification.</strong> The BBB says most legitimate locksmiths arrive in a clearly marked vehicle and provide identification.</li>
<li><strong>Compare the price.</strong> If the on-site estimate doesn&rsquo;t match the phone quote, the BBB says to have someone else do the job.</li>
<li><strong>Be wary of drilling.</strong> The BBB notes that most locksmiths have the skills to open almost any lock, and that it isn&rsquo;t routine for a locksmith to insist on drilling the lock to open it.</li>
</ul>

<h2>Paying</h2>
<ul>
<li><strong>Insist on an itemized invoice.</strong> The BBB says it should list parts, labor, mileage and service charges, plus the business&rsquo;s name and address.</li>
<li><strong>Pay by credit card</strong> for added security.</li>
</ul>

<h2>General scam warning signs</h2>
<p>The FTC&rsquo;s general advice on avoiding scams applies here too. One of the most common signs is pressure: scammers usually push you to act quickly so you don&rsquo;t have time to check what they&rsquo;re saying. A legitimate locksmith can tell you the price and wait while you decide. If you think you&rsquo;ve been scammed, you can report it to the FTC at ReportFraud.ftc.gov.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Need a locksmith in Salt Lake City? Call Eagle Locksmith inc at <a href="tel:+13855577669">385-557-7669</a>, and ask us the same questions.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Better Business Bureau, <a href="https://www.bbb.org/article/news-releases/22797-bbb-scam-alert-locked-out-dont-fall-for-a-locksmith-cons" rel="noopener">BBB Scam Alert: Locked out? Don&rsquo;t fall for a locksmith scam</a> (July 24, 2020)</li>
<li>Federal Trade Commission, <a href="https://www.ftc.gov/news-events/news/press-releases/2008/05/ftc-urges-consumers-use-caution-when-seeking-locksmith" rel="noopener">FTC Urges Consumers to Use Caution When Seeking a Locksmith</a> (May 30, 2008)</li>
<li>Federal Trade Commission, <a href="https://consumer.ftc.gov/articles/how-avoid-scam" rel="noopener">How To Avoid a Scam</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Salt Lake City from Ensign Peak &middot; Iansmh98, CC BY-SA 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Hiring a locksmith", H1, "From the blog &middot; Oct 23, 2026", "Blog", "How to Hire a Locksmith Without Getting Scammed | Eagle",
                  "How to hire a locksmith safely: research ahead, get the full price first, check ID and a marked vehicle, avoid needless drilling and pay by credit card.",
                  BODY, image="hero", alt="Salt Lake City from Ensign Peak", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
