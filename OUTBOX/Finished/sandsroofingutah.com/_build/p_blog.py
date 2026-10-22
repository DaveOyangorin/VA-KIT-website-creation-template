"""Blog for sandsroofingutah.com: the 6 existing posts (same URLs, the client's own text, real photos) plus one new post.

New post: "How Much Snow Can Your Roof Hold? A Utah Homeowner's Guide"
Main phrase: "how much snow can a roof hold" (informational). None of the client's posts covers it and no page targets it (snow
removal and heat cable are only lines on /services/); it links to services, the roof drains and cricket posts, and contact.
Facts and sources, checked 18 Oct 2026:
- FEMA P-957, Snow Load Safety Guide (January 2013): warning signs of an overstressed roof (sagging ceiling tiles or boards,
  ceiling boards falling out of the grid, sagging sprinkler lines and heads; popping, cracking and creaking noises; sagging roof
  members including plywood sheathing; bowing truss bottom chords or web members). If they appear, evacuate promptly and contact
  the local building authority or a qualified design professional. https://basc.pnnl.gov/library/fema-p-957-snow-load-safety-guide
  and summary at https://www.ehs.harvard.edu/node/7945
No snow weights in pounds are quoted (the figures could not be checked against the FEMA text itself). No prices.
"""
import html, re
from engine import crumbs_ld, faq_html, faq_ld, canon, img
from cfg import U, NAME, HERE, DOMAIN
from migrate import migrate

POST = ("How Much Snow Can Your Roof Hold? A Utah Homeowner’s Guide", "how-much-snow-can-a-roof-hold-utah/")
OLD = [("the_hidden_costs_of_delaying_mutli_family_roof_replacement_in_salt_lake_city_utah", "the-hidden-costs-of-delaying-mutli-family-roof-replacement-in-salt-lake-city-utah/", "The Hidden Costs of Delaying Multi-Family Roof Replacement in Salt Lake City, Utah", "2026-03-13", "multifamily-aerial"),
       ("roofing_solutions_for_condominiums_and_hoa_communities_in_utah", "roofing-solutions-for-condominiums-and-hoa-communities-in-utah/", "Roofing Solutions for Condominiums &amp; HOA Communities in Utah", "2026-02-26", "new-construction-aerial"),
       ("why_proper_roof_drains_matter_for_flat_roofing_systems", "why-proper-roof-drains-matter-for-flat-roofing-systems/", "Why Proper Roof Drains Matter for Flat Roofing Systems", "2026-01-02", "flat-roof-tpo-crew"),
       ("how_your_roof_protects_your_entire_home_and_why_it_matters_more_than_you_think", "how-your-roof-protects-your-entire-home-and-why-it-matters-more-than-you-think/", "How Your Roof Protects Your Entire Home &amp; Why It Matters More Than You Think", "2025-12-17", "drone-home-shingles"),
       ("what_is_a_roofing_cricket_why_are_they_needed", "what-is-a-roofing-cricket-why-are-they-needed/", "What is a Roofing Cricket? Why Are They Needed?", "2025-12-15", "crew-flat-roof-seams"),
       ("sands_roofing_provides_a_new_roof_for_utah_ukrainian_refugee_hub", "sands-roofing-provides-a-new-roof-for-utah-ukrainian-refugee-hub/", "S&amp;S Roofing Provides a New Roof for Utah Ukrainian Refugee Hub", "2025-06-03", "refugee-hub-after-1")]
GAL = {"sands_roofing_provides_a_new_roof_for_utah_ukrainian_refugee_hub": [("refugee-hub-before", "Before: the old roof"), ("refugee-hub-tear-off", "Stripped to bare wood"), ("refugee-hub-vent", "Vents going in"),
                                                                             ("refugee-hub-after-1", "After: the new roof"), ("refugee-hub-after-2", "After, from above"), ("refugee-hub-team", "At the hub")]}
MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
_ = {}


def setup(phero, cta, side, arrow, home, contact, tidy):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, CONTACT=contact, tidy=tidy)


def nice(d):
    y, m, dd = d.split("-"); return f"{MON[int(m) - 1]} {int(dd)}, {y}"


DROP = re.compile(r"35\+|over 35|guarantee|Call us today at|^contact$|Phone Number|Full Physical|Select Choice|Send Message|^Name \*", re.I)


