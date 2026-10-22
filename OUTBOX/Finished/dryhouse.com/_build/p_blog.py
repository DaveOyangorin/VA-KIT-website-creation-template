"""Blog for dryhouse.com: the 4 existing K2 posts (same URLs, the client's own text and photos), the K2 listing URLs, and one new post.

New post: "Before You Backfill: A Foundation Checklist for Utah Builders"
Main phrase: "foundation backfill checklist" (informational, for builders). None of the client's posts covers it and no service page
targets it; it links to the waterproofing, damp proofing, drains, ties, honeycomb, cold joints and pipe penetration pages.
Facts and sources, checked 19 Oct 2026:
- Utah Residential Code 2021 (IRC 2021 as adopted in Utah), Chapter 4, on UpCodes:
  https://up.codes/viewer/utah/irc-2021/chapter/4/foundations
  R401.3: grade shall fall not fewer than 6 inches within the first 10 feet. R404.1.7: backfill not placed until the wall has
  sufficient strength and is anchored or braced (bracing not required for walls with less than 4 ft of unbalanced backfill).
  R405.1: gravel or crushed stone drains extend not less than 1 foot beyond the outside edge of the footing and 6 inches above the
  top of the footing, covered with an approved filter membrane; not required on well-drained (Group I) soils. R406.1: dampproofing
  from the higher of the top of the footing or 6 in. below the top of the basement floor, to finished grade. R406.2: waterproofing
  where a high water table or other severe soil-water conditions are known to exist.
- Everything else is the client's own text (ties, honeycomb, cold joints, pipe penetrations, mils, hydrostatic head, strip drain,
  downspouts 5-10 ft, Thermal Drain installed the same day). No prices.
"""
import html, re
from engine import crumbs_ld, faq_html, faq_ld, canon, img
from cfg import U, NAME

POST = ("Before You Backfill: A Foundation Checklist for Utah Builders", "blog/before-you-backfill-foundation-checklist/")
SRC = "https://up.codes/viewer/utah/irc-2021/chapter/4/foundations"
OLD = [("blog_item_20_the_house_that_she_built", "blog/item/20-the-house-that-she-built/", "The House That SHE Built", "2020-10-29", "Chris Douglas", "she-built-sign"),
       ("blog_item_19_salt_lake_home_builders_association_member_spot_5697ff", "blog/item/19-salt-lake-home-builders-association-member-spotlight-rocky-mountain-waterproofing/",
        "Salt Lake Home Builders Association &ndash; Member Spotlight &ndash; Rocky Mountain Waterproofing", "2020-06-18", "Sam Douglas", "chris-douglas"),
       ("blog_item_17_don_t_cut_corners_waterproof_your_home", "blog/item/17-don-t-cut-corners-waterproof-your-home/", "Don&rsquo;t Cut Corners &ndash; Waterproof Your Home", "2019-04-09", "Chris Douglas", "tie-patch-closeup"),
       ("blog_item_16_wjchamber_join", "blog/item/16-wjchamber-join/", "Rocky Mountain Waterproofing Joins the West Jordan Chamber of Commerce", "2018-02-05", "Chris Douglas", "libby-shop")]
MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
_ = {}
META = {"blog_item_20_the_house_that_she_built": ("The House That SHE Built | Rocky Mountain Waterproofing Blog", "The House That SHE Built, a home built entirely by women: Libby and Sarah did the Tuff-N-Dri waterproofing, window wells and strip drain footing drain."),
        "blog_item_19_salt_lake_home_builders_association_member_spot_5697ff": ("Salt Lake HBA Member Spotlight: Chris Douglas | RMWP Blog", "Chris Douglas of Rocky Mountain Waterproofing is on the Salt Lake Home Builders Association Membership Committee. Read the HBA member spotlight."),
        "blog_item_17_don_t_cut_corners_waterproof_your_home": ("Don't Cut Corners: Waterproof Your Home | Rocky Mountain", "Is your waterproofer cutting corners? Rocky Mountain Waterproofing breaks and patches ties, cleans footings and waterproofs foundations in West Jordan, Utah."),
        "blog_item_16_wjchamber_join": ("We Joined the West Jordan Chamber of Commerce | Rocky Mountain", "Rocky Mountain Waterproofing has joined the West Jordan Chamber of Commerce. Find our member listing and learn more about the chamber in West Jordan, Utah.")}


def setup(phero, cta, side, arrow, home, bid, tidy, mig):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, BID=bid, tidy=tidy, mig=mig)


def nice(d):
    y, m, dd = d.split("-"); return f"{MON[int(m) - 1]} {int(dd)}, {y}"


