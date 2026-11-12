"""Veterans Day 2026 card, code-made (Pillow + numpy). No AI image, no photos, no flag, no insignia.
Variants A (centered glow) and B (sunrise rays, left aligned). Sizes 1080x1350, 1080x1080, 1920x1080.
Fonts: Poppins bundled in wwd-review-pipeline/assets/fonts.
Run: python make_veterans_day_card.py
"""
import math, os, shutil
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FD = r"D:\WKP\.claude\skills\wwd-review-pipeline\assets\fonts"
BOLD = os.path.join(FD, "Poppins-Bold.ttf"); SEMI = os.path.join(FD, "Poppins-SemiBold.ttf")
OUT = r"P:\WWD Kit\Veterans Day"
COPY = r"D:\WKP Reports\WWD Social Captions\Veterans Day 2026 Graphics"
SIZES = {"4x5": (1080, 1350), "1x1": (1080, 1080), "16x9": (1920, 1080)}
GOLD = (244, 190, 90); CREAM = (255, 243, 222); NAVY_T = (8, 18, 44); NAVY_B = (22, 40, 82)
CYAN = (150, 215, 235)
SS = 1

def bg(w, h, variant):
    y = np.linspace(0, 1, h)[:, None, None]; x = np.linspace(0, 1, w)[None, :, None]
    base = np.array(NAVY_T)[None, None, :] * (1 - y) + np.array(NAVY_B)[None, None, :] * y
    base = np.broadcast_to(base, (h, w, 3)).astype(np.float32).copy()
    cx, cy = (0.5, 1.05) if variant == "A" else (0.5, 0.98)
    r = np.sqrt(((x - cx) * w) ** 2 + ((y - cy) * h) ** 2) / max(w, h)
    glow = np.clip(1 - r / (0.85 if variant == "A" else 0.7), 0, 1) ** 2.2
    amber = np.array([255, 150, 40], np.float32)
    base += glow * amber * 0.75
    if variant == "B":
        ang = np.arctan2((y - cy) * h, (x - cx) * w)
        rays = (np.sin(ang * 14) > 0.55).astype(np.float32) * np.clip(1 - r / 1.0, 0, 1) * 0.14
        base += rays * amber
    rng = np.random.default_rng(11)
    base += rng.normal(0, 2.2, (h, w, 1))  # subtle grain
    # vignette
    vr = np.sqrt(((x - .5) * 1.1) ** 2 + ((y - .5) * 1.1) ** 2)
    base *= (1 - 0.35 * np.clip(vr - 0.35, 0, 1))[..., :]
    return Image.fromarray(np.clip(base, 0, 255).astype(np.uint8)).convert("RGB")

def fit(draw, text, font_path, max_w, start):
    s = start
    while s > 10:
        f = ImageFont.truetype(font_path, s)
        if draw.textlength(text, font=f) <= max_w: return f
        s -= 2
    return ImageFont.truetype(font_path, 10)

def stars(draw, w, h, cx, cy, n=22):
    rng = np.random.default_rng(5)
    for _ in range(n):
        px = rng.uniform(0.05, 0.95) * w; py = rng.uniform(0.04, 0.42) * h
        if abs(px - cx) < w * 0.0 and False: continue
        r = rng.uniform(1.5, 3.2)
        draw.ellipse([px - r, py - r, px + r, py + r], fill=(255, 235, 190, int(rng.uniform(90, 200))))

