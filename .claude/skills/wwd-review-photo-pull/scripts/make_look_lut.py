"""make_look_lut.py - build a color look as a .cube 3D LUT (Premiere Lumetri Input LUT,
DaVinci Resolve free node LUT) from parameters, a named preset, or a reference frame.

Built 2026-10-25 for the wwd-color bench. Needs numpy, scipy, Pillow and ffmpeg only
(no opencv). Input is assumed to be Rec709 display-referred video (what Premiere and
Resolve show for normal webcam and screen-recorded footage). Not for log footage.

Examples (python = the interpreter in LOCAL-PATHS.md):
  python make_look_lut.py --preset clayface_safe --out "P:\\WWD Kit\\Color\\Clayface Safe 2026-10-25.cube"
  python make_look_lut.py --preset clayface_bold --out ... --strip frame1.png frame2.png --strip-out strip.png
  python make_look_lut.py --params my_look.json --out my.cube
  python make_look_lut.py --reference ref_frame.png --out ref_look.cube   (approximate, see below)
  python make_look_lut.py --list-presets

Pipeline order: exposure, temperature/tint, CDL (slope, offset, power), contrast S-curve,
zone tints (shadows, mids, highs), saturation with skin protection, black floor,
highlight shoulder, clip. All numbers live in the PRESETS dict below or a JSON file,
so any look can be rebuilt and nudged.

Also writes <out>.cdl.txt with the global CDL numbers (slope/offset/power/sat) for typing into
a Resolve primary wheel or Lumetri by hand. CDL covers only the simple part of the look,
the .cube is the whole look.

Reference mode is a rough estimate from one frame's statistics (levels, shadow and highlight
tint, saturation). It assumes a neutral starting point, so treat it as a starting look and
compare it against the frame yourself.
"""
import argparse
import json
import os
import subprocess
import sys

import numpy as np
from PIL import Image
from scipy.ndimage import map_coordinates

LUMA = np.array([0.2126, 0.7152, 0.0722])
SKIN_HUE = 0.0   # degrees in atan2(Q, I) space, see skin_mask

NEUTRAL = dict(
    exposure=0.0,        # stops, applied in linear light
    temp=0.0,            # + warm, - cool (linear light gain on R and B)
    tint=0.0,            # + magenta, - green
    slope=[1.0, 1.0, 1.0],
    offset=[0.0, 0.0, 0.0],
    power=[1.0, 1.0, 1.0],
    contrast=1.0,        # S curve strength around pivot (1 = none)
    pivot=0.42,
    shadow_rgb=[0.5, 0.5, 0.5], shadow_amt=0.0, shadow_range=0.45,
    mid_rgb=[0.5, 0.5, 0.5], mid_amt=0.0,
    high_rgb=[0.5, 0.5, 0.5], high_amt=0.0, high_range=0.55,
    sat=1.0,
    skin_sat=1.0,        # saturation applied to skin-hue pixels instead of sat
    skin_warm=0.0,       # small red/yellow push on skin pixels only
    skin_width=26.0,     # degrees either side of the skin line in YIQ hue
    skin_tint_protect=0.0,  # 0..1: how much the shadow/mid/highlight tints are held back on skin
                            # (added 2026-10-25: tints were draining skin chroma 40 to 60 percent)
    floor=0.0, floor_rgb=[0.5, 0.5, 0.5],   # black floor (lift), tinted
    knee=1.0,            # highlight shoulder start (1.0 = off)
    accent_hue=-1.0,     # degrees (HSV hue, 0 = red). -1 = off. Keeps one color alive
    accent_width=16.0,   # while the rest is drained (added 2026-10-25)
    accent_boost=1.0,    # saturation multiplier applied on top of sat inside the accent hue
)

