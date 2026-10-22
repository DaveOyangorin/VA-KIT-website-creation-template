"""New blog post for m3industriesconcrete.com (/post/..., like their other posts).
"Cutting or Grinding Concrete Yourself? Read This About Silica Dust First"
Main phrase: "concrete silica dust" (informational, safety). None of their 12 posts covers it; the services it touches (repairs and
replacements, control joints, coatings prep, cleaning) are linked, not targeted.
Facts and sources, checked 20 Oct 2026 (fetched and read):
- OSHA, "Silica, Crystalline" (https://www.osha.gov/silica-crystalline): crystalline silica is in sand, stone, concrete and
  mortar; respirable particles (at least 100 times smaller than ordinary sand) are created when cutting, sawing, grinding,
  drilling and crushing stone, rock, concrete, brick, block and mortar; about 2.3 million people in the U.S. are exposed at work;
  diseases: silicosis (incurable, can lead to disability and death), lung cancer, COPD, kidney disease.
- OSHA, "Silica, Crystalline: Health Effects" (https://www.osha.gov/silica-crystalline/health-effects): silica dust in the
  lungs causes scar tissue that makes it hard to take in oxygen; there is no cure for silicosis.
- OSHA, "Silica, Crystalline: Construction" (https://www.osha.gov/silica-crystalline/construction): the construction standard;
  Table 1 controls; written exposure control plan; a competent person; restrict housekeeping practices that expose workers where
  alternatives exist; "Applying water to a saw blade when cutting materials that contain crystalline silica ... substantially
  reduces the amount of dust created"; fact sheets for handheld power saws, grinders, walk-behind saws, jackhammers, drills.
- The client's own text: proper control joints; removal of old concrete before installation; coatings over existing concrete.
OSHA rules apply to employers and workers; the post is clear a homeowner is not covered but faces the same dust. No prices."""
from engine import faq_html, faq_ld, canon
from cfg import U, NAME

POST = ("Cutting or Grinding Concrete Yourself? Read This About Silica Dust First", "post/concrete-silica-dust-diy/")
O1 = "https://www.osha.gov/silica-crystalline"
O2 = "https://www.osha.gov/silica-crystalline/health-effects"
O3 = "https://www.osha.gov/silica-crystalline/construction"
FAQ = [("Is concrete dust dangerous?", f'The fine dust from cutting, grinding or drilling concrete contains respirable crystalline silica. <a href="{O1}" rel="noopener">OSHA</a> lists silicosis, lung cancer, COPD and kidney disease among the diseases linked to breathing it.'),
       ("Does wetting concrete really help?", f'Yes. OSHA says applying water to a saw blade when cutting materials that contain crystalline silica, such as concrete, substantially reduces the amount of dust created.'),
       ("Should I sweep up concrete dust?", "Dry sweeping and blowing it around puts the fine dust back in the air. OSHA&rsquo;s construction rule restricts those housekeeping practices on job sites where better options exist; wetting it down or using a vacuum with a proper filter is the safer approach.")]


