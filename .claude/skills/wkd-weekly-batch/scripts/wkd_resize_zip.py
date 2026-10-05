"""
WKD digital bundle builder - reusable weekly version, based on the
2026-09-01 Christian-line script (scratch\\wkd_christian_resize.py).

Resizes raw WKD source PNGs into the standard digital wall-art size set
(8x10, 5x7, 11x14, 16x20, A4, A3, all @300 DPI, JPG) and zips each
design's 6 sizes into a single per-design ZIP, written into a
category subfolder under D:\\04 New Warrior King Designs\\_Print Exports\\
(never the flat root, to avoid colliding with older 4-size-PNG exports
that already exist there for some designs).

Source is landscape-oriented (historically ~1536x1024, 3:2). All
target print sizes are requested as portrait paper dimensions, but
since every target ratio (max ~1.414 for A4/A3) is narrower than a
3:2 source, each frame is rendered in LANDSCAPE orientation (matching
the source's natural composition) and center-cropped on the width
only - never stretched, never letterboxed.

Source files are never modified.

Edit the DESIGNS dict below per run: {source filename: clean design name}.
Set SRC_DIR and OUT_ROOT per the category being processed.
"""
import os
import sys
import zipfile
from PIL import Image

# ---- EDIT PER RUN ----
SRC_DIR = r"PLACEHOLDER"
OUT_ROOT = r"PLACEHOLDER"
DESIGNS = {
    # "raw_filename.png": "Clean Design Name",
}
# -----------------------

SIZES = {
    "8x10": (3000, 2400),
    "5x7": (2100, 1500),
    "11x14": (4200, 3300),
    "16x20": (6000, 4800),
    "A4": (3508, 2481),
    "A3": (4961, 3508),
}


def run(src_dir, out_root, designs):
    os.makedirs(out_root, exist_ok=True)
    results = []
    for fname, name in designs.items():
        src_path = os.path.join(src_dir, fname)
        if not os.path.exists(src_path):
            results.append((name, "MISSING SOURCE FILE", None))
            continue
        try:
            im = Image.open(src_path).convert("RGB")
        except Exception as e:
            results.append((name, f"OPEN FAILED: {e}", None))
            continue

        design_dir = os.path.join(out_root, name)
        os.makedirs(design_dir, exist_ok=True)
        zip_path = os.path.join(out_root, f"{name}.zip")

        max_upscale = 1.0
        try:
            with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
                for size_name, (tw, th) in SIZES.items():
                    src_ratio = im.width / im.height
                    tgt_ratio = tw / th
                    if src_ratio > tgt_ratio:
                        new_height = im.height
                        new_width = int(round(new_height * tgt_ratio))
                    else:
                        new_width = im.width
                        new_height = int(round(new_width / tgt_ratio))
                    left = (im.width - new_width) // 2
                    top = (im.height - new_height) // 2
                    cropped = im.crop((left, top, left + new_width, top + new_height))
                    upscale_factor = th / new_height
                    max_upscale = max(max_upscale, upscale_factor)
                    resized = cropped.resize((tw, th), Image.LANCZOS)
                    out_name = f"{name} - {size_name}.jpg"
                    out_path = os.path.join(design_dir, out_name)
                    resized.save(out_path, "JPEG", quality=95, dpi=(300, 300))
                    zf.write(out_path, out_name)
            results.append((name, "OK", round(max_upscale, 2)))
        except Exception as e:
            results.append((name, f"PROCESS FAILED: {e}", None))

    print(f"\n{'Design':40s} {'Status':20s} {'MaxUpscale'}")
    ok_count = 0
    for name, status, upscale in results:
        print(f"{name:40s} {status:20s} {upscale if upscale else ''}")
        if status == "OK":
            ok_count += 1
    print(f"\n{ok_count}/{len(designs)} designs processed OK.")
    print(f"Output root: {out_root}")
    return results


if __name__ == "__main__":
    if SRC_DIR == "PLACEHOLDER":
        print("Edit SRC_DIR / OUT_ROOT / DESIGNS before running, or import run() directly.")
        sys.exit(1)
    run(SRC_DIR, OUT_ROOT, DESIGNS)
