"""Converts Jordan River Roofing's real photos (from jordanriverroofing.com, 17 Oct 2026) to local WebP.
  python -I imgprep.py <pylib> <dl_dir> <out_img_dir>
The site's 23 other images (1376x768 / 1200x896 PNGs on the service and city pages) look AI-generated and are not used."""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
DL, OUT = sys.argv[2], sys.argv[3]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
# Not used: the wide "crew and truck" banner photo (6a85b196...png). Its truck and trailer lettering is garbled and the
# phone number on it is wrong, which points to an AI-generated or AI-altered image (see notes).
jobs = [("truck-and-dump-trailer-on-job", "6a85b9531447bf72d96532e3.jpg", 600),
        ("jordan-river-roofing-truck-owner", "6a85b9534502c702e541c7d4.jpg", 600),
        ("yard-banner-finished-roof", "6a85b95362d760a82d19f2d3.jpg", 600),
        ("tudor-brick-home-tear-off", "6a85b953c0d6fd7d6b9972a9.jpg", 600),
        ("victorian-home-reroof", "6a85b953ee714bf5428b37ad.jpg", 600),
        ("finished-architectural-shingle-roof", "6a85b953ee714bf5428b37b1.jpg", 600),
        ("crew-tear-off-with-truck", "6a85b955b3a1bcf4fa853bac.jpg", 600)]
meta = {}
for name, src, maxw in jobs:
    im = Image.open(os.path.join(DL, src)).convert("RGB")
    if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=(74 if maxw > 1000 else 82), method=6)
    meta[name] = [im.width, im.height, os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024]
logo = Image.open(os.path.join(DL, "6a8551b9b8d260ce2a49266f.png")).convert("RGBA")
logo.save(os.path.join(OUT, "jordan-river-roofing-logo.png"), optimize=True)
logo.save(os.path.join(OUT, "jordan-river-roofing-logo.webp"), "WEBP", quality=90)
meta["jordan-river-roofing-logo"] = [logo.width, logo.height, os.path.getsize(os.path.join(OUT, "jordan-river-roofing-logo.webp")) // 1024]
Image.open(os.path.join(DL, "favicon.png")).save(os.path.join(OUT, "favicon.png")) if os.path.exists(os.path.join(DL, "favicon.png")) else logo.resize((96, 37)).save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print(meta)
