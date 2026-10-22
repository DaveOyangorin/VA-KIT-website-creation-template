"""pagekit.py: shared page furniture for the Novarte drafts (v2). Each site's pages.py imports this, sets its own concept
(home page, drawings, CSS) and calls page() for inner pages. Everything site-specific comes from cfg:
  cfg.NAV       [(label, path)]            main nav links (after the Services dropdown)
  cfg.SVC       [(path, label, icon_or_None)]  services for the dropdown / grids
  cfg.CTA_PATH  path of the contact / quote page;  cfg.CTA_LABEL  button text ("Free Estimate")
  cfg.PHONES    [(label, display, tel)]    one or more phones; first is primary
  cfg.ADDRESS   [(label, html)] or []      office lines (empty for service-area businesses)
  cfg.AREAS     [str]                      areas served (words, for service-area businesses)
  cfg.HOURS, cfg.EMAIL, cfg.SOCIAL [(label, url)], cfg.BLURB (footer sentence), cfg.LOGO (img name)
  cfg.SIDE_HTML optional extra html for the sidebar card;  cfg.CTA_TITLE / cfg.CTA_TEXT
"""
import html, re
from engine import img, crumbs_html, crumbs_ld, faq_html, faq_ld, canon
import cfg as C

ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25 11.4 11.4 0 0 0 3.6.57 1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1z"/></svg>'
STAR = '<svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 1.5l2.6 5.4 5.9.8-4.3 4.1 1 5.8L10 14.8l-5.2 2.8 1-5.8L1.5 7.7l5.9-.8z" fill="currentColor"/></svg>'
HOME = ("Home", "")


def Q(s):
    return re.sub(r'href=(@/[^\s>"]+)>', r'href="\1">', s)


def P1():
    return C.PHONES[0]


