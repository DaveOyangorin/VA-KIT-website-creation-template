"""Builds a kit2 site draft:  python -I build.py <out_site> <out_preview>
style.css = theme.css + base.css + premium.css + concept.css; site.js = premium.js + concept.js. The mobile header fix block
(appended by mobilefix.py, marker MFIX-2026-10-19) is carried over on every rebuild."""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)


def join(out, parts):
    p = os.path.join(HERE, out)
    old = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    m = re.search(r"/\* MFIX-2026-10-19.*", old, re.S)
    src = [open(os.path.join(HERE, f), encoding="utf-8").read() for f in parts if os.path.exists(os.path.join(HERE, f))]
    if src:
        open(p, "w", encoding="utf-8", newline="\n").write("\n".join(src) + ("\n" + m.group(0) if m else ""))


join("style.css", ("theme.css", "base.css", "premium.css", "concept.css"))
join("site.js", ("premium.js", "concept.js"))
import cfg, engine
engine.setup(cfg)
import pages
engine.build(sys.argv[1], sys.argv[2], pages.make_pages(), pages.header, pages.footer)
