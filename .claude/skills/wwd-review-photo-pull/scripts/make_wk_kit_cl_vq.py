"""Kit for the Crystal Lake and Vision Quest mass record (2026-10-20). Original looks, owned sounds only.
No studio logos, fonts or art.

  python make_wk_kit_cl_vq.py [--only cl_spoiler,cl_weird,vq_boot,vq_tags,vq_counter,vq_spoiler]
Writes to P:\\WWD Kit\\Crystal Lake\\ and P:\\WWD Kit\\Vision Quest\\.
"Next Up - Vision Quest" for the Crystal Lake end card comes from make_next_up.py (run separately).
Remake any piece by running this script again (it overwrites).
"""
import argparse, os, random, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, FPS, blank, put, put_tl, fade, ease_out, grad_text, render, flash  # noqa: E402

IMPACT = r"C:\Windows\Fonts\impact.ttf"
MONO = r"C:\Windows\Fonts\consolab.ttf"
SFX = "P:\\Sounds\\Sound FX\\"
SIREN = SFX + "short-siren_fkRtHTE_.mp3"
STAB = SFX + "jg-032316-sfx-frightening-cymbal-stab-1.mp3"
THUD = SFX + "hit-thud-dark_GkAfpDV_.mp3"
GLITCH = SFX + "Adobe\\Imaging Elements\\Module Production Element Title Imaging Beeps Digital Glitch 01.wav"
COMP = SFX + "Adobe\\Imaging Elements\\Module Production Element Title Imaging Digital Computer Beeps Static 01.wav"
TICK = SFX + "Adobe\\Technology\\Technology Electronic Buttons Arcade Game Buttons Single 01.wav"
for p in (SIREN, STAB, THUD, GLITCH, COMP, TICK):
    assert os.path.exists(p), p

CYAN = (90, 225, 255)
RED = (235, 40, 35)


def font(path, size):
    return ImageFont.truetype(path, size)


def panel(w, h, fill=(5, 12, 20, 205), edge=CYAN, radius=10, edge_w=3):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius, fill=fill, outline=edge + (255,), width=edge_w)
    return im


def scan_overlay(im, i, strength=40):
    arr = np.asarray(im).copy()
    arr[::3, :, 3] = np.minimum(255, arr[::3, :, 3].astype(int) + strength).astype(np.uint8)
    return Image.fromarray(arr, "RGBA")


def fade_k(i, n, tail=8, head=0):
    k = 1.0
    if i > n - tail:
        k = max(0.0, (n - i) / tail)
    if head and i < head:
        k = min(k, i / head)
    return k


# ---------- Crystal Lake ----------
def cl_spoiler(out):
    n = 96
    random.seed(11)
    drips = [(random.randint(-420, 420), random.randint(60, 230), random.randint(0, 14)) for _ in range(16)]
    txt = grad_text("SPOILER ALERT", 250, "fire", 12)

    def f(i):
        cv = blank()
        k = fade_k(i, n, 10)
        a = int(min(1, i / 5) * 215 * k)
        band = Image.new("RGBA", (W, 330), (0, 0, 0, a))
        put_tl(cv, band, 0, 375)
        s = 1.0 + 0.7 * (1 - ease_out(i / 8))
        sx = random.Random(i).randint(-9, 9) if i < 7 else 0
        put(cv, txt, W / 2 + sx, 540, scale=s, alpha=k)
        d = ImageDraw.Draw(cv)
        for dx, ln, st in drips:
            t = max(0.0, min(1.0, (i - 10 - st) / 38))
            if t <= 0:
                continue
            x = int(W / 2 + dx)
            y0 = 600
            y1 = int(y0 + ln * ease_out(t))
            col = (170, 8, 8, int(255 * k))
            d.rectangle((x - 5, y0, x + 5, y1), fill=col)
            d.ellipse((x - 9, y1 - 6, x + 9, y1 + 14), fill=col)
        return cv

    render(f, n, out, [(SIREN, 0, 0.5), (STAB, 260, 0.8)])


def stamp(text, color, n=84, cx=1330, cy=260, tilt=-6, size=125):
    f_ = font(IMPACT, size)
    b = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), text, font=f_)
    w, h = b[2] - b[0] + 90, b[3] - b[1] + 70
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((6, 6, w - 7, h - 7), 14, outline=color + (255,), width=10)
    d.rounded_rectangle((20, 20, w - 21, h - 21), 8, outline=color + (255,), width=4)
    d.text((45 - b[0], 35 - b[1]), text, font=f_, fill=color + (255,))
    arr = np.asarray(im).copy()
    rng = np.random.default_rng(5)
    holes = rng.random(arr.shape[:2]) < 0.07
    arr[holes, 3] = (arr[holes, 3] * 0.35).astype(np.uint8)
    im = Image.fromarray(arr, "RGBA").rotate(tilt, expand=True, resample=Image.BICUBIC)

    def f(i):
        cv = blank()
        k = fade_k(i, n, 9)
        s = 1.0 + 1.3 * (1 - ease_out(i / 5))
        dx = random.Random(i).randint(-7, 7) if 5 <= i < 11 else 0
        put(cv, im, cx + dx, cy, scale=s, alpha=k * min(1.0, i / 3))
        return cv

    return f, n