PRESETS = {
    "neutral": {},
    # Cold, wet, low key. Desaturated world, warm skin kept alive, a hint of green-teal
    # in the shadows. The safe option for Clayface.
    "clayface_safe": dict(
        exposure=-0.32, temp=-0.05, tint=-0.02,
        power=[1.04, 1.0, 1.0],
        contrast=1.17, pivot=0.40,
        shadow_rgb=[0.28, 0.56, 0.52], shadow_amt=0.34, shadow_range=0.42,
        mid_rgb=[0.42, 0.55, 0.55], mid_amt=0.10,
        high_rgb=[0.50, 0.54, 0.58], high_amt=0.07, high_range=0.58,
        sat=0.72, skin_sat=0.95, skin_warm=0.012,
        floor=0.016, floor_rgb=[0.25, 0.55, 0.50],
        knee=0.84,
    ),
    # Same world pushed harder: crushed blacks, green-teal shadows you can see, sickly
    # green-grey mids, wet clay amber only in the brightest highlights, skin pulled warm
    # so faces read as clay against a drained room.
    "clayface_bold": dict(
        exposure=-0.22, temp=-0.04, tint=-0.05,
        power=[1.10, 1.02, 1.04],
        slope=[1.0, 1.0, 0.98],
        contrast=1.30, pivot=0.38,
        shadow_rgb=[0.15, 0.60, 0.50], shadow_amt=0.55, shadow_range=0.50,
        mid_rgb=[0.40, 0.58, 0.48], mid_amt=0.20,
        high_rgb=[0.66, 0.53, 0.40], high_amt=0.18, high_range=0.60,
        sat=0.62, skin_sat=0.98, skin_warm=0.030,
        floor=0.010, floor_rgb=[0.18, 0.60, 0.46],
        knee=0.80,
    ),
}


