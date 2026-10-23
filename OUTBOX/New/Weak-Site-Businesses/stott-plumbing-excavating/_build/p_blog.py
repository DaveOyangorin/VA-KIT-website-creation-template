"""New post (23 Oct 2026): Blue Stakes 811 in Utah. Informational; doesn't target "plumber salt lake city". Sources: Blue Stakes of Utah
811 home page and Professional Excavator page (Internet Archive captures of 13 Oct 2026 and 21 May 2026; the live site blocks automated
requests); Virginia 811, "What do the markings mean"; 811beforeyoudig.com, "Before you dig"."""
from engine import faq_html, faq_ld, canon

SLUG = "blue-stakes-811-utah-before-you-dig/"
H1 = "Blue Stakes 811 in Utah: what to know before you dig"
FAQ = [("How far ahead do I need to contact Blue Stakes?", "At least 3 business days, but not more than 14 calendar days, before you start excavating, according to Blue Stakes of Utah&rsquo;s summary of state law."),
       ("Does it cost anything?", "No. Blue Stakes says the service is free of charge to excavators and is funded by its participating member facility operators."),
       ("What if the marks are missing when the wait is over?", "Blue Stakes&rsquo; process says to verify all markings are present before excavating, and if they aren&rsquo;t, submit a No Response Notice."),
       ("Who marks my sewer lateral?", "Usually no one, through 811. Utah law requires operators to mark only the lines they own and maintain, usually up to the meter, so private laterals may not be marked. Blue Stakes suggests considering a private locator.")]
