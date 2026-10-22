"""New blog post for equitypmusa.com (21 Oct 2026): spotting rental listing scams. For renters; it doesn't target any property
management keyword. Source: Federal Trade Commission consumer advice, "Rental Listing Scams" (consumer.ftc.gov). Equity's own
application process from its Application Criteria page."""
from engine import faq_html, faq_ld, canon

SLUG = "blog/how-to-spot-a-rental-scam/"
H1 = "How to spot a rental listing scam before you pay a dime"
FAQ = [("Is it safe to pay a deposit before seeing a rental?", "The FTC&rsquo;s advice is no. Scammers often ask for a security deposit or first month&rsquo;s rent before you&rsquo;ve met, toured the place or signed a lease. If you can&rsquo;t see the home or sign a lease first, keep looking."),
       ("Why is wiring money a red flag?", "According to the FTC, wiring money, sending gift cards or paying with cryptocurrency is the same as sending cash: once it&rsquo;s gone, you probably can&rsquo;t get it back. There&rsquo;s never a good reason to wire money for a deposit, application fee or first month&rsquo;s rent."),
       ("How do I check whether a listing is real?", "Search the property address along with the owner&rsquo;s or company&rsquo;s name. If the same home shows up in other ads under a different name, that&rsquo;s a warning sign. Check the property manager&rsquo;s own website to see whether the home is listed there."),
       ("Where do I report a rental scam?", "Report it to the FTC at ReportFraud.ftc.gov, and tell the website where the ad appeared. The FTC also suggests notifying local law enforcement and your state attorney general.")]
BODY = f'''<p class="answer">A rental is probably a scam if the &ldquo;landlord&rdquo; wants money before you&rsquo;ve seen the home or signed a lease, asks you to wire money or pay with gift cards or crypto, says they&rsquo;re out of the country and can&rsquo;t show it, or the rent is far below everything else nearby. Verify the listing with the actual manager before you pay anything.</p>

<p>Finding a rental takes work, and a listing that looks perfect can feel like a stroke of luck. Unfortunately, it&rsquo;s exactly what rental scammers count on. The Federal Trade Commission (FTC) has documented the patterns these scams follow. Once you know them, they&rsquo;re easier to spot. Here&rsquo;s what to watch for, how to check a listing, and what to do if something feels off.</p>

<h2>How rental scams work</h2>
<p>Most rental scams take one of two forms. In the first, a scammer copies a real listing (photos, description and all), changes the contact information, and posts it as their own. The home is real, but the &ldquo;landlord&rdquo; has no right to rent it. In the second, the listing is for a home that isn&rsquo;t for rent at all, or doesn&rsquo;t exist. Either way, the goal is the same: to collect a deposit, an application fee or the first month&rsquo;s rent before you discover the truth.</p>

<h2>The warning signs the FTC lists</h2>
<h3>1. They want money before you&rsquo;ve seen the place or signed a lease</h3>
<p>The FTC says scammers often ask for a security deposit or first month&rsquo;s rent before you&rsquo;ve met, toured the home or signed a lease. Its advice is simple: if you can&rsquo;t see the rental, or sign a lease, before you pay, keep looking.</p>

<h3>2. They ask you to wire money, or pay with gift cards or crypto</h3>
<p>This is the clearest red flag. In the FTC&rsquo;s words, wiring money, sending gift cards or paying with cryptocurrency is the same as sending cash: once you send it, you probably can&rsquo;t get it back. There is never a good reason to wire money to pay a security deposit, application fee or first month&rsquo;s rent.</p>

<h3>3. The &ldquo;owner&rdquo; is far away and can&rsquo;t show the home</h3>
<p>When you ask to see the rental, a fake owner might claim to be out of the country or give another excuse for not showing it, and may rush you into a quick decision. A real landlord or property manager wants you to see the home before you commit.</p>

<h3>4. The rent is much lower than everything nearby</h3>
<p>If the rent is far below what similar homes in the area rent for, treat that as a warning sign rather than a bargain.</p>

<h2>How to check a listing</h2>
<ol>
<li><strong>Search the address with the owner&rsquo;s or company&rsquo;s name.</strong> The FTC notes that if other ads show up for the same address with a different owner or company name, that&rsquo;s a sign of a scam.</li>
<li><strong>Go to the source.</strong> If a home is listed by a property management company, check that company&rsquo;s own website and call its published phone number to confirm the listing is real.</li>
<li><strong>See it in person,</strong> or have someone you trust do it, before you pay anything.</li>
<li><strong>Read the lease before you pay.</strong> A legitimate rental comes with a written lease from a landlord or manager you can verify.</li>
<li><strong>Pay through official channels</strong>, never by wire, gift card or cryptocurrency.</li>
</ol>

<h2>What a legitimate application looks like</h2>
<p>A real property manager has a clear, written process and doesn&rsquo;t pressure you into skipping steps. At Equity Real Estate Property Management, for example, the application criteria are published for anyone to read:</p>
<ul>
<li>A <strong>$65 non-refundable application fee</strong>, with a separate application for each person 18 or older who will live in the home.</li>
<li>A <strong>photo ID</strong> submitted with the application.</li>
<li><strong>Employment verification</strong>, generally at least 6 months with your current employer, and combined gross income of at least <strong>3&times; the monthly rent</strong> (or savings equal to 12 months of rent).</li>
<li><strong>Rental history</strong> for the past two years, and a credit and background review.</li>
</ul>
<p>Applications are reviewed on a first-completed, first-served basis, following Fair Housing guidelines, and the lease is signed before you move in. You can see the full list on our <a href="@/copy-of-tenants/">application criteria</a> page.</p>

<h2>If you think you&rsquo;ve been targeted</h2>
<p>Stop communicating with the &ldquo;landlord&rdquo; and don&rsquo;t send any more money. If you paid by wire, gift card or payment app, contact the company you used right away and ask whether the payment can be stopped. Then report the scam:</p>
<ul>
<li>To the FTC at <strong>ReportFraud.ftc.gov</strong></li>
<li>To the website where you saw the ad</li>
<li>To local law enforcement and your state attorney general</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Looking for a rental managed by Equity? Start with our <a href="@/copy-of-tenants/">application criteria</a>, or call our Sandy office at <a href="tel:+18015454302">801-545-4302</a> to confirm any listing.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Federal Trade Commission, Consumer Advice: <a href="https://consumer.ftc.gov/articles/rental-listing-scams" rel="noopener">Rental Listing Scams</a></li>
<li>Equity Real Estate Property Management, <a href="@/copy-of-tenants/">Application Criteria</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Rental scams", H1, "For renters &middot; Oct 21, 2026", "Blog", "How to Spot a Rental Listing Scam | Equity PM, Sandy UT",
                  "Rental scams ask for money before you see the home, by wire or gift card. The FTC's warning signs, how to check a listing, and where to report a rental scam.",
                  BODY, crumbs=[], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "Equity Real Estate Property Management"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
