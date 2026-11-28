"""PJ S3 review intro, FINISHED: Zac-approved Firefly (Veo 3.1) clip + code-built title + real WWD logo bug.
Inputs : firefly-intro.mp4 (8 s, 1920x1080, picture area y140..940 with black letterbox bars), wwd_logo_a.png (real logo, alpha).
Title  : "Percy Jackson and the Olympians: Season 3" (set in caps, Constantia Bold, system font). Text is code-built, never in the AI clip.
Timing : trident forms 2.5-3.5 s -> title letters reveal 3.3 s, SEASON 3 at 4.3 s, logo bug 4.7 s, light sweep 5.4 s, hold to 8 s.
Usage  : python make_pj_firefly_title.py <workdir>   (workdir holds firefly-intro.mp4 and wwd_logo_a.png; writes overlay frames + title_only.mp4)
Free, no credits, no studio font/logo/art. Never writes into P:\WWD Kit (the caller copies).
"""
import sys, os, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, N = 1920, 1080, 30, 240
WD = sys.argv[1]
OV = os.path.join(WD, "overlay"); os.makedirs(OV, exist_ok=True)
FB = r"C:\Windows\Fonts\constanb.ttf"
L1 = "PERCY JACKSON AND THE OLYMPIANS:"
L2 = "SEASON 3"
S1, S2 = 68, 74        # font sizes
TR1, TR2 = 7, 22       # tracking px
Y1, Y2 = 898, 1006     # line centres
GOLD_HI, GOLD_MID, GOLD_LO = (255, 240, 184), (232, 190, 98), (150, 98, 38)
SEA = (150, 240, 232)  # sea-glass highlight


def ease(x):
    x = min(1, max(0, x)); return 1 - (1 - x) ** 3


def layout(text, size, tr):
    f = ImageFont.truetype(FB, size)
    fd = ImageFont.truetype(r"C:\Windows\Fonts\cambriab.ttf", int(size * 1.0))  # lining figures (Constantia digits are old-style)
    xs, x = [], 0
    for ch in text:
        xs.append(x); x += (fd if ch.isdigit() else f).getlength(ch) + tr
    return f, xs, x - tr, fd


def glyph_masks(text, size, tr, cy):
    """per-letter full-width L masks (band only) and band y-range"""
    f, xs, tw, fd = layout(text, size, tr)
    x0 = (W - tw) / 2
    bt, bh = int(cy - size), size * 2
    masks = []
    for ch, x in zip(text, xs):
        m = Image.new("L", (W, bh), 0)
        if ch != " ":
            ImageDraw.Draw(m).text((x0 + x, size + int(size * 0.33)), ch, font=(fd if ch.isdigit() else f), fill=255, anchor="ls")
        masks.append(np.asarray(m, np.float32) / 255.0)
    return masks, bt, bh, x0, x0 + tw


def gold_fill(bh, size):
    y = np.linspace(0, 1, bh)
    top, mid, lo = (np.array(c_, np.float32) for c_ in (GOLD_HI, GOLD_MID, GOLD_LO))
    t1 = np.clip((y - 0.30) / 0.22, 0, 1)[:, None]
    t2 = np.clip((y - 0.52) / 0.22, 0, 1)[:, None]
    rows = np.where(y[:, None] < 0.52, top + (mid - top) * t1, mid + (lo - mid) * t2)
    return np.repeat(rows[:, None, :], W, axis=1) / 255.0


L1M, L1T, L1H, L1X0, L1X1 = glyph_masks(L1, S1, TR1, Y1)
L2M, L2T, L2H, L2X0, L2X1 = glyph_masks(L2, S2, TR2, Y2)
F1, F2 = gold_fill(L1H, S1), gold_fill(L2H, S2)

# logo bug
logo = Image.open(os.path.join(WD, "wwd_logo_a.png")).convert("RGBA")
logo = logo.crop(logo.getchannel("A").getbbox())
LH = 270; LWd = int(logo.width * LH / logo.height)
logo = logo.resize((LWd, LH), Image.LANCZOS)
LX, LY = 64, 158


def env(t, start, dur=0.5):
    return ease((t - start) / dur)


