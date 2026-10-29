"""Medieval host name tags for the edit kit (2026-10-26). Original design, owned sounds only.
No studio logos, fonts or art. Fonts are the Windows system fonts Constantia and Georgia.

Concept: a banner on an iron rod. It unrolls, a wax seal is stamped on it, the handle is inked in,
a rule is drawn, then it rolls back up. Handle only, no sub line. Scaled to the 820x190 VQ tag footprint at (90,790).
  KING-Z      crimson wax, gold crown, warm torch flicker, embers.
  Winter Wolf frost wax, wolf head, cool flicker, frost creeping over the parchment, falling snow motes.
Both carry a thin frost-cyan stitched border (the show colour).

  python make_host_tags_medieval.py [--only kingz,wolf] [--test]   (--test dumps key frames to scratch only)
Writes to P:\\WWD Kit\\Host Tags\\ : Host Tag - X.mov (alpha), Host Tag - X (MP4 green).mp4 (chroma green),
and copies of the owned sounds into P:\\WWD Kit\\Host Tags\\Sounds\\.
Remake by running again (overwrites).
"""
import argparse, math, os, random, shutil, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, FPS, blank, put_tl, fade, ease_out  # noqa: E402

OUT = "P:\\WWD Kit\\Host Tags\\"
SFXD = "P:\\Sounds\\Sound FX\\"
SCRATCH = "D:\\WKP\\scratch\\host_tags\\"
SNAP = {
    "sword": SFXD + "sword-pull-from-sheathe_zyjdbqEu.mp3",
    "hit": SFXD + "hit-metal-hard_M1WQr3Eu.mp3",
    "fire": SFXD + "fire-wood-crackle-flames_G1y2ewE_.mp3",
    "frost": SFXD + "audioblocks-frost-low-whoosh_BWSg1QdQKvL.mp3",
}
for p in SNAP.values():
    assert os.path.exists(p), p

CONSTB = r"C:\Windows\Fonts\constanb.ttf"
CONSTI = r"C:\Windows\Fonts\constani.ttf"
N = 108                      # 3.6 s at 30 fps, same as the Vision Quest tags
RW, RH, RX, RY = 1100, 520, 20, 520   # region canvas and where it sits on the 1920x1080 frame
BW, BH = 800, 180            # banner size (fits the 820x190 Vision Quest footprint after scaling)
SX, SY = 92, 90              # seal centre inside the banner
TX, TW = 170, 590            # handle area
FOOT = (90, 790, 820, 190)   # target footprint on the 1920x1080 frame: x, y, w, h (same as the VQ AI tags)
BXr, BYr = 60, 216           # banner top-left inside the region
ROD_Y = 214
FOOT_L, FOOT_T, FOOT_W, FOOT_H = BXr - 32, 200, BW + 78, 196   # content bounds in region coords
PAD = 20
INK = (38, 24, 14)
FROST = (70, 200, 235)
GREEN = (0, 177, 64)

TAGS = {
    "kingz": dict(file="KING-Z", name="KING-Z", 
                  wax=(150, 22, 30), emblem="crown", emb_col=(236, 190, 72), accent=(176, 132, 40),
                  tint=(1.0, 0.965, 0.89), flick=0.05, ring=(255, 210, 120), seed=3),
    "wolf": dict(file="Winter Wolf", name="WINTER WOLF", 
                 wax=(58, 130, 178), emblem="wolf", emb_col=(232, 247, 255), accent=(40, 150, 200),
                 tint=(0.93, 0.98, 1.05), flick=0.03, ring=(170, 236, 255), seed=8),
}


def clamp(v, a=0.0, b=1.0):
    return max(a, min(b, v))


def ease_in(t):
    t = clamp(t)
    return t * t * t


