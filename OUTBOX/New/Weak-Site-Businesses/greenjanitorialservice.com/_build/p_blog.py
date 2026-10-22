"""New blog post for greenjanitorialservice.com (22 Oct 2026): how to tell whether a cleaning product is really "green". Informational;
it doesn't target janitorial, commercial, office or carpet cleaning keywords, and doesn't repeat their existing posts. Sources: EPA "Learn
About the Safer Choice Label" (updated 1 Sep 2026); EPA "Learn About Design for the Environment (DfE) Certification" (updated 17 Apr 2026);
EPA news release on the modernized DfE logo (May 2022); FTC "Green Guides" page."""
from engine import faq_html, faq_ld, canon

SLUG = "post/how-to-read-green-cleaning-labels/"
H1 = "Is that cleaner really green? How to read eco labels"
FAQ = [("What does the EPA Safer Choice label mean?", "It marks products with safer chemical ingredients that still perform. EPA reviews every chemical ingredient regardless of percentage, and labeled products must also meet performance, packaging, pH and VOC requirements."),
       ("Is there a green label for disinfectants?", "Yes. EPA&rsquo;s Design for the Environment (DfE) logo is for antimicrobial products such as disinfectants and sanitizers that meet extra health and environmental criteria on top of pesticide registration."),
       ("Does &ldquo;eco-friendly&rdquo; on a label mean anything?", "Not much by itself. The FTC&rsquo;s Green Guides exist to help marketers avoid misleading environmental claims, and broad terms like &ldquo;eco-friendly&rdquo; are hard to back up. Look for a specific claim or a certification you can check."),
       ("Is Safer Choice the same as an EPA endorsement?", "No. Participation is voluntary, and for the DfE list EPA states that inclusion does not constitute an endorsement; it means EPA reviewed the product against its criteria.")]
