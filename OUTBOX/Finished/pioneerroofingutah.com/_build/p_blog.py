from build import U, BIZ_ID, S, ARROW, INSPECT, img, faq_html, faq_ld, crumbs_ld, cta, side, phero

# Same URL pattern as the client's other posts (blog-<slug>/ at the site root).
PATH = "blog-what-is-the-25-percent-rule-for-roofing/"
FBC = "https://www.floridabuilding.org/fbc/commission/FBC_0820/DEC_Statements/DS_2020-022-STAFF-ANALYSIS-Final.htm"
SB4D = "https://www.flsenate.gov/Session/Bill/2022D/4D"
ICC = "https://www.iccsafe.org/about/periodicals-and-newsroom/utah-enhances-building-safety-statewide-with-adoption-of-2021-international-codes"
WESTPOINT = "https://www.westpointutah.gov/DocumentCenter/View/329/Re-Roof-Application-Permit-PDF"
FIRESTONE = "https://www.firestoneco.gov/DocumentCenter/View/9461/Firestone-Reroof-Requirements-2018-IRC-updated-81123"

# Main keyword: "25% rule roofing" / "what is the 25 percent rule for roofing" (a real Google question from the 14 Oct report,
# marked "check Utah rules"). Supporting: 25 percent roof rule Utah, roof repair vs replacement rule.
# Not targeted (owned by other pages, linked only): roofing company salt lake city (home), roof repair salt lake city
# (roofing-repairs/), roof replacement (residential-roofing/), roof inspection (roof-inspections/), and the client's
# existing posts on repair-or-replace and how often to replace a roof.

FAQ = [
    ("Does the 25% roof rule apply in Utah?",
     "The 25% rule people search for is a provision of the Florida Building Code. Utah builds to the 2021 International codes it adopted in 2023, and we haven&rsquo;t found an equivalent statewide 25% rule in them. Your city&rsquo;s building department has the final word on your project, so ask them before work starts."),
    ("Do I need a permit to re-roof in Utah?",
     "Many Utah cities require one. West Point City, for example, has a dedicated re-roof permit application that asks whether the job is a tear-off, deck repair or recover, how many layers are already on the roof, and the roofing contractor&rsquo;s Utah state license number."),
    ("Can a new roof go over my old one in Utah?",
     "Only if there&rsquo;s just one layer. Under the International Residential Code&rsquo;s re-roofing rules, where an existing roof already has two or more layers of roof covering, all the old material has to come off. Even with one layer, the roof and decking need to be sound."),
    ("My insurance adjuster mentioned a 25% rule. What does that mean?",
     "Ask them which policy language or code section they&rsquo;re referring to, since the Florida rule doesn&rsquo;t govern Utah homes. Insurance coverage depends on your own policy. A roofer can document the damage, but only your insurer can tell you what the policy covers."),
]

