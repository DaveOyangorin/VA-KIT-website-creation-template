"""fx.py: pulls the client's own text out of the Framer pages (src/pages/<key>.html) as clean blocks.
  blocks(key) -> [(tag, inner_html)]  tags: h1 h2 h3 h4 p li ; stops at the site-wide footer CTA ("Protect What Matters Most")."""
import html, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
STOP = ("Protect What Matters Most", "Learn About More Utah Pests")


def blocks(key):
    raw = open(os.path.join(HERE, "src", "pages", key + ".html"), encoding="utf-8").read()
    raw = re.sub(r"(?s)<(script|style|svg|noscript)\b.*?</\1>", "", raw)
    out, seen = [], set()
    for tag, inner in re.findall(r"(?s)<(h1|h2|h3|h4|p|li)\b[^>]*>(.*?)</\1>", raw):
        inner = re.sub(r"(?s)<(?!/?(?:strong|b|em|i|a)\b)[^>]+>", "", inner)
        inner = re.sub(r"<a\b[^>]*>(.*?)</a>", r"\1", inner, flags=re.S)
        inner = re.sub(r"<(/?)(?:b)>", r"<\1strong>", re.sub(r'<(strong|em|i)\b[^>]*>', r"<\1>", inner))
        t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", inner))).strip()
        if not t: continue
        if any(t.startswith(s) for s in STOP): break
        if t in seen: continue
        seen.add(t)
        out.append((tag, re.sub(r"\s+", " ", inner).strip()))
    return out