BODY = f'''<p class="answer">To tell whether a cleaner is really &ldquo;green,&rdquo; look past words like &ldquo;eco-friendly&rdquo; and check for a certification you can verify. In the U.S., EPA&rsquo;s Safer Choice label marks cleaning products whose every ingredient EPA has reviewed, and its Design for the Environment (DfE) logo does the same job for disinfectants and sanitizers. Broad green claims without specifics are exactly what the FTC&rsquo;s Green Guides warn about.</p>

<p>&ldquo;Natural.&rdquo; &ldquo;Non-toxic.&rdquo; &ldquo;Eco.&rdquo; Walk down any cleaning aisle and almost every bottle sounds good for the planet. At Green Janitorial Services, choosing products that are safe for people, pets and the environment is the core of what we do, so we get asked a lot how to tell the difference. Here&rsquo;s what the official labels actually mean, based on what the U.S. Environmental Protection Agency and the Federal Trade Commission publish.</p>

<h2>Why the front of the bottle isn&rsquo;t enough</h2>
<p>There&rsquo;s no single legal definition that makes a cleaner &ldquo;green.&rdquo; What exists instead is guidance on how sellers may talk about environmental benefits. The FTC&rsquo;s <strong>Green Guides</strong> are, in the agency&rsquo;s words, designed to help marketers avoid making environmental claims that mislead consumers. They include general principles that apply to all environmental marketing claims and explain how marketers can qualify their claims to avoid deceiving people. The Guides were first issued in 1992 and revised in 1996, 1998 and 2012, and the FTC has been reviewing them again since 2022.</p>
<p>The practical takeaway: a broad word like &ldquo;eco-friendly&rdquo; tells you very little on its own. A specific claim (&ldquo;fragrance-free,&rdquo; &ldquo;made from recycled plastic&rdquo;) or a third-party certification tells you much more. The 2012 update to the Green Guides specifically added guidance on product certifications and seals of approval.</p>

<h2>Label 1: EPA Safer Choice (everyday cleaners)</h2>
<p>EPA&rsquo;s <strong>Safer Choice</strong> label helps consumers and commercial buyers identify products with safer chemical ingredients, without sacrificing quality or performance. Participation is voluntary, and EPA says nearly 2,000 products currently qualify to carry the label. To earn it, a product has to clear several bars:</p>
<ul>
<li><strong>Every ingredient is reviewed.</strong> EPA reviews all chemical ingredients, regardless of their percentage in the product, and each must meet safety criteria for human health and the environment.</li>
<li><strong>It has to work.</strong> All products must perform comparably to conventional products.</li>
<li><strong>Packaging is reviewed.</strong> EPA checks packaging against the Safer Choice Standard, and partners must add sustainable packaging measures during the partnership.</li>
<li><strong>pH limits.</strong> Labeled products must meet pH standards that minimize the potential for skin and eye irritation or injury.</li>
<li><strong>VOC limits.</strong> Safer Choice restricts volatile organic compound content to minimize indoor air pollution and associated respiratory concerns.</li>
</ul>
<p>There are a few versions worth knowing: a version for business, industrial and institutional products; a <strong>fragrance-free</strong> label for people who prefer unscented products; and an outdoor-use label for products that meet added environmental criteria.</p>

<h2>Label 2: EPA Design for the Environment (disinfectants)</h2>
<p>Disinfectants and sanitizers are a different category: because they claim to kill germs, EPA treats them as antimicrobial pesticides. For these products, EPA uses the <strong>Design for the Environment (DfE)</strong> logo, which it modernized in 2022.</p>
<p>According to EPA, the DfE logo helps consumers identify antimicrobial products that meet the health and safety standards of pesticide registration, plus additional criteria:</p>
<ul>
<li><strong>Human health:</strong> products must fall within a set pH range to limit skin and eye irritation, and they exclude ingredients with potential long-term health risks, such as cancer risk.</li>
<li><strong>Environment:</strong> EPA considers how quickly chemicals break down and how they affect fish and other aquatic life.</li>
<li><strong>Ingredients:</strong> EPA reviews every chemical ingredient, including impurities and low-level components.</li>
<li><strong>Packaging:</strong> manufacturers must improve packaging&rsquo;s environmental impact where possible.</li>
</ul>
<p>One more important detail: DfE-certified sanitizers and disinfectants can only claim to kill viruses and bacteria that cause human illness after EPA approves laboratory testing data showing they work. EPA keeps a list of products qualified to display the logo, and notes that being on the list does not constitute an endorsement; it means EPA reviewed the product against its criteria.</p>

<h2>Words to read carefully</h2>
<ul>
<li><strong>&ldquo;Eco-friendly,&rdquo; &ldquo;green,&rdquo; &ldquo;earth-safe.&rdquo;</strong> General environmental benefit claims. On their own, they&rsquo;re hard to verify. Look for what specifically makes the product better.</li>
<li><strong>&ldquo;Non-toxic.&rdquo;</strong> A strong claim. Treat it as a reason to look for the details or a certification, not as proof.</li>
<li><strong>&ldquo;Natural.&rdquo;</strong> Says where ingredients come from, not how safe they are.</li>
<li><strong>Seals and badges.</strong> Check that a seal comes from an organization you can look up, like EPA&rsquo;s Safer Choice or DfE programs, rather than a logo the brand designed itself.</li>
</ul>

<h2>A quick checklist for your cleaning cabinet</h2>
<ol>
<li>For everyday cleaners, look for the <strong>Safer Choice</strong> label (or the fragrance-free version if scents bother you).</li>
<li>For disinfectants and sanitizers, look for the <strong>DfE</strong> logo, and remember that only EPA-reviewed efficacy data backs a germ-killing claim.</li>
<li>Be skeptical of broad &ldquo;green&rdquo; words with nothing specific behind them.</li>
<li>Read and follow the directions on the label; a safer product still works best used as directed.</li>
<li>Ask your cleaning company what they use, and why.</li>
</ol>

<h2>How we think about it at GJS</h2>
<p>Our cleaning methods are built around biodegradable, environmentally friendly products that are safer for the people, pets and plants in the spaces we clean, from offices and facilities to family homes across the Salt Lake Valley. If you&rsquo;d like to know more about the products we&rsquo;d use in your space, just ask when you request a quote.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Looking for a cleaner that takes the &ldquo;green&rdquo; part seriously? Call Green Janitorial Services at <a href="tel:+18015778703">+1 801-577-8703</a>, Monday to Saturday from 7:00 AM.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/saferchoice/learn-about-safer-choice-label" rel="noopener">Learn About the Safer Choice Label</a> (updated September 1, 2026)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/pesticide-labels/design-environment-logo-antimicrobial-pesticide-products" rel="noopener">Learn About Design for the Environment (DfE) Certification</a> (updated April 17, 2026)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/newsreleases/epa-launches-modernized-design-environment-logo-disinfectant-and-other-antimicrobial" rel="noopener">EPA Launches Modernized Design for the Environment Logo for Disinfectant and Other Antimicrobial Products</a> (2022)</li>
<li>Federal Trade Commission, <a href="https://www.ftc.gov/news-events/topics/truth-advertising/green-guides" rel="noopener">Green Guides</a></li>
</ul></div>
<p class="small photo-credit">Banner photo: Salt Lake City &middot; Garrett from Salt Lake City, CC BY 2.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Reading eco labels", H1, "From the blog &middot; Oct 22, 2026", "Blog", "How to Read Green Cleaning Labels: EPA Safer Choice | GJS",
                  "Is that cleaner really green? What EPA's Safer Choice and Design for the Environment labels mean, and why broad eco claims say little. Sourced to EPA and FTC.",
                  BODY, image="gj-slc", alt="Salt Lake City", crumbs=[("Blog", "bloghome/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Green Janitorial Services"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
