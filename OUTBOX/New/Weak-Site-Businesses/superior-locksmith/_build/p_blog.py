"""New post (23 Oct 2026): lock grades explained. Informational; doesn't target "locksmith west jordan". Sources: BHMA standard highlights
on buildershardware.com: A156.2-2022 Locks and Latches; A156.39-2025 Residential Locksets and Latches; ANSI/BHMA A156.5-2014 (auxiliary
locks/cylinders) revision document; BHMA, "Understanding BHMA Standards"."""
from engine import faq_html, faq_ld, canon

SLUG = "lock-grades-explained/"
H1 = "Lock grades explained: what BHMA ratings actually test"
FAQ = [("Who grades locks?", "The Builders Hardware Manufacturers Association (BHMA) publishes ANSI/BHMA standards that set performance tests for door hardware, and products are graded against them."),
       ("What does Grade 1 mean?", "It&rsquo;s the highest of the three numbered grades. Under A156.2, a Grade 1 bored lock must pass one million opening-and-closing cycles with a 10 lbf axial load, plus strength and security tests."),
       ("What is a Grade A residential lock?", "A156.39 covers residential locksets with letter grades. Grade A locks must pass 400,000 cycles with a 5 lb load, eleven strength and security tests, and a salt-spray finish test."),
       ("How can I check a lock&rsquo;s grade?", "BHMA maintains a Certified Products Directory where you can confirm a specific product&rsquo;s listing and grade."),
       ("Are lab tests tougher than real use?", "BHMA says its demanding laboratory tests typically exceed actual real-world usage, in order to ensure high performance."),
       ("What kinds of locks does A156.2 cover?", "Bored and preassembled locks and latches, the familiar cylindrical knob and lever locks. BHMA says it covers durability, load, operational, material, finish and dimensional testing."),
       ("Is a Grade 3 deadbolt good enough?", "BHMA&rsquo;s A156.5 document notes Grade 3 is generally used in residential applications, and advises specifying Grade 1 or Grade 2 for a relatively high level of security."),
       ("Do graded lever locks have to be easy to turn?", "Under A156.39, lever-operated residential locks must open with no more than 28 inch-pounds of torque, so they stay easy to operate.")]
