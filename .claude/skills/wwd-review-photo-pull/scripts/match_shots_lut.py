"""match_shots_lut.py - match shot A (source) to shot B (target or reference frame) by
measured color statistics, and save the correction as a .cube 3D LUT.

Built 2026-10-25 for the wwd-color bench. numpy, scipy, Pillow and ffmpeg only.
Use it to make the King-Z cam, the Winter Wolf cam and the main recording sit together,
or to pull any shot toward a reference frame. Load the .cube on the SOURCE clip (Premiere:
Lumetri Color > Basic Correction > Input LUT > Browse. Resolve free: right-click a node >
LUT).

How it measures (CIE Lab, so lightness and color are separate):
  lightness  histogram (quantile) match in whole-frame mode, or a clamped gain and offset
             in skin-only mode
  color      mean shift and clamped spread match on the a and b channels
  The shift fades out in the deepest blacks and brightest whites so they do not tint.
  --strength 0..1 blends the match toward no change (0.6 is a good first try).

Inputs: an image file, or a video with times: "clip.mp4@120,300" (frames pulled with ffmpeg
into D:\\WKP\\scratch\\color\\frames\\). Several frames per side are pooled.

Whole-frame mode compares everything in the frame, so it only makes sense when the two
shots show similar content. For two different webcams with different backgrounds use
--skin-only (stats come from skin-colored pixels, which is what must match) or --region
x0,y0,x1,y1 (fractions of the frame, e.g. 0.3,0.2,0.7,0.8 for the face area).

Examples:
  python match_shots_lut.py --source "ww.mp4@300" --target "kz.mp4@300" --skin-only ^
      --out "P:\\WWD Kit\\Color\\Match WinterWolf to KingZ 2026-10-25.cube" --strength 0.7 ^
      --strip-out D:\\WKP\\scratch\\color\\match_strip.png
"""
import argparse
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_look_lut import (apply_cube, build_cube, load_img, save_img, smoothstep,  # noqa: E402
                           write_cube)

FRAMES_DIR = r"D:\WKP\scratch\color\frames"
D65 = np.array([0.95047, 1.0, 1.08883])
M_RGB2XYZ = np.array([[0.4124564, 0.3575761, 0.1804375],
                      [0.2126729, 0.7151522, 0.0721750],
                      [0.0193339, 0.1191920, 0.9503041]])


def srgb_to_lab(rgb):
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    xyz = lin @ M_RGB2XYZ.T / D65
    f = np.where(xyz > 216 / 24389, np.cbrt(xyz), (24389 / 27 * xyz + 16) / 116)
    L = 116 * f[..., 1] - 16
    a = 500 * (f[..., 0] - f[..., 1])
    b = 200 * (f[..., 1] - f[..., 2])
    return np.stack([L, a, b], axis=-1)


def lab_to_srgb(lab):
    fy = (lab[..., 0] + 16) / 116
    fx = fy + lab[..., 1] / 500
    fz = fy - lab[..., 2] / 200
    f = np.stack([fx, fy, fz], axis=-1)
    xyz = np.where(f ** 3 > 216 / 24389, f ** 3, (116 * f - 16) / (24389 / 27)) * D65
    lin = xyz @ np.linalg.inv(M_RGB2XYZ).T
    lin = np.clip(lin, 0, 1)
    return np.where(lin <= 0.0031308, lin * 12.92, 1.055 * np.power(lin, 1 / 2.4) - 0.055)


def skin_pixels(rgb):
    """YCbCr box for skin, plus a sane luma range. rgb in 0..1, shape (N,3)."""
    r, g, b = rgb[:, 0] * 255, rgb[:, 1] * 255, rgb[:, 2] * 255
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = 128 - 0.168736 * r - 0.331264 * g + 0.5 * b
    cr = 128 + 0.5 * r - 0.418688 * g - 0.081312 * b
    return (cb > 77) & (cb < 127) & (cr > 133) & (cr < 173) & (y > 45) & (y < 235)


def grab(spec, tag):
    """spec is a path, or 'video@t1,t2'. Returns a list of image arrays (0..1)."""
    if "@" in spec:
        path, times = spec.rsplit("@", 1)
        os.makedirs(FRAMES_DIR, exist_ok=True)
        out = []
        for i, t in enumerate(times.split(",")):
            dst = os.path.join(FRAMES_DIR, f"{tag}_{i}_{t}.png")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", path,
                            "-frames:v", "1", dst], check=True)
            out.append(load_img(dst, 960))
        return out
    return [load_img(spec, 960)]


