"""Blog for skybridgeroofings.com, on the client's existing blog URL (/blogs/noticias, empty today), plus one new post.

Post: "Do You Need a Permit to Replace a Roof in South Salt Lake?"
Main phrase: "permit to replace a roof south salt lake" (informational, long tail). Kept off it on purpose: "roofing company
south salt lake" (home), "roof replacement south salt lake" (replacement page) and "roof repair south salt lake" (repair page);
the post only links to those pages. Facts and sources, checked 18 Oct 2026:
- South Salt Lake FAQ: "Any reroof of a structure requires a building permit." Work started without a permit "may be subject to
  citation and a double fee for the application." "All building permits require an inspection." Inspections: 801-483-6032.
  Review within 15 business days; applications expire after 180 days.  https://sslc.gov/m/faq?cat=25
- South Salt Lake Building Permits page: roofing listed as a renovation that needs a permit; apply by emailing the application
  and checklist or with the online form; City Hall, 220 E Morris Avenue.  https://sslc.gov/431/Building-Permits
- ICC: Utah adopted the 2021 International Codes statewide, effective July 1, 2023.
  https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes
- Bountiful City reroof policy (a Utah city applying the same state code): a roof recover is not allowed where the existing roof
  already has two or more applications of roofing.  https://bountifulutah.gov/file/d0bd72b1-0143-472f-801a-39881f38cb08
No fees or prices are stated (none published in the sources above).
"""
from build import U, S, ARROW, CONTACT, BLOG_POST, img, phero, cta, faq_html, faq_ld, crumbs_ld

HOME = ("Home", "")
BLOG = ("Guides", "blogs/noticias/")

FAQ = [("Do I need a permit to replace my roof in South Salt Lake?", "Yes. South Salt Lake&rsquo;s building department says any reroof of a structure requires a building permit."),
       ("Does a small roof repair need a permit?", "The city&rsquo;s FAQ talks about reroofing, not small repairs. If you are only replacing a few shingles or resealing a vent, ask the Building Division before you assume either way."),
       ("Who gets the permit, me or the roofer?", "Either can apply, but on most jobs the roofing contractor pulls the permit as part of the work. Ask your roofer to confirm it in writing before the job starts."),
       ("How long does a permit take?", "The city says it reviews applications and gives feedback within 15 business days, and that applications expire after 180 days."),
       ("Is the roof inspected?", "Yes. The city says all building permits require an inspection. Inspections are scheduled at 801-483-6032.")]


