"""New blog post for pineapplepropertygroup.com (22 Oct 2026): Fair Housing Act basics for landlords. Informational; it doesn't target
"property management salt lake city" or another service keyword. Sources: 42 U.S.C. 3604 and 3603 (via Cornell LII); U.S. Department of
Justice, Civil Rights Division, "The Fair Housing Act" (updated 22 Jun 2023). General information, not legal advice."""
from engine import faq_html, faq_ld, canon

SLUG = "fair-housing-basics-for-landlords/"
H1 = "Fair housing basics every Salt Lake City landlord should know"
FAQ = [("Who is protected under the Fair Housing Act?", "The Justice Department lists race or color, religion, sex, national origin, familial status and disability."),
       ("Can an ad say &ldquo;no kids&rdquo; or &ldquo;ideal for singles&rdquo;?", "No. 42 U.S.C. 3604(c) makes it unlawful to publish any notice, statement or advertisement that indicates a preference, limitation or discrimination based on a protected characteristic, and that rule applies even to otherwise exempt owners."),
       ("Do I have to allow changes for a tenant with a disability?", "The Act treats refusing reasonable modifications of the premises, generally at the tenant&rsquo;s expense, and refusing reasonable accommodations in rules, policies, practices or services when necessary, as discrimination. A landlord may, where reasonable, require the interior be restored, reasonable wear and tear excepted."),
       ("Are any landlords exempt?", "Section 3603(b) exempts some single-family houses rented by an owner of no more than three such houses without a broker, and owner-occupied buildings with living quarters for no more than four families, but the advertising rule still applies. Using a property manager or broker can remove the single-family exemption.")]
