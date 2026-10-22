"""Blog for armour-crete.com (the live site has none): a blog index and one new post.

"White Stains on Concrete in St. George: What Efflorescence Is and How to Stop It"
Main phrase: "efflorescence on concrete" (informational). No page on the site targets it (the home page mentions the word once);
it links to driveway sealing, pool deck sealing, expansion joints and products without competing with them.
Facts and sources, checked 20 Oct 2026:
- Ritchie, T. (1960). CBD-2 Efflorescence. Canadian Building Digest, National Research Council Canada (mirror):
  https://web.mit.edu/parmstr/Public/NRCan/CanBldgDigests/cbd002_e.html - a crystalline salt deposit left when water carries
  soluble salts to the surface and evaporates; needs salts, water to move them, and evaporation at the surface; salts come from
  cement, the materials, ground water and splashing/drainage water; fix the source of wetting first; scrub with water or a dilute
  acid (salts may return if the wetting continues); water repellents can push salt deposits beneath the surface and cause spalling
  in porous materials.
- The client's own text: salt off the pool, out of the softener, in the soil and the hard water; crystals growing in confined pores
  lift the surface (scaling, spalling, efflorescence); sealing keeps the pore network from staying saturated; Salt Shield 303 for
  pool decks and softener discharge.
No prices."""
from engine import faq_html, faq_ld, canon
from cfg import U, NAME, PHONES

POST = ("White Stains on Concrete in St. George: What Efflorescence Is and How to Stop It", "blog/efflorescence-white-stains-concrete-st-george/")
NRC = "https://web.mit.edu/parmstr/Public/NRCan/CanBldgDigests/cbd002_e.html"
FAQ = [("Is efflorescence harmful to concrete?", "The white deposit itself is mostly a cosmetic problem. What matters is what it tells you: water is moving through the slab and carrying salt, and the same salt crystallising inside the pores is what causes scaling and spalling."),
       ("Will efflorescence come back after I clean it?", "It can. As long as water keeps moving through the concrete and evaporating at the surface, salts keep arriving. That&rsquo;s why the source of the water has to be dealt with first."),
       ("Can I seal over efflorescence?", "Not over the deposit. Clean it off, let the concrete dry completely, deal with the water source, and then seal with a penetrating product suited to the surface.")]


