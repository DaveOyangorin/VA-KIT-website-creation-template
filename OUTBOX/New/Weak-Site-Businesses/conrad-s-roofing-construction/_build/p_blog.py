"""New post (23 Oct 2026): how much snow a roof can hold. Informational; doesn't target "roofing company lehi". Sources: Maine Emergency
Management Agency, "Removing Snow from Roofs" (citing IBHS); FEMA P-957 Snow Load Safety Guidance flyer (2014)."""
from engine import faq_html, faq_ld, canon

SLUG = "how-much-snow-can-a-roof-hold/"
H1 = "How much snow can a roof hold? Weights, warning signs and safe removal"
FAQ = [("How much does snow weigh on a roof?", "By IBHS&rsquo;s rules of thumb, 10 to 12 inches of new snow or 3 to 5 inches of old snow equals about an inch of water, roughly 5 pounds per square foot. An inch of ice is about the same as a foot of fresh snow."),
       ("How much weight can a typical roof handle?", "IBHS estimates about 20 pounds per square foot of additional weight for a typical roof, and less for an older home or older roof."),
       ("What are the warning signs of too much snow?", "FEMA lists sagging ceilings or roof members, popping or cracking noises, bowing trusses, doors or windows that won&rsquo;t open or close, cracks in walls, split wood and severe leaks."),
       ("Is it safe to shovel my own roof?", "FEMA says snow removal is dangerous and should only be done by qualified people. Maine Emergency Management suggests a roof rake from the ground and saying no to ladders.")]
BODY = f'''<p class="answer">A typical roof can handle about 20 pounds per square foot of extra weight, according to the Insurance Institute for Business &amp; Home Safety (IBHS), and less if the roof is older. That&rsquo;s roughly 4 feet of fresh snow or 2 feet of old, packed snow. Watch for sagging, cracking sounds and sticking doors, and if you see them, get out and call a professional.</p>

<p>Utah winters can stack snow on a roof storm after storm, and what&rsquo;s up there changes as it settles, melts and refreezes. It helps to know how to estimate the weight, what signs say a roof is struggling, and why climbing up with a shovel is usually the wrong answer.</p>

<h2>What snow weighs</h2>
<p>The Maine Emergency Management Agency publishes a set of rules of thumb from IBHS that translate snow depth into weight:</p>
<ul>
<li><strong>Fresh snow:</strong> 10 to 12 inches of new snow equals about one inch of water, or about 5 pounds per square foot of roof. So you could have up to 4 feet of new snow before a typical roof becomes stressed.</li>
<li><strong>Packed snow:</strong> 3 to 5 inches of old snow equals about one inch of water, again about 5 pounds per square foot. So more than 2 feet of old snow could be too much for a typical roof.</li>
<li><strong>Ice:</strong> one inch of ice equals about one foot of fresh snow, or about 5 pounds per square foot.</li>
</ul>
<p>The layers add up. The same guidance gives an example: two feet of old snow plus two feet of new snow could weigh as much as 60 pounds per square foot, beyond the typical snow load capacity of most roofs. Our <a href="@/#tool">snow load calculator</a> does this math for you.</p>

<h2>How much a roof can take</h2>
<p>IBHS estimates the typical roof can handle 20 pounds per square foot of additional weight. If you have an older home or an older roof, especially one that has had problems before, the guidance suggests figuring on less than 20 pounds.</p>
<p>Roof shape matters too. FEMA&rsquo;s snow load guidance explains that simple roofs with steep slopes shed snow most easily, while roofs with irregular shapes collect drifts unevenly. It names flat roofs with parapets, stepped roofs, saw-tooth roofs and roofs with obstructions such as equipment or chimneys.</p>

<h2>Why snow loads become dangerous</h2>
<p>FEMA lists several ways roof snow can overload a structure:</p>
<ul>
<li><strong>Drifting and sliding snow.</strong> When snow builds up at different depths in different places, it creates high, concentrated loads.</li>
<li><strong>Rain on snow.</strong> Heavy rain on top of snow can saturate it and significantly increase the load.</li>
<li><strong>Melt between storms.</strong> If roof drainage is blocked, ice dams can form, concentrating weight at the eaves and making it harder for a sloped roof to shed snow. On flat or low-slope roofs, meltwater can pool in low areas.</li>
</ul>

<h2>Warning signs of an overstressed roof</h2>
<p>FEMA says overstressed roofs typically show warning signs before failure. Its list includes:</p>
<ul>
<li>Sagging ceiling tiles or boards, or ceiling boards falling out of a ceiling grid</li>
<li>Sagging sprinkler lines, or sprinkler heads deflecting below suspended ceilings</li>
<li>Popping, cracking and creaking noises</li>
<li>Sagging roof members, including metal decking or plywood sheathing</li>
<li>Bowing truss bottom chords or web members</li>
<li>Doors and windows that can no longer be opened or closed</li>
<li>Cracked or split wood members</li>
<li>Cracks in walls or masonry</li>
<li>Severe roof leaks</li>
<li>Water collecting where it shouldn&rsquo;t on low-slope roofs</li>
</ul>
<p>FEMA&rsquo;s instruction is direct: if any of these signs are observed, the building should be promptly evacuated and a local building authority or a qualified design professional should be contacted to perform a detailed structural inspection.</p>

<h2>Removing snow safely</h2>
<p>FEMA warns that snow removal is a dangerous activity that should only be done by qualified individuals following safety protocols, and that if there&rsquo;s any concern the roof could collapse, all removal should stop and the building should be evacuated.</p>
<p>For homeowners clearing small amounts from a pitched roof, the Maine guidance suggests:</p>
<ul>
<li>Consider hiring professionals; heights plus ice make this one of the more dangerous house chores.</li>
<li>Use a snow rake from the ground, stand well back, and rake small amounts at a time, starting from the edge.</li>
<li>Leave 2 to 3 inches of snow on the roof rather than scraping it clean, which can damage shingles.</li>
<li>Remember that an aluminum rake conducts electricity; stay well away from where power lines enter the house.</li>
<li>Say no to ladders, and keep gutters, drains and downspouts clear.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Worried about your roof this winter in Lehi or Utah Valley? Call Conrad&rsquo;s Roofing &amp; Construction at <a href="tel:+14353753396">435-375-3396</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Maine Emergency Management Agency, <a href="https://www.maine.gov/mema/hazards/natural-hazards/severe-winter-storms/roof-snow-removal" rel="noopener">Removing Snow from Roofs</a> (citing the Insurance Institute for Business &amp; Home Safety)</li>
<li>FEMA, <a href="https://www.fema.gov/sites/default/files/2020-07/fema_snow_load_2014.pdf" rel="noopener">Snow Load Safety Guidance, FEMA P-957</a> (flyer, 2014)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Mount Timpanogos and Utah Valley &middot; Ken Lund, CC BY-SA 2.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Roof snow load", H1, "From the blog &middot; Oct 23, 2026", "Blog", "How Much Snow Can a Roof Hold? | Conrad's Roofing, Lehi",
                  "How much snow a roof can hold: IBHS's 20 psf rule of thumb, what fresh snow, packed snow and ice weigh, FEMA's warning signs and safe removal.",
                  BODY, image="hero", alt="Mount Timpanogos and Utah Valley in snow", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": K.C.NAME}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
