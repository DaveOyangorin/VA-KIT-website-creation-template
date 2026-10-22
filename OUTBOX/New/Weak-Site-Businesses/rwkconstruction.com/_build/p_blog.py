"""New blog post for rwkconstruction.com (21 Oct 2026): radon testing for Utah homeowners. Informational; it doesn't target basement
finishing, remodeling, home theater or custom home keywords. Sources: U.S. EPA, "A Citizen's Guide to Radon" (EPA 402/K-12/002, 2025),
"Consumer's Guide to Radon Reduction" (EPA 402/K-10/005, 2025), "What is EPA's Action Level for Radon", "Radon-Resistant Construction
Basics and Techniques", "Health Risk of Radon". Utah DEQ's radon pages were unreachable (403) on 21 Oct, so the post points readers to
their state radon office through EPA's directory rather than quoting state figures."""
from engine import faq_html, faq_ld, canon

SLUG = "radon-testing-utah-homes/"
H1 = "Radon in Utah homes: when to test, what the numbers mean, and how it&rsquo;s fixed"
IMG = "rw-hall"
FAQ = [("What radon level is too high?", "EPA recommends fixing your home if radon is 4 picocuries per liter (pCi/L) or higher, and suggests considering a fix between 2 and 4 pCi/L, because there is no known safe level of exposure."),
       ("Which floor should I test on?", "The lowest lived-in level of the home: the basement if you use it regularly, otherwise the first floor. Use a room you spend time in, not a kitchen or bathroom, and set the kit at least 20 inches off the floor."),
       ("Should I test before converting a basement into living space?", "Yes. EPA says it is especially important to test before a major renovation such as converting an unfinished basement into living space, and to test again after the work is finished."),
       ("Can I just seal the cracks?", "Sealing helps other methods work, but EPA does not recommend sealing alone, because by itself it has not been shown to lower radon significantly or consistently.")]