def old_post(key, path, title, date, im):
    A = _["A"]; plain = html.unescape(title)
    body_txt = _["tidy"](migrate(HERE, key, DOMAIN, DROP, skip_heads=(plain, plain.upper())))
    trail = [_["HOME"], ("Blog", "blog/"), (title, path)]
    gal = GAL.get(key)
    galh = ('<div class="pgal">' + "".join(f'<figure>{img(n, c)}<figcaption>{c}</figcaption></figure>' for n, c in gal) + "</div>") if gal else f'<figure class="post-img">{img(im, plain)}</figure>'
    body = _["phero"](trail, title, None, "Blog &middot; " + nice(date), buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post"><p class="meta">By {NAME} &middot; {nice(date)}</p>
{body_txt}{galh}<p class="more"><a class="tlink" href="@/blog/">All posts {A}</a></p></article>{_["side"]()}</div></section>''' + _["cta"]()
    t = re.sub(r"<[^>]+>", " ", body_txt); t = re.sub(r"\s+", " ", html.unescape(t)).strip()
    meta = t[:158].rsplit(" ", 1)[0].rstrip(",;:") + "…" if len(t) > 158 else t
    ttl = plain if len(plain) > 44 else f"{plain} | S&S Roofing"
    if len(ttl) > 60: ttl = ttl[:60].rsplit(" ", 1)[0].rstrip(":,.-&")
    return {"path": path, "canonical": canon(path), "title": ttl, "meta": meta, "body": body, "ogtype": "article", "og": im,
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": plain, "datePublished": date, "image": U + f"assets/img/{im}.webp",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)}, crumbs_ld(path, trail)]}


SIGNS = [("Sagging ceilings", "Sagging ceiling tiles or boards, ceiling boards falling out of the grid, or sagging sprinkler lines and heads."),
         ("Noises", "Popping, cracking and creaking sounds from the roof structure."),
         ("Sagging roof members", "Visible sag in the roof framing or in the plywood sheathing."),
         ("Bowing trusses", "Bottom chords or web members of the trusses bowing or bending.")]
FAQ = [("How much snow can a house roof hold?", "It depends on two things: the snow load the roof was designed for, which the building code sets by location and elevation, and how heavy the snow actually is. A foot of light powder and a foot of wet, packed snow or ice are very different loads. Your city&rsquo;s building department can tell you the design load for your area."),
       ("What are the signs a roof has too much snow?", "FEMA lists sagging ceiling tiles or boards, ceiling boards falling out of the grid, sagging sprinkler lines, popping or creaking noises, sagging roof framing or sheathing, and bowing truss members. If you see them, get everyone out and call your building department or a structural professional."),
       ("Should I shovel my own roof?", "We don&rsquo;t recommend climbing onto a snowy roof. A long-handled roof rake used from the ground is safer for clearing the edges, and a roofing crew with the right equipment can handle the rest."),
       ("Does heat cable stop ice dams?", "Heat cable melts snow and ice along the roof edges, which helps prevent ice dams from forming there. It works best alongside good attic insulation and ventilation."),
       ("Do you remove snow from roofs?", "Yes. Snow removal is one of our services, along with heat cable installation and post-winter roof inspections.")]


def new_post():
    A = _["A"]; path = POST[1]
    trail = [_["HOME"], ("Blog", "blog/"), ("How much snow can a roof hold", path)]
    signs = "".join(f'<li><span class="n">{i + 1:02d}</span><div><b>{t}</b><p>{d}</p></div></li>' for i, (t, d) in enumerate(SIGNS))
    body = _["phero"](trail, POST[0], "Depth tells you less than you think. Here is what actually loads a roof in a Utah winter, the warning signs FEMA lists, and how to clear snow safely.", "Blog &middot; October 18, 2026", buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">
<p class="meta">By {NAME} &middot; October 18, 2026 &middot; 6 min read</p>
<p class="answer">How much snow a roof can hold depends on the snow load it was designed for and on how heavy the snow is, not just how deep. Design loads are set by the building code and rise with elevation, so a roof in Park City is built for far more than one in West Valley City. Wet, packed snow and ice weigh much more than fresh powder, and drifts pile extra weight in a few spots.</p>

<h2>Weight, not depth</h2>
<p>Two feet of snow on your roof can be a light load or a heavy one. Fresh, dry powder is mostly air. Snow that has settled, been rained on, or melted and refrozen holds far more water in the same depth, and ice is heavier still. That&rsquo;s why the riskiest moment is often not the big storm itself but the days after, when a warm spell or rain soaks the snow that&rsquo;s already up there and then it freezes again.</p>
<p>So when you look at your roof after a storm, ask two questions: how much is up there, and what has the weather done to it since?</p>

<h2>What your roof was built for</h2>
<p>Every roof is designed for a <b>snow load</b>, the weight it must carry safely. Building codes set that load by location, and in Utah it varies a lot with elevation. Homes in the mountain towns we serve, like Park City, Deer Valley, Summit Park, Heber City and Midway, are designed for much heavier snow than homes on the valley floor in Salt Lake City or West Valley City.</p>
<p>If you want to know your own number, your city or county building department can tell you the design snow load for your area. Older homes, additions and remodels may not all have been built to the same standard, and damaged or rotted framing carries less than it was built for. If you&rsquo;re unsure about your roof&rsquo;s structure, have it checked.</p>

<h2>Where snow piles up</h2>
<p>Snow rarely sits evenly. The heaviest loads tend to build in a few predictable places:</p>
<ul>
<li><b>Lower roofs next to taller walls.</b> Wind drifts snow off the upper roof and dumps it on the lower one.</li>
<li><b>Valleys,</b> where two roof slopes meet and snow slides together.</li>
<li><b>Behind chimneys and dormers,</b> where drifts collect on the uphill side. A <a href="@/what-is-a-roofing-cricket-why-are-they-needed/">roof cricket</a> helps here by diverting water and snow around the obstruction.</li>
<li><b>Below a roof step,</b> where snow sliding off a metal or steep upper roof lands all at once.</li>
<li><b>Flat roofs with blocked drains.</b> When meltwater can&rsquo;t leave, it ponds and refreezes. Our post on <a href="@/why-proper-roof-drains-matter-for-flat-roofing-systems/">why roof drains matter</a> explains how flat roofs are meant to shed water.</li>
</ul>
<figure class="post-img">{img("snowy-cabin-roof", "A snow-covered roof with a ladder against the eave")}<figcaption>Snow on a pitched roof. Drifts and slides concentrate weight in a few spots.</figcaption></figure>

<h2>The warning signs FEMA lists</h2>
<p>FEMA&rsquo;s Snow Load Safety Guide lists signs that a roof structure is overstressed by snow:</p>
<ol class="items">{signs}</ol>
<p>FEMA&rsquo;s advice if you see any of these is direct: evacuate the building promptly and contact your local building authority or a qualified design professional for a structural inspection. Don&rsquo;t go up on the roof to fix it yourself.</p>

<h2>Ice dams and heat cable</h2>
<p>Snow load and ice dams are separate problems that show up together. Ice dams form along the eaves when snow melts higher on the roof and refreezes at the cold edge, and the water backed up behind them can work its way under shingles. Heat cable along the roof edges melts paths through the snow and ice there, which helps prevent ice dams from forming. It&rsquo;s one of the <a href="@/services/">services we install</a>, and it works best on a home with good attic insulation and ventilation.</p>

<h2>Clearing snow safely</h2>
<p>If snow needs to come off, safety comes first:</p>
<ul>
<li><b>Stay off the roof.</b> A snowy or icy roof is one of the easiest places to fall. Use a long-handled roof rake from the ground to clear the edges.</li>
<li><b>Leave a thin layer.</b> Scraping down to the shingles can damage them. The goal is to take weight off, not to clean the roof.</li>
<li><b>Look up first.</b> Keep rakes and ladders well away from power lines, and watch for snow and ice sliding off.</li>
<li><b>Keep vents and exits clear.</b> Snow that slides off can block furnace and water-heater vents, doors and walkways.</li>
<li><b>Call a crew for the rest.</b> Large, steep or high roofs, flat commercial roofs and anything with signs of stress are a job for people with the right equipment.</li>
</ul>
<p>Snow removal is part of what we do in winter. We use specialized equipment and techniques to clear heavy buildup without damaging the roof.</p>

<h2>After the season</h2>
<p>When the snow is gone, take a look. Heavy loads, ice dams and sliding snow can leave behind lifted or cracked shingles, bent gutters, damaged flashing and leaks that only show up with the spring rain. A roof inspection in spring catches these early. If you see damage, <a href="@/{_["CONTACT"]}">request a free quote</a> and we&rsquo;ll take a look.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>FEMA P-957, Snow Load Safety Guide (January 2013), listed in the Building America Solution Center library: <a href="https://basc.pnnl.gov/library/fema-p-957-snow-load-safety-guide" rel="noopener">basc.pnnl.gov</a></li>
<li>Harvard Environmental Health &amp; Safety, roof snow load warning signs (based on FEMA guidance): <a href="https://www.ehs.harvard.edu/node/7945" rel="noopener">ehs.harvard.edu</a></li>
</ul></div>
</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "How Much Snow Can Your Roof Hold? A Utah Guide | S&S",
            "meta": "How much snow can your roof hold? Why weight matters more than depth, where drifts load a Utah roof, FEMA's warning signs, and how to clear snow safely.",
            "body": body, "ogtype": "article", "og": "snowy-cabin-roof",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18", "image": U + "assets/img/snowy-cabin-roof.webp",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index():
    A = _["A"]; trail = [_["HOME"], ("Blog", "blog/")]
    items = [(POST[1], POST[0], "2026-10-18", "snowy-cabin-roof")] + [(p, t, d, i) for k, p, t, d, i in OLD]
    cards = "".join(f'<a class="bcard reveal" href="@/{p}">{img(i, "")}<span class="meta">{nice(d)}</span><b>{t}</b><em>Read {A}</em></a>' for p, t, d, i in items)
    body = _["phero"](trail, "The S&amp;S Roofing Blog", "Roofing guides and project stories from the Salt Lake Valley.", "Blog", buttons=False) + f'''
<section class="sec"><div class="wrap"><div class="bgrid">{cards}</div></div></section>''' + _["cta"]()
    return {"path": "blog/", "canonical": canon("blog/"), "title": "Roofing Blog | S&S Roofing, Inc., West Valley City &amp; SLC",
            "meta": "The S&S Roofing blog: guides on roof snow loads, flat roof drains, roof crickets and HOA roofing, plus our new roof for the Utah Ukrainian refugee hub.",
            "body": body, "schema": [crumbs_ld("blog/", trail)]}


def pages():
    return [index(), new_post()] + [old_post(*o) for o in OLD]
