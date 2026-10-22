import sys, os, re, json, html, glob
root = sys.argv[1]
BANNED = ["in today's", "ever-evolving", "furthermore", "moreover", "additionally", "in conclusion", "to summarize", "in summary",
  "lastly", "first and foremost", "that being said", "it is worth noting", "it is important to note", "deep dive", "delve", "unlock",
  "journey", "game-changer", "cutting-edge", "at the end of the day", "leverage", "holistic", "robust", "seamless", "streamline",
  "empower", "elevate", "transform", "revolutionize", "innovative", "dynamic", "synergy", "best practices", "multifaceted",
  "paramount", "pivotal", "crucial", "comprehensive", "utilize", "facilitate", "in order to", "due to the fact", "studies show",
  "experts say", "top-notch", "world-class", "second to none", "let's dive", "without further ado", "needless to say"]
bad = 0
rows = []
for f in sorted(glob.glob(os.path.join(root, '**', '*.html'), recursive=True)):
    rel = os.path.relpath(f, root).replace(os.sep, '/')
    s = open(f, encoding='utf-8').read()
    t = html.unescape(re.search(r'<title>(.*?)</title>', s).group(1))
    m = html.unescape(re.search(r'<meta name="description" content="([^"]*)"', s).group(1))
    can = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    h1 = len(re.findall(r'<h1[\s>]', s))
    main = re.search(r'(?s)<main id="main">(.*)</main>', s).group(1)
    main_txt = re.sub(r'(?s)<section class="cta">.*?</section>', ' ', main)
    main_txt = re.sub(r'(?s)<(script|style)[^>]*>.*?</\1>', ' ', main_txt)
    txt = html.unescape(re.sub(r'<[^>]+>', ' ', main_txt))
    words = len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’\-]*", txt))
    issues = []
    if not 50 <= len(t) <= 60: issues.append(f'title {len(t)}')
    if not 150 <= len(m) <= 160: issues.append(f'meta {len(m)}')
    if h1 != 1: issues.append(f'h1 x{h1}')
    for blk in re.findall(r'(?s)<script type="application/ld\+json">(.*?)</script>', s):
        try: json.loads(blk)
        except Exception as e: issues.append('JSON-LD ' + str(e))
    # links + images
    base = os.path.dirname(f)
    for href in re.findall(r'(?:href|src)="([^"]+)"', s):
        if href.startswith(('http', 'tel:', 'mailto:', '#', 'data:')): continue
        target = os.path.normpath(os.path.join(base, href.split('#')[0]))
        if href.endswith('/') or href == './' or href == '../' * href.count('../') and href:
            target = os.path.join(target, 'index.html')
        if not os.path.exists(target): issues.append('broken ' + href)
    low = txt.lower()
    for b in BANNED:
        if re.search(r'\b' + re.escape(b) + r'\b', low): issues.append('banned: ' + b)
    imgs_nodim = [i for i in re.findall(r'<img[^>]*>', s) if 'width=' not in i or 'alt=' not in i]
    if imgs_nodim: issues.append(f'{len(imgs_nodim)} img w/o dims/alt')
    intl = len(set(re.findall(r'href="(\.\./[^"#]*|\./|[a-z][^":#]*/)"', main)))
    rows.append((rel, len(t), len(m), words, intl, can.group(1) if can else '-', issues))
    bad += len(issues)
for r in rows:
    print(f'{r[0]:<72} T{r[1]:>3} M{r[2]:>3} W{r[3]:>5} L{r[4]:>3}  {r[5]}')
    for i in r[6]: print('     !!', i)
print('issues:', bad)
