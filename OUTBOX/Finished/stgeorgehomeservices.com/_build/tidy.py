"""tidy.py: generic cleanup of migrated page text for kit2 sites.
  tidy(s, trail=True, claims=None, stop=()) -> html
- drops "click here / read more / learn more" sentences, empty blocks and CTA-only lines;
- drops sentences matching the site's CLAIMS regex (unconfirmed claims);
- short label paragraphs become h3; old H2s become H3 (the page's own headings carry the outline);
- stops at the first block whose text starts with any of `stop` (footer/CTA boilerplate);
- internal @/ links normalised to the site's slash style."""
import re, html

SCRUB = re.compile(r"\s*(?:[^.<>]*?\b(?:Click (?:on|here)|Read more|To learn more|Learn more|click on this link|on the following link)\b[^.<>]*(?:\.|$))", re.I)
CTA = re.compile(r"^(Get|Schedule|Book|Call|Contact|Talk|Request|Ask|See|View|Find|Start|Click|Read More|Learn More|Download|Submit|Send)\b[^.]{0,60}[!.]?$", re.I)
SENT = re.compile(r"(?<=[.!?])\s+")


def txt(b): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()


def mend(s):
    """Repair site-builder markup split around inline links: headings broken across a <p>, and sentence fragments
    ("dealing with" / <a>water damage</a> / ", which is why") re-joined into one paragraph."""
    s = re.sub(r"<(h2|h3)>([^<]*)</p>\s*([^<]{0,3}?)\s*<p>([^<]*)</\1>", lambda m: f"<{m.group(1)}>{m.group(2)}{m.group(3).strip()}{m.group(4)}</{m.group(1)}>", s)
    s = re.sub(r"<(h2|h3)>([^<]*)</p>", r"<\1>\2</\1>", s)
    blocks = re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s)
    out = []
    for b in blocks:
        if out and b.startswith("<p>") and out[-1].startswith("<p>"):
            prev, cur = txt(out[-1]), txt(b)
            link_only = re.fullmatch(r"<p>\s*<a [^>]*>[^<]*</a>\s*</p>", b) is not None
            if prev and cur and not re.search(r"[.!?:”\")]$", prev) and (link_only or re.match(r"[a-z,.;:)’']", cur)):
                sep = "" if re.match(r"[,.;:)]", cur) else " "
                out[-1] = out[-1][:-4].rstrip() + sep + b[3:].lstrip()
                continue
        out.append(b)
    return "\n".join(out)


def tidy(s, trail=True, claims=None, stop=(), skip=()):
    s = mend(s.replace("&nbsp;", " "))
    out = []
    for b in re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s):
        t = txt(b)
        if any(t.startswith(x) for x in stop): break
        if len(t) < 3 or any(t.lower() == x.lower() for x in skip): continue
        if b.startswith("<p>") and (re.fullmatch(r"<p>(?:\s*<a [^>]*>[^<]*</a>\s*)+</p>", b) or re.match(r"Home\s*/", t)): continue
        if b.startswith(("<p>", "<li>")):
            b = SCRUB.sub("", b)
            if claims:
                tag = b[1:b.index(">")]; inner = b[len(tag) + 2:-(len(tag) + 3)]
                inner = " ".join(x for x in SENT.split(inner) if not claims.search(txt(x)))
                b = f"<{tag}>{inner.strip()}</{tag}>"
            t = txt(b)
            if len(t) < 3 or CTA.match(t): continue
            if len(t) < 44 and not re.search(r"[.!?:,;]$", t) and not t[0].isdigit() and "$" not in t and b.startswith("<p>"):
                b = f"<h3>{t}</h3>"
        elif b.startswith(("<ul>", "<ol>")) and claims:
            items = [i for i in re.findall(r"(?s)<li>(.*?)</li>", b) if not claims.search(txt(i))]
            if not items: continue
            b = b[:4] + "".join(f"<li>{i}</li>" for i in items) + b[-5:]
        elif claims and claims.search(t):
            continue
        out.append(b)
    def head(b): return b.startswith(("<h2>", "<h3>"))
    out = [b for i, b in enumerate(out) if not (head(b) and i + 1 < len(out) and head(out[i + 1]))]
    while out and head(out[-1]): out.pop()
    s = "\n".join(out).replace("<h2>", "<h3>").replace("</h2>", "</h3>")
    s = re.sub(r'href="@/([^"#]*?)/?"', lambda m: (f'href="@/{m.group(1).strip("/")}/"' if m.group(1).strip("/") else 'href="@/"'), s)
    return s