def smoothstep(a, b, x):
    t = np.clip((x - a) / (b - a), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def luma(x):
    return x @ LUMA


def contrast_curve(x, c, pivot):
    """Continuous, monotone S curve around pivot. c > 1 adds contrast."""
    if abs(c - 1.0) < 1e-6:
        return x
    x = np.clip(x, 0.0, 1.0)
    lo = pivot * np.power(np.clip(x / pivot, 0, None), c)
    hi = 1 - (1 - pivot) * np.power(np.clip((1 - x) / (1 - pivot), 0, None), c)
    return np.where(x < pivot, lo, hi)


def skin_mask(rgb, width_deg):
    """1 near the skin line, faded by chroma so greys and saturated non-skin colors are
    excluded. BUG FIXED 2026-10-25: hue here is atan2(Q, I), where skin sits near 0 degrees
    (measured on real skin: median -6 to +4). The old center of 123 degrees is the vectorscope
    convention, so the mask was always 0 and skin_sat, skin_warm never did anything."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    i = 0.596 * r - 0.274 * g - 0.322 * b
    q = 0.211 * r - 0.523 * g + 0.312 * b
    hue = np.degrees(np.arctan2(q, i))
    d = np.abs((hue - SKIN_HUE + 180.0) % 360.0 - 180.0)
    hmask = np.exp(-(d / width_deg) ** 2)
    chroma = np.hypot(i, q)
    cmask = smoothstep(0.02, 0.07, chroma) * (1 - smoothstep(0.30, 0.50, chroma))
    return hmask * cmask


def apply_look(rgb, p):
    """rgb float array (..., 3) in 0..1. Returns array of same shape."""
    P = dict(NEUTRAL)
    P.update(p)
    x = np.clip(rgb.astype(np.float64), 0, 1)
    skin = skin_mask(x, P["skin_width"])

    # exposure and white balance in linear light
    lin = np.power(x, 2.2)
    lin = lin * (2.0 ** P["exposure"])
    t, ti = P["temp"], P["tint"]
    lin = lin * np.array([1 + t * 0.35 + ti * 0.10, 1 - ti * 0.35, 1 - t * 0.35 + ti * 0.10])
    x = np.power(np.clip(lin, 0, None), 1 / 2.2)

    # CDL
    x = np.clip(x * np.array(P["slope"]) + np.array(P["offset"]), 0, None)
    x = np.power(x, np.array(P["power"]))
    x = np.clip(x, 0, 1)

    # contrast
    x = contrast_curve(x, P["contrast"], P["pivot"])

    # zone tints (zero-mean color offsets, so they shift hue without changing luma much)
    y = luma(x)[..., None]
    w_s = (1 - smoothstep(0.0, P["shadow_range"], y)) ** 1.5
    w_h = smoothstep(P["high_range"], 1.0, y)
    w_m = 4 * y * (1 - y)

    def off(col):
        col = np.array(col)
        return col - luma(col)

    keep = 1.0 - P["skin_tint_protect"] * skin[..., None]
    x = x + keep * P["shadow_amt"] * w_s * off(P["shadow_rgb"]) * 0.5
    x = x + keep * P["mid_amt"] * w_m * off(P["mid_rgb"]) * 0.5
    x = x + keep * P["high_amt"] * w_h * off(P["high_rgb"]) * 0.5

    # saturation with skin protection
    y = luma(x)[..., None]
    sat = P["sat"] * (1 - skin[..., None]) + P["skin_sat"] * skin[..., None]
    x = y + (x - y) * sat

    # accent color: re-boost one hue so it survives a heavy desaturation
    if P["accent_hue"] >= 0 and P["accent_boost"] != 1.0:
        r_, g_, b_ = x[..., 0], x[..., 1], x[..., 2]
        hue = np.degrees(np.arctan2(np.sqrt(3) * (g_ - b_), 2 * r_ - g_ - b_)) % 360.0
        dh = np.abs((hue - P["accent_hue"] + 180.0) % 360.0 - 180.0)
        ch = np.max(x, axis=-1) - np.min(x, axis=-1)
        am = np.exp(-(dh / P["accent_width"]) ** 2) * smoothstep(0.06, 0.18, ch) * (1 - skin)
        y2 = luma(x)[..., None]
        x = y2 + (x - y2) * (1 + am[..., None] * (P["accent_boost"] - 1))

    # skin warmth
    if P["skin_warm"]:
        x = x + skin[..., None] * P["skin_warm"] * np.array([1.0, 0.35, -0.7])

    # black floor with tint
    if P["floor"]:
        fl = np.array(P["floor_rgb"])
        x = x * (1 - P["floor"]) + P["floor"] * (0.5 + (fl - luma(fl)) * 1.2) * 0.9

    # highlight shoulder
    k = P["knee"]
    if k < 1.0:
        over = np.clip(x - k, 0, None)
        x = np.where(x > k, k + (1 - k) * np.tanh(over / (1 - k)), x)

    return np.clip(x, 0, 1)


# ---------------------------------------------------------------- cube io
def build_cube(fn, size=33):
    """Evaluate fn on a size^3 grid. .cube order: red changes fastest."""
    g = np.linspace(0, 1, size)
    b, gg, r = np.meshgrid(g, g, g, indexing="ij")   # axis0=B, axis1=G, axis2=R
    grid = np.stack([r, gg, b], axis=-1).reshape(-1, 3)
    out = fn(grid)
    return np.clip(out, 0, 1).reshape(size, size, size, 3)  # [b, g, r, ch]


def write_cube(path, lut, title):
    size = lut.shape[0]
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", newline="\n") as f:
        f.write(f'TITLE "{title}"\n')
        f.write(f"LUT_3D_SIZE {size}\n")
        f.write("DOMAIN_MIN 0.0 0.0 0.0\nDOMAIN_MAX 1.0 1.0 1.0\n")
        for row in lut.reshape(-1, 3):
            f.write(f"{row[0]:.6f} {row[1]:.6f} {row[2]:.6f}\n")


def read_cube(path):
    size = None
    vals = []
    with open(path) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#") or s.startswith("TITLE"):
                continue
            if s.startswith("LUT_3D_SIZE"):
                size = int(s.split()[1])
            elif s.startswith("DOMAIN") or s.startswith("LUT_1D"):
                continue
            else:
                vals.append([float(v) for v in s.split()])
    arr = np.array(vals)
    return arr.reshape(size, size, size, 3)


def apply_cube(img_rgb01, lut):
    """Trilinear apply of lut[b,g,r,ch] to an image array (H,W,3) in 0..1."""
    n = lut.shape[0] - 1
    h, w, _ = img_rgb01.shape
    c = np.clip(img_rgb01, 0, 1).reshape(-1, 3) * n
    out = np.empty_like(c)
    coords = [c[:, 2], c[:, 1], c[:, 0]]       # b, g, r
    for ch in range(3):
        out[:, ch] = map_coordinates(lut[..., ch], coords, order=1, mode="nearest")
    return out.reshape(h, w, 3)


def load_img(path, max_w=None):
    im = Image.open(path).convert("RGB")
    if max_w and im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    return np.asarray(im, dtype=np.float64) / 255.0


def save_img(arr, path):
    Image.fromarray((np.clip(arr, 0, 1) * 255 + 0.5).astype(np.uint8)).save(path)


def ffmpeg_apply(src, cube, dst):
    """Independent check: ffmpeg's own lut3d filter reads the same .cube."""
    cube_ff = cube.replace("\\", "/").replace(":", "\\:")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf",
                    f"lut3d=file='{cube_ff}':interp=trilinear", dst], check=True)


def make_strip(before_paths, lut, out_path, width=640):
    rows = []
    for p in before_paths:
        a = load_img(p, width)
        b = apply_cube(a, lut)
        rows.append(np.concatenate([a, b], axis=1))
    save_img(np.concatenate(rows, axis=0), out_path)


