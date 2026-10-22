"""Pages for the sterlingtreeco.godaddysites.com redesign: "Canopy".

Sterling is a crew of ISA certified climbing arborists, and their best photo shows exactly that: a climber in a London plane, high above
Salt Lake City with the Wasatch behind him. It opens the page full-bleed. The signature is the tree check: the International Society of
Arboriculture's own tree risk checklist, drawn onto a tree. Each question lights the part of the tree it concerns (roots, trunk, branch
unions, canopy, site); answer yes to any and ISA's advice is to have the tree examined by an ISA Certified Arborist, with the ways an
arborist may manage the risk (pruning, cabling and bracing, routine care, removal) linked to what Sterling does.
Evergreen and sterling silver; DM Serif Display, Manrope, IBM Plex Mono.
References (screenshotted 21 Oct 2026): Studio McGee (dark frame, big photography), Dwell (headline over a full photo), ArchDaily (grid).
Same single URL plus one new post."""
import html, json, os, re
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, HERE
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import p_blog

header, footer = K.header, K.footer
cta = K.cta

# ISA, "Recognizing Tree Risk" (TreesAreGood consumer brochure, 2021): the checklist, each mapped to the part of the tree it concerns
CHECK = [("deadb", "canopy", "Are there large dead branches?"), ("hang", "canopy", "Are there detached, hanging branches?"), ("fallen", "canopy", "Have any branches fallen from the tree?"),
         ("bark", "trunk", "Is there loose bark on the trunk?"), ("crack", "union", "Are there cracks or splits in the trunk or where branches are attached?"),
         ("form", "trunk", "Has the trunk developed unusually?"), ("cavity", "trunk", "Are there cavities or rotten wood along the trunk or in major branches?"),
         ("mush", "roots", "Are mushrooms present at the base of or under the tree?"), ("site", "roots", "Has the area recently been altered by construction, changes in soil level, or installations of lawns or pavement?"),
         ("leaf", "canopy", "Have the leaves developed an unusual yellow color or do they seem smaller in size?"), ("topped", "union", "Has the tree been topped or heavily pruned?")]
MANAGE = [("Prune the tree and remove the defective branches.", "Tree trimming, hedges &amp; ornamental pruning"), ("Cable and brace the tree for weak branches and stems.", "Cabling / bracing"),
          ("Provide routine care: water, mulch, pruning and, in some cases, nutrients.", "Tree trimming &amp; pruning"), ("Remove the tree, and plant an appropriate replacement if possible.", "Tree removals, storm damage")]
SERV = [("Tree trimming &amp; removals", "Trimming for health and structure, and removals when a tree has to come down, by climbing arborists."),
        ("Hedges &amp; ornamental pruning", "Shaping hedges and ornamental trees with the care an arborist brings to the big ones."),
        ("Land clearing", "Clearing trees and brush from lots and overgrown ground."),
        ("Cabling / bracing", "Physical support for weak branches and stems, to increase their strength and stability."),
        ("Storm damage", "Broken limbs and storm-damaged trees, cleaned up and made safe.")]


def tree_svg():
    return '''<svg class="tc-tree" viewBox="0 0 320 380" aria-hidden="true">
<g class="z z-canopy"><path d="M160 30c-58 0-104 36-112 86-24 8-38 30-34 54 5 30 34 46 64 42 18 22 50 32 82 32s64-10 82-32c30 4 59-12 64-42 4-24-10-46-34-54-8-50-54-86-112-86z"/></g>
<g class="z z-union"><path d="M150 236l-34-58M170 236l38-64M160 220v-70" stroke-width="12" stroke-linecap="round" fill="none"/></g>
<g class="z z-trunk"><path d="M142 236h36l8 96h-52z"/></g>
<g class="z z-roots"><path d="M134 330c-22 6-48 10-72 10M186 330c22 6 48 10 72 10M150 334l-16 26M170 334l16 26" stroke-width="9" stroke-linecap="round" fill="none"/><path d="M40 344h240" stroke-width="3" fill="none" class="ground"/></g>
<g class="tags"><text x="292" y="86" text-anchor="end" class="t t-canopy">CANOPY</text><text x="232" y="164" class="t t-union">UNIONS</text><text x="196" y="296" class="t t-trunk">TRUNK</text><text x="270" y="372" text-anchor="end" class="t t-roots">ROOTS &amp; SITE</text></g>
</svg>'''


def treecheck():
    qs = "".join(f'<li><span class="q">{t}</span><span class="yn" role="group" aria-label="{html.escape(t)}"><button type="button" data-q="{k}" data-z="{z}" data-v="yes" aria-pressed="false">Yes</button><button type="button" data-q="{k}" data-z="{z}" data-v="no" aria-pressed="false">No</button></span></li>' for k, z, t in CHECK)
    mg = "".join(f'<li><b>{a}</b><span>Sterling: {s}</span></li>' for a, s in MANAGE)
    return f'''<div class="tc" data-tc>
<div class="tc-art">{tree_svg()}<p class="tc-count"><span data-tc-yes>0</span> yes &middot; <span data-tc-ans>0</span> of {len(CHECK)} answered</p></div>
<div class="tc-q"><ol class="tc-list">{qs}</ol>
<div class="tc-res" data-tc-res aria-live="polite"><p class="mono" data-tc-h>Answer the questions above</p><p data-tc-p>Look at one tree at a time. Based on the ISA&rsquo;s tree risk checklist.</p>
<div data-tc-more hidden><p class="mono">How an arborist may manage the risk</p><ul class="tc-manage">{mg}</ul><a class="btn accent" href="#estimate">Ask for a free estimate {ARROW}</a></div></div>
<p class="small">Checklist from the International Society of Arboriculture, <em>Recognizing Tree Risk</em> (TreesAreGood.org). It doesn&rsquo;t replace an on-site assessment.</p></div>
</div>'''


