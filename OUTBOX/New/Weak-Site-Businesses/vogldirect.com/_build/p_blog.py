"""New blog post for vogldirect.com (22 Oct 2026): R-22 and refrigerant rules for homeowners. Informational; it doesn't target AC repair,
furnace repair, HVAC company or installation keywords. Sources: U.S. EPA fact sheet "Residential Air Conditioning and the Phaseout of HCFC-22:
What You Need to Know" (EPA-430-FR-20001), "Stationary Refrigeration Resources for Homeowners", "Stationary Refrigeration Safe Disposal
Requirements", "Hydrofluorocarbons (HFCs)" (AIM Act) and "Regulatory Actions for Technology Transitions"."""
from engine import faq_html, faq_ld, canon

SLUG = "r-22-refrigerant-what-homeowners-should-know/"
H1 = "R-22 and your air conditioner: what Utah homeowners should know"
FAQ = [("Do I have to replace my R-22 air conditioner?", "No. EPA says no immediate change is required. U.S. production and import of HCFC-22 (R-22) ended on January 1, 2020, but you may keep using R-22 in your existing system for as long as necessary."),
       ("How do I know if my AC uses R-22?", "Check the nameplate on the outdoor unit. EPA notes most air conditioners have a nameplate that identifies the refrigerant it contains, along with safety certifications and electrical ratings."),
       ("Is R-22a the same as R-22?", "No. EPA warns that R-22a has been falsely marketed as R-22 or a replacement. It is a hydrocarbon blend of flammable substances such as propane and butane, and it is not an acceptable alternative for a home AC system."),
       ("Can a technician just release old refrigerant?", "No. Under Section 608 of the Clean Air Act, it is illegal for anyone to knowingly vent or intentionally release refrigerant while servicing, repairing, maintaining or disposing of AC equipment. Central residential AC must have its refrigerant recovered before disposal.")]
