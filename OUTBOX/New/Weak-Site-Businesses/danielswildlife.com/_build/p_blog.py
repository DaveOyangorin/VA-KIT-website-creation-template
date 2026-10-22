"""New blog post for danielswildlife.com (22 Oct 2026): cleaning up mouse droppings safely (hantavirus basics). Informational; it doesn't
target "pest control cottonwood heights", rodent control or any removal keyword. Sources: CDC "About Hantavirus" (13 May 2024); National
Park Service "Hantavirus" fact sheet with light-infestation cleanup and trapping guidance (June 2025)."""
from engine import faq_html, faq_ld, canon

SLUG = "how-to-clean-up-mouse-droppings/"
H1 = "Found mouse droppings? How to clean up safely"
FAQ = [("Can I vacuum or sweep up mouse droppings?", "No. The National Park Service says to never sweep or vacuum, because disturbing contaminated material and breathing the dust is the most common way people are exposed to hantavirus."),
       ("What disinfectant should I use?", "NPS guidance is a bleach solution diluted 1:10 with water, made fresh each day, or a pre-made product labeled as a disinfectant with an EPA registration number. Soak the area and let it sit at least 10 minutes."),
       ("How do people get hantavirus?", "CDC says people get it from contact with rodents like rats and mice, especially their urine, droppings and saliva. In the U.S., the most common hantavirus that causes hantavirus pulmonary syndrome is spread by the deer mouse."),
       ("When should I call a professional?", "The NPS steps are written for light infestations. Heavy infestations call for more stringent protective measures. If droppings are widespread, the building has sat vacant, or you can&rsquo;t find how mice are getting in, get help.")]
