# -*- coding: utf-8 -*-
"""
WWD B-Roll prep - resize a folder of stills into numbered, frame-ready PNGs.

Orientation-based rule (locked in with Zac 2026-08-24, EP1 pass):
- Landscape or square source (width >= height): cover-fit and center-crop
  to fill the target frame completely, edge to edge, no black space.
- Portrait source (height > width, e.g. movie posters, key art): scale to
  touch the top and bottom of the frame, keep the full width visible
  (nothing cropped off the sides), pillarbox with black bars left/right.

Never distorts aspect ratio either way - scaling is always uniform.

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

def cover_fill(img, target_w, target_h):
    """Scale to cover the frame, center-crop the overflow. Edge to edge,
    no bars. Used for landscape/square sources."""
    src_w, src_h = img.size
    scale = max(target_w / src_w, target_h / src_h)
    new_w, new_h = round(src_w * scale), round(src_h * scale)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (new_w - target_w) // 2
    top = (new_h - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))

def pillarbox_vertical(img, target_w, target_h):
    """Scale to touch top and bottom, keep full width visible (no crop),
    center on a black canvas. Used for portrait sources."""
    src_w, src_h = img.size
    scale = target_h / src_h
    new_w, new_h = round(src_w * scale), target_h
    img = img.resize((new_w, new_h), Image.LANCZOS)
    canvas = Image.new("RGB", (target_w, target_h), (0, 0, 0))
    x = (target_w - new_w) // 2
    canvas.paste(img, (x, 0))
    return canvas

def process(img, target_w, target_h):
    src_w, src_h = img.size
    if src_h > src_w:
        return pillarbox_vertical(img, target_w, target_h)
    return cover_fill(img, target_w, target_h)

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
        img = Image.open(src_path).convert("RGB")
        out = process(img, args.width, args.height)
        out_path = os.path.join(args.dst, f"{i}.png")
        out.save(out_path, "PNG")
        log.append(f"{i}.png  <-  {fname}")

    print("\n".join(log))
    print(f"\nDone. {len(manifest)} files written to {args.dst}")

if __name__ == "__main__":
    main()
