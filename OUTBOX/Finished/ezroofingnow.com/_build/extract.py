"""Pulls the real content out of the old WordPress (Genesis + Genesis Blocks) pages.

  python -I extract.py <pages_dir> <out.json>

For every page it keeps: URL, title, meta description, canonical, dates, the H1,
the body as clean HTML (headings, paragraphs, lists, tables, images, links),
accordion FAQs and testimonials. Page-builder wrappers, forms, buttons and the
blocks repeated on every page are dropped.
"""
import sys, os, re, json, html, glob
from html.parser import HTMLParser

SITE = "https://ezroofingnow.com"
KEEP = {"h1", "h2", "h3", "h4", "h5", "h6", "p", "ul", "ol", "li", "a", "strong", "em", "img", "table", "thead",
        "tbody", "tr", "th", "td", "blockquote", "br", "figure", "figcaption"}
RENAME = {"b": "strong", "i": "em"}
SKIP_TAGS = {"script", "style", "noscript", "svg", "form", "iframe", "select", "textarea", "button", "nav", "video", "header", "footer"}
SKIP_CLASS = re.compile(r"elementor-widget-(?:button|nav-menu|breadcrumbs|divider|spacer|social-icons|theme-site-logo|form|shortcode|html|icon|icon-box-button|theme-post-featured-image|google_maps|video|lottie|counter|search-form)(?![\w-])|e-n-accordion-item-title-icon|fusion-button|gform_wrapper|fusion-separator|fusion-sharing-box|related-posts|fusion-meta-info|"
                        r"fusion-pagination|fusion-blog-shortcode|fusion-recent-posts|awb-toc|fusion-post-cards|fusion-social|"
                        r"fusion-breadcrumb|fusion-page-title-bar|screen-reader-text|fusion-image-carousel|fusion-rollover|"
                        r"single-navigation|about-author|fusion-author|comments|fusion-flip-box-back|wp-block-buttons|gb-block-testimonial|wp-block-spacer|"
                        r"tces-js-style-encoded|wpv-pagination|entry-meta|entry-footer|sharedaddy|gf_browser|gfield|ginput|sharedaddy|jp-relatedposts|wpcf7|post-navigation|adjacent-entry-pagination")
VOID = {"img", "br", "hr", "input", "meta", "link", "source", "wbr", "col", "area", "base", "embed", "param", "track"}
BOILER = re.compile(r"^(get a free quote today|what our clients are saying|roofing services with american roofing|latest articles|"
                    r"free consultation|recent posts|related posts|share this|leave a comment|our services|get free consultation|"
                    r"schedule your free roof evaluation|request a free quote|schedule your free inspection now)\b", re.I)


class Node:
    __slots__ = ("tag", "attrs", "kids", "parent")
    def __init__(self, tag, attrs, parent):
        self.tag, self.attrs, self.kids, self.parent = tag, dict(attrs), [], parent


class Tree(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root", {}, None); self.cur = self.root
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur); self.cur.kids.append(n)
        if tag not in VOID: self.cur = n
    def handle_startendtag(self, tag, attrs):
        self.cur.kids.append(Node(tag, attrs, self.cur))
    def handle_endtag(self, tag):
        n = self.cur
        while n is not None and n.tag != tag: n = n.parent
        if n is not None and n.parent is not None: self.cur = n.parent
    def handle_data(self, data):
        self.cur.kids.append(data)


def cls(n): return n.attrs.get("class") or ""


def text(n):
    if isinstance(n, str): return n
    return "".join(text(k) for k in n.kids)


def find_all(n, pred, out=None):
    out = [] if out is None else out
    if isinstance(n, Node):
        if pred(n): out.append(n)
        for k in n.kids: find_all(k, pred, out)
    return out


def norm_link(href):
    if not href: return None
    href = href.strip()
    if href.startswith(("tel:", "mailto:", "#")): return href
    h = re.sub(r"^https?://(www\.)?ezroofingnow\.com", "", href)
    if h != href or href.startswith("/"):
        h = h.split("?")[0]
        if "/wp-content/" in h: return SITE + h
        if not h.endswith("/") and "." not in h.rsplit("/", 1)[-1]: h += "/"
        return "@/" + h.lstrip("/")
    return href


def img_src(n):
    for k in ("data-orig-src", "data-lazy-src", "data-src", "src"):
        v = n.attrs.get(k)
        if v and not v.startswith("data:"): return v
    return None