BODY = f'''<p class="answer">Lock grades come from standards published by the Builders Hardware Manufacturers Association (BHMA). For bored locks under ANSI/BHMA A156.2, Grade 1 is the highest and must survive one million operating cycles plus strength and security tests. Residential locksets have their own standard, A156.39, where Grade A must pass 400,000 cycles and eleven strength and security tests. A grade tells you the lock was tested; BHMA&rsquo;s directory lets you confirm it.</p>

<p>Walk down the lock aisle and you&rsquo;ll see &ldquo;Grade 1,&rdquo; &ldquo;Grade 2&rdquo; or &ldquo;Grade A&rdquo; on some packages and nothing on others. Those grades aren&rsquo;t marketing terms; they refer to specific laboratory tests. Here&rsquo;s what they mean, from BHMA&rsquo;s own summaries of its standards.</p>

<h2>Who sets lock grades</h2>
<p>BHMA publishes the ANSI/BHMA A156 series of standards for builders hardware: locks, latches, cylinders, closers, hinges and more. Each standard sets requirements for things like durability, strength, security, operation and finish, and BHMA notes that these demanding laboratory tests typically exceed real-world use, in order to ensure high performance.</p>
<p>Grading generally runs in three levels, one, two and three, with grade one being the highest performance. Some newer standards, like the one for residential locksets, use letters instead.</p>

<h2>A156.2: bored locks and latches</h2>
<p>A156.2 establishes requirements for bored and preassembled locks and latches, the familiar cylindrical knob and lever locks. BHMA says it covers durability, load, operational, material, finish and dimensional testing.</p>
<ul>
<li><strong>Cycles:</strong> a Grade 1 lock must pass a test of one million cycles of opening and closing with a 10 lbf axial load applied.</li>
<li><strong>Strength and security:</strong> seven aggressive tests are specified, including a 1,200 inch-pound locked lever torque test and impact tests from two directions.</li>
</ul>
<p>That cycle count is what &ldquo;durability&rdquo; means in a lab: a mechanism operated a million times without failing.</p>

<h2>A156.39: residential locksets</h2>
<p>A156.39 establishes performance requirements for bored residential locksets and latches, covering durability, security, finish, operation and accessibility. It uses letter grades. BHMA&rsquo;s summary gives the Grade A thresholds:</p>
<ul>
<li><strong>Durability:</strong> 400,000 cycles of opening and closing with a 5 lb axial load.</li>
<li><strong>Security and strength:</strong> eleven aggressive tests; for Grade A, the latch must withstand 800 lb of force and the locked lever must hold at 500 inch-pounds.</li>
<li><strong>Finish:</strong> corrosion resistance evaluated with a salt-spray test to ASTM B117.</li>
<li><strong>Operation:</strong> lever-operated locks must open with no more than 28 inch-pounds of torque, so they stay easy to use.</li>
</ul>
<p>In practical terms, a Grade A residential lock has been tested for years of daily use, resistance to forced entry from outside, a finish that holds up, and easy operation.</p>

<h2>Cylinders and auxiliary locks</h2>
<p>Deadbolts and other auxiliary locks have their own standard, A156.5. BHMA&rsquo;s revision document notes that Grade 3 is generally used in residential applications, and advises that anyone wanting a relatively high level of security should specify Grade 1 or Grade 2. In other words, the grade on a deadbolt is worth reading.</p>

<h2>How to use grades when you shop</h2>
<ul>
<li><strong>Read the package.</strong> Look for the ANSI/BHMA standard number and grade, not just words like &ldquo;secure&rdquo; or &ldquo;heavy duty.&rdquo;</li>
<li><strong>Compare like with like.</strong> Numbered grades under A156.2 and letter grades under A156.39 come from different standards with different tests.</li>
<li><strong>Verify it.</strong> BHMA&rsquo;s Certified Products Directory lets you confirm a specific product&rsquo;s listing and grade.</li>
<li><strong>Remember installation.</strong> A well-rated lock still depends on the door, frame and strike it&rsquo;s installed in; ask a locksmith to look at the whole opening.</li>
</ul>

<h2>Rekey, repair or replace?</h2>
<p>A grade matters most when you&rsquo;re replacing a lock. If the lock you have is in good shape and you just need old keys to stop working, after a move or a lost key, rekeying changes the pins inside so a new key operates it and keeps the hardware you already have. Our <a href="@/#tool">rekey, repair or replace guide</a> walks through the common situations.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Choosing a new lock or rekeying in West Jordan? Call Superior Locksmith at <a href="tel:+18015650226">801-565-0226</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Builders Hardware Manufacturers Association, <a href="https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights/A1562-2022-Locks-and-Latches" rel="noopener">A156.2-2022 Locks and Latches</a></li>
<li>Builders Hardware Manufacturers Association, <a href="https://buildershardware.com/ANSI-BHMA-Standards/Hardware-Highlights/A15639-2025-Residential-Locksets-and-Latches" rel="noopener">A156.39-2025 Residential Locksets and Latches</a></li>
<li>Builders Hardware Manufacturers Association, <a href="https://buildershardware.com/LinkClick.aspx?fileticket=SIUnQOpH8Bo%3D&amp;portalid=0" rel="noopener">ANSI/BHMA A156.5-2014 revision</a></li>
<li>Builders Hardware Manufacturers Association, <a href="https://buildershardware.com/LinkClick.aspx?fileticket=PFMtyf1Dmak%3D&amp;portalid=0" rel="noopener">Understanding BHMA Standards</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Redwood Rd crossing, West Jordan &middot; An Errant Knight, CC BY-SA 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Lock grades", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Lock Grades Explained: BHMA Grade 1, 2, 3 and A | Superior",
                  "Lock grades explained: what BHMA Grade 1, 2 and 3 and residential Grade A locks are tested for, from cycle counts to strength tests, and how to check yours.",
                  BODY, image="hero", alt="Redwood Rd crossing in West Jordan", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
