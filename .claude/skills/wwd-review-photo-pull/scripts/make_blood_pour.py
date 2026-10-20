"""Blood pour transition: a wet, dripping sheet of blood pours down, covers the
frame, then slides off leaving drip streaks. 1920x1080 ProRes 4444 with alpha,
splash sound baked in. Put it on a track above the cut; make the cut on the
COVER frame printed at the end.

  python make_blood_pour.py --out "P:\\WWD Kit\\Transitions\\Blood Pour.mov"
"""
import argparse, os, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage

W, H, FPS = 1920, 1080, 30
S = 2  # render at half size for speed, upscale at the end
w, h = W // S, H // S
POUR_F, HOLD_F, OFF_F = 14, 6, 34
N = POUR_F + HOLD_F + OFF_F
SPLASH = r"P:\Sounds\Sound FX\Adobe\Liquid-Water\Liquid Mud Dropped Wet Splash Hard 03.wav"
SPLAT = r"P:\Sounds\Sound FX\splat-juicy-wet_fJlSm3EO.mp3"

rng = np.random.default_rng(11)
# drip fingers on the leading edge: x, width, length, speed
DRIPS = [(rng.uniform(0, w), rng.uniform(6, 22), rng.uniform(25, 140), rng.uniform(0.7, 1.4)) for _ in range(46)]
# streaks left behind when the sheet slides off
STREAKS = [(rng.uniform(0, w), rng.uniform(2, 6), rng.uniform(0.3, 0.95), rng.uniform(0, 6.28)) for _ in range(15)]
WAVE = ndimage.gaussian_filter1d(rng.normal(0, 1, w), 18) * 60


def ease_in(t):
    return t * t


FLOW = ndimage.gaussian_filter(rng.normal(0, 1, (h * 3, w)), (45, 5))  # vertical flow texture, tall so it can slide without a seam
FLOW /= FLOW.std()
BLOT = ndimage.gaussian_filter(rng.normal(0, 1, (h, w)), 20); BLOT /= BLOT.std()


def shade(mask, i):
    """Wet look: deep red body with flowing streaks, thin bright edges, glossy highlights."""
    m = mask.astype(float)
    off = max(0, h * 2 - i * 9); flow = FLOW[off:off + h]  # texture slides down with the pour
    thick = ndimage.distance_transform_edt(mask)
    thin = np.exp(-thick / 10)  # 1 at the edge, 0 deep inside
    hgt = ndimage.gaussian_filter(m, 4) + flow * 0.02
    gy, gx = np.gradient(hgt)
    spec = np.clip((-gx * 0.5 - gy * 0.9) * 14, 0, 1) ** 3
    gloss = np.clip(flow - 2.3, 0, 1) * 0.35  # thin shiny runs inside the sheet
    dark, mid, hi = np.array([48, 0, 3]), np.array([118, 2, 8]), np.array([185, 18, 24])
    k = np.clip(0.5 + flow * 0.08 + BLOT * 0.16, 0, 1)[..., None]
    col = dark + (mid - dark) * k
    col = col + (hi - col) * (thin * 0.55)[..., None]
    col = col + (spec + gloss)[..., None] * np.array([255, 190, 190]) * 0.8
    a = ndimage.gaussian_filter(m, 0.8) * (0.93 + 0.07 * (1 - thin))
    return np.dstack([np.clip(col, 0, 255), np.clip(a * 255, 0, 255)]).astype(np.uint8)

def frame_mask(i):
    img = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(img)
    if i < POUR_F + HOLD_F:  # pouring down, then covering
        t = min(1, (i + 1) / POUR_F)
        edge = -150 + ease_in(t) * (h + 300)
        pts = [(0, 0)] + [(x, edge + WAVE[x]) for x in range(0, w, 4)] + [(w, edge + WAVE[-1]), (w, 0)]
        d.polygon(pts, fill=255)
        for x, dw, ln, sp in DRIPS:
            L = ln * sp * (0.4 + 0.6 * t)
            y0 = edge + WAVE[int(min(x, w - 1))]
            d.rounded_rectangle([x - dw / 2, y0 - 10, x + dw / 2, y0 + L], radius=dw / 2, fill=255)
            d.ellipse([x - dw * 0.7, y0 + L - dw * 0.9, x + dw * 0.7, y0 + L + dw * 0.5], fill=255)
    else:  # sliding off the bottom, leaving streaks
        t = (i - POUR_F - HOLD_F + 1) / OFF_F
        top = ease_in(t) * (h + 200) - 60
        pts = [(x, top + WAVE[x] * 0.6) for x in range(0, w, 4)] + [(w, h), (0, h)]
        d.polygon(pts, fill=255)
        for x, sw, keep, ph in STREAKS:
            if t < keep:
                y_end = top + WAVE[int(min(x, w - 1))] * 0.6
                life = 1 - t / keep
                pts = []
                for y in np.linspace(0, max(1, y_end), 40):
                    xx = x + np.sin(y / 45 + ph) * 6
                    r = sw * (0.35 + 0.65 * y / max(1, y_end)) * life + 0.6
                    pts.append((xx, y, r))
                for xx, y, r in pts:
                    d.ellipse([xx - r, y - r, xx + r, y + r], fill=255)
    m = np.asarray(img.filter(ImageFilter.GaussianBlur(4))) > 110  # rounds the drip tips
    return m


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(N):
            m = frame_mask(i)
            rgba = Image.fromarray(shade(m, i), "RGBA").resize((W, H), Image.BICUBIC)
            if i >= POUR_F + HOLD_F + OFF_F - 6:  # fade the last streaks
                k = (N - i) / 6
                rgba.putalpha(rgba.getchannel("A").point(lambda v: int(v * k)))
            rgba.save(os.path.join(tmp, f"f{i:04d}.png"))
        hit = int(POUR_F / FPS * 1000)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png"),
                        "-i", SPLASH, "-i", SPLAT,
                        "-filter_complex", f"[1:a]volume=0.8[a1];[2:a]adelay={hit}|{hit},volume=1.3[a2];[a1][a2]amix=inputs=2:normalize=0,apad[a]",
                        "-map", "0:v", "-map", "[a]", "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le",
                        "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{N / FPS:.3f}", a.out], check=True)
    print("wrote", a.out, f"| {N} frames | fully covered frames {POUR_F} to {POUR_F + HOLD_F - 1} | make the picture cut at frame {POUR_F + 2}")


if __name__ == "__main__":
    main()