def header():
    lab, ph, tel = P1()
    drop = "".join(f'<a href="@/{p}">{img(ic, "") if ic else ""}<span>{l}</span></a>' for p, l, ic in C.SVC)
    nav = "".join(f'<li><a href="@/{p}">{l}</a></li>' for l, p in C.NAV)
    mob = "".join(f'<a href="@/{p}">{l}</a>' for p, l, ic in C.SVC[:6]) + "".join(f'<a href="@/{p}">{l}</a>' for l, p in C.NAV)
    calls = "".join(f'<a class="btn{" ghost" if i else ""}" href="tel:{t}">{"Call " if not i else ""}{l + " " if len(C.PHONES) > 1 else ""}{d}</a>' for i, (l, d, t) in enumerate(C.PHONES))
    return Q(f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header"><div class="wrap">
<a class="brand" href="@/" aria-label="{C.NAME} home">{img(C.LOGO, C.NAME, lazy=False)}</a>
<nav class="nav" aria-label="Main"><ul>
<li><details><summary>{getattr(C, "SVC_LABEL", "Services")}</summary><div class="drop">{drop}</div></details></li>{nav}</ul></nav>
<div class="head-cta"><a class="head-phone" href="tel:{tel}">{PHONE}<span>{ph}</span></a><a class="btn" href="@/{C.CTA_PATH}">{C.CTA_LABEL}</a></div>
<details class="menu"><summary aria-label="Open menu"><span></span></summary><div class="menu-panel">
<a href="@/">Home</a>{mob}<a href="@/{C.CTA_PATH}">{C.CTA_LABEL}</a>{calls}</div></details>
</div></header>''')


def footer():
    phones = "".join(f'<p><span class="small">{l}</span><br><a class="fph" href="tel:{t}">{d}</a></p>' for l, d, t in C.PHONES)
    addr = "".join(f'<p><span class="small">{l}</span><br><address>{a}</address></p>' for l, a in C.ADDRESS)
    soc = " &middot; ".join(f'<a href="{u}" rel="noopener">{l}</a>' for l, u in C.SOCIAL)
    svc = "".join(f'<li><a href="@/{p}">{l}</a></li>' for p, l, ic in C.SVC[:8])
    areas = " &middot; ".join(C.AREAS)
    lab, ph, tel = P1()
    return Q(f'''<footer class="site-footer"><div class="wrap">
<div class="foot">
<div class="f-brand"><span class="flogo">{img(C.LOGO, C.NAME + " logo")}</span><p>{C.BLURB}</p>{f'<p class="small">{soc}</p>' if soc else ""}</div>
<div><h3>{getattr(C, "SVC_LABEL", "Services")}</h3><ul>{svc}</ul></div>
<div><h3>Contact</h3>{phones}{f'<p><a href="mailto:{C.EMAIL}">{C.EMAIL}</a></p>' if C.EMAIL else ""}{f'<p class="small">{C.HOURS}</p>' if C.HOURS else ""}</div>
<div><h3>{"Office" if C.ADDRESS else "Where we work"}</h3>{addr or f"<p>{areas}</p>"}</div>
</div>
{f'<p class="fareas"><b>Serving</b> {areas}</p>' if C.ADDRESS and areas else ""}
<div class="fbottom"><span>&copy; 2026 {C.NAME}</span><span>{" &middot; ".join(f'<a href="@/{p}">{l}</a>' for l, p in C.NAV)}</span></div></div></footer>
<div class="callbar"><a href="tel:{tel}">{PHONE} Call</a><a href="@/{C.CTA_PATH}">{C.CTA_LABEL}</a></div>''')


def cta(title=None, text=None):
    title = title or C.CTA_TITLE; text = text or C.CTA_TEXT
    ph = "".join(f'<a class="office" href="tel:{t}"><small>{l}</small><b>{d}</b></a>' for l, d, t in C.PHONES)
    return f'''<section class="cta"><div class="wrap cta-in">
<div><p class="label">{C.CTA_LABEL}</p><h2>{title}</h2><p class="lede">{text}</p><a class="btn accent" href="@/{C.CTA_PATH}">{C.CTA_LABEL} {ARROW}</a></div>
<div class="offices">{ph}{f'<p class="cta-hours">{C.HOURS}</p>' if C.HOURS else ""}</div></div></section>'''


def phero(trail, h1, lede, tag, image=None, alt="", art=None):
    """Inner-page hero: full-bleed photo (or the dark brand ground with the site's drawn art) under a heavy display title."""
    lab, ph, tel = P1()
    bg = f'<div class="pf-bg">{img(image, alt, priority=True)}</div>' if image else ""
    right = f'<div class="ph-art">{art}</div>' if (art and not image) else ""
    return f'''<section class="phero-full{"" if image else " no-photo"}">{bg}<div class="wrap ph-in{" has-art" if right else ""}"><div class="ph-text">{crumbs_html(trail)}<p class="label">{tag}</p><h1>{h1}</h1>{f'<p class="lede">{lede}</p>' if lede else ""}
<div class="btn-row"><a class="btn accent" href="@/{C.CTA_PATH}">{C.CTA_LABEL} {ARROW}</a><a class="btn ghost" href="tel:{tel}">{PHONE} {ph}</a></div></div>{right}</div></section>'''


def side(extra=""):
    ph = "".join(f'<div><dt>{l}</dt><dd><a href="tel:{t}">{d}</a></dd></div>' for l, d, t in C.PHONES)
    return f'''<aside class="sv-side"><div class="side-card"><p class="label">{C.CTA_LABEL}</p><p class="sc-t">{getattr(C, "SIDE_TITLE", C.CTA_TITLE)}</p>{getattr(C, "SIDE_HTML", "")}
<a class="btn" href="@/{C.CTA_PATH}">{C.CTA_LABEL} {ARROW}</a><dl>{ph}{f'<div><dt>Hours</dt><dd>{C.HOURS}</dd></div>' if C.HOURS else ""}</dl></div>{extra}</aside>'''


def form(title=None, fields=None, msg_label="How can we help?"):
    title = title or C.CTA_LABEL
    extra = "".join(f'<label for="f-{n}">{l}<input id="f-{n}" name="{n}"></label>' for n, l in (fields or []))
    return f'''<form class="form" method="post" action=""><h3>{title}</h3>
<div class="row"><label for="f-name">Name *<input id="f-name" name="name" autocomplete="name" required></label><label for="f-phone">Phone *<input id="f-phone" type="tel" name="phone" autocomplete="tel" required></label></div>
<label for="f-email">Email *<input id="f-email" type="email" name="email" autocomplete="email" required></label>{extra}
<label for="f-msg">{msg_label}<textarea id="f-msg" name="message"></textarea></label>
<button class="btn" type="submit">Send {ARROW}</button></form>'''


def page(path, label, h1, lede, tag, title, meta, content, image=None, alt="", art=None, intro="", crumbs=None, faqs=None, form_side=False,
         schema=None, canonical=None, sitemap=True, robots=None, og=None, ogtype=None):
    trail = [HOME] + (crumbs or []) + [(label, path)]
    faqs = faqs or []
    main = (f'<p class="answer">{intro}</p>' if intro else "") + content + (f"<h2>Common questions</h2>{faq_html(faqs)}" if faqs else "")
    right = f'<div class="form-col">{form()}</div>' if form_side else side()
    body = phero(trail, h1, lede, tag, image, alt, art) + f'''
<section class="sec"><div class="wrap sv-grid"><article class="prose">{main}</article>{right}</div></section>''' + ("" if form_side else cta())
    pg = {"path": path, "canonical": canonical or canon(path), "title": title, "meta": meta, "body": body, "og": og or image,
          "schema": [crumbs_ld(path, trail)] + (schema or []) + ([faq_ld(faqs)] if faqs else [])}
    if ogtype: pg["ogtype"] = ogtype
    if not sitemap: pg["sitemap"] = False
    if robots: pg["robots"] = robots
    return pg


def svc_schema(path, name, area):
    return [{"@type": "Service", "@id": canon(path) + "#service", "name": name, "provider": {"@id": C.U + "#business"}, "areaServed": {"@type": "City", "name": area}}]


def fit(pg, adds):
    for add in adds:
        if len(html.unescape(pg["meta"])) < 150 and len(html.unescape(pg["meta"] + add)) <= 160 and add.strip(" .") not in pg["meta"]:
            pg["meta"] += add
    return pg


def notfound(links=(("Services", "services/"),)):
    lab, ph, tel = P1()
    body = phero([HOME, ("Not found", "404.html")], "This page isn&rsquo;t here.", f"Try the links below, or call {ph}.", "404") + \
        '<section class="sec"><div class="wrap"><p>' + " &nbsp; ".join(f'<a class="tlink" href="@/{p}">{l} {ARROW}</a>' for l, p in links) + "</p></div></section>"
    return {"path": "404.html", "title": f"Page Not Found | {C.NAME}"[:60], "meta": f"This page was not found. See {C.NAME}'s services or call {ph} to talk to the team about your project. We're glad to help."[:160],
            "body": body, "robots": "noindex, follow", "sitemap": False}