def render(i):
    t = i / FPS
    rgba = np.zeros((H, W, 4), np.float32)
    # bottom readability gradient (fades in with title)
    g_a = ease((t - 3.1) / 1.0)
    yy = np.linspace(0, 1, H)[:, None]
    grad = np.clip((yy - 0.64) / 0.30, 0, 1) ** 1.1 * 0.90 * g_a
    rgba[..., 3] = np.maximum(rgba[..., 3], np.repeat(grad, W, 1))
    # top-left vignette for logo
    if t > 4.3:
        vy, vx = np.mgrid[0:H, 0:W]
        v = np.clip(1 - np.hypot((vx - 190) / 520, (vy - 300) / 440), 0, 1) ** 1.5 * 0.55 * ease((t - 4.3) / 0.8)
        rgba[..., 3] = 1 - (1 - rgba[..., 3]) * (1 - v)
    text_alpha_full = np.zeros((H, W), np.float32)
    text_rgb = np.zeros((H, W, 3), np.float32)

    def line(masks, top, bh, fill, start, step, drift):
        a = np.zeros((bh, W), np.float32)
        for k, m in enumerate(masks):
            e = env(t, start + k * step, 0.55)
            if e <= 0: continue
            dy = int(round((1 - e) * drift))
            mm = m * e
            if dy: mm = np.roll(mm, dy, axis=0)
            a = np.maximum(a, mm)
        return a

    a1 = line(L1M, L1T, L1H, F1, 3.30, 0.045, 14)
    a2 = line(L2M, L2T, L2H, F2, 4.30, 0.07, 14)
    sweep_x = -300 + (t - 5.4) / 1.1 * (W + 700)
    for a, top, bh, fill in ((a1, L1T, L1H, F1), (a2, L2T, L2H, F2)):
        rgb = fill.copy()
        if 5.4 <= t <= 6.5:
            xs = np.arange(W)[None, :, None]
            ysb = np.arange(bh)[:, None, None]
            d = (xs - (sweep_x + ysb * 0.5)) / 110.0
            band = np.exp(-d * d)
            rgb = rgb + band * (np.array([1.0, 1.0, 0.94], np.float32) - rgb) * 0.85 + band * 0.0
        ga = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(16))
        glow = np.asarray(ga, np.float32) / 255.0
        # glow under text: warm gold plus a touch of sea-glass
        gcol = (np.array(GOLD_MID, np.float32) * 0.8 + np.array(SEA, np.float32) * 0.2) / 255.0
        # dark shadow for legibility
        sh = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(5))
        sha = np.asarray(sh, np.float32) / 255.0
        sha = np.roll(sha, 5, axis=0) * 0.85
        reg = slice(top, top + bh)
        # composite: shadow, glow, text onto rgba region (premultiplied-free simple over)
        for layer_rgb, layer_a in ((np.zeros((bh, W, 3), np.float32), np.clip(sha, 0, 1)),
                                   (np.repeat(gcol[None, None, :], bh, 0).repeat(W, 1), glow * 0.38),
                                   (rgb, a)):
            base_a = rgba[reg, :, 3:4]; base_c = text_rgb[reg]
            la = layer_a[..., None]
            out_a = la + base_a * (1 - la)
            text_rgb[reg] = (layer_rgb * la + base_c * base_a * (1 - la)) / np.maximum(out_a, 1e-6)
            rgba[reg, :, 3:4] = out_a
    # fold text_rgb into rgba rgb (gradient is black so rgb = text_rgb where alpha)
    rgba[..., :3] = text_rgb
    # logo bug
    le = env(t, 4.7, 0.7)
    if le > 0:
        sc = 0.93 + 0.07 * le
        lg = logo.resize((int(LWd * sc), int(LH * sc)), Image.LANCZOS)
        cx, cy = LX + LWd / 2, LY + LH / 2
        pos = (int(cx - lg.width / 2), int(cy - lg.height / 2))
        arr = np.asarray(lg, np.float32) / 255.0
        la_ = arr[..., 3] * le
        # cyan glow behind
        glow_im = Image.new("L", (W, H), 0)
        glow_im.paste(Image.fromarray((la_ * 255).astype(np.uint8)), pos)
        gl = np.asarray(glow_im.filter(ImageFilter.GaussianBlur(22)), np.float32) / 255.0 * 0.55
        ca = np.array([90, 225, 255], np.float32) / 255.0
        ba = rgba[..., 3:4]; la = gl[..., None]; oa = la + ba * (1 - la)
        rgba[..., :3] = (ca * la + rgba[..., :3] * ba * (1 - la)) / np.maximum(oa, 1e-6); rgba[..., 3:4] = oa
        x, y = pos
        sl = (slice(y, y + lg.height), slice(x, x + lg.width))
        ba = rgba[sl][..., 3:4]; la = la_[..., None]; oa = la + ba * (1 - la)
        rgba[sl][..., :3] = (arr[..., :3] * la + rgba[sl][..., :3] * ba * (1 - la)) / np.maximum(oa, 1e-6)
        rgba[sl][..., 3:4] = oa
    # thin gold rules beside SEASON 3
    re_ = env(t, 4.6, 0.8)
    if re_ > 0:
        rule = Image.new("L", (W, H), 0); d = ImageDraw.Draw(rule)
        cy = Y2
        half = 190 * re_
        gap = (L2X1 - L2X0) / 2 + 34
        for sgn in (-1, 1):
            xa = 960 + sgn * gap; xb = 960 + sgn * (gap + half)
            d.line([(min(xa, xb), cy), (max(xa, xb), cy)], fill=200, width=2)
            d.polygon([(960 + sgn * (gap - 14), cy), (960 + sgn * (gap - 8), cy - 5), (960 + sgn * (gap - 2), cy), (960 + sgn * (gap - 8), cy + 5)], fill=230)
        ra = np.asarray(rule, np.float32)[..., None] / 255.0
        gc = np.array(GOLD_MID, np.float32) / 255.0
        ba = rgba[..., 3:4]; oa = ra + ba * (1 - ra)
        rgba[..., :3] = (gc * ra + rgba[..., :3] * ba * (1 - ra)) / np.maximum(oa, 1e-6); rgba[..., 3:4] = oa
    out = np.clip(rgba, 0, 1)
    out8 = (out * 255 + 0.5).astype(np.uint8)
    return Image.fromarray(out8, "RGBA")


if __name__ == "__main__":
    only = [int(a) for a in sys.argv[2:]] if len(sys.argv) > 2 else range(N)
    for i in only:
        render(i).save(os.path.join(OV, "o%04d.png" % i), compress_level=1)
    print("done", len(list(only)))
