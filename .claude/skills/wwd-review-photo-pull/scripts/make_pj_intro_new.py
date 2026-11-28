"""PJ intro v2, "Trident Tide" (wwd-vfx 2026-11-23). 6.0 s, 1920x1080, 30 fps, code-built (numpy + Pillow), no AI video.
Original look: deep icy water, WWD wolf shield rises, a bronze trident thrusts up behind it (crest), impact, crest travels to the
title lockup, title surfaces, hosts slots slide in on the left. Own caustics, own trident vector, own Greek key.
No studio logo/font/art. Fonts: Windows Constantia (system). Logo: the show's own WWD logo (L:\\...\\Pictures\\logo.png, copied to scratch).
Writes frames to scratch, then ffmpeg encodes. Never writes into P:\\WWD Kit (the caller copies, asserts no overwrite).
Usage: python make_pj_intro_new.py [outdir]
"""
import sys, os, math, subprocess
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H, FPS, N = 1920, 1080, 30, 180
OUT = sys.argv[1] if len(sys.argv) > 1 else r"D:\WKP\scratch\pj-intro-new"
FR = os.path.join(OUT, "frames"); os.makedirs(FR, exist_ok=True)
LOGO = os.path.join(OUT, "wwd_logo_a.png")
SERIF_B = r"C:\Windows\Fonts\constanb.ttf"; SERIF_I = r"C:\Windows\Fonts\constani.ttf"
CYAN = np.array([90, 225, 255]) / 255.0
GOLD_HI, GOLD_LO = (255, 232, 160), (176, 116, 48)
rng = np.random.RandomState(7)

def ease_out(x, p=3): x = min(max(x, 0.0), 1.0); return 1 - (1 - x) ** p
def ease_io(x): x = min(max(x, 0.0), 1.0); return 3 * x * x - 2 * x ** 3
def ease_back(x, s=1.9): x = min(max(x, 0.0), 1.0); x -= 1; return 1 + (s + 1) * x ** 3 + s * x ** 2
def clamp01(x): return min(max(x, 0.0), 1.0)

# ---------------------------------------------------------------- background
BW, BH = 960, 540
YY, XX = np.mgrid[0:BH, 0:BW].astype(np.float32); XX /= BW; YY /= BH
def background(t):
    top = np.array([0.30, 0.66, 0.80]); mid = np.array([0.015, 0.17, 0.36]); bot = np.array([0.003, 0.02, 0.08])
    g = np.clip(YY / 0.55, 0, 1)[..., None]
    col = np.where(YY[..., None] < 0.55, top * (1 - g) ** 1.6 + mid * (1 - (1 - g) ** 1.6), mid)
    g2 = np.clip((YY - 0.55) / 0.45, 0, 1)[..., None]
    col = np.where(YY[..., None] >= 0.55, mid * (1 - g2) + bot * g2, col)
    # caustics, warped ridges
    u, v = XX * 62.0, YY * 34.0
    for i in range(3):
        u, v = u + 0.30 * np.sin(v * 0.9 + t * 1.1 + i * 2.1), v + 0.30 * np.cos(u * 0.8 - t * 0.8 + i * 1.3)
    f = np.sin(u) + np.sin(v * 1.1) + np.sin((u + v) * 0.7)
    caus = np.exp(-np.abs(f) * 9.0)
    depth = np.clip(1.0 - YY / 0.62, 0, 1) ** 1.6
    col = col + (caus * depth * 0.55)[..., None] * np.array([0.55, 0.95, 1.0])
    # light shafts
    sh = np.zeros_like(XX)
    for k in range(7):
        x0 = 0.18 + 0.64 * (k / 6.0) + 0.02 * math.sin(t * 0.7 + k)
        slope = (x0 - 0.5) * 0.55
        d = (XX - x0 - slope * YY) / (0.035 + 0.02 * ((k * 37) % 5) / 5)
        sh += np.exp(-d * d) * (0.55 + 0.45 * math.sin(t * 0.9 + k * 1.7)) * 0.17
    sh *= np.clip(1.15 - YY * 1.25, 0, 1)
    col = col + sh[..., None] * np.array([0.6, 0.95, 1.0])
    # surface band
    sf = np.clip(1 - YY / 0.10, 0, 1) ** 1.5 * (0.6 + 0.4 * np.sin(XX * 60 + t * 2.0 + np.sin(XX * 17 + t)))
    col = col + sf[..., None] * np.array([0.25, 0.4, 0.45])
    return (1 - np.exp(-np.clip(col, 0, 3) * 1.25)).astype(np.float32) / (1 - math.exp(-1.25))

