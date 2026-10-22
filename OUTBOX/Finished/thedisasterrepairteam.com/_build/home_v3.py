"""Premium home (v3) for thedisasterrepairteam.com: "Four kinds of bad day".
References (screenshotted 20 Oct 2026): SERVPRO (category urgency, water/fire/mold tiles), Paul Davis (dark emergency hero with
a help panel), Linear (dark interface, each state re-colours the page). Signature: the damage-type switcher. Pick water, fire,
smoke or mold; the hero re-colours, swaps to that damage's real job photo, and lists the client's own four steps for it.
Second piece: the one-team line (the client's "fewer handoffs" claim drawn as one continuous line)."""
import html
from engine import img, crumbs_ld, faq_html, faq_ld
from cfg import U
from pagekit import ARROW, PHONE, HOME, cta, form
import p_blog

ELS = [("water", "Water", "water_damage_cleanup_restoration", "water-damage-cleanup-restoration/", "drt-ceiling", "A ceiling bulging with trapped water from a leak above"),
       ("fire", "Fire", "fire_damage_cleanup_restoration", "fire-damage-cleanup-restoration/", "drt-fire", "A fire-damaged ceiling opened above a bathtub, charred joists and soot"),
       ("smoke", "Smoke", "smoke_damage_cleanup_restoration", "smoke-damage-cleanup-restoration/", "drt-fire", "Soot and smoke residue across a ceiling after a fire"),
       ("mold", "Mold", "mold_remediation_restoration", "mold-remediation-restoration/", "drt-mold", "Mold growth behind removed baseboard and drywall")]
FAQ = [("Do you work with insurance?", "Yes. Damage is documented clearly, with photos, readings and scope notes, so the job can move forward with stronger claim support and fewer communication gaps. Coverage decisions are your insurer&rsquo;s."),
       ("How fast can you get here?", "The target is a 60-minute on-site response for emergencies, available 24/7. For active damage, calling is the fastest option."),
       ("Can you do the repairs, or just the cleanup?", "Both. Because the company is also a licensed B-100 general contractor, cleanup does not have to stop where reconstruction starts."),
       ("Do you cover St. George?", "Yes. Northern Utah is 385-287-6344; Southern Utah (St. George) is 435-619-9594.")]


