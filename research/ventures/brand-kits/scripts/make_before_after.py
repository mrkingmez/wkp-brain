"""Compose a real before/after image (contain-fit, never crops). Photo restore only.
python make_before_after.py --before B.jpg --after A.jpg --out out.png [--mode light|dark]
       [--shape landscape|square] [--preview]   (--preview adds a diagonal PREVIEW watermark)
Reads the look from brand_kit.py in the same folder. Use only photos Zac may show."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_kit as bk
from PIL import Image
ap = argparse.ArgumentParser()
ap.add_argument("--before", required=True); ap.add_argument("--after", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--mode", default="light")
ap.add_argument("--shape", default="landscape"); ap.add_argument("--preview", action="store_true")
a = ap.parse_args()
kit = dict(bk.KITS["photo"]); kit["key"] = "photo"
W, H = (1920, 1080) if a.shape == "landscape" else (1080, 1080)
im = bk.before_after(kit, a.mode, Image.open(a.before), Image.open(a.after), W, H, watermark=a.preview)
im.save(a.out); print("saved", a.out)
