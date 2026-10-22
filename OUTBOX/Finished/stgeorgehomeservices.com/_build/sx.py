"""sx.py: structure-preserving extractor for stgeorgehomeservices.com (clean, semantic static markup).
extract(key) -> dict(h1, lede, body, imgs, faqs)
- body keeps headings, paragraphs, lists, tables, footnote <sup>s, the numbered source lists and <details> FAQs;
- drops the page hero (we draw our own), call-to-action bands, the repeated services band, forms, video players;
- imgs: the page's own photos (brand/ hero renders and illustration-* lighting renders are left out), with alt text;
- internal links become @/ paths (no trailing slash on this site)."""
import html, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
KEEP = {"h2", "h3", "h4", "p", "ul", "ol", "li", "table", "thead", "tbody", "tfoot", "tr", "th", "td", "caption", "blockquote", "strong", "em", "b", "i", "a", "sup", "sub",
        "br", "dl", "dt", "dd", "details", "summary", "small", "cite", "abbr", "code", "figcaption"}
DROPSEC = re.compile(r'class="[^"]*\b(phero|hero|closing|band-sand|svc|hero__actions|article__house|cta|callout-call|book|form|video|player|crumbs|breadcrumb|skip)\b', re.I)
SKIPIMG = re.compile(r"/images/brand/|illustration-|-m\.webp$|poster-|video-poster", re.I)


def _strip_blocks(s, tag_rx):
    """Remove whole elements whose opening tag matches tag_rx (balanced by tag name)."""
    out, i = [], 0
    for m in list(re.finditer(r"<(section|div|aside|header|footer|nav|form|figure|picture|video|button|svg|template|dialog|iframe)\b[^>]*>", s)):
        pass
    while True:
        m = re.search(tag_rx, s[i:])
        if not m: out.append(s[i:]); break
        st = i + m.start(); name = m.group(1)
        out.append(s[i:st])
        depth, j = 0, st
        for t in re.finditer(r"<(/?)" + name + r"\b[^>]*?(/?)>", s[st:]):
            if t.group(2): continue
            depth += -1 if t.group(1) else 1
            if depth == 0: j = st + t.end(); break
        else:
            j = len(s)
        i = j
    return "".join(out)


def extract(key):
    raw = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    main = raw[raw.find("<main"):raw.find("</main>")] if "<main" in raw else raw
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    h1 = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else ""
    ph = re.search(r'<(?:div|section|header)[^>]*class="[^"]*\bphero\b.*?</header>', main, re.S)
    lede = ""
    if ph:
        ps = [re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", p)).strip() for p in re.findall(r"<p[^>]*>(.*?)</p>", ph.group(0), re.S)]
        ps = [p for p in ps if len(p) > 40 and "(435)" not in p]
        lede = ps[0] if ps else ""
    imgs = []
    for tag in re.findall(r"<img\b[^>]*>", main):
        src = re.search(r'\ssrc="([^"]+)"', tag); alt = re.search(r'alt="([^"]*)"', tag)
        if not src: continue
        u = html.unescape(src.group(1))
        if "url=" in u: u = __import__("urllib.parse").parse.unquote(re.search(r"url=([^&]+)", u).group(1))
        if SKIPIMG.search(u) or "/images/" not in u: continue
        name = u.split("/images/", 1)[1].replace("/", "__")
        name = re.sub(r"\?.*$", "", name)
        if name not in [n for n, a in imgs]: imgs.append((name, html.unescape(alt.group(1)) if alt else ""))
    s = main
    s = re.sub(r"(?s)<(script|style|noscript|template)\b.*?</\1>", "", s)
    s = re.sub(r"(?s)<!--.*?-->", "", s)
    # drop the hero and the generic bands
    s = _strip_blocks(s, r'<(section|div|header|aside|nav|form|ul|ol)\b[^>]*class="[^"]*\b(?:phero|hero|closing|hero__actions|article__house|crumbs|breadcrumb|cta|svc|townindex)\b[^"]*"[^>]*>')
    s = _strip_blocks(s, r"<(form|video|picture|figure|button|svg|iframe|nav|dialog)\b[^>]*>")
    s = re.sub(r"<img\b[^>]*>", "", s)
    s = re.sub(r"(?s)<h1\b.*?</h1>", "", s)

    def tag(m):
        close, name, attrs = m.group(1), m.group(2).lower(), m.group(3) or ""
        if name not in KEEP: return ""
        if close: return f"</{name}>"
        if name == "a":
            h = re.search(r'href="([^"]*)"', attrs)
            href = html.unescape(h.group(1)) if h else ""
            if href.startswith("/") and not href.startswith("//"):
                href = "@/" + href.strip("/") + ("/" if href.strip("/") and "#" not in href and "." not in href.split("/")[-1] else "")
                if href == "@//": href = "@/"
            ext = ' rel="noopener"' if href.startswith("http") else ""
            return f'<a href="{html.escape(href, quote=True)}"{ext}>' if href else "<a>"
        if name in ("th", "td"):
            keep = " ".join(x for x in re.findall(r'\b(?:colspan|rowspan|scope)="[^"]*"', attrs))
            return f"<{name}{' ' + keep if keep else ''}>"
        if name == "details": return "<details>"
        idm = re.search(r'id="((?:src|source|fn|note)[^"]*)"', attrs)
        if idm and name in ("li", "p", "ol", "h2", "h3", "dt"): return f'<{name} id="{idm.group(1)}">'
        return f"<{name}>"
    s = re.sub(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b([^>]*)>", tag, s)
    s = re.sub(r"<a>(.*?)</a>", r"\1", s, flags=re.S)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"<(p|li|h2|h3|h4|td|th|dd|dt|summary)>\s*</\1>", "", s)
    s = re.sub(r"<(ul|ol|dl)>\s*</\1>", "", s)
    for _ in range(3): s = re.sub(r"<(ul|ol|dl|table|tbody|thead|tr|details)>\s*</\1>", "", s)
    s = re.sub(r"\s*(</?(?:h2|h3|h4|p|ul|ol|li|table|thead|tbody|tr|blockquote|details|summary|dl|dt|dd)>)\s*", r"\1", s)
    s = re.sub(r"(</(?:h2|h3|h4|p|ul|ol|table|blockquote|details|dl)>)", r"\1\n", s)
    s = s.replace("<table>", '<div class="tbl"><table>').replace("</table>", "</table></div>")
    # FAQs written as <details>
    faqs = [(re.sub(r"<[^>]+>", "", q).strip(), a.strip()) for q, a in re.findall(r"<details><summary>([^<]*\?)</summary>(.*?)</details>", s, re.S)]
    if len(faqs) >= 2: s = re.sub(r"<details><summary>[^<]*\?</summary>.*?</details>", "", s, flags=re.S)
    else: faqs = []
    return {"h1": html.unescape(h1), "lede": html.unescape(lede), "body": s.strip(), "imgs": imgs, "faqs": faqs}


if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")
    for k in sys.argv[1:]:
        d = extract(k); print("=====", k, "|", d["h1"], "|", d["lede"][:120], "| imgs", d["imgs"][:4], "| faqs", len(d["faqs"])); print(d["body"][:2500])
