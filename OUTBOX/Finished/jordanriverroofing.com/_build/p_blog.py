import re, html as h
from build import U, S, ARROW, CONTACT, BLOG, img, faq_html, faq_ld, crumbs_ld, cta, phero, canon

# New post. The site has no blog; /blog/<slug> follows the site's existing folder-style URLs.
# Main keyword: "ridge vent vs turtle vents" (+ box vents vs ridge vent, can you mix roof vents, attic ventilation requirements).
# Ties to the attic ventilation service and a real customer review (Ket Knok: other bidders "wanted to keep the old inefficient turtle vents").
# Not targeted (owned by other pages, linked only): roofing company taylorsville (home), roof replacement/repair taylorsville,
# attic ventilation & skylights taylorsville (service page). No overlap with earlier kit posts.
TITLE, PATH = BLOG
PHRC = "https://www.phrc.psu.edu/assets/docs/Webinars/PHRC-Webinar_Attic-Ventilation-Understanding-the-Why_HANDOUTS.pdf"
AIRVENT = "https://help.gibraltarbuildingproducts.com/en/knowledge/is-mixing-exhaust-vents-of-any-combination-ridge-vents-roof-louvers-wind-turbines-gable-louvers-and-power-fans-on-the-same-roof-when-its-a-common-attic-ok-to-do"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"