def ser(n, imgs):
    if isinstance(n, str):
        return html.escape(n, quote=False)
    tag = RENAME.get(n.tag, n.tag)
    if tag in SKIP_TAGS or SKIP_CLASS.search(cls(n)) or "fusion-testimonials" in cls(n) or "fusion-accordian" in cls(n):
        return ""
    if n.attrs.get("aria-hidden") == "true" or "display:none" in (n.attrs.get("style") or "").replace(" ", ""): return ""
    if "e-n-accordion" == cls(n).strip():
        return ""  # FAQs are pulled out separately
    if re.search(r"elementor-widget-(?:gallery|n-carousel|image-carousel|image-gallery)(?![\w-])", cls(n)):
        items, seen_src = [], set()
        for im in find_all(n, lambda x: x.tag == "img" or (x.tag == "a" and "e-gallery-item" in cls(x))):
            src = im.attrs.get("href") if im.tag == "a" else img_src(im)
            if not src or not re.search(r"\.(jpe?g|png|webp|avif)$", src.split("?")[0], re.I): continue
            src = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", src.split("?")[0])
            if src in seen_src or re.search(r"logo|icon|star", src, re.I): continue
            seen_src.add(src); imgs.append(src)
            items.append(f'<img data-src="{html.escape(src)}" alt="{html.escape(im.attrs.get("alt") or "", quote=True)}">')
        return '<div class="gal">' + "".join(items) + "</div>" if items else ""
    if re.search(r"(^|\s)fusion-gallery(\s|$)", cls(n)):
        items = []
        for a in find_all(n, lambda x: x.tag == "a" and "fusion-lightbox" in cls(x)):
            href = a.attrs.get("href") or ""
            if not re.search(r"\.(jpe?g|png|webp)$", href, re.I): continue
            im = find_all(a, lambda x: x.tag == "img")
            t = (im[0].attrs.get("alt") or im[0].attrs.get("title") or "") if im else ""
            t = re.sub(r"[-_]+", " ", re.sub(r"\d+$", "", t)).strip()
            imgs.append(href)
            items.append(f'<img data-src="{html.escape(href)}" alt="{html.escape(t, quote=True)}">')
        return '<div class="gal">' + "".join(items) + "</div>" if items else ""
    inner = "".join(ser(k, imgs) for k in n.kids)
    if tag not in KEEP:
        # block-level wrappers become breaks between blocks; inline wrappers just pass through
        return inner
    if tag == "img":
        src = img_src(n)
        if not src or not re.search(r"\.(jpe?g|png|webp|avif)$", src.split("?")[0], re.I): return ""
        if re.search(r"icon|logo|badge|arrow|bbb|master_elite|google-latest-star|ic-(?:one|two|three|four)|favicon|sa-map", src, re.I): return ""
        src = re.sub(r"-\d+x\d+(\.\w+)$", r"\1", src.split("?")[0])
        imgs.append(src)
        return f'<img data-src="{html.escape(src)}" alt="{html.escape(n.attrs.get("alt") or "", quote=True)}">'
    if tag == "br": return "<br>"
    if tag == "a":
        href = norm_link(n.attrs.get("href"))
        if not inner.strip(): return ""
        return f'<a href="{html.escape(href)}">{inner}</a>' if href else inner
    if tag in ("strong", "em") and not inner.strip(): return inner
    return f"<{tag}>{inner}</{tag}>"


def clean_html(h):
    h = re.sub(r"[ \t\r\n\xa0]+", " ", h)
    for t in ("p", "li", "h2", "h3", "h4", "h5", "h6", "strong", "em", "figcaption", "td", "th"):
        h = re.sub(rf"<{t}>\s*(<br>\s*)*</{t}>", "", h)
    h = re.sub(r"<(ul|ol)>\s*</\1>", "", h)
    h = re.sub(r"(<br>\s*){2,}", "<br>", h)
    h = re.sub(r"<p>\s*<br>", "<p>", h); h = re.sub(r"<br>\s*</p>", "</p>", h)
    h = re.sub(r"\s*(</?(?:p|h\d|ul|ol|li|table|thead|tbody|tr|td|th|blockquote|figure|figcaption)>)\s*", r"\1", h)
    # stray text between blocks -> paragraph
    h = re.sub(r"(</(?:p|ul|ol|h\d|table|blockquote|figure)>)([^<]{3,}?)(?=<(?:p|ul|ol|h\d|table|blockquote|figure|img)[ >])", r"\1<p>\2</p>", h)
    h = re.sub(r"<li>\s*</li>", "", h)
    h = re.sub(r'<p>\s*(<div class="gal">.*?</div>)\s*</p>', r"\1", h)
    # headings the old builder nested inside each other, and headings wrapped in links/strong
    for _ in range(3):
        h = re.sub(r"<(h[1-6])>\s*<(h[1-6])>(.*?)</\2>\s*</\1>", r"<\2>\3</\2>", h)
        h = re.sub(r"<(h[1-6])>\s*<strong>(.*?)</strong>\s*</\1>", r"<\1>\2</\1>", h)
    for _ in range(2):
        h = re.sub(r"<figure>\s*<figure>(.*?)</figure>\s*</figure>", r"<figure>\1</figure>", h)
    h = re.sub(r"<figure>\s*</figure>", "", h)
    h = re.sub(r"<p>\s*(<(?:h\d|ul|ol|table|figure)>)", r"\1", h)
    h = re.sub(r"(</(?:h\d|ul|ol|table|figure)>)\s*</p>", r"\1", h)
    return h.strip()


