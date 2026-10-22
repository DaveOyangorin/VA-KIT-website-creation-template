"""New blog post for trustyappliancerepairutah.com (22 Oct 2026): refrigerator and freezer temperatures for food safety. Informational; it
doesn't target refrigerator repair or other repair keywords. Sources: U.S. FDA "Are You Storing Food Safely?", "Refrigerator Thermometers:
Cold Facts about Food Safety" and "Food and Water Safety During Power Outages and Floods". USDA FSIS and FoodSafety.gov pages were
unreachable (403) on 22 Oct."""
from engine import faq_html, faq_ld, canon

SLUG = "refrigerator-freezer-temperature-food-safety/"
H1 = "What temperature should your fridge and freezer be? A food-safety guide"
FAQ = [("What temperature should a refrigerator be?", "FDA says to keep your refrigerator at or below 40&deg;F (4&deg;C)."),
       ("What temperature should a freezer be?", "0&deg;F (&minus;18&deg;C). Food kept frozen at 0&deg;F stays safe indefinitely, though quality drops the longer it&rsquo;s stored."),
       ("How long does food last in the fridge without power?", "About 4 hours if the door stays closed, according to FDA. A full freezer holds its temperature about 48 hours (24 hours if half full) with the door closed."),
       ("Does putting hot food in the fridge hurt it?", "No. FDA notes that putting hot food in the refrigerator doesn&rsquo;t harm the appliance. To help it cool faster, divide leftovers into smaller containers.")]
