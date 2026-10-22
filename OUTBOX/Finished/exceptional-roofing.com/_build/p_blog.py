"""Blog for exceptional-roofing.com: the blog index (the live one only held WordPress's "Hello world!") and one new post.
WordPress puts posts at the root (/hello-world/), so the new post does too.

New post: "Ice Dams on Utah Roofs: Why They Form and How to Stop Them"
Main phrase: "ice dams utah" (informational). No page on the site covers it; it links to roof repair, inspections, emergency
roofing, preventative maintenance and metal roofing without targeting their keywords.
Facts and sources, checked 19 Oct 2026:
- University of Minnesota Extension, "Dealing with and preventing ice dams":
  https://extension.umn.edu/garden-and-home/home-maintenance/caring-for-a-home/dealing-with-and-preventing-ice-dams
  ice dams form when heat from the house melts roof snow that refreezes at the colder eaves; warm air leaking into the attic is in
  many homes the main heat source; insulation and ventilation work together; seal air leaks first.
- Utah Residential Code 2021 (IRC as adopted in Utah), R905.1.2 Ice barriers, on UpCodes:
  https://up.codes/viewer/utah/irc-2021/chapter/9/roof-assemblies  - required where there is a history of ice forming along the
  eaves (Table R301.2); two cemented layers of underlayment or a self-adhering polymer-modified bitumen sheet; from the eave to at
  least 24 in. inside the exterior wall line; on 8:12 and steeper, also at least 36 in. measured along the slope.
No prices."""
import re
from engine import crumbs_ld, faq_html, faq_ld, canon
from cfg import U, NAME, PHONES

POST = ("Ice Dams on Utah Roofs: Why They Form and How to Stop Them", "ice-dams-utah-roofs/")
UMN = "https://extension.umn.edu/garden-and-home/home-maintenance/caring-for-a-home/dealing-with-and-preventing-ice-dams"
IRC = "https://up.codes/viewer/utah/irc-2021/chapter/9/roof-assemblies"
_ = {}


def setup(K, img):
    _.update(K=K, img=img)


FAQ = [("Are ice dams a roofing problem or an attic problem?", "Both. The dam forms on the roof, but the heat that melts the snow usually comes from the house: warm air leaking into the attic and too little insulation. The roof&rsquo;s job is to resist the water that backs up; the attic&rsquo;s job is to stop making it."),
       ("Does the code require an ice barrier in Utah?", "Where there is a history of ice forming along the eaves, the Utah Residential Code (R905.1.2) requires an ice barrier from the eave to at least 24 inches inside the exterior wall line, and at least 36 inches up the slope on roofs 8:12 and steeper."),
       ("Should I chip the ice off?", "No. Chipping or hammering at an ice dam damages shingles, flashing and gutters, and working on an icy roof is dangerous. Call a roofer if water is coming inside.")]