def post():
    path = BLOG_POST[1]
    trail = [HOME, BLOG, ("Roof permits in South Salt Lake", path)]
    body = phero(trail, BLOG_POST[0], "Short answer: yes. Here is what South Salt Lake requires, what the inspection is for, and when a new roof can and can&rsquo;t go over the old one.", "Guide &middot; Permits", "office-roof-detail-drawings", "Roof detail drawings on a monitor in the Sky Bridge office", sheet="G-01", buttons=False) + f'''
<section class="sec"><div class="wrap post-grid">
<article class="prose post">
<p class="meta-line mono">By Sky Bridge Roofing &middot; 18 Oct 2026 &middot; 7 min read</p>
<p class="answer">Yes. In South Salt Lake, any roof replacement needs a building permit. The city&rsquo;s building department puts it plainly: &ldquo;Any reroof of a structure requires a building permit.&rdquo; Every permit also comes with an inspection.</p>

<p>Plenty of homeowners are surprised by that. A new roof can feel like maintenance, the same as painting or replacing a fence. But a roof holds up snow, sheds water away from the walls and carries the weight of every layer put on it, so the city treats reroofing as construction. Here is what that means if you are planning a new roof.</p>

<h2>What South Salt Lake says</h2>
<p>The city&rsquo;s building FAQ and Building Permits page cover the basics:</p>
<ul>
<li><b>Reroofing needs a permit.</b> &ldquo;Any reroof of a structure requires a building permit.&rdquo; Roofing is listed with other renovations, like basement finishes and kitchen expansions, as work that needs a permit.</li>
<li><b>Work comes after the permit.</b> The city says construction work can only be performed after a permit is obtained.</li>
<li><b>Starting early costs more.</b> &ldquo;Any project that starts work without a permit may be subject to citation and a double fee for the application.&rdquo;</li>
<li><b>Every permit is inspected.</b> &ldquo;All building permits require an inspection.&rdquo; Inspections are scheduled by phone at 801-483-6032.</li>
<li><b>Timing.</b> The city reviews applications and gives feedback within 15 business days, and applications expire after 180 days.</li>
</ul>
<p>You apply by emailing the completed application and checklist to the Building Division, or through the city&rsquo;s online building permit form for permit types that qualify. The Building Division is at City Hall, 220 E Morris Avenue.</p>

<h2>Why a roof needs a permit at all</h2>
<p>The permit is how the city checks that the new roof meets the building code. Utah adopted the 2021 International Codes statewide, effective July 1, 2023, so the same rules for roof coverings, underlayment and flashing apply across the state. An inspection is a second set of eyes on the things that are hard to see once the roof is finished: whether the deck was sound, whether flashing was installed at walls and penetrations, and whether the layers went on in the right order.</p>
<p>It also protects you. A permitted, inspected roof is part of your home&rsquo;s record. When you sell, a buyer&rsquo;s inspector or lender may ask about work done without permits, and unpermitted work can mean delays and repairs. The city also notes that work which hasn&rsquo;t been inspected may have to be removed or replaced.</p>

<h2>Can a new roof go over the old one?</h2>
<p>This is the question that most often changes the price of a job. Laying new shingles over the existing roof, called a recover or a layover, skips the tear-off. The building code limits when that is allowed. Utah cities applying the state code, such as Bountiful in its reroof policy, spell out the main rule: a recover is not allowed when the roof already has two or more layers of roofing.</p>
<p>Even when a second layer would be allowed, it isn&rsquo;t always a good idea:</p>
<ul>
<li><b>You can&rsquo;t see the deck.</b> Soft or rotted sheathing stays hidden under the new roof.</li>
<li><b>Flashing is a compromise.</b> Old flashing at walls and chimneys is hard to do properly over an extra layer.</li>
<li><b>Weight adds up.</b> Every layer adds load to the roof framing, which also carries Utah snow.</li>
<li><b>Wet or damaged roofs don&rsquo;t qualify.</b> A recover goes over a sound, dry roof, not one that is soaked or failing.</li>
</ul>
<p>That is why, on most <a href="@/pages/roof-raplecement/">roof replacements</a>, we recommend a full tear-off: it is the only way to inspect the deck and replace the flashing, and it resets the roof to one layer for the next owner.</p>

<h2>What about repairs?</h2>
<p>The city&rsquo;s FAQ answer is about reroofing. It doesn&rsquo;t list small repairs, such as replacing a few blown-off shingles or resealing a pipe boot. Some Utah cities set a size limit below which repairs don&rsquo;t need a permit, but those limits are set city by city. If your job is somewhere between a repair and a partial reroof, ask the South Salt Lake Building Division before work starts. For true <a href="@/pages/roof-repair/">roof repairs</a>, we will tell you what we think applies and help you check.</p>

<h2>Who pulls the permit?</h2>
<p>On most reroofs the roofing contractor applies for the permit, schedules the inspection and makes sure the work is ready for it. That is worth confirming before you sign: ask your roofer, in writing, who is pulling the permit and when the inspection will happen. Be careful with any bid that seems to leave the permit out; if the work is ever questioned, it is your house and your record.</p>

<h2>A simple checklist before a new roof</h2>
<ol>
<li>Get a <a href="@/pages/roof-inspection/">roof inspection</a> and find out how many layers are on the roof now.</li>
<li>Decide on the system: shingles, metal, or a membrane for flat sections.</li>
<li>Get a written estimate that says whether it includes a tear-off and deck repairs.</li>
<li>Confirm who is applying for the permit, and wait for it before work starts.</li>
<li>Make sure the inspection is scheduled and passed when the work is done.</li>
</ol>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>South Salt Lake, Building FAQ (reroof permits, inspections, timing): <a href="https://sslc.gov/m/faq?cat=25" rel="noopener">sslc.gov/m/faq?cat=25</a></li>
<li>South Salt Lake, Building Permits: <a href="https://sslc.gov/431/Building-Permits" rel="noopener">sslc.gov/431/Building-Permits</a></li>
<li>International Code Council, Utah adoption of the 2021 International Codes: <a href="https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes" rel="noopener">iccsafe.org</a></li>
<li>Bountiful City, residential reroof policy: <a href="https://bountifulutah.gov/file/d0bd72b1-0143-472f-801a-39881f38cb08" rel="noopener">bountifulutah.gov</a></li>
</ul><p>City rules can change. Check with the South Salt Lake Building Division for your project.</p></div>
</article>
<aside class="sv-side"><div class="side-card"><p class="label light">Planning a new roof?</p><h3>Start with a free inspection</h3><p>We&rsquo;ll tell you how many layers you have and what the job involves.</p><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a></div>
<div class="side-rel"><p class="label">Related</p><ul><li><a href="@/pages/roof-raplecement/"><span class="mono">Roof Replacement</span>Tear-off to new roof</a></li><li><a href="@/pages/roof-inspection/"><span class="mono">Roof Inspection</span>Free, by foot or drone</a></li><li><a href="@/pages/roof-repair/"><span class="mono">Roof Repair</span>Leaks and damage</a></li></ul></div></aside>
</div></section>''' + cta()
    return {"path": path, "canonical": U + path.rstrip("/"), "title": "Permit to Replace a Roof in South Salt Lake? What to Know",
            "meta": "Do you need a permit to replace a roof in South Salt Lake? Yes. What the city requires, inspections, timing, and when a new roof can go over the old one.",
            "body": body, "og": "office-roof-detail-drawings", "ogtype": "article",
            "schema": [{"@type": "BlogPosting", "@id": U + path.rstrip("/") + "#post", "headline": BLOG_POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18",
                        "author": {"@type": "Organization", "name": S["name"], "@id": U + "#business"}, "publisher": {"@id": U + "#business"},
                        "image": U + "assets/img/office-roof-detail-drawings.webp", "mainEntityOfPage": U + path.rstrip("/")}, crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    trail = [HOME, BLOG]
    body = phero(trail, "Roofing Guides from Sky Bridge Roofing", "Plain answers to the questions South Salt Lake homeowners and property owners ask us.", "Guides", None, sheet="G-00", buttons=False) + f'''
<section class="sec"><div class="wrap"><div class="posts">
<a class="postcard reveal" href="@/{BLOG_POST[1]}">{img("office-roof-detail-drawings", "Roof detail drawings on a monitor")}<div class="in"><span class="mono">Permits &middot; 7 min</span><b>{BLOG_POST[0]}</b><p>Yes, and here is what South Salt Lake requires, what the inspection checks, and when a new roof can go over the old one.</p><em>Read the guide {ARROW}</em></div></a>
</div></div></section>''' + cta()
    return {"path": "blogs/noticias/", "canonical": U + "blogs/noticias", "title": "Roofing Guides for South Salt Lake | Sky Bridge Roofing",
            "meta": "Roofing guides from Sky Bridge Roofing in South Salt Lake: permits, repairs, replacements and roofing systems, explained in plain language for owners.",
            "body": body, "schema": [crumbs_ld("blogs/noticias/", trail), {"@type": "Blog", "@id": U + "blogs/noticias#blog", "url": U + "blogs/noticias", "publisher": {"@id": U + "#business"}}]}


def pages():
    return [index(), post()]
