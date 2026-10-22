"""All pages for the skybridgeroofings.com redesign, on the client's current URLs plus the blog post and a 404.

Facts come only from the client's own site (18 Oct 2026) and the Google profile in the report: the ten services and the
system types on each page; free roof inspections and free estimates; drone-assisted inspections; residential and
commercial projects; "Emergency response available"; hours Mon-Fri 8-6; call or text (435) 659-4915; blueprints and RFPs
to cesar@skybridgeroofing.com; seamless gutters formed on site, 5-inch and 6-inch, stainless mesh gutter guards; the
mission statement, quoted.
Not used (see notes): the three home-page reviews (Alex M., Priya K., Diego R.; they read like theme placeholders), and every
unverified number or promise: "2-hour emergency response", "1-year workmanship guarantee", "triple-seal guarantee",
"decade+ of expertise", "1M+ sq ft protected", "zero recurrence rate", the lifespans, wind ratings and warranty names in the
comparison tables, "cooling costs down up to 30% / 40%", "Class A fire rating", "130 MPH", "50 yrs designed lifespan",
"insurance documentation support", and the 5-star / 25-review rating (shown once the client confirms it).
Report (17 Oct 2026): home targets "roofing company south salt lake"; every service page names South Salt Lake in the
title, H1 and first paragraph.
"""
import html
from build import (U, S, ARROW, PHONE, CHECK, CONTACT, BLOG_POST, SERVICES, IMG, img, video, phero, cta, faq_html, faq_ld,
                   crumbs_ld, quote_form, tblock)
from details import DETAILS
import p_blog

HOME = ("Home", "")


def checks(items):
    return '<ul class="checks">' + "".join(f"<li><i>{CHECK}</i><span>{x}</span></li>" for x in items) + "</ul>"


def svc_by(k):
    return next(s for s in SERVICES if s[0] == k)


