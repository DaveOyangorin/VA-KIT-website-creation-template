"""sfclean.py: site-specific cleanup of migrated sfrutah.com page text (site-builder export from the Wayback captures).
Drops the repeated service-teaser grid ("... MORE"), the quote-form boilerplate and testimonial stubs; turns "●" paragraphs into
lists; pulls the built-in FAQ list out as (question, answer) pairs."""
import re, html
JUNK = re.compile(r"MORE\s*$|Mbl Touch Call|^Get you ?R$|^FREE Quote$|Don't let more damage|^Testimonials$|MORE GOOGLE REVIEWS|^Submit$|Please click on the checkbox|"
                  r"^Full Name|^Email Address|^Phone Number|^City or town|^Message$|COMING SOON|^Contact Now!?$|^Toggle navigation|^Read More|^Call Now!?$", re.I)


def txt(b): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()


CLAIM = re.compile(r"15\+? ?years|over 15|fifteen years|premier|most trusted|Utah.s best|the best |best solutions|top[- ]rated|top choice|strong guarantee|certified|#1|"
                   r"decades of|highest[- ]quality|unmatched|industry-leading|locally made|top of the line|top-of-the-line|BEST FOUNDATION", re.I)
SENT = re.compile(r"(?<=[.!?])\s+")


def scrub(b):
    """Drop sentences carrying unconfirmed claims; drop the block if nothing is left."""
    if not b.startswith(("<p>", "<li>")): return "" if CLAIM.search(txt(b)) else b
    tag = b[1:b.index(">")]
    inner = b[len(tag) + 2:-(len(tag) + 3)]
    parts = [x for x in SENT.split(inner) if not CLAIM.search(txt(x))]
    out = " ".join(parts).strip()
    return f"<{tag}>{out}</{tag}>" if len(txt(out)) > 2 else ""


def clean(s):
    s = re.sub(r"<(h2|h3)>([^<]*(?:<br>[^<]*)*)</p>", r"<></>", s)
    s = re.sub(r"<p>([^<]*)</h[23]>", r"<p></p>", s)
    faqs = []
    for m in re.finditer(r"(?s)<ul>((?:\s*<li>\s*<h3>.*?</li>)+)\s*</ul>", s):
        for q, a in re.findall(r"(?s)<li>\s*<h3>(.*?)</h3>(.*?)</li>", m.group(1)):
            a = re.sub(r"<p>(\s|&nbsp;)*</p>", "", a).strip()
            if txt(q) and txt(a) and not CLAIM.search(txt(a)): faqs.append((txt(q), a))
    s = re.sub(r"(?s)<ul>((?:\s*<li>\s*<h3>.*?</li>)+)\s*</ul>", "", s)
    blocks = re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s)
    out = []
    for b in blocks:
        b = b.replace("&nbsp;", " ")
        t = txt(b)
        if len(t) < 3 or JUNK.search(t): continue
        if b.startswith("<p>"):
            b = re.sub(r"^<p>(?:\s|<br>)*", "<p>", b)
            t2 = txt(b)
            if t2.startswith("●"):
                out.append("<li>" + t2.lstrip("● ").strip() + "</li>"); continue
        out.append(b)
    # re-join paragraph fragments split by old link spans ("From minor" / "foundation crack repair" / "in Utah" / "to basement ...")
    merged = []
    for b in out:
        if merged and b.startswith("<p>") and merged[-1].startswith("<p>") and not re.search(r"[.!?:”\"]\s*$", txt(merged[-1])) and re.match(r"[a-z]", txt(b)):
            merged[-1] = merged[-1][:-4].rstrip() + " " + b[3:]
        else:
            merged.append(b)
    out = [x for x in (scrub(b) for b in merged) if x]
    # wrap runs of <li>
    s = "\n".join(out)
    s = re.sub(r"((?:<li>.*?</li>\n?)+)", lambda m: "<ul>" + m.group(1).replace("\n", "") + "</ul>\n", s)
    blocks = re.findall(r"(?s)<(?:h2|h3|p|ul|ol|blockquote)>.*?</(?:h2|h3|p|ul|ol|blockquote)>", s)
    def head(b): return b.startswith(("<h2>", "<h3>"))
    # teaser titles left behind: a heading followed by another heading
    keep = [b for i, b in enumerate(blocks) if not (head(b) and i + 1 < len(blocks) and head(blocks[i + 1]))]
    while keep and head(keep[-1]): keep.pop()
    return "\n".join(keep), faqs
