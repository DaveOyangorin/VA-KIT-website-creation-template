"""New blog post for actionyardcare.com (22 Oct 2026): how high to mow a Utah lawn, and why to leave the clippings. Informational; it
doesn't target "landscaping murray", lawn care, mowing or aeration service keywords. Sources: USU Extension "Basic Turfgrass Care"
(Kopp and Johnson, March 2011); USU Extension "Training Turfgrass for Drought Resilience" (Kopp and Goodspeed, April 2026)."""
from engine import faq_html, faq_ld, canon

SLUG = "how-high-to-mow-a-utah-lawn/"
H1 = "How high should you mow a Utah lawn?"
FAQ = [("What height should I mow my lawn in Utah?", "USU Extension says common Utah lawn grasses can be mowed at 2 to 4 inches, and recommends about 3 inches to improve heat and drought tolerance."),
       ("What is the one-third rule?", "Never cut off more than one third of the grass blade&rsquo;s length in a single mowing. If the lawn is overgrown, lower the height gradually over several mowings."),
       ("Should I bag my grass clippings?", "USU Extension recommends returning or mulching clippings whenever possible: they return nitrogen to the soil and help reduce evaporation."),
       ("When does mowing season run in northern Utah?", "USU Extension lists March to November for the northern region and February to November for the southern region.")]
BODY = f'''<p class="answer">Mow most Utah lawns at about 3 inches. USU Extension says common lawn grasses can be cut anywhere from 2 to 4 inches, but 3 inches improves heat and drought tolerance. Never take off more than a third of the blade at once, mow shady areas a little higher, and leave the clippings on the lawn.</p>

<p>Mowing is the job everyone does and almost nobody thinks about. But how high you cut changes how deep the roots grow, how much water the lawn needs and how many weeds move in. Utah State University Extension has published clear numbers for Utah lawns. Here they are.</p>

<h2>The number: about 3 inches</h2>
<p>In its fact sheet <em>Basic Turfgrass Care</em>, USU Extension says the common lawn species in Utah can all be mowed at a height of <strong>2 to 4 inches</strong>, and recommends mowing at <strong>3 inches to improve heat and drought tolerance</strong>.</p>
<p>The reason is simple: in USU&rsquo;s words, <em>taller grass means deeper roots</em>. Deeper roots reach more of the water in the soil, which matters in a dry Utah summer.</p>
<p>USU&rsquo;s newer fact sheet on drought resilience (April 2026) makes the same point from another angle: a higher mowing height helps shade the soil surface, reduce evaporation and support deeper rooting.</p>

<h2>Why not just cut it short?</h2>
<p>A short cut looks tidy for a day, but it works against the lawn. Cutting low removes the leaf area grass uses to feed itself, exposes more soil to the sun (USU&rsquo;s 2026 fact sheet notes a higher cut shades the soil and reduces evaporation), and, by USU&rsquo;s logic that taller grass means deeper roots, leaves you with a shallower-rooted lawn that needs water more often.</p>

<h2>The rule: never cut more than one third</h2>
<p>USU Extension&rsquo;s rule is to <strong>never mow more than one third of the total length of the grass blades off at a time</strong>. If you want a 3-inch lawn, mow before the grass passes about 4&frac12; inches.</p>
<p>Fell behind after a vacation or a wet spring? Don&rsquo;t scalp it all at once. USU advises lowering the height <strong>gradually over several mowings</strong>.</p>

<h2>Shade: mow a little higher</h2>
<p>Grass in the shade needs more leaf to collect the light it gets. USU Extension recommends mowing shaded areas higher than sunny ones. If part of your yard sits under mature trees or on the north side of the house, set the deck a notch up there.</p>

<h2>Leave the clippings</h2>
<p>Bagging clippings is extra work you can usually skip. USU Extension says to <strong>return or mulch the clippings whenever possible</strong>, because they return nitrogen to the soil and help decrease evaporation. The 2026 drought fact sheet lists returning clippings as one of the ways to build healthier soil and deeper roots.</p>

<h2>Mowing as weed control</h2>
<p>It sounds too easy, but USU Extension states that <strong>proper mowing controls most weeds</strong>.</p>

<h2>When to mow in Utah</h2>
<p>USU Extension lists the mowing season as <strong>March to November</strong> in the northern region and February to November in the southern region. Growth speeds up and slows down with the weather, so mow by the height of the grass, not the calendar: when it&rsquo;s about a third taller than your target, it&rsquo;s time.</p>

<h2>Mowing works with watering</h2>
<p>Height and water go together. USU&rsquo;s turfgrass guidance recommends watering in the early morning when it&rsquo;s cool and calm, avoiding 10 AM to 6 PM, and applying between &frac12; and 1 inch of water per irrigation. A lawn mowed at 3 inches with deep roots makes the most of every one of those waterings. And if drought pushes the lawn dormant and golden, USU notes it recovers when water returns; just keep heavy traffic off it in the meantime.</p>

<h2>Fertilizing and aeration fit around mowing</h2>
<p>A lawn mowed at the right height still needs feeding. USU Extension says cool-season grasses need 2 to 5 pounds of nitrogen per 1,000 square feet a year, but typical home lawns under moderate maintenance need only 2 to 3 pounds; the higher end is for intensively used turf. Timing follows the grass&rsquo;s growth pattern, and USU lists April, June and October for both regions.</p>
<p>Aeration helps water soak in and reduces compaction and thatch. USU&rsquo;s windows for the northern region are March to May and September to October. The April 2026 drought fact sheet also lists aeration to relieve compaction, along with appropriate fertilization, among the practices that support deeper rooting.</p>
<p>Put together, that&rsquo;s a simple rhythm for a northern Utah lawn: mow at about 3 inches from March through November, feed in April, June and October, aerate in spring or early fall, and water deeply in the cool early morning.</p>

<h2>Quick checklist</h2>
<ul>
<li>Set the mower to about 3 inches (anywhere from 2 to 4 works for common Utah grasses).</li>
<li>Never remove more than a third of the blade in one cut.</li>
<li>Lower an overgrown lawn gradually over several mowings.</li>
<li>Mow shaded areas a little higher.</li>
<li>Leave or mulch the clippings.</li>
<li>Mow by height, from about March to November in northern Utah.</li>
<li>Fertilize in April, June and October; typical home lawns need only 2&ndash;3 lbs of nitrogen per 1,000 sq ft a year.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Rather hand the mower to someone else? Action Lawn &amp; Yardcare does weekly lawn mowing with string trimming and edging across Murray and the Salt Lake Valley. Call <a href="tel:+18012444035">801-244-4035</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Kelly Kopp and Paul Johnson, USU Extension, <a href="https://extension.usu.edu/yardandgarden/research/basic-turfgrass-care" rel="noopener">Basic Turfgrass Care</a> (March 2011)</li>
<li>Kelly Kopp and Jerry Goodspeed, USU Extension, <a href="https://extension.usu.edu/cwel/research/training-turfgrass-for-drought-resilience" rel="noopener">Training Turfgrass for Drought Resilience</a> (April 2026)</li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Mowing height", H1, "From the blog &middot; Oct 22, 2026", "Blog", "How High to Mow a Utah Lawn (and Leave Clippings) | Action",
                  "How high to mow a Utah lawn: USU Extension's 2 to 4 inch range, why 3 inches helps in drought, the one-third rule, shade, and leaving the clippings.",
                  BODY, image="ay-leaves", alt="Action crew on a yard clean up", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Action Lawn & Yardcare"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
