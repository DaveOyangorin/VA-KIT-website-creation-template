"""Pages for a business with no website: home, contact, one post, 404. All copy lives in content.py (facts from the Google listing only,
plus sourced help). Layout variant (T.LAYOUT): "overlay" (headline over the photo), "split" (text panel beside the photo) or "low"
(headline anchored to the bottom of a tall photo)."""
from engine import img, canon, faq_html, faq_ld, crumbs_ld
from cfg import U, NAME, PHONES, ADDRESS, AREAS
import pagekit as K
from pagekit import ARROW, PHONE, HOME, Q
import content as T
import p_blog

header, footer = K.header, K.footer
LAB, DISP, TEL = PHONES[0]


def hero():
    btns = f'<div class="btn-row"><a class="btn accent" href="tel:{TEL}">{PHONE} Call {DISP}</a><a class="btn ghost" href="#tool">{T.SIG_BTN} {ARROW}</a></div>'
    txt = f'<p class="label">{T.LABEL}</p><h1>{T.H1}</h1><p class="lede">{T.LEDE}</p>{btns}'
    pic = img("hero", T.HERO_ALT, priority=True)
    if T.LAYOUT == "split":
        return f'<section class="lx-hero lx-split"><div class="lx-panel"><div class="lx-txt">{txt}</div></div><div class="lx-pic">{pic}<p class="credit">{T.CREDIT}</p></div></section>'
    return f'<section class="lx-hero lx-{T.LAYOUT}"><div class="lx-bg" data-parallax="0.08">{pic}</div><div class="wrap lx-in"><div class="lx-txt">{txt}</div></div><p class="credit">{T.CREDIT}</p></section>'


def facts():
    addr = "".join(f'<div><dt>{l}</dt><dd><address>{a}</address></dd></div>' for l, a in ADDRESS) or f'<div><dt>Where we work</dt><dd>{" &middot; ".join(AREAS)}</dd></div>'
    return f'<dl class="lx-facts"><div><dt>Phone</dt><dd><a href="tel:{TEL}">{DISP}</a></dd></div>{addr}<div><dt>Trade</dt><dd>{T.TRADE}</dd></div></dl>'


def home():
    tips = "".join(f'<div class="reveal"><span class="mono">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(T.TIPS))
    body = hero() + f'''
<section class="sec lx-intro"><div class="wrap lx-2">
<div class="reveal"><p class="label">{T.INTRO_LABEL}</p><h2>{T.INTRO_H2}</h2>{facts()}</div>
<div class="reveal">{"".join(f'<p{" class=lede" if i == 0 else ""}>{p}</p>' for i, p in enumerate(T.INTRO))}</div>
</div></section>

<section class="sec lx-tool" id="tool"><div class="wrap">
<div class="lx-head split-h reveal"><div><p class="label">{T.SIG_LABEL}</p><h2>{T.SIG_H2}</h2></div><p class="lede">{T.SIG_LEDE}</p></div>
{T.SIG_HTML}
</div></section>

<section class="sec lx-tips"><div class="wrap">
<div class="lx-head split-h reveal"><div><p class="label">{T.TIPS_LABEL}</p><h2>{T.TIPS_H2}</h2></div><a class="tlink" href="@/{p_blog.SLUG}">{T.TIPS_LINK} {ARROW}</a></div>
<div class="lx-grid">{tips}</div>
<p class="small lx-src">{T.TIPS_SRC}</p>
</div></section>

<section class="sec lx-faq"><div class="wrap split" style="align-items:start">
<div class="reveal"><p class="label">Questions</p><h2>{T.FAQ_H2}</h2>
<a class="post-card lx-post" href="@/{p_blog.SLUG}"><span class="label">From the blog</span><b>{p_blog.H1}</b><p>{T.POST_BLURB}</p><em>Read it {ARROW}</em></a></div>
<div class="reveal">{faq_html(T.FAQ)}</div>
</div></section>
''' + K.cta()
    return {"path": "", "canonical": U, "title": T.TITLE, "meta": T.META, "body": body, "body_class": "is-home", "og": "hero",
            "schema": [crumbs_ld("", [HOME]), faq_ld(T.FAQ)]}


def make_pages():
    out = [home()]
    addr = "".join(f'<div><dt>{l}</dt><dd><address>{a}</address></dd></div>' for l, a in ADDRESS) or f'<div><dt>Where we work</dt><dd>{" &middot; ".join(AREAS)}</dd></div>'
    con = f'''<p class="answer">Call {NAME} at <a href="tel:{TEL}">{DISP}</a>, or send the form.</p>
<dl class="info"><div><dt>Phone</dt><dd><a href="tel:{TEL}">{DISP}</a></dd></div>{addr}</dl>
<h2>Before you call</h2><ul>{"".join(f"<li>{x}</li>" for x in T.BEFORE)}</ul>'''
    out.append(K.page("contact/", "Contact", f"Contact {NAME}", T.CONTACT_LEDE, "Contact", T.CONTACT_TITLE, T.CONTACT_META, con, canonical=canon("contact/"), form_side=True))
    out.append(p_blog.page(K))
    out.append(K.notfound((("Home", ""), ("Contact", "contact/"))))
    return [K.fit(dict(x, body=Q(x["body"])), (f" Call {DISP}.", f" {T.CITY}, Utah.")) for x in out]
