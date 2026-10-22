"""Sky Bridge Roofing images (18 Oct 2026).
Used: the client's own photos (team photo, crew with the trucks, a wall-panel job, a ballasted low-slope roof from their
Facebook, soffit and gutter), stills from their own drone video of a standing-seam metal roof on a new build, and stills
from their own office video. The logo is the client's.
Not used: banner graphics with text baked in (ASPHALT_D, COATINGS_D and the rest), Pinterest-size stock files with hash
names (26a30c.., 31f95f.., 78d377.., c497d2.., 770997.., edca26.., c0136d..), a stock hard-hat photo (safety.webp), a stock
EPDM sunset (epdm-systems.webp), generic TPO and coating photos whose source can't be confirmed, and icons.
  python -I imgprep.py <pylib> <dl_dir> <stills_dir> <out_img_dir>"""
import sys, os, json
sys.path.insert(0, sys.argv[1])
from PIL import Image
DL, ST, OUT = sys.argv[2], sys.argv[3], sys.argv[4]
HERE = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)
JOBS = [("sky-bridge-roofing-team", DL, "MAX_0011.jpg", 1600, None),
        ("sky-bridge-crew-trucks", DL, "MAX_0022.jpg", 1600, None),
        ("metal-wall-panels-commercial-entry", DL, "WhatsApp_Image_2026-05-11_at_11.12.00_AM.jpg", 1024, None),
        ("ballasted-low-slope-roof", DL, "658141670_122098308752847000_4907446351184110154_n.jpg", 720, None),
        ("soffit-and-seamless-gutter", DL, "soffit_and_gutter.png", 1200, None),
        ("drone-metal-roof-new-build", ST, "w_003.jpg", 1536, None),
        ("drone-metal-roof-barn", ST, "w_010.jpg", 1536, None),
        ("drone-standing-seam-overview", ST, "d_003.jpg", 810, None),
        ("drone-standing-seam-gables", ST, "d_011.jpg", 810, None),
        ("drone-standing-seam-close", ST, "d_017.jpg", 810, None),
        ("office-sky-bridge-door", ST, "t_005.jpg", 1600, None),
        ("office-roof-detail-drawings", ST, "t_009.jpg", 1600, None),
        ("office-whiteboard-detail", ST, "t_027.jpg", 1600, None),
        ("office-project-review", ST, "t_049.jpg", 1600, None)]
meta = {}
for name, d, src, cap, crop in JOBS:
    im = Image.open(os.path.join(d, src)).convert("RGB")
    if im.width > cap: im = im.resize((cap, round(im.height * cap / im.width)), Image.LANCZOS)
    q = 82
    while True:
        im.save(os.path.join(OUT, name + ".webp"), "WEBP", quality=q, method=6)
        kb = os.path.getsize(os.path.join(OUT, name + ".webp")) // 1024
        if kb <= 150 or q <= 56: break
        q -= 6
    meta[name] = [im.width, im.height, kb]
# Logo: the client's mark on black. Kept on black (it sits in a dark header); a favicon is cut from the SBR diamond.
lg = Image.open(os.path.join(DL, "logo_6006bc15-7710-4d84-9730-64dd9da03124.webp")).convert("RGB")
lg.save(os.path.join(OUT, "sky-bridge-roofing-logo.webp"), "WEBP", quality=90)
lg.save(os.path.join(OUT, "sky-bridge-roofing-logo.png"))
meta["sky-bridge-roofing-logo"] = [lg.width, lg.height, os.path.getsize(os.path.join(OUT, "sky-bridge-roofing-logo.webp")) // 1024]
fav = lg.crop((int(lg.width * .3), 0, int(lg.width * .7), int(lg.height * .45))); fav = fav.resize((96, round(96 * fav.height / fav.width)))
sq = Image.new("RGB", (96, 96), "black"); sq.paste(fav, (0, (96 - fav.height) // 2)); sq.save(os.path.join(OUT, "favicon.png"))
json.dump(meta, open(os.path.join(HERE, "imgmeta.json"), "w"), indent=0)
print(meta)
