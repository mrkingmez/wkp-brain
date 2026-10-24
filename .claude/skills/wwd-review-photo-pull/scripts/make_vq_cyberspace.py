"""Vision Quest opener v2 (2026-10-23, Zac): the System Boot panel, longer, then it opens into a cyberspace world
(neon grid floor, data towers passing, binary rain, VISIONQUEST title, flash out). 10 seconds, 1920x1080, ProRes 4444
(opaque once the world is up). Original look, owned sounds only.

  python make_vq_cyberspace.py [--out "P:\\WWD Kit\\Vision Quest\\System Boot - Cyberspace.mov"] [--n 300]
"""
import argparse
import math
import os
import random
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, FPS, blank, put, ease_out, render, flash  # noqa: E402
import make_wk_kit_cl_vq as kit  # noqa: E402

SFX = "P:\\Sounds\\Sound FX\\"
SWEEP = SFX + "jg-032316-sfx-sci-fi-sweep-1.mp3"
WHOOSH = SFX + "deep-fast-whoosh_GyZDnHNu.mp3"
for p in (SWEEP, WHOOSH):
    assert os.path.exists(p), p

CYAN = (90, 225, 255)
MAG = (255, 70, 200)
HY = int(H * 0.46)          # horizon line
F = 520.0                   # projection scale


def smooth(t):
    t = min(max(t, 0.0), 1.0)
    return t * t * (3 - 2 * t)


def background(i, n, world):
    """Night gradient with a glowing horizon. world = 0..1 how far the cyberspace has opened."""
    ys = np.linspace(0, 1, H)[:, None]
    top = np.array([2, 4, 10], float)
    hor = np.array([30, 10, 70], float) * (0.3 + 0.7 * world)
    g = np.clip((ys * H - HY) / (H * 0.5), -1, 1)
    glow = np.exp(-((ys * H - HY) / 160.0) ** 2)[..., None]
    base = top + (hor - top) * np.clip(1 - np.abs(g), 0, 1)[..., None]
    base = base + glow * np.array([70, 40, 120], float) * world
    arr = np.broadcast_to(base, (H, W, 3)).astype(np.uint8)
    return Image.fromarray(arr, "RGB").convert("RGBA")


def grid_layer(t, world):
    """Perspective grid floor scrolling toward the camera."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    a = int(235 * world)
    # horizontal lines
    for k in range(40):
        z = (k + (t * 6.0) % 1.0) * 0.55 + 0.35
        y = HY + F * 0.85 / z
        if y > H:
            continue
        fade = min(1.0, (y - HY) / 80.0)
        d.line((0, y, W, y), fill=CYAN + (int(a * fade),), width=2 if y < HY + 200 else 3)
    # radial lines
    for j in range(-14, 15):
        x1 = W / 2 + j * 300
        d.line((W / 2 + j * 7, HY, x1, H), fill=CYAN + (int(a * 0.85),), width=2)
    return lay


def towers(t, world, seed=3):
    """Data towers and cubes rushing past on both sides."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    rng = random.Random(seed)
    items = []
    for m in range(22):
        side = -1 if m % 2 == 0 else 1
        X = side * rng.uniform(350, 1700)
        hgt = rng.uniform(160, 1100)
        z0 = rng.uniform(0.4, 9.0)
        col = CYAN if rng.random() < 0.65 else MAG
        items.append((z0, X, hgt, col))
    items.sort(key=lambda r: -((r[0] - t * 2.2) % 9.0 + 0.4))
    for z0, X, hgt, col in items:
        z = (z0 - t * 2.2) % 9.0 + 0.4
        sx = W / 2 + X * F / (z * 260.0) * 1.0
        base_y = HY + F * 0.85 / (z * 0.55 + 0.35) * 0.55
        w = max(6, 300 * F / (z * 260.0) * 0.5)
        h = hgt * F / (z * 260.0)
        top_y = base_y - h
        if sx + w < 0 or sx - w > W:
            continue
        al = int(min(1.0, 1.4 - z / 9.0) * 210 * world)
        d.rectangle((sx - w / 2, top_y, sx + w / 2, base_y), fill=col + (int(al * 0.12),), outline=col + (al,), width=3)
        for r in range(1, 6):
            yy = top_y + h * r / 6
            d.line((sx - w / 2, yy, sx + w / 2, yy), fill=col + (int(al * 0.4),), width=1)
    return lay


