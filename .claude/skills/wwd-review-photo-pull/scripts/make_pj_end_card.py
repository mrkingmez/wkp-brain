r"""Percy Jackson S3 (Eps 1 and 2) end card, 2026-11-23. Original look: night-sky star chart, constellation
lines drawing in, bronze rules, cyan and white. Code-built (Pillow), owned sounds only, no studio logo/font/art.
Background: one heavily blurred show still used as texture only (USE\artemis-huntresses-arrive-snow.png).
1920x1080, 30 fps, 12 s (360 frames). Same slots as the AKT card.
ZONES (YouTube end screen, same as AKT/VQ cards): tiles (190,420,830,780) and (1090,420,1730,780),
subscribe ring centre (960,600) r 90. Drawn from frame 20, stay to last frame; fade is on the whole picture
only at the last 8 frames (kit house style). Sounds: P:\Sounds\Sound FX\Adobe\Impacts\ (owned).
  python make_pj_end_card.py --outdir <dir>
"""
import argparse, os, subprocess, sys, random
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, render  # noqa: E402

IMPACT = r"C:\Windows\Fonts\impact.ttf"
SERIF = r"C:\Windows\Fonts\constanb.ttf"
SERIFI = r"C:\Windows\Fonts\constani.ttf"
BG = r"L:\Winter Wolfs Den review show\Raw Footage\Percey Jackson\Season 3\EP 1 and 2\USE\artemis-huntresses-arrive-snow.png"
SH = r"P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impact On Metal Shield 01.wav"
SW = r"P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impacts 02.wav"
for p in (BG, SH, SW):
    assert os.path.exists(p), p
CYAN, WHITE, BRONZE = (90, 225, 255), (255, 255, 255), (214, 160, 80)
TILES = [(190, 420, 830, 780), (1090, 420, 1730, 780)]
RING = (960, 600, 90)
TEXT = {}  # name -> box, filled at draw time for the touch test

def fnt(p, s): return ImageFont.truetype(p, s)

def plate():
    im = Image.open(BG).convert("RGB").resize((W, H)).filter(ImageFilter.GaussianBlur(40))
    a = np.asarray(im).astype(float); g = a.mean(axis=2, keepdims=True)
    a = (0.25 * a + 0.75 * g) * np.array([0.22, 0.42, 0.70])
    yy, xx = np.mgrid[0:H, 0:W]
    a *= (1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2)[..., None]
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).convert("RGBA")

random.seed(7)
STARS = [(random.randint(0, W), random.randint(90, H - 90), random.random() * 6.28, random.choice([2, 2, 3, 4])) for _ in range(120)]
# constellation (a rough bow shape) kept to the left and right margins, away from tiles and text
CONST = [(70, 330), (130, 250), (200, 210), (270, 260), (300, 340)]
CONST2 = [(1850, 330), (1790, 255), (1720, 215), (1650, 260), (1620, 340)]

def dim(c, k, a=255): return tuple(int(v * k) for v in c) + (a,)