ART = f'''
<div class="answer"><strong>Short answer:</strong> the &ldquo;25% rule&rdquo; is a Florida building code provision. It says that if more than 25% of a roof or roof section is repaired, replaced or recovered within 12 months, the whole roof or section has to be brought up to current code. Florida narrowed it in 2022. Utah builds to the International codes, and we haven&rsquo;t found an equivalent statewide 25% rule in them. What does matter in Utah: permits, and the limit on roofing over old layers.</div>

<p>It&rsquo;s one of the questions homeowners type into Google when they&rsquo;re weighing a repair against a new roof: what is the 25% rule for roofing? You&rsquo;ll find plenty of confident answers online. Most of them are about Florida.</p>
<p>Here&rsquo;s where the rule actually comes from, how Florida changed it, and what the rules look like for a roof in Salt Lake City or anywhere else in Utah.</p>

<h2>Where the 25% rule comes from</h2>
<p>The rule is written into the Florida Building Code, Existing Building. In the 2017 edition, Section 706.1.1 says that not more than 25 percent of the total area or roof section of any building &ldquo;shall be repaired, replaced or recovered in any 12-month period unless the entire existing roofing system or roof section is replaced to conform to requirements of this code.&rdquo; That&rsquo;s the wording quoted by the <a href="{FBC}" rel="noopener">Florida Building Commission</a> in a 2020 staff analysis.</p>
<p>In plain terms: fix a small part of an older roof, and only that part follows today&rsquo;s code. Cross the 25% line in a year, and the whole roof (or roof section) has to meet current code. On an older roof, that usually means a full replacement.</p>
<p>That&rsquo;s why the rule matters so much in Florida after hurricanes. It can turn a large repair into a full new roof.</p>

<h2>How Florida changed the rule in 2022</h2>
<p>In May 2022, Florida passed <a href="{SB4D}" rel="noopener">Senate Bill 4-D</a>, effective May 26, 2022. It added a new subsection to Section 553.844 of the Florida Statutes.</p>
<p>The new rule says that if an existing roof or roof section was built, repaired or replaced to the 2007 Florida Building Code or a later edition, and 25 percent or more of it is being repaired, replaced or recovered, only the repaired, replaced or recovered portion has to meet the current code.</p>
<p>So in Florida today, the 25% rule mainly bites on roofs built to codes older than 2007. Newer roofs can be repaired in larger pieces without triggering a full replacement.</p>

<h2>Does the 25% rule apply in Utah?</h2>
<p>Utah doesn&rsquo;t use the Florida Building Code. The state adopted the 2021 International codes, including the International Building Code, the International Residential Code (specific provisions) and the International Existing Building Code, effective July 1, 2023, according to the <a href="{ICC}" rel="noopener">International Code Council</a>.</p>
<p>We haven&rsquo;t found an equivalent statewide 25% roof rule in Utah&rsquo;s adopted codes. We also won&rsquo;t tell you no local rule exists anywhere, because cities enforce the codes and some add their own policies. The safe move is simple: before a big repair or a new roof, call your city or county building department, or ask your roofer to.</p>

<h2>The Utah rules that actually affect your roof</h2>
<p>Two things come up on almost every Utah re-roof: permits and existing layers.</p>
<h3>Permits</h3>
<p>Many Utah cities require a permit to re-roof. <a href="{WESTPOINT}" rel="noopener">West Point City&rsquo;s re-roof permit application</a> is a good example of what they ask for:</p>
<ul>
<li>The type of work: tear-off, deck replacement, deck repair, or recover only</li>
<li>For a recover, how many layers are already on the roof</li>
<li>The recovering material: asphalt shingles, metal, a membrane system or other</li>
<li>The roofing contractor&rsquo;s Utah state license number</li>
</ul>
<p>Rules and fees vary by city, so check where your home is. A licensed roofer should know the process in the cities they work in.</p>
<h3>The two-layer limit</h3>
<p>Utah&rsquo;s adopted residential code includes the International Residential Code&rsquo;s re-roofing rules. The key one for homeowners: where an existing roof has two or more applications of any roof covering, all the old material must be removed, and a roof recover isn&rsquo;t allowed. A city reroofing checklist that quotes the section (R908.3.1.1 in the 2018 edition) puts it bluntly: <a href="{FIRESTONE}" rel="noopener">&ldquo;Roof recover is not allowed.&rdquo;</a></p>
<p>So if your roof already has two layers, any new roof starts with a full tear-off down to the deck.</p>

<h2>Repair or replace: how to decide without the 25% rule</h2>
<p>Without a 25% trigger, the repair-or-replace call in Utah comes down to the roof itself. A few honest questions help:</p>
<ul>
<li><strong>How old is the roof, and what is it?</strong> Asphalt shingles, TPO, PVC and metal all age differently.</li>
<li><strong>Is the damage local or spread out?</strong> A few blown-off shingles or one flashing leak are classic repairs. Wear across every slope usually isn&rsquo;t.</li>
<li><strong>What&rsquo;s under it?</strong> Soft or rotted decking changes the answer.</li>
<li><strong>How many layers are there?</strong> Two layers means a tear-off for any new roof.</li>
</ul>
<p>At Pioneer Roofing, we never recommend repairs that aren&rsquo;t in a customer&rsquo;s best interest, and every quote is transparent. If a <a href="@/roofing-repairs/">roof repair</a> will do the job, we&rsquo;ll say so. If it won&rsquo;t, we&rsquo;ll show you why. Our guide on <a href="@/blog-how-to-tell-when-your-roof-needs-repair-or-replacement/">when your roof needs repair or replacement</a> goes deeper.</p>

<h2>Questions about the 25% rule</h2>
{faq_html(FAQ)}

<h2>Not sure what your roof needs?</h2>
<p>Call John directly at <a href="tel:{S["tel"]}">{S["phone"]}</a>, try our <a href="@/new-roof-estimator/">new roof estimator</a>, or <a href="@/{INSPECT}">book an inspection</a>. We&rsquo;ll tell you whether you&rsquo;re looking at a repair or a new roof, and what your city will need.</p>

<div class="sources"><h3>Sources</h3><ol>
<li><a href="{FBC}" rel="noopener">Florida Building Commission, staff analysis for declaratory statement DS 2020-022</a>, quoting Section 706.1.1, 2017 Florida Building Code, Existing Building</li>
<li><a href="{SB4D}" rel="noopener">Florida Senate, SB 4-D (2022 Special Session D), &ldquo;Building Safety&rdquo;</a>, enrolled text, Section 1 (s. 553.844(5), F.S.), effective May 26, 2022</li>
<li><a href="{ICC}" rel="noopener">International Code Council, &ldquo;Utah Enhances Building Safety Statewide With Adoption of 2021 International Codes,&rdquo; 21 July 2023</a></li>
<li><a href="{WESTPOINT}" rel="noopener">West Point City, Utah, Building Permit Application: Re-Roof</a></li>
<li><a href="{FIRESTONE}" rel="noopener">Town of Firestone, Colorado, Reroof Requirements (2018 IRC)</a>, quoting IRC R908.3.1.1</li>
</ol></div>
'''


