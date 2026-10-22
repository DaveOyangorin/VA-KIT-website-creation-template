"""Journal for xperienceroofing.com: a new /blog with one post.

Post: "How to Read a Roofing Estimate: The Line Items That Matter (Utah Edition)"
Main phrase: "how to read a roofing estimate" (informational). It builds on the client's own promise of "written estimates with
clear line items" and doesn't target any service keyword; it links to replacement, inspections and the process page.
Facts and sources, checked 18 Oct 2026:
- Utah Admin. Code R156-55a-301: the S280 Roofing Contractor classification covers asphalt, pitch, tar, felt, shakes, shingles,
  roof tile, slate and similar weatherproof roof membranes, plus roof conversion and non-electrical skylights.
  https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R156-55a-301
- Utah Division of Professional Licensing (DOPL): license lookup by name or license number. https://dopl.utah.gov/
- FTC, "Hiring a Contractor": get written estimates from several firms; the lowest bid isn't always best; check that a license
  is current where your state requires one; a competent contractor gets the necessary permits.
  https://consumer.ftc.gov/articles/hiring-contractor
No prices are given.
"""
from engine import crumbs_ld, faq_html, faq_ld, canon
from cfg import S, U, NAME

POST = ("How to Read a Roofing Estimate: The Line Items That Matter", "blog/how-to-read-a-roofing-estimate/")
_ = {}


def setup(phero, cta, arrow, home, contact):
    _.update(phero=phero, cta=cta, A=arrow, HOME=home, CONTACT=contact)


ITEMS = [("Tear-off", "Removing the existing roof down to the deck. The estimate should say how many layers are coming off, because each layer adds labor and disposal."),
         ("Decking", "Replacing damaged or soft sheathing. Since nobody can see the deck until the old roof is off, a good estimate states how decking is priced if it&rsquo;s needed."),
         ("Underlayment", "Synthetic underlayment across the roof, and ice and water shield at the eaves, valleys and penetrations. Ask where the ice and water shield goes."),
         ("Flashing", "New metal at walls, chimneys, valleys and pipes, or reused old flashing? New is usually the better answer, and the estimate should say which."),
         ("Ventilation", "Ridge vents, intake vents and anything needed to balance the attic. Poor ventilation shortens a roof&rsquo;s life."),
         ("Drip edge and trim", "Metal along the eaves and rakes that guides water into the gutter and protects the deck edge."),
         ("Surface material", "The product line, color and profile: architectural shingle, standing seam, tile, metal shake or membrane. Brand and line, not just &ldquo;shingles.&rdquo;"),
         ("Permit and disposal", "Who pulls the permit, and whether the dumpster and haul-away are included."),
         ("Warranty", "Two kinds, in writing: the manufacturer&rsquo;s warranty on the materials and the contractor&rsquo;s workmanship warranty on the installation.")]
FAQ = [("Should I always pick the lowest estimate?", "Not automatically. The FTC notes the lowest bidder may not be the best choice. Compare what each estimate includes line by line before you compare totals."),
       ("How do I check a roofer&rsquo;s license in Utah?", "Roofing in Utah falls under the S280 Roofing Contractor classification. You can look up a contractor&rsquo;s license on the Utah Division of Professional Licensing (DOPL) website by name or license number."),
       ("Why is decking often listed separately?", "Because the deck can&rsquo;t be fully inspected until the old roof is off. A clear estimate explains how decking repairs are priced if they turn out to be needed."),
       ("Should verbal promises be in the estimate?", "Yes. Anything you were told about scope, materials or schedule should be written into the estimate or contract."),
       ("Does Xperience Roofing give written estimates?", "Yes. After a free inspection you get a written scope with system options and real numbers, with time to decide.")]