DROP = re.compile(r"^Written by|^Chris Douglas$|^Sam Douglas$|day, \d\d \w+ 20\d\d|Last modified|^Featured$|\.jpg|^The House That SHE Built$|leak free for over|one of the first companies|Spotlight Text", re.I)


def old_post(key, path, title, date, author, im):
    trail = [_["HOME"], ("Blog", "blog/"), (re.sub(r" &ndash;.*", "", title)[:40], path)]
    body_txt = _["mig"](key, skip=(html.unescape(title),), drop=DROP)
    body_txt = re.sub(r"<br>\s*<br>", "</p><p>", body_txt)
    if key.endswith("waterproof_your_home"):
        body_txt = ("<h2>Is your &ldquo;waterproofer&rdquo; cutting corners?</h2><ul><li>We break &amp; patch ties</li><li>We clean footings</li><li>We waterproof</li><li>And more!</li></ul>"
                    "<p>Ties left in the wall, dirt on the footing and a thin coat of damp proofing are where corners get cut, and where leaks start. Here&rsquo;s more on each:</p>"
                    '<ul><li><a href="@/services/leak-repair/ties/">Foundation ties</a></li><li><a href="@/services/belowgrade/damp-proof/">Damp proofing vs waterproofing</a></li><li><a href="@/services/belowgrade/waterproofing/">Foundation waterproofing</a></li></ul>')
    if key.endswith("she_built"):
        gal = [("libby-sarah-site", "Libby and Sarah on site"), ("she-built-sign", "Future home of The House That SHE Built"), ("crew-in-trench", "Prepping the wall"), ("trench-wasatch-truck", "The footing drain trench"),
               ("window-well-set", "Setting a window well"), ("window-well-fasten", "Fastening the window well"), ("libby-shop", "Libby in the shop"), ("foundation-waterproofed", "Waterproofing done, wells in")]
        body_txt = body_txt.replace("<p>Rocky Mountain Waterproofing applies Damp-Proofing", '<div class="pgal">' + "".join(f"<figure>{img(n, c)}<figcaption>{c}</figcaption></figure>" for n, c in gal) + "</div><p>Rocky Mountain Waterproofing applies Damp-Proofing", 1)
    if key.endswith("wjchamber_join"):
        body_txt = body_txt.replace('href="http://business.westjordanchamber', 'rel="noopener" href="http://business.westjordanchamber')
    t, m = META[key]
    plain = html.unescape(re.sub(r"<[^>]+>", "", title))
    body = _["phero"](trail, title, f"By {author} &middot; {nice(date)}", "Blog &middot; News", im, plain) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">{body_txt}</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": t, "meta": m, "body": body, "og": im, "ogtype": "article",
            "schema": [crumbs_ld(path, trail), {"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": plain, "datePublished": date, "image": U + f"assets/img/{im}.webp",
                       "author": {"@type": "Person", "name": author}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)}]}


FAQ = [("When can you backfill a new foundation wall?", "Under the Utah Residential Code (IRC R404.1.7), not until the wall has enough strength and is anchored to the floor above or braced so the backfill can&rsquo;t damage it. Walls holding back less than 4 feet of unbalanced fill don&rsquo;t need bracing."),
       ("Is damp proofing enough before backfill?", "It meets the code minimum for most basements (R406.1). Where a high water table or other severe soil-water conditions are known, the code calls for waterproofing instead (R406.2). For a basement you plan to finish, waterproofing is the better match either way."),
       ("Does every foundation need a footing drain?", "Most do. R405.1 requires drains around concrete or masonry foundations that retain earth and enclose space below grade, except on well-drained gravel and sand soils, or where a geotechnical report covering the lot says one isn&rsquo;t needed.")]


