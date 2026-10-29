# -*- coding: utf-8 -*-
"""Clayface silent intro v2 (22 s, no audio, Zac reads over it live).
One face slowly pushes in and goes wrong: each shot melts into the next through a
liquid warp while a clay tint builds, ends on the animated clay monster, a dip to
black, then the poster rises out of the dark with a back-light bloom and a slam.
Shots are aligned on the face (cx, cy as fractions of the 1920x1080 frame) so the
morph reads as one head changing, not a slideshow.
Output is an opaque H.264 MP4 (ProRes freezes on Zac's machine).
Usage: python make_clayface_intro_v2.py <Clayface USE folder> <out.mp4> [preview <dir>]"""
import sys, subprocess, numpy as np
from PIL import Image

USE, OUT = sys.argv[1], sys.argv[2]
PREVIEW = sys.argv[3:5] if len(sys.argv) > 4 and sys.argv[3] == "preview" else None
W, H, FPS, DUR = 1920, 1080, 30, 22.0
if PREVIEW:
    W, H = 960, 540

# (picture, face cx, face cy, base zoom). cx/cy are where the face sits in the picture.
SHOTS = [
    (8, 0.39, 0.38, 2.6),   # clean premiere smile
    (2, 0.60, 0.33, 2.8),   # hand pulling at cheek
    (9, 0.30, 0.50, 1.9),   # face smoothed over, hand on it
    (14, 0.50, 0.50, 1.7),  # cracked half face
    (19, 0.57, 0.50, 2.4),  # face squashed on glass
    (17, 0.43, 0.50, 2.4),  # bloody grin
    (24, 0.68, 0.22, 2.2),  # animated clay monster
]
# start time of each shot, morph length into the next
STARTS = [0.0, 3.0, 5.0, 7.0, 9.4, 11.6, 13.8]
MORPH = [1.1, 1.0, 1.1, 1.1, 1.0, 1.3]
END_SHOTS = 16.2   # monster ends, dip to black
POSTER_AT = 17.0

def load(n):
    im = Image.open(f"{USE}/{n}.png").convert("RGBA")
    bg = Image.new("RGBA", im.size, (0, 0, 0, 255)); bg.alpha_composite(im)
    return np.asarray(bg.convert("RGB"), dtype=np.float32)

PICS = [load(s[0]) for s in SHOTS]
POSTER = load(1)
# poster art sits in the middle of the 1920x1080 PNG, find its real width for the side-bar fill
_cols = np.where(POSTER.mean(axis=(0, 2)) > 8)[0]
POSTER_HALF_W = (_cols.max() - _cols.min()) / 2.0
from PIL import ImageFilter
_bd = Image.fromarray(POSTER.astype(np.uint8)).crop((int(_cols.min()), 0, int(_cols.max()), 1080))
BACKDROP = np.asarray(_bd.resize((1920, 1080), Image.BILINEAR).filter(ImageFilter.GaussianBlur(40)).resize((W, H)), dtype=np.float32)
rng = np.random.default_rng(11)
ys, xs = np.mgrid[0:H, 0:W].astype(np.float32)
SC = W / 1920.0

