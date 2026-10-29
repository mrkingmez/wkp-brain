"""'NEXT UP: VISION QUEST EPS 3 + 4' end card drawn as an old computer monitor (2026-10-25).
Original look, owned sounds only, no studio logos, fonts or art.

  python make_vq34_next_up.py [--title "VISION QUEST"] [--sub "EPISODES 3 + 4"]
Writes P:\\WWD Kit\\Cards\\Next Up - Vision Quest 3 and 4.mov (+ MP4 copy for Zac's machine).
"""
import argparse, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, blank, render  # noqa: E402

MONO = r"C:\Windows\Fonts\consolab.ttf"
IMPACT = r"C:\Windows\Fonts\impact.ttf"
SFX = "P:\\Sounds\\Sound FX\\"
COMP = SFX + "Adobe\\Imaging Elements\\Module Production Element Title Imaging Digital Computer Beeps Static 01.wav"
TICK = SFX + "Adobe\\Technology\\Technology Electronic Buttons Arcade Game Buttons Single 01.wav"
GLITCH = SFX + "Adobe\\Imaging Elements\\Module Production Element Title Imaging Beeps Digital Glitch 01.wav"
for p in (COMP, TICK, GLITCH):
    assert os.path.exists(p), p

N = 180
GREEN = (120, 255, 160)
CYAN = (90, 225, 255)
SX0, SY0, SX1, SY1 = 190, 70, 1730, 900          # screen rectangle
rng = np.random.default_rng(7)


def fnt(path, size):
    return ImageFont.truetype(path, size)


def base_monitor():
    """Static room, bezel, stand. Screen area is left black here."""
    im = Image.new("RGB", (W, H), (8, 9, 12))
    d = ImageDraw.Draw(im)
    # bezel (beige-grey plastic)
    d.rounded_rectangle((SX0 - 70, SY0 - 55, SX1 + 70, SY1 + 85), 46, fill=(150, 150, 156), outline=(70, 70, 76), width=8)
    d.rounded_rectangle((SX0 - 52, SY0 - 38, SX1 + 52, SY1 + 40), 30, fill=(92, 92, 98))
    # power LED and button
    d.ellipse((SX1 - 40, SY1 + 52, SX1 - 22, SY1 + 70), fill=(60, 255, 120))
    d.rounded_rectangle((SX1 - 140, SY1 + 50, SX1 - 80, SY1 + 72), 6, fill=(44, 44, 48), outline=(20, 20, 24))
    # stand
    d.polygon([(860, SY1 + 85), (1060, SY1 + 85), (1100, 1010), (820, 1010)], fill=(44, 44, 48))
    d.rounded_rectangle((700, 1010, 1220, 1050), 14, fill=(52, 52, 56), outline=(20, 20, 24), width=3)
    return im


def screen_layer(i):
    """Everything that happens on the glass, as an RGB image the size of the screen."""
    sw, sh = SX1 - SX0, SY1 - SY0
    sc = Image.new("RGB", (sw, sh), (10, 40, 36))
    d = ImageDraw.Draw(sc)
    fm = fnt(MONO, 44)
    fs = fnt(MONO, 34)
    d.text((40, 28), "VQ-OS v3.4   //   REVIEW TERMINAL", font=fs, fill=(60, 140, 120))
    d.line((40, 78, sw - 40, 78), fill=(40, 100, 90), width=2)

    lines = [
        (10, "> LOADING NEXT REVIEW ...", GREEN),
        (36, "> SERIES ........ VISION QUEST", GREEN),
        (62, "> EPISODES ...... 3 + 4  FOUND", GREEN),
        (88, "> ACCESS ........ GRANTED", (255, 230, 120)),
    ]
    y = 120
    for start, text, col in lines:
        c = int(max(0, i - start) * 1.6)
        d.text((40, y), text[:c], font=fm, fill=col)
        y += 58
    # progress bar after the lines
    pr = max(0.0, min(1.0, (i - 92) / 30))
    if i >= 92:
        d.rectangle((40, y + 10, sw - 40, y + 44), outline=CYAN, width=3)
        d.rectangle((44, y + 14, 44 + int((sw - 88) * pr), y + 40), fill=CYAN)

    # title reveal
    if i >= 126:
        k = min(1.0, (i - 126) / 6)
        flick = 1.0 if (i % 5) < 4 or i > 150 else 0.55
        small = fnt(IMPACT, 80)
        big = fnt(IMPACT, 190)
        sub = fnt(IMPACT, 96)
        cx = sw // 2
        ty = 440
        d.rectangle((0, ty - 30, sw, sh), fill=(10, 40, 36))
        d.text((cx, ty + 20), "NEXT UP", font=small, fill=tuple(int(c * flick * k) for c in (255, 255, 255)), anchor="mm")
        d.text((cx, ty + 140), "VISION QUEST", font=big, fill=tuple(int(c * flick * k) for c in (255, 200, 40)), anchor="mm",
               stroke_width=4, stroke_fill=(60, 30, 0))
        d.text((cx, ty + 275), "EPISODES 3 + 4", font=sub, fill=tuple(int(c * flick * k) for c in CYAN), anchor="mm")
    # blinking cursor
    if i < 126 and (i // 8) % 2 == 0:
        d.rectangle((40, y + 70, 64, y + 110), fill=GREEN)
    arr = np.asarray(sc).astype(float)
    # scanlines
    arr[::4] *= 0.84
    # soft vignette
    yy, xx = np.mgrid[0:sh, 0:sw]
    v = 1 - 0.38 * (((xx - sw / 2) / (sw / 2)) ** 2 + ((yy - sh / 2) / (sh / 2)) ** 2) / 2
    arr *= v[..., None]
    # flicker, noise, rolling band
    arr *= 0.96 + 0.04 * np.sin(i * 1.9)
    arr += rng.normal(0, 3.0, arr.shape)
    band_y = int((i * 11) % (sh + 200)) - 100
    arr[max(0, band_y):max(0, band_y + 60)] *= 1.12
    # glitch line jump at the reveal
    if 124 <= i <= 128:
        s = int(rng.integers(-40, 40))
        r0 = int(rng.integers(100, sh - 160))
        arr[r0:r0 + 90] = np.roll(arr[r0:r0 + 90], s, axis=1)
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=r"P:\WWD Kit\Cards\Next Up - Vision Quest 3 and 4.mov")
    a = ap.parse_args()
    base = base_monitor()
    # CRT glow cast on the bezel
    def frame(i):
        im = base.copy()
        sc = screen_layer(i)
        # rounded-corner screen mask
        m = Image.new("L", sc.size, 0)
        ImageDraw.Draw(m).rounded_rectangle((0, 0, sc.width - 1, sc.height - 1), 36, fill=255)
        im.paste(sc, (SX0, SY0), m)
        halo = im.filter(ImageFilter.GaussianBlur(40))
        im = Image.blend(im, Image.eval(halo, lambda v: min(255, int(v * 1.25))), 0.18)
        # fade in from black, fade out at the end
        k = 1.0
        if i < 6:
            k = i / 6
        if i > N - 10:
            k = max(0.0, (N - i) / 10)
        out = Image.eval(im, lambda v: int(v * k)).convert("RGBA")
        return out

    audio = [(COMP, 0, 0.35), (TICK, 330, 0.5), (TICK, 1200, 0.5), (TICK, 2060, 0.5), (TICK, 2930, 0.5), (GLITCH, 4150, 0.6)]
    render(frame, N, a.out, audio, alpha=False)
    mp4 = a.out.replace(".mov", " (MP4).mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.out, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", mp4], check=True)
    print("wrote", mp4)


if __name__ == "__main__":
    main()
