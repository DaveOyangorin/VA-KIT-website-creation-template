"""Blog for utahroofingpros.com: a new /blog with one post.

Post: "Attic Ventilation for Utah Homes: Intake, Exhaust and Ice Dams"
Main phrase: "attic ventilation" (informational). No service page targets it, so it doesn't compete with repair, replacement or
inspection; it links to the inspection, replacement and swamp cooler pages (the client's own swamp cooler page mentions
"reworking ventilation"). Facts and sources, checked 18 Oct 2026:
- International Residential Code R806.2: net free ventilating area at least 1/150 of the vented space; 1/300 is allowed when one of
  the listed conditions is met, one being that 40-50% of the required area is in the upper portion of the attic, no more than
  3 feet below the ridge, with the rest at the eaves or cornice (ICC copy of R806). https://iccsafe.org/wp-content/uploads/bcac/IRC-R806.pdf
- PNNL Building America Solution Center: ice dams form with snow on the roof, heat escaping from a poorly air-sealed or poorly
  insulated attic, and freezing temperatures; air sealing and insulation come first, ventilation keeps the deck cold.
  https://basc.pnnl.gov/information/attic-air-sealing-insulating-and-ventilating-ice-dam-prevention
The worked example is arithmetic on the code ratios. No prices.
"""
from engine import crumbs_ld, faq_html, faq_ld, canon, img
from cfg import U, NAME
from illus import vents

POST = ("Attic Ventilation for Utah Homes: Intake, Exhaust and Ice Dams", "blog/attic-ventilation-utah-homes/")
_ = {}


def setup(phero, cta, side, arrow, home, inspect):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, INSPECT=inspect)


SIGNS = [("Frost or damp on the underside of the roof deck", "Visible from the attic on cold mornings. Warm, moist house air is reaching the cold deck and condensing."),
         ("Heavy icicles and ice dams at the eaves", "Snow melting high on the roof and refreezing at the cold edge, often a sign of heat escaping into the attic."),
         ("Dark stains or mildew on the sheathing", "Moisture that keeps coming back. Look near the eaves and around bathroom fan ducts."),
         ("Rusty nail tips poking through the deck", "Another moisture clue: the nails are the coldest metal in the attic and collect condensation first."),
         ("An upstairs that bakes all summer", "A hot attic radiates down through the ceiling. Ventilation helps, but insulation does most of the work here.")]
FAQ = [("How much attic ventilation does a house need?", "Under the International Residential Code, the net free vent area should be at least 1/150 of the attic floor area, or 1/300 when certain conditions are met, such as putting 40 to 50 percent of the vent area high on the roof within 3 feet of the ridge. Your city&rsquo;s building department has the final word on what applies to your home."),
       ("Should intake and exhaust be equal?", "Close to it. The 1/300 option in the code expects roughly half the vent area high and the rest low at the eaves. An attic with lots of exhaust and little intake tends to pull air from the house instead of from outside."),
       ("Will more ventilation stop ice dams?", "Not by itself. Ice dams start with heat escaping from the house into the attic. Air sealing and insulation come first; ventilation then helps keep the roof deck cold so the snow doesn&rsquo;t melt unevenly."),
       ("Can ventilation be fixed without a new roof?", "Often, yes: blocked soffits can be cleared, baffles added and vents replaced. A roof replacement is simply the easiest time to get the whole system right, because the ridge and deck are open."),
       ("Do you check ventilation during an inspection?", "Yes. Vents are part of our free roof inspection, along with shingles, flashing, valleys and penetrations.")]


