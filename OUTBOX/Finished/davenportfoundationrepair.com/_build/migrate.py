"""migrate.py: the client's own page text, cleaned, with paragraphs carrying unsupported claims dropped and internal links
pointed at the new pages.   migrate(here, key, domain, drop_regex, skip_heads=()) -> html"""
import json, os, re
from clean import clean_main


def migrate(here, key, domain, drop, skip_heads=(), first_h2_skip=True):
    d = json.load(open(os.path.join(here, "src", "extract.json"), encoding="utf-8"))[key]
    raw = open(os.path.join(here, "src", "pages", key + ".html"), encoding="utf-8").read()
    h, h1, _ = clean_main(raw, d["url"])
    out, seen = [], set()
    for tag, inner in re.findall(r"<(h2|h3|p|ul|ol|blockquote)>(.*?)</\1>", h, re.S):
        txt = re.sub(r"<[^>]+>", "", inner).strip()
        if len(txt) < 3 or drop.search(txt): continue
        if tag in ("h2", "h3"):
            inner = re.sub(r"</?(strong|b)>", "", inner)
            if txt.lower() in seen or any(s.lower() == txt.lower() for s in skip_heads): continue
            seen.add(txt.lower())
        if tag in ("ul", "ol"):
            items = [i for i in re.findall(r"<li>(.*?)</li>", inner, re.S) if not drop.search(re.sub(r"<[^>]+>", "", i))]
            if not items: continue
            inner = "".join(f"<li>{i.strip()}</li>" for i in items)
        inner = re.sub(r"^[✅✔\U0001F539\U0001F4CD\s]+", "", inner)
        out.append(f"<{tag}>{inner.strip()}</{tag}>")
    s = "\n".join(out)
    dom = re.escape(domain)
    s = re.sub(r'href="https?://(?:www\.)?' + dom + r'/?([^"#?]*?)/?"', lambda m: f'href="@/{m.group(1)}/"' if m.group(1) else 'href="@/"', s)
    s = re.sub(r'<a href="(?!@/|https?://|tel:|mailto:)[^"]*">(.*?)</a>', r"\1", s)
    return s