def post():
    return f'''<p class="answer">Concrete looks harmless until you cut it. Sawing, grinding, drilling or breaking concrete throws off a fine dust that contains crystalline silica, and breathing it is linked to serious lung disease. If you are planning to cut a control joint, grind down a trip edge, break out an old slab or prep a floor for a coating yourself, here is what to know first.</p>
<p>We cut, grind and break concrete every week in St. George, and dust control is part of every one of those jobs. This isn&rsquo;t a reason to panic about a sidewalk. It is a reason to treat a concrete saw with more respect than a circular saw.</p>
<h2>What silica is, and where the dust comes from</h2>
<p>According to <a href="{O1}" rel="noopener">OSHA</a>, crystalline silica is a common mineral in the earth&rsquo;s crust, and sand, stone, concrete and mortar all contain it. The dangerous form is <b>respirable</b> crystalline silica: particles at least 100 times smaller than ordinary sand. They are created when you cut, saw, grind, drill or crush stone, rock, concrete, brick, block and mortar.</p>
<p>That covers most of the jobs people try themselves:</p>
<ul><li>Cutting control joints or saw-cutting a slab to remove a section.</li>
<li>Grinding down a lifted edge or a high spot.</li>
<li>Drilling anchors into a slab or a block wall.</li>
<li>Breaking out an old patio or walkway with a jackhammer.</li>
<li>Grinding a garage floor before a coating goes down.</li></ul>
<h2>Why it matters</h2>
<p>OSHA lists the diseases linked to breathing respirable crystalline silica: <b>silicosis</b>, an incurable lung disease that can lead to disability and death; <b>lung cancer</b>; <b>chronic obstructive pulmonary disease (COPD)</b>; and <b>kidney disease</b>. Its <a href="{O2}" rel="noopener">health effects page</a> explains why silicosis is so serious: silica dust in the lungs causes scar tissue, which makes it hard for the lungs to take in oxygen, and there is no cure.</p>
<p>It is common enough at work that OSHA estimates about 2.3 million people in the U.S. are exposed to silica on the job. That is why it has a dedicated standard for construction.</p>
<h2>What the pros are required to do</h2>
<p>OSHA&rsquo;s <a href="{O3}" rel="noopener">respirable crystalline silica standard for construction</a> applies to employers and their workers, not to homeowners. But what it asks of a contractor is a useful checklist for anyone holding a saw. Covered employers must, among other things:</p>
<ul><li>Use the dust controls listed for each task in the standard&rsquo;s Table 1 (or measure exposure and control it to the limit).</li>
<li>Have a written exposure control plan, and a competent person to carry it out.</li>
<li>Restrict housekeeping practices that expose workers to silica, such as dry sweeping, where better alternatives are available.</li>
<li>Train workers on which tasks create silica dust and how to limit it.</li></ul>
<p>OSHA publishes task-by-task fact sheets for the tools in Table 1, including handheld power saws, handheld grinders, walk-behind saws, jackhammers and drills.</p>
<h2>The single biggest fix: water</h2>
<p>In OSHA&rsquo;s own words, applying water to a saw blade when cutting materials that contain crystalline silica, such as stone, rock, concrete, brick and block, substantially reduces the amount of dust created. That is why concrete crews cut wet: a hose or a water feed on the blade turns most of the dust into slurry.</p>
<p>The other common control is a vacuum dust collector attached to the tool, which is how grinders and drills are usually run indoors, where a hose isn&rsquo;t practical.</p>
<h2>It isn&rsquo;t only concrete</h2>
<p>The same advice applies well beyond the driveway. OSHA lists brick, block, mortar, stone and rock alongside concrete as sources of respirable silica when they are cut, drilled or crushed, and notes that crystalline silica is also used to make products such as glass, pottery, ceramics, bricks and artificial stone. In a typical St. George project that means the block retaining wall, the pavers around a pool, the stone veneer on a column and an engineered stone countertop all deserve the same respect as the slab. Mortar is a common one: grinding out old mortar joints is listed among the activities that create the dust.</p>
<h2>If you are doing it yourself</h2>
<ul><li><b>Cut wet whenever you can.</b> Use a saw set up for water, or keep a steady stream on the cut. Mind electricity: use tools rated for wet cutting and keep cords out of the slurry.</li>
<li><b>Work outside,</b> with the wind at your back, and keep children, pets and neighbors away from the dust.</li>
<li><b>Indoors, use a tool with dust collection</b> connected to a vacuum with a proper filter, rather than a shop vac with a standard filter.</li>
<li><b>Protect your lungs.</b> A respirator rated for fine dust does far more than a paper nuisance mask.</li>
<li><b>Clean up wet or with a filtered vacuum.</b> Don&rsquo;t dry sweep or blow the dust around with a leaf blower or compressed air.</li>
<li><b>Wash slurry off</b> before it dries on the driveway, and keep it out of storm drains.</li></ul>
<h2>When to hand it off</h2>
<p>Small, one-off cuts are within reach of a careful homeowner with the right saw. Large demolition, long runs of control joints, grinding a whole garage floor before a coating, or anything indoors in a living space is where a crew with wet-cutting equipment and dust collection makes the job faster, cleaner and safer. That work is part of our <a href="@/service-page/concrete-repairs-replacements/">concrete repairs and replacements</a>, our <a href="@/concrete-coatings-st-george/">coatings</a> prep, and every new <a href="@/concrete-driveway-patio/">driveway or patio</a>, where proper control joints are cut as part of the finish.</p>
<p>Call (435) 701-0081 for a free estimate. We&rsquo;ll tell you honestly whether it is a job worth doing yourself.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{O1}" rel="noopener">OSHA, &ldquo;Silica, Crystalline&rdquo;</a>; <a href="{O2}" rel="noopener">OSHA, &ldquo;Silica, Crystalline: Health Effects&rdquo;</a>; <a href="{O3}" rel="noopener">OSHA, &ldquo;Silica, Crystalline: Construction&rdquo;</a>. OSHA&rsquo;s standard applies to employers and workers.</p>'''


def page(K):
    p = K.page(POST[1], "Silica dust", POST[0], f"From the {NAME} blog &middot; October 20, 2026", "Blog", "Concrete Silica Dust: Cutting & Grinding Safely | M3 Industries",
               "Cutting, grinding or drilling concrete makes respirable silica dust. What OSHA says about the risks, why crews cut wet, and how to do small jobs more safely.",
               post(), image="m3-screed", alt="M3 Industries crew working a fresh concrete slab", crumbs=[("Blog", "blog/")], ogtype="article")
    p["body"] = p["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    p["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                  "image": U + "assets/img/m3-screed.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    return p
