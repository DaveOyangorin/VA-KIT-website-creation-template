"""Extracts every page of the rendered mandmgutters.com crawl (Divi theme) into one JSON file.

  python -I extract.py <pages_dir> <out.json>

For each page: path, title, meta description, canonical, H1, published/modified dates, author, the cleaned
content of div.entry-content (only headings, paragraphs, lists, tables, blockquotes, images, links and emphasis
survive), the images used, and a word count.
"""
import sys, os, re, json, html
from html.parser import HTMLParser

KEEP = {"h2", "h3", "h4", "p", "ul", "ol", "li", "table", "thead", "tbody", "tr", "th", "td", "blockquote", "strong", "b", "em", "i", "a", "img", "br", "figure", "figcaption"}
DROP = {"script", "style", "svg", "noscript", "form", "button", "iframe", "select", "textarea", "input", "label", "nav", "video"}
VOID = {"img", "br", "input", "meta", "link", "hr", "source", "area", "col", "embed", "param", "track", "wbr"}
SKIP_CLASS = re.compile(r"et_pb_button|et_pb_contact|et_pb_testimonial|wpforms|et_pb_social|et_pb_post_nav|et_pb_comments|sharedaddy|addtoany|et_pb_blog_grid|et_pb_posts|et_pb_signup|gform|et_pb_counters|et_pb_number_counter|et_pb_countdown|et_pb_map|post-meta|et_pb_slider|et_pb_tabs_controls")


def balanced_div(s, start):
    """Return the HTML of the <div ...> beginning at `start`, including its matching </div>."""
    depth, i = 0, start
    tag = re.compile(r"<(/?)div\b[^>]*>", re.I)
    for m in tag.finditer(s, start):
        depth += -1 if m.group(1) else 1
        if depth == 0: return s[start:m.end()]
    return s[start:]


class Clean(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip, self.stack, self.imgs = [], 0, [], []

    def handle_starttag(self, t, a):
        a = dict(a)
        cls = a.get("class") or ""
        if self.skip:
            if t not in VOID: self.skip += 1
            return
        if t in DROP or SKIP_CLASS.search(cls):
            if t not in VOID: self.skip = 1
            return
        if t not in KEEP:
            if t not in VOID: self.stack.append(None)
            return
        if t == "img":
            src = a.get("data-src") or a.get("src") or ""
            if src.startswith("data:") or not src: return
            alt = a.get("alt") or ""
            self.imgs.append((src, alt))
            self.out.append(f'<img src="{html.escape(src)}" alt="{html.escape(alt)}">')
            return
        if t == "br":
            self.out.append("<br>"); return
        if t == "a":
            href = a.get("href") or ""
            self.out.append(f'<a href="{html.escape(href)}">'); self.stack.append("a"); return
        tt = {"b": "strong", "i": "em"}.get(t, t)
        self.out.append(f"<{tt}>"); self.stack.append(tt)

    def handle_endtag(self, t):
        if self.skip:
            if t not in VOID: self.skip -= 1
            return
        if t in VOID: return
        if self.stack:
            x = self.stack.pop()
            if x: self.out.append(f"</{x}>")

    def handle_data(self, d):
        if not self.skip: self.out.append(html.escape(d, quote=False))


def tidy(h):
    h = re.sub(r"\s+", " ", h)
    for _ in range(3):
        h = re.sub(r"<(p|h2|h3|h4|li|strong|em|a[^>]*)>\s*(&nbsp;| )?\s*</(p|h2|h3|h4|li|strong|em|a)>", "", h)
    h = re.sub(r"\s*(</?(?:p|h2|h3|h4|ul|ol|li|table|thead|tbody|tr|th|td|blockquote|figure|figcaption)>)\s*", r"\1", h)
    h = re.sub(r"(<br>\s*){2,}", "<br>", h)
    return h.strip()


def meta(s, prop):
    m = re.search(r'<meta (?:name|property)="' + re.escape(prop) + r'" content="([^"]*)"', s)
    return html.unescape(m.group(1)) if m else ""


def main(src, out):
    rows = []
    for f in sorted(os.listdir(src)):
        if not f.endswith(".html") or f.startswith(("home_raw", "_")): continue
        s = open(os.path.join(src, f), encoding="utf-8").read()
        path = "" if f == "home.html" else f[:-5].replace("__", "/") + "/"
        t = re.search(r"<title>(.*?)</title>", s, re.S)
        h1 = re.search(r"(?s)<h1\b[^>]*>(.*?)</h1>", s)
        canon = re.search(r'<link rel="canonical" href="([^"]*)"', s)
        i = s.find('<div class="entry-content"')
        body = balanced_div(s, i) if i >= 0 else ""
        if not body:
            m = re.search(r'<div id="main-content"', s)
            body = balanced_div(s, m.start()) if m else ""
        c = Clean(); c.feed(body); content = tidy("".join(c.out))
        text = html.unescape(re.sub(r"<[^>]+>", " ", content))
        author = re.search(r'"author":\{"@type":"Person","@id":"[^"]*","url":"[^"]*","name":"([^"]+)"', s) or re.search(r'class="author[^"]*"[^>]*>(?:<a[^>]*>)?([^<]+)<', s)
        rows.append({"path": path, "title": html.unescape(re.sub(r"<[^>]+>", "", t.group(1))).strip() if t else "",
                     "meta": meta(s, "description"), "canonical": canon.group(1) if canon else "",
                     "h1": html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip() if h1 else "",
                     "published": meta(s, "article:published_time")[:10], "modified": meta(s, "article:modified_time")[:10],
                     "og_image": meta(s, "og:image"), "author": html.unescape(author.group(1)).strip() if author else "",
                     "content": content, "images": c.imgs, "words": len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", text))})
    json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print(len(rows), "pages;", sum(1 for r in rows if r["words"] < 100), "under 100 words")


if __name__ == "__main__":
    main(*sys.argv[1:3])
