"""A Knight's Tale end card and Next Up cards (2026-11-19). Original look: a tournament herald board,
heraldic check strips, banner frames, cyan and white with gold. Code-built with Pillow, owned sounds only,
no studio logo, font or art. Background is one heavily blurred film still used as texture only.
1920x1080, 30 fps. End card 12 s, Next Up 6 s (same as the Vision Quest cards).

  python make_akt_cards.py end
  python make_akt_cards.py next --title "PERCY JACKSON" --sub "SEASON 3 EPISODE 1" --name "Percy Jackson Season 3"
  python make_akt_cards.py next --title "NEW REVIEW" --sub "COMING TO THE DEN" --name "Next Review"
End card layout (canvas px): left tile 190..830 x 420..780, right tile 1090..1730 x 420..780,
subscribe ring centre (960, 600) r 90. Place YouTube end-screen elements there.
"""
import argparse, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, render  # noqa: E402

IMPACT = r"C:\Windows\Fonts\impact.ttf"
SERIF = r"C:\Windows\Fonts\constanb.ttf"
SERIFI = r"C:\Windows\Fonts\constani.ttf"
BG = r"L:\Winter Wolfs Den review show\Raw Footage\A Knights tale\USE\24 she takes over.png"
KIT = r"P:\WWD Kit\Cards\\"
SH = r"P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impact On Metal Shield 01.wav"
SW = r"P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impacts 02.wav"
for p in (BG, SH, SW):
    assert os.path.exists(p), p

CYAN, WHITE, GOLD = (90, 225, 255), (255, 255, 255), (255, 200, 40)
TILES = [(190, 420, 830, 780), (1090, 420, 1730, 780)]
RING = (960, 600, 90)


def fnt(p, s):
    return ImageFont.truetype(p, s)


