"""New post (23 Oct 2026): when to replace a toilet. Informational; doesn't target "plumber salt lake city". Sources: EPA WaterSense,
"Residential Toilets" (updated 29 May 2026); EPA WaterSense, "Fix a Leak Week" (updated 13 Mar 2026)."""
from engine import faq_html, faq_ld, canon

SLUG = "when-to-replace-a-toilet/"
H1 = "When to replace a toilet: what WaterSense says about old, thirsty models"
FAQ = [("How do I know how many gallons my toilet uses?", "Many toilets have the gallons per flush (gpf) stamped on the porcelain behind the seat or inside the tank. EPA WaterSense says older models can use as much as 6 gpf."),
       ("What does the WaterSense label mean?", "WaterSense-labeled toilets use 1.28 gallons per flush or less, which EPA says is 20 percent below the current federal standard of 1.6 gallons."),
       ("How much water could I save?", "WaterSense estimates that replacing old toilets could cut toilet water use by 20 to 60 percent, nearly 13,000 gallons a year for a home, and more than $170 a year in water costs."),
       ("How do I check a toilet for leaks?", "Put a few drops of food coloring in the tank and wait 10 minutes without flushing. If color appears in the bowl, WaterSense says you have a leak. Flush afterward to avoid staining."),
       ("What share of indoor water do toilets use?", "EPA WaterSense says toilets are the largest single user of water inside a typical home, accounting for nearly 30 percent of indoor water use."),
       ("How do I check my whole house for leaks?", "WaterSense suggests reading your water meter before and after a two-hour period when no water is being used. If the reading changes, you probably have a leak."),
       ("How can my winter water bill reveal leaks?", "WaterSense says to look at water use in a cold month like January or February. If a family of four uses more than 12,000 gallons a month, there could be serious leaks.")]
BODY = f'''<p class="answer">If your toilet was made before the current federal standard, it may use as much as 6 gallons per flush. EPA WaterSense says replacing old toilets with WaterSense-labeled models, which use 1.28 gallons or less, can cut toilet water use by 20 to 60 percent: nearly 13,000 gallons and more than $170 a year for a home. Before replacing anything, run the 10-minute dye test to see whether your toilet is simply leaking.</p>

<p>Toilets don&rsquo;t get much attention until they run, clog or crack. But according to the U.S. Environmental Protection Agency&rsquo;s WaterSense program, toilets are the largest single user of water inside a typical home, accounting for nearly 30 percent of indoor water use. That makes an old toilet one of the easiest places to save water. Here&rsquo;s how to tell what you have and when an upgrade makes sense.</p>

<h2>How much water toilets use</h2>
<p>WaterSense lays out three numbers worth knowing:</p>
<ul>
<li><strong>Older toilets:</strong> can use as much as 6 gallons per flush, which WaterSense calls a major source of wasted water.</li>
<li><strong>The federal standard:</strong> 1.6 gallons per flush for toilets sold today.</li>
<li><strong>WaterSense-labeled toilets:</strong> 1.28 gallons per flush or less, 20 percent below the federal standard.</li>
</ul>
<p>The difference compounds with every person in the house and every flush, every day. Our <a href="@/#tool">toilet water calculator</a> shows what it adds up to over a year for your household.</p>

<h2>Finding your toilet&rsquo;s flush volume</h2>
<p>Many toilets have the gallons per flush (gpf) or liters per flush printed on the porcelain, often just behind the seat hinge or inside the tank on the back wall. If you see 3.5 gpf or higher, or no marking at all on an older fixture, you likely have one of the thirstier models WaterSense describes. A toilet marked 1.6 gpf meets today&rsquo;s federal standard; one marked 1.28 or lower matches the WaterSense level.</p>

<h2>What replacing an old toilet saves</h2>
<p>WaterSense estimates that replacing old, inefficient toilets with WaterSense-labeled models could reduce the water used for toilets by 20 to 60 percent. For a typical home, it puts that at nearly 13,000 gallons of water a year, and says households could save more than $170 a year in water costs.</p>
<p>Your own savings depend on how old your current toilets are, how many people live in the home and how often the toilets are used, which is exactly what the calculator lets you adjust.</p>

<h2>Leaks: the other half of the story</h2>
<p>An efficient toilet that leaks isn&rsquo;t efficient. WaterSense&rsquo;s Fix a Leak Week materials note that the average household&rsquo;s leaks can account for more than 9,300 gallons of water wasted every year, and that nine percent of homes have leaks wasting 50 gallons or more per day. Nationwide, it estimates household leaks waste nearly 1 trillion gallons a year.</p>
<p>A running or silently leaking toilet is a common culprit, and it&rsquo;s easy to check.</p>

<h3>The 10-minute dye test</h3>
<ol>
<li>Put a few drops of food coloring in the toilet tank.</li>
<li>Wait 10 minutes without flushing.</li>
<li>Look in the bowl. If any color shows up, WaterSense says you have a leak.</li>
<li>Flush right away afterward so the coloring doesn&rsquo;t stain the tank.</li>
</ol>
<p>A dye test result isn&rsquo;t automatically a reason to replace the fixture. It is a reason to have it looked at.</p>

<h3>Check the whole house</h3>
<p>WaterSense suggests two more checks. Read your water meter before and after a two-hour period when no water is being used; if the reading changes, you probably have a leak somewhere. And look at your water use in a cold month such as January or February: if a family of four uses more than 12,000 gallons a month, there could be serious leaks.</p>

<h2>Signs it may be time to replace</h2>
<ul>
<li>The toilet is an older model using 3.5 gallons or more per flush.</li>
<li>It keeps leaking or running after repairs.</li>
<li>The porcelain is cracked.</li>
<li>You&rsquo;re remodeling the bathroom anyway.</li>
</ul>
<p>When you do replace, look for the WaterSense label, which tells you the toilet uses 1.28 gallons per flush or less.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>A running toilet, a leak or a replacement in Salt Lake City? Call Gross Family Plumbing LLC at <a href="tel:+13853311988">385-331-1988</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA WaterSense, <a href="https://www.epa.gov/watersense/residential-toilets" rel="noopener">Residential Toilets</a> (updated May 29, 2026)</li>
<li>U.S. EPA WaterSense, <a href="https://www.epa.gov/watersense/fix-leak-week" rel="noopener">Fix a Leak Week</a> (updated March 13, 2026)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Salt Lake City skyline &middot; Invictus323, CC BY 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Replacing a toilet", H1, "From the blog &middot; Oct 23, 2026", "Blog", "When to Replace a Toilet: WaterSense Guide | Gross Family",
                  "When to replace a toilet: older models use up to 6 gallons a flush, WaterSense toilets 1.28. Save nearly 13,000 gallons a year, plus a simple leak test.",
                  BODY, image="hero", alt="Salt Lake City skyline", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