def post():
    path = POST[1]; A = _["A"]
    trail = [_["HOME"], ("Journal", "blog/"), ("Reading a roofing estimate", path)]
    rows = "".join(f'<li><span class="mono">{i + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(ITEMS))
    body = _["phero"](trail, "How to Read a Roofing Estimate: The Line Items That Matter", "A roofing estimate is a list of decisions. Here is what each line means, what should be on it, and what to ask before you sign.", "Journal &middot; Utah edition", buttons=False) + f'''
<section class="sec"><div class="wrap post-grid"><article class="prose post">
<p class="mono meta">By {NAME} &middot; 18 Oct 2026 &middot; 7 min read</p>
<p class="answer">A good roofing estimate is written, itemized and specific: it names the materials by brand and line, says what happens to the old roof and the deck, lists the flashing, underlayment and ventilation, and spells out the permit, cleanup and both warranties. If two estimates list different things, you aren&rsquo;t comparing the same roof.</p>

<h2>Start with the scope, not the total</h2>
<p>It&rsquo;s natural to look at the bottom line first. But two roofing estimates with very different totals are often describing two different jobs: one tears off two layers and replaces every piece of flashing, the other leaves the old metal in place and says nothing about the deck. Read the scope line by line, and only then compare prices.</p>
<p>The FTC&rsquo;s advice on hiring a contractor makes the same point: get written estimates from several firms, and keep in mind that the lowest bidder may not be the best choice.</p>

<h2>The line items, one by one</h2>
<p>Here are the items a complete estimate for a roof replacement should cover, in the order the roof goes on:</p>
<ol class="items">{rows}</ol>

<h2>Words to look out for</h2>
<ul>
<li><b>&ldquo;As needed&rdquo; with no price.</b> Fine for decking, as long as the estimate says how it will be charged.</li>
<li><b>&ldquo;Reuse existing.&rdquo;</b> Reused flashing or vents save money now and are a common source of leaks later.</li>
<li><b>&ldquo;Shingles&rdquo; with no brand.</b> Product lines vary widely. Ask for the manufacturer, the line and the color.</li>
<li><b>&ldquo;Today only&rdquo; pricing.</b> A real estimate gives you time to compare and decide.</li>
</ul>

<h2>Check the license before you sign</h2>
<p>In Utah, roofing work falls under the <b>S280 Roofing Contractor</b> license classification. Under the state&rsquo;s administrative code, that covers asphalt, tar, felt, shakes, shingles, roof tile, slate and similar roofing materials, plus roof conversions and non-electrical skylights. You can look up any contractor on the Utah Division of Professional Licensing (DOPL) website by name or license number and confirm the license is active. The FTC also advises making sure a contractor&rsquo;s license is current wherever your state requires one.</p>

<h2>Permits are part of the job</h2>
<p>A competent contractor gets the necessary permits before starting work, the FTC notes. Many Utah cities require a building permit for a reroof, so ask who is pulling it and whether its cost is in the estimate. If an estimate leaves permits out entirely, ask why.</p>

<h2>Two warranties, both in writing</h2>
<p>There are two different warranties on a new roof. The <b>manufacturer&rsquo;s warranty</b> covers the materials. The <b>workmanship warranty</b> comes from the contractor and covers the installation. Ask for both in writing, with the length and what voids them, before you sign. A materials warranty doesn&rsquo;t help much if the leak comes from how the flashing was installed.</p>

<h2>Get every promise on paper</h2>
<p>If the estimator told you the crew will protect the landscaping, run a magnet for nails, or replace the gutters at the same time, those promises belong in the estimate or the contract. What isn&rsquo;t written down is hard to hold anyone to later.</p>

<h2>Five questions to ask the estimator</h2>
<ol>
<li>How many layers are on the roof now, and are they all coming off?</li>
<li>How will decking be handled if you find soft or damaged boards?</li>
<li>Where exactly will ice and water shield go on my roof?</li>
<li>Is all of the flashing new, including at the chimney and walls?</li>
<li>Who is my contact during the job, and how will cleanup be checked at the end?</li>
</ol>
<p>Good answers are specific. If an answer is vague on the doorstep, it will usually be vague on the estimate too.</p>

<h2>How we write ours</h2>
<p>Our estimates follow the same logic as our <a href="@/process/">six-step process</a>: a free <a href="@/services/roof-inspections/">inspection</a> with photos you keep, then a written scope with system options and real numbers, line by line. Take it home, compare it, sleep on it. If you&rsquo;re planning a <a href="@/services/roof-replacement/">roof replacement</a>, start there.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>Utah Admin. Code R156-55a-301, License classifications and scope of practice (S280 Roofing Contractor): <a href="https://www.law.cornell.edu/regulations/utah/Utah-Admin-Code-R156-55a-301" rel="noopener">law.cornell.edu</a></li>
<li>Utah Division of Professional Licensing, license lookup: <a href="https://dopl.utah.gov/" rel="noopener">dopl.utah.gov</a></li>
<li>Federal Trade Commission, Hiring a Contractor: <a href="https://consumer.ftc.gov/articles/hiring-contractor" rel="noopener">consumer.ftc.gov</a></li>
</ul></div>
</article>
<aside class="sv-side"><div class="side-card"><p class="label">Need an estimate?</p><h3>Free inspection</h3><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{_["CONTACT"]}">Request a Free Estimate {A}</a></div></aside>
</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "How to Read a Roofing Estimate: Line Items That Matter",
            "meta": "How to read a roofing estimate: tear-off, decking, underlayment, flashing, ventilation, permits and warranties, plus how to check a Utah roofer's license.",
            "body": body, "ogtype": "article",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    A = _["A"]; trail = [_["HOME"], ("Journal", "blog/")]
    body = _["phero"](trail, "The Xperience Roofing Journal", "Notes from the Midvale office on roofs, materials and the choices behind them.", "Journal", buttons=False) + f'''
<section class="sec"><div class="wrap"><a class="guide wide" href="@/{POST[1]}"><span class="mono">Journal No. 01</span><b>{POST[0]}</b><em>Read it {A}</em></a></div></section>''' + _["cta"]()
    return {"path": "blog/", "canonical": canon("blog/"), "title": "The Xperience Roofing Journal | Midvale, Utah Roofers",
            "meta": "The Xperience Roofing journal: notes from our Midvale office on roofing systems, materials, estimates and the choices behind a roof that lasts in Utah.",
            "body": body, "schema": [crumbs_ld("blog/", trail)]}


def pages():
    return [index(), post()]