FAQ = [("Are your arborists ISA certified?", "<p>Yes. Sterling Tree Co. is a team of ISA certified, climbing arborists.</p>"),
       ("What does an ISA Certified Arborist do differently?", "<p>According to the International Society of Arboriculture, ISA Certified Arborists have proven a level of knowledge in the art and science of tree care through experience and a comprehensive exam, and must continue their education to keep the certification.</p>"),
       ("Do you give free estimates?", "<p>Yes. Call 315-863-6747 today for a free estimate.</p>"),
       ("Can a weak tree be saved without removing it?", "<p>Sometimes. ISA notes that an arborist may suggest pruning out defective branches or cabling and bracing weak branches and stems; such supports increase strength and stability but are not guarantees against failure. Some trees with unacceptable risk are best removed.</p>")]


def home():
    body = f'''
<section class="s-hero"><div class="sh-img" data-parallax="0.08">{img("st-hero", "A Sterling Tree Co. arborist climbing a bare London plane tree high above Salt Lake City homes, with snowy mountains in the distance", priority=True)}</div>
<div class="wrap sh-in"><div class="sh-txt"><p class="label">Salt Lake City &middot; ISA certified arborists</p>
<h1>Tree service in Salt Lake City, <em>for the love of trees.</em></h1>
<p class="lede">Sterling Tree Co. is a tree service in Salt Lake City run by a team of ISA certified, climbing arborists. Trimming and removals, hedges and ornamental pruning, land clearing, cabling and bracing, and storm damage, with a fun, personal customer service experience.</p>
<div class="btn-row"><a class="btn accent" href="tel:+13158636747">{PHONE} Call 315-863-6747</a><a class="btn ghost" href="#treecheck">Check a tree {ARROW}</a></div></div></div>
<p class="sh-cap">Sterling arborist in a London plane, Salt Lake City</p></section>

<section class="sec s-intro"><div class="wrap s-intro-in">
<div class="reveal"><p class="label">Who we are</p><h2>Built on a deep-rooted <em>interest in arboriculture.</em></h2></div>
<div class="reveal"><p class="lede">We strive to provide the absolute best quality tree care in Salt Lake City, second to none. Our company was built on a deep rooted interest in arboriculture as well as providing a fun, personal customer service experience.</p>
<p>Our team of climbing arborists is ISA certified, and estimates are free.</p></div>
</div></section>

<section class="sec s-check" id="treecheck"><div class="wrap">
<div class="s-head split-h reveal"><div><p class="label">The tree check</p><h2>Is your tree <em>trying to tell you something?</em></h2></div><p class="lede">Walk around one tree and answer ISA&rsquo;s eleven questions. The parts of the tree you flag light up.</p></div>
{treecheck()}
</div></section>

<section class="sec s-serv" id="services"><div class="wrap">
<div class="s-head reveal"><p class="label">Our services</p><h2>Five things, <em>done right.</em></h2></div>
<div class="serv">{"".join(f'<div class="sv reveal"><span class="mono">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(SERV))}
<figure class="sv-fig reveal">{img("st-climb", "A Sterling arborist roped in high on a tall tree against a blue sky")}<figcaption>Our team of climbing arborists</figcaption></figure></div>
</div></section>

<section class="s-band"><div class="band-img" data-parallax="0.1">{img("st-elm", "A large elm with snow on its branches, looking up into the canopy")}</div>
<div class="wrap"><blockquote class="reveal"><p class="label">ISA on certified arborists</p><p>&ldquo;Regular tree care performed by an ISA Certified Arborist will provide an opportunity to identify trees that have defects and unacceptable risk levels.&rdquo;</p><cite>International Society of Arboriculture, <em>Recognizing Tree Risk</em></cite></blockquote></div></section>

<section class="sec s-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>Ask an <em>arborist.</em></h2>
<a class="post-card s-post" href="@/{p_blog.SLUG}"><span class="label">New on the blog</span><b>{p_blog.H1}</b><p>What topping does to a tree, from the International Society of Arboriculture, and what to do instead.</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(FAQ)}</div>
</div></section>

<section class="sec s-est" id="estimate"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Free estimate</p><h2>Call today for <em>a free estimate.</em></h2><p class="lede">Call <a href="tel:+13158636747">315-863-6747</a> or send the form and we&rsquo;ll get back to you.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:+13158636747">315-863-6747</a></dd></div><div><dt>Address</dt><dd><address>1826 S 1100 E<br>Salt Lake City, UT 84105</address></dd></div></dl></div>
<div class="reveal form-col">{K.form("Request a free estimate")}</div>
</div></section>
'''
    return {"path": "", "canonical": U, "title": "Tree Service Salt Lake City | ISA Arborists | Sterling Tree",
            "meta": "Sterling Tree Co.: tree service in Salt Lake City by ISA certified climbing arborists. Trimming, removals, pruning, cabling and bracing, storm damage.",
            "body": body, "body_class": "is-home", "og": "st-hero", "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}


def make_pages():
    out = [home(), p_blog.page(K), K.notfound((("Home", ""), ("Tree check", "#treecheck"), ("Blog", p_blog.SLUG)))]
    return [K.fit(dict(x, body=Q(x["body"])), (" Call 315-863-6747.", " Salt Lake City, UT.")) for x in out]