def rain_layer(i, world):
    """Falling binary columns in the sky."""
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    f = kit.font(kit.MONO, 26)
    rng = random.Random(9)
    for c in range(46):
        x = rng.randint(10, W - 30)
        sp = rng.uniform(5, 14)
        off = rng.uniform(0, H)
        for r in range(14):
            y = (off + i * sp + r * 32) % (HY + 30)
            d.text((x, y), rng.choice("01"), font=f, fill=CYAN + (int(max(0, 150 - r * 10) * world),))
    return lay


def build(n=300, out=None):
    random.seed(5)
    boot_end = 150                      # the boot panel is on screen to here
    open_from = 105                     # the world starts opening under the panel
    tfont = kit.font(kit.IMPACT, 190)
    l1, l2, l3 = "> BOOTING VISIONQUEST REVIEW", "> ENTERING THE VIRTUAL SPACE", "> LINK ESTABLISHED"
    fm = kit.font(kit.MONO, 46)
    pw, ph = 1360, 430

    def f(i):
        world = smooth((i - open_from) / 60.0)
        cv = background(i, n, world)
        if world > 0:
            t = (i - open_from) / FPS
            cv.alpha_composite(rain_layer(i, world))
            tw = towers(t, world)
            cv.alpha_composite(tw)
            gr = grid_layer(t, world)
            cv.alpha_composite(gr)
            glow = Image.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 0)), gr).filter(ImageFilter.GaussianBlur(6))
            cv.alpha_composite(glow)
        # boot panel (types in, then fades out as the world opens)
        pk = 1.0
        if i < 6:
            pk = i / 6.0
        if i > boot_end - 12:
            pk = max(0.0, (boot_end + 18 - i) / 30.0)
        if pk > 0:
            p = kit.panel(pw, ph)
            dd = ImageDraw.Draw(p)
            c1 = int(max(0, i - 4) * 1.1)
            dd.text((50, 40), l1[:c1], font=fm, fill=CYAN + (255,))
            c2 = int(max(0, i - 36) * 1.1)
            dd.text((50, 105), l2[:c2], font=fm, fill=CYAN + (255,))
            pr = max(0.0, min(1.0, (i - 28) / 78))
            dd.rectangle((50, 190, pw - 50, 222), outline=CYAN + (255,), width=3)
            dd.rectangle((54, 194, 54 + int((pw - 108) * pr), 218), fill=CYAN + (230,))
            dd.text((pw - 190, 232), f"{int(pr * 100):3d}%", font=fm, fill=CYAN + (255,))
            if i >= 108:
                dd.text((50, 290), l3[:int((i - 108) * 1.4)], font=fm, fill=(120, 255, 150, 255))
            p = kit.scan_overlay(p, i)
            s = 1.0 + 0.5 * smooth((i - 120) / 40.0)
            put(cv, p, W / 2, H / 2, scale=s, alpha=pk)
        # title over the horizon
        if i >= 185:
            ts = ease_out((i - 185) / 26.0)
            flick = 1.0 if (i % 7) < 5 else 0.55
            ti = Image.new("RGBA", (1700, 260), (0, 0, 0, 0))
            td = ImageDraw.Draw(ti)
            td.text((850, 130), "VISIONQUEST", font=tfont, fill=CYAN + (int(255 * flick),), anchor="mm", stroke_width=5, stroke_fill=(0, 30, 50, 255))
            gl = ti.filter(ImageFilter.GaussianBlur(14))
            put(cv, gl, W / 2, HY - 150, scale=0.6 + 0.4 * ts, alpha=min(1.0, ts))
            put(cv, ti, W / 2, HY - 150, scale=0.6 + 0.4 * ts, alpha=min(1.0, ts))
        # glitch slices at the open and a flash out
        if 100 <= i < 112 or 180 <= i < 186:
            rr = random.Random(i)
            for _ in range(4):
                y0 = rr.randint(0, H - 60)
                hh = rr.randint(14, 50)
                dx = rr.randint(-60, 60)
                strip = cv.crop((0, y0, W, y0 + hh))
                cv.paste(strip, (dx, y0))
        if i >= n - 12:
            flash(cv, 255 * min(1.0, (i - (n - 12)) / 8.0))
        return cv

    audio = [(kit.GLITCH, 0, 0.5), (kit.COMP, 1500, 0.35), (SWEEP, 3300, 0.8), (WHOOSH, 8900, 0.9)]
    render(f, n, out, audio)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=r"P:\WWD Kit\Vision Quest\System Boot - Cyberspace.mov")
    ap.add_argument("--n", type=int, default=300)
    a = ap.parse_args()
    build(a.n, a.out)
