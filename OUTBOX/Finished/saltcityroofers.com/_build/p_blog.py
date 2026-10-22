"""Blog for saltcityroofers.com: the 22 existing posts (same URLs, the client's own text, stock images removed, the three project
posts given their real photos) plus one new post.

New post: "Tear-Off or Roof-Over? Utah's Two-Layer Rule for Re-Roofing"
Main phrase: "tear off vs roof over" (informational). The client's blog has no post on it and no service page targets it; it
links to the asphalt system, Q&A and warranty pages. Facts and sources, checked 18 Oct 2026:
- International Residential Code R908.3.1.1 (as reproduced in city re-roof handouts): a new roof covering may not be installed
  over an existing one when the existing roof is water-soaked or deteriorated, when it is slate, clay, cement or asbestos-cement
  tile, or when it already has two or more applications of roof covering. Des Moines adds: or where the manufacturer's
  instructions prohibit a recover. https://gillettewy.gov/files/assets/public/v/1/development-services/documents/reroofing-2018.pdf
  https://cms2.revize.com/revize/desmoines/document_center/Development%20Services/Permit%20Development%20Center/Residential/City%20of%20Des%20Moines%20Roof%20Shingle%20Requirements.pdf
- Bountiful City, Utah, re-roof handout: with two or more layers, only removal of the existing layers and replacement may be done.
  https://bountifulutah.gov/file/d0bd72b1-0143-472f-801a-39881f38cb08
- The client's own Q&A and neighbors pages: tear-off and disposal, re-sheeting with new plywood when needed, about a week per job.
No prices.
"""
import html, json, os, re
from engine import crumbs_ld, faq_html, faq_ld, canon, img
from cfg import U, NAME, HERE
from migrate import migrate

EXT = json.load(open(os.path.join(HERE, "src", "extract.json"), encoding="utf-8"))
POSTDROP = re.compile(r"\$\s?\d|^admin$|Comments Off|^on |Share This Story|^(Facebook|Twitter|Linkedin|Reddit|Tumblr|Google\+|Pinterest|Vk|Email)$|^\d{4}-\d\d-\d\dT|"
                      r"^[A-Z][a-z]+ \d{1,2}(st|nd|rd|th), \d{4}$|^(Diagnosing Roofing Problems|Roofing FAQ.s|Roofing in Utah 101|Residential Roofing|Roofing System Upgrades|Fun Home and Garden Tips|Roofing Contractor News)(, .*)?$|Gallery$", re.I)
POST = ("Tear-Off or Roof-Over? Utah’s Two-Layer Rule for Re-Roofing", "blog/2026/10/18/tear-off-or-roof-over-utah-two-layer-rule/")
AVE = ("", "blog/2021/03/29/before-and-after-pictures-for-a-roofing-project-in-the-avenues/")
DRAPER = ("", "blog/2022/02/16/exterior-remodel-draper-utah/")
PARK = ("", "blog/2022/04/03/snow-retention-on-metal-roof-in-park-city-ut-done-by-salt-city-roofers/")
GAL = {"blog_2021_03_29_before_and_after_pictures_for_a_roofing_project_in_the_avenues": [("avenues-before-shingles", "Before: the worn shingle roof"), ("avenues-finished-a", "After: the finished roof"), ("avenues-finished-b", "After, from the street")],
       "blog_2021_03_19_finished_membrane_asphalt_roof_salt_lake_city_avenues_home": [("avenues-before-flat", "Before: the old low-slope roof"), ("avenues-finished-c", "Finished roof"), ("avenues-finished-d", "Finished roof, another angle")],
       "blog_2022_02_16_exterior_remodel_draper_utah": [("draper-craftsman-remodel", "The finished exterior"), ("draper-porch-mountains", "New porch and roofline"), ("draper-covered-porch", "Covered porch"), ("draper-roof-aerial", "The roof from above"), ("draper-soffit-ceiling", "Wood soffit ceiling"), ("draper-front-door", "Custom front door")],
       "blog_2022_04_03_snow_retention_on_metal_roof_in_park_city_ut_done_by_salt_city_roofers": [("park-city-metal-aerial", "Bird&rsquo;s-eye view of the snow retention"), ("park-city-metal-wing", "Backyard aerial view"), ("park-city-metal-top", "From directly above"), ("park-city-snow-guards", "A closer look at the snow guards")]}
