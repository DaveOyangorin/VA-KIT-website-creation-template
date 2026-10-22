import re, html as h
from build import U, S, ARROW, CONTACT, BLOG, img, faq_html, faq_ld, crumbs_ld, cta, phero

# New post. Main keyword: "tpo vs epdm vs pvc" (+ tpo vs epdm, pvc vs tpo roofing, best flat roof membrane commercial).
# Oakley installs all three (their commercial pages). No page on the site covers how they differ.
# Not targeted (owned by other pages, linked only): commercial roofing salt lake city (/commercial/),
# commercial roofing installation salt lake city (/commercial-roofing-installation/), roof repair salt lake city.
TITLE, PATH = BLOG
JM = "https://continuingeducation.bnpmedia.com/courses/johns-manville/understanding-single-ply-roofing-systems/2"
CS = "https://www.carlislesyntec.com/en/Resources/Media/Blog-Landing-Page/SpecTopics/2021/12/16/Understanding-ASTM-Standards-for-Roofing-Membranes"
UP = "https://up.codes/viewer/utah/ibc-2021/chapter/15/roof-assemblies-and-rooftop-structures"

FAQ = [
    ("What is the difference between TPO and EPDM?",
     f"TPO is a thermoplastic: it softens with heat, so its seams are welded together. EPDM is a thermoset rubber that can&rsquo;t be re-melted once cured, so its seams are joined with tape or adhesive (<a href=\"{JM}\" rel=\"noopener\">Johns Manville / BNP Media</a>)."),
    ("Is PVC better than TPO?",
     "Neither is better for every roof. Both are heat-welded thermoplastics. PVC resists oils and grease best, which makes it a common choice over restaurant kitchens and manufacturing exhaust; TPO is made without added plasticizers."),
    ("What slope does a single-ply roof need in Utah?",
     f"Utah adopted the 2021 International Building Code, which requires single-ply membrane roofs to have a design slope of at least 1/4 inch per foot, about 2 percent, for drainage (<a href=\"{UP}\" rel=\"noopener\">IBC 2021, Utah, Section 1507.12.1</a>)."),
    ("Can a new membrane go over my old roof?",
     f"Sometimes. The code doesn&rsquo;t allow a recover when the existing roof already has two or more layers of roof covering (<a href=\"{UP}\" rel=\"noopener\">Section 1512.2.1.1</a>). An inspection tells you which case you&rsquo;re in."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> all three are single-ply membranes for flat and low-slope roofs. <strong>TPO</strong> and <strong>PVC</strong> are thermoplastics with heat-welded seams; PVC is the one to pick where oil and grease reach the roof. <strong>EPDM</strong> is a rubber with taped or glued seams, comes in very wide sheets, and often costs less. The right one depends on what the building does, not on which membrane is &ldquo;best&rdquo;.</div>

<p>Most commercial roofs in the Salt Lake Valley, on offices, warehouses, retail and apartment buildings, are low-slope roofs covered with a single-ply membrane. Oakley Roofing installs all three of the common ones: TPO, EPDM and PVC. Building owners ask us which one they should choose, and the honest answer starts with how each one is made.</p>

<h2>What the three have in common</h2>
<p>TPO, EPDM and PVC are the most popular single-ply materials for low-slope roofs (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>). Each is a factory-made sheet laid over the roof deck, insulation and cover board, then joined at the seams and secured to the roof.</p>
<p>The building code treats them the same way on drainage. Utah adopted the 2021 International Building Code, which says single-ply membrane roofs need a design slope of at least 1/4 unit vertical in 12 horizontal, about 2 percent (<a href="{UP}" rel="noopener">IBC 2021, Utah, Section 1507.12.1</a>). The same code points to one material standard for each membrane: ASTM D6878 for TPO, ASTM D4637 for EPDM and ASTM D4434 for PVC (<a href="{UP}" rel="noopener">Table 1507.12.2</a>; <a href="{CS}" rel="noopener">Carlisle SynTec</a>).</p>
<p>The big difference is chemistry. TPO and PVC are <em>thermoplastics</em>: they soften when heated, so two sheets can be welded into one. EPDM is a <em>thermoset</em>: its molecules are cross-linked as it cures, so once it&rsquo;s cured it can only bond to itself with tape or adhesive (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>).</p>

<h2>TPO: the white, welded membrane</h2>
<p>TPO (thermoplastic polyolefin) is made from polypropylene and ethylene-propylene rubber, with fire retardants, UV stabilizers and pigments added. The sheet has a cap layer and a core layer with a polyester reinforcing scrim between them. Unlike PVC, it doesn&rsquo;t use added plasticizers to stay flexible. It&rsquo;s typically white, and its seams are heat-welded on site (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>).</p>
<p>TPO can be mechanically fastened, fully adhered or induction welded to plates under the sheet. It&rsquo;s the youngest of the three, introduced in the 1980s.</p>

<h2>EPDM: the rubber roof</h2>
<p>EPDM (ethylene propylene diene terpolymer) is a synthetic rubber. Roughly half to 60 percent of its formula is polymer and carbon black, and the carbon black is what gives it UV resistance. It comes in black or white, 0.045 to 0.090 inch thick, in sheets from 10 to 50 feet wide and up to 200 feet long (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>).</p>
<p>Those wide sheets mean fewer seams on a big, open roof. The seams are joined with butyl seam tape, which the same source puts at about 10 to 12 pounds per inch of seam strength, up from 3 to 5 with the older cement method. EPDM can be mechanically fastened, fully adhered, or held down with stone or paver ballast. It has the longest history of the three: the first EPDM roof membrane was made in 1965.</p>

<h2>PVC: the grease-resistant membrane</h2>
<p>PVC (poly(vinyl chloride)) sheets are two layers of PVC over a reinforcing scrim. The top layer is built for UV resistance; the bottom layer carries more plasticizer to stay flexible and weldable. Like TPO, the seams are heat-welded on site (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>).</p>
<p>PVC&rsquo;s standout trait is that it&rsquo;s the most resistant of the three to oils and grease, which is why it shows up over restaurant kitchens and manufacturing exhaust. It&rsquo;s also fire-resistant and recyclable. PVC was the first single-ply system with its own ASTM standard, D4434, in 1985, and that standard requires at least 16 mils of material over the scrim (<a href="{CS}" rel="noopener">Carlisle SynTec</a>).</p>

<h2>Side by side</h2>
<div class="tablebox"><table><thead><tr><th></th><th>TPO</th><th>EPDM</th><th>PVC</th></tr></thead><tbody>
<tr><td>Type</td><td>Thermoplastic</td><td>Thermoset rubber</td><td>Thermoplastic</td></tr>
<tr><td>Seams</td><td>Heat-welded</td><td>Tape or adhesive</td><td>Heat-welded</td></tr>
<tr><td>Usual color</td><td>White</td><td>Black or white</td><td>White or light</td></tr>
<tr><td>Added plasticizers</td><td>None</td><td>&mdash;</td><td>Yes</td></tr>
<tr><td>Most resistant to oils and grease</td><td></td><td></td><td>Yes</td></tr>
<tr><td>Attachment</td><td>Fastened, adhered or induction-welded</td><td>Fastened, adhered or ballasted</td><td>Fastened or adhered</td></tr>
<tr><td>Recyclable</td><td>Yes</td><td>No</td><td>Yes</td></tr>
<tr><td>ASTM standard</td><td>D6878</td><td>D4637</td><td>D4434</td></tr>
</tbody></table></div>
<p class="small">Sources: <a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>, <a href="{CS}" rel="noopener">Carlisle SynTec</a>, <a href="{UP}" rel="noopener">IBC 2021 (Utah)</a>. Check the specific product&rsquo;s data sheet for your building.</p>

<figure>{img("white-membrane-roof-sunset", "A finished white membrane roof at sunset")}<figcaption>A white membrane roof on an Oakley Roofing job. White is the usual color for TPO and PVC.</figcaption></figure>

<h2>How to choose for your building</h2>
<h3>What happens on the roof?</h3>
<p>If a restaurant hood, a fryer exhaust or a manufacturing process puts oil or grease on the roof, PVC is the usual answer, because it resists them best. For an office, warehouse or apartment roof without that exposure, TPO and EPDM are both in play.</p>
<h3>How open is the roof?</h3>
<p>A big, simple roof with few penetrations suits EPDM&rsquo;s wide sheets: fewer seams to make. A roof crowded with units, curbs and pipes means a lot of detail work, where welded TPO or PVC seams are an advantage.</p>
<h3>What&rsquo;s the budget?</h3>
<p>Thermosets like EPDM are often cost-effective; thermoplastics are generally a little more expensive (<a href="{JM}" rel="noopener">Johns Manville / BNP Media</a>). Your quote will show the real numbers for your roof, because insulation, tear-off and details usually matter more than the membrane line item.</p>
<h3>Does recycling matter to you?</h3>
<p>TPO and PVC can be recycled; EPDM, as a thermoset, can&rsquo;t be remolded or reshaped once installed.</p>
<h3>What&rsquo;s already up there?</h3>
<p>Before any new membrane, someone has to look at the existing roof. Utah&rsquo;s code doesn&rsquo;t allow a recover, a new roof over the old one, when the existing roof already has two or more layers (<a href="{UP}" rel="noopener">IBC 2021, Utah, Section 1512.2.1.1</a>). In that case it&rsquo;s a full tear-off to the deck.</p>

<h2>Maintenance matters more than the logo on the roll</h2>
<p>Whichever membrane you choose, the roof lasts longer if it&rsquo;s looked after. We recommend a commercial roof inspection twice a year, in spring and fall, before the extreme seasons, and fixing small problems while they&rsquo;re small. See <a href="@/commercial-roofing-repair-maintenance/">commercial repair and maintenance</a>.</p>
<p>Planning a re-roof or a new building? See <a href="@/commercial-roofing-installation/">commercial roofing installation</a>, or call <a href="tel:{S["tel"]}">{S["phone"]}</a> for a free quote.</p>

<h2>Frequently asked questions</h2>
{faq_html(FAQ)}

<p class="sources"><strong>Sources:</strong> <a href="{JM}" rel="noopener">Andrew A. Hunt, &ldquo;Understanding Single-Ply Roofing Systems,&rdquo; CE Center / BNP Media, sponsored by Johns Manville, January 2019</a> &middot; <a href="{CS}" rel="noopener">Taylor Gingerich, &ldquo;SpecTopics: Understanding ASTM Standards for Roofing Membranes,&rdquo; Carlisle SynTec, December 2021</a> &middot; <a href="{UP}" rel="noopener">2021 International Building Code as adopted by Utah, Chapter 15 (UpCodes)</a>. All checked 17 October 2026.</p>
'''


def page():
    trail = [("Home", ""), ("Blog", "blog/"), (TITLE, PATH)]
    lede = "How TPO, EPDM and PVC differ, what Utah&rsquo;s building code asks of a flat roof, and how to pick a membrane for your building."
    items = []
    def h2(m):
        t = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        sid = re.sub(r"[^a-z0-9]+", "-", h.unescape(t).lower()).strip("-")[:48]
        items.append((sid, t)); return f'<h2 id="{sid}">{m.group(1)}</h2>'
    art = re.sub(r"<h2>(.*?)</h2>", h2, ART)
    toc = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in items)
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", h.unescape(re.sub(r"<[^>]+>", " ", ART))))
    body = phero(trail, TITLE, lede, "Guide &middot; commercial roofing", "single-ply-roof-deck-new-install", "A new white single-ply roof deck, with the Wasatch on the horizon", "B-001", buttons=False) + f'''
<section class="sec article"><div class="wrap art-grid"><aside class="art-side"><nav class="toc" aria-label="In this article"><p class="label">In this article</p><ol>{toc}</ol></nav>
<div class="panel dark"><p class="label light">Free quote</p><a class="big-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Get a Free Quote {ARROW}</a></div></aside>
<article class="prose post reveal"><p class="byline">By <b>Oakley Roofing</b> &middot; Salt Lake City &middot; 17 October 2026 &middot; {max(1, round(words / 230))} min read</p>{art}</article></div></section>''' + cta()
    return {"path": PATH, "canonical": U + PATH, "title": "TPO vs. EPDM vs. PVC: Flat Roof Membranes Compared | Oakley Roofing",
            "meta": "TPO vs. EPDM vs. PVC: how the three flat roof membranes differ in seams, materials and grease resistance, what Utah code requires, and how to choose one.",
            "body": body, "og": "single-ply-roof-deck-new-install", "ogtype": "article", "full_biz": False, "words": words,
            "schema": [crumbs_ld(PATH, trail), faq_ld(FAQ),
                       {"@type": "BlogPosting", "@id": U + PATH + "#article", "headline": TITLE, "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": U + "#business"}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": U + PATH,
                        "image": U + "assets/img/single-ply-roof-deck-new-install.webp", "wordCount": words, "inLanguage": "en-US",
                        "about": ["TPO roofing", "EPDM roofing", "PVC roofing", "Commercial roofing"], "citation": [JM, CS, UP]}]}