BODY = f'''<p class="answer">Don&rsquo;t sweep or vacuum mouse droppings. Air the space out for at least 30 minutes, put on gloves, soak the droppings and the area around them with a 1:10 bleach solution or an EPA-registered disinfectant, wait at least 10 minutes, then wipe up with paper towels, bag everything twice and wash your hands. That&rsquo;s National Park Service guidance for light infestations; heavy ones need more protection.</p>

<p>The National Park Service notes that indoor mouse activity is highest in fall and winter, and droppings are often the first sign, in a garage, a pantry, a storage room or the attic. Cleaning them up is a normal part of homeownership in Utah, but the way you do it matters because of hantavirus. Here&rsquo;s what federal health and parks guidance says.</p>

<h2>Why droppings aren&rsquo;t just a mess</h2>
<p>According to the CDC, hantaviruses are a family of viruses that can cause serious illness and death. People get them from contact with rodents like rats and mice, especially when exposed to their urine, droppings and saliva. In the United States, the most common hantavirus that causes hantavirus pulmonary syndrome (HPS) is spread by the <strong>deer mouse</strong>.</p>
<p>The National Park Service&rsquo;s June 2025 fact sheet adds that the deer mouse is the primary host in the western U.S., that most human illnesses have occurred in rural residents of western states, and that infected rodents typically show no signs of illness. The virus responsible for disease in the U.S. cannot be transmitted from person to person, and pets are not known to transmit it to people.</p>
<p>Most importantly for cleanup: NPS says <strong>disturbing contaminated material, such as sweeping, vacuuming or disturbing nests, and breathing in the dust is the most common cause of exposure.</strong></p>

<h2>Know the symptoms</h2>
<p>CDC says symptoms of HPS usually start 1 to 8 weeks after contact with an infected rodent. Early symptoms can include fever, muscle aches, headaches, nausea and vomiting; later symptoms such as coughing and shortness of breath appear 4 to 10 days after that first phase. CDC notes that HPS can be deadly: 38% of people who develop respiratory symptoms may die from the disease.</p>
<p>If you have symptoms and were recently around rodents or their droppings, NPS advises telling your healthcare provider. There is no specific treatment, but early supportive care can improve outcomes.</p>

<h2>Step by step: cleaning up a light infestation</h2>
<p>The NPS directions below are written for <strong>light</strong> rodent infestations, meaning signs of rodent activity or droppings in a building:</p>
<ol>
<li><strong>Air it out first.</strong> Open windows to ventilate for at least 30 minutes before cleaning, and leave the area during that time. Direct sunlight also helps inactivate the virus. Don&rsquo;t stir up dust, and never sweep or vacuum.</li>
<li><strong>Mix your disinfectant.</strong> If using bleach, dilute it with water to a 1:10 solution, made fresh each day, or use a pre-made disinfectant. Make sure the product is labeled as a disinfectant and has an EPA registration number.</li>
<li><strong>Wear gloves.</strong> Disinfect reusable gloves after use.</li>
<li><strong>Soak, then wait.</strong> Thoroughly soak the droppings, nest, dead rodent or trap with disinfectant, spraying at least a 2-foot area around each. Let it sit undisturbed for <strong>at least 10 minutes</strong>.</li>
<li><strong>Bag it.</strong> Turn a plastic bag inside out over your gloved hand, pick up the trap or carcass, seal the bag, then seal it inside a second bag. Keep the rodent at arm&rsquo;s length.</li>
<li><strong>Wipe up what&rsquo;s left.</strong> Re-spray any exposed droppings, then clean them up with disposable paper towels.</li>
<li><strong>Clean yourself up.</strong> Spray your gloves while still wearing them; bag and seal disposable gloves. Wash your hands with soap and water after the gloves come off.</li>
<li><strong>Dispose of the trash</strong> in a regularly emptied bin, following local trash rules.</li>
<li><strong>Deal with soft items.</strong> Steam clean upholstery, shampoo with a disinfectant, or throw out heavily contaminated items.</li>
</ol>

<h2>Light or heavy?</h2>
<p>NPS points out that heavy infestations require more stringent personal protection than the steps above. When judging how bad it is, it suggests considering how long a building has been vacant and the season, since indoor mouse activity is highest in fall and winter. It also notes that mice can leave up to 100 droppings a day under certain conditions, so a problem can grow quickly.</p>

<h2>Stop them coming back</h2>
<p>Cleanup only fixes what&rsquo;s already there. NPS prevention guidance includes:</p>
<ul>
<li><strong>Seal gaps larger than one quarter of an inch</strong> to keep rodents out of buildings.</li>
<li><strong>Store food and trash properly</strong>, and keep pet food in sealed containers.</li>
<li><strong>Keep vegetation at least 18 inches from buildings.</strong></li>
<li><strong>Trap and monitor.</strong> Snap traps set with the trigger end against the wall work well; two side by side can be more effective. NPS suggests about 10 snap traps for a 12-by-12-foot room in an active infestation.</li>
</ul>
<p>Finding every entry point is the hard part, and sealing them with durable, chew-resistant materials is what makes the fix last.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Droppings in the attic, crawlspace or walls, or mice that keep coming back? Daniel&rsquo;s Wildlife &amp; Pest handles rodent control, exclusion and cleanup across the Salt Lake Valley. Call or text <a href="tel:+18017839638">(801) 783-9638</a>, 24/7.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>CDC, <a href="https://www.cdc.gov/hantavirus/about/index.html" rel="noopener">About Hantavirus</a> (May 13, 2024)</li>
<li>CDC, <a href="https://www.cdc.gov/hantavirus/prevention/index.html" rel="noopener">Preventing Hantavirus</a> (May 13, 2024)</li>
<li>National Park Service, <a href="https://www.nps.gov/articles/000/upload/Hantavirus-fact-sheet-and-light-infestation-cleaning-guidanceJune2025-508c.pdf" rel="noopener">Hantavirus fact sheet and light infestation cleaning guidance</a> (June 2025)</li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Cleaning up mouse droppings", H1, "From the blog &middot; Oct 22, 2026", "Blog", "How to Clean Up Mouse Droppings Safely | Daniel's Wildlife",
                  "Found mouse droppings? Why you shouldn't sweep or vacuum, the step-by-step safe cleanup from National Park Service guidance, and hantavirus facts from CDC.",
                  BODY, image="dw-mice", alt="A rodent bait station", ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Daniel's Wildlife & Pest Control"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
