"""Center-tear rip (v2). A printed photo torn straight down the vertical middle by two hands.
Crack starts top center, zips down in ~0.3 s, each half hinges on its OUTER edge (perspective
swing, up to 15 degrees) and slides fully out left and right. B sits dead flat behind.
Reuses helpers from rip.py (v1 stays untouched).

Usage: python rip_center.py --a W1a.png --b W1b.png --out out.mp4 [--frames-dir DIR]
  [--seed 7 --tear-x 0.5 --jag 14 --hold 1.2 --crack 0.3 --pull 0.8 --total 3.0 --fps 24 --dust 40]
"""
import argparse, subprocess, os, math
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
import rip
from rip import W, H, FFMPEG, contain, tear_path, build_half, smoothstep


def homography(dst, src):
    """Coeffs for PIL PERSPECTIVE: maps output (dst) pixel to input (src) pixel."""
    A, b = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    return tuple(np.linalg.solve(np.array(A, float), np.array(b, float)))


def swing_layer(rgb, alpha, side, theta, T):
    """Hinge on the outer edge, rotate about the vertical axis by theta, slide outward by T."""
    im = Image.fromarray(np.dstack([rgb.clip(0, 255), alpha * 255]).astype(np.uint8), "RGBA")
    c, s = math.cos(theta), math.sin(theta)
    cy = H / 2
    s1 = 1 + 0.5 * s  # far edge swings toward the camera, so it reads taller
    src = [(0, 0), (W, 0), (W, H), (0, H)]
    if side == "L":
        xo = -T
        dst = [(xo, 0), (xo + W * c, cy - H / 2 * s1), (xo + W * c, cy + H / 2 * s1), (xo, H)]
    else:
        xo = W + T
        dst = [(xo - W * c, cy - H / 2 * s1), (xo, 0), (xo, H), (xo - W * c, cy + H / 2 * s1)]
    return im.transform((W, H), Image.PERSPECTIVE, homography(dst, src), Image.BICUBIC)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--tear-x", type=float, default=0.5)
    ap.add_argument("--jag", type=float, default=14)
    ap.add_argument("--hold", type=float, default=1.2)
    ap.add_argument("--crack", type=float, default=0.3)
    ap.add_argument("--pull", type=float, default=0.8)  # seconds from first crack until halves are gone
    ap.add_argument("--total", type=float, default=3.0)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--dust", type=int, default=40)
    ap.add_argument("--shake", type=float, default=7)
    ap.add_argument("--frames-dir", default=None)
    a = ap.parse_args()

    rng = np.random.RandomState(a.seed)
    A, B = contain(a.a), contain(a.b)
    path = tear_path(rng, a.tear_x, 0.0, a.jag)
    halves = {s: build_half(A, path, s, rng) for s in ("R", "L")}
    Aimg = Image.fromarray(A.clip(0, 255).astype(np.uint8)).convert("RGBA")
    Bimg = Image.fromarray(B.clip(0, 255).astype(np.uint8)).convert("RGBA")

    prng = np.random.RandomState(a.seed + 101)
    parts = []
    for i in range(a.dust + 5):
        y = prng.uniform(0, H)
        side = prng.choice([-1, 1])
        bit = i >= a.dust
        parts.append(dict(y=y, x=path[int(y)] + prng.uniform(-5, 5), bit=bit,
                          vx=side * (prng.uniform(120, 420) if bit else prng.uniform(40, 360)),
                          vy=prng.uniform(-240, 80), r=prng.uniform(4, 8) if bit else prng.uniform(1, 3.2),
                          life=prng.uniform(.35, .7), rot=prng.uniform(0, 6.28), spin=prng.uniform(-9, 9)))

    n = int(round(a.total * a.fps))
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
    pull_start = a.crack * 0.75
    T_END = W * 0.5 + 160

    for f in range(n):
        tp = f / a.fps - a.hold
        if tp <= 0:
            frame = Aimg.copy()
        else:
            frame = Bimg.copy()
            front = H * 1.15 * (tp / a.crack)
            shift_f = 14 * np.clip((front - ys_f) / 260, 0, 1)
            u = min(max((tp - pull_start) / (a.pull - pull_start), 0), 1)
            e = u * u * (3 - 2 * u) * 0.35 + u ** 2.2 * 0.65  # eases out of the hinge, then accelerates away
            theta = math.radians(15) * smoothstep(u / 0.6)
            T = T_END * e
            curl = min(1.0, tp / 0.3)
            for side in ("R", "L"):
                if u >= 1:
                    continue
                rgb, al, d, wmask = halves[side]
                sh_i = np.rint(shift_f if side == "R" else -shift_f).astype(int)
                src = xs[None, :] - sh_i[:, None]
                valid = (src >= 0) & (src < W)
                idx = np.clip(src, 0, W - 1)
                rows = ys[:, None]
                rgb2 = rgb[rows, idx]
                al2 = al[rows, idx] * valid
                d2 = d[rows, idx]
                lip = np.exp(-d2 / 38.0) * 0.20 * curl
                shade = 1 - (0.12 * curl + 0.10 * u) * (1 - np.exp(-d2 / 520.0))
                gain = (shade + lip)[..., None]
                rgb2 = rgb2 * gain
                plain = A[rows, idx] * gain
                sep = np.clip(np.abs(sh_i).astype(np.float32) / 5.0, 0, 1)[:, None, None]
                wm = wmask[rows, idx][..., None]
                rgb3 = rgb2 + (plain - rgb2) * wm * (1 - sep)
                pc = swing_layer(rgb3, al2, side, theta, T)
                sa = pc.split()[3].filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.5))
                shl = Image.new("RGBA", (W, H), (0, 0, 0, 255))
                shl.putalpha(sa)
                shl = shl.transform((W, H), Image.AFFINE, (1, 0, -8 if side == "L" else 8, 0, 1, -14))
                frame = Image.alpha_composite(frame, shl)
                frame = Image.alpha_composite(frame, pc)

            if parts:
                ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                dr = ImageDraw.Draw(ov)
                for p in parts:
                    age = tp - p["y"] / H * a.crack
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

            if tp < 0.16 and a.shake > 0:  # first crack only, very short
                env = math.exp(-tp / 0.045)
                dx, dy = shakes[f, 0] * a.shake * env, shakes[f, 1] * a.shake * env
                sc = 1 + 0.012 * env
                Mi = np.linalg.inv(np.eye(2) * sc)
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
