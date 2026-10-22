"""QA for a build folder:  python -I qa.py <root> [--all]"""
import sys, os, re, json, html, glob

root = sys.argv[1]
show_all = "--all" in sys.argv
issues = 0
rows = []
for f in sorted(glob.glob(os.path.join(root, "**", "*.html"), recursive=True)):
    rel = os.path.relpath(f, root).replace(os.sep, "/")
    s = open(f, encoding="utf-8").read()
    t = html.unescape(re.search(r"<title>(.*?)</title>", s, re.S).group(1))
    m = re.search(r'<meta name="description" content="([^"]*)"', s)
    m = html.unescape(m.group(1)) if m else ""
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    probs = []
    h1 = len(re.findall(r"<h1[\s>]", s))
    if h1 != 1: probs.append(f"h1 x{h1}")
    if not can and rel != "404.html": probs.append("no canonical")
    for blk in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', s):
        try: json.loads(blk)
        except Exception as e: probs.append("JSON-LD " + str(e)[:60])
    base = os.path.dirname(f)
    for href in re.findall(r'(?:href|src)="([^"]+)"', s):
        if href.startswith(("http", "tel:", "mailto:", "#", "data:")): continue
        tgt = os.path.normpath(os.path.join(base, href.split("#")[0]))
        if href.split("#")[0].endswith("/") or href in ("./",): tgt = os.path.join(tgt, "index.html")
        if not os.path.exists(tgt): probs.append("broken " + href)
    # OWN-DOMAIN: absolute links back to the client's domain must point at a page that exists in this build
    m_dom = re.search(r'<link rel="canonical" href="(https?://[^/]+)/', s)
    if m_dom:
        dom = m_dom.group(1)
        for href in re.findall(r'href="(' + re.escape(dom) + r'/[^"#?]*)', s):
            pth = href[len(dom) + 1:]
            if pth.startswith(("wp-content", "assets", "es/")): continue  # es/ = the Spanish pages, kept on the live site (checked 200 on 17 Oct)
            tgt = os.path.join(root, pth, "index.html") if not pth.endswith((".xml", ".txt", ".html")) else os.path.join(root, pth)
            if not os.path.exists(tgt) and pth != "": probs.append("own-domain link to missing page " + href)
    for i in re.findall(r"<img[^>]*>", s):
        if "width=" not in i or 'alt="' not in i: probs.append("img w/o dims/alt")
    if "@/" in re.sub(r"(?s)<script.*?</script>", "", s): probs.append("unresolved @/ link")
    main = re.search(r'(?s)<main id="main">(.*)</main>', s)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r'(?s)<section class="cta">.*?</section>', " ", main.group(1) if main else "")))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", txt))
    rows.append((rel, len(t), len(m), words, probs))
    issues += len(probs)
for r in rows:
    if show_all or r[4]:
        print(f"{r[0]:<74} T{r[1]:>3} M{r[2]:>3} W{r[3]:>5}")
        for p in r[4][:6]: print("    !!", p)
print("pages:", len(rows), "| issues:", issues)
print("titles outside 50-60:", sum(1 for r in rows if not 50 <= r[1] <= 60), "| metas outside 150-160:", sum(1 for r in rows if not 150 <= r[2] <= 160))