def plate():
    im = Image.open(BG).convert("RGB").resize((W, H)).filter(ImageFilter.GaussianBlur(34))
    a = np.asarray(im).astype(float)
    g = a.mean(axis=2, keepdims=True)
    a = 0.35 * a + 0.65 * g                       # mostly desaturate
    a *= np.array([0.30, 0.55, 0.75])             # cold steel-cyan grade, dark
    yy, xx = np.mgrid[0:H, 0:W]
    a *= (1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2)[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")


def checks(d, y, h, shift, col=CYAN):
    """Heraldic check strip, two rows, scrolling by shift px."""
    s = h // 2
    for r in range(2):
        for k in range(-2, W // s + 3):
            if (k + r) % 2 == 0:
                x = k * s + (shift % (2 * s)) * (1 if r == 0 else -1)
                d.rectangle((x, y + r * s, x + s, y + (r + 1) * s), fill=col + (200,))


def frame_common(bg, i, n, title_fn):
    im = bg.copy()
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    sl = min(1.0, i / 14)                           # strips slide in
    off = int((1 - sl) * 120)
    checks(d, 30 - off, 40, i * 2)
    checks(d, H - 70 + off, 40, -i * 2)
    d.rectangle((0, 70 - off, W, 74 - off), fill=GOLD + (255,))
    d.rectangle((0, H - 74 + off, W, H - 70 + off), fill=GOLD + (255,))
    title_fn(d, ov, i)
    im = Image.alpha_composite(im, ov)
    k = 1.0
    if i < 6:
        k = i / 6
    if i > n - 8:
        k = max(0.0, (n - i) / 8)
    return Image.eval(im.convert("RGB"), lambda v: int(v * k))


def banner_tile(d, box, label, k, i):
    x0, y0, x1, y1 = box
    c = tuple(int(v * k) for v in CYAN)
    d.rectangle(box, fill=(6, 18, 26, int(110 * k)), outline=c + (255,), width=4)
    d.rectangle((x0 - 10, y0 - 10, x1 + 10, y1 + 10), outline=tuple(int(v * k) for v in GOLD) + (255,), width=2)
    d.rectangle((x0 - 24, y0 - 62, x1 + 24, y0 - 50), fill=tuple(int(v * k) for v in GOLD) + (255,))   # hanging rod
    for xx in (x0, x1):
        d.line((xx, y0 - 50, xx, y0 - 2), fill=c + (255,), width=3)
    d.text(((x0 + x1) // 2, y0 - 84), label, font=fnt(SERIF, 34), fill=c + (255,), anchor="mm")
    d.polygon([(x0, y1 + 12), (x1, y1 + 12), (x1, y1 + 56), ((x0 + x1) // 2, y1 + 34), (x0, y1 + 56)],
              fill=tuple(int(v * k * 0.5) for v in CYAN) + (255,))   # swallowtail


def end_title(d, ov, i):
    if i >= 8:
        k = min(1.0, (i - 8) / 10)
        d.text((960, 120), "THE LISTS ARE CLOSED", font=fnt(SERIFI, 52), fill=tuple(int(v * k) for v in CYAN) + (255,), anchor="mm")
    if i >= 36:
        k = min(1.0, (i - 36) / 8)
        d.text((960, 235), "THANKS FOR WATCHING", font=fnt(IMPACT, 104), anchor="mm",
               fill=tuple(int(v * k) for v in WHITE) + (255,), stroke_width=5, stroke_fill=(50, 30, 0, int(255 * k)))
    if i >= 20:
        k = min(1.0, (i - 20) / 10)
        for box, lab in zip(TILES, ["LATEST UPLOAD", "BEST FOR YOU"]):
            banner_tile(d, box, lab, k, i)
        cx, cy, r = RING
        rr = int(r * (1 + 0.04 * np.sin(i * 0.22)))
        c = tuple(int(v * k) for v in CYAN) + (255,)
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=c, width=6)
        d.text((cx, cy + r + 42), "SUBSCRIBE", font=fnt(SERIF, 36), fill=c, anchor="mm")
    if i >= 70:
        k = min(1.0, (i - 70) / 12)
        d.text((960, 905), "NEXT: FROSTCAST, EVERY WEDNESDAY 9 PM ET", font=fnt(SERIF, 50),
               fill=tuple(int(v * k) for v in WHITE) + (255,), anchor="mm")
    if i >= 110:
        k = min(1.0, (i - 110) / 12)
        d.text((960, 972), "THE WINTER WOLF'S DEN", font=fnt(SERIFI, 40),
               fill=tuple(int(v * k) for v in GOLD) + (255,), anchor="mm")


def make_next_title(title, sub):
    def fn(d, ov, i):
        if i >= 8:
            k = min(1.0, (i - 8) / 8)
            x = int(-600 * (1 - k))
            d.text((960 + x, 330), "NEXT UP", font=fnt(IMPACT, 110), anchor="mm",
                   fill=tuple(int(v * k) for v in WHITE) + (255,), stroke_width=4, stroke_fill=(50, 30, 0, int(255 * k)))
        if i >= 30:
            k = min(1.0, (i - 30) / 6)
            size = 230
            while fnt(IMPACT, size).getlength(title) > 1560:
                size -= 6
            sc = 1 + 0.25 * (1 - k)
            lay = Image.new("RGBA", (W, 400), (0, 0, 0, 0))
            ld = ImageDraw.Draw(lay)
            ld.text((960, 200), title, font=fnt(IMPACT, size), anchor="mm", fill=GOLD + (int(255 * k),),
                    stroke_width=5, stroke_fill=(60, 30, 0, int(255 * k)))
            lay = lay.resize((int(W * sc), int(400 * sc)), Image.LANCZOS)
            ov.alpha_composite(lay, (960 - lay.width // 2, 560 - lay.height // 2))
        if i >= 62:
            k = min(1.0, (i - 62) / 8)
            d.text((960, 740), sub, font=fnt(SERIF, 80), anchor="mm", fill=tuple(int(v * k) for v in CYAN) + (255,))
            d.line((460, 810, 1460, 810), fill=tuple(int(v * k) for v in GOLD) + (255,), width=4)
        if i >= 80:
            k = min(1.0, (i - 80) / 8)
            d.text((960, 880), "THE WINTER WOLF'S DEN", font=fnt(SERIFI, 44), anchor="mm",
                   fill=tuple(int(v * k) for v in GOLD) + (255,))
    return fn


def finish(out, frame, n, audio):
    render(frame, n, out, audio, alpha=False)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", out.replace(".mov", " (MP4).mp4")], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["end", "next"])
    ap.add_argument("--title", default="NEW REVIEW")
    ap.add_argument("--sub", default="COMING TO THE DEN")
    ap.add_argument("--name", default="Next Review")
    ap.add_argument("--outdir", default=KIT)
    a = ap.parse_args()
    bg = plate()
    if a.kind == "end":
        n, out = 360, os.path.join(a.outdir, "End Card - A Knights Tale.mov")
        f = lambda i: frame_common(bg, i, n, end_title)
        finish(out, f, n, [(SH, 0, 0.4), (SH, 1200, 0.5), (SW, 2350, 0.4)])
        f(200).save(out.replace(".mov", ".png"))
    else:
        n, out = 180, os.path.join(a.outdir, f"Next Up - {a.name}.mov")
        tf = make_next_title(a.title, a.sub)
        f = lambda i: frame_common(bg, i, n, tf)
        finish(out, f, n, [(SH, 250, 0.4), (SH, 1000, 0.55), (SW, 2060, 0.4)])
    print("done", out)


if __name__ == "__main__":
    main()
