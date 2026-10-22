"""New blog post for pestx.org (21 Oct 2026). Topic picked so it doesn't compete with any of the ten pest pages (ticks have no page)
or the three existing posts. Facts from: USU Extension "Ticks and Tickborne Diseases of Utah" (July 2023), Utah DHHS Tick Surveillance
Annual Report 2024, and CDC "Preventing Tick Bites". Nothing about Pestx's services is claimed beyond its own pages."""
from engine import faq_html, faq_ld
from pagekit import ARROW

SLUG = "blogs/ticks-in-utah/"
TITLE = "Ticks in Utah: Where They Live, When They Bite, and What to Do"
H1 = "Ticks in Utah: where they live, when they bite, and what to do"
FAQ = [("When is tick season in Utah?", "Ticks are most likely to be found from snowmelt through mid-July, according to USU Extension. Activity can pick up again in the fall, and timing shifts with elevation and the year&rsquo;s weather."),
       ("Is there Lyme disease in Utah?", "Utah has reported Lyme disease cases, but the state health department says most patients had traveled to areas where Lyme is common, and there is no current evidence of Lyme being passed by ticks inside Utah."),
       ("What&rsquo;s the most common tick in Utah?", "The Rocky Mountain wood tick (<i>Dermacentor andersoni</i>). It&rsquo;s the tick people and pets meet most often, and it can carry Colorado tick fever and Rocky Mountain spotted fever."),
       ("Should I keep a tick after removing it?", "USU Extension suggests saving it in rubbing alcohol. If a rash or fever shows up later, knowing which tick bit you helps a doctor with the diagnosis.")]