def bg_frame(t, zoom):
    a = np.clip(background(t), 0, 1)
    im = Image.fromarray((a * 255).astype(np.uint8))
    cw, ch = BW / zoom, BH / zoom
    x0, y0 = (BW - cw) / 2, (BH - ch) * 0.35
    return np.asarray(im.resize((W, H), Image.BICUBIC, box=(x0, y0, x0 + cw, y0 + ch))).astype(np.float32) / 255.0

# ---------------------------------------------------------------- sprites
def load_logo():
    im = Image.open(LOGO).convert("RGBA"); bb = im.getchannel("A").getbbox(); return im.crop(bb)
LOGO_IM = load_logo()
LW0, LH0 = LOGO_IM.size

def make_trident():
    S = 2; cw, ch = 720, 770
    m = Image.new("L", (cw, ch), 0); d = ImageDraw.Draw(m)
    d.polygon([(360, 10), (404, 130), (384, 148), (384, 440), (336, 440), (336, 148), (316, 130)], fill=255)
    def bez(p0, p1, p2, p3, n=40):
        out = []
        for i in range(n + 1):
            s = i / n; a = (1 - s) ** 3; b = 3 * s * (1 - s) ** 2; c = 3 * s * s * (1 - s); e = s ** 3
            out.append((a * p0[0] + b * p1[0] + c * p2[0] + e * p3[0], a * p0[1] + b * p1[1] + c * p2[1] + e * p3[1]))
        return out
    for side in (1, -1):
        mx = (lambda x: x) if side == 1 else (lambda x: cw - x)
        pts = bez((340, 450), (120, 470), (105, 320), (125, 170))
        for i, (x, y) in enumerate(pts):
            r = 17 - 8 * i / len(pts)
            d.ellipse((mx(x) - r, y - r, mx(x) + r, y + r), fill=255)
        d.polygon([(mx(125), 70), (mx(158), 180), (mx(92), 180)], fill=255)
    d.rounded_rectangle((292, 425, 428, 485), 16, fill=255)
    d.rounded_rectangle((306, 485, 414, 510), 10, fill=255)
    d.polygon([(342, 510), (378, 510), (372, 770), (348, 770)], fill=255)
    arr = np.asarray(m).astype(np.float32) / 255.0
    ys = np.linspace(0, 1, ch)[:, None, None]
    hi, lo = np.array(GOLD_HI) / 255.0, np.array(GOLD_LO) / 255.0
    col = hi * (1 - ys) + lo * ys; col = np.broadcast_to(col, (ch, cw, 3)).copy()
    mi = m.filter(ImageFilter.GaussianBlur(2))
    sh = np.asarray(ImageChops.offset(mi, 5, 5)).astype(np.float32) / 255.0
    li = np.asarray(ImageChops.offset(mi, -5, -5)).astype(np.float32) / 255.0
    mb = np.asarray(mi).astype(np.float32) / 255.0
    col += np.clip(mb - sh, 0, 1)[..., None] * 0.55   # highlight on upper left edge
    col -= np.clip(mb - li, 0, 1)[..., None] * 0.45   # shade on lower right edge
    er = np.asarray(m.filter(ImageFilter.MinFilter(7))).astype(np.float32) / 255.0
    rim = np.clip(arr - er, 0, 1)
    col = col * (1 - rim[..., None] * 0.8) + rim[..., None] * 0.8 * CYAN
    rgba = np.dstack([np.clip(col, 0, 1), arr])
    return Image.fromarray((rgba * 255).astype(np.uint8), "RGBA")
TRI = make_trident()