def wolf_mark(size):
    """Simple geometric wolf head, gold, front view. Not militarized."""
    s = size; im = Image.new("RGBA", (s, s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    P = lambda pts: [(a * s, b * s) for a, b in pts]
    head = [(.50, .90), (.30, .70), (.18, .50), (.12, .08), (.34, .26), (.66, .26), (.88, .08), (.82, .50), (.70, .70)]
    d.polygon(P(head), fill=GOLD + (255,))
    d.polygon(P([(.20, .22), (.27, .33), (.20, .40)]), fill=(150, 90, 20, 255))
    d.polygon(P([(.80, .22), (.73, .33), (.80, .40)]), fill=(150, 90, 20, 255))
    # eyes and nose in navy
    d.polygon(P([(.30, .50), (.43, .54), (.34, .58)]), fill=NAVY_T + (255,))
    d.polygon(P([(.70, .50), (.57, .54), (.66, .58)]), fill=NAVY_T + (255,))
    d.polygon(P([(.44, .72), (.56, .72), (.50, .80)]), fill=NAVY_T + (255,))
    return im

def build(variant, size):
    w, h = SIZES[size]; wide = w > h
    img = bg(w, h, variant).convert("RGBA")
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    m = int(min(w, h) * 0.09)           # safe margin (also covers grid-crop of 4:5 to 1:1 centre)
    # frame
    fm = int(min(w, h) * 0.035)
    d.rectangle([fm, fm, w - fm, h - fm], outline=GOLD + (200,), width=3)
    d.rectangle([fm + 12, fm + 12, w - fm - 12, h - fm - 12], outline=GOLD + (90,), width=1)
    stars(d, w, h, w / 2, h / 2)
    left = variant == "B" and not wide or (variant == "B" and wide)
    tw = int(w * (0.56 if wide else 0.80)) if wide else int(w * 0.80)
    # layout
    wm = wolf_mark(int(min(w, h) * (0.17 if not wide else 0.22)))
    if wide:
        cx_text = w * 0.66; area = w * 0.50
    else:
        cx_text = w / 2; area = w - 2 * m - 40
    dd = ImageDraw.Draw(ov)
    f1a = fit(dd, "Happy", BOLD, area, int(h * 0.20 if not wide else h * 0.2))
    big = int(min(f1a.size, h * (0.15 if not wide else 0.22)))
    f_h = fit(dd, "Veterans Day", BOLD, area, int(h * (0.11 if not wide else 0.2)))
    f_h1 = ImageFont.truetype(BOLD, int(f_h.size * 0.62))
    f_s = fit(dd, "Thank you to everyone", SEMI, area, int(f_h.size * 0.42))
    f_f = ImageFont.truetype(SEMI, int(min(w, h) * 0.030 + 8))
    lines = [("Happy", f_h1, GOLD), ("Veterans Day", f_h, CREAM)]
    sub = ["Thank you to everyone", "who has served."]
    # measure
    def lh(f): return f.getbbox("Hg")[3] - f.getbbox("Hg")[1]
    gap = int(f_h.size * 0.12)
    block_h = lh(f_h1) + gap + lh(f_h) + int(f_h.size * 0.55) + 4 + int(f_h.size * .45) + lh(f_s) * 2 + int(f_s.size * 0.4)
    if wide:
        wm_h = wm.size[1]
        top = (h - block_h) / 2
        ox = w * 0.175 - wm.size[0] / 2
        img_wm_pos = (int(ox), int((h - wm_h) / 2) - 20)
        # divider
        d.line([(w * 0.355, h * 0.22), (w * 0.355, h * 0.78)], fill=GOLD + (140,), width=2)
    else:
        top = h * 0.30 if h > w else h * 0.27
        img_wm_pos = (int(w / 2 - wm.size[0] / 2), int(h * 0.075 if h > w else h * 0.06))
    ov.alpha_composite(wm, img_wm_pos) if False else None
    y = top
    def ctext(txt, f, fill, yy, shadow=True):
        tw_ = dd.textlength(txt, font=f)
        x = cx_text - tw_ / 2 if variant == "A" or not left else cx_text - tw_ / 2
        if shadow:
            dd.text((x + 3, yy + 5), txt, font=f, fill=(0, 0, 0, 120))
        dd.text((x, yy), txt, font=f, fill=fill + (255,))
        return yy
    ctext("Happy", f_h1, GOLD, y); y += lh(f_h1) + gap + int(f_h1.size * 0.35)
    ctext("Veterans Day", f_h, CREAM, y); y += lh(f_h) + int(f_h.size * 0.55)
    # rule
    rw = int(area * 0.28)
    dd.rectangle([cx_text - rw / 2, y, cx_text + rw / 2, y + 4], fill=GOLD + (230,)); y += int(f_h.size * .45)
    for s_ in sub:
        ctext(s_, f_s, CREAM, y, shadow=False); y += lh(f_s) + int(f_s.size * 0.45)
    # footer
    ft = "The Winter Wolf's Den"
    ftw = dd.textlength(ft, font=f_f)
    fy = h - fm - int(f_f.size * 2.6)
    fx = (w - ftw) / 2 if not wide else cx_text - ftw / 2
    dd.text((fx + 2, fy + 3), ft, font=f_f, fill=(0, 0, 0, 200)); dd.text((fx, fy), ft, font=f_f, fill=CYAN + (255,))
    img.alpha_composite(ov)
    # wolf mark with soft glow
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0)); glow.alpha_composite(wm, img_wm_pos)
    gl = glow.filter(ImageFilter.GaussianBlur(26)); gl.putalpha(gl.getchannel("A").point(lambda a: int(a * .7)))
    img.alpha_composite(gl); img.alpha_composite(glow)
    return img.convert("RGB")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True); os.makedirs(COPY, exist_ok=True)
    for v in "AB":
        for s in SIZES:
            name = f"Veterans Day 2026 - Variant {v} - {s}.png"
            p = os.path.join(OUT, name); build(v, s).save(p)
            shutil.copy(p, os.path.join(COPY, name)); print(p)