BODY = f'''<p class="answer">Utah&rsquo;s ticks are most active from snowmelt through mid-July. The one you&rsquo;re most likely to find on yourself, your kids or your dog is the Rocky Mountain wood tick. A quick check after time outdoors, and removing a tick the right way, prevents most problems.</p>

<p>Ticks aren&rsquo;t on Pestx&rsquo;s list of <a href="@/pests/">common Utah pests</a>, and that&rsquo;s fair: they live in grass and brush, not in kitchens and basements. Still, anyone who hikes the Wasatch foothills, camps in the Uintas or lets the dog run in a field at the edge of town will meet one sooner or later. This guide pulls together what Utah State University Extension, the Utah Department of Health and Human Services and the CDC say about ticks here: which species you&rsquo;ll see, when and where, which diseases matter, and what to do if one bites.</p>

<h2>Which ticks live in Utah?</h2>
<p>USU Extension&rsquo;s fact sheet <i>Ticks and Tickborne Diseases of Utah</i> lists several species. The ones that matter most to people are:</p>
<ul>
<li><strong>Rocky Mountain wood tick</strong> (<i>Dermacentor andersoni</i>). By far the most common tick found on people and pets in Utah. The state&rsquo;s 2024 tick surveillance report also names it the most common tick in the state.</li>
<li><strong>Brown dog tick</strong> (<i>Rhipicephalus sanguineus</i>). It usually develops on dogs and can come indoors on an infested dog. This is the one tick that can become a household problem.</li>
<li><strong>Winter tick</strong> (<i>Dermacentor albipictus</i>). It spends its life on one large animal such as an elk, moose or horse, so people rarely meet it.</li>
<li><strong>Western blacklegged tick</strong> (<i>Ixodes pacificus</i>). Uncommon in Utah. It matters because it&rsquo;s the only tick here that can carry Lyme disease (more on that below).</li>
<li><strong>Soft ticks</strong> (<i>Ornithodoros</i> species). These live in animal burrows and in cabins with rodent nests. They feed quickly, often at night, and people seldom notice them.</li>
</ul>

<h2>When are ticks active?</h2>
<p>According to USU Extension, Utah ticks are most likely to be encountered <strong>from snowmelt through mid-July</strong>. A moist spring means more ticks; hot, dry summer weather slows them down. Activity can pick up again in the fall. Because the season starts at snowmelt, it moves uphill as the year goes on. A south-facing foothill trail can have active ticks in early spring while higher canyons are still under snow.</p>

<h2>Where do they wait?</h2>
<p>Ticks don&rsquo;t jump, fly or drop from trees. They &ldquo;quest&rdquo;: they climb grass, low plants or sagebrush, hold out their front legs, and grab whatever brushes past. USU Extension says they usually wait from ground level up to about three feet, along the edges of fields and woodlands. That&rsquo;s why ankles, legs and the dog&rsquo;s face take the most contact, and why staying in the middle of a trail makes such a difference. The CDC gives the same advice: avoid brushy areas with high grass and leaf litter, and walk in the center of trails.</p>
<p>Once on a host, a tick often wanders for a while before it bites. USU Extension notes that ticks often take two hours or more to find a feeding spot and attach, and that disease transmission usually starts 12 to 24 hours after feeding begins. That gap is your window: a tick found and removed the same day is far less likely to pass anything on.</p>

<h2>Which diseases matter here?</h2>
<p>The Utah Department of Health and Human Services&rsquo; 2024 tick surveillance report puts it plainly: <strong>Colorado tick fever</strong> is the most common tickborne disease in Utah, followed by <strong>Rocky Mountain spotted fever</strong>. The Rocky Mountain wood tick can carry both. They&rsquo;re rare. The report counts one or two Colorado tick fever cases a year and, on average, one Rocky Mountain spotted fever case every five years. Rare doesn&rsquo;t mean ignore it, though: there&rsquo;s no vaccine or specific treatment for Colorado tick fever, while Rocky Mountain spotted fever is treated with antibiotics and is serious if it&rsquo;s missed.</p>
<p>USU Extension lists a few others: tularemia and tick paralysis from the wood tick, and tick-borne relapsing fever from soft ticks. Tick paralysis starts in the feet and moves upward. It reverses once the tick is removed, which is one more reason to check children and dogs after time outdoors.</p>

<h3>What about Lyme disease?</h3>
<p>Lyme disease is reported in Utah, but the state health department says most patients had traveled to places where Lyme is common, such as the upper Midwest and the East Coast, and that there&rsquo;s no current evidence of ticks passing Lyme inside Utah. USU Extension explains why: only the western blacklegged tick can carry it here, and it&rsquo;s scarce. In a three-year survey, 119 were collected from 160 sites, almost all from a few spots in the Sheeprock Mountains of Tooele County, and every one tested negative.</p>

<h2>Before you head out</h2>
<ul>
<li>Use an EPA-registered insect repellent. The CDC adds: apply sunscreen first and repellent second, and don&rsquo;t use products with oil of lemon eucalyptus (OLE) or PMD on children under three.</li>
<li>Treat boots, clothing and camping gear with 0.5% permethrin, or buy pre-treated gear. Utah&rsquo;s health department recommends this too.</li>
<li>Wear long pants and long sleeves. Tucking pants into socks keeps questing ticks on the outside, where you can see them.</li>
<li>Stay in the center of the trail, away from tall grass and brush.</li>
</ul>

<h2>When you get home</h2>
<p>The CDC recommends showering within two hours of coming inside and doing a full-body check with a mirror. Check under the arms, in and around the ears, inside the belly button, behind the knees, in and around the hair, between the legs and around the waist. Tumble-dry clothes on high heat for ten minutes to kill any ticks still on them, and look over gear and pets before they come inside.</p>

<h2>How to remove a tick</h2>
<ol>
<li>Grasp the tick with fine tweezers as close to the skin as you can, by its mouthparts.</li>
<li>Pull straight up with steady pressure. Don&rsquo;t twist, crush or squeeze the body.</li>
<li>For very small ticks, USU Extension suggests scraping them off with the edge of a credit card or knife blade.</li>
<li>If the head breaks off, clean the area and lift it out with a sterile needle.</li>
<li>Wash the bite and your hands with soap and water, then apply an antibiotic ointment.</li>
</ol>
<p>Skip the old tricks: matches, nail polish and petroleum jelly. They keep the tick attached longer. Save the tick in a small container of rubbing alcohol, note the date and where you were, and watch for a rash or fever over the next few weeks. If either appears, see a doctor and mention the bite.</p>

<h2>Dogs and the yard</h2>
<p>Wood ticks attach to pets as readily as to people, and the brown dog tick can come home on a dog and settle indoors. Check your dog after every outing, especially the ears, neck, armpits and between the toes, and ask your vet about tick prevention.</p>
<p>Most Salt Lake Valley yards aren&rsquo;t prime tick habitat, but homes that back onto open space or foothill brush can be. The CDC&rsquo;s yard advice is simple: clear tall grass and brush at the edge of the lawn, remove leaf litter, mow often, stack firewood neatly in a dry spot, and keep play equipment and patios away from the yard&rsquo;s wild edges. A three-foot strip of wood chips or gravel between lawn and brush helps too. Many of the same habits, such as trimmed vegetation, less clutter and fewer hiding places, also keep the <a href="@/pests/rodents/">rodents</a> that carry ticks away from the house.</p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<p>Dealing with pests closer to home? Read the <a href="@/pests/">Utah pest field guide</a>, or call Pestx at <a href="tel:+18018719233">801-871-9233</a>.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>Utah State University Extension, <a href="https://extension.usu.edu/planthealth/research/ticks-and-tickborne-diseases-of-utah" rel="noopener">Ticks and Tickborne Diseases of Utah</a> (July 2023)</li>
<li>Utah Department of Health and Human Services, <a href="https://epi.utah.gov/wp-content/uploads/Tick-Surveillance-Annual-Report_2024.pdf" rel="noopener">Tick Surveillance Annual Report 2024</a></li>
<li>Centers for Disease Control and Prevention, <a href="https://www.cdc.gov/ticks/prevention/index.html" rel="noopener">Preventing Tick Bites</a></li>
<li>Utah State University Extension, <a href="https://extension.usu.edu/planthealth/news/avoiding-ticks" rel="noopener">Avoiding Ticks in Utah</a> (November 2023)</li>
</ul></div>'''


def page(K):
    from engine import canon
    pg = K.page(SLUG, "Ticks in Utah", H1, "Natural pest control solutions &middot; Oct 21, 2026", "Blog", "Ticks in Utah: Where They Live and What to Do | Pestx",
                "Utah ticks are most active from snowmelt to mid-July. Which species you'll meet, Colorado tick fever and Lyme facts, and how to remove a tick the safe way.",
                BODY, art=None, crumbs=[("Blog", "blogs/")], ogtype="article",
                schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": H1, "datePublished": "2026-10-21", "dateModified": "2026-10-21",
                         "author": {"@type": "Organization", "name": "Pestx"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
    return pg