def post():
    path = POST[1]; A = _["A"]
    trail = [_["HOME"], ("Blog", "blog/"), ("Attic ventilation", path)]
    signs = "".join(f'<li><span class="mono">{i + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(SIGNS))
    body = _["phero"](trail, POST[0], "Your roof breathes through two sets of openings. Here is how attic ventilation works, how much a house needs, and why it matters in a Utah winter.", "Blog &middot; Roof care", buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">
<p class="mono meta">By {NAME} &middot; 18 Oct 2026 &middot; 7 min read</p>
<p class="answer">Attic ventilation is a steady flow of outside air through the attic: in low at the eaves, out high near the ridge. It keeps the roof deck cold and dry in winter, lets summer heat out, and protects the shingles and sheathing from moisture. Most homes need about 1 square foot of net vent area for every 150 to 300 square feet of attic floor, split between intake and exhaust.</p>

<h2>Why an attic needs to breathe</h2>
<p>An attic sits between two very different climates. Below it is a heated, lived-in house that puts moisture into the air every day from cooking, showers and breathing. Above it is a roof deck that, on a January night along the Wasatch Front, can be far below freezing. If warm, moist air reaches that cold deck and stays there, it condenses. Over a few winters that means damp sheathing, mildew and rusted fasteners, problems you won&rsquo;t see from the yard until they show up as stains on a ceiling.</p>
<p>Ventilation solves this by replacing attic air with outside air. Cold, dry winter air keeps the deck close to the outdoor temperature, and summer airflow carries off some of the heat that builds under the shingles.</p>
<figure class="post-img">{img("roof-vents-mountains", "Shingle roof with exhaust vents and the mountains behind")}<figcaption>Exhaust vents near the top of a roof. Intake vents sit out of sight under the eaves.</figcaption></figure>

<h2>Intake and exhaust: how the air moves</h2>
<p>A working system has two halves. <b>Intake</b> vents sit low, usually in the soffits under the eaves. <b>Exhaust</b> vents sit high: a continuous ridge vent, or individual box vents near the ridge. Warm air rises, so outside air enters at the eaves, sweeps along the underside of the deck, and leaves at the top.</p>
{vents()}
<p>Two details make or break it. First, insulation must not block the soffits; foam or cardboard <b>baffles</b> hold a channel open between the insulation and the deck. Second, the exhaust has to be fed by intake. A ridge vent over sealed-off soffits moves very little air, and a powered fan with no intake will pull air out of the house instead.</p>
<p>It also helps to keep one kind of exhaust on a roof. A ridge vent combined with a gable vent or a powered fan can short-circuit: the exhaust vents feed each other, and the soffits at the bottom stop doing their job.</p>

<h2>How much ventilation a house needs</h2>
<p>The International Residential Code sets the baseline in Section R806. The net free ventilating area (the open area of a vent after screens and louvers, printed on the product in square inches) must be at least <b>1/150</b> of the attic floor area. It can drop to <b>1/300</b> when the attic meets one of the listed conditions, the common one being that 40 to 50 percent of the required area comes from vents in the upper part of the attic, no more than 3 feet below the ridge, with the rest at the eaves.</p>
<p>Here is what that means for an attic with 1,500 square feet of floor:</p>
<ul>
<li>At 1/150: 10 square feet, or 1,440 square inches of net free area.</li>
<li>At 1/300: 5 square feet, or 720 square inches, about 360 high and 360 low.</li>
</ul>
<p>Utah adopts the IRC with state amendments, and your city&rsquo;s building department has the final word on what applies, so treat these numbers as the starting point, not the last word. On a re-roof, a roofer should check what&rsquo;s there now, count the net free area, and say on the estimate what will change.</p>

<h2>Ventilation and ice dams</h2>
<p>Ice dams are a familiar sight in Utah neighborhoods after a snowy week: a ridge of ice along the eaves with water backed up behind it. According to the Building America Solution Center, run by the Pacific Northwest National Laboratory for the U.S. Department of Energy, ice dams need three things: snow on the roof, heat escaping from a poorly air-sealed or poorly insulated attic, and freezing temperatures. Heat from the house melts the snow high on the roof; the water runs down to the cold eaves and freezes there.</p>
<p>The fix starts below the roof. Sealing the gaps where house air leaks into the attic (around light fixtures, the attic hatch, plumbing and duct chases) and adding insulation stop most of the heat. Ventilation then keeps the deck cold and even, so the snow melts from the sun, not from the house. Ventilation alone won&rsquo;t cure an attic that leaks heat, and an ice and water shield membrane at the eaves is still the roof&rsquo;s backup when ice does form.</p>

<h2>Five signs your attic isn&rsquo;t venting well</h2>
<ol class="items">{signs}</ol>
<p>If you see more than one of these, it&rsquo;s worth having someone look at the intake, the exhaust and the insulation together.</p>

<h2>Old swamp coolers and other holes in the system</h2>
<p>Many older homes along the Wasatch Front still have a swamp cooler on the roof, or the patched opening where one used to be. A cooler opening, a bathroom fan venting into the attic instead of outside, or a kitchen duct that ends short of the roof all add moisture or upset the airflow. When we <a href="@/services/residential-roofing/swamp-cooler-removal-roof-repair/">remove a swamp cooler</a>, the opening is repaired and sealed, and it&rsquo;s a good moment to look at how the attic is vented.</p>

<h2>The best time to fix it</h2>
<p>Ventilation can often be improved on an existing roof: clearing blocked soffits, adding baffles, or swapping a few box vents. But a <a href="@/services/residential-roofing/roof-replacement/">roof replacement</a> is the easiest time to get the whole system right, because the deck and ridge are open and a continuous ridge vent can be cut in. If you&rsquo;re not sure where your attic stands, it&rsquo;s part of our <a href="@/{_["INSPECT"]}">free roof inspection</a>.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>International Code Council, International Residential Code, Section R806 (Roof Ventilation): <a href="https://iccsafe.org/wp-content/uploads/bcac/IRC-R806.pdf" rel="noopener">iccsafe.org</a></li>
<li>Building America Solution Center (PNNL / U.S. Department of Energy), Attic Air Sealing, Insulating and Ventilating for Ice Dam Prevention: <a href="https://basc.pnnl.gov/information/attic-air-sealing-insulating-and-ventilating-ice-dam-prevention" rel="noopener">basc.pnnl.gov</a></li>
</ul></div>
</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Attic Ventilation for Utah Homes: Intake, Exhaust, Ice Dams",
            "meta": "Attic ventilation for Utah homes: intake and exhaust vents, the 1/150 and 1/300 code ratios with a worked example, and how ventilation affects ice dams.",
            "body": body, "ogtype": "article", "og": "roof-vents-mountains",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18",
                        "image": U + "assets/img/roof-vents-mountains.webp",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    A = _["A"]; trail = [_["HOME"], ("Blog", "blog/")]
    body = _["phero"](trail, "The Utah Roofing Pros Blog", "Roof care notes from our Cottonwood Heights office.", "Blog", buttons=False) + f'''
<section class="sec"><div class="wrap"><a class="guide reveal" href="@/{POST[1]}"><span class="arch">{img("roof-vents-mountains", "")}</span><span><span class="label dark">Roof care</span><b>{POST[0]}</b><em>Read it {A}</em></span></a></div></section>''' + _["cta"]()
    return {"path": "blog/", "canonical": canon("blog/"), "title": "The Utah Roofing Pros Blog | Roof Care Notes for Utah Homes",
            "meta": "The Utah Roofing Pros blog: roof care notes from our Cottonwood Heights office on attic ventilation, storm damage, repairs and keeping a Utah roof healthy.",
            "body": body, "schema": [crumbs_ld("blog/", trail)]}


def pages():
    return [index(), post()]
