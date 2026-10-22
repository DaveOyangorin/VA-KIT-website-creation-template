"""clean.py: turn a page's main content into clean prose HTML (h2/h3/p/ul/ol/li/blockquote/strong/em/a) for migration.
Use: from clean import clean_main; html, h1, imgs = clean_main(raw_html, base_url)"""
import re, html as H, urllib.parse

DROP = r"<(script|style|svg|noscript|form|iframe|nav|header|footer|button|select|textarea)\b.*?</\1>"
CONTAINERS = [r'<div[^>]+class="[^"]*\bentry-content\b[^"]*"', r'<div[^>]+class="[^"]*\bpost-content\b[^"]*"', r'<article\b', r'<main\b',
              r'<div[^>]+id="content"', r'<div[^>]+class="[^"]*\bpage-content\b[^"]*"']
KEEP = ("h2", "h3", "p", "ul", "ol", "li", "blockquote", "strong", "b", "em", "i", "a", "br")


def _region(raw):
    """The candidate content container with the most text (entry-content, article, main, #content...)."""
    best, best_n = None, 0
    for pat in CONTAINERS:
        for m in re.finditer(pat, raw, re.I):
            seg = raw[m.start():]
            end = re.search(r"<footer\b|<div[^>]+(?:id|class)=\"[^\"]*(?:footer|comments|related-posts|sidebar)[^\"]*\"", seg[1:], re.I)
            seg = seg[:end.start() + 1] if end else seg
            n = len(re.sub(r"<[^>]+>", "", re.sub(r"(?s)<(script|style)\b.*?</\1>", "", seg)))
            if n > best_n: best, best_n = seg, n
    return best if best is not None else raw.split("<body", 1)[-1]


def _tidy(s):
    s = re.sub(r"\s+", " ", s)
    for _ in range(4):
        s = re.sub(r"<p>\s*<p>", "<p>", s)
        s = re.sub(r"</p>\s*</p>", "</p>", s)
        s = re.sub(r"<(li|h2|h3)>\s*<p>(.*?)(?:</p>)?\s*</\1>", r"<\1>\2</\1>", s)
        s = re.sub(r"<p>\s*(<(?:h2|h3|ul|ol)>)", r"\1", s)
        s = re.sub(r"(</(?:h2|h3|ul|ol)>)\s*</p>", r"\1", s)
        s = re.sub(r"<(p|li|h2|h3|strong|em|b|i)>\s*(?:<br>\s*)*</\1>", "", s)
    s = re.sub(r"<p>((?:(?!</?p>).)*?)(?=<p>)", r"<p>\1</p>", s)
    s = re.sub(r"</li>\s*</p>", "</li>", s)
    s = re.sub(r"(?:<br>\s*)+</p>", "</p>", s)
    s = re.sub(r"</p>\s*(?:<br>\s*)+", "</p>", s)
    s = re.sub(r"<p>((?:(?!</?p>|<h).){5,140}\?)\s*</p>", r"<h3>\1</h3>", s)
    s = re.sub(r"(<(?:h2|h3|p|ul|ol|li|blockquote)>)", r"\n\1", s)
    return s.strip()


def clean_main(raw, base=""):
    seg = re.sub(DROP, " ", _region(raw), flags=re.S | re.I)
    seg = re.sub(r"<!--.*?-->", " ", seg, flags=re.S)
    imgs = [urllib.parse.urljoin(base, s) for s in re.findall(r'<img[^>]+(?:data-src|data-lazy-src|src)="([^"]+)"', seg)]
    h1 = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", seg, re.S | re.I)
    if m: h1 = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip()
    seg = re.sub(r"<h1[^>]*>.*?</h1>", " ", seg, flags=re.S | re.I)
    seg = re.sub(r"<(/?)h[456][^>]*>", r"<\1h3>", seg, flags=re.I)

    def tag(m):
        close, name = m.group(1), m.group(2).lower()
        if name not in KEEP: return "\n"
        if name == "a" and not close:
            href = re.search(r'href="([^"]*)"', m.group(0))
            return f'<a href="{href.group(1)}">' if href else ""
        if name == "a" and close: return "</a>"
        return f"<{close}{name}>"
    seg = re.sub(r"<(/?)([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>", tag, seg)
    out = []
    for line in re.split(r"\n+", seg):
        t = line.strip()
        if not t: continue
        if not re.match(r"</?(h2|h3|p|ul|ol|li|blockquote)\b", t) and len(re.sub(r"<[^>]+>", "", t)) > 2:
            t = f"<p>{t}</p>"
        out.append(t)
    return _tidy("\n".join(out)), h1, imgs
