"""New blog post for iraut.com (22 Oct 2026): 1031 exchange rules for Utah investors. Informational; it doesn't target property management,
brokerage or "property management midvale". Sources: IRS "Like-Kind Exchanges - Real Estate Tax Tips", IRS news release IR-2018-227
("Like-kind exchanges now limited to real property"), Instructions for Form 8824 (2025) and "About Form 8824". Not tax advice."""
from engine import faq_html, faq_ld, canon

SLUG = "post/1031-exchange-rules-for-utah-investors/"
H1 = "1031 exchange rules: what Utah real estate investors need to know"
FAQ = [("What property qualifies for a 1031 exchange?", "Since January 1, 2018, only real property held for use in a trade or business or for investment. Property held primarily for sale, like a flip, doesn&rsquo;t qualify, and personal property such as equipment or vehicles no longer does either."),
       ("What are the 45-day and 180-day rules?", "In a deferred exchange, the replacement property must be identified in writing within 45 days after you transfer the property you&rsquo;re giving up, and received within 180 days or by your tax return due date (including extensions), whichever is earlier."),
       ("Is an apartment building like-kind to raw land?", "Generally, yes. The IRS says real properties are generally like-kind whether improved or unimproved; for example, an apartment building would generally be like-kind to unimproved land. U.S. property is not like-kind to property outside the U.S."),
       ("Do I owe any tax in a 1031 exchange?", "If you also receive money or other property that isn&rsquo;t like-kind, you must recognize gain to the extent of that money or property. You can&rsquo;t recognize a loss in a like-kind exchange.")]
