# -*- coding: utf-8 -*-
"""
WWD B-Roll prep - resize a folder of stills into numbered, frame-ready PNGs.

Contain/fit rule (superseded 2026-08-29, "Trim nothing, make it fit" -
see memory/topics/visual-media.md for the prior cover-crop default this
replaced): every source, regardless of orientation, is scaled uniformly to
fit entirely inside the target frame - nothing ever gets cropped. Never
distorts aspect ratio.

Padding is ALPHA TRANSPARENCY, not black bars (corrected 2026-08-30 - Zac
caught black bars on a poster and asked for alpha instead, so the editor can
composite the image without a black box baked in). Output is RGBA PNG.

Manifest format (list, in final output order - just filenames):
["fire-in-the-sky-dvd-movie-cover.webp", "images (3).jpg", ...]

Usage:
  python resize_broll.py --src "<B-Roll folder>" --dst "<USE folder>" \
      --manifest "<manifest.json>" [--width 1920] [--height 1080]

Output: <dst>\1.png, 2.png, ... in manifest order.
"""
import argparse
import json
import os
from PIL import Image

def fit_contain(img, target_w, target_h):
    """Scale to fit entirely inside the frame, no cropping, centered on a
    transparent RGBA canvas. Used for every source regardless of orientation."""
    src_w, src_h = img.size
    scale = min(target_w / src_w, target_h / src_h)
    new_w, new_h = round(src_w * scale), round(src_h * scale)
    img = img.convert("RGBA").resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGBA", (target_w, target_h), (0, 0, 0, 0))
    x = (target_w - new_w) // 2
    y = (target_h - new_h) // 2
    canvas.paste(img, (x, y), img)
    return canvas

def process(img, target_w, target_h):
    return fit_contain(img, target_w, target_h)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", required=True, help="Folder containing source images")
    ap.add_argument("--dst", required=True, help="Output folder for numbered PNGs")
    ap.add_argument("--manifest", required=True, help="JSON manifest, ordered list of filenames")
    ap.add_argument("--width", type=int, default=1920)
    ap.add_argument("--height", type=int, default=1080)
    args = ap.parse_args()

    with open(args.manifest, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    os.makedirs(args.dst, exist_ok=True)

    log = []
    for i, fname in enumerate(manifest, start=1):
        src_path = os.path.join(args.src, fname)
        img = Image.open(src_path)
        out = process(img, args.width, args.height)
        out_path = os.path.join(args.dst, f"{i}.png")
        out.save(out_path, "PNG")
        log.append(f"{i}.png  <-  {fname}")

    print("\n".join(log))
    print(f"\nDone. {len(manifest)} files written to {args.dst}")

if __name__ == "__main__":
    main()