def sample(imgs, region, skin_only):
    px = []
    for im in imgs:
        h, w, _ = im.shape
        if region:
            x0, y0, x1, y1 = region
            im = im[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)]
        px.append(im.reshape(-1, 3))
    px = np.concatenate(px)
    if skin_only:
        total = len(px)
        px = px[skin_pixels(px)]
        frac = len(px) / max(total, 1)
        if frac > 0.30 and not region:
            print(f"WARNING: skin mask covers {frac:.0%} of the sampled area. That is usually a "
                  "wall, sand or a strong color cast, not a face. Use --region on the face.",
                  file=sys.stderr)
        if len(px) < 500:
            raise SystemExit(f"only {len(px)} skin pixels found, widen --region or use another frame")
    return px


def stats(lab):
    return dict(L=float(lab[:, 0].mean()), Lsd=float(lab[:, 0].std()),
                a=float(lab[:, 1].mean()), asd=float(lab[:, 1].std()),
                b=float(lab[:, 2].mean()), bsd=float(lab[:, 2].std()))


def skin_weight(lab):
    """Soft 0..1 weight for skin-like colors (warm hue, moderate chroma) in Lab."""
    a, b = lab[:, 1], lab[:, 2]
    hue = np.degrees(np.arctan2(b, a))
    chroma = np.hypot(a, b)
    return (np.exp(-((hue - 48.0) / 28.0) ** 2) * smoothstep(3, 9, chroma)
            * (1 - smoothstep(40, 55, chroma)))


