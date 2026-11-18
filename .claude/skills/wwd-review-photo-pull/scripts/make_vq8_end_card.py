"""Vision Quest EP 8 FINALE end card (2026-11-15). Same VQ-OS monitor look as the Next Up cards,
but a SESSION END screen: end-screen layout (two tile boxes + subscribe ring), FrostCast plug,
monitor powers down in the last second. No next-review title (hosts do not name one). Original look,
owned sounds only, no studio logos, fonts or art. 12 s, 1920x1080, 30 fps.

  python make_vq8_end_card.py
Writes P:\WWD Kit\Cards\End Card - Vision Quest Finale.mov (+ " (MP4).mp4" and .png)
Layout in canvas px (1920x1080): left tile 190..830 x 420..780, right tile 1090..1730 x 420..780,
subscribe ring centre (960, 600) r 90. Place YouTube end-screen elements on these.
"""
import os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, render  # noqa: E402

MONO = r"C:\Windows\Fonts\consolab.ttf"
IMPACT = r"C:\Windows\Fonts\impact.ttf"
SFX = "P:\Sounds\Sound FX\\"
COMP = SFX + "Adobe\Imaging Elements\Module Production Element Title Imaging Digital Computer Beeps Static 01.wav"
TICK = SFX + "Adobe\Technology\Technology Electronic Buttons Arcade Game Buttons Single 01.wav"
GLITCH = SFX + "Adobe\Imaging Elements\Module Production Element Title Imaging Beeps Digital Glitch 01.wav"
PDOWN = SFX + "Adobe\Production Elements\Production Element Title Transition Electrical Power Down 01.wav"
for p in (COMP, TICK, GLITCH, PDOWN):
    assert os.path.exists(p), p

N = 360
SHUT = 318                      # shutdown starts
GREEN, CYAN, GOLD = (120, 255, 160), (90, 225, 255), (255, 200, 40)
GX0, GY0, GX1, GY1 = 36, 36, 1884, 1044          # glass
TILES = [(190, 420, 830, 780), (1090, 420, 1730, 780)]
RING = (960, 600, 90)
rng = np.random.default_rng(11)


def fnt(p, s):
    return ImageFont.truetype(p, s)


def base():
    im = Image.new("RGB", (W, H), (8, 9, 12))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, W - 1, H - 1), 40, fill=(120, 120, 128), outline=(60, 60, 66), width=8)
    return im


def typed(d, x, y, text, start, i, font, col, cps=1.6):
    c = int(max(0, i - start) * cps)
    if c > 0:
        d.text((x, y), text[:c], font=font, fill=col)
    return c >= len(text)