# ---------- service pages ----------
SV = {
"roof-repair": dict(
    title="Roof Repair in South Salt Lake, UT | Sky Bridge Roofing",
    meta="Roof repair in South Salt Lake for leaks, damaged shingles and flashing. Sky Bridge Roofing finds the cause, fixes it and matches your roof. Free inspection.",
    h1="Roof Repair in South Salt Lake", label="Service 01 &middot; Repair", image="drone-standing-seam-close",
    alt="Close drone view of a dark metal roof and stone gables",
    lede="Leaks, damaged shingles, failed flashing and storm damage, traced to the cause and fixed so they stay fixed.",
    answer="Sky Bridge Roofing handles roof repair in South Salt Lake for homes and commercial buildings: leaks, missing or damaged shingles, loose or rusted flashing, and storm damage. We start by finding where the water is really getting in, because the stain on the ceiling is rarely right under the problem, then repair it with materials that match what is already on your roof.",
    sections=[("What a repair visit covers", """<p>A leak is usually a symptom. Water runs along the deck, the rafters or the top of the insulation before it shows up indoors, so the first job is to trace it back. We look at the places roofs most often fail: flashing at walls, chimneys and skylights; pipe boots and vents; valleys; the eaves; and any shingles or panels that have lifted, cracked or blown off.</p>"""
                                + checks(["Leaks traced from the inside stain back to the entry point", "Damaged or missing shingles replaced and sealed", "Step and counter flashing reset or replaced at walls and chimneys", "Pipe boots, vents and penetrations resealed", "Metal panels and seams re-secured", "Storm damage made safe first, then repaired"])),
              ("Matching what is already there", "<p>A repair should not look like a patch. We source shingles and metal that blend with your existing roof as closely as the product line allows, so the repair protects the house without leaving a different-colored square on the front slope.</p>"),
              ("Repair or replace?", f"""<p>Not every roof needs replacing. If the damage is local and the rest of the roof is sound, a repair is the right call and we will tell you so. When the problems are spread across the roof, the decking is soft, or the same areas keep failing, putting money into repairs stops making sense. In that case we will walk you through <a href="@/pages/roof-raplecement/">roof replacement</a> and show you why.</p>
<p>If you are not sure which one you need, start with a <a href="@/pages/roof-inspection/">free roof inspection</a>.</p>"""),
              ("When it can&rsquo;t wait", f"<p>If water is coming in now, call or text {S['phone']}. Emergency response is available, and the first step is always to stop more water getting in and protect the inside of the house.</p>")],
    faqs=[("What causes roof leaks?", "Most leaks start at a transition: flashing at a wall, chimney or skylight, a cracked pipe boot, a valley, or the eaves. Missing or lifted shingles, loose metal fasteners and clogged gutters that back water up under the roof edge are the other common causes."),
          ("Can a handyman fix a roof leak?", "A handyman can seal an obvious gap, but leaks rarely show up where they start. Without tracing the water path, a patch often moves the leak instead of stopping it. A roofer also knows how flashing and underlayment are meant to overlap, which is what keeps water out."),
          ("Do you repair metal roofs too?", "Yes. We repair both shingle and metal roofs, including resealing seams and penetrations and replacing damaged panels."),
          ("How do I get a repair started?", f"Call or text {S['phone']} or send the estimate form with a short description and, if you can, a photo. Inspections and estimates are free.")],
    related=["inspection", "replacement", "shingles"]),

"replacement": dict(
    title="Roof Replacement in South Salt Lake | Sky Bridge Roofing",
    meta="Roof replacement in South Salt Lake: full tear-off, deck check and a new shingle or metal roof installed as one system. Free estimates from Sky Bridge Roofing.",
    h1="Roof Replacement in South Salt Lake", label="Service 02 &middot; Replacement", image="drone-metal-roof-new-build",
    alt="Drone view of a new build with dark standing-seam metal roofs",
    lede="When a roof is past repair, we take it down to the deck and build a new one, every layer in the right order.",
    answer="Sky Bridge Roofing replaces roofs in South Salt Lake for homeowners and property owners. A replacement means tearing off the old roof, checking and repairing the deck, and installing a new system from the underlayment up: shingles, standing seam metal or metal shingles, with new flashing and edge metal.",
    sections=[("How a replacement goes", """<ol class="steps"><li><b>Inspection and estimate.</b> We look at the roof, the deck where we can, the attic and the gutters, and give you a written estimate.</li>
<li><b>Tear-off.</b> The old roofing comes off down to the deck, so nothing is hidden under the new roof.</li>
<li><b>Deck repair.</b> Soft or damaged decking is replaced before anything goes on top of it.</li>
<li><b>New layers.</b> Underlayment, flashing at every wall and penetration, edge metal, then the new roof covering.</li>
<li><b>Clean-up and final walk.</b> Nails and debris picked up, and a final look at the finished roof with you.</li></ol>"""),
              ("Choosing the new roof", f"""<p>The three systems we install most for replacements:</p>
<div class="opt3"><div><b>Architectural shingles</b><p>Layered asphalt shingles with a dimensional look. The most common choice for homes. <a href="@/pages/shingles/">Shingle roofing</a></p></div>
<div><b>Standing seam metal</b><p>Long panels with raised seams and concealed fasteners. A clean modern line. <a href="@/pages/metal-roofing/">Metal roofing</a></p></div>
<div><b>Metal shingles</b><p>Metal formed to look like slate, shake or tile.</p></div></div>
<p>Flat or low-slope sections get a membrane instead: <a href="@/pages/tpo/">TPO</a> or <a href="@/pages/epdm/">EPDM</a>.</p>"""),
              ("Replacement or new installation?", "<p>A replacement takes off a roof that is already there. New roofs on new builds and additions follow the same layer-by-layer approach without the tear-off; the metal roof in the photos on this page is a new build we roofed.</p>"),
              ("Permits", f"""<p>South Salt Lake requires a building permit for any reroof, and permitted work is inspected. We cover what that means for you in our guide: <a href="@/{BLOG_POST[1]}">{BLOG_POST[0]}</a></p>""")],
    faqs=[("How do I know I need a new roof and not a repair?", "Damage spread across the roof, soft decking, granule loss across many shingles, or repeated leaks in different places all point to replacement. One damaged area on an otherwise sound roof usually means a repair. A free inspection will tell you which."),
          ("Can a new roof go over the old one?", "Sometimes a second layer is allowed, but not over two existing layers, and not over a roof that is wet or deteriorated. We usually recommend a full tear-off, because it is the only way to see and fix the deck."),
          ("Do I need a permit?", "Yes. South Salt Lake requires a building permit for any reroof, and all permitted work is inspected."),
          ("What does a new roof cost?", "It depends on the roof size, pitch, the number of layers coming off, deck repairs and the system you choose. We give a written estimate after a free inspection.")],
    related=["metal", "shingles", "inspection"]),

"metal": dict(
    title="Metal Roofing in South Salt Lake, UT | Sky Bridge Roofing",
    meta="Metal roofing in South Salt Lake: standing seam, corrugated panels and metal shingles, installed and repaired by Sky Bridge Roofing. Call for a free estimate.",
    h1="Metal Roofing in South Salt Lake", label="Service 03 &middot; Metal", image="drone-standing-seam-gables",
    alt="Drone view of standing-seam metal roofs and stone gables on a new home",
    lede="Standing seam, corrugated panels and metal shingles, installed and repaired.",
    answer="Sky Bridge Roofing installs and repairs metal roofing in South Salt Lake for homes, shops and commercial buildings. We work with three kinds of metal roof: standing seam panels, corrugated panels and metal shingles, and we can repair seams, fasteners and damaged panels on metal roofs that are already in place.",
    sections=[("Three kinds of metal roof", """<div class="opt3"><div><b>Standing seam</b><p>Panels run from ridge to eave and lock together at raised seams, with the fasteners hidden under the seam on clips. The look in the drone photos on this page.</p></div>
<div><b>Corrugated metal</b><p>Ribbed panels fastened through the face. A simpler, classic profile common on shops, barns and outbuildings.</p></div>
<div><b>Metal shingles</b><p>Interlocking metal pieces shaped like slate, wood shake or tile, for a traditional look in metal.</p></div></div>"""),
              ("Why people choose metal", "<p>Metal sheds snow and rain well, does not rot, and in a light or reflective finish it helps keep summer heat out of the attic. It is also lighter than tile. On the other side of the ledger, it costs more up front than asphalt shingles, and it has to be installed with room for the panels to expand and contract.</p>"),
              ("How we install it", checks(["Deck and framing checked before the panels go on", "High-temperature underlayment under the metal", "Panels anchored with clips or fasteners for the profile", "Trim, flashing and closures at every edge, wall and penetration"])),
              ("Recent work", "<p>The photos on this page are from our own drone footage of a new build we roofed in dark standing seam metal, including the main house, the garage and an outbuilding.</p>")],
    faqs=[("Is metal roofing loud in the rain?", "Over a solid deck with underlayment, as on a house, rain noise is close to that of other roofs. The loud metal roofs people remember are usually panels over open framing on barns."),
          ("Can you put metal over shingles?", "In some cases, but we usually remove the old roof so the deck can be checked and the panels sit flat. We will tell you what your roof allows."),
          ("Do you repair metal roofs?", "Yes: loose fasteners, failed seams and sealant, leaking penetrations and damaged panels."),
          ("Standing seam or corrugated?", "Standing seam has concealed fasteners and a cleaner look; corrugated is simpler and costs less. We can show you both.")],
    related=["replacement", "walls", "coatings"]),

"inspection": dict(
    title="Roof Inspection in South Salt Lake | Sky Bridge Roofing",
    meta="Free roof inspection in South Salt Lake. Sky Bridge Roofing checks shingles, metal, flashing, gutters and penetrations, with drone-assisted inspections too.",
    h1="Roof Inspection in South Salt Lake", label="Service 04 &middot; Inspection", image="drone-standing-seam-overview",
    alt="Drone view looking down on a home with a metal roof and stone walls",
    lede="A free inspection that finds the small problems before they turn into leaks and repairs.",
    answer="Sky Bridge Roofing offers free roof inspections in South Salt Lake. We check the roof covering, flashing, penetrations, gutters and the signs of trouble inside, so homeowners and property managers can fix small problems early instead of paying for bigger repairs later. Drone-assisted inspections are available for roofs that are steep, large or hard to walk.",
    sections=[("What we look at", checks(["Shingles: lifting, cracking, missing pieces and granule loss", "Metal: loose fasteners, seams, sealant and rust", "Membranes: seams, punctures and ponding water", "Flashing at walls, chimneys, skylights and valleys", "Pipe boots, vents and other penetrations", "Gutters, downspouts and the roof edge", "Inside: stains, damp insulation or daylight in the attic"])),
              ("Drone-assisted inspection", "<p>On steep, tall or fragile roofs, a drone gets a close look without anyone walking on the surface, and gives you photos of what we found. The roof photos on this site come from our own drone footage.</p>"),
              ("When to get one", "<p>After a hail or wind storm, before buying or selling a home, when you notice a stain or a drip, when a roof is getting old, or simply once a year as a check-up. Catching a lifted shingle or a cracked boot early is far cheaper than drying out a ceiling.</p>"),
              ("What you get", f"<p>A plain answer: what we found, photos, and whether it needs a <a href=\"@/pages/roof-repair/\">repair</a>, a <a href=\"@/pages/roof-raplecement/\">replacement</a>, or nothing at all yet.</p>")],
    faqs=[("Is the roof inspection really free?", "Yes. Our roof inspections and estimates are free."),
          ("How long does an inspection take?", "It depends on the size and access of the roof. We will give you a time window when we schedule it."),
          ("Do you inspect commercial roofs?", "Yes, including flat and low-slope roofs with TPO or EPDM membranes."),
          ("What happens if you find a problem?", "We show you what we found, explain your options and give you a written estimate. There is no obligation.")],
    related=["roof-repair", "replacement", "gutters"]),

"shingles": dict(
    title="Shingle Roofing in South Salt Lake, UT | Sky Bridge Roofing",
    meta="Asphalt and architectural shingle roofing in South Salt Lake. Sky Bridge Roofing installs, replaces and repairs shingle roofs on homes. Free estimates.",
    h1="Shingle Roofing in South Salt Lake", label="Service 05 &middot; Shingles", image="drone-metal-roof-barn",
    alt="Drone view of a construction site with new roofs on a home and garage",
    lede="Asphalt and architectural shingles, installed course by course for protection and curb appeal.",
    answer="Sky Bridge Roofing installs asphalt and architectural shingle roofs in South Salt Lake, along with shingle repairs and full replacements. Shingles are the most common roof on homes here: they suit almost any style, come in many colors and cost less than metal.",
    sections=[("Three-tab or architectural?", """<div class="opt3 two"><div><b>Three-tab asphalt</b><p>A single flat layer with a uniform look. The simplest and most budget-friendly shingle.</p></div>
<div><b>Architectural (dimensional)</b><p>Two or more layers laminated together for a thicker shingle and a shadowed, textured look. The usual choice for replacements today.</p></div></div>"""),
              ("The parts you don&rsquo;t see", "<p>A shingle roof is more than shingles. Underneath are the deck, underlayment, ice and water protection along the eaves and valleys, starter strip, drip edge and flashing at every wall and penetration, with ridge vents or other ventilation for the attic. Every piece has to overlap the right way for water to run off instead of in.</p>"),
              ("How we install it", checks(["Old roof removed and deck checked", "Underlayment and edge metal", "Flashing at walls, chimneys and penetrations", "Shingles placed and nailed course by course", "Ridge cap and ventilation finished", "Site cleaned and nails picked up"])),
              ("Repairs", f"<p>Wind-lifted, cracked or missing shingles can usually be repaired. See <a href=\"@/pages/roof-repair/\">roof repair</a>.</p>")],
    faqs=[("How long does a shingle roof last?", "It depends on the shingle, the ventilation and the weather it sees. We can tell you more about the specific shingle you are considering."),
          ("Can you match my existing shingles for a repair?", "We match as closely as the product line allows, so the repair blends in."),
          ("Do shingles work on low-slope roofs?", "Shingles need enough slope to shed water. Flat and very low-slope areas get a membrane like TPO or EPDM instead."),
          ("Do I need a permit to reshingle?", "Yes, South Salt Lake requires a building permit for any reroof.")],
    related=["replacement", "roof-repair", "inspection"]),

"tpo": dict(
    title="TPO Roofing in South Salt Lake, UT | Sky Bridge Roofing",
    meta="TPO roofing in South Salt Lake for flat and commercial roofs: white single-ply membrane with heat-welded seams, installed by Sky Bridge Roofing. Free estimate.",
    h1="TPO Roofing in South Salt Lake", label="Service 06 &middot; TPO", image="ballasted-low-slope-roof",
    alt="Low-slope roof with gravel ballast and a raised metal roof section",
    lede="White single-ply membrane with heat-welded seams, for flat and low-slope roofs.",
    answer="Sky Bridge Roofing installs TPO roofing in South Salt Lake on flat and low-slope roofs, mostly on commercial buildings but also on flat sections of homes. TPO is a single-ply membrane, usually white, whose seams are welded together with hot air so the sheets become one continuous surface.",
    sections=[("What TPO is", "<p>TPO (thermoplastic polyolefin) is a flexible sheet that softens with heat. That is what makes it useful: the overlapping edges of two sheets are heated and pressed together so they fuse, instead of being glued. A white TPO surface also reflects sunlight, which helps keep heat out of the building in summer.</p>"),
              ("How it is built up", checks(["Deck checked and repaired", "Insulation boards", "Cover board where the system calls for it", "TPO membrane, mechanically fastened or adhered", "Heat-welded seams and detailed flashing at curbs, walls and drains"])),
              ("TPO or EPDM?", f"<p>Both are single-ply membranes for flat roofs. TPO is welded and usually white; <a href=\"@/pages/epdm/\">EPDM</a> is rubber, usually black, with taped or glued seams. The right one depends on the building, the roof traffic and the budget. We can quote both.</p>"),
              ("Commercial roofs", f"<p>Most of our TPO work is on commercial buildings. For planned projects, send blueprints and RFPs to <a href=\"mailto:{S['email']}\">{S['email']}</a>.</p>")],
    faqs=[("Why are TPO seams welded?", "Because TPO melts with heat, the seams can be fused into one piece of membrane, which is stronger than a glued joint."),
          ("Can TPO go on a home?", "Yes, on flat or very low-slope sections such as porches, additions and modern flat roofs."),
          ("Can TPO be repaired?", "Yes. Punctures and failed seams can be patched and re-welded."),
          ("Do you work from plans?", f"Yes. Send blueprints and RFPs to {S['email']}.")],
    related=["epdm", "coatings", "inspection"]),

"epdm": dict(
    title="EPDM Roofing in South Salt Lake, UT | Sky Bridge Roofing",
    meta="EPDM rubber roofing in South Salt Lake for flat and low-slope roofs. Sky Bridge Roofing installs and repairs EPDM membranes on homes and commercial buildings.",
    h1="EPDM Roofing in South Salt Lake", label="Service 07 &middot; EPDM", image="ballasted-low-slope-roof",
    alt="Low-slope roof with gravel ballast beside a metal-roofed section",
    lede="Synthetic rubber membrane for flat and low-slope roofs, installed and repaired.",
    answer="Sky Bridge Roofing installs and repairs EPDM roofing in South Salt Lake. EPDM is a synthetic rubber membrane for flat and low-slope roofs on commercial buildings and homes. It comes in large sheets, so a roof has fewer seams, and the seams it does have are bonded with tape or adhesive.",
    sections=[("What EPDM is", "<p>EPDM (ethylene propylene diene monomer) is a rubber roofing sheet, usually black. Unlike TPO it does not melt, so the seams are joined with seam tape or adhesive rather than heat. It stays flexible in cold weather and is a long-standing choice for low-slope roofs.</p>"),
              ("How it is installed", checks(["Deck checked and repaired", "Insulation boards", "Membrane fully adhered, mechanically fastened or ballasted", "Seams bonded with tape or adhesive", "Flashing at curbs, walls, drains and penetrations"])),
              ("EPDM or TPO?", f"<p>EPDM is rubber, usually black, with bonded seams; <a href=\"@/pages/tpo/\">TPO</a> is white with welded seams. We will recommend the one that fits the building.</p>"),
              ("Repairs and coatings", f"<p>Older EPDM roofs can often be repaired, or restored with a <a href=\"@/pages/roof-coatings/\">roof coating</a> instead of being replaced.</p>")],
    faqs=[("What is a ballasted roof?", "A ballasted roof holds the membrane down with the weight of stone or pavers instead of fasteners or glue, like the gravel roof in the photo on this page."),
          ("Can EPDM be repaired?", "Yes. Splits, punctures and loose seams can be patched with compatible EPDM materials."),
          ("Is EPDM only black?", "Black is most common; white EPDM is also made."),
          ("Can you coat an old EPDM roof?", "Often, yes, if the membrane is still sound. We check it first.")],
    related=["tpo", "coatings", "roof-repair"]),

"coatings": dict(
    title="Roof Coatings in South Salt Lake, UT | Sky Bridge Roofing",
    meta="Silicone roof coatings in South Salt Lake. Sky Bridge Roofing applies seamless coatings over sound flat and low-slope roofs to add a protective layer.",
    h1="Roof Coatings in South Salt Lake", label="Service 08 &middot; Coatings", image="drone-metal-roof-barn",
    alt="Drone view of roofs on a construction site",
    lede="A seamless silicone layer over a sound roof, to stop leaks and add years before a replacement.",
    answer="Sky Bridge Roofing applies roof coatings in South Salt Lake, mainly silicone coatings on flat and low-slope commercial roofs. A coating is rolled or sprayed over the existing roof to form one seamless layer that keeps water out and reflects sunlight, often adding years of life to a roof that is worn but still sound.",
    sections=[("When a coating makes sense", "<p>A coating is a restoration, not a replacement. It works on a roof whose deck and insulation are dry and solid but whose surface is aging: worn membranes, seams starting to open, small leaks. If the roof underneath is wet or failing, a coating will not fix that; the roof needs to be repaired or replaced first.</p>"),
              ("How we apply it", checks(["Inspection, including checking for wet insulation", "Repairs to seams, flashing and damaged areas", "Cleaning and surface preparation", "Primer where the surface needs it", "Silicone coating applied in a continuous layer, thicker at seams and details"])),
              ("Why silicone", "<p>Silicone forms a seamless, monolithic surface and handles standing water and UV well. A bright white coating also reflects the sun, which helps keep the building cooler in summer.</p>"),
              ("What it goes over", f"<p>Coatings are commonly applied over <a href=\"@/pages/epdm/\">EPDM</a>, <a href=\"@/pages/tpo/\">TPO</a>, metal and other low-slope roofs. We will tell you whether yours is a good candidate.</p>")],
    faqs=[("Will a coating stop my roof leaking?", "If the leaks come from worn seams or surface wear on an otherwise sound roof, yes. Leaks from wet insulation or failed decking need repair first."),
          ("Can you coat a shingle roof?", "Coatings are mainly for flat, low-slope and metal roofs. Shingle roofs are usually repaired or replaced instead."),
          ("Does a coating replace a new roof?", "No. It extends the life of a roof that is still sound. A roof past that point needs replacing."),
          ("How do I know if my roof qualifies?", "Book a free inspection and we will check it.")],
    related=["tpo", "epdm", "metal"]),

"gutters": dict(
    title="Gutter Installation in South Salt Lake | Sky Bridge Roofing",
    meta="Seamless gutter installation in South Salt Lake: 5-inch and 6-inch gutters formed on site, downspouts and gutter guards. Free estimate from Sky Bridge Roofing.",
    h1="Gutter Installation in South Salt Lake", label="Service 09 &middot; Gutters", image="soffit-and-seamless-gutter",
    alt="Looking up at a soffit and seamless gutter against a blue sky",
    lede="Seamless gutters formed on site, sized for the roof, with downspouts that move water away from the house.",
    answer="Sky Bridge Roofing installs seamless gutters in South Salt Lake. We form the gutter on site from a continuous aluminum coil, so each run is one piece without leak-prone joints, then hang it, set the pitch and add downspouts that send water away from your foundation.",
    sections=[("Gutter options", """<div class="opt3"><div><b>5-inch seamless</b><p>The standard size for most homes.</p></div>
<div><b>6-inch seamless</b><p>More capacity for large or steep roofs and long runs, with oversized downspouts.</p></div>
<div><b>Gutter guards</b><p>Stainless steel mesh that keeps leaves and debris out of the gutter.</p></div></div>"""),
              ("Why gutters matter", "<p>A roof sheds a lot of water. Without working gutters it pours off the edge, splashes the siding, wears away the soil and soaks the ground beside the foundation. Overflowing or clogged gutters can also back water up under the roof edge.</p>"),
              ("How we install them", checks(["Measure runs and plan downspout locations", "Form seamless gutter on site", "Hang with internal hangers and set the pitch", "Seal the corners and end caps", "Downspouts aimed away from the foundation"])),
              ("Gutters with a new roof", f"<p>If you are replacing your roof, it is a good time to replace old gutters too. See <a href=\"@/pages/roof-raplecement/\">roof replacement</a>.</p>")],
    faqs=[("What does seamless mean?", "Each straight run is one continuous piece formed on site, so there are no joints along the length to leak. Only the corners and downspouts are joined."),
          ("5-inch or 6-inch gutters?", "Five-inch suits most homes; six-inch is for bigger or steeper roofs that send more water to the edge."),
          ("Do gutter guards work?", "Mesh guards keep leaves and debris out, which means far less cleaning. They still need an occasional check."),
          ("Do you install gutters on commercial buildings?", "Yes. Ask us for an estimate.")],
    related=["shingles", "replacement", "inspection"]),

"walls": dict(
    title="Metal Wall Panels in South Salt Lake | Sky Bridge Roofing",
    meta="Architectural metal wall panels and cladding in South Salt Lake. Sky Bridge Roofing installs exterior wall systems for commercial and modern residential builds.",
    h1="Metal Wall Panels in South Salt Lake", label="Service 10 &middot; Wall panels", image="metal-wall-panels-commercial-entry",
    alt="Dark metal wall panels around a glass entry on a new building",
    lede="Architectural wall panels and cladding for modern commercial and residential buildings.",
    answer="Sky Bridge Roofing installs architectural metal wall panels in South Salt Lake. These exterior cladding systems give commercial and modern residential buildings a clean, durable face, like the dark panels around the entry in the photo on this page, one of our own jobs.",
    sections=[("What a wall panel system is", "<p>Metal wall panels hang on the outside of the building over a weather barrier, attached to girts or clips. The panels are the visible finish; behind them, the barrier and the flashing at windows, doors and corners keep water out of the wall.</p>"),
              ("Where they are used", checks(["Commercial entries and storefronts", "Offices, shops and warehouses", "Modern homes and accent walls", "Additions that need to match a metal roof"])),
              ("How we install them", checks(["Weather barrier over the sheathing", "Girts or clips set plumb and level", "Panels hung with consistent reveals", "Trim and flashing at openings, corners and the base"])),
              ("Roof and walls together", f"<p>Because we also install <a href=\"@/pages/metal-roofing/\">metal roofs</a>, we can roof and clad the same building and detail the joint between them.</p>")],
    faqs=[("Are wall panels only for commercial buildings?", "No. They are common on modern homes and accent walls too."),
          ("Can wall panels match a metal roof?", "Yes, panels and roofing can be ordered in matching colors."),
          ("Do you work from architectural drawings?", f"Yes. Send blueprints and RFPs to {S['email']}."),
          ("How do I get a quote?", f"Call or text {S['phone']} or use the estimate form.")],
    related=["metal", "tpo", "replacement"]),
}