_ = {}
MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def setup(phero, cta, side, arrow, home, contact, tidy, compare):
    _.update(phero=phero, cta=cta, side=side, A=arrow, HOME=home, CONTACT=contact, tidy=tidy, compare=compare)


def posts():
    out = []
    for k, v in EXT.items():
        m = re.match(r"blog_(\d{4})_(\d\d)_(\d\d)_", k)
        if not m: continue
        path = v["url"].replace(U, "")
        title = html.unescape(re.split(r" – Salt City Roofers", v["title"])[0]).strip()
        out.append({"key": k, "path": path, "title": title, "date": f"{m.group(1)}-{m.group(2)}-{m.group(3)}"})
    return sorted(out, key=lambda p: p["date"], reverse=True)


def nice(d):
    y, m, dd = d.split("-")
    return f"{MON[int(m) - 1]} {int(dd)}, {y}"


def excerpt(body, n=150):
    t = html.unescape(re.sub(r"<[^>]+>", " ", body))
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) <= n: return t
    return t[:n].rsplit(" ", 1)[0].rstrip(",;:") + "…"


def old_post(p):
    A = _["A"]
    body_txt = _["tidy"](migrate(HERE, p["key"], "saltcityroofers.com", POSTDROP, skip_heads=(p["title"],)))
    trail = [_["HOME"], ("Blog", "roofing-blog/"), (p["title"], p["path"])]
    gal = GAL.get(p["key"])
    galh = ('<div class="pgal">' + "".join(f'<figure>{img(n, html.unescape(c))}<figcaption>{c}</figcaption></figure>' for n, c in gal) + "</div>") if gal else ""
    note = '<p class="note-old">Originally published ' + nice(p["date"]) + '. Some details may have changed since; call us for current information.</p>' if p["date"] < "2020" else ""
    body = _["phero"](trail, html.escape(p["title"], quote=False), None, "Blog &middot; " + nice(p["date"]), buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post"><p class="mono meta">By {NAME} &middot; {nice(p["date"])}</p>{note}
{body_txt}{galh}
<p class="more"><a class="tlink" href="@/roofing-blog/">All posts {A}</a></p></article>{_["side"]()}</div></section>''' + _["cta"]()
    ex = excerpt(body_txt, 400)
    meta = excerpt(f"{p['title']}: {ex}", 159)
    title = p["title"] if len(p["title"]) > 42 else f"{p['title']} | Salt City Roofers"
    if len(title) > 60: title = title[:60].rsplit(" ", 1)[0].rstrip(":,.-")
    return {"path": p["path"], "canonical": canon(p["path"]), "title": title, "meta": meta, "body": body, "ogtype": "article", "og": gal[0][0] if gal else None, "_ex": excerpt(body_txt, 170),
            "schema": [{"@type": "BlogPosting", "@id": canon(p["path"]) + "#post", "headline": p["title"], "datePublished": p["date"], "author": {"@type": "Organization", "@id": U + "#business", "name": NAME},
                        "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(p["path"])}, crumbs_ld(p["path"], trail)]}


FAQ = [("Can I put new shingles over my old ones?", "Sometimes. Under the International Residential Code a second roof can go over the first only if the existing roof isn&rsquo;t water-soaked or deteriorated, isn&rsquo;t slate, clay, cement or asbestos-cement tile, and doesn&rsquo;t already have two or more layers. The shingle manufacturer&rsquo;s instructions must allow it too, and your city has the final word."),
       ("What happens if my roof already has two layers?", "Both have to come off. As Bountiful City&rsquo;s re-roof handout puts it, with two or more layers only removal of the existing layers and replacement may be done."),
       ("How can I tell how many layers I have?", "Look at the roof edge at a gutter or rake: stacked shingle edges show the layers. A roofer will confirm on the inspection, and it should be written on the estimate."),
       ("Why tear off if a roof-over is allowed?", "Because a tear-off lets the crew see and re-sheet soft decking, install ice and water membrane at the eaves, and replace flashing and drip edge instead of working around the old ones."),
       ("How long does a tear-off add?", "Tear-off and disposal is simply the first part of the job. Most of our re-roofs take about a week from start to finish, give or take a day or two for weather.")]


def new_post():
    A = _["A"]; path = POST[1]
    trail = [_["HOME"], ("Blog", "roofing-blog/"), ("Tear-off or roof-over", path)]
    body = _["phero"](trail, POST[0], "A second layer of shingles looks like a shortcut. Here is when Utah building codes allow it, when they don&rsquo;t, and why most re-roofs start with a tear-off.", "Blog &middot; October 18, 2026", buttons=False) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose post">
<p class="mono meta">By {NAME} &middot; October 18, 2026 &middot; 6 min read</p>
<p class="answer">A roof-over (installing new shingles on top of the old ones) is allowed only in narrow cases. Under the International Residential Code, which Utah cities enforce, you can&rsquo;t recover a roof that already has two or more layers, a roof that is water-soaked or deteriorated, or a slate or tile roof, and the shingle manufacturer has to allow it. Everywhere else, a tear-off down to the deck is the standard, and usually the better roof.</p>

<h2>Roof-over, recover, layover: same idea</h2>
<p>Contractors use several names for it: a roof-over, an overlay, a layover, or in code language a <b>roof recover</b>. They all mean the same thing: leaving the existing shingles in place and nailing a new layer on top. It skips the tear-off and the disposal, which is why it&rsquo;s tempting.</p>
<p>A <b>tear-off</b>, or roof replacement, removes every existing layer down to the roof deck, the plywood or boards the roof is built on. Then the deck is checked, repaired where needed, and a complete new system goes on.</p>

<h2>What the code says</h2>
<p>The International Residential Code covers re-roofing in Section R908. Its rule on recovers, R908.3.1.1, lists the cases where a new roof covering may <b>not</b> be installed over an existing one:</p>
<ul>
<li>The existing roof or roof covering is water-soaked or has deteriorated to the point that it isn&rsquo;t an adequate base for more roofing.</li>
<li>The existing roof covering is slate, clay, cement or asbestos-cement tile.</li>
<li>The existing roof already has <b>two or more applications</b> of any type of roof covering.</li>
</ul>
<p>Some city handouts add a fourth condition that matters just as much in practice: no recover where the manufacturer&rsquo;s installation instructions prohibit it. If the new shingle&rsquo;s instructions say tear-off only, a roof-over isn&rsquo;t an option.</p>

<h2>The two-layer rule in Utah</h2>
<p>Utah cities enforce the same rule. Bountiful City&rsquo;s re-roof handout says it plainly: when a roof has two or more layers, only removal of the existing layers and roof replacement may be done. Requirements and permits are set by each city&rsquo;s building department, so check with yours, but the two-layer limit is the common thread.</p>
<p>In other words, if your house was already roofed over once, the next roof starts with a full tear-off. On older homes, it&rsquo;s worth finding out how many layers are up there before you compare bids.</p>

<h2>Why a tear-off is usually the better roof</h2>
<p>Even when a roof-over is allowed, a tear-off has real advantages:</p>
<ul>
<li><b>You can see the deck.</b> Soft or rotted boards hide under old shingles. After tear-off, damaged areas get re-sheeted with new plywood before the new roof goes on.</li>
<li><b>Ice and water membrane goes where it belongs.</b> In a Utah winter, ice backs water up at the eaves and in valleys. A self-adhering ice and water membrane is installed directly on the deck there, which a roof-over can&rsquo;t do properly.</li>
<li><b>New flashing and drip edge.</b> The places where roofs leak (walls, chimneys, pipes, valleys) get new metal instead of being shimmed around the old.</li>
<li><b>A flatter, longer-lasting finish.</b> New shingles over old ones telegraph every bump and curl underneath.</li>
<li><b>Less weight.</b> Every layer adds load to the framing, and a Utah roof already has to carry snow.</li>
<li><b>Warranty.</b> Manufacturer warranties depend on installation to their specifications. Ask how a recover would affect yours.</li>
</ul>
<p>That&rsquo;s why our own process starts with tear-off and disposal of the old materials. As we explain in our <a href="@/roofing-q-a/">roofing Q&amp;A</a>, sometimes we then re-sheet the roof, and whether or not we do, the next step is installing the complete new system.</p>
<figure class="post-img">{img("avenues-before-flat", "An older Salt Lake City roof before a re-roof")}<figcaption>Before a re-roof in the Avenues. What&rsquo;s under the old roofing only shows once it comes off.</figcaption></figure>

<h2>When a roof-over can make sense</h2>
<p>A recover isn&rsquo;t always wrong. On a roof with a single layer, a sound deck, no soft spots, and a shingle whose manufacturer allows it, it can be a legitimate choice, for example on a detached garage or shed, or where the budget really can&rsquo;t stretch. The point is to make it a decision based on what&rsquo;s actually up there, not a shortcut offered without a look at the roof.</p>

<h2>How to check your roof before you get bids</h2>
<ol>
<li>Look at the roof edge at a gutter or along a rake. Stacked shingle edges mean more than one layer.</li>
<li>From the attic, look for stains, daylight, or sagging between rafters.</li>
<li>Ask every bidder how many layers are on the roof now and how they know.</li>
<li>Ask whether the bid includes tear-off, disposal and re-sheeting, and how damaged decking will be handled.</li>
<li>Make sure the estimate names the system: underlayment, ice and water, flashing, drip edge and ventilation, not just &ldquo;shingles.&rdquo;</li>
</ol>
<p>Our <a href="@/asphalt-shingle-systems/">asphalt shingle system</a> page lists every layer that should be on that estimate, and our <a href="@/roof-warranty-information/">warranty information</a> page explains the coverage options. If you&rsquo;d like a look at your own roof, our inspection and written quote cost nothing; <a href="@/{_["CONTACT"]}">get in touch</a>.</p>

<h2>Questions</h2>
{faq_html(FAQ)}

<div class="sources"><h3>Sources</h3><ul>
<li>International Residential Code, Section R908.3.1.1 (Roof recover not allowed), as reproduced in the City of Gillette re-roofing handout: <a href="https://gillettewy.gov/files/assets/public/v/1/development-services/documents/reroofing-2018.pdf" rel="noopener">gillettewy.gov</a></li>
<li>Bountiful City, Utah, residential re-roof handout: <a href="https://bountifulutah.gov/file/d0bd72b1-0143-472f-801a-39881f38cb08" rel="noopener">bountifulutah.gov</a></li>
<li>City of Des Moines, roof shingle requirements (manufacturer instructions and recovers): <a href="https://cms2.revize.com/revize/desmoines/document_center/Development%20Services/Permit%20Development%20Center/Residential/City%20of%20Des%20Moines%20Roof%20Shingle%20Requirements.pdf" rel="noopener">City of Des Moines (PDF)</a></li>
</ul></div>
</article>{_["side"]()}</div></section>''' + _["cta"]()
    return {"path": path, "canonical": canon(path), "title": "Tear-Off or Roof-Over? Utah's Two-Layer Re-Roofing Rule",
            "meta": "Tear-off or roof-over? When the building code lets new shingles go over old ones in Utah, the two-layer rule, and why most re-roofs start with a tear-off.",
            "body": body, "ogtype": "article", "og": "avenues-before-flat", "_ex": "When Utah building codes allow new shingles over old ones, the two-layer rule, and why most re-roofs start with a tear-off.", "_date": "2026-10-18",
            "schema": [{"@type": "BlogPosting", "@id": canon(path) + "#post", "headline": POST[0], "datePublished": "2026-10-18", "dateModified": "2026-10-18", "image": U + "assets/img/avenues-before-flat.webp",
                        "author": {"@type": "Organization", "@id": U + "#business", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(path)},
                       crumbs_ld(path, trail), faq_ld(FAQ)]}


def index(items):
    A = _["A"]; trail = [_["HOME"], ("Blog", "roofing-blog/")]
    rows = "".join(f'<a class="prow reveal" href="@/{pg["path"]}"><span class="mono">{nice(d)}</span><b>{t}</b><span class="ex">{pg["_ex"]}</span><i>{A}</i></a>' for pg, t, d in items)
    body = _["phero"](trail, "The Salt City Roofers Blog", "Roofing notes, project write-ups and homeowner guides from Salt Lake City, since 2013.", "Blog", buttons=False) + f'''
<section class="sec"><div class="wrap"><div class="plist">{rows}</div></div></section>''' + _["cta"]()
    return {"path": "roofing-blog/", "canonical": canon("roofing-blog/"), "title": "Roofing Blog | Salt City Roofers, Salt Lake City Roofers",
            "meta": "The Salt City Roofers blog: project write-ups from the Avenues, Draper and Park City, plus guides on warranties, shingles, ice dams and choosing a roofer.",
            "body": body, "schema": [crumbs_ld("roofing-blog/", trail)]}


def pages():
    ps = posts()
    olds = [(old_post(p), p["title"], p["date"]) for p in ps]
    np = new_post()
    items = [(np, POST[0], "2026-10-18")] + olds
    out = [index(items), np] + [o[0] for o in olds]
    for pg in out: pg.pop("_ex", None); pg.pop("_date", None)
    return out
