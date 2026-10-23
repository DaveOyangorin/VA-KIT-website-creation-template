"""New blog post for marble-builders.com (23 Oct 2026): lead paint and asbestos before remodeling an older home. Informational; it doesn't
target "general contractor riverton" or a service keyword. Sources: US EPA, "Lead Renovation, Repair and Painting Program" (updated
17 Jun 2026); EPA, "Lead Renovation, Repair and Painting Program Rules: Information for Contractors" (31 Mar 2026); EPA, "Summary of the RRP
Rule"; EPA, "Protect Your Family from Sources of Lead" (5 Oct 2026); EPA, "Protect Your Family from Exposures to Asbestos" (25 Jun 2026)."""
from engine import faq_html, faq_ld, canon

SLUG = "2026/10/lead-paint-asbestos-before-remodeling-older-home/"
H1 = "Lead paint and asbestos: what to know before remodeling an older home"
FAQ = [("Does the lead rule apply to my house?", "EPA&rsquo;s Renovation, Repair and Painting (RRP) rule covers paid renovation work that disturbs paint in housing built before 1978, along with child care facilities and preschools built before 1978."),
       ("Do I need a certified contractor for a small job?", "EPA treats interior jobs that disturb 6 square feet or less of painted surface, or 20 square feet or less outside, as minor repair and maintenance that the rule doesn&rsquo;t cover, unless the job includes window replacement or demolition of painted surfaces, which are always covered."),
       ("Can I test for asbestos myself?", "EPA advises that if you suspect a material contains asbestos and it&rsquo;s in good condition, leave it alone. Before a remodel that will disturb it, have it inspected by a trained, accredited professional, and leave removal to trained professionals."),
       ("What paperwork should I get from a contractor?", "Before work starts in a pre-1978 home, the renovator must give you EPA&rsquo;s Renovate Right pamphlet. You can confirm a firm&rsquo;s RRP certification with EPA&rsquo;s online firm search.")]