def smooth(a, b, v):
    t = np.clip((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

def field(seed, scale):
    """low-frequency smooth noise field, 0..1, size HxW"""
    r = np.random.default_rng(seed)
    gh, gw = max(2, int(H / scale)), max(2, int(W / scale))
    g = r.random((gh + 1, gw + 1)).astype(np.float32)
    im = Image.fromarray((g * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)
    return np.asarray(im, dtype=np.float32) / 255.0

F1, F2 = field(1, 260 * SC), field(2, 260 * SC)
F3 = field(3, 90 * SC)

def sample(img, sx, sy):
    h, w = img.shape[:2]
    sx = np.clip(sx, 0, w - 1); sy = np.clip(sy, 0, h - 1)
    x0 = sx.astype(np.int32); y0 = sy.astype(np.int32)
    x1 = np.clip(x0 + 1, 0, w - 1); y1 = np.clip(y0 + 1, 0, h - 1)
    fx = (sx - x0)[..., None]; fy = (sy - y0)[..., None]
    return ((img[y0, x0] * (1 - fx) + img[y0, x1] * fx) * (1 - fy) +
            (img[y1, x0] * (1 - fx) + img[y1, x1] * fx) * fy)

def view(i, lt, dxw=0.0, dyw=0.0):
    """shot i seen at local time lt: face-centered, slow push, optional warp (pixels in 1920 space)"""
    n, cx, cy, z0 = SHOTS[i]
    img = PICS[i]
    z = z0 * (1.0 + 0.07 * lt / 3.0)
    sx = (xs - W / 2) / (z * SC) + cx * 1920 + dxw
    sy = (ys - H / 2) / (z * SC) + cy * 1080 + dyw
    return sample(img, sx, sy)

def clay(img, amt):
    gray = img.mean(axis=2, keepdims=True)
    tone = np.array([150, 88, 66], np.float32)
    return img * (1 - amt) + (gray * 0.55 + tone * 0.6) * amt

def shot_frame(t):
    i = max(k for k in range(len(SHOTS)) if t >= STARTS[k])
    lt = t - STARTS[i]
    prog = i / (len(SHOTS) - 1)
    if i < len(SHOTS) - 1:
        m0 = STARTS[i + 1] - MORPH[i]
        if t >= m0:
            p = (t - m0) / MORPH[i]
            e = p * p * (3 - 2 * p)
            # liquid warp: both pictures are pulled along the same flowing field, opposite directions
            amp = 70 * np.sin(np.pi * e) + 8
            fx = (F1 - 0.5) * 2 * amp * 2; fy = (F2 - 0.5) * 2 * amp * 2 + 40 * e
            a = view(i, lt, fx * e, fy * e)
            b = view(i + 1, 0.0, -fx * (1 - e), -fy * (1 - e))
            # ragged melting edge instead of a flat crossfade
            edge = smooth(0.0, 1.0, e * 1.4 + (F3 - 0.5) * 0.9 + (ys / H - 0.5) * 0.5 * e)
            out = a * (1 - edge[..., None]) + b * edge[..., None]
            return clay(out, 0.55 * (prog + e / (len(SHOTS) - 1)))
    return clay(view(i, lt), 0.55 * prog)

def lens(img, t, strength=1.0):
    """Spielberg touch: horizontal anamorphic streak on the brightest spots, soft vignette, film grain"""
    lum = img.mean(axis=2)
    hot = np.clip((lum - 170) / 60, 0, 1)
    streak = hot.copy()
    k = int(60 * SC)
    for _ in range(3):
        streak = (streak + np.roll(streak, k, 1) * 0.6 + np.roll(streak, -k, 1) * 0.6) / 2.2
    blue = np.array([0.55, 0.75, 1.0], np.float32)
    img = img + streak[..., None] * blue * 120 * strength
    v = 1 - 0.38 * smooth(0.45, 1.0, np.sqrt(((xs / W - 0.5) * 1.3) ** 2 + ((ys / H - 0.5) * 1.6) ** 2) * 1.4)
    img = img * v[..., None]
    grain = np.random.default_rng(int(t * 30)).normal(0, 5, (H, W, 1)).astype(np.float32)
    return img + grain

def poster_frame(t):
    k = t - POSTER_AT
    z = 1.0 + 0.16 * max(0, 1 - k / 0.35) ** 2 + 0.015 * k
    sx = (xs - W / 2) / (z * SC) + 960; sy = (ys - H / 2) / (z * SC) + 540
    p = sample(POSTER, sx, sy)
    # the poster is portrait, so fill the side bars with a dark blurred red copy of itself
    side = np.abs(xs - W / 2) > (POSTER_HALF_W * z * SC)
    p = np.where(side[..., None], BACKDROP * np.array([0.42, 0.10, 0.10], np.float32), p)
    # back-light bloom rising behind the poster, then settling
    bloom = np.exp(-(((xs / W - 0.5) * 2.2) ** 2 + ((ys / H - 0.45) * 1.6) ** 2)) * 90 * max(0, 1 - k / 3.0)
    p = p + bloom[..., None] * np.array([1.0, 0.25, 0.2], np.float32)
    fade = smooth(0, 0.35, k)
    flash = max(0, 1 - k / 0.14)
    out = p * fade + np.array([140, 0, 0], np.float32) * flash * 0.8
    return out

def frame(t):
    if t < END_SHOTS:
        f = lens(shot_frame(t), t)
        # heartbeat pulse every ~1.4 s, stronger as the clay takes over
        beat = (np.exp(-((t % 1.4) / 0.12) ** 2) + 0.6 * np.exp(-(((t % 1.4) - 0.28) / 0.12) ** 2))
        f = f * (1 + 0.05 * beat * (0.5 + t / END_SHOTS))
        if t < 1.0:
            f = f * smooth(0.0, 1.0, t)   # open from black
        return f
    if t < POSTER_AT:
        d = 1 - smooth(END_SHOTS, END_SHOTS + 0.5, t)
        return lens(shot_frame(END_SHOTS - 0.01), t) * d
    return poster_frame(t)

if PREVIEW:
    import os; os.makedirs(PREVIEW[1], exist_ok=True)
    for t in [0.5, 2.2, 3.6, 4.6, 6.0, 8.0, 9.0, 10.2, 12.6, 14.4, 16.0, 17.1, 17.4, 19.0]:
        Image.fromarray(np.clip(frame(t), 0, 255).astype(np.uint8)).save(f"{PREVIEW[1]}/t{t:05.2f}.png")
    print("preview done"); sys.exit()

cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
       "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14",
       "-g", "15", "-bf", "0", "-movflags", "+faststart", OUT]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    pr.stdin.write(np.clip(frame(i / FPS), 0, 255).astype(np.uint8).tobytes())
pr.stdin.close(); pr.wait(); print("done", OUT)
