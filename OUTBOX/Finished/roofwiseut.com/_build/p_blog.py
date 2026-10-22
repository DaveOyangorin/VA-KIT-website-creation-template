import re, html as h
from build import U, S, ARROW, SCHED, BLOG, DISCLAIMER, img, faq_html, faq_ld, crumbs_ld, cta, phero, canon, notice

# New post. The site has no blog; /blog/<slug> follows the site's existing folder-style URLs.
# Main keyword: "what does hail damage look like on a roof" (+ hail damage roof signs, hail damage shingles, roof hail inspection).
# Ties to the client's focus on storm damage and insurance. Not targeted (owned by other pages, linked only):
# roofing company salt lake city (home), roof repair salt lake city, roof insurance claims (insurance-claims page).
TITLE, PATH = BLOG
NWS = "https://www.weather.gov/mlb/hail_rules"
IBHS = "https://ibhs.org/ImpactRatings"
IJ = "https://www.insurancejournal.com/news/southeast/2025/10/02/842108.htm"
UID = "https://insurance.utah.gov/consumers/home-insurance/home-claims-info/"

FAQ = [
    ("What size hail damages a roof?",
     f"The National Weather Service treats hail of 1 inch (quarter size) or larger as severe. Research from the Insurance Institute for Business &amp; Home Safety suggests repeated smaller hail can wear shingles too, by knocking off granules over time (<a href=\"{IJ}\" rel=\"noopener\">Insurance Journal</a>)."),
    ("Can you see hail damage from the ground?",
     "Sometimes you can see clues: dents in gutters, downspouts and metal vents, and shingle granules collecting at the downspouts. The shingles themselves usually need a closer look by someone on the roof."),
    ("Should I climb on my roof to check for hail damage?",
     "No. Check what you can safely from the ground and have a roofer inspect the roof itself."),
    ("Does homeowner&rsquo;s insurance cover hail damage?",
     f"It depends on your policy. {DISCLAIMER}"),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> on asphalt shingles, hail damage usually shows up as <strong>spots where the granules have been knocked off</strong>, <strong>dents or bruises</strong> in the shingle, and sometimes <strong>cracks or tears</strong>. From the ground, look for dented gutters, downspouts and metal vents, and for granules washing out of the downspouts. Hail of 1 inch (quarter size) or larger is what the National Weather Service calls severe.</div>

<p>After a hail storm along the Wasatch Front, the question we hear first is simple: did it damage my roof? From the driveway, a roof often looks fine. The damage, if there is any, is in the shingles up close.</p>
<p>Here&rsquo;s what hail does to a shingle roof, what you can check safely from the ground, and what to do next.</p>

<h2>How big does hail have to be?</h2>
<p>The National Weather Service uses everyday objects to describe hail size. Its Melbourne, Florida office publishes this scale (<a href="{NWS}" rel="noopener">NWS: hail size</a>):</p>
<div class="tablebox"><table><thead><tr><th>Category</th><th>Size</th></tr></thead><tbody>
<tr><td>Non-severe</td><td>Pea (about 1/4&Prime;), marble (1/2&Prime;), dime, nickel or penny (about 3/4&Prime;)</td></tr>
<tr><td>Severe</td><td>Quarter (about 1&Prime;), half dollar (1 1/4&Prime;), walnut (1 1/2&Prime;), golf ball (1 3/4&Prime;)</td></tr>
<tr><td>Significant severe</td><td>Hen egg (2&Prime;), tennis ball (2 1/2&Prime;), baseball (2 3/4&Prime;) and larger</td></tr>
</tbody></table></div>
<p>A thunderstorm counts as severe when it produces hail at least the size of a quarter, 1 inch, or winds of 58 mph or more.</p>

<h3>Smaller hail still matters</h3>
<p>A study published in 2025 by researchers at the Insurance Institute for Business &amp; Home Safety (IBHS) tested hail smaller than an inch on asphalt shingles. In a series of tests, the cumulative granule loss from those small impacts was greater than the granule loss from a single 2-inch hailstone (<a href="{IJ}" rel="noopener">Insurance Journal, 2 October 2025</a>). The researchers suggest that repeated small-hail storms may knock off enough granules to speed up the aging of a roof.</p>

<h2>What hail damage looks like on shingles</h2>
<p>IBHS, which rates shingles for hail resistance, describes the damage it measures as ranging from granule loss and dents to surface cracks and, at the worst, a fully compromised shingle (<a href="{IBHS}" rel="noopener">IBHS hail impact ratings</a>). On a real roof, that looks like:</p>
<ul>
<li><strong>Granule loss:</strong> dark spots where the gritty top layer has been knocked off, exposing the black asphalt underneath. Granules protect the asphalt from the sun.</li>
<li><strong>Dents and bruises:</strong> round marks where the shingle has been dented. Pressing on a bruise can feel soft compared with the shingle around it.</li>
<li><strong>Cracks and tears:</strong> splits in the shingle from a hard hit, which can let water through.</li>
<li><strong>Damage on the metal:</strong> dents in vents, flashing and drip edge on the roof.</li>
</ul>
<p>Hail marks tend to be scattered randomly across the slopes that faced the storm. Wear from age is usually more even, which is one reason an inspection matters before deciding what the damage is.</p>

<figure>{img("drone-reroof-crew-on-roof", "Drone view of a RoofWise re-roof in progress on a hillside home")}<figcaption>A RoofWise re-roof, seen from the drone. Up close is where hail damage shows.</figcaption></figure>

<h2>Hail damage or normal aging?</h2>
<p>Not every worn-looking shingle was hit by hail. Older roofs lose granules gradually, and shingles can blister, curl or crack with age and sun. The differences an inspector looks for:</p>
<ul>
<li><strong>Pattern:</strong> hail hits are scattered and concentrated on the slopes that faced the storm; aging tends to show across the whole roof, often worst on the sunniest side.</li>
<li><strong>Shape:</strong> a hail mark is usually a roughly round spot or dent; age shows up as curling edges, cracking along the shingle or a generally thin, worn surface.</li>
<li><strong>Timing:</strong> damage that wasn&rsquo;t there before a known storm, with dented metal and granules in the downspouts after it, points to hail.</li>
</ul>
<p>That&rsquo;s also why the cause matters for insurance: storm damage and wear from age are usually treated very differently by a policy.</p>

<h2>What happens during a RoofWise inspection</h2>
<p>It follows the same four steps as any RoofWise job: you schedule a time, a roofing professional inspects the roof for visible signs of damage, we explain what we found and, where it&rsquo;s relevant, the roofing side of the insurance process, and if work is needed you get a clear plan for it.</p>

<h2>What you can check from the ground</h2>
<p>Don&rsquo;t climb onto the roof. Instead, walk around the house and look for:</p>
<ul>
<li>Dents in gutters, downspouts, metal vents and window wraps</li>
<li>Shingle granules collecting at the bottom of downspouts or in the gutters</li>
<li>Pieces of shingle in the yard</li>
<li>Dings in siding, window screens, fences and outdoor furniture</li>
<li>New water stains on ceilings, especially upstairs</li>
</ul>
<p>Photograph what you find and note the date of the storm.</p>

<h2>What to do next</h2>
<p>The Utah Insurance Department&rsquo;s advice for home damage claims (<a href="{UID}" rel="noopener">insurance.utah.gov</a>) is to contact your insurance company or agent as soon as possible, take photos or video of the damage, make temporary repairs to prevent more damage, and keep every receipt. It also says not to have permanent repairs made until the insurer has inspected the property and you&rsquo;ve agreed on repair costs.</p>
<p>A roof inspection fits in at the start. RoofWise inspects the roof, documents visible damage and explains the findings, so you can decide whether an insurance conversation makes sense.</p>
{notice(DISCLAIMER)}

<h2>Choosing shingles for next time</h2>
<p>If you&rsquo;re replacing a roof anyway, hail resistance is worth asking about. IBHS publishes ratings that compare how shingle products hold up to realistic hail impacts (<a href="{IBHS}" rel="noopener">IBHS hail impact ratings</a>).</p>
<p>Had a storm in Salt Lake City or anywhere in Northern Utah? <a href="@/{SCHED}">Schedule an inspection</a> or call <a href="tel:{S["tel"]}">{S["phone"]}</a>. More on how claims work on our <a href="@/insurance-claims">insurance claims page</a>.</p>

<h2>Frequently asked questions</h2>
{faq_html(FAQ)}

<p class="sources"><strong>Sources:</strong> <a href="{NWS}" rel="noopener">National Weather Service (Melbourne, FL office): hail size and severe criteria</a> &middot; <a href="{IJ}" rel="noopener">Insurance Journal, 2 October 2025: IBHS study on sub-severe hail (published in Frontiers in Materials)</a> &middot; <a href="{IBHS}" rel="noopener">IBHS: Hail Impact-Resistant Shingle Ratings</a> &middot; <a href="{UID}" rel="noopener">Utah Insurance Department: home claims information</a>. Checked 17 October 2026.</p>
'''


def page():
    trail = [("Home", ""), ("Hail damage guide", PATH)]
    lede = "What hail does to a shingle roof, what you can safely check from the ground after a storm, and what to do next."
    items = []
    def h2(m):
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        sid = re.sub(r"[^a-z0-9]+", "-", h.unescape(t).lower()).strip("-")[:48]
        items.append((sid, t)); return f'<h2 id="{sid}">{m.group(1)}</h2>'
    art = re.sub(r"<h2>(.*?)</h2>", h2, ART)
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    body = phero(trail, TITLE, lede, "RoofWise guide", [("Topic", "Hail &amp; storm damage"), ("Area", "Salt Lake City &amp; Northern Utah"), ("Checked", "17 October 2026")], buttons=False) + f'''
<section class="sec article"><div class="wrap art-grid"><aside class="art-side"><nav class="toc" aria-label="In this article"><p class="label">In this article</p><ol>{toc}</ol></nav>
<div class="panel dark"><p class="label light">After a storm</p><h3>Not sure if the hail hurt your roof?</h3><a class="btn" href="@/{SCHED}">Schedule Inspection {ARROW}</a><p class="small">Or call <a href="tel:{S["tel"]}">{S["phone"]}</a></p></div></aside>
<article class="prose post reveal"><p class="byline">By <b>RoofWise</b> &middot; Salt Lake City, Utah &middot; 17 October 2026 &middot; 6 min read</p>{art}</article>
</div></section>''' + cta()
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", h.unescape(re.sub(r"<[^>]+>", " ", ART))))
    return {"path": PATH, "title": "What Does Hail Damage Look Like on a Roof? | RoofWise",
            "meta": "What hail damage looks like on a shingle roof: granule loss, dents and cracks, what to check from the ground, hail sizes, and what to do next in Utah.",
            "body": body, "og": "drone-reroof-crew-on-roof", "ogtype": "article", "full_biz": False, "words": words,
            "schema": [crumbs_ld(PATH, trail), faq_ld(FAQ),
                       {"@type": "BlogPosting", "@id": canon(PATH) + "#article", "headline": TITLE, "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": U + "/#business"}, "publisher": {"@id": U + "/#business"}, "mainEntityOfPage": canon(PATH),
                        "image": U + "/assets/img/drone-reroof-crew-on-roof.webp", "wordCount": words, "inLanguage": "en-US",
                        "about": ["Hail damage", "Roof inspection", "Asphalt shingles"], "citation": [NWS, IJ, IBHS, UID]}]}