def noise(w, h, scale, rng):
    small = rng.random((h // scale + 3, w // scale + 3)).astype(np.float32)
    im = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    return np.asarray(im, np.float32) / 255.0


def parchment(seed):
    """Aged parchment with torn edge, swallowtail bottom. Returns (RGBA image, L mask)."""
    rng = np.random.default_rng(seed)
    S = 2
    w, h = BW, BH
    tex = 0.5 * noise(w, h, 64, rng) + 0.3 * noise(w, h, 16, rng) + 0.2 * noise(w, h, 4, rng)
    base = np.array([218, 196, 152], np.float32)
    dark = np.array([150, 112, 66], np.float32)
    k = np.clip((tex - 0.25) * 1.6, 0, 1)[..., None]
    col = base * (1 - 0.55 * k) + dark * (0.55 * k)
    # fibres
    fib = noise(w, h, 2, rng)[..., None]
    col = col * (0.94 + 0.12 * fib)
    # torn outline, drawn at 2x then reduced for smooth edges
    r2 = random.Random(seed)
    pts = []

    def jitter(n, amp):
        ph = [r2.uniform(0, 6.28) for _ in range(3)]
        return [amp * (0.6 * math.sin(i / 5.0 + ph[0]) + 0.3 * math.sin(i / 2.3 + ph[1]) + 0.4 * r2.uniform(-1, 1)) for i in range(n)]

    notch_x, notch_d, notch_w = w / 2, 26, 60
    # top edge straight, down the right, bottom with swallowtail, up the left
    pts.append((0, 0))
    pts.append((w, 0))
    jr = jitter(int(h / 6), 4)
    for i, j in enumerate(jr):
        pts.append((w - 3 + j, i * 6))
    bottom_r = [(w - 3, h)]
    pts += bottom_r
    seg = jitter(int((w / 2 - notch_w) / 6), 4)
    for i, j in enumerate(seg):
        x = (w - 3) - i * 6
        if x < notch_x + notch_w:
            break
        pts.append((x, h - 2 + j))
    pts.append((notch_x + notch_w, h))
    pts.append((notch_x, h - notch_d))
    pts.append((notch_x - notch_w, h))
    seg = jitter(int((w / 2 - notch_w) / 6), 4)
    for i, j in enumerate(seg):
        x = notch_x - notch_w - i * 6
        if x < 3:
            break
        pts.append((x, h - 2 + j))
    pts.append((3, h))
    jl = jitter(int(h / 6), 4)
    for i, j in enumerate(jl):
        pts.append((3 + j, h - i * 6))
    m = Image.new("L", (w * S, h * S), 0)
    ImageDraw.Draw(m).polygon([(x * S, y * S) for x, y in pts], fill=255)
    mask = m.resize((w, h), Image.LANCZOS)
    inner = np.asarray(mask.filter(ImageFilter.GaussianBlur(11)), np.float32) / 255.0
    burn = (0.50 + 0.50 * np.clip(inner * 1.25, 0, 1) ** 0.8)[..., None]
    col = col * burn
    # a few foxing stains
    for _ in range(14):
        cx, cy, rr = int(rng.integers(0, w)), int(rng.integers(0, h)), int(rng.integers(10, 40))
        st = Image.new("L", (w, h), 0)
        ImageDraw.Draw(st).ellipse((cx - rr, cy - rr, cx + rr, cy + rr), fill=int(rng.integers(20, 55)))
        st = np.asarray(st.filter(ImageFilter.GaussianBlur(rr / 2)), np.float32)[..., None] / 255.0
        col = col * (1 - st * 0.5)
    rgba = np.dstack([np.clip(col, 0, 255).astype(np.uint8), np.asarray(mask)])
    return Image.fromarray(rgba, "RGBA"), mask


def emblem_polys(kind):
    """Polygons in a 0..100 box. Returns list of (points, role) role in fill|cut."""
    if kind == "crown":
        crown = [(18, 70), (14, 32), (34, 50), (50, 18), (66, 50), (86, 32), (82, 70)]
        band = [(18, 74), (82, 74), (82, 88), (18, 88)]
        return [(crown, "fill"), (band, "fill")], [(14, 30, 6), (50, 16, 6), (86, 30, 6)]
    half = [(50, 24), (62, 24), (70, 3), (78, 34), (90, 54), (82, 62), (86, 76), (70, 74), (60, 90), (54, 96), (50, 98)]
    full = half + [(100 - x, y) for x, y in reversed(half)]
    eye_r = [(57, 53), (71, 47), (66, 57)]
    eye_l = [(100 - x, y) for x, y in eye_r]
    return [(full, "fill"), (eye_r, "cut"), (eye_l, "cut")], [(50, 91, 5, "cutc")]


def seal_img(t, r=54):
    S = 4
    sz = (2 * r + 24) * S
    cx = cy = sz // 2
    rng = random.Random(t["seed"])
    ph = [rng.uniform(0, 6.28) for _ in range(4)]
    pts = []
    for a in range(0, 360, 4):
        ang = math.radians(a)
        rr = r * S * (1 + 0.035 * math.sin(3 * ang + ph[0]) + 0.025 * math.sin(7 * ang + ph[1]) + 0.015 * math.sin(13 * ang + ph[2]))
        pts.append((cx + rr * math.cos(ang), cy + rr * math.sin(ang)))
    mask = Image.new("L", (sz, sz), 0)
    ImageDraw.Draw(mask).polygon(pts, fill=255)
    yy, xx = np.mgrid[0:sz, 0:sz].astype(np.float32)
    d = np.sqrt((xx - (cx - 0.3 * r * S)) ** 2 + (yy - (cy - 0.35 * r * S)) ** 2) / (r * S * 1.6)
    shade = np.clip(1.28 - d, 0.6, 1.3)[..., None]
    wax = np.array(t["wax"], np.float32)
    col = np.clip(wax * shade, 0, 255).astype(np.uint8)
    im = Image.fromarray(np.dstack([col, np.full((sz, sz), 255, np.uint8)]), "RGBA")
    d_ = ImageDraw.Draw(im)
    dark = tuple(int(c * 0.55) for c in t["wax"]) + (255,)
    light = tuple(min(255, int(c * 1.35) + 20) for c in t["wax"]) + (255,)
    rr = int(r * S * 0.80)
    d_.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=dark, width=S * 3)
    d_.ellipse((cx - rr + S * 3, cy - rr + S * 3, cx + rr - S * 3, cy + rr - S * 3), outline=light, width=S * 2)
    polys, extras = emblem_polys(t["emblem"])
    size = int(r * S * 1.12)
    ox, oy = cx - size / 2, cy - size / 2

    def tr(p, dx=0, dy=0):
        return [(ox + x * size / 100 + dx, oy + y * size / 100 + dy) for x, y in p]

    def draw_all(fillc, dx, dy):
        for pl, role in polys:
            if role == "fill":
                d_.polygon(tr(pl, dx, dy), fill=fillc)
        for e in extras:
            if len(e) == 3:
                x, y, rd = e
                d_.ellipse((ox + (x - rd) * size / 100 + dx, oy + (y - rd) * size / 100 + dy,
                            ox + (x + rd) * size / 100 + dx, oy + (y + rd) * size / 100 + dy), fill=fillc)

    draw_all(dark, 3 * S // 2, 3 * S // 2)
    draw_all(light, -S, -S)
    draw_all(t["emb_col"] + (255,), 0, 0)
    for pl, role in polys:
        if role == "cut":
            d_.polygon(tr(pl), fill=dark)
    for e in extras:
        if len(e) == 4:
            x, y, rd, _ = e
            d_.ellipse((ox + (x - rd) * size / 100, oy + (y - rd) * size / 100, ox + (x + rd) * size / 100, oy + (y + rd) * size / 100), fill=dark)
    im.putalpha(Image.fromarray(np.minimum(np.asarray(im.getchannel("A")), np.asarray(mask))))
    return im.resize((sz // S, sz // S), Image.LANCZOS)


def build_frost(seed):
    """Frost branches in banner coords: (x0,y0,x1,y1,t0,t1,width)."""
    rng = random.Random(seed)
    segs = []

    def branch(x, y, ang, ln, depth, t0):
        x1, y1 = x + ln * math.cos(ang), y + ln * math.sin(ang)
        t1 = t0 + 0.10 + 0.04 * ln / 20
        segs.append((x, y, x1, y1, t0, t1, 2 if depth == 0 else 1))
        if depth < 2 and ln > 9:
            for s in (-1, 1):
                if rng.random() < 0.85:
                    branch(x + (x1 - x) * 0.55, y + (y1 - y) * 0.55, ang + s * math.radians(55), ln * 0.5, depth + 1, t1 - 0.04)

    for x in range(14, BW - 10, 26):
        x += rng.randint(-8, 8)
        y = BH - 4
        if abs(x - BW / 2) < 60:
            y = BH - 26 + abs(x - BW / 2) * 26 / 60 - 4
        branch(x, y, -math.pi / 2 + rng.uniform(-0.5, 0.5), rng.uniform(12, 24), 0, rng.uniform(0, 0.55))
    for cx, cy, a0 in ((6, BH - 6, -0.6), (BW - 6, BH - 6, -2.5), (BW - 6, 6, 2.3), (6, 6, 0.8)):
        for k in range(5):
            branch(cx, cy, a0 + rng.uniform(-0.7, 0.7), rng.uniform(22, 38), 0, rng.uniform(0.1, 0.6))
    return segs


def fit_size(text, track, avail):
    for sz in range(90, 30, -1):
        f = ImageFont.truetype(CONSTB, sz)
        wd = sum(f.getlength(c) + track for c in text) - track
        if wd <= avail:
            return sz
    return 30


def build_particles(t, rng):
    parts = []
    seal_c = (BXr + SX, BYr + SY)
    if t["emblem"] == "crown":
        for _ in range(46):  # burst at stamp
            a = rng.uniform(math.pi * 1.05, math.pi * 1.95)
            sp = rng.uniform(2.5, 9.0)
            parts.append(dict(x=seal_c[0], y=seal_c[1], vx=math.cos(a) * sp, vy=math.sin(a) * sp * 0.9 - 1.5, g=-0.02, t0=16, life=rng.randint(22, 42),
                              r=rng.uniform(1.6, 3.6), c=(255, rng.randint(140, 210), 50), kind="dot"))
        for _ in range(30):  # trickle from the rod
            parts.append(dict(x=BXr + rng.uniform(20, BW), y=ROD_Y, vx=rng.uniform(-0.4, 0.8), vy=rng.uniform(-2.0, -0.9), g=0.0,
                              t0=rng.randint(8, 78), life=rng.randint(26, 46), r=rng.uniform(1.2, 2.6), c=(255, rng.randint(120, 190), 40), kind="dot"))
    else:
        for _ in range(40):  # ice burst
            a = rng.uniform(math.pi * 1.0, math.pi * 2.0)
            sp = rng.uniform(2.5, 8.5)
            parts.append(dict(x=seal_c[0], y=seal_c[1], vx=math.cos(a) * sp, vy=math.sin(a) * sp - 1.0, g=0.12, t0=16, life=rng.randint(22, 40),
                              r=rng.uniform(2.5, 5.5), c=(200, 240, 255), kind="shard"))
        for _ in range(34):  # snow motes
            parts.append(dict(x=BXr + rng.uniform(0, BW + 40), y=ROD_Y + rng.uniform(-30, 20), vx=rng.uniform(-0.6, 0.6), vy=rng.uniform(0.6, 1.6), g=0.0,
                              t0=rng.randint(6, 74), life=rng.randint(30, 52), r=rng.uniform(1.4, 2.8), c=(225, 247, 255), kind="dot"))
    return parts


def draw_particles(layer_sharp, layer_glow, parts, i):
    ds, dg = ImageDraw.Draw(layer_sharp), ImageDraw.Draw(layer_glow)
    for p in parts:
        age = i - p["t0"]
        if age < 0 or age > p["life"]:
            continue
        x = p["x"] + p["vx"] * age
        y = p["y"] + p["vy"] * age + 0.5 * p["g"] * age * age
        k = 1 - age / p["life"]
        a = int(255 * min(1, k * 1.6))
        r = p["r"] * (0.5 + 0.5 * k)
        c = p["c"]
        if p["kind"] == "shard":
            ang = math.atan2(p["vy"] + p["g"] * age, p["vx"])
            dx, dy = math.cos(ang) * r * 2.2, math.sin(ang) * r * 2.2
            px, py = -dy * 0.35, dx * 0.35
            poly = [(x + dx, y + dy), (x + px, y + py), (x - dx, y - dy), (x - px, y - py)]
            ds.polygon(poly, fill=c + (a,))
            dg.polygon(poly, fill=(90, 210, 255, a))
        else:
            ds.ellipse((x - r, y - r, x + r, y + r), fill=c + (a,))
            dg.ellipse((x - r * 2.6, y - r * 2.6, x + r * 2.6, y + r * 2.6), fill=c + (int(a * 0.6),))


def build_tag(key):
    t = TAGS[key]
    par, mask = parchment(t["seed"] * 7 + 1)
    seal = seal_img(t)
    frost = build_frost(t["seed"]) if key == "wolf" else []
    rng = random.Random(t["seed"] + 100)
    parts = build_particles(t, rng)
    track = 5
    fsz = fit_size(TAGS["wolf"]["name"], track, TW)  # same size for both, so they match as a pair
    fname = ImageFont.truetype(CONSTB, fsz)
    nw = sum(fname.getlength(c) + track for c in t["name"]) - track
    letters = []
    x = TX + (TW - nw) / 2
    for c in t["name"]:
        letters.append((c, x))
        x += fname.getlength(c) + track
    name_w = nw
    hb = fname.getbbox("H")
    name_y = 76 - (hb[1] + hb[3]) / 2
    # pre-render the static ornament layer (border, ruled line placeholders drawn per frame)
    return dict(t=t, par=par, mask=mask, seal=seal, frost=frost, parts=parts, fname=fname, name_y=name_y,
                letters=letters, name_w=name_w, TX=TX, key=key)


def banner_layer(b, i):
    t = b["t"]
    ban = b["par"].copy()
    d = ImageDraw.Draw(ban)
    # stitched frost-cyan border, same on both tags
    cy_ = FROST + (210,)
    ins = 20
    def dashes(x0, y0, x1, y1):
        L = math.hypot(x1 - x0, y1 - y0)
        n = int(L // 14)
        for k in range(n):
            a, c = k * 14, k * 14 + 8
            d.line((x0 + (x1 - x0) * a / L, y0 + (y1 - y0) * a / L, x0 + (x1 - x0) * c / L, y0 + (y1 - y0) * c / L), fill=cy_, width=3)
    dashes(ins, ins + 8, BW - ins, ins + 8)
    dashes(ins, ins + 8, ins, BH - ins)
    dashes(BW - ins, ins + 8, BW - ins, BH - ins)
    dashes(ins, BH - ins, BW / 2 - 70, BH - ins)
    dashes(BW / 2 + 70, BH - ins, BW - ins, BH - ins)
    # ink rule under the name
    rp = ease_out(clamp((i - 38) / 11))
    if rp > 0:
        y = 126
        x1 = b["TX"] + TW * rp
        d.line((b["TX"], y, x1, y), fill=t["accent"] + (255,), width=3)
        d.line((b["TX"], y + 6, b["TX"] + (TW - 80) * rp, y + 6), fill=t["accent"] + (150,), width=1)
        if rp > 0.98:
            for xx in (b["TX"], b["TX"] + TW):
                d.polygon([(xx - 7, y), (xx, y - 7), (xx + 7, y), (xx, y + 7)], fill=t["accent"] + (255,))
    # frost creeping (wolf)
    if b["frost"]:
        lay = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        prog = clamp((i - 20) / 42)
        for x0, y0, x1, y1, ta, tb, wd in b["frost"]:
            if prog <= ta:
                continue
            f = clamp((prog - ta) / (tb - ta))
            ld.line((x0, y0, x0 + (x1 - x0) * f, y0 + (y1 - y0) * f), fill=(238, 252, 255, 235), width=wd)
        lay.paste((0, 0, 0, 0), (TX - 15, 30, TX + TW + 15, 136))   # keep frost off the text area
        glow = lay.filter(ImageFilter.GaussianBlur(3))
        g = np.asarray(glow).copy()
        g[..., 0], g[..., 1], g[..., 2] = 80, 200, 245
        glow = Image.fromarray(g, "RGBA")
        lay.alpha_composite(Image.new("RGBA", (1, 1)), (0, 0))
        ban.alpha_composite(glow)
        ban.alpha_composite(lay)
    # name, letter by letter, ink bleed
    ink_s = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
    ink_b = Image.new("RGBA", (BW, BH), (0, 0, 0, 0))
    ds, db = ImageDraw.Draw(ink_s), ImageDraw.Draw(ink_b)
    n = len(b["letters"])
    for j, (c, x) in enumerate(b["letters"]):
        s0 = 20 + j * (16.0 / n)
        a = clamp((i - s0) / 3.5)
        if a <= 0:
            continue
        sc = 1.0
        ds.text((x, b["name_y"]), c, font=b["fname"], fill=INK + (int(255 * a),))
        db.text((x, b["name_y"] + 2), c, font=b["fname"], fill=INK + (int(110 * a),))
    ink_b = ink_b.filter(ImageFilter.GaussianBlur(2.2))
    ban.alpha_composite(ink_b)
    ban.alpha_composite(ink_s)
    # seal stamp
    sj = i - 12
    if sj >= 0:
        k = ease_out(sj / 5)
        sc = 1.0 + 0.75 * (1 - k)
        al = clamp(sj / 2)
        sl = b["seal"]
        sl2 = sl.resize((int(sl.width * sc), int(sl.height * sc)), Image.BICUBIC)
        # squash a touch on landing
        if 4 <= sj <= 8:
            q = 1.0 - 0.06 * math.sin((sj - 4) / 4 * math.pi)
            sl2 = sl2.resize((int(sl2.width * (2 - q)), int(sl2.height * q)), Image.BICUBIC)
        if al < 1:
            sl2 = fade(sl2, al)
        # soft shadow
        sh = Image.new("RGBA", sl2.size, (0, 0, 0, 0))
        sh.putalpha(sl2.getchannel("A").point(lambda v: int(v * 0.5)))
        sh = sh.filter(ImageFilter.GaussianBlur(5))
        cx, cy = SX, SY
        ban.alpha_composite(sh, (cx - sh.width // 2 + 5, cy - sh.height // 2 + 7))
        ban.alpha_composite(sl2, (cx - sl2.width // 2, cy - sl2.height // 2))
    return ban


def frame(b, i):
    t = b["t"]
    cv = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    # timeline
    rod_p = ease_out(i / 7)
    un = ease_out(clamp((i - 4) / 11))
    out = ease_in(clamp((i - 95) / 12))
    reveal = un * (1 - out)
    glob = 1.0 - clamp((i - 100) / 8) * 0.0
    k_alpha = 1.0 if i < 98 else clamp((N - i) / 10)
    if reveal > 0.005:
        ban = banner_layer(b, i)
        # light flicker and tint
        fl = 1 + t["flick"] * (math.sin(i * 1.9) * 0.6 + math.sin(i * 4.3 + 1.0) * 0.4) + (0.07 * max(0, 1 - (i - 16) / 6) if i >= 16 else 0)
        arr = np.asarray(ban).astype(np.float32)
        for c in range(3):
            arr[..., c] *= fl * t["tint"][c]
        ban = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGBA")
        # unroll crop
        hcut = int(BH * reveal)
        arr = np.asarray(ban).copy()
        arr[hcut:, :, 3] = 0
        ban = Image.fromarray(arr, "RGBA")
        layer = Image.new("RGBA", (BW + 2 * PAD, BH + 2 * PAD), (0, 0, 0, 0))
        layer.alpha_composite(ban, (PAD, PAD))
        ld = ImageDraw.Draw(layer)
        if 0 < reveal < 0.97:  # rolled front edge
            ra = int(255 * (1 - clamp((reveal - 0.80) / 0.17)))
            ry = PAD + hcut
            ld.rounded_rectangle((PAD + 6, ry - 4, PAD + BW - 6, ry + 13), 8, fill=(196, 168, 118, ra), outline=(110, 80, 44, ra), width=2)
            ld.line((PAD + 12, ry + 2, PAD + BW - 12, ry + 2), fill=(236, 216, 170, ra), width=2)
        # sway about the top centre
        age = i - 8
        ang = 0.0
        if age > 0:
            ang += 1.6 * math.sin(age / 3.0) * math.exp(-age / 22.0)
        if i >= 16:
            ang += -2.2 * math.sin((i - 16) / 2.6) * math.exp(-(i - 16) / 9.0)  # jolt from the stamp
        layer = layer.rotate(ang, center=((BW + 2 * PAD) / 2, PAD), resample=Image.BICUBIC)
        sh = Image.new("RGBA", layer.size, (0, 0, 0, 0))
        sh.putalpha(layer.getchannel("A").point(lambda v: int(v * 0.45)))
        sh = sh.filter(ImageFilter.GaussianBlur(9))
        cv.alpha_composite(sh, (BXr - PAD + 6, BYr - PAD + 11))
        cv.alpha_composite(layer, (BXr - PAD, BYr - PAD))
    # rod
    rl = int((BW + 40) * rod_p)
    if rl > 4:
        rd = ImageDraw.Draw(cv)
        x0 = BXr - 20
        x1 = x0 + rl
        rd.rounded_rectangle((x0, ROD_Y - 8, x1, ROD_Y + 8), 6, fill=(36, 38, 44, 255))
        rd.line((x0 + 4, ROD_Y - 5, x1 - 4, ROD_Y - 5), fill=(120, 126, 138, 255), width=3)
        rd.line((x0 + 4, ROD_Y + 5, x1 - 4, ROD_Y + 5), fill=(18, 18, 22, 255), width=2)
        # finials: left ball, right spear point at the leading end
        rd.ellipse((x0 - 12, ROD_Y - 14, x0 + 12, ROD_Y + 14), fill=(46, 48, 56, 255), outline=(130, 136, 148, 255), width=2)
        rd.polygon([(x1, ROD_Y - 12), (x1 + 26, ROD_Y), (x1, ROD_Y + 12)], fill=(70, 74, 84, 255), outline=(140, 146, 158, 255))
        rd.ellipse((x1 - 6, ROD_Y - 12, x1 + 6, ROD_Y + 12), fill=(46, 48, 56, 255))
        # frost-cyan ring clasps
        for cx in (BXr + 25, BXr + BW - 25):
            if cx < x1:
                rd.ellipse((cx - 10, ROD_Y - 13, cx + 10, ROD_Y + 13), outline=FROST + (255,), width=3)
    # shockwave at the stamp
    sj = i - 16
    if 0 <= sj < 9:
        rr = 28 + sj * 11
        a = int(220 * (1 - sj / 9))
        rg = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
        ImageDraw.Draw(rg).ellipse((BXr + SX - rr, BYr + SY - rr, BXr + SX + rr, BYr + SY + rr), outline=t["ring"] + (a,), width=4)
        cv.alpha_composite(rg)
    # particles
    sharp = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    glow = Image.new("RGBA", (RW, RH), (0, 0, 0, 0))
    draw_particles(sharp, glow, b["parts"], i)
    cv.alpha_composite(glow.filter(ImageFilter.GaussianBlur(5)))
    cv.alpha_composite(sharp)
    if k_alpha < 1:
        cv = fade(cv, k_alpha)
    sc = min(FOOT[2] / FOOT_W, FOOT[3] / FOOT_H)
    cv = cv.resize((int(RW * sc), int(RH * sc)), Image.LANCZOS)
    full = blank()
    put_tl(full, cv, int(FOOT[0] - FOOT_L * sc), int(FOOT[1] - FOOT_T * sc))
    return full


def cue(src, start_s, dur_s, delay_ms, vol, fin=0.02, fout=0.2):
    return dict(src=src, ss=start_s, t=dur_s, ms=delay_ms, vol=vol, fin=fin, fout=fout)


CUES = {
    "kingz": [cue(SNAP["sword"], 0, 0.34, 70, 0.55, 0.0, 0.05),
              cue(SNAP["hit"], 0, 1.7, 500, 0.42, 0.0, 0.8),
              cue(SNAP["fire"], 10.0, 3.5, 40, 0.20, 0.3, 0.7)],
    "wolf": [cue(SNAP["frost"], 0, 2.0, 0, 0.45, 0.02, 0.9),
             cue(SNAP["hit"], 0, 1.7, 500, 0.34, 0.0, 0.8)],
}


def make_audio(key, path):
    cmd = ["ffmpeg", "-v", "error", "-y"]
    parts = []
    cs = CUES[key]
    for k, c in enumerate(cs):
        cmd += ["-ss", f"{c['ss']}", "-t", f"{c['t']}", "-i", c["src"]]
        parts.append(f"[{k}:a]aformat=sample_rates=48000:channel_layouts=stereo,afade=t=in:d={max(c['fin'], 0.001)},"
                     f"afade=t=out:st={max(0.0, c['t'] - c['fout']):.3f}:d={c['fout']},volume={c['vol']},adelay={c['ms']}:all=1[a{k}]")
    fc = ";".join(parts) + ";" + "".join(f"[a{k}]" for k in range(len(cs))) + f"amix=inputs={len(cs)}:normalize=0,apad[a]"
    cmd += ["-filter_complex", fc, "-map", "[a]", "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{N / FPS:.3f}", path]
    subprocess.run(cmd, check=True)


def render(key, test=False):
    b = build_tag(key)
    t = b["t"]
    os.makedirs(SCRATCH, exist_ok=True)
    if test:
        for i in (6, 14, 24, 27, 40, 60, 80, 100):
            frame(b, i).save(SCRATCH + f"test_{key}_{i:03d}.png")
        print("test frames in", SCRATCH)
        return
    os.makedirs(OUT, exist_ok=True)
    wav = SCRATCH + f"{key}_audio.wav"
    make_audio(key, wav)
    mov = OUT + f"Host Tag - {t['file']}.mov"
    mp4 = OUT + f"Host Tag - {t['file']} (MP4 green).mp4"
    with tempfile.TemporaryDirectory(dir=SCRATCH) as tmp:
        os.makedirs(tmp + "\\a"), os.makedirs(tmp + "\\g")
        for i in range(N):
            im = frame(b, i)
            im.save(f"{tmp}\\a\\f{i:04d}.png", compress_level=1)
            g = Image.new("RGBA", (W, H), GREEN + (255,))
            g.alpha_composite(im)
            g.convert("RGB").save(f"{tmp}\\g\\f{i:04d}.png", compress_level=1)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}\\a\\f%04d.png", "-i", wav,
                        "-map", "0:v", "-map", "1:a", "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le",
                        "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{N / FPS:.3f}", mov], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", f"{tmp}\\g\\f%04d.png", "-i", wav,
                        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-crf", "14", "-pix_fmt", "yuv420p", "-r", str(FPS),
                        "-c:a", "aac", "-b:a", "192k", "-t", f"{N / FPS:.3f}", "-movflags", "+faststart", mp4], check=True)
    print("wrote", mov, mp4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="kingz,wolf")
    ap.add_argument("--test", action="store_true")
    a = ap.parse_args()
    if not a.test:
        sd = OUT + "Sounds\\"
        os.makedirs(sd, exist_ok=True)
        notes = {"sword": "KING-Z: blade drawn as the banner drops",
                 "hit": "both: seal stamp (iron hit, trimmed to 1.7 s in the mix)",
                 "fire": "KING-Z: torch crackle bed, from 10 s into the file",
                 "frost": "Winter Wolf: frost whoosh as the banner drops"}
        for k, src in SNAP.items():
            dst = sd + os.path.basename(src)
            shutil.copy2(src, dst)
        with open(sd + "CUES.txt", "w", encoding="utf-8") as f:
            for k, src in SNAP.items():
                f.write(f"{os.path.basename(src)}  =  {notes[k]}\n")
    for k in a.only.split(","):
        render(k.strip(), a.test)


if __name__ == "__main__":
    main()
