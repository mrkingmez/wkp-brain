"""
Kingdom Planners preview watermark.

Takes a listing screenshot (a tab, a calculator, a contents graphic)
and produces a watermarked preview JPEG - a rotated, semi-transparent
tile of a name across the image, so the listing photo can't be
screenshotted and used as the product itself.

Usage:
    python watermark.py --input "work\raw\va-tracker-tab2.png" ^
                         --text "Kingdom Planners" ^
                         --out "work\previews\va-tracker-tab2_PREVIEW.jpg"

Requires: Pillow  (pip install pillow)
"""

import argparse
import os
import sys

from PIL import Image, ImageDraw, ImageFont

PREVIEW_LONG_EDGE = 1600
JPEG_QUALITY = 88
TILE_OPACITY = 70   # 0-255, higher = more visible
ROTATE_DEGREES = 30


def make_preview(img, text, out_path):
    p = img.copy()
    p.thumbnail((PREVIEW_LONG_EDGE, PREVIEW_LONG_EDGE), Image.LANCZOS)
    p = p.convert("RGBA")

    layer = Image.new("RGBA", p.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    try:
        font = ImageFont.truetype("arial.ttf", max(18, p.size[0] // 26))
    except OSError:
        font = ImageFont.load_default()

    step_x = p.size[0] // 2
    step_y = p.size[1] // 5
    for y in range(0, p.size[1] + step_y, step_y):
        for x in range(-step_x, p.size[0] + step_x, step_x):
            draw.text((x, y), text, fill=(255, 255, 255, TILE_OPACITY), font=font)

    layer = layer.rotate(ROTATE_DEGREES, expand=False)
    out = Image.alpha_composite(p, layer).convert("RGB")
    out.save(out_path, "JPEG", quality=JPEG_QUALITY)
    return out_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--text", default="Kingdom Planners")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    if not os.path.exists(args.input):
        sys.exit(f"Input not found: {args.input}")

    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    img = Image.open(args.input).convert("RGB")
    make_preview(img, args.text, args.out)
    print(f"[watermark] wrote {args.out}")


if __name__ == "__main__":
    main()