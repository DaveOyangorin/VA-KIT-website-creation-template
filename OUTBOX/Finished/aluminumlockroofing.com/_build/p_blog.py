from build import U, BIZ_ID, S, ARROW, PHONE, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

PATH = "blog/can-you-put-a-new-roof-over-an-old-roof/"
FIRESTONE = "https://www.firestoneco.gov/DocumentCenter/View/9461/Firestone-Reroof-Requirements-2018-IRC-updated-81123"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"
FHB = "https://www.finehomebuilding.com/project-guides/roofing/ice-barriers-explained-far-roof-slope"

# Main keyword: "can you put a new roof over an old roof" (informational, long-tail, blog only).
# Supporting: roof over vs tear off, how many layers of shingles are allowed, metal roof over shingles.
# Not targeted here (owned by current/future service pages, linked only): roofing company salt lake city (home),
# roof installation / roof replacement / metal roofing salt lake city (pages the client still has to confirm).
# Topic chosen because the client's own FAQ answers it, and "How long do roofs last in Utah?" is reserved
# for the future metal roofing page per the 5 Oct audit.

FAQ = [
    ("How many layers of roofing are allowed in Utah?",
     "Utah uses the International Residential Code. Under its re-roofing rules, if the existing roof already has two or more layers of roof covering, all of the old material has to come off; a roof-over isn't allowed. Your city or county building department enforces this, so check with them for your project."),
    ("Is it cheaper to put a new roof over an old one?",
     "A roof-over usually avoids the labor and disposal cost of tearing off the old layer, so it can cost less up front. The trade-off is that nobody gets to see or fix the decking underneath. Ask any roofer to price both options and explain what each estimate includes."),
    ("Can aluminum shingles go over existing asphalt shingles?",
     "Sometimes. Aluminum Lock Roofing says a roof-over may be possible on some homes, depending on the condition of the existing roof, the number of layers, the decking, local requirements and the installation instructions. The existing roof needs to be assessed before deciding."),
    ("Does a roof-over affect my warranty?",
     "It can. Manufacturers set their own installation requirements, and some products or warranties have specific rules about installing over an existing roof. Ask for the applicable written warranty and confirm which terms apply to your materials and installation before you choose."),
    ("Do I need a permit to re-roof?",
     "Most cities require a permit for re-roofing, whether it's a tear-off or a roof-over, and the inspector checks the code requirements. Rules vary, so call your local building department before work starts. Your roofer should know the process in the cities they work in."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> sometimes. A new roof can go over one existing layer if that roof is flat, dry and sound, the decking is solid, and the new product's instructions allow it. If there are already two or more layers, building code requires a full tear-off. Damaged, soaked or sagging roofs should come off no matter what.</div>

<p>When a roof is worn out, a roof-over can sound like an easy win: skip the tear-off, skip the dumpster, finish faster. Sometimes it is. Other times it buries problems you'll pay for later.</p>
<p>Here's how to tell which side of that line your roof is on, what the code says in Utah, and what to ask before anyone starts.</p>

<h2>What "roofing over" means</h2>
<p>A roof-over, also called a recover or overlay, means installing a new roof covering on top of the existing one instead of removing it first. A tear-off means stripping the old roof down to the decking, fixing anything underneath, and starting fresh.</p>
<p>Both are legitimate. The question is which one your roof can handle.</p>

<figure>{img("copper-aluminum-shingle-new-construction", "Copper-colored aluminum shingles being installed on a home")}<figcaption>Whatever goes on top, the roof only works if what's underneath is sound.</figcaption></figure>

<h2>What the building code says in Utah</h2>
<p>Utah adopted the <a href="{ICC}" rel="noopener">2021 International Residential Code</a> for homes. Its re-roofing section sets the main limit on roof-overs: <strong>where an existing roof already has two or more applications of any roof covering, all old material must be removed, and a roof recover isn't allowed.</strong> A Colorado city's reroofing checklist, which quotes the same section (R908.3.1.1 in the 2018 edition), puts it plainly: <a href="{FIRESTONE}" rel="noopener">"Roof recover is not allowed"</a> once there are two layers.</p>
<p>So the first question is simple: how many roofs are already up there? If the answer is two, the decision is made for you.</p>
<p>Your city or county building department is the final word. They issue the permit, enforce local amendments, and inspect the work, so call them early.</p>

<h2>When a roof-over can work</h2>
<p>If there's only one existing layer, a roof-over may be possible when all of these are true:</p>
<ul>
<li>The existing roof is dry, with no active leaks or soaked areas</li>
<li>The decking underneath is solid, with no soft spots or sagging</li>
<li>The surface is reasonably flat, without badly curled or buckled shingles</li>
<li>The roof structure can carry the added weight</li>
<li>The new roofing product's installation instructions allow it</li>
<li>Your local building department allows it for your project</li>
</ul>
<p>That last pair matters more than people expect. Every roofing system has its own installation instructions, and they decide what the product can go over and how. Aluminum Lock Roofing puts it this way on its own FAQ: the condition of the existing roof, the number of roof layers, decking, local requirements and installation instructions determine whether removal is needed.</p>

<h2>When the old roof has to come off</h2>
<p>A tear-off is the right call, and often the required one, when:</p>
<ul>
<li>There are already <strong>two or more layers</strong> of roofing</li>
<li>The roof has been leaking and the decking may be wet or rotted</li>
<li>You can see sagging, or the roof feels soft when walked on</li>
<li>Shingles are badly curled, cupped or buckled, so the new roof won't lie flat</li>
<li>The flashing, vents or ice protection at the eaves need to be redone properly</li>
<li>The new product's instructions or warranty require a bare deck</li>
</ul>
<p>The biggest hidden risk of a roof-over is what you can't see. Rot, old leak damage and failed flashing stay buried under the new roof, and they keep getting worse.</p>

<h2>Roof-over vs. tear-off at a glance</h2>
<div class="tablebox"><table>
<thead><tr><th></th><th>Roof-over</th><th>Tear-off</th></tr></thead>
<tbody>
<tr><td>Allowed with 2+ existing layers?</td><td>No</td><td>Yes (required)</td></tr>
<tr><td>Decking inspected and repaired?</td><td>No, it stays hidden</td><td>Yes</td></tr>
<tr><td>Added weight on the structure</td><td>Yes, old roof stays</td><td>No, old roof removed</td></tr>
<tr><td>Labor and disposal</td><td>Usually less</td><td>Usually more</td></tr>
<tr><td>Flashing and eave details</td><td>Limited by what's underneath</td><td>Can be redone from scratch</td></tr>
<tr><td>Best for</td><td>One sound, dry, flat layer</td><td>Two layers, damage, or any doubt</td></tr>
</tbody></table></div>

<h2>Weight: why lighter roofing helps</h2>
<p>Keeping the old roof means the structure carries both roofs, plus Utah snow. That's one reason the weight of the new material matters on a roof-over. Aluminum is a lightweight roofing option, though the roof structure, decking and complete assembly still need to be assessed on every project. Heavier products may rule a roof-over out entirely.</p>

<h2>Don't forget the edges and the ice</h2>
<p>A new roof is more than the field of shingles. Flashings at eaves, rakes, valleys, walls and penetrations do most of the work keeping water out, and on a roof-over they have to be fitted correctly over or around the old roof.</p>
<p>In snow country, the eaves need special attention. The residential code's ice barrier rule, which <a href="{FHB}" rel="noopener">Fine Homebuilding explains in detail</a>, calls for a waterproof membrane from the roof edge to at least 24 inches inside the exterior wall where ice dams are a known problem. Ask how that will be handled on your roof.</p>

<figure>{img("aluminum-shingle-home-deep-snow", "Home with an aluminum shingle roof surrounded by deep snow")}<figcaption>Snow load and ice at the eaves are part of the roof-over decision in Utah.</figcaption></figure>

<h2>Five questions to ask before you agree to a roof-over</h2>
<ol>
<li><strong>How many layers are on my roof now?</strong> Ask them to check, not guess.</li>
<li><strong>What condition is the decking in, and how do you know?</strong> Look for an attic check or core sample, not just a look from the ladder.</li>
<li><strong>Do the installation instructions allow this product over my existing roof?</strong></li>
<li><strong>How will flashing, vents and the eaves be handled?</strong></li>
<li><strong>What does the written warranty say about roof-overs?</strong> Get the terms before you sign.</li>
</ol>
<p>A good roofer will price both options if both are possible, and explain what each estimate includes, from preparation and any removal to materials and finishing details.</p>

<h2>Roof-over questions</h2>
{faq_html(FAQ)}

<h2>Thinking about an aluminum shingle roof?</h2>
<p>Aluminum Lock Roofing installs interlocking aluminum shingle roofs in Salt Lake City and sells aluminum roofing materials to roofers. Tell us your project location, your current roof type and what you want to accomplish, and we'll talk through whether a roof-over or a tear-off makes sense. See <a href="@/services/">our aluminum shingle roof installation</a>, read the <a href="@/faq/">FAQ</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a>.</p>

<h3>Sources</h3>
<ul style="font-size:.92rem">
<li>International Code Council: <a href="{ICC}" rel="noopener">Utah adopts the 2021 International Codes</a></li>
<li>Town of Firestone, Colorado: <a href="{FIRESTONE}" rel="noopener">Reroof requirements (2018 IRC)</a>, quoting IRC R908.3.1.1 and R905.1.2</li>
<li>Fine Homebuilding: <a href="{FHB}" rel="noopener">Ice barriers explained</a></li>
<li>Aluminum Lock Roofing: <a href="@/faq/">Roofing FAQ</a></li>
</ul>
'''


def pages():
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("Can You Put a New Roof Over an Old Roof?", PATH)]
    extra = '<div class="meta-line"><span>By Aluminum Lock Roofing</span><span>Published <time datetime="2026-10-17">October 17, 2026</time></span><span>About 8 minutes to read</span></div>'
    hero = phero(trail, "Can You Put a New Roof Over an Old Roof?", "When a roof-over works, when the old roof has to come off, and what Utah's building code says.",
                 "gray-aluminum-shingle-bungalow", "Small home with a gray aluminum shingle roof", "Roofing guide")
    hero = hero.replace('<div class="btn-row"', extra + '<div class="btn-row"', 1)
    rel = [("Aluminum shingle installation", "services/"), ("Roofing FAQ", "faq/"), ("About us", "about-us/"), ("Contact", "contact-us/")]
    post = {"path": PATH, "canonical": url, "modified": "2026-10-17", "ogtype": "article", "og": "gray-aluminum-shingle-bungalow", "full_biz": False,
            "title": "Can You Put a New Roof Over an Old Roof? | Aluminum Lock",
            "meta": "Can you put a new roof over an old roof? When a roof-over works, when Utah code requires a tear-off, and what to ask your roofer first. A plain guide.",
            "body": hero + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side(rel)}</div></section>'
                    + cta("Roof-over or tear-off?", "Tell us about your current roof and we'll talk through which approach fits."),
            "schema": [{"@type": "BlogPosting", "@id": url + "#article", "headline": "Can You Put a New Roof Over an Old Roof?", "url": url,
                        "mainEntityOfPage": url, "description": "When a roof-over works, when Utah code requires a tear-off, and what to ask your roofer.",
                        "image": U + "assets/img/gray-aluminum-shingle-bungalow.webp", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "inLanguage": "en-US", "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "isPartOf": {"@id": U + "blog/#blog"}},
                       faq_ld(FAQ), crumbs_ld(url, trail)]}
    idx = {"path": "blog/", "canonical": U + "blog/", "og": "copper-aluminum-shingle-log-home", "full_biz": False,
           "title": "Aluminum Roofing Blog | Aluminum Lock Roofing, Utah",
           "meta": "Guides on aluminum shingle roofing from Aluminum Lock Roofing in Salt Lake City: roof-overs, tear-offs, materials and planning your next new roof in Utah.",
           "body": phero([("Home", ""), ("Blog", "blog/")], "The Aluminum Lock Blog", "Plain guides on aluminum roofing and planning a new roof in Utah.",
                         "copper-aluminum-shingle-log-home", "Log home with a copper-colored aluminum shingle roof", "Blog")
                   + f'<section class="sec"><div class="wrap"><div class="grid"><a class="postcard reveal" href="@/{PATH}">{img("gray-aluminum-shingle-bungalow", "Home with a gray aluminum shingle roof")}<div class="in"><small>Oct 17, 2026 &middot; Roofing guide</small><b>Can You Put a New Roof Over an Old Roof?</b></div></a></div></div></section>' + cta(),
           "schema": [{"@type": "Blog", "@id": U + "blog/#blog", "url": U + "blog/", "name": "Aluminum Lock Roofing Blog", "publisher": {"@id": BIZ_ID}},
                      crumbs_ld(U + "blog/", [("Home", ""), ("Blog", "blog/")])]}
    return [idx, post]