def service_page(k):
    key, name, path, short = svc_by(k)
    d = SV[k]
    trail = [HOME, (name, path)]
    secs = "".join(f'<section class="sv-sec reveal"><h2>{h}</h2>{body}</section>' for h, body in d["sections"])
    rel = "".join(f'<li><a href="@/{svc_by(r)[2]}"><span class="mono">{svc_by(r)[1]}</span>{svc_by(r)[3]}</a></li>' for r in d["related"])
    body = phero(trail, d["h1"], d["lede"], d["label"], d["image"], d["alt"], detail=None) + f'''
<section class="sec"><div class="wrap sv-grid">
<article class="prose">
<p class="answer">{d["answer"]}</p>
{secs}
<section class="sv-sec reveal"><h2>Questions about {name.lower()}</h2>{faq_html(d["faqs"])}</section>
</article>
<aside class="sv-side">
<figure class="sheetfig">{DETAILS[k]()}<figcaption>Typical build-up, not to scale.</figcaption></figure>
<div class="side-card"><p class="label light">Free estimate</p><h3>Talk to Sky Bridge</h3><p>Call or text, or send a few details about the roof.</p><a class="side-phone" href="tel:{S["tel"]}">{S["phone"]}</a><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a><p class="mono small">{S["hours"]}</p></div>
<div class="side-rel"><p class="label">Related</p><ul>{rel}</ul></div>
</aside></div></section>
''' + cta()
    return {"path": path, "canonical": U + path.rstrip("/"), "title": d["title"], "meta": d["meta"], "body": body, "og": d["image"],
            "schema": [{"@type": "Service", "@id": U + path.rstrip("/") + "#service", "name": name, "serviceType": name, "provider": {"@id": U + "#business"},
                        "areaServed": {"@type": "City", "name": "South Salt Lake"}}, crumbs_ld(path, trail), faq_ld(d["faqs"])]}