BODY = f'''<p class="answer">Radon is a radioactive gas you can&rsquo;t see, smell or taste, and testing is the only way to know if your home has it. EPA recommends testing every home below the third floor, fixing the home if the level is 4 pCi/L or higher, and testing before (and again after) any major renovation, such as turning an unfinished basement into living space.</p>

<p>Most Utah homeowners have heard the word &ldquo;radon&rdquo; during a home inspection and then forgotten about it. That&rsquo;s understandable. Radon gives no warning: no odor, no stain on the wall, no symptom you&rsquo;d notice day to day. But the U.S. Environmental Protection Agency (EPA) calls it the second leading cause of lung cancer in the United States after smoking, and the leading cause among non-smokers. The good news is that testing is cheap and easy, and high levels can be brought down. Here&rsquo;s what EPA&rsquo;s guidance says, in plain terms.</p>

<h2>What radon is and how it gets in</h2>
<p>Radon forms naturally when uranium, thorium or radium break down in rock, soil and groundwater. It moves up through the ground and into buildings through cracks and other openings in the foundation. EPA lists the usual entry points as cracks in solid floors, construction joints, cracks in walls, gaps in suspended floors, gaps around service pipes, cavities inside walls, and sometimes the water supply.</p>
<p>The reason it collects indoors comes down to air pressure. EPA explains that the air pressure inside a home is usually lower than the pressure in the soil around the foundation, so the house acts a little like a vacuum, drawing soil gas in. Once inside, radon gets trapped and can build up.</p>
<p>It isn&rsquo;t only an old-house problem. EPA is clear that <strong>any home may have a radon problem</strong>: new and old, well sealed or drafty, with or without a basement. Nearly 1 in every 15 homes in the U.S. is estimated to have elevated radon levels.</p>

<h2>Why it matters</h2>
<p>When you breathe air that contains radon, you raise your risk of lung cancer. EPA estimates radon is responsible for about 21,000 lung cancer deaths in the U.S. every year, about 2,900 of them among people who have never smoked. For smokers the risk is much higher, because radon and smoking compound each other.</p>
<p>Because you spend most of your time at home, that&rsquo;s where most of your exposure happens. That&rsquo;s also why the level in the rooms you actually use matters most.</p>

<h2>The numbers: what a test result means</h2>
<p>Radon in air is measured in picocuries per liter, written <strong>pCi/L</strong>. EPA&rsquo;s reference points:</p>
<ul>
<li><strong>0.4 pCi/L</strong>: the average level in outdoor air.</li>
<li><strong>1.3 pCi/L</strong>: the estimated average indoor level in American homes.</li>
<li><strong>2 to 4 pCi/L</strong>: EPA suggests considering a fix, because there is no known safe level of exposure.</li>
<li><strong>4 pCi/L or higher</strong>: EPA&rsquo;s action level. Fix the home.</li>
</ul>
<p>EPA adds that with today&rsquo;s technology, radon in most homes can be reduced to 2 pCi/L or below.</p>

<h2>How to test your home</h2>
<p>There are two kinds of test. <strong>Short-term tests</strong> stay in the home for two to 90 days, depending on the device. <strong>Long-term tests</strong> stay more than 90 days and give a better picture of your year-round average, since radon levels move from day to day and season to season. All radon tests should run for at least 48 hours. Low-cost do-it-yourself kits are sold by mail and in some hardware stores, or you can hire a qualified tester, which is common when a home is being bought or sold.</p>

<h3>Where to put the kit</h3>
<ul>
<li>In the <strong>lowest lived-in level</strong> of the home: the basement if it&rsquo;s used regularly, otherwise the first floor.</li>
<li>In a room you use, like a living room, playroom, den or bedroom. Not the kitchen or a bathroom.</li>
<li>At least <strong>20 inches above the floor</strong>, where it won&rsquo;t be disturbed, away from drafts, high heat, high humidity and exterior walls.</li>
</ul>

<h3>Setting up a short-term test</h3>
<p>Close windows and outside doors and keep them closed as much as possible during the test. For a test of just two or three days, close them at least 12 hours before you start. Furnace and air-conditioning fans that recirculate air can run, but don&rsquo;t run fans that bring in outside air. Avoid short tests during unusually severe storms or high winds. When the test ends, reseal the kit and mail it to the lab right away.</p>

<h3>EPA&rsquo;s three steps</h3>
<ol>
<li><strong>Take a short-term test.</strong> If the result is 4 pCi/L or higher, follow up to be sure.</li>
<li><strong>Follow up</strong> with a long-term test for a better year-round picture, or a second short-term test if you need results quickly. If the first result is more than twice the action level (over 8 pCi/L), take the second short-term test right away.</li>
<li><strong>Decide.</strong> Fix the home if a long-term result is 4 pCi/L or more, or consider fixing it if the average of two short-term tests is 4 pCi/L or more.</li>
</ol>

<h2>Test before you renovate, and again after</h2>
<p>This is the part that matters most if you&rsquo;re planning work on your home. EPA&rsquo;s Citizen&rsquo;s Guide says that if you&rsquo;re planning any major structural renovation, <strong>such as converting an unfinished basement area into living space, it is especially important to test the area for radon before you begin</strong>. If the results show a problem, radon-resistant techniques can be included inexpensively as part of the renovation. And because major renovations can change radon levels in any home, EPA says to <strong>always test again after the work is completed</strong>.</p>
<p>EPA also notes that if your living patterns change and you start using a lower level of the home, like a basement, you should retest on that level. If you already have a radon reduction system and you&rsquo;re converting basement space, EPA suggests asking your radon contractor whether the changes could affect the system&rsquo;s warranty, then retesting the lowest lived-in area after the remodel.</p>

<h2>How high radon is fixed</h2>
<p>Radon reduction works. EPA says some systems can cut radon levels by up to 99 percent, and most homes can be fixed for about the same cost as other common home repairs, though costs vary with the home&rsquo;s size and design.</p>
<p>For homes with a basement or a slab-on-grade foundation, the usual approach is <strong>soil suction</strong>: drawing radon from beneath the home and venting it through a pipe to the air above the roofline, where it quickly dilutes. EPA describes <strong>active subslab suction</strong> (also called subslab depressurization) as the most common and usually the most reliable method. One or more suction pipes go through the slab into the gravel or soil underneath, and a fan keeps the system running.</p>
<p>A few points from EPA&rsquo;s Consumer&rsquo;s Guide to Radon Reduction worth knowing:</p>
<ul>
<li><strong>Sealing alone isn&rsquo;t enough.</strong> Sealing cracks makes other methods work better, but EPA does not recommend sealing by itself, because it hasn&rsquo;t been shown to lower radon significantly or consistently, and normal settling opens new gaps.</li>
<li><strong>Active systems need a warning device</strong>, such as a gauge, light or alarm, placed where you&rsquo;ll see or hear it if the system stops working.</li>
<li><strong>Test after installation.</strong> A post-mitigation test should be done within 30 days of installation, but no sooner than 24 hours after.</li>
<li><strong>Keep the fan running</strong> continuously, and retest at least every two years.</li>
<li><strong>Use a qualified contractor.</strong> EPA suggests starting with your state radon office, since many states require radon professionals to be licensed, certified or registered.</li>
</ul>

<h2>New homes: radon-resistant construction</h2>
<p>If you&rsquo;re building, radon-resistant features are simplest to add while the house goes up. EPA&rsquo;s basic list is a 4-inch layer of clean, coarse gravel under the slab, heavy plastic sheeting over it, a 3- or 4-inch solid PVC vent pipe running from the gravel up through the roof, sealing and caulking foundation openings, and an electrical junction box in the attic in case a vent fan is needed later. EPA notes the builder&rsquo;s cost for these features is typically less than mitigating the home afterward, and that every new home should still be tested after move-in, even if it was built radon-resistant.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>Test the lowest lived-in level of your home. It&rsquo;s inexpensive and takes minutes.</li>
<li>4 pCi/L or higher: fix it. Between 2 and 4: consider fixing it.</li>
<li>Planning to turn a basement into living space? Test first, and test again when the work is done.</li>
<li>Use a qualified radon professional, and keep any system&rsquo;s fan running.</li>
</ul>

<p>For radon testing kits, qualified testers and mitigation contractors in Utah, start with EPA&rsquo;s directory of state radon offices below. If you&rsquo;re planning a project in your home, RWK Construction offers a free consultation and estimate across Salt Lake, Utah, Davis and Tooele Counties. Call <a href="tel:+18018204049">801-820-4049</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/sites/default/files/2016-12/documents/2016_a_citizens_guide_to_radon.pdf" rel="noopener">A Citizen&rsquo;s Guide to Radon</a> (EPA 402/K-12/002)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/sites/default/files/2016-12/documents/2016_consumers_guide_to_radon_reduction.pdf" rel="noopener">Consumer&rsquo;s Guide to Radon Reduction: How to Fix Your Home</a> (EPA 402/K-10/005)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean" rel="noopener">What is EPA&rsquo;s Action Level for Radon and What Does it Mean?</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/radon/health-risk-radon" rel="noopener">Health Risk of Radon</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/radon/radon-resistant-construction-basics-and-techniques" rel="noopener">Radon-Resistant Construction Basics and Techniques</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/radon/find-information-about-local-radon-zones-and-state-contact-information" rel="noopener">Find Information about Local Radon Zones and State Contact Information</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Radon in Utah homes", H1, "From the blog &middot; Oct 21, 2026", "Blog", "Radon Testing in Utah Homes: What EPA Says | RWK Blog",
                  "When to test for radon, what 4 pCi/L means, where to put the kit, and why EPA says to test both before and after converting a basement into living space.",
                  BODY, image=IMG, alt="A finished hallway in a Utah home", crumbs=[("Blog", "blog/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "Radon in Utah homes: when to test, what the numbers mean, and how it's fixed", "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                           "author": {"@type": "Organization", "name": "RWK Construction Co."}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