FAQ = [
    ("Is a ridge vent better than turtle vents?",
     "On a roof with enough ridge length and good soffit intake, a continuous ridge vent usually ventilates the attic more evenly than a few box vents. On hip roofs with very short ridges, box vents may still be the practical choice. Either way, the system needs balanced intake low on the roof."),
    ("Can I have a ridge vent and turtle vents on the same roof?",
     f"The vent manufacturer Air Vent says no: it doesn&rsquo;t recommend mixing two types of exhaust vents on the same roof over a common attic, because one can act as an intake for the other and short-circuit the airflow (<a href=\"{AIRVENT}\" rel=\"noopener\">Air Vent</a>)."),
    ("How much attic ventilation do I need?",
     "The International Residential Code&rsquo;s baseline is 1 square foot of net free vent area for every 150 square feet of attic. It can drop to 1 per 300 when certain conditions are met, such as putting 40&ndash;50% of the vent area high in the attic, within 3 feet of the ridge."),
    ("When is the best time to switch to a ridge vent?",
     "During a re-roof. The ridge is already open, the old box vents come off with the old shingles, and the holes can be decked over before the new roof goes on."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> a <strong>ridge vent</strong> runs continuously along the peak of the roof; <strong>turtle vents</strong> (box vents) are individual openings cut into the roof near the top. With enough ridge length and good soffit intake, a ridge vent usually ventilates an attic more evenly. Just don&rsquo;t combine the two over the same attic: the vent maker Air Vent warns that mixing exhaust types can short-circuit the airflow.</div>

<p>One of our customers, Ket, put it bluntly in a review. Other roofers who bid on the job &ldquo;didn&rsquo;t even include the new ridge venting system. These bidders wanted to keep the old inefficient turtle vents, slap the roof on and run.&rdquo;</p>
<p>It&rsquo;s a common situation in the Salt Lake Valley, where plenty of homes still have a row of box vents near the top of the roof. Here&rsquo;s how the two systems differ, what the building code asks for, and why you shouldn&rsquo;t simply add one to the other.</p>

<h2>What attic ventilation is for</h2>
<p>A vented attic works like a chimney. Cooler outside air comes in low, through vents in the soffits under the eaves, and warm, moist air leaves high, near the ridge. That steady flow does two jobs:</p>
<ul>
<li><strong>In summer</strong>, it carries heat out of the attic, which is easier on the shingles and the roof deck.</li>
<li><strong>In winter</strong>, it carries out moisture from the house and keeps the roof deck cold and even, which helps stop the uneven snow melt that leads to ice dams along the eaves.</li>
</ul>
<p>The key word is <em>balanced</em>. Exhaust vents at the top can only move as much air as the intake vents at the bottom let in.</p>

<h2>Turtle vents (box vents)</h2>
<p>Turtle vents are the low, square hoods you see in a row near the top of many roofs. Each one covers a hole cut through the roof deck. They&rsquo;re simple and they work on almost any roof shape, including hip roofs with very little ridge.</p>
<p>The drawback is coverage. Each box vent pulls air from the area right around it, so an attic with a handful of them can have spots where air barely moves. Every vent is also another hole in the roof that has to be flashed and kept watertight.</p>

<h2>Ridge vents</h2>
<p>A ridge vent is a continuous vent along the peak of the roof. The roofer cuts a slot in the deck on each side of the ridge, and a low vent, usually covered with ridge cap shingles, sits over it. From the street it mostly disappears into the roofline.</p>
<p>Because it runs the length of the ridge, it draws air evenly along the whole top of the attic, from the soffit vents below. It needs two things to work well: enough ridge length to provide the vent area, and enough soffit intake to feed it.</p>

<figure>{img("victorian-home-reroof", "Crew re-roofing a two-story Victorian home")}<figcaption>A re-roof is the natural time to rethink the ventilation, as on this Victorian.</figcaption></figure>

<h2>Why you shouldn&rsquo;t mix them</h2>
<p>It&rsquo;s tempting to add a ridge vent and leave the old turtle vents in place: more vents, more airflow. The vent maker says otherwise. Air Vent&rsquo;s guidance is that it doesn&rsquo;t recommend mixing two types of exhaust vents on the same roof when it&rsquo;s a common attic, because it could short-circuit the attic ventilation system (<a href="{AIRVENT}" rel="noopener">Air Vent</a>).</p>
<p>What happens is that one exhaust vent starts acting as an intake for the other. A ridge vent can pull air in through the nearby box vents instead of from the soffits, so the lower part of the attic gets bypassed, and the box vents can let in weather. A Penn State housing research center webinar makes the same point: adding a vent product to supplement the ridge &ldquo;may in fact be introducing new intake location&rdquo; (<a href="{PHRC}" rel="noopener">PHRC, Penn State</a>).</p>

<h2>How much ventilation the code asks for</h2>
<p>Utah adopted the 2021 International Residential Code for homes, effective July 1, 2023 (<a href="{ICC}" rel="noopener">International Code Council</a>). The code&rsquo;s attic ventilation section, R806, is quoted from the 2018 edition in Penn State PHRC&rsquo;s attic ventilation webinar handout (<a href="{PHRC}" rel="noopener">PHRC, October 2022</a>):</p>
<ul>
<li><strong>Baseline:</strong> the minimum net free ventilating area is 1/150 of the area of the vented space.</li>
<li><strong>Exception:</strong> it can be 1/300 when one or more conditions are met. One is that 40&ndash;50% of the required vent area is in the upper part of the attic, no more than 3 feet below the ridge, with the rest at the eaves.</li>
<li><strong>Air space:</strong> at least 1 inch of space between the insulation and the roof sheathing at the vents.</li>
</ul>
<p>As a worked example, a 1,500-square-foot attic at 1/150 needs 10 square feet (1,440 square inches) of net free vent area. With the 1/300 exception it needs 5 square feet (720 square inches), split roughly half high at the ridge and half low at the soffits. Each vent product lists its net free area per piece or per foot, which is how a roofer sizes the system. Your city&rsquo;s building department enforces the code edition it has adopted, so it has the final say on local details.</p>

<h2>Which one is right for your roof?</h2>
<p>For most gable roofs with a decent ridge and room for soffit vents, a continuous ridge vent with matching soffit intake is the cleaner, more even system. For hip roofs with short ridges, or attics that can&rsquo;t get enough intake, box vents may still make sense, as long as they aren&rsquo;t mixed with another type of exhaust vent over the same attic.</p>
<p>The right time to change is during a re-roof. The old box vents come off with the old shingles, the holes get decked over, and the ridge is already open. Another customer, Kevin, wrote that our crew &ldquo;helped me achieve a fully ventilated attic space&rdquo; on his re-roof.</p>
<p>If you&rsquo;re in Taylorsville or anywhere in the Salt Lake Valley and want your attic ventilation looked at, call <a href="tel:{S["tel"]}">{S["phone"]}</a> for a free inspection, or read more about our <a href="@/services/attic-ventilation-skylights">attic ventilation and skylight work</a>.</p>

<h2>Frequently asked questions</h2>
{faq_html(FAQ)}

<p class="sources"><strong>Sources:</strong> <a href="{AIRVENT}" rel="noopener">Air Vent (Gibraltar Building Products): mixing exhaust vents over a common attic</a> &middot; <a href="{PHRC}" rel="noopener">Pennsylvania Housing Research Center, Penn State: &ldquo;Attic Ventilation: Understanding the Why&rdquo; webinar handout, 7 October 2022 (quotes 2018 IRC R806.2 and R806.3)</a> &middot; <a href="{ICC}" rel="noopener">International Code Council: Utah adopts the 2021 I-Codes</a>. Checked 17 October 2026.</p>
'''


def page():
    trail = [("Home", ""), ("Guide", PATH)]
    lede = "How the two exhaust systems differ, what the building code asks for, and why adding a ridge vent to old turtle vents can make ventilation worse."
    body = phero(trail, TITLE, lede, "Jordan River Roofing guide") + f'''
<section class="sec"><div class="wrap split top post-grid"><article class="prose post reveal">
<p class="byline mono">By Jordan River Roofing &middot; Taylorsville, Utah &middot; 17 October 2026</p>{ART}</article>
<aside class="side reveal"><div class="card navy"><p class="label light">Free inspection</p><h3>Not sure what&rsquo;s venting your attic?</h3><p>We&rsquo;ll check intake and exhaust when we inspect your roof.</p>
<a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn lime" href="@/{CONTACT}">Request an inspection {ARROW}</a></div>
<ul class="side-links"><li><a href="@/services/attic-ventilation-skylights">Attic ventilation &amp; skylights</a></li><li><a href="@/services/new-roof-replacement">Roof replacement</a></li><li><a href="@/warranties">DiamondShield warranty</a></li></ul></aside>
</div></section>''' + cta()
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", h.unescape(re.sub(r"<[^>]+>", " ", ART))))
    return {"path": PATH, "title": "Ridge Vent vs. Turtle Vents: Which Is Better? | Jordan River",
            "meta": "Ridge vent vs. turtle (box) vents: how each works, why you shouldn't mix them over one attic, and the code's 1/150 and 1/300 attic ventilation rules.",
            "body": body, "og": "victorian-home-reroof", "ogtype": "article", "full_biz": False, "words": words,
            "schema": [crumbs_ld(PATH, trail), faq_ld(FAQ),
                       {"@type": "BlogPosting", "@id": canon(PATH) + "#article", "headline": TITLE, "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": U + "/#business"}, "publisher": {"@id": U + "/#business"}, "mainEntityOfPage": canon(PATH),
                        "image": U + "/assets/img/victorian-home-reroof.webp", "wordCount": words, "inLanguage": "en-US",
                        "about": ["Ridge vent", "Box vent", "Attic ventilation"], "citation": [AIRVENT, PHRC, ICC]}]}