# ---------- home ----------
HOME_FAQ = [("Where is Sky Bridge Roofing?", f"Our office is at {S['street']}, {S['city']}, {S['st']} {S['zip']}. We are open {S['hours'].replace('&ndash;', 'to')}, and emergency response is available."),
            ("Are your inspections and estimates free?", "Yes. Roof inspections and estimates are free."),
            ("Do you work on commercial roofs?", "Yes. Along with homes, we roof commercial buildings, including flat and low-slope roofs with TPO and EPDM membranes, roof coatings and metal wall panels."),
            ("Can I text you?", f"Yes. Call or text {S['phone']}.")]


def home():
    idx = "".join(f'''<a class="sys reveal" href="@/{p}"><span class="sys-n mono">{i + 1:02d}</span><span class="sys-d">{DETAILS[k]()}</span><b>{n}</b><small>{d}</small><em>View service {ARROW}</em></a>'''
                  for i, (k, n, p, d) in enumerate(SERVICES))
    body = f'''
<section class="hero">
<div class="hero-media">{video("drone-metal-roof-wide", "drone-metal-roof-new-build", cls="hv-wide")}{video("drone-metal-roof-tall", "drone-standing-seam-overview", cls="hv-tall")}</div>
<div class="grid-ov" aria-hidden="true"></div>
<div class="wrap hero-in">
<div class="hero-text">
<p class="label light">Sky Bridge Roofing &middot; South Salt Lake, Utah</p>
<h1>The roofing company South Salt Lake <span>plans before it builds.</span></h1>
<p class="lede">Sky Bridge Roofing is a roofing company in South Salt Lake for homes and commercial buildings: roof repair and replacement, metal and shingle roofs, TPO and EPDM membranes, coatings, gutters and wall panels. Inspections and estimates are free.</p>
<div class="btn-row"><a class="btn" href="@/{CONTACT}">Get a Free Estimate {ARROW}</a><a class="btn ghost light" href="tel:{S["tel"]}">{PHONE} Call or text {S["phone"]}</a></div>
</div>
{tblock([("Project", "New build, standing seam metal"), ("Footage", "Our drone, our crew"), ("Office", "South Salt Lake, UT"), ("Sheet", "R-01")])}
</div>
<p class="hero-cap mono">Live footage &middot; a new build we roofed in standing seam metal</p>
</section>

<section class="strip" aria-label="At a glance"><div class="wrap strip-in">
<div><b>Free</b><span>Roof inspections</span></div><div><b>Free</b><span>Estimates</span></div><div><b>10</b><span>Roofing and exterior systems</span></div><div><b>Mon&ndash;Fri</b><span>8 AM &ndash; 6 PM &middot; emergency response available</span></div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head reveal"><p class="label">Roofers in South Salt Lake</p><h2>Ten systems, <span>one detail sheet each.</span></h2>
<p class="lede">As roofing contractors in South Salt Lake, we work on steep roofs and flat ones, homes and commercial buildings. Pick the system you have, or the problem you&rsquo;re seeing.</p></div>
<div class="sys-grid">{idx}</div>
</div></section>

<section class="desk">
<div class="desk-media">{video("team-office", "office-roof-detail-drawings", cls="dv", label="The Sky Bridge Roofing team reviewing roof drawings in the office")}</div>
<div class="wrap desk-in">
<div class="desk-card reveal"><p class="label light">From the drawing board</p><h2>Every roof starts <span>at a desk.</span></h2>
<p>Before a crew goes up, the job is worked out: the drawings, the details at every wall and penetration, the materials, the order things go on. It is the same whether the roof is a porch or a commercial building.</p>
<p>Planning a commercial project? Send blueprints and formal RFPs to <a href="mailto:{S["email"]}">{S["email"]}</a>.</p>
<a class="tlink light" href="@/pages/about-us/">About Sky Bridge {ARROW}</a></div>
</div></section>

<section class="sec work"><div class="wrap">
<div class="head reveal"><p class="label">On the roof</p><h2>A new build in <span>standing seam metal.</span></h2><p class="lede">From our own drone footage: the main house, the garage and an outbuilding, all roofed in dark standing seam.</p></div>
<div class="work-grid">
<figure class="w1 reveal">{img("drone-standing-seam-overview", "Drone view looking down on a new home with dark standing-seam metal roofs and stone walls")}<figcaption><span class="mono">01</span>The whole site</figcaption></figure>
<figure class="w2 reveal">{img("drone-standing-seam-gables", "Standing-seam metal roof meeting stone gables")}<figcaption><span class="mono">02</span>Seams and gables</figcaption></figure>
<figure class="w3 reveal">{img("drone-standing-seam-close", "Close drone view of standing-seam panels and a stone chimney")}<figcaption><span class="mono">03</span>Panel detail</figcaption></figure>
<figure class="w4 reveal">{img("metal-wall-panels-commercial-entry", "Dark metal wall panels around a glass entry")}<figcaption><span class="mono">04</span>Wall panels, commercial entry</figcaption></figure>
</div></div></section>

<section class="sec dark"><div class="wrap split">
<div class="reveal"><p class="label light">How it works</p><h2>From first call <span>to final walk.</span></h2>
<ol class="flow">
<li><b>Call, text or send the form</b><p>Tell us where the roof is and what you&rsquo;re seeing. Residential, commercial or just a consultation.</p></li>
<li><b>Free inspection</b><p>We look at the roof, by foot or by drone, and show you what we found.</p></li>
<li><b>Written estimate</b><p>The work, the materials and the price, in writing.</p></li>
<li><b>The work, then a final walk</b><p>Done in the right order, cleaned up, and checked with you at the end.</p></li>
</ol></div>
<div class="reveal">{quote_form()}</div>
</div></section>

<section class="team-band"><div class="team-img">{img("sky-bridge-roofing-team", "The Sky Bridge Roofing team in front of the company trucks")}</div>
<div class="wrap"><div class="team-card reveal"><p class="label light">Our mission</p>
<blockquote>&ldquo;To deliver superior roofing solutions with unmatched craftsmanship, integrity, and professionalism.&rdquo;</blockquote>
<p class="mono">Sky Bridge Roofing &middot; South Salt Lake</p></div></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Before <span>you call.</span></h2>
<a class="guide" href="@/{BLOG_POST[1]}"><span class="mono">Guide</span><b>{BLOG_POST[0]}</b><em>Read the guide {ARROW}</em></a></div>
<div class="reveal">{faq_html(HOME_FAQ)}</div>
</div></section>
''' + cta()
    return {"path": "", "canonical": U, "title": "Roofing Company South Salt Lake, UT | Sky Bridge Roofing",
            "meta": "Sky Bridge Roofing is a roofing company in South Salt Lake for roof repair, replacement, metal, shingles, TPO, EPDM, coatings and gutters. Free estimates.",
            "body": body, "og": "drone-metal-roof-new-build",
            "schema": [{"@type": "BreadcrumbList", "@id": U + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": U}]}, faq_ld(HOME_FAQ)]}


def about():
    trail = [HOME, ("About Us", "pages/about-us/")]
    body = phero(trail, "About Sky Bridge Roofing, South Salt Lake", "A South Salt Lake roofing team that works the job out at the desk before it goes up on the roof.", "About us", "sky-bridge-crew-trucks", "Three Sky Bridge Roofing crew members in front of a company truck", sheet="A-01") + f'''
<section class="sec"><div class="wrap split">
<div class="reveal prose"><p class="answer">Sky Bridge Roofing is a roofing company based in South Salt Lake, Utah, working on homes and commercial buildings. We repair and replace roofs, install metal, shingle, TPO and EPDM systems, apply roof coatings, and install gutters and metal wall panels.</p>
<h2>Our mission</h2>
<blockquote class="pull">&ldquo;At Sky Bridge Roofing, our mission is to deliver superior roofing solutions with unmatched craftsmanship, integrity, and professionalism.&rdquo;</blockquote>
<p>In practice that means three things we care about: quality materials and careful work, honest advice about whether a roof needs repairing or replacing, and the same standard on a small repair as on a commercial roof.</p>
<h2>How we work</h2>
<p>A roof is a system: deck, underlayment, flashing, the covering and the details where they meet walls, chimneys and drains. We plan those details before the crew goes up, and on commercial projects we work from the drawings. Send blueprints and RFPs to <a href="mailto:{S["email"]}">{S["email"]}</a>.</p></div>
<figure class="reveal frame-img">{img("office-whiteboard-detail", "A Sky Bridge team member sketching a roof detail on a whiteboard")}<figcaption>Working out a detail in the office.</figcaption></figure>
</div></section>
<section class="desk">
<div class="desk-media">{video("team-office", "office-project-review", cls="dv", label="The Sky Bridge Roofing team at work in the office")}</div>
<div class="wrap desk-in"><div class="desk-card reveal"><p class="label light">The office</p><h2>Plans, drawings <span>and a phone that gets answered.</span></h2><p>Call or text {S["phone"]}, {S["hours"]}. Emergency response is available.</p><a class="tlink light" href="@/{CONTACT}">Contact us {ARROW}</a></div></div></section>
<section class="team-band"><div class="team-img">{img("sky-bridge-roofing-team", "The Sky Bridge Roofing team")}</div>
<div class="wrap"><div class="team-card reveal"><p class="label light">The team</p><blockquote>Quality. Trust. Excellence.</blockquote><p class="mono">The three values Sky Bridge builds on</p></div></div></section>
''' + cta()
    return {"path": "pages/about-us/", "canonical": U + "pages/about-us", "title": "About Sky Bridge Roofing | Roofers in South Salt Lake, UT",
            "meta": "Meet Sky Bridge Roofing, a South Salt Lake roofing company for homes and commercial buildings. Our mission, how we plan every roof, and how to reach us.",
            "body": body, "og": "sky-bridge-roofing-team", "schema": [crumbs_ld("pages/about-us/", trail), {"@type": "AboutPage", "@id": U + "pages/about-us#page", "url": U + "pages/about-us", "about": {"@id": U + "#business"}}]}


def contact():
    trail = [HOME, ("Contact", CONTACT)]
    body = phero(trail, "Contact Sky Bridge Roofing in South Salt Lake", "Call, text or email. Inspections and estimates are free.", "Contact", None, sheet="C-01", buttons=False) + f'''
<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal">
<div class="channels">
<a class="ch" href="tel:{S["tel"]}"><span class="mono">Call</span><b>{S["phone"]}</b><small>Speak directly with a project manager</small></a>
<a class="ch" href="sms:{S["tel"]}"><span class="mono">Text</span><b>{S["phone"]}</b><small>Fast response by text</small></a>
<a class="ch" href="mailto:{S["email"]}"><span class="mono">Email</span><b>{S["email"]}</b><small>For blueprints and formal RFPs</small></a>
<div class="ch"><span class="mono">Office</span><b>{S["street"]}<br>{S["city"]}, {S["st"]} {S["zip"]}</b><small>{S["hours"]} &middot; Emergency response available</small></div>
</div>
<figure class="frame-img">{img("office-sky-bridge-door", "Sky Bridge Roofing logo on the office door")}</figure>
</div>
<div class="reveal">{quote_form("Request a free estimate")}</div>
</div></section>'''
    return {"path": CONTACT, "canonical": U + "pages/contact", "title": "Contact Sky Bridge Roofing | South Salt Lake Roofers",
            "meta": "Contact Sky Bridge Roofing in South Salt Lake: call or text (435) 659-4915, email blueprints and RFPs, or request a free roofing estimate online today.",
            "body": body, "schema": [crumbs_ld(CONTACT, trail), {"@type": "ContactPage", "@id": U + "pages/contact#page", "url": U + "pages/contact", "about": {"@id": U + "#business"}}]}


def notfound():
    body = phero([HOME, ("Page not found", "404.html")], "This page isn&rsquo;t on the plans.", "The link may be old. Try a service below, or call us.", "404", None, sheet="404") + f'''
<section class="sec"><div class="wrap"><div class="sys-grid small">{"".join(f'<a class="sys" href="@/{p}"><b>{n}</b><small>{d}</small></a>' for k, n, p, d in SERVICES)}</div></div></section>'''
    return {"path": "404.html", "title": "Page Not Found | Sky Bridge Roofing", "meta": "This page could not be found. Browse Sky Bridge Roofing services in South Salt Lake or call (435) 659-4915 for a free roof inspection and estimate.",
            "body": body, "robots": "noindex, follow", "sitemap": False}


def make_pages():
    pages = [home()] + [service_page(k) for k, *_ in SERVICES] + [about(), contact()] + p_blog.pages() + [notfound()]
    return pages