def glass(i):
    gw, gh = GX1 - GX0, GY1 - GY0
    sc = Image.new("RGB", (gw, gh), (10, 40, 36))
    d = ImageDraw.Draw(sc)
    ox, oy = -GX0, -GY0             # draw in canvas coords
    fm, fs, fl = fnt(MONO, 44), fnt(MONO, 32), fnt(MONO, 30)

    def T(x, y, *a, **k):
        d.text((x + ox, y + oy), *a, **k)

    T(110, 62, "VQ-OS v8.0   //   SESSION END", font=fs, fill=(60, 140, 120))
    d.line((110 + ox, 112 + oy, 1810 + ox, 112 + oy), fill=(40, 100, 90), width=2)
    for start, y, text, col in [(6, 135, "> SERIES ........ VISION QUEST", GREEN),
                                (20, 190, "> STATUS ........ FINALE COMPLETE", (255, 230, 120)),
                                (34, 245, "> SESSION ....... CLOSING", GREEN)]:
        c = int(max(0, i - start) * 1.6)
        if c > 0:
            T(110, y, text[:c], font=fm, fill=col)
    # headline
    if i >= 50:
        k = min(1.0, (i - 50) / 6)
        fl_ = 1.0 if (i % 5) < 4 or i > 75 else 0.6
        T(960, 348, "THANKS FOR WATCHING", font=fnt(IMPACT, 96), anchor="mm",
          fill=tuple(int(c * fl_ * k) for c in (255, 255, 255)))
    # tiles + subscribe ring appear at 30
    if i >= 30:
        k = min(1.0, (i - 30) / 10)
        flick = 1.0 if (i % 4) < 3 or i > 48 else 0.5
        col = tuple(int(c * k * flick) for c in CYAN)
        dim = tuple(int(c * k * flick) for c in (60, 140, 130))
        labels = ["> LATEST UPLOAD", "> BEST FOR YOU"]
        for (x0, y0, x1, y1), lab in zip(TILES, labels):
            d.rectangle((x0 + ox, y0 + oy, x1 + ox, y1 + oy), fill=(8, 30, 28), outline=col, width=3)
            L = 34
            for (cx, cy, sx, sy) in [(x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)]:
                d.line((cx + ox - 8 * sx, cy + oy - 8 * sy, cx + ox - 8 * sx + L * sx, cy + oy - 8 * sy), fill=col, width=5)
                d.line((cx + ox - 8 * sx, cy + oy - 8 * sy, cx + ox - 8 * sx, cy + oy - 8 * sy + L * sy), fill=col, width=5)
            T(x0, y0 - 40, lab, font=fl, fill=dim)
        cx, cy, r = RING
        pulse = 1 + 0.04 * np.sin(i * 0.22)
        rr = int(r * pulse)
        d.ellipse((cx - rr + ox, cy - rr + oy, cx + rr + ox, cy + rr + oy), outline=col, width=5)
        T(cx, cy + r + 38, "SUBSCRIBE", font=fl, fill=col, anchor="mm")
    # FrostCast plug
    t1 = typed(d, 110 + ox, 862 + oy, "> NEXT: FROSTCAST, LIVE WEDNESDAYS 9 PM ET", 70, i, fnt(MONO, 46), CYAN)
    typed(d, 110 + ox, 930 + oy, "> SEE YOU IN THE NEXT ONE, WHATEVER IT MAY BE", 112, i, fnt(MONO, 36), GREEN)
    if i < SHUT and (i // 8) % 2 == 0 and i > 150:
        d.rectangle((1790 + ox, 935 + oy, 1812 + ox, 970 + oy), fill=GREEN)
    arr = np.asarray(sc).astype(float)
    arr[::4] *= 0.84
    yy, xx = np.mgrid[0:gh, 0:gw]
    arr *= (1 - 0.38 * (((xx - gw / 2) / (gw / 2)) ** 2 + ((yy - gh / 2) / (gh / 2)) ** 2) / 2)[..., None]
    arr *= 0.96 + 0.04 * np.sin(i * 1.9)
    arr += rng.normal(0, 3.0, arr.shape)
    by = int((i * 11) % (gh + 200)) - 100
    arr[max(0, by):max(0, by + 60)] *= 1.1
    if 48 <= i <= 52:
        s = int(rng.integers(-40, 40)); r0 = int(rng.integers(100, gh - 160))
        arr[r0:r0 + 90] = np.roll(arr[r0:r0 + 90], s, axis=1)
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def frame(i):
    im = base()
    g = glass(i)
    m = Image.new("L", g.size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, g.width - 1, g.height - 1), 30, fill=255)
    led = (60, 255, 120)
    if i >= SHUT:                                   # CRT collapse to a line, then a dot
        j = (i - SHUT) / 18.0
        if j < 1:
            hh = max(3, int(g.height * (1 - j) ** 2.2)); ww = g.width
        else:
            hh = 3; ww = max(6, int(g.width * max(0.0, 1 - (j - 1) * 1.6)))
        bg = Image.new("RGB", g.size, (0, 0, 0))
        g2 = g.resize((ww, hh)) if (ww > 0 and hh > 0) else g
        bg.paste(g2, ((g.width - ww) // 2, (g.height - hh) // 2))
        g = bg
        led = (200, 40, 40)
    im.paste(g, (GX0, GY0), m)
    ImageDraw.Draw(im).ellipse((1830, 1052 - 8, 1848, 1052 + 10), fill=led) if False else None
    halo = im.filter(ImageFilter.GaussianBlur(40))
    im = Image.blend(im, Image.eval(halo, lambda v: min(255, int(v * 1.25))), 0.18)
    k = 1.0
    if i < 6:
        k = i / 6
    if i > N - 8:
        k = max(0.0, (N - i) / 8)
    return Image.eval(im, lambda v: int(v * k)).convert("RGBA")


def main():
    out = r"P:\WWD Kit\Cards\End Card - Vision Quest Finale.mov"
    audio = [(COMP, 0, 0.35), (TICK, 300, 0.5), (TICK, 700, 0.5), (TICK, 1100, 0.5), (GLITCH, 1650, 0.55),
             (TICK, 2400, 0.4), (PDOWN, int(SHUT / 30 * 1000) - 150, 0.6)]
    render(frame, N, out, audio, alpha=False)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", out.replace(".mov", " (MP4).mp4")], check=True)
    frame(200).convert("RGB").save(out.replace(".mov", ".png"))
    print("done")


if __name__ == "__main__":
    main()