def split_sections(body):
    """Drop boilerplate h2 sections and empty headings."""
    parts = re.split(r"(?=<h2>)", body)
    keep = []
    for p in parts:
        m = re.match(r"<h2>(.*?)</h2>", p)
        if m:
            head = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
            if not head:
                p = p[m.end():]
            elif BOILER.match(head):
                continue
        keep.append(p)
    return "".join(keep)


def meta(s, prop):
    m = re.search(rf'<meta (?:name|property)="{prop}" content="([^"]*)"', s)
    return html.unescape(m.group(1)) if m else None


def extract(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    out = {"file": os.path.basename(path)}
    out["title"] = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1)).strip()
    out["meta"] = meta(s, "description") or ""
    c = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    out["canonical"] = c.group(1) if c else None
    out["published"] = meta(s, "article:published_time")
    out["modified"] = meta(s, "article:modified_time")
    out["og_image"] = meta(s, "og:image")
    out["robots"] = meta(s, "robots")
    # Genesis: page content sits in the article's entry-content (archives: the whole <main>)
    a = s.find('<div class="entry-content"')
    if a > 0:
        b = s.find("</article>", a)
        region = s[a:b if b > 0 else len(s)]
        h1m = re.search(r'<h1[^>]*class="entry-title"[^>]*>(.*?)</h1>', s, re.S)
    else:
        a = s.find("<main"); b = s.find("</main>", a)
        region = s[a:b] if a > 0 else s
        h1m = None
    out["entry_title"] = html.unescape(re.sub(r"<[^>]+>", "", h1m.group(1))).strip() if h1m else None
    t = Tree(); t.feed(region); root = t.root
    h1s = find_all(root, lambda n: n.tag == "h1")
    out["h1"] = re.sub(r"\s+", " ", text(h1s[0])).strip() if h1s else None
    for h in h1s:  # the H1 goes into the page hero
        h.parent.kids = [k for k in h.parent.kids if k is not h]
    faqs = []
    for p in find_all(root, lambda n: "e-n-accordion-item" == cls(n).strip() or "fusion-panel" in cls(n)):
        q = find_all(p, lambda n: "e-n-accordion-item-title-text" in cls(n) or "fusion-toggle-heading" in cls(n))
        a = find_all(p, lambda n: n.attrs.get("role") == "region" or "panel-body" in cls(n))
        if q and a:
            ah = clean_html("".join(ser(k, []) for k in a[0].kids))
            if not ah.startswith("<"): ah = f"<p>{ah}</p>"
            faqs.append([re.sub(r"\s+", " ", text(q[0])).strip(), ah])
    out["faqs"] = faqs
    tests = []
    for tw in find_all(root, lambda n: "gb-block-testimonial" in cls(n)):
        q = find_all(tw, lambda n: "gb-testimonial-text" in cls(n)); au = find_all(tw, lambda n: "gb-testimonial-name" in cls(n))
        if q: tests.append([re.sub(r"\s+", " ", text(q[0])).strip(), re.sub(r"\s+", " ", text(au[0])).strip() if au else ""])
    for tw in find_all(root, lambda n: "fusion-testimonials" in cls(n)):
        for rv in find_all(tw, lambda n: n.tag == "div" and re.search(r"\breview\b", cls(n))):
            q = find_all(rv, lambda n: n.tag == "q") or find_all(rv, lambda n: n.tag == "blockquote")
            au = find_all(rv, lambda n: "company-name" in cls(n)) or find_all(rv, lambda n: "author" in cls(n))
            qt = re.sub(r"\s+", " ", text(q[0])).strip() if q else ""
            at = re.sub(r"\s+", " ", text(au[0])).strip().strip(",") if au else ""
            if qt: tests.append([qt, at])
    seen = set(); out["testimonials"] = [x for x in tests if not (x[0] in seen or seen.add(x[0]))]
    imgs = []
    body = clean_html(ser(root, imgs))
    body = split_sections(body)
    body = re.sub(r"^\s*<h2>\s*Quality Roofing Services\s*</h2>", "", body, flags=re.I)  # label repeated on top of every post
    out["body"] = body
    out["images"] = list(dict.fromkeys(imgs))
    out["words"] = len(re.findall(r"[A-Za-z0-9']+", html.unescape(re.sub(r"<[^>]+>", " ", body))))
    return out


if __name__ == "__main__":
    res = [extract(f) for f in sorted(glob.glob(os.path.join(sys.argv[1], "*.html")))]
    json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in res:
        print(f'{r["file"][:60]:<60} w{r["words"]:>5} faq{len(r["faqs"]):>2} t{len(r["testimonials"]):>2} img{len(r["images"]):>2} | {r["h1"] or r["entry_title"]}')