BODY = f'''<p class="answer">If your home was built before 1978, assume painted surfaces may contain lead and hire an EPA lead-safe certified firm for any paid work that disturbs them. Older homes can also hide asbestos in flooring, pipe and furnace insulation, and some wall materials. If you suspect it, don&rsquo;t disturb it: have it inspected before the remodel starts, and leave removal to trained professionals.</p>

<p>Opening up walls, pulling old flooring or replacing windows in an older home is exciting. It can also release two hazards you can&rsquo;t see: lead dust from old paint and fibers from asbestos-containing materials. Neither is a reason to avoid remodeling. Both are reasons to plan the first week of demo carefully. Here is what the US Environmental Protection Agency (EPA) says homeowners should know.</p>

<h2>Why 1978 matters</h2>
<p>The federal government banned lead-based paint for consumer use in 1978, so EPA says homes built before then are more likely to contain it. Lead paint that is in good condition is usually not a hazard on its own. The problem is disturbance: sanding, scraping, cutting and demolition turn old paint into fine dust and chips that settle on floors, windowsills and soil.</p>
<p>EPA notes that the main concern is young children, who can swallow lead dust from hands and toys, and pregnant women. Lead exposure in children can affect behavior, learning and growth. That&rsquo;s why the rules focus on homes and child-occupied facilities.</p>

<h2>The EPA lead rule for renovations (RRP)</h2>
<p>EPA&rsquo;s Lead Renovation, Repair and Painting (RRP) rule applies to renovation, repair and painting work that disturbs paint in pre-1978 housing and child-occupied facilities. Its core requirements:</p>
<ul>
<li><strong>Certified firms.</strong> Firms that are paid to do this work must be certified by EPA (or by a state with an EPA-authorized program), and use certified renovators trained in lead-safe work practices.</li>
<li><strong>The Renovate Right pamphlet.</strong> Before work begins, the renovator must give the owner and occupants EPA&rsquo;s <em>Renovate Right</em> pamphlet.</li>
<li><strong>Lead-safe work practices.</strong> That means containing the work area, minimizing dust and cleaning thoroughly afterward.</li>
<li><strong>Prohibited methods.</strong> The rule bans open-flame burning or torching of paint, heat guns operating at 1100&deg;F or higher, and power sanding, grinding or planing without HEPA-filtered exhaust.</li>
</ul>
<p>Some states run their own EPA-authorized RRP programs, in which case the state certifies firms instead of EPA. Either way, you can check a contractor with EPA&rsquo;s online lead-safe certified firm search before you sign anything.</p>

<h3>What counts as a small job</h3>
<p>EPA&rsquo;s guidance for contractors treats jobs that disturb 6 square feet or less of painted surface per room inside, or 20 square feet or less outside, as minor repair and maintenance not covered by the rule. There are two important exceptions: window replacement and demolition of painted surfaces are covered regardless of size. A kitchen or bathroom remodel in a pre-1978 home will almost always exceed those limits.</p>

<h3>Doing the work yourself</h3>
<p>EPA says the RRP rule generally doesn&rsquo;t apply to homeowners renovating their own owner-occupied home. It does apply if you&rsquo;re paid, if the home is a rental, or if it&rsquo;s used as a child care facility. EPA still urges do-it-yourselfers to follow lead-safe practices, because the dust is just as harmful when you create it yourself.</p>

<h2>Asbestos in older homes</h2>
<p>Asbestos is a mineral fiber that was widely used in building products for its strength and heat resistance. EPA lists places it may be found in older homes, including:</p>
<ul>
<li>Vinyl floor tiles, the backing on vinyl sheet flooring, and flooring adhesives</li>
<li>Insulation on hot water and steam pipes, and on older furnaces and boilers</li>
<li>Some textured paints, patching compounds and wall and ceiling materials</li>
<li>Older roofing and siding shingles</li>
<li>Vermiculite attic insulation</li>
</ul>
<p>The risk comes when those materials are damaged, crumbling or disturbed by sanding, cutting or tearing out, which releases fibers into the air. EPA&rsquo;s advice is plain: if you think a material may contain asbestos and it&rsquo;s in good condition, leave it alone. If a remodel will disturb it, have it inspected by a trained, accredited professional first. Removal should be done by trained professionals.</p>
<p>Federal law doesn&rsquo;t require an accredited inspector or contractor for work in a single-family home, but EPA notes that states and local governments may have their own requirements. Check with your state before you schedule demo.</p>

<h2>A pre-remodel checklist for an older home</h2>
<ol>
<li><strong>Find the year it was built.</strong> County records or your closing documents will tell you. Before 1978 means planning for lead.</li>
<li><strong>Walk the areas you&rsquo;ll disturb.</strong> Old vinyl floors, pipe wrap, textured ceilings and the furnace room are the usual suspects for asbestos.</li>
<li><strong>Test before demo, not during.</strong> A lead inspection or risk assessment, and an asbestos inspection of suspect materials, gives everyone a clear scope.</li>
<li><strong>Ask for certification.</strong> Ask for the firm&rsquo;s RRP certification, then confirm it on EPA&rsquo;s firm search.</li>
<li><strong>Expect the pamphlet and the plastic.</strong> A lead-safe contractor will give you <em>Renovate Right</em>, seal off the work area and clean up with HEPA equipment.</li>
<li><strong>Plan around kids.</strong> If young children or a pregnant family member live in the home, keep them out of the work area until final cleaning is done.</li>
</ol>

<h2>The same rules apply after water or fire damage</h2>
<p>A burst pipe or a fire doesn&rsquo;t change the age of the house. When mitigation crews tear out wet drywall, flooring or insulation in an older home, and when the rebuild opens more walls, the same lead and asbestos precautions apply. Ask early whether suspect materials were tested so the rebuild scope, and your insurance claim, reflect it.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Planning a remodel or a rebuild in an older home on the Wasatch Front? Marble Builders can walk the project with you before demo begins. Call <a href="tel:+18018285540">801-828-5540</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>US EPA, <a href="https://www.epa.gov/lead/lead-renovation-repair-and-painting-program" rel="noopener">Lead Renovation, Repair and Painting Program</a> (updated June 17, 2026)</li>
<li>US EPA, <a href="https://www.epa.gov/lead/lead-renovation-repair-and-painting-program-rules" rel="noopener">Lead Renovation, Repair and Painting Program Rules: information for contractors</a> (updated March 31, 2026)</li>
<li>US EPA, <a href="https://www.epa.gov/lead/summary-renovation-repair-and-painting-rule" rel="noopener">Summary of the Renovation, Repair and Painting Rule</a></li>
<li>US EPA, <a href="https://www.epa.gov/lead/protect-your-family-sources-lead" rel="noopener">Protect Your Family from Sources of Lead</a> (updated October 5, 2026)</li>
<li>US EPA, <a href="https://www.epa.gov/asbestos/protect-your-family-exposures-asbestos" rel="noopener">Protect Your Family from Exposures to Asbestos</a> (updated June 25, 2026)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Lone Peak, Utah &middot; runt35, CC BY 3.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Lead paint &amp; asbestos", H1, "From the blog &middot; Oct 23, 2026", "Blog", "Lead Paint &amp; Asbestos Before Remodeling an Older Home | Marble",
                  "Remodeling a home built before 1978? What EPA says about lead paint, the RRP rule, certified contractors and asbestos in old floors, pipes and walls.",
                  BODY, image="mb-hero", alt="Lone Peak, Utah", crumbs=[("Blog", "blog/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
                           "author": {"@type": "Organization", "name": "Marble Builders"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
