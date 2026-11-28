"""Torn-photo rip transition. Free tools only: Python 3 + Pillow + numpy + ffmpeg.

Usage:
  python rip.py --a W1a.png --b W1b.png --out out.mp4
     [--seed 7 --tear-x 0.5 --slope 0.10 --jag 40 --hold 1.2 --rip 0.7
      --total 3.0 --fps 24 --shake 14 --no-dust --frames-dir DIR]

Props: seed changes the tear shape; tear-x (0..1) is where the tear starts at mid height;
slope is the diagonal lean (px per px, 0 = vertical); jag is the roughness in px;
hold = seconds of photo A before the rip; rip = seconds from first crack until the
halves are gone; total = clip length.
Photos are contain-fit (never cropped) with blurred fill if the aspect differs. 1920x1080.
"""
import argparse, subprocess, os, math
import numpy as np
from PIL import Image, ImageFilter, ImageDraw

W, H = 1920, 1080
PAPER = np.array([246, 243, 236], np.float32)
FFMPEG = r"C:\Users\kingz\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"


def contain(path):
    im = Image.open(path).convert("RGB")
    s = min(W / im.width, H / im.height)
    fg = im.resize((max(1, round(im.width * s)), max(1, round(im.height * s))), Image.LANCZOS)
    if fg.size == (W, H):
        return np.asarray(fg, np.float32)
    bg = im.resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(40))
    bg = Image.eval(bg, lambda v: int(v * 0.55))
    bg.paste(fg, ((W - fg.width) // 2, (H - fg.height) // 2))
    return np.asarray(bg, np.float32)


def smooth_noise(rng, n, period, amp):
    k = int(n / period) + 3
    v = rng.uniform(-1, 1, k)
    xs = np.arange(n) / period
    i = xs.astype(int)
    f = xs - i
    f = f * f * (3 - 2 * f)
    return amp * (v[i] * (1 - f) + v[i + 1] * f)


def tear_path(rng, tx, slope, jag):
    ys = np.arange(H, dtype=np.float32)
    p = tx * W + slope * (ys - H / 2)
    p += smooth_noise(rng, H, 230, jag) + smooth_noise(rng, H, 75, jag * .42) + smooth_noise(rng, H, 24, jag * .18)
    for _ in range(16):  # sharp teeth
        c = rng.uniform(0, H)
        w = rng.uniform(10, 34)
        a = rng.uniform(-1, 1) * jag * .6
        p += a * np.clip(1 - np.abs(ys - c) / w, 0, 1)
    return p.astype(np.float32)


def build_half(img, path, side, rng):
    xs = np.arange(W, dtype=np.float32)[None, :]
    micro = smooth_noise(rng, H, 5, 3.0) + smooth_noise(rng, H, 2, 1.6)
    edge = (path + micro + (2.5 if side == "L" else -2.5)).astype(np.float32)[:, None]
    d = (edge - xs) if side == "L" else (xs - edge)  # distance inside piece from the tear edge
    wband = (7 + smooth_noise(rng, H, 14, 5) + smooth_noise(rng, H, 4, 3)).clip(2, 22)[:, None]
    fib = rng.uniform(0, 1, (H, W)).astype(np.float32)
    ragged = d + (fib - .5) * 7 + smooth_noise(rng, H, 3, 2.5)[:, None]  # fuzzy fibrous fringe
    alpha = np.clip(ragged + .5, 0, 1)
    t = np.clip((wband - d) / 3.0 + (fib - .5) * .9, 0, 1)  # peeled-emulsion white band
    t2 = np.clip((wband * 1.9 - d) / 9.0 + (fib - .5) * 1.1, 0, 1) * .55  # pale halo
    white = np.clip(np.maximum(t, t2), 0, 1)[..., None]
    paper = PAPER * (0.93 + 0.07 * rng.uniform(0, 1, (H, W, 1)).astype(np.float32))
    rgb = img * (1 - white) + paper * white
    rgb = np.where(alpha[..., None] > 0, rgb, PAPER)
    return rgb.astype(np.float32), alpha.astype(np.float32), np.maximum(d, 0).astype(np.float32), white[..., 0]


def affine_layer(rgb, alpha, pivot, ang, scale_xy, trans):
    """Forward map p' = pivot + trans + R(ang) S (p - pivot), done as an inverse affine."""
    c, s = math.cos(ang), math.sin(ang)
    M = np.array([[c, -s], [s, c]]) @ np.diag(scale_xy)
    Mi = np.linalg.inv(M)
    pv = np.array(pivot, float)
    tr = np.array(trans, float)
    off = pv - Mi @ (pv + tr)
    data = (Mi[0, 0], Mi[0, 1], off[0], Mi[1, 0], Mi[1, 1], off[1])
    im = Image.fromarray(np.dstack([rgb.clip(0, 255), alpha * 255]).astype(np.uint8), "RGBA")
    return im.transform((W, H), Image.AFFINE, data, Image.BICUBIC)


def smoothstep(x):
    x = min(max(x, 0), 1)
    return x * x * (3 - 2 * x)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--tear-x", type=float, default=0.5)
    ap.add_argument("--slope", type=float, default=0.10)
    ap.add_argument("--jag", type=float, default=40)
    ap.add_argument("--hold", type=float, default=1.2)
    ap.add_argument("--rip", type=float, default=0.7)
    ap.add_argument("--total", type=float, default=3.0)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--shake", type=float, default=14)
    ap.add_argument("--no-dust", action="store_true")
    ap.add_argument("--frames-dir", default=None)
    a = ap.parse_args()

    rng = np.random.RandomState(a.seed)
    A = contain(a.a)
    B = contain(a.b)
    path = tear_path(rng, a.tear_x, a.slope, a.jag)
    halves = {s: build_half(A, path, s, rng) for s in ("R", "L")}

    prng = np.random.RandomState(a.seed + 101)
    parts = []
    if not a.no_dust:
        for _ in range(150):
            y = prng.uniform(0, H)
            side = prng.choice([-1, 1])
            parts.append(dict(y=y, x=path[int(y)] + prng.uniform(-6, 6), vx=side * prng.uniform(40, 420) + prng.uniform(-80, 80),
                              vy=prng.uniform(-260, 120), r=prng.uniform(1, 3.6), life=prng.uniform(.25, .7), bit=False))
        for _ in range(16):
            y = prng.uniform(0, H)
            side = prng.choice([-1, 1])
            parts.append(dict(y=y, x=path[int(y)], vx=side * prng.uniform(120, 520), vy=prng.uniform(-300, 80),
                              r=prng.uniform(4, 9), life=prng.uniform(.4, .8), bit=True,
                              rot=prng.uniform(0, 6.28), spin=prng.uniform(-9, 9)))

    n = int(round(a.total * a.fps))
    t_rip = a.hold
    prop = 0.15  # seconds for the crack to run top to bottom
    if a.frames_dir:
        os.makedirs(a.frames_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    ff = subprocess.Popen([FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                           "-r", str(a.fps), "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "14",
                           "-pix_fmt", "yuv420p", "-r", str(a.fps), "-movflags", "+faststart", a.out], stdin=subprocess.PIPE)
    ys = np.arange(H)
    xs = np.arange(W)
    ys_f = ys.astype(np.float32)
    shakes = np.random.RandomState(a.seed + 5).uniform(-1, 1, (n + 2, 3))
    Bimg = Image.fromarray(B.clip(0, 255).astype(np.uint8))

    for f in range(n):
        t = f / a.fps
        tp = t - t_rip
        bs = 1.03 - 0.03 * smoothstep(tp / 1.2) if tp > 0 else 1.03  # backdrop settles in
        frame = Bimg.transform((W, H), Image.AFFINE, (1 / bs, 0, W / 2 * (1 - 1 / bs), 0, 1 / bs, H / 2 * (1 - 1 / bs)),
                               Image.BICUBIC).convert("RGBA")
        push = 1.0 + 0.02 * min(t / a.hold, 1.0)
        trem = np.zeros(2)
        if -0.14 < tp < 0:
            k = (1 + tp / .14) * 3.2
            trem = np.array([shakes[f, 0] * k, shakes[f, 1] * k])
        shift_f = np.zeros(H, np.float32)
        ang = {"L": 0.0, "R": 0.0}
        tr = {"L": np.zeros(2), "R": np.zeros(2)}
        curl = 0.0
        if tp > 0:
            front = H * 1.25 * (tp / prop)
            shift_f = 20 * np.clip((front - ys_f) / 320, 0, 1)
            u = max((tp - 0.10) / max(a.rip - 0.10, .05), 0)
            e = u * u * (1 + .6 * u)  # accelerating fall
            ang["L"] = -0.55 * e
            tr["L"] = np.array([-W * 0.95 * e, H * 0.50 * e])
            ang["R"] = 0.62 * e
            tr["R"] = np.array([W * 0.95 * e, H * 0.62 * e])
            curl = min(1.0, tp / 0.3)

        pieces = []
        for side in ("R", "L"):
            rgb, al, d, wmask = halves[side]
            sh_i = np.rint(shift_f if side == "R" else -shift_f).astype(int)
            src = xs[None, :] - sh_i[:, None]
            valid = (src >= 0) & (src < W)
            idx = np.clip(src, 0, W - 1)
            rows = ys[:, None]
            rgb2 = rgb[rows, idx]
            al2 = al[rows, idx] * valid
            d2 = d[rows, idx]
            lip = np.exp(-d2 / 38.0) * 0.20 * curl  # lit paper lip at the tear
            shade = 1 - 0.20 * curl * (1 - np.exp(-d2 / 520.0))
            gain = (shade + lip)[..., None]
            rgb2 = rgb2 * gain
            plain = A[rows, idx] * gain
            sep = np.clip(np.abs(sh_i).astype(np.float32) / 5.0, 0, 1)[:, None, None]
            wm = wmask[rows, idx][..., None]
            rgb3 = rgb2 + (plain - rgb2) * wm * (1 - sep)  # fibres only appear once the halves part
            sx = 1 - 0.05 * curl
            if tp <= 0:
                lay = affine_layer(rgb3, al2, (W / 2, H / 2), 0.0, (push, push), trem)
            else:
                pv = (0, H) if side == "L" else (W, 0)
                lay = affine_layer(rgb3, al2, pv, ang[side], (sx, 1), tr[side])
            pieces.append(lay)

        for pc in pieces:
            if tp > 0:
                sa = pc.split()[3].filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.55))
                shl = Image.new("RGBA", (W, H), (0, 0, 0, 255))
                shl.putalpha(sa)
                shl = shl.transform((W, H), Image.AFFINE, (1, 0, -10, 0, 1, -18))
                frame = Image.alpha_composite(frame, shl)
            frame = Image.alpha_composite(frame, pc)

        if tp > 0 and parts:
            ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            dr = ImageDraw.Draw(ov)
            for p in parts:
                age = tp - p["y"] / H * prop
                if age < 0 or age > p["life"]:
                    continue
                x = p["x"] + p["vx"] * age
                y = p["y"] + p["vy"] * age + 700 * age * age
                al = int(255 * (1 - age / p["life"]) ** 1.3 * .9)
                r = p["r"]
                if p["bit"]:
                    th = p["rot"] + p["spin"] * age
                    pts = [(x + r * math.cos(th + k * 2.1 + .3 * k), y + r * .7 * math.sin(th + k * 2.1)) for k in range(4)]
                    dr.polygon(pts, fill=(246, 243, 236, al))
                else:
                    dr.ellipse((x - r, y - r, x + r, y + r), fill=(236, 230, 218, al))
            frame = Image.alpha_composite(frame, ov.filter(ImageFilter.GaussianBlur(.8)))

        if tp > 0 and a.shake > 0 and tp < 0.5:
            env = math.exp(-tp / 0.11)
            if env > 0.02:
                dx, dy = shakes[f, 0] * a.shake * env, shakes[f, 1] * a.shake * env
                sc = 1 + 0.035 * env
                rot = shakes[f, 2] * 0.006 * env
                c, s = math.cos(rot), math.sin(rot)
                Mi = np.linalg.inv(np.array([[c, -s], [s, c]]) * sc)
                cen = np.array([W / 2, H / 2])
                off = cen - Mi @ (cen + [dx, dy])
                frame = frame.transform((W, H), Image.AFFINE, (Mi[0, 0], Mi[0, 1], off[0], Mi[1, 0], Mi[1, 1], off[1]), Image.BICUBIC)

        out = frame.convert("RGB")
        if a.frames_dir:
            out.save(os.path.join(a.frames_dir, f"f{f:03d}.png"))
        ff.stdin.write(out.tobytes())
    ff.stdin.close()
    ff.wait()
    print("rendered", a.out, n, "frames")


if __name__ == "__main__":
    main()
