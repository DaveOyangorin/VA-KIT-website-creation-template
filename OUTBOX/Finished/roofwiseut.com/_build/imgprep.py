"""RoofWise images (17 Oct 2026). The only real footage on roofwiseut.com is the home page hero video: a drone
orbit of a RoofWise re-roof. Four frames from it are the site's photos. The site's other 12 images (job "photos" and
3D graphics) look AI-generated and are not used.
  python -I imgprep.py <pylib> <frames_dir> <logo.png> <out_img_dir>"""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
FR, LOGO, OUT = sys.argv[2], sys.argv[3], sys.argv[4]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
jobs = [("drone-reroof-hillside-home", "frame_1.jpg"), ("drone-reroof-crew-on-roof", "frame_11.jpg"),
        ("drone-reroof-underlayment", "frame_19.jpg"), ("drone-reroof-full-property", "frame_29.jpg")]
meta = {}
for name, src in jobs:
    im = Image.open(os.path.join(FR, src)).convert("RGB").resize((1600, 900), Image.LANCZOS)
    im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=76, method=6)
    meta[name] = [1600, 900, os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024]
lg = Image.open(LOGO).convert("RGBA"); lg.thumbnail((600, 600))
lg.save(os.path.join(OUT, "roofwise-logo.png"), optimize=True); lg.save(os.path.join(OUT, "roofwise-logo.webp"), "WEBP", quality=90)
meta["roofwise-logo"] = [lg.width, lg.height, os.path.getsize(os.path.join(OUT, "roofwise-logo.webp")) // 1024]
fav = lg.crop((0, 0, lg.width, int(lg.height * 0.62))); fav.thumbnail((96, 96)); fav.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print(meta)