BODY = f'''<p class="answer">In Utah, anyone digging with tools or equipment must notify Blue Stakes of Utah 811 at least 3 business days, and no more than 14 calendar days, before excavating. The service is free. Wait for the legal start time, confirm every line is marked, and dig by hand within 2 feet of the marks. Remember that private lines, such as your water and sewer laterals, may not be marked at all.</p>

<p>A fence post, a new tree, a sprinkler trench or a sewer repair all start the same way: with a shovel going into ground that may hold gas, power, water and communication lines. Utah runs its call-before-you-dig program through Blue Stakes of Utah 811. Here is how it works, what the paint means, and the gap most homeowners don&rsquo;t know about.</p>

<h2>What Blue Stakes is</h2>
<p>Blue Stakes of Utah 811 describes itself as the communications link between excavators and the utility companies, which it calls participating member facility operators. You submit a locate request, Blue Stakes passes it to the operators with lines in the area, and they send locators to mark their lines. Blue Stakes says the service is free of charge to excavators and funded by those member operators. It summarizes it as: free, and the law.</p>
<p>811 is the national call-before-you-dig number, and the national 811 site advises anyone planning to dig to contact their state center a few business days ahead, since state laws vary. In Utah, requests can be made by phone or online through Blue Stakes&rsquo; Internet Ticket Entry system.</p>

<h2>The five steps</h2>
<p>Blue Stakes lays out a five-step process for safer digging:</p>
<ol>
<li><strong>Notify.</strong> Contact Blue Stakes of Utah 811 at least 3 business days before excavation, with specific dig-site location information. Its excavator guide puts the legal window at no more than 14 calendar days ahead.</li>
<li><strong>Wait.</strong> Once your request goes to the operators, wait until the legal date and time shown on your locate request.</li>
<li><strong>Confirm.</strong> Check your locate request and verify that all markings for your dig site are present before excavating. If they aren&rsquo;t, submit a No Response Notice.</li>
<li><strong>Respect.</strong> Use hand tools and dig carefully 2 feet on either side of the markings. Request new markings if they&rsquo;re destroyed.</li>
<li><strong>Dig carefully.</strong> Stay aware of your surroundings and respect the utilities and the markings.</li>
</ol>
<p>Blue Stakes adds that marks destroyed by weather, traffic or excavation need a re-mark request, which also takes at least 3 business days, and that a re-mark doesn&rsquo;t extend the life of the original ticket.</p>

<h2>What the colors mean</h2>
<p>Locators use a uniform color code for paint and flags. The American Public Works Association (APWA) colors, as listed by Virginia 811:</p>
<ul>
<li><strong>Red:</strong> electric power lines, cables, conduit and lighting cables</li>
<li><strong>Orange:</strong> communication, alarm or signal lines, cables or conduit</li>
<li><strong>Yellow:</strong> gas, oil, steam, petroleum or gaseous material</li>
<li><strong>Green:</strong> sewers and drain lines</li>
<li><strong>Blue:</strong> potable water</li>
<li><strong>Purple:</strong> reclaimed water, irrigation and slurry lines</li>
<li><strong>White:</strong> proposed excavation</li>
</ul>
<p>White is the one you can use yourself. The national 811 site suggests that if you&rsquo;re only digging in a small part of your yard, you can outline the area in white paint or flags so that only the utilities in that area are located and marked. Blue Stakes also asks for pre-marking in some situations, such as potholing.</p>

<h2>The lines 811 won&rsquo;t mark</h2>
<p>This is the part that surprises homeowners. Blue Stakes explains that Utah law requires facility operators to mark only the lines they own and maintain, which usually means up to the meter. Underground lines beyond the meter, or not owned by a member operator, may not be marked. Its examples:</p>
<ul>
<li>Water and sewer laterals</li>
<li>Power to a detached garage or lamppost</li>
<li>Sprinkler and irrigation systems</li>
<li>Lines connected to a propane tank or septic system</li>
</ul>
<p>Blue Stakes notes that almost every job site includes some privately owned underground pipe or cable. It advises excavators to inspect the property carefully, ask the owner about private lines before digging, and consider hiring a private locator to mark them.</p>
<p>For a homeowner, that means the sewer line running from your house to the street, often the very pipe a plumbing and excavating job is about, may be unmarked even after a valid locate request. Knowing roughly where it runs, where it leaves the foundation and where any cleanouts are helps everyone dig safely.</p>

<h2>Before your project</h2>
<ul>
<li>Submit a locate request 3 to 14 days ahead, even for a shallow job.</li>
<li>Outline the dig area in white if it&rsquo;s small.</li>
<li>Wait for the legal start time and check that every operator has marked or cleared.</li>
<li>Hand-dig within 2 feet of each mark.</li>
<li>List the private lines on your property and plan for them separately.</li>
<li>If you&rsquo;ve hired a contractor, ask whether they&rsquo;ve submitted the locate request.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Need a sewer lateral, water line or other plumbing dug up in Salt Lake City? Call Stott Plumbing &amp; Excavating at <a href="tel:+18014672432">801-467-2432</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Blue Stakes of Utah 811, <a href="https://web.archive.org/web/20261013181829/https://www.bluestakes.org/" rel="noopener">home page and five-step process</a> (Internet Archive capture, October 13, 2026)</li>
<li>Blue Stakes of Utah 811, <a href="https://web.archive.org/web/20260521141818/https://www.bluestakes.org/excavator/" rel="noopener">Professional Excavator page and FAQs</a> (Internet Archive capture, May 21, 2026)</li>
<li>Virginia 811, <a href="https://va811.com/what-do-the-markings-mean/" rel="noopener">What do the markings mean?</a></li>
<li>811beforeyoudig.com, <a href="http://811beforeyoudig.com/before-you-dig/" rel="noopener">Before you dig</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Salt Lake City &middot; Garrett, CC BY 2.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Blue Stakes 811", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Blue Stakes 811 in Utah: Before You Dig | Stott Plumbing",
                  "Blue Stakes 811 in Utah: notify 3 business days ahead, what the paint colors mean, hand-digging near marks, and private lines like water and sewer laterals.",
                  BODY, image="hero", alt="Salt Lake City and the Wasatch", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
