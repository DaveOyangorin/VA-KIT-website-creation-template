"""New blog post for poly-lift.com (their posts sit at the site root, e.g. /sinking-foundation-repair/, so this one does too).
"When Is an Uneven Sidewalk a Trip Hazard? The Quarter-Inch Rule, Explained"
Main phrase: "uneven sidewalk trip hazard" (informational). No page targets it: the leveling page and city pages target
"concrete leveling/lifting"; the post links to them, to the sealing page and to the foam-lifting article, without competing.
Facts and sources, checked 20 Oct 2026 (fetched and read):
- U.S. Access Board, 2010 ADA Standards for Accessible Design (https://www.access-board.gov/ada/): 302.1 floor and ground surfaces
  stable, firm and slip resistant; 303.2 changes in level of 1/4 inch high maximum may be vertical; 303.3 between 1/4 and 1/2 inch
  must be beveled no steeper than 1:2 (advisory: 1/4 vertical plus 1/4 beveled, combined never over 1/2 inch); 303.4 greater than
  1/2 inch must be ramped (405/406); 403.3 walking surfaces: running slope no steeper than 1:20, cross slope no steeper than 1:48.
- The ADA Standards apply to places covered by the ADA (businesses open to the public, state and local government); a private
  house is not covered, but the numbers are the published reference for what a "change in level" means.
- The client's own text: causes of settling (base compaction, freeze-thaw heave and settle, drought/expansive clay, erosion from
  water and sewer lines and downspouts, vibration, slab curl); "It is unsafe to have raised concrete"; most lifting jobs done in
  less than a day and ready immediately; cracked concrete can be leveled; sealing after lifting; usually around 50% or less than
  replacing.
No city sidewalk-ordinance claims (Logan's could not be confirmed): readers are told to check with their city. No prices."""
from engine import faq_html, faq_ld, canon, img
from cfg import U, NAME

POST = ("When Is an Uneven Sidewalk a Trip Hazard? The Quarter-Inch Rule, Explained", "uneven-sidewalk-trip-hazard/")
ADA = "https://www.access-board.gov/ada/"
FAQ = [("How high does a sidewalk lip have to be to count as a trip hazard?", f'There is no single legal number for every sidewalk, but the <a href="{ADA}" rel="noopener">2010 ADA Standards</a> are the common reference: a change in level of up to 1/4 inch may be vertical, 1/4 to 1/2 inch must be beveled, and more than 1/2 inch must be ramped. A lip past a quarter inch is where most people start paying attention.'),
       ("Does the ADA apply to my home's sidewalk?", "The ADA Standards apply to places the ADA covers, such as businesses open to the public and state and local government facilities. A private house is generally not covered, but the same numbers are a useful yardstick for what is safe to walk on."),
       ("Can a cracked, sunken slab be lifted, or does it need replacing?", "Cracked concrete can be leveled. Lifting usually costs around 50% or less than replacing, and most jobs are done in less than a day.")]