def new_post():
    path = POST[1]
    trail = [_["HOME"], ("Blog", "blog/"), ("Before you backfill", path)]
    A = _["A"]
    checklist = [("Wall braced or anchored", "R404.1.7"), ("Form ties broken, patched and sealed", "Ties"), ("Honeycomb grouted and patched", "Honeycomb"), ("Cold joints detailed", "Cold joints"),
                 ("Pipe penetrations sealed", "Pipes"), ("Coating matches the space", "R406"), ("Footing drain in and draining", "R405.1"), ("Drainage or protection board on", "Board"), ("Grade falls 6 in. in 10 ft", "R401.3")]
    body_txt = f'''<p class="answer">A foundation backfill checklist is the list of things to finish while the outside of a basement wall is still open: ties, rock pockets, joints, pipes, the coating, the drain and the grade. Once the dirt goes back, every one of them gets harder, slower and more expensive to fix, and most of them can only be reached again with an excavator or by tearing out finished drywall.</p>
<p>We&rsquo;ve waterproofed Utah foundations since 1960, and nearly every leak we&rsquo;re called back to fix started as something that could have been handled in an hour before backfill. Here is the list we&rsquo;d want every builder to walk before the excavator comes back, with the Utah Residential Code sections (the 2021 IRC as adopted in Utah) that apply.</p>
<div class="checklist"><p class="label code">Pre-backfill walk &middot; 9 items</p><ol>{"".join(f"<li><span>{a}</span><small>{b}</small></li>" for a, b in checklist)}</ol></div>
<h2>1. The wall can take the load</h2>
<p>Backfill pushes sideways on a wall that was designed to be held at the top by the floor framing. The code is plain about it: backfill should not be placed against the wall until the wall has sufficient strength and has been anchored to the floor above, or braced well enough that the backfill can&rsquo;t damage it (R404.1.7). The exception is a wall holding back less than 4 feet of unbalanced fill. Backfilling a tall basement wall before the floor deck is on is how walls crack, bow or get knocked by a machine, and a structural crack is one of the hardest leaks to fix.</p>
<h2>2. Form ties are broken, patched and sealed</h2>
<p>Every poured wall is full of form ties, the metal pieces that held the forms while the concrete cured. The forms come off; the ties stay in the wall. They&rsquo;re normally snapped off and patched on the outside, but a tie that isn&rsquo;t treated properly is a straight path for water. Break them, patch them and coat over them before anything else goes on the wall. <a href="@/services/leak-repair/ties/">More on tie leaks</a>.</p>
<h2>3. Honeycomb is grouted and patched</h2>
<p>Honeycomb, or rock pockets, are spots where the cement paste didn&rsquo;t fill in around the aggregate, usually because the wall wasn&rsquo;t vibrated enough. It&rsquo;s more common than most people think, and it&rsquo;s easy to handle while the wall is open: the form crew grouts the pockets soon after stripping, then the waterproofer patches over them (we use roller-grade waterproofing, sometimes with a fabric strip embedded for reinforcement) before coating the whole wall. Missed, honeycomb acts like a pathway straight through the wall. <a href="@/services/leak-repair/honeycomb/">More on honeycomb</a>.</p>
<h2>4. Cold joints are detailed</h2>
<p>A cold joint forms wherever one pour of concrete ends and the next begins: footing to wall, or between pours on a long wall. It&rsquo;s a formed crack, and in our area it&rsquo;s the second most common leak source we find. There are three ways to seal it, and all of them depend on timing: a waterstop or joint sealant placed before the next pour (by the concrete contractor), a waterproofing joint detail on the outside before backfill (by the waterproofing contractor), or an injection repair from the inside before the basement is finished. The cheapest of the three is the one done before backfill. <a href="@/services/leak-repair/cold-joints/">More on cold joints</a>.</p>
<h2>5. Pipe penetrations are sealed</h2>
<p>Every house has at least one pipe through the foundation, usually the main water line. The opening is larger than most leak points, so when it leaks it soaks the surrounding finishes quickly. Seal around every pipe before backfill, and check again before the area around it is finished inside. <a href="@/services/leak-repair/pipe-penetrations/">More on pipe penetrations</a>.</p>
<h2>6. The coating matches the space</h2>
<p>The code minimum is damp proofing from the top of the footing (or 6 inches below the top of the basement floor, whichever is higher) up to finished grade (R406.1). Where a high water table or other severe soil-water conditions are known, the code requires waterproofing instead (R406.2).</p>
<p>The bigger question is what the space will become. Damp proofing is a thin asphalt coat, 10 to 20 mils, that slows vapor and cracks with the concrete. Waterproofing is rubber-modified, at least 40 mils and up to 80 or more, and stretches over cracks as they open. On our comparison chart damp proofing is rated for no water pressure at all, while our waterproofing options are rated from 3 feet up to 8 or 12 feet of water at a crack. A crawlspace and a finished custom basement shouldn&rsquo;t get the same coating. <a href="@/services/belowgrade/waterproofing/">Compare the options</a>.</p>
<h2>7. The footing drain is in and goes somewhere</h2>
<p>Most basements need a drain at the footing (R405.1). The code exceptions are well-drained gravel and sand soils, or a lot covered by a geotechnical report that says no drain is needed. A traditional gravel drain has to extend at least 1 foot beyond the outside edge of the footing and 6 inches above its top, covered with an approved filter membrane, and the water has to discharge somewhere: by gravity or a pump to an approved drainage system.</p>
<p>We usually install strip drain instead of pipe and gravel. It&rsquo;s an engineered system that ICC stands behind, set vertically at the base of the wall or the face of the footing, and it doesn&rsquo;t need a gravel bed in most cases. Whatever the system, confirm the outlet before the trench is filled. <a href="@/services/belowgrade/foundation-drains/">More on foundation drains</a>.</p>
<h2>8. Drainage or protection board is on</h2>
<p>A drainage board between the wall and the backfill does two jobs: it lets water fall straight down to the footing drain instead of building pressure against the wall, and it protects the coating from rocks in the fill. Drainage mat, Warm-N-Dri and Thermal Drain each add drainage, and the last two add insulation. Thermal Drain also adds strength to the waterproofing, as long as it goes on the same day as the coating. <a href="@/services/belowgrade/foundation-insulation/">Compare the boards</a>.</p>
<h2>9. The grade falls away from the wall</h2>
<p>Finally, the backfill itself. The code calls for the grade to fall at least 6 inches within the first 10 feet from the foundation (R401.3), and backfill settles, so plan for it. Downspouts should carry water at least 5 to 10 feet from the house, and sprinklers should face away from the wall. A perfect coating and drain can still be overwhelmed by a yard that sends every storm toward the basement.</p>
<h2>Walk it before the excavator comes back</h2>
<p>None of these items takes long while the wall is open. If you&rsquo;d like us to look at a foundation before backfill, or bid the waterproofing and drain together, <a href="@/{_["BID"]}">send us the plans</a>.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Source: <a href="{SRC}" rel="noopener">Utah Residential Code 2021, Chapter 4 (Foundations), sections R401.3, R404.1.7, R405.1, R406.1 and R406.2</a>. Always check the current code and your local building department&rsquo;s amendments.</p>'''
    body = _["phero"](trail, POST[0], f"By {NAME} &middot; {nice('2026-10-19')}", "Blog &middot; For builders", "trench-wasatch-truck", "Open footing drain trench along a new foundation, before backfill") + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">{body_txt}</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Foundation Backfill Checklist: Utah Builders | Rocky Mountain",
            "meta": "A foundation backfill checklist for Utah builders: ties, honeycomb, cold joints, pipes, coating, footing drain and grade, with the Utah code sections.",
            "body": body, "og": "trench-wasatch-truck", "ogtype": "article",
            "schema": [crumbs_ld(path, trail), faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-19", "dateModified": "2026-10-19",
                       "image": U + "assets/img/trench-wasatch-truck.webp", "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)}]}


def listing(path, label, h1, title, meta, canonical=None, robots=None):
    trail = [_["HOME"], ("Blog", "blog/")] + ([(label, path)] if path != "blog/" else [])
    if path == "blog/": trail = [_["HOME"], ("Blog", "blog/")]
    A = _["A"]
    items = [(POST[0], POST[1], "2026-10-19", NAME, "trench-wasatch-truck")] + [(t, p, d, a, i) for k, p, t, d, a, i in OLD]
    cards = "".join(f'<a class="post-card reveal" href="@/{p}">{img(i, "")}<span class="pc-meta">{nice(d)} &middot; {a}</span><b>{t}</b><em>Read {A}</em></a>' for t, p, d, a, i in items)
    body = _["phero"](trail, h1, "News, projects and how-to from Rocky Mountain Waterproofing in West Jordan.", "Blog &middot; News &amp; more") + f'<section class="sec"><div class="wrap"><div class="posts">{cards}</div></div></section>' + _["cta"]()
    pg = {"path": path, "canonical": canonical or canon(path), "title": title, "meta": meta, "body": body, "schema": [crumbs_ld(path, trail)]}
    if canonical: pg["sitemap"] = False
    if robots: pg["robots"] = robots; pg["sitemap"] = False
    return pg


def pages():
    blog = canon("blog/")
    m = "News, projects and how-to articles from Rocky Mountain Waterproofing in West Jordan, Utah: foundation waterproofing, leak repair and The House That SHE Built."
    return [listing("blog/", "Blog", "Blog: News &amp; More", "Blog: News &amp; More | Rocky Mountain Waterproofing", m),
            listing("blog/categories/", "Categories", "Blog Categories", "Blog Categories | Rocky Mountain Waterproofing, West Jordan", m, canonical=blog),
            listing("blog/latest-items/", "Latest items", "Latest Blog Items", "Latest Blog Items | Rocky Mountain Waterproofing, Utah", m, canonical=blog),
            listing("blog/items/", "Items", "Blog Items", "Blog Items | Rocky Mountain Waterproofing, West Jordan, Utah", m, canonical=blog),
            listing("blog/tag/", "Tag", "Blog Posts Tagged &ldquo;News&rdquo;", "Posts Tagged News | Rocky Mountain Waterproofing Blog", m, robots="noindex, follow"),
            listing("blog/search/", "Search", "Search the Blog", "Search the Blog | Rocky Mountain Waterproofing, West Jordan", m, robots="noindex, follow"),
            new_post()] + [old_post(*o) for o in OLD]