BODY = f'''<p class="answer">Keep your refrigerator at or below 40&deg;F and your freezer at 0&deg;F, and check both with an inexpensive appliance thermometer, because most refrigerator controls don&rsquo;t show the actual temperature. Don&rsquo;t leave perishable food out more than 2 hours (1 hour above 90&deg;F), and after a power outage, use the thermometer, not your nose, to decide what to keep.</p>

<p>Your refrigerator is one of the most important food-safety tools in your house, and also one of the easiest to take for granted. If it runs a few degrees warm, nothing looks wrong. The milk still pours, the leftovers still look fine. But according to the U.S. Food and Drug Administration (FDA), temperature is exactly what keeps the bacteria behind foodborne illness in check. Here&rsquo;s what FDA recommends, and how to tell whether your fridge is actually doing its job.</p>

<h2>The two numbers that matter</h2>
<ul>
<li><strong>Refrigerator: 40&deg;F (4&deg;C) or below.</strong></li>
<li><strong>Freezer: 0&deg;F (&minus;18&deg;C).</strong></li>
</ul>
<p>FDA explains why: at room temperature, the bacteria that cause foodborne illness can double every 20 minutes. Chilling food to proper temperatures is one of the best ways to slow that growth. Freezing doesn&rsquo;t kill most bacteria, but it does stop them from growing, so food kept at 0&deg;F stays safe indefinitely. Quality is a different matter: tenderness, flavor, aroma, juiciness and color all fade the longer food sits in the freezer.</p>

<h2>Why you need an appliance thermometer</h2>
<p>Here&rsquo;s the catch: FDA points out that few refrigerator controls show actual temperatures. A dial set to &ldquo;4&rdquo; or &ldquo;colder&rdquo; tells you nothing about what&rsquo;s happening on the shelves.</p>
<p>FDA&rsquo;s fix is simple and cheap: buy a freestanding appliance thermometer for the refrigerator and another for the freezer. Put each one in the front, in an easy-to-read spot, and <strong>check them regularly, at least once a week</strong>. If the readings drift above 40&deg;F or 0&deg;F, adjust the setting.</p>
<p>If you adjust the controls and the fridge still won&rsquo;t hold 40&deg;F, that&rsquo;s worth paying attention to. A refrigerator that can&rsquo;t keep temperature is a food-safety problem, not just an inconvenience.</p>

<h2>Help your fridge stay cold</h2>
<p>FDA&rsquo;s refrigerator strategies are mostly about letting cold air do its work:</p>
<ul>
<li><strong>Don&rsquo;t overpack.</strong> Cold air has to circulate around food to keep it properly chilled. That goes for the freezer too.</li>
<li><strong>Wipe up spills right away.</strong> It helps reduce the growth of Listeria, which can grow even at refrigerator temperatures, and stops drips from thawing meat spreading bacteria to other food.</li>
<li><strong>Keep food covered</strong> in containers or sealed bags, and check leftovers daily for spoilage.</li>
<li><strong>Store eggs in their carton on a shelf</strong>, not in the door, where it&rsquo;s warmer.</li>
<li><strong>Clean the fridge out frequently</strong> as part of your kitchen routine.</li>
</ul>

<h2>The 2-hour rule</h2>
<p>FDA&rsquo;s most important timing rule: <strong>never leave meat, poultry, seafood, eggs, produce or other food that needs refrigeration at room temperature for more than 2 hours, or 1 hour if the air is above 90&deg;F.</strong> That includes:</p>
<ul>
<li><strong>Groceries.</strong> Put cold items away as soon as you get home, and remember a car is usually hotter than room temperature.</li>
<li><strong>Leftovers.</strong> Refrigerate or freeze them within 2 hours. FDA notes that putting hot food in the fridge doesn&rsquo;t harm the appliance; divide large amounts into smaller containers so they cool faster.</li>
<li><strong>Take-out and doggie bags.</strong> The same 2-hour limit applies. If you can&rsquo;t get home within 2 hours, FDA suggests skipping the doggie bag.</li>
<li><strong>Marinating food.</strong> Always marinate in the refrigerator, and never reuse marinade as a sauce unless you bring it to a rapid boil first.</li>
</ul>

<h3>Thaw in the fridge, not on the counter</h3>
<p>FDA says it&rsquo;s unsafe to thaw food at room temperature. There are three safe ways: in the refrigerator, in cold water (change the water every half hour), or in the microwave (then cook it immediately).</p>

<h2>Freezer facts</h2>
<ul>
<li><strong>Freezer burn isn&rsquo;t a safety problem.</strong> FDA calls it a quality issue: grayish-brown leathery spots where air reached the food.</li>
<li><strong>Freezing doesn&rsquo;t reduce nutrients.</strong> There&rsquo;s little change in a food&rsquo;s protein value.</li>
<li><strong>Store leftovers in tight containers</strong>, and follow package cooking instructions for commercially frozen foods.</li>
</ul>

<h2>When the power goes out</h2>
<p>Utah storms and summer heat can knock out power. FDA&rsquo;s guidance starts before the outage: keep appliance thermometers in the fridge and freezer, freeze containers of water for ice, and group food together in the freezer so it stays cold longer.</p>
<h3>During the outage</h3>
<ul>
<li><strong>Keep the doors closed</strong> as much as possible.</li>
<li>An unopened refrigerator keeps food cold for <strong>about 4 hours</strong>.</li>
<li>A full freezer holds its temperature for <strong>about 48 hours</strong> (24 hours if half full) with the door closed.</li>
<li>For a long outage, dry or block ice helps. FDA says 50 pounds of dry ice should keep an 18-cubic-foot, fully stocked freezer cold for two days.</li>
</ul>
<h3>When power comes back</h3>
<ul>
<li>If the freezer thermometer reads <strong>40&deg;F or below</strong>, the food is safe and can be refrozen. Without a thermometer, check each package: food that still has ice crystals or is 40&deg;F or below can be refrozen or cooked.</li>
<li>Refrigerated food should be safe if the power was out <strong>no more than 4 hours</strong> and the doors stayed closed.</li>
<li><strong>Discard</strong> refrigerated perishables such as meat, poultry, seafood, milk, eggs and leftovers that sat above 40&deg;F for 4 hours or more.</li>
<li>Don&rsquo;t rely on appearance or smell. FDA warns that food can make you sick even when it doesn&rsquo;t look, smell or taste spoiled.</li>
</ul>
<p>When in doubt, FDA&rsquo;s rule is simple: <strong>throw it out.</strong></p>

<h2>Common questions</h2>
{faq_html(FAQ)}

<h2>The short version</h2>
<ul>
<li>Fridge at or below 40&deg;F, freezer at 0&deg;F. Check with appliance thermometers weekly.</li>
<li>Don&rsquo;t overpack, keep food covered, and keep eggs off the door.</li>
<li>Two hours out, max (one hour above 90&deg;F).</li>
<li>In an outage, keep doors shut: about 4 hours for the fridge, 48 for a full freezer.</li>
</ul>

<p>If your refrigerator or freezer won&rsquo;t hold temperature, Trusty Appliance Repair in Sandy can take a look. Call <a href="tel:+18012559063">(801) 255-9063</a>. Licensed and insured, with a 90-day warranty on all repairs.</p>

<div class="sources"><p class="label">Sources</p><ul>
<li>U.S. FDA, <a href="https://www.fda.gov/consumers/consumer-updates/are-you-storing-food-safely" rel="noopener">Are You Storing Food Safely?</a></li>
<li>U.S. FDA, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/refrigerator-thermometers-cold-facts-about-food-safety" rel="noopener">Refrigerator Thermometers: Cold Facts about Food Safety</a></li>
<li>U.S. FDA, <a href="https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods" rel="noopener">Food and Water Safety During Power Outages and Floods</a></li>
</ul></div>'''


def page(K):
    return K.page(SLUG, "Fridge &amp; freezer temperature", H1, "From the blog &middot; Oct 22, 2026", "Blog", "Fridge &amp; Freezer Temperature for Food Safety | Trusty",
                  "Keep your fridge at 40°F or below and your freezer at 0°F. FDA tips on appliance thermometers, the 2-hour rule and what to keep or toss after a power outage.",
                  BODY, image="tr-steel", alt="A stainless steel refrigerator door", crumbs=[("Tips", "blogs/")], ogtype="article",
                  schema=[{"@type": "BlogPosting", "@id": canon(SLUG) + "#post", "headline": "What temperature should your fridge and freezer be? A food-safety guide", "datePublished": "2026-10-22", "dateModified": "2026-10-22",
                           "author": {"@type": "Organization", "name": "Trusty Appliance Repair"}, "publisher": {"@id": K.C.U + "#business"}, "mainEntityOfPage": canon(SLUG)}, faq_ld(FAQ)])