BODY = f'''<p class="answer">The federal Fair Housing Act makes it illegal to refuse to rent, set different terms, publish discriminatory ads, or falsely say a unit is unavailable because of race or color, religion, sex, national origin, familial status or disability. Landlords must also allow reasonable modifications and make reasonable accommodations for tenants with disabilities. A few small owners are exempt from parts of the law, but never from the advertising rule.</p>

<p>Whether you own one rental house in Sugar House or a 12-unit building downtown, fair housing rules shape how you advertise, screen, and treat tenants. Most problems don&rsquo;t come from bad intent; they come from a careless line in a listing or a policy applied unevenly. Here are the basics, straight from the statute and the U.S. Department of Justice.</p>
<p><em>This is general information, not legal advice. Utah and local rules can add protections; talk to an attorney about specific situations.</em></p>

<h2>Who is protected</h2>
<p>According to the Justice Department&rsquo;s Civil Rights Division, the Fair Housing Act prohibits discrimination in housing because of:</p>
<ul><li>Race or color</li><li>Religion</li><li>Sex</li><li>National origin</li><li><strong>Familial status</strong> (families with children under 18)</li><li><strong>Disability</strong></li></ul>

<h2>What landlords can&rsquo;t do</h2>
<p>The core prohibitions are in 42 U.S.C. section 3604. Because of a protected characteristic, it is unlawful to:</p>
<ol>
<li><strong>Refuse to rent</strong>, refuse to negotiate, or otherwise make a dwelling unavailable or deny it (3604(a)).</li>
<li><strong>Set different terms, conditions or privileges</strong> of rental, or provide different services or facilities (3604(b)).</li>
<li><strong>Publish discriminatory advertising.</strong> Any notice, statement or advertisement that indicates a preference, limitation or discrimination is unlawful (3604(c)).</li>
<li><strong>Misstate availability.</strong> Telling someone a unit isn&rsquo;t available for inspection or rental when it actually is (3604(d)).</li>
<li><strong>Steer for profit</strong> by making representations about who is moving into a neighborhood (3604(e)).</li>
</ol>
<p>The Justice Department adds that sexual harassment by landlords, such as demanding sexual favors or creating a sexually hostile environment, also violates the Act.</p>

<h2>Families with children</h2>
<p>The Justice Department notes the Act generally prohibits discrimination against families with children under 18. Housing providers may not impose special requirements on families with children, such as confining them to one part of a complex, setting unreasonable occupancy limits, or restricting their access to recreational services.</p>
<p>In practice: no &ldquo;adults only&rdquo; listings (unless the property legally qualifies as housing for older persons), no steering families to the ground floor, and occupancy standards that are reasonable and applied the same way to everyone.</p>

<h2>Tenants with disabilities</h2>
<p>Section 3604(f) covers disability, and it goes further than simply not refusing to rent. Under 3604(f)(3), discrimination includes:</p>
<ul>
<li><strong>Refusing reasonable modifications</strong> of the existing premises that a person with a disability needs, generally at the tenant&rsquo;s expense. Where it&rsquo;s reasonable, a landlord may condition permission on the tenant agreeing to restore the interior, reasonable wear and tear excepted.</li>
<li><strong>Refusing reasonable accommodations</strong> in rules, policies, practices or services when they may be necessary for equal opportunity to use and enjoy the home.</li>
</ul>
<p>The Justice Department stresses that what counts as a reasonable accommodation is a case-by-case determination. It also notes that the Act does not protect individuals who pose a direct threat to others, but that decision must be individualized, not based on assumptions about a disability.</p>

<h2>Who is exempt, and who isn&rsquo;t</h2>
<p>Section 3603(b) carves out two narrow exemptions from section 3604:</p>
<ul>
<li><strong>Some single-family houses rented by an owner</strong> who owns no more than three such houses at a time, rented without using a broker, agent or anyone in the business of renting, and without discriminatory advertising.</li>
<li><strong>Owner-occupied small buildings</strong>: rooms or units in a dwelling with living quarters for no more than four families, if the owner actually lives in one of them.</li>
</ul>
<p>Two things matter for investors. First, the exemptions never cover advertising: 3604(c) still applies. Second, the single-family exemption depends on renting <strong>without</strong> a broker or anyone in the business of renting. Once a property manager handles the rental, plan on full compliance.</p>
<p>The Justice Department also notes that housing for older persons meeting the Housing for Older Persons Act may operate as senior housing, and noncommercial housing run by a religious organization may be reserved for people of the same religion.</p>

<h2>A practical checklist</h2>
<ul>
<li><strong>Write listings about the property</strong>, not the tenant you imagine: bedrooms, rent, amenities, location.</li>
<li><strong>Use written, consistent screening criteria</strong> and apply them to every applicant the same way.</li>
<li><strong>Answer availability questions truthfully</strong> to everyone who asks.</li>
<li><strong>Treat accommodation and modification requests as a process</strong>: respond promptly and evaluate each one individually.</li>
<li><strong>Keep occupancy limits reasonable</strong> and the same for every household.</li>
<li><strong>Train anyone who shows or leases your units</strong>; their words are your words.</li>
</ul>

<h2>Enforcement</h2>
<p>The Justice Department explains that people who believe they&rsquo;ve faced housing discrimination can file a complaint with HUD or bring their own lawsuit in federal or state court. DOJ brings cases on behalf of individuals based on HUD referrals and pursues pattern-or-practice cases.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Pineapple Property Group manages apartment buildings, condos, townhomes and single-family rentals across the Salt Lake City area, including new tenant finding, credit and background checks, and a new lease signed each year. Call or text <a href="tel:+18012079699">801-207-9699</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>42 U.S.C. &sect; 3604, <a href="https://www.law.cornell.edu/uscode/text/42/3604" rel="noopener">Discrimination in the sale or rental of housing</a> (Cornell Legal Information Institute)</li>
<li>42 U.S.C. &sect; 3603, <a href="https://www.law.cornell.edu/uscode/text/42/3603" rel="noopener">Effective dates of certain prohibitions</a> (exemptions; Cornell LII)</li>
<li>U.S. Department of Justice, Civil Rights Division, <a href="https://www.justice.gov/crt/fair-housing-act-1" rel="noopener">The Fair Housing Act</a> (updated June 22, 2023)</li>
</ul></div>
<p class="small photo-credit">Banner photo: Salt Lake City &middot; Invictus323, CC BY 4.0, via Wikimedia Commons</p>'''


def page(K):
    return K.page(SLUG, "Fair housing basics", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Fair Housing Basics for Salt Lake City Landlords | Pineapple",
                  "Fair Housing Act basics for landlords: protected classes, ads, families with children, disability modifications and accommodations, and the narrow exemptions.",
                  BODY, image="pp-skyline", alt="Salt Lake City skyline", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Pineapple Property Group"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