def tile(d, box, label, k):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(4, 14, 28, int(120 * k)), outline=dim(CYAN, k), width=4)
    d.rectangle((x0 - 10, y0 - 10, x1 + 10, y1 + 10), outline=dim(BRONZE, k), width=2)
    for cx, cy, sx, sy in ((x0, y0, 1, 1), (x1, y0, -1, 1), (x0, y1, 1, -1), (x1, y1, -1, -1)):   # star-chart corner ticks
        d.line((cx - 22 * sx, cy, cx + 40 * sx, cy), fill=dim(BRONZE, k), width=4)
        d.line((cx, cy - 22 * sy, cx, cy + 40 * sy), fill=dim(BRONZE, k), width=4)
    d.text(((x0 + x1) // 2, y0 - 50), label, font=fnt(SERIF, 34), fill=dim(CYAN, k), anchor="mm")

def lines(d, pts, k, i, t0):
    seg = max(0.0, min(len(pts) - 1, (i - t0) / 10))
    for j in range(len(pts) - 1):
        f = max(0.0, min(1.0, seg - j))
        if f > 0:
            (x0, y0), (x1, y1) = pts[j], pts[j + 1]
            d.line((x0, y0, x0 + (x1 - x0) * f, y0 + (y1 - y0) * f), fill=dim(CYAN, 0.8 * k), width=3)
    for j, (x, y) in enumerate(pts):
        if seg >= j:
            d.ellipse((x - 8, y - 8, x + 8, y + 8), fill=dim(WHITE, k))

def frame(bg, i, n):
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    for x, y, ph, s in STARS:
        t = 0.55 + 0.45 * np.sin(i * 0.12 + ph)
        d.ellipse((x - s / 2, y - s / 2, x + s / 2, y + s / 2), fill=(200, 230, 255, int(170 * t)))
    sl = min(1.0, i / 14); off = int((1 - sl) * 120)
    d.rectangle((0, 74 - off, W, 78 - off), fill=BRONZE + (255,)); d.rectangle((0, H - 78 + off, W, H - 74 + off), fill=BRONZE + (255,))
    if i >= 8:
        k = min(1.0, (i - 8) / 10)
        d.text((960, 124), "LOOK TO THE STARS", font=fnt(SERIFI, 52), fill=dim(CYAN, k), anchor="mm")
    if i >= 36:
        k = min(1.0, (i - 36) / 8)
        d.text((960, 235), "THANKS FOR WATCHING", font=fnt(IMPACT, 104), anchor="mm", fill=dim(WHITE, k), stroke_width=5, stroke_fill=(10, 30, 60, int(255 * k)))
    if i >= 20:
        k = min(1.0, (i - 20) / 10)
        for box, lab in zip(TILES, ["LATEST UPLOAD", "BEST FOR YOU"]): tile(d, box, lab, k)
        cx, cy, r = RING; rr = int(r * (1 + 0.04 * np.sin(i * 0.22)))
        d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=dim(CYAN, k), width=6)
        d.text((cx, cy + r + 42), "SUBSCRIBE", font=fnt(SERIF, 36), fill=dim(CYAN, k), anchor="mm")
        lines(d, CONST, k, i, 24); lines(d, CONST2, k, i, 30)
    if i >= 70:
        k = min(1.0, (i - 70) / 12)
        d.text((960, 905), "NEXT: FROSTCAST, EVERY WEDNESDAY 9 PM ET", font=fnt(SERIF, 50), fill=dim(WHITE, k), anchor="mm")
    if i >= 110:
        k = min(1.0, (i - 110) / 12)
        d.text((960, 972), "THE WINTER WOLF'S DEN", font=fnt(SERIFI, 40), fill=dim(BRONZE, k), anchor="mm")
    im = Image.alpha_composite(bg, ov)
    k = 1.0
    if i < 6: k = i / 6
    if i > n - 8: k = max(0.0, (n - i) / 8)
    return Image.eval(im.convert("RGB"), lambda v: int(v * k))

def touch_test():
    d = ImageDraw.Draw(Image.new("RGB", (W, H)))
    items = {"LOOK TO THE STARS": ((960, 124), SERIFI, 52), "THANKS FOR WATCHING": ((960, 235), IMPACT, 104),
             "NEXT line": ((960, 905), SERIF, 50), "WWD line": ((960, 972), SERIFI, 40)}
    txt = {"LOOK TO THE STARS": "LOOK TO THE STARS", "THANKS FOR WATCHING": "THANKS FOR WATCHING",
           "NEXT line": "NEXT: FROSTCAST, EVERY WEDNESDAY 9 PM ET", "WWD line": "THE WINTER WOLF'S DEN"}
    zones = {"tileL": (190, 420 - 70, 830, 780 + 12), "tileR": (1090, 420 - 70, 1730, 780 + 12), "ring+label": (860, 500, 1060, 732)}
    bad = 0
    for k, (xy, f, s) in items.items():
        b = d.textbbox(xy, txt[k], font=fnt(f, s), anchor="mm")
        inside = b[0] >= 96 and b[2] <= 1824 and b[1] >= 54 and b[3] <= 1026
        hit = [z for z, zb in zones.items() if not (b[2] < zb[0] or b[0] > zb[2] or b[3] < zb[1] or b[1] > zb[3])]
        print(f"TEXT {k}: box {b} inside96..1824x54..1026={inside} zone_hits={hit}")
        bad += (not inside) + len(hit)
    print("TOUCH TEST", "PASS" if bad == 0 else "FAIL")
    return bad

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--outdir", default=r"P:\WWD Kit\Cards"); a = ap.parse_args()
    if touch_test(): sys.exit(1)
    bg = plate(); n = 360
    out = os.path.join(a.outdir, "End Card - Percy Jackson S3.mov")
    assert not os.path.exists(out), "exists, never overwrite"
    f = lambda i: frame(bg, i, n)
    render(f, n, out, [(SH, 0, 0.4), (SH, 1200, 0.5), (SW, 2350, 0.4)], alpha=False)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", out.replace(".mov", " (MP4).mp4")], check=True)
    f(200).save(out.replace(".mov", ".png"))
    print("done", out)