def post():
    return f'''<p class="answer">A sidewalk becomes a trip hazard long before it looks dramatic. The published reference point is small: under the 2010 ADA Standards for Accessible Design, a change in level of more than a quarter of an inch can no longer be a plain vertical edge. Past half an inch, it needs a ramp. Here is what those numbers mean, why slabs in Cache Valley drift out of them, and what can be done.</p>
<p>We lift sunken sidewalks, driveways, steps and garage floors around Logan and across Utah. The question people ask most often isn&rsquo;t how the foam works. It is &ldquo;is this bad enough to fix?&rdquo; This is the honest way to answer it.</p>
<h2>The numbers: what the ADA Standards say</h2>
<p>The U.S. Access Board publishes the <a href="{ADA}" rel="noopener">2010 ADA Standards</a>. Section 303 covers &ldquo;changes in level&rdquo;, which is the technical name for a lip between two slabs:</p>
<ul><li><b>Up to 1/4 inch</b> may be vertical (303.2). A plain edge that small is allowed.</li>
<li><b>Between 1/4 and 1/2 inch</b> must be beveled, with a slope no steeper than 1:2 (303.3). The standard&rsquo;s own note: a quarter inch vertical plus a quarter inch beveled, never more than half an inch combined.</li>
<li><b>More than 1/2 inch</b> must be ramped (303.4), which on a sidewalk in practice means the slabs need to be brought back into line.</li></ul>
<p>The same standards ask that walking surfaces be stable, firm and slip resistant (302.1), with a running slope no steeper than 1:20 and a cross slope no steeper than 1:48 (403.3). A slab that has tipped toward a house or a gutter can fail the cross-slope number even with no lip at all.</p>
<h2>Does that apply to your sidewalk?</h2>
<p>Strictly, the ADA Standards apply to places the ADA covers: businesses open to the public, and state and local government facilities. A private home&rsquo;s walkway generally isn&rsquo;t covered. But the numbers are the clearest published answer to &ldquo;how much is too much&rdquo;, and they are a good yardstick for a front walk that a grandparent, a stroller or a delivery driver uses every day. For a business, an HOA or a property manager, they matter more directly.</p>
<p>Who has to repair the public sidewalk in front of a property varies from city to city. If the slab is in the park strip or along the street, check with your city before doing anything.</p>
<h2>Why slabs here drift out of level</h2>
<p>Concrete doesn&rsquo;t usually sink because of the concrete. It sinks because of what is under it:</p>
<ul><li><b>The base.</b> If the base under a slab was never compacted properly, the slab settles as it cures and gets heavier, and that can happen quickly.</li>
<li><b>Freeze and thaw.</b> When frost is in the ground, it expands and heaves slabs up. When it melts, they settle, often not back to where they started. That is how trip spots appear after a winter.</li>
<li><b>Water.</b> Damaged water or sewer lines, and downspouts that pour water next to a slab, wash out the base material and leave voids.</li>
<li><b>Dry spells.</b> Drought can shrink expansive clay soils under a slab, and wet conditions can make them swell again.</li></ul>
<p>Once one slab drops, the joint next to it becomes the lip. Water then gets into that joint and under the slab, and the problem tends to grow.</p>
<h2>How to measure a lip yourself</h2>
<ol><li>Lay a straight board or a level across the joint, resting on the higher slab.</li>
<li>Measure the gap down to the lower slab with a tape or ruler.</li>
<li>Note anything over a quarter inch, and anything over half an inch especially.</li>
<li>While you are there, check whether the slab tilts toward the house. Water running back toward a foundation is a second problem.</li></ol>
<p>Take a photo with the tape in it. It makes an estimate faster and gives you a record of whether the slab is still moving.</p>
<h2>The fixes, from smallest to largest</h2>
<ul><li><b>Grinding</b> can take down a small lip on a slab that is otherwise sound and not moving. It doesn&rsquo;t fix what is under it.</li>
<li><b>Lifting</b> raises the sunken slab back into line by filling the void under it. Our method, <a href="@/concrete-leveling-and-lifting/">Deep Foamjection</a>, injects polyurethane foam through small holes. The foam is light compared with grout, the slab can be used almost straight away, and most jobs take less than a day. Cracked slabs can be lifted too.</li>
<li><b>Replacing</b> is the answer when a slab is broken up beyond repair. It costs more and takes longer; lifting is usually around half the cost of replacement or less.</li></ul>
<p>After a lift, <a href="@/concrete-sealing/">sealing</a> the surface and the joints helps keep water out of the base, which is what started the trouble in the first place.</p>
<h2>When to call</h2>
<p>If a lip is past a quarter inch, if it is getting bigger each spring, or if a slab is tipping toward your house, it is worth an estimate. We&rsquo;ll look at the slab, tell you whether lifting is the right fix, and give you the number. Read more about <a href="@/polyurethane-foam-concrete-lifting/">how effective polyurethane foam is for lifting concrete</a>.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Source: <a href="{ADA}" rel="noopener">U.S. Access Board, 2010 ADA Standards for Accessible Design</a>, sections 302.1, 303.2&ndash;303.4 and 403.3. Who repairs public sidewalks varies by city: check with yours.</p>'''


def page(K):
    p = K.page(POST[1], "Trip hazards", POST[0], f"From the {NAME} blog &middot; October 20, 2026", "Blog", "Uneven Sidewalk Trip Hazard: The 1/4-Inch Rule | Poly-Lift",
               "When does an uneven sidewalk become a trip hazard? The ADA's 1/4-inch and 1/2-inch rules, why slabs in Cache Valley sink, how to measure, and the fixes.",
               post(), image="pl-sidewalk-concrete-raised-before-and-after", alt="A sidewalk before and after being raised by Poly-Lift", crumbs=[("Blog", "blog/")], faqs=None, ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/pl-sidewalk-concrete-raised-before-and-after.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    return p