def post(K, img):
    body = f'''<p class="answer">Efflorescence is the white, chalky film or crust that shows up on concrete, pavers, block and brick. It&rsquo;s salt. Water dissolves salts inside or beneath the concrete, carries them to the surface, and evaporates, leaving the salt behind. In St. George, with hard water, salty soil, pool decks and water softeners, it&rsquo;s one of the most common things homeowners notice on a slab.</p>
<p>It&rsquo;s easy to treat efflorescence as a stain and scrub it off. It&rsquo;s more useful to treat it as a message. The white bloom is telling you water is moving through the concrete, and in southern Utah that water usually brings salt with it. That&rsquo;s the same process that breaks a slab apart from the inside.</p>
<h2>What efflorescence actually is</h2>
<p>A classic building-science digest from the <a href="{NRC}" rel="noopener">National Research Council of Canada (CBD-2, &ldquo;Efflorescence&rdquo;)</a> lays out the mechanism in three conditions, and all three have to be there:</p>
<ol><li><b>Soluble salts</b> in or under the material.</li><li><b>Water</b> to dissolve them and carry them.</li><li><b>Evaporation</b> at the surface, where the water leaves and the salt stays.</li></ol>
<p>Take away any one and efflorescence stops. You can&rsquo;t take the salt out of concrete, so in practice the lever is water.</p>
<h2>Where the salt comes from here</h2>
<p>The digest lists the usual sources: the cement itself, salts in the other materials, ground water rising from below, and water from drains, splashing and runoff. In Washington County you can add a few local ones:</p>
<ul><li><b>Pool water.</b> Salt-water pools splash and drain onto the deck around them every day of the season.</li><li><b>Water softener discharge.</b> The brine from a softener often drains onto the slab beside the house or the garage.</li><li><b>Hard water.</b> Sprinklers and hoses leave mineral-heavy water on driveways and walks, over and over.</li><li><b>The soil.</b> Desert soils already carry salt, and water wicking up from below brings it with it.</li></ul>
<h2>Why it&rsquo;s more than a stain</h2>
<p>When the salt crystallises on the surface, you see efflorescence. When it crystallises just under the surface, inside the pores, it pushes. Crystals growing in a confined pore can push hard enough to lift flakes of the surface off: that&rsquo;s scaling, and deeper, spalling. The white bloom and the flaking are the same story at different depths.</p>
<p>That&rsquo;s also why the digest warns that some water-repellent treatments can backfire on porous materials: if water still gets in from behind and can&rsquo;t leave at the face, the salt can deposit just beneath the surface instead, where it does damage. The right product, on a dry slab, with the water source dealt with, matters more than putting anything on the surface.</p>
<h2>Step one: find the water</h2>
<p>The digest is clear on order: correct the source of excess wetting before removing the efflorescence, or it comes back. Walk the slab and look for the pattern:</p>
<ul><li>Bloom next to the pool edge or the softener drain points straight at the water source.</li><li>Bloom along a joint or crack suggests water getting into the sub-base and wicking back up; failed joint filler is a common culprit (see <a href="@/expansion-joint-replacement/">expansion joints</a>).</li><li>Bloom in a sprinkler arc means the irrigation needs redirecting.</li><li>Bloom along the bottom of a wall or step can be water rising from the ground or splashing off a downspout.</li></ul>
<h2>Step two: clean it off properly</h2>
<p>For light efflorescence, the digest&rsquo;s first suggestion is the simple one: scrub with water and a stiff brush, then rinse. Tougher deposits can be removed with a dilute acid solution followed by a thorough rinse, but acid etches concrete and needs care, protection and neutralising, so on decorative or sealed surfaces it&rsquo;s worth having it assessed first. Either way, the salts can return if the surface keeps getting wet, which brings you back to step one.</p>
<h2>Step three: keep the pores from staying wet</h2>
<p>Sealing doesn&rsquo;t stop concrete moving, and it doesn&rsquo;t remove the salt that&rsquo;s already in it. What a penetrating sealer does is keep the pore network from staying saturated, which starves salt crystallisation (and freeze&ndash;thaw) of the water it needs. On pool decks and around softener drains we use <a href="@/products/">Salt Shield 303</a>, a penetrating sealer made for exactly this; on driveways, <a href="@/driveway-sealing/">DECO 20 Clear</a>.</p>
<p>The order matters: clean, then let the slab dry completely, then seal. Sealer over moisture is how finishes fail. And here, sealer goes down early in the morning, before the slab takes on the day&rsquo;s heat; on a hot surface it flash-dries and leaves whiting and streaks, which is easy to confuse with efflorescence.</p>
<h2>Pavers, block walls and travertine</h2>
<p>Efflorescence isn&rsquo;t only a slab problem. Concrete pavers, block retaining walls and the mortar joints around them all contain cement, and they sit in exactly the places water collects: around pools, at the bottom of slopes, under sprinklers. The same three conditions apply, and so does the same order of work: find where the water is coming from, clean the deposit off, let everything dry, and then protect it. Travertine around a pool needs its own product rather than a concrete sealer, which is why we keep a separate one for it.</p>
<h2>When to call</h2>
<p>A little bloom on a new slab in its first season isn&rsquo;t unusual as it gives up water. Recurring efflorescence, efflorescence with flaking, or bloom that keeps returning around the pool or the softener drain is worth an assessment. We&rsquo;ll look at the surface and the water around it, and tell you what it needs; the visit is free. Call Dylan at <a href="tel:{PHONES[0][2]}">{PHONES[0][1]}</a> or Zac at <a href="tel:{PHONES[1][2]}">{PHONES[1][1]}</a>.</p>
<h2>Questions</h2>{faq_html(FAQ)}
<p class="small sources">Source: <a href="{NRC}" rel="noopener">T. Ritchie, &ldquo;Efflorescence&rdquo;, Canadian Building Digest CBD-2, National Research Council Canada (1960)</a>.</p>'''
    pg = K.page(POST[1], "Efflorescence", POST[0], f"By {NAME} &middot; October 20, 2026", "Blog", "Efflorescence on Concrete: White Stains in St. George | Armour Crete",
                "What efflorescence on concrete is, why St. George slabs get it (pool salt, softeners, hard water), and how to stop it: find the water, clean, then seal.",
                body, art=f'<div class="tex-hero bloom">' + __import__("illus").texture("broom", "ph-bloom") + '<span>Efflorescence</span></div>', crumbs=[("Blog", "blog/")], ogtype="article")
    pg["body"] = pg["body"].replace('<article class="prose">', '<article class="prose post">', 1)
    pg["schema"] += [faq_ld(FAQ), {"@type": "BlogPosting", "@id": canon(POST[1]) + "#post", "headline": POST[0], "datePublished": "2026-10-20", "dateModified": "2026-10-20",
                                   "author": {"@type": "Organization", "name": NAME}, "publisher": {"@id": U + "#business"}, "mainEntityOfPage": canon(POST[1])}]
    return pg


def pages(K, img):
    idx = K.page("blog/", "Blog", "Concrete Sealing Blog", "Notes on concrete, salt and sun in southern Utah.", "Blog", "Concrete Sealing Blog | Armour Crete, St. George UT",
                 "Concrete care notes from Armour Crete in St. George: efflorescence, salt damage, sealing schedules and how desert heat and hard water affect concrete.",
                 f'<div class="posts one"><a class="post-card" href="@/{POST[1]}"><b>{POST[0]}</b><em>Read {K.ARROW}</em></a></div>')
    return [idx, post(K, img)]
