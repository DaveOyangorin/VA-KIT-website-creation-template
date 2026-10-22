"""clean.py: turn a page's main content into clean prose HTML (h2/h3/p/ul/ol/li/blockquote/strong/em/a) for migration.
Use: from clean import clean_main; html, h1, imgs = clean_main(raw_html, base_url)"""
import re, html as H, urllib.parse

DROP = r"<(script|style|svg|noscript|form|iframe|nav|header|footer|button|select|textarea)\b.*?</\1>"
CONTAINERS = [r'<div[^>]+class="[^"]*\bentry-content\b[^"]*"', r'<div[^>]+class="[^"]*\bpost-content\b[^"]*"', r'<article\b', r'<main\b',
              r'<div[^>]+id="content"', r'<div[^>]+class="[^"]*\bpage-content\b[^"]*"']


def _region(raw):
    for pat in CONTAINERS:
        m = re.search(pat, raw, re.I)
        if m:
            seg = raw[m.start():]
            end = re.search(r"<footer\b|<div[^>]+(?:id|class)=\"[^\"]*(?:footer|comments|related-posts|sidebar)[^\"]*\"", seg, re.I)
            return seg[:end.start()] if end else seg
    b = raw.split("<body", 1)[-1]
    return b


def clean_main(raw, base=""):
    seg = re.sub(DROP, " ", _region(raw), flags=re.S | re.I)
    seg = re.sub(r"<!--.*?-->", " ", seg, flags=re.S)
    imgs = [urllib.parse.urljoin(base, s) for s in re.findall(r'<img[^>]+(?:data-src|data-lazy-src|src)="([^"]+)"', seg)]
    h1 = ""
    m = re.search(r"<h1[^>]*>(.*?)</h1>", seg, re.S | re.I)
    if m: h1 = re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", "", m.group(1)))).strip()
    seg = re.sub(r"<h1[^>]*>.*?</h1>", " ", seg, flags=re.S | re.I)
    seg = re.sub(r"<h[56][^>]*>", "<h3>", seg, flags=re.I); seg = re.sub(r"</h[56]>", "</h3>", seg, flags=re.I)
    seg = re.sub(r"<h4[^>]*>", "<h3>", seg, flags=re.I); seg = re.sub(r"</h4>", "</h3>", seg, flags=re.I)

    def keep_a(m):
        href = re.search(r'href="([^"]*)"', m.group(0))
        return f'<a href="{href.group(1)}">' if href else ""
    seg = re.sub(r"<a\b[^>]*>", keep_a, seg, flags=re.I)
    seg = re.sub(r"<(/?)(h2|h3|p|ul|ol|li|blockquote|strong|b|em|i|a|br)\b[^>]*>", lambda m: f"<{m.group(1)}{m.group(2).lower()}>" if m.group(2).lower() != "a" or m.group(1) else m.group(0), seg, flags=re.I)
    seg = re.sub(r"<(?!/?(?:h2|h3|p|ul|ol|li|blockquote|strong|b|em|i|a|br)\b)[^>]+>", "\n", seg, flags=re.I)
    seg = re.sub(r"<(p|li|h2|h3|strong|em|b|i)>\s*</\1>", "", seg)
    # wrap loose text lines as paragraphs
    out = []
    for line in re.split(r"\n+", seg):
        t = line.strip()
        if not t: continue
        if not re.match(r"<(h2|h3|p|ul|ol|li|/ul|/ol|blockquote|/blockquote|/li|/p|/h2|/h3)", t) and len(re.sub(r"<[^>]+>", "", t)) > 2:
            t = f"<p>{t}</p>"
        out.append(t)
    s = "\n".join(out)
    s = re.sub(r"<p>\s*(<(?:h2|h3|ul|ol|li|blockquote)>)", r"\1", s)
    s = re.sub(r"(</(?:h2|h3|ul|ol|li|blockquote)>)\s*</p>", r"\1", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"(<(?:h2|h3|p|ul|ol|li|blockquote)>)", r"\n\1", s)
    return s.strip(), h1, imgs