BODY = f'''<p class="answer">A 1031 (like-kind) exchange lets you defer gain when you trade real property held for business or investment for other like-kind real property. Since 2018 it applies only to real property. In a deferred exchange, you must identify the replacement property within 45 days and receive it within 180 days (or by your tax return due date, if earlier), and you report the exchange on IRS Form 8824. Talk to a tax professional before you sell.</p>

<p>For Utah investors trading up from a rental house to a fourplex, or from a small retail building to a larger one, Section 1031 of the Internal Revenue Code is one of the most useful tools available. It&rsquo;s also unforgiving about rules and deadlines. Here is a plain-language overview of what the IRS says, so you know the questions to ask your tax advisor and your broker before you list a property.</p>
<p><em>This article is general information from IRS publications, not tax or legal advice. Every exchange depends on your facts; work with a qualified tax professional.</em></p>

<h2>What a like-kind exchange is</h2>
<p>The IRS describes a like-kind exchange as exchanging real property used for business or held as an investment solely for other business or investment property that is the same type, or &ldquo;like-kind.&rdquo; Generally, if you make a like-kind exchange, you are not required to recognize a gain or loss under Section 1031. That&rsquo;s what makes it valuable: gain that would otherwise be taxed on a sale can be deferred into the replacement property.</p>

<h2>Since 2018: real property only</h2>
<p>The Tax Cuts and Jobs Act changed the rules. According to the IRS, effective January 1, 2018, like-kind exchange treatment applies <strong>only to exchanges of real property</strong> held for use in a trade or business or for investment. Exchanges of personal or intangible property, such as machinery, equipment, vehicles, artwork, collectibles, patents and other intellectual property, generally no longer qualify. (Certain exchanges of mutual ditch, reservoir or irrigation stock are still eligible, a detail that matters in Utah.)</p>
<p>The IRS defines real property as land and generally anything built on or attached to it.</p>

<h2>What doesn&rsquo;t qualify</h2>
<ul>
<li><strong>Property held primarily for sale.</strong> The IRS is explicit that an exchange of real property held primarily for sale still does not qualify. A house bought to fix and flip is generally inventory, not an investment, for this purpose.</li>
<li><strong>Foreign property for U.S. property.</strong> Real property in the United States is not like-kind to real property outside the United States.</li>
<li><strong>Personal property</strong>, after the 2018 change.</li>
</ul>

<h2>&ldquo;Like-kind&rdquo; is broader than you might think</h2>
<p>Properties are like-kind if they&rsquo;re of the same nature or character, even if they differ in grade or quality. The IRS says real properties generally are of like-kind regardless of whether they&rsquo;re improved or unimproved. Its own examples: an apartment building would generally be like-kind to another apartment building, and an apartment building would generally be like-kind to unimproved land. In practice, that gives investors room to move between property types: a rental house into a small commercial building, or land into a multifamily property.</p>

<h2>The two deadlines that make or break a deferred exchange</h2>
<p>Most exchanges aren&rsquo;t simultaneous swaps. You sell first and buy later, which the IRS calls a <strong>deferred exchange</strong>. For the replacement property to qualify, the Form 8824 instructions set two timing rules:</p>
<ol>
<li><strong>45 days to identify.</strong> The replacement property must be identified within 45 days after the property you&rsquo;re giving up is transferred.</li>
<li><strong>180 days to close.</strong> The replacement property must be received within 180 days, or by the due date of your tax return (including extensions) for the year of the transfer, <strong>whichever is earlier</strong>.</li>
</ol>
<p>The identification has to be in writing. According to the IRS instructions, the replacement property must be designated in a document you sign (or a written agreement signed by all parties), described clearly, using a legal description, street address or distinguishable name, and sent within the 45 days to the person required to transfer the replacement property to you or another person involved in the exchange, as the instructions specify.</p>
<p>The &ldquo;whichever is earlier&rdquo; detail catches people. A sale late in the year can run into the tax return due date before 180 days pass, unless you file an extension.</p>

<h2>Qualified intermediaries</h2>
<p>Deferred exchanges are commonly done through a <strong>qualified intermediary (QI)</strong>. The IRS instructions explain that if you make a deferred exchange using a QI, the transfer of the property given up and receipt of the like-kind property is treated as a like-kind exchange. The QI arrangement is one of the safe harbors described in IRS Publication 544.</p>
<p>Two cautions from the IRS:</p>
<ul>
<li><strong>Related parties and your agents can&rsquo;t serve as your QI.</strong> The IRS calls them &ldquo;disqualified persons.&rdquo;</li>
<li><strong>The deadlines still apply.</strong> If the timing requirements are missed because of the QI, the transaction won&rsquo;t qualify as a deferred exchange, and gain may be taxable in the year you transferred the property.</li>
</ul>

<h2>Cash and other property (&ldquo;boot&rdquo;)</h2>
<p>An exchange doesn&rsquo;t have to be perfectly even, but anything that isn&rsquo;t like-kind has tax consequences. The IRS says if, as part of the exchange, you also receive other (not like-kind) property or money, you must recognize a gain to the extent of the other property and money received. And you can&rsquo;t recognize a loss in a like-kind exchange.</p>

<h2>Related-party exchanges</h2>
<p>Exchanges with family members or related entities get extra scrutiny. The Form 8824 instructions say that after a related-party exchange, you must file Form 8824 for the year of the exchange and for the <strong>2 years following</strong> it.</p>

<h2>Reporting the exchange</h2>
<p>Like-kind exchanges are reported on <strong>IRS Form 8824</strong>, filed with your tax return for the year you transfer property in the exchange. The form figures the amount of gain deferred and the basis of the property you receive, along with any gain you must report if cash or non-like-kind property was involved.</p>

<h2>Practical checklist for a Utah investor</h2>
<ul>
<li>Confirm with your tax advisor that the property you&rsquo;re selling is held for investment or business use, not primarily for sale.</li>
<li>Line up a qualified intermediary <strong>before</strong> the sale closes.</li>
<li>Start looking for replacement property early. Day 45 comes fast.</li>
<li>Put the identification in writing, with clear property descriptions, and send it on time.</li>
<li>Watch your tax return due date if you sell late in the year.</li>
<li>Expect to file Form 8824, and for 2 more years after a related-party exchange.</li>
</ul>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Investment Realty Advisors&rsquo; agents can assist with the brokerage side of both legs of a 1031 exchange: selling the relinquished property and finding and closing on the replacement. Call <a href="tel:+18015284557">(801) 528-4557</a>. For tax treatment, consult your tax advisor.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>IRS, <a href="https://www.irs.gov/businesses/small-businesses-self-employed/like-kind-exchanges-real-estate-tax-tips" rel="noopener">Like-Kind Exchanges: Real Estate Tax Tips</a></li>
<li>IRS, <a href="https://www.irs.gov/newsroom/like-kind-exchanges-now-limited-to-real-property" rel="noopener">Like-kind exchanges now limited to real property</a> (IR-2018-227)</li>
<li>IRS, <a href="https://www.irs.gov/pub/irs-pdf/i8824.pdf" rel="noopener">Instructions for Form 8824 (2025)</a></li>
<li>IRS, <a href="https://www.irs.gov/forms-pubs/about-form-8824" rel="noopener">About Form 8824, Like-Kind Exchanges</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "1031 exchange rules", H1, "From the blog &middot; Oct 22, 2026", "Blog", "1031 Exchange Rules for Utah Real Estate Investors | IRA",
                  "What the IRS says about 1031 exchanges: real property only since 2018, the 45- and 180-day deadlines, qualified intermediaries, boot and IRS Form 8824.",
                  BODY, image="ira-aerial", alt="Aerial view of commercial property", crumbs=[("Blog", "blog/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "1031 exchange rules: what Utah real estate investors need to know", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Investment Realty Advisors"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