def home(steps_of):
    tabs = "".join(f'<button type="button" role="tab" class="et et-{e}" aria-selected="{"true" if i == 0 else "false"}" data-el="{e}"><span class="ed"></span>{n}</button>' for i, (e, n, k, p, im, a) in enumerate(ELS))
    bgs = "".join(f'<figure class="eb{" on" if i == 0 else ""}" data-el="{e}">{img(im, a, priority=(i == 0))}</figure>' for i, (e, n, k, p, im, a) in enumerate(ELS))
    panels = ""
    for i, (e, n, k, p, im, a) in enumerate(ELS):
        st = "".join(f'<li><span>{j + 1:02d}</span><b>{t}</b><p>{d}</p></li>' for j, (t, d) in enumerate(steps_of(k)))
        panels += f'<div class="ep" data-el="{e}"{"" if i == 0 else " hidden"}><p class="label">What happens with {n.lower()} damage</p><ol class="esteps">{st}</ol><a class="tlink light" href="@/{p}">{n} damage restoration {ARROW}</a></div>'
    stages = ["Immediate triage", "On-site stabilization", "Insurance &amp; scope", "Repair &amp; rebuild"]
    node = lambda cls: "".join(f'<li class="{cls}"><span></span><b>{s}</b></li>' for s in stages)
    body = f'''
<section class="dr-hero el-water" data-els><div class="eb-wrap">{bgs}</div><div class="wrap dh-grid">
<div class="dh-text"><p class="label"><span class="pulse"></span>24/7 cleanup, repair &amp; insurance claim support</p>
<h1>Water damage restoration in Lehi and across Utah. <span class="h1-sub">Fire, smoke and mold too.</span></h1>
<p class="lede">Disaster Repair Team does water damage restoration in Lehi, across Northern Utah and in St. George, plus fire, smoke and mold restoration, for homes and businesses. One team from the first call through the rebuild.</p>
<div class="btn-row"><a class="btn accent" href="tel:+13852876344">{PHONE} Call 385-287-6344</a><a class="btn ghost" href="@/request-help/">Request help or an estimate {ARROW}</a></div>
<ul class="dh-facts"><li>Licensed &amp; insured (B-100)</li><li>IICRC certified</li><li>Target 60-minute response</li><li>4.9 &middot; 120+ Google reviews</li></ul></div>
<div class="dh-panel"><p class="dp-q">What happened?</p><div class="etabs" role="tablist" aria-label="Choose the type of damage">{tabs}</div>{panels}</div>
</div></section>

<section class="sec"><div class="wrap">
<div class="head split-head reveal-up"><div><p class="label">One team</p><h2>Fewer handoffs. <span>One line from call to rebuild.</span></h2></div>
<p>The work centers on stabilizing active damage, documenting the loss, and keeping the project moving toward cleanup, repairs and reconstruction with fewer handoffs. Because the company is also a licensed general contractor, cleanup does not have to stop where reconstruction starts.</p></div>
<div class="handoff reveal-up" data-handoff><div class="hrow broken"><span class="hl">Separate companies</span><ol>{node("n")}</ol></div><div class="hrow one"><span class="hl">Disaster Repair Team</span><ol>{node("n")}</ol></div></div>
</div></section>

<section class="sec svc-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Specialty services</p><h2>Some losses need <span>more than mitigation.</span></h2></div>
<div class="svc-grid">
<a class="sv el-water reveal-up" href="@/water-damage-cleanup-restoration/">{img("drt-carpet", "")}<b>Water damage</b><span>Mitigation, extraction, drying and repair coordination for leaks, floods, plumbing failures and storm water.</span></a>
<a class="sv el-fire reveal-up" href="@/fire-damage-cleanup-restoration/">{img("drt-fire", "")}<b>Fire damage</b><span>Cleanup, smoke remediation, documentation and rebuild support.</span></a>
<a class="sv el-mold reveal-up" href="@/mold-remediation-restoration/">{img("drt-mold-corner", "")}<b>Mold</b><span>Inspection, containment, remediation and moisture-source correction.</span></a>
<a class="sv el-sewage plain reveal-up" href="@/sewage-cleanup/"><b>Sewage backup cleanup</b><span>Safer handling and cleanup for sewage backups, drain overflows and contaminated water.</span></a>
<a class="sv el-foundation plain reveal-up" href="@/foundation-repair/"><b>Foundation crack &amp; leak repair</b><span>Wall cracks, seepage and water intrusion, with honest guidance when a structural evaluation is needed.</span></a>
<a class="sv el-insulation plain reveal-up" href="@/insulation-services/"><b>Insulation</b><span>In-house insulation removal and replacement after a loss.</span></a>
<a class="sv el-commercial plain reveal-up" href="@/commercial-restoration/"><b>Commercial restoration</b><span>Fast response and clear coordination for occupied office, retail, industrial and apartment properties.</span></a></div>
</div></section>

<section class="quote-band"><div class="qb-bg" data-parallax="0.15">{img("drt-mold-corner", "")}</div><div class="wrap"><blockquote class="reveal-up">Extraction alone is not <span>the finish line.</span></blockquote><footer>The job also needs documented drying, moisture monitoring and a repair strategy that fits the actual scope of damage. <a href="@/water-damage-cleanup-restoration/">How we handle water damage</a></footer></div></section>

<section class="sec areas-sec"><div class="wrap">
<div class="head reveal-up"><p class="label">Proudly serving Northern &amp; Southern Utah</p><h2>Two numbers. <span>Northern Utah and St. George.</span></h2></div>
<div class="two"><div class="loc reveal-up"><span class="label">Northern Utah &middot; 24/7</span><a class="lp" href="tel:+13852876344">385-287-6344</a><p>Salt Lake, Utah, Davis, Weber, Box Elder, Summit, Tooele, Wasatch and Juab counties.</p></div>
<div class="loc reveal-up"><span class="label">Southern Utah &middot; St. George</span><a class="lp" href="tel:+14356199594">435-619-9594</a><p>Washington and Iron counties, including St. George and Cedar City.</p></div></div>
<p><a class="tlink" href="@/landing-pages/">Find restoration help in your city {ARROW}</a></p></div></section>

<section class="sec"><div class="wrap split" style="align-items:start">
<div class="reveal-up"><p class="label">Questions</p><h2>Good to know.</h2>{faq_html(FAQ)}
<a class="guide-mini" href="@/{p_blog.POST[1]}"><span class="label">New on the blog</span><b>{p_blog.POST[0]}</b><em>Read it {ARROW}</em></a></div>
<div class="reveal-up form-col">{form("Request help or an estimate", msg_label="What happened?")}<p class="small">Active damage? Calling is still the fastest option: <a href="tel:+13852876344">385-287-6344</a>.</p></div>
</div></section>
''' + cta()
    return {"path": "", "canonical": "https://thedisasterrepairteam.com/", "title": "Water Damage Restoration Lehi, UT | Disaster Repair Team", "og": "drt-ceiling",
            "meta": "Water damage restoration in Lehi and across Utah, plus fire, smoke and mold. 24/7, IICRC certified, B-100 licensed, insurance documentation support.",
            "body": body, "schema": [crumbs_ld("", [HOME]), faq_ld(FAQ)]}