def new_post():
    K, img = _["K"], _["img"]
    A = K.ARROW
    body = f'''<p class="answer">An ice dam is a ridge of ice that forms along the bottom edge of a roof. Snow higher up melts, the water runs down to the colder eave, and it freezes again. As the ridge grows, meltwater pools behind it and can back up under the shingles, into the walls and through the ceiling.</p>
<p>Along the Wasatch Front and up in Park City and Heber, the conditions are right most winters: real snow on the roof, cold nights, and sunny days. We see the results every spring: stained ceilings, peeling paint at the top of exterior walls, and gutters pulled loose by ice. The good news is that ice dams are predictable, and most of the fix happens before the snow falls.</p>
<h2>Why ice dams form</h2>
<p>A roof covered in snow should stay cold enough that the snow sits there until the weather warms. Ice dams happen when part of the roof is warm and part is cold. The <a href="{UMN}" rel="noopener">University of Minnesota Extension</a> explains the pattern: heat from the house warms the upper roof, snow melts against the shingles, and the water refreezes when it reaches the eave, which hangs out past the warm walls and stays at outdoor temperature.</p>
<p>Where does the heat come from? Extension&rsquo;s guidance is that in many homes the biggest source is warm indoor air leaking into the attic through gaps around light fixtures, plumbing and wiring penetrations, attic hatches and chimneys. Thin or uneven insulation adds to it. Ventilation helps carry the heat away, but it works together with insulation and air sealing, not instead of them.</p>
<h2>Signs you have a problem</h2>
<ul><li>Thick ice along the eaves and in the gutters, often with icicles</li><li>Water stains or damp spots on ceilings near exterior walls</li><li>Peeling paint or stains at the top of exterior walls, inside or out</li><li>Bare patches on a snowy roof (a sign of heat escaping from below)</li><li>Gutters sagging or pulling away from the fascia</li></ul>
<h2>What the code requires at the eaves</h2>
<p>Because ice dams are common in cold, snowy places, the building code builds in protection. Under the <a href="{IRC}" rel="noopener">Utah Residential Code (R905.1.2)</a>, where there is a history of ice forming along the eaves and causing water to back up, roofs covered with asphalt shingles, metal shingles, wood shingles or shakes and similar materials need an <b>ice barrier</b>: either two layers of underlayment cemented together or a self-adhering polymer-modified bitumen sheet.</p>
<p>It runs from the lowest edge of the roof to at least 24 inches inside the exterior wall line of the house. On steep roofs, 8:12 and steeper, it also has to extend at least 36 inches measured along the slope from the eave. That covers the zone where meltwater backs up behind a dam.</p>
<p>An ice barrier doesn&rsquo;t stop ice dams from forming; it keeps the water that backs up behind them out of the house. That&rsquo;s why it matters most when a roof is replaced: it&rsquo;s the moment to make sure the eaves are protected properly, especially on older homes that were roofed before the requirement or with less coverage than the overhang needs.</p>
<h2>How to stop ice dams</h2>
<h3>1. Keep the heat out of the attic</h3>
<p>Air sealing comes first: closing the gaps where warm air leaks from the house into the attic. Then bring the insulation up to a consistent depth, without blocking the soffit vents at the eaves. This is the part that keeps the roof deck cold and evenly frozen, which is what actually prevents the melt.</p>
<h3>2. Let the attic breathe</h3>
<p>Intake vents at the soffits and exhaust vents near the ridge let cold outside air flow under the roof deck. Blocked soffits (often by insulation pushed too far) are a common problem we find on inspections.</p>
<h3>3. Protect the eaves when you re-roof</h3>
<p>When a roof is replaced, the ice barrier goes down first along the eaves and in the valleys, under the new roofing. On metal roofs, snow tends to slide rather than sit, which changes how ice builds up, and snow guards may be part of the plan above doors and walkways. We size the details to the roof, the pitch and the exposure.</p>
<h3>4. Deal with the snow safely</h3>
<p>A roof rake used from the ground can pull the first few feet of snow off the eaves after a big storm, which removes the snow that would feed a dam. Don&rsquo;t climb onto an icy roof, and don&rsquo;t chip at the ice with a hammer or shovel; it damages shingles, flashing and gutters.</p>
<h2>If water is already coming in</h2>
<p>Catch the water, move what you can, and call us. We can deal with the immediate leak (<a href="@/emergency-roofing/">emergency roofing</a>), then look at the roof and the eaves once the weather allows (<a href="@/roof-inspections/">roof inspection</a>). Often the right answer is a <a href="@/roof-repair/">repair</a> at the eaves plus attic work. If the roof is near the end of its life anyway, replacement with proper ice and water protection is the long-term fix. Regular <a href="@/preventative-maintenance/">maintenance</a> catches the problem areas before winter.</p>
<p>Seeing ice along your eaves this winter? Call or text {PHONES[0][1]} for a free estimate.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Sources: <a href="{UMN}" rel="noopener">University of Minnesota Extension, Dealing with and preventing ice dams</a>; <a href="{IRC}" rel="noopener">Utah Residential Code 2021, Chapter 9, R905.1.2 Ice barriers</a>.</p>'''
    trail = [K.HOME, ("Blog", "blog/"), ("Ice dams", POST[1])]
    pg = K.page(POST[1], "Ice dams", POST[0], f"By {NAME} &middot; October 19, 2026", "Blog &middot; Winter", "Ice Dams on Utah Roofs: Causes &amp; Prevention | Exceptional",
                "Why ice dams form on Utah roofs, the signs to watch for, what the Utah code requires at the eaves, and how to stop them, from attic air sealing to ice barriers.",
                body, image="winter-new-build", alt="New construction roof in the snow", crumbs=[("Blog", "blog/")], ogtype="article")
    pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    pg["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-19", "dateModified": "2026-10-19",
                                   "image": U + "assets/img/winter-new-build.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    pg["title"] = "Ice Dams on Utah Roofs: Causes &amp; Prevention | Exceptional"
    return pg


def index():
    K, img = _["K"], _["img"]
    card = f'<a class="post-card reveal" href="@/{POST[1]}">{img("winter-new-build", "")}<b>{POST[0]}</b><em>Read {K.ARROW}</em></a>'
    return K.page("blog/", "Blog", "Roofing Blog", "Guides for Utah homeowners and property managers.", "Blog", "Roofing Blog | Exceptional Roofing, Salt Lake City",
                  "Roofing guides from Exceptional Roofing in Salt Lake City: ice dams, materials, repair vs replacement and caring for a roof through Utah winters.",
                  f'<div class="posts one">{card}</div>')


def pages():
    return [index(), new_post()]
