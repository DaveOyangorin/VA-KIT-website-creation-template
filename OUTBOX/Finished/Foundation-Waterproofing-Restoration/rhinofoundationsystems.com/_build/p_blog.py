"""New blog post for rhinofoundationsystems.com (the live site has no blog posts beyond the WordPress default).
"Radon and Foundation Cracks: What Utah Homeowners Should Know"
Main phrase: "radon foundation cracks" (informational). No service page covers radon; the post links to foundation repair,
basement waterproofing and crawl space encapsulation without competing for them, and does not claim Rhino does radon testing or
mitigation (it points readers to EPA guidance and to testing).
Facts and sources, fetched and read 20 Oct 2026:
- EPA, "What is Radon?" (https://www.epa.gov/radon/what-radon): a radioactive gas that forms naturally when uranium, thorium or
  radium break down in rocks, soil and groundwater; people are exposed mainly by breathing radon that comes through cracks and
  gaps in buildings and homes; because it comes from the earth, people are always exposed to some.
- EPA, "What is EPA's Action Level for Radon and What Does it Mean?" (https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean):
  fix the home at 4 pCi/L (150 Bq/m3) or more; consider fixing between 2 and 4 pCi/L because there is no known safe level; the
  average indoor level in U.S. homes is about 1.3 pCi/L and outdoor air about 0.4 pCi/L; links to "A Citizen's Guide to Radon"
  and "Consumer's Guide to Radon Reduction: How to Fix Your Home".
- EPA, "Health Risk of Radon" (https://www.epa.gov/radon/health-risk-radon): radon is the number one cause of lung cancer among
  non-smokers (EPA estimate) and the second leading cause overall; about 21,000 lung cancer deaths a year, about 2,900 among
  people who never smoked; a smoker also exposed to radon has a much higher risk; U.S. Surgeon General national health advisory,
  13 January 2005.
- Rhino's own text: horizontal foundation cracks, drywall and foundation wall cracks, water in the basement or crawl space,
  temperature swings making cracks worse; clay, silt and sand behaviour.
No prices. No Utah radon statistics (the state sources could not be reached and checked)."""
from engine import faq_html, faq_ld, canon
from cfg import U, NAME

POST = ("Radon and Foundation Cracks: What Utah Homeowners Should Know", "blog/radon-foundation-cracks/")
WHAT = "https://www.epa.gov/radon/what-radon"
ACT = "https://www.epa.gov/radon/what-epas-action-level-radon-and-what-does-it-mean"
RISK = "https://www.epa.gov/radon/health-risk-radon"
FAQ = [("Do foundation cracks cause radon?", f'No. Radon comes from the natural breakdown of uranium, thorium and radium in rock, soil and groundwater. But the <a href="{WHAT}" rel="noopener">EPA</a> says people are exposed mainly through radon that comes into buildings through cracks and gaps, so cracks are one of the ways it gets in.'),
       ("What radon level is too high?", f'The <a href="{ACT}" rel="noopener">EPA</a> recommends fixing a home at 4 pCi/L or more, and considering a fix between 2 and 4 pCi/L, because there is no known safe level of exposure.'),
       ("Will repairing my foundation fix a radon problem?", "Don&rsquo;t assume it will. Repairing cracks fixes a structural problem; whether radon is still an issue is something only a test can tell you. Test before and after any work, and follow the EPA&rsquo;s radon reduction guidance if the level is high.")]


