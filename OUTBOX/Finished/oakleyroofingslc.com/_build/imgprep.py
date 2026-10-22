"""Oakley Roofing images (17 Oct 2026). Only photos that look like the client's own jobs (phone or drone shots of real
roofs) are used. Not used: Depositphotos stock (9 files), stock roofer/house photos, Tesla marketing renders and product
shots, a stock appliance photo, and the partner logos (GAF, Johns Manville, NRCA, Owens Corning, TAMKO, Versico), which
wait for the client to confirm each certification.
  python -I imgprep.py <pylib> <dl_dir> <out_img_dir>"""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
DL, OUT = sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
JOBS = [("single-ply-roof-deck-new-install", "20200802_095859-scaled.jpg", 2200),
        ("residential-new-construction-roof", "20210417_130918-1-scaled-e1621876162445.jpg", 2200),
        ("restaurant-metal-roof-aerial", "Screen-Shot-2021-04-14-at-12.44.03-PM.png", 2200),
        ("apartment-new-build-white-roof", "Commercial-roof-new-build-e1620232814479.jpg", 1400),
        ("commercial-flat-roof-aerial", "utah-commercial-roofing-contractor.jpg", 1400),
        ("solar-roof-home-aerial", "Solar-panels-on-home.jpg", 1400),
        ("white-membrane-roof-sunset", "33093-1-e1624380261962.jpeg", 1400)]
meta = {}
for name, src, cap in JOBS:
    im = Image.open(os.path.join(DL, src)).convert("RGB")
    if im.width > cap: im = im.resize((cap, round(im.height * cap / im.width)), Image.LANCZOS)
    q = 82
    while True:
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
        kb = os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024
        if kb <= (300 if cap > 1400 else 160) or q <= 56: break
        q -= 6
    meta[name] = [im.width, im.height, kb]
# Logo: the client's black mark on transparent; a white copy is made for the dark header and footer.
lg = Image.open(os.path.join(DL, "Oakley-Roofing-Logo-1.png")).convert("RGBA")
lg.thumbnail((760, 760))
lg.save(os.path.join(OUT, "oakley-roofing-logo.png"), optimize=True)
white = Image.new("RGBA", lg.size, (255, 255, 255, 0)); white.putalpha(lg.getchannel("A"))
white.save(os.path.join(OUT, "oakley-roofing-logo-white.png"), optimize=True)
for n in ("oakley-roofing-logo", "oakley-roofing-logo-white"): meta[n] = [lg.width, lg.height, 0]
mark = lg.crop((0, 0, lg.width, int(lg.height * 0.66))); bb = mark.getbbox(); mark = mark.crop(bb)
fav = Image.new("RGBA", (max(mark.size),) * 2, (255, 255, 255, 255)); fav.alpha_composite(mark, ((fav.width - mark.width) // 2, (fav.height - mark.height) // 2))
fav.thumbnail((96, 96)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print(meta)