def new_post(hero):
    url = U + PATH
    trail = [("Home", ""), ("Blog", "blog/"), ("The 25% Rule for Roofing", PATH)]
    return {"path": PATH, "canonical": url, "ogtype": "article", "og": hero, "modified": "2026-10-17",
            "title": "What Is the 25% Rule for Roofing? Does It Apply in Utah?",
            "meta": "The 25% rule for roofing explained: where it comes from (Florida's building code), how it changed in 2022, and the re-roof rules that apply in Utah today.",
            "body": phero(trail, "What Is the 25% Rule for Roofing?", "And does it apply to a roof in Salt Lake City or anywhere else in Utah?",
                          hero, "Roof by Pioneer Roofing in Utah", "Pioneer Roofing blog",
                          extra='<div class="meta-line"><span>By Pioneer Roofing</span><span>Published 17 Oct 2026</span><span>7 min read</span></div>')
                    + f'<section class="sec"><div class="wrap layout"><article class="prose">{ART}</article>{side([("Roof repairs", "roofing-repairs/"), ("Roof inspections", "roof-inspections/"), ("Residential roofing", "residential-roofing/"), ("Pricing", "pricing/"), ("All articles", "blog/")])}</div></section>' + cta(),
            "schema": [crumbs_ld(url, trail),
                       {"@type": "BlogPosting", "@id": url + "#article", "headline": "What Is the 25% Rule for Roofing? (And Does It Apply in Utah?)",
                        "description": "Where the 25% roofing rule comes from, Florida's 2022 change, and the re-roof rules that apply in Utah today.",
                        "image": U + "assets/img/" + hero + ".webp", "datePublished": "2026-10-17", "dateModified": "2026-10-17",
                        "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": url, "inLanguage": "en-US",
                        "citation": [FBC, SB4D, ICC, WESTPOINT, FIRESTONE]},
                       faq_ld(FAQ)],
            "full_biz": False}
