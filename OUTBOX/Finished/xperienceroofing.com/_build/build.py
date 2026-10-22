"""Builds the xperienceroofing.com redesign:  python -I build.py <out_site> <out_preview>
Same URLs and canonicals as the current Next.js site (no trailing slash; the host must serve /services/roof-repair from a
folder index), the client's GA4 tag kept, plus a new /blog. See pages.py and the notes."""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import cfg, engine
engine.setup(cfg)
import pages
engine.build(sys.argv[1], sys.argv[2], pages.make_pages(), pages.header, pages.footer)