def build_transform(src_lab, tgt_lab, skin_only, strength, skin_spread=1.0):
    """skin_spread (skin-only mode): share of the color shift applied to NON-skin colors.
    0 = shift only skin-like colors, 1 = shift everything equally (old behaviour)."""
    s, t = stats(src_lab), stats(tgt_lab)
    gain_ab = lambda sd_s, sd_t: float(np.clip(sd_t / max(sd_s, 1e-3), 0.7, 1.4))
    ga, gb = gain_ab(s["asd"], t["asd"]), gain_ab(s["bsd"], t["bsd"])
    if skin_only:
        gL = float(np.clip(t["Lsd"] / max(s["Lsd"], 1e-3), 0.75, 1.33))
        qs = qt = None
    else:
        p = np.linspace(1, 99, 41)
        qs = np.concatenate([[0], np.percentile(src_lab[:, 0], p), [100]])
        qt = np.concatenate([[0], np.percentile(tgt_lab[:, 0], p), [100]])
        qs = np.maximum.accumulate(qs + np.arange(len(qs)) * 1e-6)
        qt = np.maximum.accumulate(qt)

    def fn(grid):
        lab = srgb_to_lab(grid)
        L = lab[:, 0]
        if skin_only:
            # gain and offset anchored on the skin mean, rolled off toward black and white
            Ln = t["L"] + (L - s["L"]) * gL
            Ln = L + (Ln - L) * smoothstep(0, 12, L) * (1 - smoothstep(92, 100, L))
        else:
            Ln = np.interp(L, qs, qt)
        edge = smoothstep(2, 12, L) * (1 - smoothstep(92, 100, L))
        if skin_only:
            w = skin_spread + (1 - skin_spread) * skin_weight(lab)
            edge = edge * w
        an = lab[:, 1] + ((lab[:, 1] - s["a"]) * ga + t["a"] - lab[:, 1]) * edge
        bn = lab[:, 2] + ((lab[:, 2] - s["b"]) * gb + t["b"] - lab[:, 2]) * edge
        out = lab_to_srgb(np.stack([Ln, an, bn], axis=-1))
        return grid + (out - grid) * strength

    return fn, dict(source=s, target=t, gain_a=ga, gain_b=gb, strength=strength,
                    skin_spread=skin_spread if skin_only else None,
                    mode="skin-only" if skin_only else "whole-frame")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, nargs="+", help="shot A (the one that gets fixed)")
    ap.add_argument("--target", required=True, nargs="+", help="shot B or a reference frame")
    ap.add_argument("--out", required=True, help=".cube output path")
    ap.add_argument("--skin-only", action="store_true")
    ap.add_argument("--region", help="x0,y0,x1,y1 fractions, applied to both sides")
    ap.add_argument("--src-region", help="x0,y0,x1,y1 for the source only")
    ap.add_argument("--tgt-region", help="x0,y0,x1,y1 for the target only")
    ap.add_argument("--strength", type=float, default=0.7)
    ap.add_argument("--skin-spread", type=float, default=1.0,
                    help="skin-only mode: share (0..1) of the color shift applied to non-skin colors")
    ap.add_argument("--frames-dir", help="where frames pulled from videos are saved "
                    "(default D:\\WKP\\scratch\\color\\frames)")
    ap.add_argument("--size", type=int, default=33)
    ap.add_argument("--strip-out", help="save source | matched | target PNG")
    a = ap.parse_args()
    global FRAMES_DIR
    if a.frames_dir:
        FRAMES_DIR = a.frames_dir

    reg = lambda s: tuple(float(v) for v in s.split(",")) if s else None
    src_imgs = [im for i, sp in enumerate(a.source) for im in grab(sp, f"src{i}")]
    tgt_imgs = [im for i, sp in enumerate(a.target) for im in grab(sp, f"tgt{i}")]
    src_px = sample(src_imgs, reg(a.src_region or a.region), a.skin_only)
    tgt_px = sample(tgt_imgs, reg(a.tgt_region or a.region), a.skin_only)
    src_lab, tgt_lab = srgb_to_lab(src_px), srgb_to_lab(tgt_px)
    if not a.skin_only:
        ss, tt = stats(src_lab), stats(tgt_lab)
        if abs(ss["L"] - tt["L"]) > 12 or not 0.6 < tt["Lsd"] / max(ss["Lsd"], 1e-3) < 1.67:
            print("WARNING: the two shots differ a lot in brightness or contrast (different "
                  "scenes?). Whole-frame mode forces one histogram onto the other and can wreck "
                  "the picture. Use --skin-only with --region on the face instead.", file=sys.stderr)
    fn, rep = build_transform(src_lab, tgt_lab, a.skin_only, a.strength, a.skin_spread)

    lut = build_cube(fn, a.size)
    title = os.path.splitext(os.path.basename(a.out))[0]
    write_cube(a.out, lut, title)

    # measure the result on the same pixels
    matched_px = apply_cube(src_px.reshape(-1, 1, 3), lut).reshape(-1, 3)
    rep["result"] = stats(srgb_to_lab(matched_px))
    dE = lambda x, y: float(np.sqrt((x["L"] - y["L"]) ** 2 + (x["a"] - y["a"]) ** 2 + (x["b"] - y["b"]) ** 2))
    rep["mean_color_distance_before"] = dE(rep["source"], rep["target"])
    rep["mean_color_distance_after"] = dE(rep["result"], rep["target"])
    with open(a.out + ".report.json", "w") as f:
        json.dump(rep, f, indent=1)
    print(f"wrote {a.out}")
    print(f"mode {rep['mode']}, strength {a.strength}")
    print("mean Lab  source %(L).1f %(a).1f %(b).1f" % rep["source"])
    print("mean Lab  target %(L).1f %(a).1f %(b).1f" % rep["target"])
    print("mean Lab  result %(L).1f %(a).1f %(b).1f" % rep["result"])
    print("distance between the MEAN colors only (CIE76 Lab): %.1f before, %.1f after. "
          "This says nothing about contrast, tint spread or the rest of the frame, "
          "so it can read near 0 while the picture is still wrong. Look at the strip."
          % (rep["mean_color_distance_before"], rep["mean_color_distance_after"]))

    if a.strip_out:
        cols = []
        for src in src_imgs[:1]:
            cols.append(src)
            cols.append(apply_cube(src, lut))
        cols.append(tgt_imgs[0])
        h = min(c.shape[0] for c in cols)
        cols = [np.asarray(Image.fromarray((c * 255).astype(np.uint8)).resize(
            (int(c.shape[1] * h / c.shape[0]), h))) / 255.0 for c in cols]
        save_img(np.concatenate(cols, axis=1), a.strip_out)
        print("strip:", a.strip_out)


if __name__ == "__main__":
    main()