def make_meander(width, tile=30, stroke=4):
    n = int(width // tile); w = n * tile
    im = Image.new("L", (w, tile), 0); d = ImageDraw.Draw(im)
    for i in range(n):
        x = i * tile; p = [(x, tile - 3), (x, 3), (x + tile - 6, 3), (x + tile - 6, tile - 12), (x + 9, tile - 12), (x + 9, 13), (x + 20, 13)]
        d.line(p, fill=255, width=stroke, joint="curve")
    return im
MEAN = make_meander(760)

def tracked(text, font, track):
    ws = [font.getlength(c) for c in text]; return ws, sum(ws) + track * (len(text) - 1)

def title_layers(cx, y1, y2, y3, ymean):
    """returns dict of RGBA float layers (full canvas) sharp and blurred for line1, line2, tag, plus meander"""
    def line(text, fontpath, size, track, y, fill_top, fill_bot, outline, glow):
        f = ImageFont.truetype(fontpath, size); ws, tw = tracked(text, f, track)
        mask = Image.new("L", (W, H), 0); d = ImageDraw.Draw(mask); x = cx - tw / 2; xs = []
        for c, w in zip(text, ws):
            d.text((x, y), c, font=f, fill=255, anchor="lm"); xs.append(x); x += w + track
        return mask, (cx - tw / 2, cx + tw / 2)
    def colorize(mask, top, bot, y, size, outline_px, glow_col, glow_amt):
        m = np.asarray(mask).astype(np.float32) / 255.0
        ol = np.asarray(mask.filter(ImageFilter.MaxFilter(outline_px * 2 + 1))).astype(np.float32) / 255.0
        yy = np.linspace(0, 1, H)[:, None]; t = np.clip((yy - (y - size * 0.45)) / (size * 0.9), 0, 1)
        fill = np.array(top) / 255.0 * (1 - t[..., None]) + np.array(bot) / 255.0 * t[..., None]
        fill = np.broadcast_to(fill, (H, W, 3)).copy()
        mi = mask.filter(ImageFilter.GaussianBlur(1.5))
        hi = np.clip(np.asarray(mi).astype(np.float32) / 255.0 - np.asarray(ImageChops.offset(mi, 3, 3)).astype(np.float32) / 255.0, 0, 1)
        fill += hi[..., None] * 0.7
        navy = np.array([0.02, 0.09, 0.2])
        rgb = navy * (ol - m)[..., None] + fill * m[..., None]
        a = ol
        gl = np.asarray(mask.filter(ImageFilter.GaussianBlur(22))).astype(np.float32) / 255.0 * glow_amt
        return np.dstack([np.clip(rgb, 0, 2), a]), gl
    out = {}
    m1, ext1 = line("PERCY JACKSON", SERIF_B, 124, 6, y1, 0, 0, 0, 0)
    m2, ext2 = line("& THE OLYMPIANS", SERIF_B, 76, 14, y2, 0, 0, 0, 0)
    m3, ext3 = line("A WINTER WOLF'S DEN REVIEW", SERIF_I, 42, 7, y3, 0, 0, 0, 0)
    c1, g1 = colorize(m1, GOLD_HI, GOLD_LO, y1, 124, 5, CYAN, 0.9)
    c2, g2 = colorize(m2, (235, 252, 255), (120, 205, 235), y2, 76, 4, CYAN, 0.8)
    c3, g3 = colorize(m3, (190, 240, 255), (110, 200, 235), y3, 42, 2, CYAN, 0.4)
    for k, (c, g, e, blur) in {"l1": (c1, g1, ext1, 7), "l2": (c2, g2, ext2, 5), "l3": (c3, g3, ext3, 3)}.items():
        ci = Image.fromarray((np.clip(c, 0, 1) * 255).astype(np.uint8), "RGBA")
        b = np.asarray(ci.filter(ImageFilter.GaussianBlur(blur))).astype(np.float32) / 255.0
        out[k] = dict(sharp=np.clip(c, 0, 1).astype(np.float32), blur=b, glow=g.astype(np.float32), ext=e)
    mm = Image.new("L", (W, H), 0); mm.paste(MEAN, (int(cx - MEAN.width / 2), ymean))
    out["mean"] = dict(mask=np.asarray(mm).astype(np.float32) / 255.0, x0=cx - MEAN.width / 2, x1=cx + MEAN.width / 2)
    return out

# ---------------------------------------------------------------- compositing helpers
def put(base, spr, cx, cy, scale=1.0, alpha=1.0, add=0.0, tint=None, disp=0.0, t=0.0):
    """spr PIL RGBA, straight alpha. base float HxWx3. centered at cx,cy."""
    if alpha <= 0.001: return
    w, h = max(2, int(spr.width * scale)), max(2, int(spr.height * scale))
    s = spr.resize((w, h), Image.LANCZOS)
    a = np.asarray(s).astype(np.float32) / 255.0
    if disp > 0.01:
        from scipy.ndimage import map_coordinates
        yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
        dx = disp * np.sin(yy * 0.045 + t * 14.0) + disp * 0.5 * np.sin(yy * 0.11 - t * 9.0)
        dy = disp * 0.4 * np.sin(xx * 0.05 + t * 11.0)
        a = np.dstack([map_coordinates(a[..., c], [yy + dy, xx + dx], order=1, mode="constant") for c in range(4)])
    rgb, al = a[..., :3], a[..., 3] * alpha
    if tint is not None: rgb = rgb * tint[0] + tint[1]
    x0, y0 = int(cx - w / 2), int(cy - h / 2)
    sx0, sy0 = max(0, -x0), max(0, -y0); ex, ey = min(w, W - x0), min(h, H - y0)
    if ex <= sx0 or ey <= sy0: return
    reg = base[y0 + sy0:y0 + ey, x0 + sx0:x0 + ex]
    r = rgb[sy0:ey, sx0:ex]; aa = al[sy0:ey, sx0:ex][..., None]
    reg[:] = reg * (1 - aa) + r * aa
    if add > 0:
        reg[:] += aa * CYAN * add * 0.0 + aa * 0

def glow_of(spr, scale, cx, cy, radius, amt, base):
    w, h = int(spr.width * scale), int(spr.height * scale)
    a = spr.resize((w, h), Image.BILINEAR).getchannel("A")
    pad = radius * 3
    big = Image.new("L", (w + pad * 2, h + pad * 2), 0); big.paste(a, (pad, pad))
    g = np.asarray(big.filter(ImageFilter.GaussianBlur(radius))).astype(np.float32) / 255.0 * amt
    x0, y0 = int(cx - w / 2 - pad), int(cy - h / 2 - pad)
    sx0, sy0 = max(0, -x0), max(0, -y0); ex, ey = min(g.shape[1], W - x0), min(g.shape[0], H - y0)
    if ex <= sx0 or ey <= sy0: return
    base[y0 + sy0:y0 + ey, x0 + sx0:x0 + ex] += g[sy0:ey, sx0:ex][..., None] * CYAN

def radial(base, cx, cy, r, amt, col=(1, 1, 1)):
    x0, x1, y0, y1 = int(max(0, cx - r)), int(min(W, cx + r)), int(max(0, cy - r)), int(min(H, cy + r))
    if x1 <= x0 or y1 <= y0: return
    yy, xx = np.mgrid[y0:y1, x0:x1].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    base[y0:y1, x0:x1] += (np.clip(1 - d, 0, 1) ** 2 * amt)[..., None] * np.array(col)

def ring(base, cx, cy, r, width, amt):
    pad = int(r + width * 3); x0, x1, y0, y1 = int(max(0, cx - pad)), int(min(W, cx + pad)), int(max(0, cy - pad)), int(min(H, cy + pad))
    if x1 <= x0 or y1 <= y0: return
    yy, xx = np.mgrid[y0:y1, x0:x1].astype(np.float32)
    d = np.sqrt((xx - cx) ** 2 + ((yy - cy) * 1.0) ** 2)
    base[y0:y1, x0:x1] += (np.exp(-((d - r) / width) ** 2) * amt)[..., None] * np.array([0.8, 1.0, 1.0])

# bubbles
class Bub:
    def __init__(s, t0, x, y, r, vy, ph, life=99): s.t0, s.x, s.y, s.r, s.vy, s.ph, s.life = t0, x, y, r, vy, ph, life
BUBS = [Bub(rng.uniform(-3, 3.5), rng.uniform(80, 1840), 1160, rng.choice([4, 6, 9, 14, 22], p=[.3, .3, .2, .15, .05]), 0, rng.uniform(0, 6.28)) for _ in range(46)]
for b in BUBS: b.vy = 60 + b.r * 9 + rng.uniform(0, 40)
BURST = []
for i in range(46):
    ang = rng.uniform(-math.pi * 0.95, -math.pi * 0.05); sp = rng.uniform(260, 900)
    BURST.append((ang, sp, rng.choice([4, 6, 9, 13, 18]), rng.uniform(0, 6.28)))

def draw_bubbles(base, t, burst_t, cx_burst, cy_burst):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    def one(x, y, r, a):
        if y < -40 or y > H + 40: return
        d.ellipse((x - r, y - r, x + r, y + r), outline=(210, 245, 255, int(150 * a)), width=max(1, r // 6))
        d.ellipse((x - r * 0.55, y - r * 0.6, x - r * 0.15, y - r * 0.25), fill=(255, 255, 255, int(190 * a)))
    for b in BUBS:
        tt = t - b.t0
        if tt < 0: continue
        y = b.y - b.vy * tt; x = b.x + 18 * math.sin(tt * 1.7 + b.ph) * (1 + b.r / 14)
        one(x, y, int(b.r), clamp01(1.4 - y / H * 0.0) * (0.25 + 0.75 * clamp01(tt / 0.8)))
    if burst_t is not None and t >= burst_t:
        tt = t - burst_t
        for ang, sp, r, ph in BURST:
            drag = 1 - math.exp(-tt * 2.2)
            x = cx_burst + math.cos(ang) * sp * drag / 2.2; y = cy_burst + math.sin(ang) * sp * drag / 2.2 - 70 * tt * tt
            one(x, y, int(r), clamp01(1 - tt / 2.4))
    a = np.asarray(lay).astype(np.float32) / 255.0
    al = a[..., 3:4]; base[:] = base * (1 - al) + a[..., :3] * al

# ---------------------------------------------------------------- scene
CXL = 1227                    # center of the right panel (hosts column is 0..535)
SH_SC0, SH_SCL = 0.62, 0.25   # stage scale, lockup scale
TOP = 70                       # lockup block offset
LOCK_CY = 345                  # shield center y in lockup
TL = title_layers(CXL, 560, 722, 815, 645)
IMPACT = 1.95

def crest(base, t, shake):
    """returns shield center and scale; draws trident + shield (+ glow)."""
    # stage position
    if t < 2.05:
        rise = ease_out((t - 0.30) / 1.2)
        cx, cy = 960, 740 - 180 * rise + 450 * (1 - rise)
        sc = 0.56 + 0.06 * rise
        if t >= IMPACT: sc += 0.03 * math.exp(-(t - IMPACT) * 9)
    else:
        k = ease_io((t - 2.05) / 0.65)
        cx = 960 + (CXL - 960) * k; cy = 560 + (LOCK_CY - 560) * k; sc = SH_SC0 + (SH_SCL - SH_SC0) * k
    cx += shake[0]; cy += shake[1]
    a_in = clamp01((t - 0.30) / 0.5)
    disp = 9.0 * (1 - clamp01((t - 0.3) / 1.4)) ** 2
    sh_h = LH0 * sc; sh_w = LW0 * sc
    head_sc = sc * (0.60 + 0.50 * ease_io((t - 2.05) / 0.65))
    # trident thrust
    th = ease_back((t - 1.45) / 0.5) if t >= 1.45 else 0.0
    hh = TRI.height * head_sc
    ty = cy - sh_h / 2 + 0.08 * sh_h - 125 * head_sc + (1 - th) * (hh * 0.75)
    # trident sits behind shield: draw before shield
    if t >= 1.45:
        glow_of(TRI, head_sc, cx, ty + 0, 14, 0.9 * clamp01(th), base)
        put(base, TRI, cx, ty, head_sc, alpha=clamp01((t - 1.45) / 0.15))
    uw = (np.array([0.55 + 0.45 * (1 - clamp01((t - 0.3) / 1.4))] * 3), 0.0)
    pulse = 0.55 + 0.25 * math.sin(t * 5.0)
    glow_of(LOGO_IM, sc, cx, cy, 20, 0.45 * pulse * a_in, base)
    put(base, LOGO_IM, cx, cy, sc, alpha=a_in, tint=((1.0, 1.0, 1.0), 0.0) if t > 1.7 else ((0.82, 0.95, 1.0), 0.03), disp=disp, t=t)
    return cx, cy, sc

def title_pass(base, t):
    # line reveals (left to right sweep, blur to sharp, rise)
    def reveal(L, t0, dur, rise_px):
        x0, x1 = L["ext"]
        prog = np.clip((t - t0 - (np.arange(W) - x0) / (x1 - x0) * dur * 0.6) / (dur * 0.4), 0, 1)
        p = ease_out_arr(prog)[None, :, None]
        spr = L["blur"] * (1 - p) + L["sharp"] * p
        alpha = spr[..., 3:4] * np.clip(prog[None, :, None] * 1.4, 0, 1)
        dy = int(rise_px * (1 - float(prog.mean())))
        if dy: spr = np.roll(spr, dy, axis=0); alpha = np.roll(alpha, dy, axis=0)
        g = np.roll(L["glow"], dy, axis=0)[..., None] * prog[None, :, None] * 0.55
        base[:] += g * CYAN
        base[:] = base * (1 - alpha) + spr[..., :3] * alpha
    if t >= 2.55: reveal(TL["l1"], 2.55, 1.0, 26)
    if t >= 3.15: reveal(TL["l2"], 3.15, 0.8, 20)
    # meander draws out from center
    if t >= 3.0:
        M = TL["mean"]; k = ease_out((t - 3.0) / 0.8)
        half = (M["x1"] - M["x0"]) / 2 * k; cxm = (M["x0"] + M["x1"]) / 2
        mask = M["mask"].copy(); xs = np.arange(W)
        mask *= (np.abs(xs - cxm) <= half)[None, :]
        mask *= 0.9
        gold = np.array([0.82, 0.60, 0.27]); base[:] = base * (1 - mask[..., None]) + gold * mask[..., None]
    if t >= 3.9: reveal(TL["l3"], 3.9, 0.7, 12)

def ease_out_arr(x): return 1 - (1 - x) ** 3

def slots(base, t):
    for i, (y0, t0) in enumerate(((0, 4.15), (540, 4.30))):
        k = ease_out((t - t0) / 0.55)
        if k <= 0: continue
        x1 = int(535 * k); x0 = 0
        if x1 < 2: continue
        reg = base[y0:y0 + 540, 0:x1]
        reg[:] = reg * 0.15 + np.array([0.02, 0.06, 0.14]) * 0.85
        c = np.array([0.35, 0.88, 1.0]); bw = 4
        reg[:bw, :] = c; reg[-bw:, :] = c; reg[:, max(0, x1 - bw):] = c
        if x1 > 60:
            br = np.array([0.84, 0.63, 0.31]); reg[bw:bw + 3, 0:60] = br; reg[-bw - 3:-bw, 0:60] = br

def render(i):
    t = i / FPS
    zoom = 1.0 + 0.07 * (t / 6.0) + (0.045 * math.exp(-(t - IMPACT) * 7) if t >= IMPACT else 0)
    base = bg_frame(t, zoom)
    fade = clamp01(t / 0.55); base *= (0.12 + 0.88 * fade)
    # shake
    shake = (0.0, 0.0)
    if IMPACT <= t < IMPACT + 0.4:
        a = math.exp(-(t - IMPACT) * 11); shake = (14 * a * math.sin(t * 90), 10 * a * math.cos(t * 77))
    draw_bubbles(base, t, IMPACT if t >= IMPACT else None, 960, 560)
    cx, cy, sc = crest(base, t, shake)
    if t >= IMPACT:
        tt = t - IMPACT
        radial(base, 960 + shake[0], 560, 620, 0.7 * math.exp(-tt * 14))
        ring(base, 960, 560, 60 + 1250 * ease_out(tt / 0.8), 22 + 30 * tt, 0.9 * clamp01(1 - tt / 0.8))
        ring(base, 960, 560, 30 + 780 * ease_out(tt / 0.7), 10, 0.5 * clamp01(1 - tt / 0.7))
    title_pass(base, t)
    slots(base, t)
    # glint across the title block
    if 5.0 <= t <= 5.6:
        k = (t - 5.0) / 0.6; xs = np.arange(W)[None, :].astype(np.float32); ys = np.arange(H)[:, None].astype(np.float32)
        pos = 700 + k * 1500 - ys * 0.55
        band = np.exp(-((xs - pos) / 38) ** 2) * 0.55
        tm = np.clip(np.maximum(TL["l1"]["sharp"][..., 3], TL["l2"]["sharp"][..., 3]), 0, 1)
        base += (band * tm)[..., None] * np.array([1, 1, 0.92])
    # vignette and bloom
    yy, xx = np.mgrid[0:H:8, 0:W:8].astype(np.float32)
    vg = 1 - 0.38 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2
    vg = np.asarray(Image.fromarray((vg * 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)).astype(np.float32) / 255.0
    base *= vg[..., None]
    bright = np.clip(base - 0.78, 0, 1)
    bl = Image.fromarray((np.clip(bright, 0, 1) * 255).astype(np.uint8)).resize((W // 4, H // 4)).filter(ImageFilter.GaussianBlur(9)).resize((W, H), Image.BILINEAR)
    base += np.asarray(bl).astype(np.float32) / 255.0 * 0.55
    # final fade out is not used (the lockup holds into the live cams)
    img = Image.fromarray((np.clip(base, 0, 1) * 255).astype(np.uint8))
    img.save(os.path.join(FR, "f%04d.png" % i), compress_level=1)

if __name__ == "__main__":
    idxs = [int(x) for x in sys.argv[2:]] if len(sys.argv) > 2 else range(N)
    for i in idxs: render(i)
    print("frames done", len(list(idxs)))