def cl_weird(out):
    f, n = stamp("THAT WAS WEIRD", RED)
    render(f, n, out, [(THUD, 150, 0.9)])


def cl_weird_good(out):
    f, n = stamp("WEIRD GOOD", (60, 200, 90), size=150)
    render(f, n, out, [(THUD, 150, 0.9)])


# ---------- Vision Quest ----------
def vq_boot(out):
    n = 150
    l1 = "> BOOTING VISIONQUEST REVIEW"
    l2 = "> EPISODES 1 + 2 ... LOADED"
    l3 = "> REVIEW STATUS: ONLINE"
    fm = font(MONO, 46)
    big = font(IMPACT, 130)
    pw, ph = 1360, 430

    def f(i):
        cv = blank()
        k = fade_k(i, n, 10, head=4)
        p = panel(pw, ph)
        d = ImageDraw.Draw(p)
        c1 = int(max(0, i - 4) * 1.1)
        d.text((50, 40), l1[:c1], font=fm, fill=CYAN + (255,))
        c2 = int(max(0, i - 36) * 1.1)
        d.text((50, 105), l2[:c2], font=fm, fill=CYAN + (255,))
        pr = max(0.0, min(1.0, (i - 28) / 62))
        d.rectangle((50, 190, pw - 50, 222), outline=CYAN + (255,), width=3)
        d.rectangle((54, 194, 54 + int((pw - 108) * pr), 218), fill=CYAN + (230,))
        d.text((pw - 190, 232), f"{int(pr * 100):3d}%", font=fm, fill=CYAN + (255,))
        if i >= 98:
            c3 = int((i - 98) * 1.4)
            d.text((50, 290), l3[:c3], font=fm, fill=(120, 255, 150, 255))
        if i >= 112:
            flick = 1.0 if (i % 6) < 4 else 0.55
            t = big.getbbox("VISIONQUEST")
            tw = t[2] - t[0]
            d.text(((pw - tw) // 2, 330 - 28), "", font=big)
        p = scan_overlay(p, i)
        put(cv, p, W / 2, H / 2, alpha=k)
        if i >= 112:
            tt = Image.new("RGBA", (1500, 200), (0, 0, 0, 0))
            dd = ImageDraw.Draw(tt)
            flick = 1.0 if (i % 6) < 4 else 0.5
            dd.text((750, 100), "VISIONQUEST", font=big, fill=CYAN + (int(255 * flick),), anchor="mm", stroke_width=3, stroke_fill=(0, 30, 50, 255))
            put(cv, tt, W / 2, H / 2 + 330, alpha=k)
        return cv

    render(f, n, out, [(GLITCH, 0, 0.5), (COMP, 1500, 0.35)])


AI_TAGS = [
    ("EDITH", "E.D.I.T.H.", "EMILY HAMPSHIRE"),
    ("FRIDAY", "F.R.I.D.A.Y.", "ORLA BRADY"),
    ("JARVIS", "J.A.R.V.I.S.", "JAMES D'ARCY"),
    ("DUM-E", "D.U.M.-E.", "HENRY LEWIS"),
    ("U", "U.", "JONATHAN SAYER"),
]


def ai_tag(name, actor, out):
    n = 108
    pw, ph = 820, 190
    f1, f2, f3 = font(MONO, 82), font(MONO, 32), font(MONO, 24)

    def f(i):
        cv = blank()
        k = fade_k(i, n, 8)
        reveal = ease_out(i / 9)
        p = panel(pw, ph)
        d = ImageDraw.Draw(p)
        d.rectangle((0, 0, 14, ph), fill=CYAN + (255,))
        d.text((44, 20), "AI ONLINE", font=f3, fill=(120, 255, 150, 255))
        c = int(max(0, i - 6) * 0.9) + 0
        d.text((44, 52), name[:c], font=f1, fill=CYAN + (255,))
        d.text((44, 140), actor, font=f2, fill=(205, 235, 245, 255))
        sweep = int(((i * 38) % (pw + 200)) - 100)
        d.rectangle((max(0, sweep), 0, max(0, sweep + 6), ph), fill=CYAN + (70,))
        p = scan_overlay(p, i)
        w = max(1, int(pw * reveal))
        p = p.crop((0, 0, w, ph))
        put_tl(cv, fade(p, k), 90, 790)
        return cv

    render(f, n, out, [(GLITCH, 0, 0.35)])


def vq_counter(num, label, out):
    n = 108
    pw, ph = 640, 250
    f1, f2, f3 = font(MONO, 30), font(IMPACT, 150), font(IMPACT, 64)

    def f(i):
        cv = blank()
        k = fade_k(i, n, 9)
        slide = ease_out(i / 7)
        p = panel(pw, ph, edge=RED)
        d = ImageDraw.Draw(p)
        d.text((pw // 2, 38), "WRONG SPADER NAMES", font=f1, fill=RED + (255,), anchor="mm")
        d.line((30, 70, pw - 30, 70), fill=RED + (255,), width=2)
        d.text((130, 150), "", font=f2)
        p = scan_overlay(p, i, 30)
        put_tl(cv, fade(p, k), int(W + 20 - (pw + 70) * slide), 70)
        # big number pops
        s = 1.0 + 0.9 * (1 - ease_out((i - 8) / 6)) if i >= 8 else 0.0
        if s > 0:
            nt = Image.new("RGBA", (300, 190), (0, 0, 0, 0))
            ImageDraw.Draw(nt).text((150, 95), str(num), font=f2, fill=(255, 255, 255, 255), anchor="mm", stroke_width=5, stroke_fill=(120, 10, 10, 255))
            put(cv, nt, W - 70 - pw + 170, 190, scale=s, alpha=k)
            lt = Image.new("RGBA", (330, 100), (0, 0, 0, 0))
            ImageDraw.Draw(lt).text((165, 50), label, font=f3, fill=(255, 220, 90, 255), anchor="mm", stroke_width=3, stroke_fill=(60, 30, 0, 255))
            put(cv, lt, W - 70 - 190, 205, scale=min(1.0, s), alpha=k)
        return cv

    render(f, n, out, [(TICK, 8 * 1000 // FPS, 0.9)])


def vq_spoiler(out):
    n = 96
    f1, f2 = font(IMPACT, 180), font(MONO, 40)

    def f(i):
        cv = blank()
        k = fade_k(i, n, 10)
        pulse = 0.55 + 0.45 * abs(np.sin(i / 3.0))
        a = int(min(1, i / 5) * 205 * k)
        put_tl(cv, Image.new("RGBA", (W, 340), (20, 0, 0, a)), 0, 370)
        t = Image.new("RGBA", (1700, 260), (0, 0, 0, 0))
        d = ImageDraw.Draw(t)
        d.text((850, 110), "SPOILER WARNING", font=f1, fill=RED + (int(255 * pulse),), anchor="mm", stroke_width=6, stroke_fill=(60, 0, 0, 255))
        d.text((850, 225), "> CONTENT BEYOND THIS POINT: RESTRICTED", font=f2, fill=CYAN + (255,), anchor="mm")
        s = 1.0 + 0.4 * (1 - ease_out(i / 7))
        put(cv, scan_overlay(t, i, 30), W / 2, 540, scale=s, alpha=k)
        return cv

    render(f, n, out, [(SIREN, 0, 0.5), (GLITCH, 0, 0.3)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="cl_spoiler,cl_weird,vq_boot,vq_tags,vq_counter,vq_spoiler")
    a = ap.parse_args()
    want = a.only.split(",")
    cl = r"P:\WWD Kit\Crystal Lake"
    vq = r"P:\WWD Kit\Vision Quest"
    if "cl_spoiler" in want:
        cl_spoiler(os.path.join(cl, "Spoiler Alert.mov"))
    if "cl_weird" in want:
        cl_weird(os.path.join(cl, "That Was Weird.mov"))
        cl_weird_good(os.path.join(cl, "Weird Good.mov"))
    if "vq_boot" in want:
        vq_boot(os.path.join(vq, "System Boot.mov"))
    if "vq_tags" in want:
        for key, name, actor in AI_TAGS:
            ai_tag(name, actor, os.path.join(vq, f"AI Tag - {key}.mov"))
    if "vq_counter" in want:
        for num, label in ((1, "KEVIN"), (2, "DAVID"), (3, "DAVE")):
            vq_counter(num, label, os.path.join(vq, f"Wrong Name Counter {num} - {label.title()}.mov"))
    if "vq_spoiler" in want:
        vq_spoiler(os.path.join(vq, "Spoiler Alert.mov"))


if __name__ == "__main__":
    main()