def post():
    return f'''<p class="answer">Radon is a gas you can&rsquo;t see or smell, and it comes from the ground under every home. The <a href="{WHAT}" rel="noopener">U.S. Environmental Protection Agency</a> says people are exposed to it mainly by breathing radon that comes into buildings through cracks and gaps. That puts it in the same conversation as foundation cracks, damp crawl spaces and basement leaks, even though a foundation contractor isn&rsquo;t the person who measures it. Here is what the EPA says, and what to do about it.</p>

<h2>What radon is, in plain terms</h2>
<p>According to the <a href="{WHAT}" rel="noopener">EPA</a>, radon is a radioactive gas that forms naturally when uranium, thorium or radium, radioactive metals found in rock, soil and groundwater, break down. Because it comes straight out of the earth, everyone is exposed to some of it all the time. Outdoors it disperses. Indoors, it can collect.</p>
<p>The <a href="{ACT}" rel="noopener">EPA puts it this way</a>: radon is in outdoor air and in the indoor air of buildings of every kind. The average outdoor level is about 0.4 picocuries per liter (pCi/L). The average indoor level in American homes is about 1.3 pCi/L, roughly three times higher. The difference is the building: the house sits on the soil the gas comes from, and the gas follows the easiest path inside.</p>

<h2>Why it matters</h2>
<p>The reason the EPA cares about a gas you can&rsquo;t sense is lung cancer. On its <a href="{RISK}" rel="noopener">health risk page</a>, the agency says radon is the number one cause of lung cancer among people who don&rsquo;t smoke, by EPA estimates, and the second leading cause overall after smoking. It estimates about 21,000 lung cancer deaths a year from radon, about 2,900 of them among people who have never smoked. For smokers, the risk compounds: a smoker who is also exposed to radon has a much higher risk.</p>
<p>The U.S. Surgeon General issued a national health advisory on radon on 13 January 2005. This isn&rsquo;t a fringe concern. It is a standard part of knowing what is going on in a house.</p>

<h2>How radon gets in: the cracks-and-gaps problem</h2>
<p>Here is where foundations come in. The EPA&rsquo;s summary is short: radon comes into buildings and homes through cracks and gaps. A house that sits tight on the ground gives it fewer ways in. A house with a cracked foundation wall, open gaps where the slab meets the wall, or a crawl space open to the soil gives it more.</p>
<p>Those are the same openings we look for when we inspect a foundation for other reasons. Settlement cracks, a horizontal crack in a basement wall, cracks in drywall that track down to the foundation, or a crawl space that stays damp: every one of them is a sign the house has moved or water is getting in. They are also paths between the soil and the air you breathe.</p>
<p>Soil plays a part in both stories. Clay expands when it&rsquo;s wet and shrinks when it dries. Silt holds water and heaves with frost. Sand shifts under load. Every one of those movements works on a foundation over the years, and movement opens cracks. Temperature swings in a wet basement or crawl space make existing cracks worse over time.</p>

<h2>What the numbers mean</h2>
<p>Radon is measured in picocuries per liter of air. The EPA&rsquo;s guidance, from its <a href="{ACT}" rel="noopener">action level page</a>, has three useful numbers:</p>
<ul>
<li><strong>4 pCi/L or more:</strong> the EPA recommends fixing the home.</li>
<li><strong>Between 2 and 4 pCi/L:</strong> the EPA recommends considering a fix, because there is no known safe level of exposure.</li>
<li><strong>About 1.3 pCi/L:</strong> the average indoor level in U.S. homes, the figure the EPA based its lung cancer estimate on.</li>
</ul>
<p>The point is that nobody can tell you your number by looking at the house. Two houses on the same street can test very differently. The only way to know is to test.</p>

<h2>A sensible order of operations</h2>
<p>If you have both foundation concerns and radon questions, the two jobs are related but separate. Here is a practical way to handle them.</p>
<h3>1. Test first</h3>
<p>Get a radon test result for the lowest lived-in level of the house before anything changes. That is your baseline. The EPA&rsquo;s &ldquo;A Citizen&rsquo;s Guide to Radon&rdquo;, linked from its <a href="{ACT}" rel="noopener">action level page</a>, is the place to start.</p>
<h3>2. Deal with structural and water problems on their own merits</h3>
<p>A horizontal crack in a basement wall, bowing walls, sticking doors and windows, or water in the basement are reasons to have the foundation looked at whether or not radon is a factor. Fix what needs fixing for the house&rsquo;s sake: <a href="@/foundation-repair/">foundation repair</a> for movement and cracks, <a href="@/basement-waterproofing/">basement waterproofing</a> for leaks and seepage, <a href="@/crawl-space-encapsulation/">crawl space encapsulation</a> for a damp crawl space.</p>
<h3>3. Don&rsquo;t assume the radon is solved</h3>
<p>Repairing a foundation or sealing a crawl space changes how a house meets the ground. It is reasonable to hope that helps, but it isn&rsquo;t a radon fix by definition, and nobody should promise you it is. Test again after the work. If the level is still at or above the EPA&rsquo;s action level, follow the agency&rsquo;s &ldquo;Consumer&rsquo;s Guide to Radon Reduction: How to Fix Your Home&rdquo;, which is written for exactly that decision.</p>
<h3>4. Keep testing over time</h3>
<p>Houses keep moving, slowly. Soil gets wetter and drier with the seasons and freezes and thaws through Utah winters. A crack that wasn&rsquo;t there five years ago can be there now. Retesting after major work, and from time to time, is the only way to keep the number honest.</p>

<h2>Signs worth a closer look</h2>
<p>None of these tells you anything about radon by itself. They tell you the house is moving or taking on water, which is worth knowing for its own sake, and they are openings between the soil and the house:</p>
<ul>
<li>Horizontal cracks in a basement or foundation wall</li>
<li>Cracks in drywall, especially ones that keep growing</li>
<li>Walls that bow or lean, or are misaligned at the top or bottom</li>
<li>Doors and windows that start to stick</li>
<li>Water pooling in the basement or crawl space, or a crawl space that stays damp</li>
</ul>
<p>If you see any of them, call 801-509-5344 for a free consultation and estimate on the foundation side. For the radon side, test, and use the EPA&rsquo;s guidance to decide what comes next.</p>

<div class="sources"><h3>Sources</h3><ul>
<li>U.S. EPA, <a href="{WHAT}" rel="noopener">What is Radon?</a></li>
<li>U.S. EPA, <a href="{ACT}" rel="noopener">What is EPA&rsquo;s Action Level for Radon and What Does it Mean?</a></li>
<li>U.S. EPA, <a href="{RISK}" rel="noopener">Health Risk of Radon</a></li>
</ul><p>The soil and warning-sign descriptions are Rhino Foundation Systems&rsquo; own. This article is general information, not medical or testing advice.</p></div>'''


def page(K):
    p = POST[1]
    schema = [{"@type": "BlogPosting", "@id": canon(p) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
               "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p), "image": U + "assets/img/wall-crack-door.webp"}]
    return K.page(p, "Radon and foundation cracks", POST[0], "Published 20 October 2026 &middot; Sources: U.S. EPA", "Blog",
                  "Radon and Foundation Cracks in Utah | Rhino Foundation Systems",
                  "Radon gets into homes through cracks and gaps, the EPA says. What the numbers mean, how it links to foundation cracks, and why to test before and after repairs.",
                  post(), image="wall-crack-door", alt="A crack running up the wall from a door frame", faqs=FAQ, schema=schema, ogtype="article")
