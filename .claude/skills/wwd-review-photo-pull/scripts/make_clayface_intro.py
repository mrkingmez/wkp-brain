# -*- coding: utf-8 -*-
"""Clayface silent intro (15.5 s, no audio, Zac reads over it live).
Beats: 0-4.5 s slow push on the premiere still (the perfect face), 4.5-9.5 s the
picture melts and drips into clay, 9.5-11.5 s the cracked-face close-up with a
slow shake, 11.5 s dark-red flash and the poster slams in, holds to the end.
Frames come from the USE PNGs of the mass record folder. Output is an opaque
H.264 MP4 (ProRes freezes on Zac's machine, see memory/topics/visual-media.md).
Usage: python make_clayface_intro.py <Clayface USE folder> <out.mp4>"""
import sys, subprocess, numpy as np
from PIL import Image

USE, OUT = sys.argv[1], sys.argv[2]
W, H, FPS, DUR = 1920, 1080, 30, 15.5
A_N, B_N, P_N = 8, 14, 1   # premiere smile, cracked face, poster

def load(n):
    im = Image.open(f"{USE}/{n}.png").convert("RGBA")
    bg = Image.new("RGBA", im.size, (0, 0, 0, 255)); bg.alpha_composite(im)
    return np.asarray(bg.convert("RGB"), dtype=np.float32)

A, B, P = load(A_N), load(B_N), load(P_N)
rng = np.random.default_rng(7)

def noise1d(n, octaves=((3, 1.0), (9, 0.5), (27, 0.25))):
    x = np.linspace(0, 1, n); out = np.zeros(n)
    for f, a in octaves:
        pts = rng.random(f + 2)
        out += a * np.interp(x * f, np.arange(f + 2), pts)
    out -= out.min(); return out / out.max()

NX = noise1d(W)
ys, xs = np.mgrid[0:H, 0:W]

def smooth(a, b, v):
    t = np.clip((v - a) / (b - a), 0, 1); return t * t * (3 - 2 * t)

def zoom(img, s, dx=0, dy=0):
    h, w = img.shape[:2]
    sy = (ys - H / 2) / s + h / 2 + dy; sx = (xs - W / 2) / s + w / 2 + dx
    sy = np.clip(sy, 0, h - 1).astype(np.int32); sx = np.clip(sx, 0, w - 1).astype(np.int32)
    return img[sy, sx]

def frame(t):
    if t < 9.5:
        base = zoom(A, 1.0 + 0.09 * t / 9.5)
        if t < 4.5:
            return np.clip(base, 0, 255)
        p = (t - 4.5) / 5.0
        # drip: every column drags its picture downward by its own amount
        d = (p ** 1.6) * (80 + 700 * NX)[None, :] * (0.25 + 0.75 * smooth(0, H, ys))
        src = np.clip(ys - d, 0, H - 1)
        y0 = src.astype(np.int32); y1 = np.clip(y0 + 1, 0, H - 1); fr = (src - y0)[..., None]
        melted = base[y0, xs] * (1 - fr) + base[y1, xs] * fr
        clay = np.array([150, 82, 62], np.float32)
        gray = melted.mean(axis=2, keepdims=True)
        tint = 0.55 * p
        melted = melted * (1 - tint) + (gray * 0.6 + clay * 0.55) * tint
        # crossfade into the cracked face, ragged edge so it reads as the drips arriving
        edge = smooth(0.55, 1.0, p + 0.25 * (NX[None, :] - 0.5) + 0.5 * (ys / H - 0.5) * p)
        return melted * (1 - edge[..., None]) + zoom(B, 1.05) * edge[..., None]
    if t < 11.5:
        k = t - 9.5
        sh = 6 * np.sin(k * 40) * (k / 2.0)
        return zoom(B, 1.05 + 0.04 * k / 2.0, dx=sh, dy=-sh * 0.6)
    k = t - 11.5
    if k < 0.12:  # dark red flash
        return np.full((H, W, 3), (120, 0, 0), np.float32) * (1 - k / 0.12) + zoom(B, 1.09) * (k / 0.12) * 0.2
    s = 1.0 + 0.16 * max(0, 1 - (k - 0.12) / 0.3) ** 2
    return zoom(P, s)

cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
       "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14",
       "-g", "15", "-bf", "0", "-movflags", "+faststart", OUT]
pr = subprocess.Popen(cmd, stdin=subprocess.PIPE)
for i in range(int(DUR * FPS)):
    pr.stdin.write(np.clip(frame(i / FPS), 0, 255).astype(np.uint8).tobytes())
pr.stdin.close(); pr.wait(); print("done", OUT)