# ---------------------------------------------------------------- reference mode
def params_from_reference(path):
    """Rough look parameters from one reference frame. Assumes neutral start."""
    a = load_img(path, 640).reshape(-1, 3)
    y = luma(a)
    keep = (y > 0.03) & (y < 0.97)            # ignore letterbox bars and clipped titles
    a, y = a[keep], y[keep]
    p = dict(NEUTRAL)
    p5, p50, p95 = np.percentile(y, [5, 50, 95])
    p["contrast"] = float(np.clip(1.0 + (0.62 - (p95 - p5)) * 0.9, 0.9, 1.35))
    p["exposure"] = float(np.clip(np.log2(max(p50, 1e-3) / 0.42) * 0.6, -0.6, 0.4))
    chroma = np.linalg.norm(a - y[:, None], axis=1)
    p["sat"] = float(np.clip(np.mean(chroma) / 0.17, 0.5, 1.3))

    def zone(mask):
        col = a[mask].mean(axis=0)
        return (col - luma(col)) / max(np.linalg.norm(col - luma(col)), 1e-6), np.linalg.norm(col - luma(col))

    lo, hi = y < np.percentile(y, 30), y > np.percentile(y, 80)
    if lo.sum() > 50:
        d, mag = zone(lo)
        p["shadow_rgb"] = (0.5 + d * 0.5).tolist()
        p["shadow_amt"] = float(np.clip(mag * 5, 0, 0.6))
    if hi.sum() > 50:
        d, mag = zone(hi)
        p["high_rgb"] = (0.5 + d * 0.5).tolist()
        p["high_amt"] = float(np.clip(mag * 5, 0, 0.5))
    p["floor"] = float(np.clip(np.percentile(y, 1) * 0.5, 0, 0.04))
    return p