BODY = f'''<p class="answer">If your home air conditioner uses R-22 (HCFC-22), you don&rsquo;t have to replace it. U.S. production and import of R-22 ended on January 1, 2020, but EPA says you can keep using it in your existing system for as long as necessary. Keep it maintained and leak-free, never let anyone add &ldquo;R-22a,&rdquo; and make sure any refrigerant is recovered, not vented, when the system is serviced or replaced.</p>

<p>Refrigerant used to be something homeowners never thought about. Then came the R-22 phaseout, rising refrigerant prices, and newer rules on the refrigerants that replaced it. If you have an older AC or heat pump in Utah County or the Salt Lake Valley, or you&rsquo;re weighing a repair against a replacement, here&rsquo;s what the U.S. Environmental Protection Agency (EPA) actually says, in plain terms.</p>

<h2>What R-22 is, and why it was phased out</h2>
<p>HCFC-22, commonly called R-22, is a refrigerant used in many applications, including home air conditioning. It belongs to a family of chemicals called hydrochlorofluorocarbons (HCFCs) that deplete the stratospheric ozone layer.</p>
<p>To protect the ozone layer, under the U.S. Clean Air Act and the Montreal Protocol, the United States has phased out the production and import of HCFCs, with limited exceptions. EPA explains that phasing out ozone-depleting substances reduces the risk of skin cancer from UV radiation, and that many of these substances are also potent greenhouse gases.</p>
<p>The key date for homeowners: <strong>U.S. production and import of R-22 ended on January 1, 2020.</strong></p>

<h2>Do you need to do anything right now?</h2>
<p>No. EPA&rsquo;s fact sheet puts it plainly: <strong>no immediate change is required.</strong> You may continue to use R-22 in your existing system for as long as necessary. R-22 that is recovered and reclaimed, along with R-22 produced before 2020, helps meet the needs of people who still own R-22 systems.</p>
<p>That last point matters. Reclaimed refrigerant, recovered from equipment being serviced or removed and cleaned up for reuse, is part of how existing systems keep running. It&rsquo;s one reason proper recovery is required, not optional.</p>

<h2>How to tell what refrigerant your AC uses</h2>
<p>Go look at the outdoor unit. EPA notes that most air conditioners have a <strong>nameplate</strong> that identifies the refrigerant the system contains, along with other information like safety certifications and electrical ratings. If the plate says HCFC-22 or R-22, you have an R-22 system. If you can&rsquo;t find or read it, your technician can tell you during a service visit.</p>

<h2>Keeping an R-22 system running well</h2>
<p>Even though nothing is forced on you, EPA recommends planning ahead. Its advice is to <strong>ask your service technician to check for leaks and perform preventive maintenance.</strong> That helps keep refrigerant emissions down and reduces the need to buy additional R-22.</p>
<p>A system that keeps needing a refrigerant top-off has a leak somewhere. Finding and fixing it protects the refrigerant you have, keeps the system running the way it was designed, and avoids paying for refrigerant that ends up in the air.</p>

<h2>When it&rsquo;s time to replace or retrofit</h2>
<p>EPA notes that air conditioning equipment generally runs most efficiently on the refrigerant it was designed for. When the time does come to replace or retrofit, there are many non-ozone-depleting alternatives available, listed as acceptable under EPA&rsquo;s Significant New Alternatives Policy (SNAP) program. Some are for new systems, others for both new and retrofitted systems.</p>
<p>If a technician is <strong>retrofitting</strong> your existing system to a different refrigerant, EPA says to make sure they:</p>
<ol>
<li>Recover any R-22 still in your AC.</li>
<li>Follow the manufacturer&rsquo;s handling and installation guidelines for that particular alternative.</li>
<li>Explain how the conversion might affect your system&rsquo;s performance and energy use.</li>
</ol>
<p>When you&rsquo;re buying new equipment, EPA&rsquo;s homeowner resources also suggest looking for the ENERGY STAR&reg; label, which marks equipment that meets efficiency guidelines set by EPA and the U.S. Department of Energy.</p>

<h2>Never use R-22a</h2>
<p>This is the warning EPA repeats most often. <strong>R-22a (or &ldquo;22a&rdquo;) is not R-22 and not an acceptable replacement.</strong> EPA says it has been falsely marketed as R-22 or an R-22 replacement, but it is a hydrocarbon blend whose main components include flammable substances such as propane and butane. EPA notes these propane-based refrigerants have never been submitted to it for review of their health and environmental impacts, and that using them in an air conditioner not designed for flammable refrigerants poses a threat to homeowners and service technicians. EPA has taken enforcement action where appropriate.</p>
<p>If anyone offers to &ldquo;top off&rdquo; your R-22 system with a cheap substitute, ask exactly what it is.</p>

<h2>Venting refrigerant is illegal</h2>
<p>Under Section 608 of the Clean Air Act and EPA&rsquo;s regulations, it is <strong>illegal for anyone to knowingly vent or intentionally release refrigerant</strong> while servicing, repairing, maintaining or disposing of air conditioning equipment. Additional handling, recovery and sales requirements apply to certain refrigerants, and technicians who service this equipment must be certified.</p>
<p>That applies when equipment is removed, too. EPA&rsquo;s safe disposal rules say equipment that is typically dismantled on site before disposal, which <strong>includes central residential air conditioning</strong>, must have its refrigerant recovered according to EPA&rsquo;s servicing requirements before it is disposed of. If you&rsquo;re remodeling, demolishing, or simply replacing an old condenser, the refrigerant has to be properly recovered first.</p>

<h2>What about the newer refrigerants?</h2>
<p>R-22 isn&rsquo;t the only refrigerant in transition. Many systems installed after R-22 use hydrofluorocarbons (HFCs). Under the American Innovation and Manufacturing (AIM) Act, EPA is addressing HFCs by phasing down their production and consumption, maximizing reclamation and minimizing releases from equipment, and facilitating the move to next-generation technologies through sector-based restrictions.</p>
<p>For home air conditioning and heat pumps, EPA has issued rules on which refrigerants new systems can use and when. Those rules have been adjusted more than once: in December 2023, for example, EPA allowed inventory of higher-GWP HFC residential equipment manufactured or imported before January 1, 2025 to be installed until January 1, 2026, and in May 2026 EPA finalized a rule reconsidering certain Technology Transitions requirements, including for residential and light commercial air conditioning and heat pumps. If you&rsquo;re buying a new system, ask your contractor which refrigerant it uses and how current rules apply to it.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>Check the nameplate on your outdoor unit to see which refrigerant you have.</li>
<li>An R-22 system can keep running. No immediate change is required.</li>
<li>Fix leaks and keep up maintenance so you don&rsquo;t need more R-22.</li>
<li>Never let anyone put R-22a in your system.</li>
<li>Refrigerant must be recovered, never vented, during service and before disposal.</li>
</ul>

<p>Vogl Direct is certified and licensed to recover refrigerant, and services and installs heating and air across Utah County, Salt Lake County and Tooele. For a free on-site estimate or a second opinion, call or text <a href="tel:+13853523285">(385) 352-3285</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. EPA, <a href="https://www.epa.gov/ods-phaseout/residential-air-conditioning-and-phaseout-hcfc-22-what-you-need-know" rel="noopener">Residential Air Conditioning and the Phaseout of HCFC-22: What You Need to Know</a> (EPA-430-FR-20001)</li>
<li>U.S. EPA, <a href="https://www.epa.gov/section608/stationary-refrigeration-resources-homeowners" rel="noopener">Stationary Refrigeration Resources for Homeowners</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/section608/stationary-refrigeration-safe-disposal-requirements" rel="noopener">Stationary Refrigeration Safe Disposal Requirements</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/climate-hfcs-reduction" rel="noopener">Hydrofluorocarbons (HFCs) and the AIM Act</a></li>
<li>U.S. EPA, <a href="https://www.epa.gov/hfcs/regulatory-actions-technology-transitions" rel="noopener">Regulatory Actions for Technology Transitions</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "R-22 refrigerant", H1, "From the blog &middot; Oct 22, 2026", "Blog", "R-22 Refrigerant: What Utah Homeowners Should Know | Vogl",
                  "Your R-22 air conditioner can keep running. What EPA says about the phaseout, checking your nameplate, R-22a dangers and why venting refrigerant is illegal.",
                  BODY, image="vg-lake", alt="Utah Lake and the Lake Mountains", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "R-22 and your air conditioner: what Utah homeowners should know", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Vogl Direct"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