def params_from_reference_fit(ref_path, src_paths):
    """Source-aware reference mode. Fits exposure, contrast, saturation, temp and tint so the
    SOURCE frame(s) end up with the reference frame's luma spread and color stats (Lab).
    Added 2026-10-25 after the one-frame estimate (params_from_reference) failed a
    known-answer test: it cannot know how saturated or bright the source starts."""
    from scipy.optimize import minimize
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from match_shots_lut import srgb_to_lab        # lazy import: that module imports this one

    ref = load_img(ref_path, 320).reshape(-1, 3)
    ref = ref[(luma(ref) > 0.03) & (luma(ref) < 0.97)]
    src = np.concatenate([load_img(s, 320).reshape(-1, 3) for s in src_paths])
    src = src[::max(1, len(src) // 12000)]
    q = [2, 10, 25, 50, 75, 90, 98]

    def sig(rgb):
        lab = srgb_to_lab(rgb)
        return np.concatenate([np.percentile(lab[:, 0], q), [lab[:, 1].mean(), lab[:, 2].mean(),
                                                             lab[:, 1].std(), lab[:, 2].std()]])

    target = sig(ref)
    wts = np.array([1.0] * 7 + [3.0, 3.0, 1.5, 1.5])

    def mk(v):
        return dict(exposure=v[0], contrast=v[1], sat=v[2], temp=v[3], tint=v[4])

    def loss(v):
        v = np.clip(v, [-2, 0.6, 0.2, -0.5, -0.5], [2, 2.5, 2.5, 0.5, 0.5])
        return float((np.abs(sig(apply_look(src, mk(v))) - target) * wts).sum())

    r = minimize(loss, [0, 1.0, 1.0, 0, 0], method="Nelder-Mead",
                 options=dict(maxiter=500, xatol=1e-3, fatol=1e-3))
    v = np.clip(r.x, [-2, 0.6, 0.2, -0.5, -0.5], [2, 2.5, 2.5, 0.5, 0.5])
    p = dict(NEUTRAL)
    p.update(mk(v))
    p["_fit_loss"] = float(r.fun)
    return p


# ---------------------------------------------------------------- correction helpers
def params_neutral(path, region):
    """White balance from a patch that should be neutral grey or white.
    region = x0,y0,x1,y1 as fractions of the frame. Returns slope gains (CDL, gamma space)."""
    a = load_img(path, 640)
    h, w, _ = a.shape
    x0, y0, x1, y1 = region
    patch = a[int(y0 * h):int(y1 * h), int(x0 * w):int(x1 * w)].reshape(-1, 3)
    m = patch.mean(axis=0)
    gain = np.clip(m.mean() / np.maximum(m, 1e-3), 0.7, 1.4)
    gain = gain / (gain @ LUMA)          # keep brightness
    return gain


def params_auto_levels(paths, gain=None, black=0.04, white=0.96, lo=1.0, hi=99.0,
                       max_slope=2.2):
    """Set black and white points from the luma percentiles of one or more frames.
    Returns slope/offset so lo-percentile lands on `black` and hi-percentile on `white`.
    Pushing a lot (slope near max_slope) on 8-bit footage can band: check the render."""
    ys = []
    for p in paths:
        a = load_img(p, 640).reshape(-1, 3)
        if gain is not None:
            a = np.clip(a * gain, 0, 1)
        ys.append(luma(a))
    y = np.concatenate(ys)
    plo, phi = np.percentile(y, [lo, hi])
    slope = float(np.clip((white - black) / max(phi - plo, 1e-3), 0.6, max_slope))
    offset = black - slope * plo
    return slope, float(offset), float(plo), float(phi)


def cdl_text(p):
    P = dict(NEUTRAL)
    P.update(p)
    return ("CDL (global part only; the .cube is the whole look)\n"
            f"slope  {P['slope']}\noffset {P['offset']}\npower  {P['power']}\n"
            f"saturation {P['sat']}  (skin pixels use {P['skin_sat']})\n"
            f"exposure {P['exposure']} stops, temp {P['temp']}, tint {P['tint']}, "
            f"contrast {P['contrast']} around {P['pivot']}\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--preset", choices=sorted(PRESETS))
    ap.add_argument("--params", help="JSON file of parameters (overrides preset keys)")
    ap.add_argument("--reference", help="reference frame image, estimate a look from it")
    ap.add_argument("--out", help=".cube output path")
    ap.add_argument("--size", type=int, default=33)
    ap.add_argument("--title", default=None)
    ap.add_argument("--strip", nargs="+", help="frames to render as before|after rows")
    ap.add_argument("--strip-out", help="where to save the before/after strip PNG")
    ap.add_argument("--list-presets", action="store_true")
    ap.add_argument("--source", nargs="+", metavar="FRAME",
                    help="with --reference: fit the look to turn THESE source frames into the "
                         "reference (accurate). Without it, --reference is a rough one-frame estimate.")
    ap.add_argument("--auto-levels", nargs="+", metavar="FRAME",
                    help="CORRECTION: set black and white points from these frames (flat or hazy clips)")
    ap.add_argument("--neutral", nargs=2, metavar=("FRAME", "x0,y0,x1,y1"),
                    help="CORRECTION: white balance from a patch that should be neutral (fractions of frame)")
    a = ap.parse_args()

    if a.list_presets:
        print("\n".join(sorted(PRESETS)))
        return
    if not a.out:
        ap.error("--out is required")
    p = {}
    if a.reference and a.source:
        p.update(params_from_reference_fit(a.reference, a.source))
        print("fit loss (lower is closer):", round(p.pop("_fit_loss"), 2))
    elif a.reference:
        p.update(params_from_reference(a.reference))
        print("NOTE: one-frame reference estimate. It assumes a neutral start and failed a "
              "known-answer test (made frames worse). Add --source FRAME to fit it properly.")
    if a.preset:
        p.update(PRESETS[a.preset])
    if a.params:
        with open(a.params) as f:
            p.update(json.load(f))
    gain = None
    if a.neutral:
        gain = params_neutral(a.neutral[0], tuple(float(v) for v in a.neutral[1].split(",")))
        p["slope"] = gain.tolist()
        print("neutral patch gains (R,G,B):", np.round(gain, 3))
    if a.auto_levels:
        s, o, plo, phi = params_auto_levels(a.auto_levels, gain)
        p["slope"] = (np.array(p.get("slope", [1, 1, 1])) * s).tolist()
        p["offset"] = [o, o, o]
        print(f"auto levels: frame 1st/99th luma percentile {plo:.3f}/{phi:.3f} -> slope {s:.2f}, offset {o:.3f}"
              + ("  (WARNING: strong push, 8-bit footage may band)" if s > 1.8 else ""))
    lut = build_cube(lambda g: apply_look(g, p), a.size)
    title = a.title or os.path.splitext(os.path.basename(a.out))[0]
    write_cube(a.out, lut, title)
    with open(a.out + ".cdl.txt", "w") as f:
        f.write(cdl_text(p))
    with open(a.out + ".params.json", "w") as f:
        json.dump({k: p[k] for k in p}, f, indent=1, default=lambda o: o.tolist())
    print(f"wrote {a.out} (size {a.size}, {lut.shape[0] ** 3} entries)")
    if a.strip:
        make_strip(a.strip, lut, a.strip_out or (a.out + ".strip.png"))
        print("strip:", a.strip_out or (a.out + ".strip.png"))


if __name__ == "__main__":
    main()
