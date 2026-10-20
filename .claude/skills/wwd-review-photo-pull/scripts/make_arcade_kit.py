"""Arcade kit for the Street Fighter review (V1 rounds, V2 versus, V3 health bars, V5 combo,
V8 continue card, V10 fireball). Original looks, owned sounds only. Never use Capcom art,
font, logo or audio.

  python make_arcade_kit.py [--out "P:\\WWD Kit\\Street Fighter"] [--only round,versus,tags,combo,continue,fireball]
  python make_arcade_kit.py --only continue --title "CRYSTAL LAKE" --sub "SEASON 1 REVIEW" --name "Continue - Crystal Lake"
"""
import argparse, os, subprocess, tempfile, functools
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1920, 1080, 30
FONT = r"C:\Windows\Fonts\impact.ttf"
SFX = "P:\\Sounds\\Sound FX\\"
GONG = SFX + "hit-metal-gong-bell-deep_M17-SnNu.mp3"
PUNCH_HARD = SFX + "Adobe\\Impacts\\Impact Punch Hard Single 01.wav"
PUNCH = SFX + "Adobe\\Impacts\\Impact Punch Single 01.wav"
SIZZLE = SFX + "electric-sizzle_zyuNWG4u.mp3"
BLEEP = SFX + "Adobe\\Technology\\Technology Electronic Buttons Arcade Game Buttons Single 01.wav"
COIN = SFX + "Adobe\\Foley\\Foley Coin Drop On Wood Platform 05.wav"
WHOOSH = SFX + "fireball-whoosh_GknWsSNu.mp3"

PAL = {
    "gold": ((255, 244, 120), (255, 170, 30), (220, 60, 20)),
    "fire": ((255, 230, 120), (255, 110, 20), (200, 10, 10)),
    "white": ((255, 255, 255), (235, 235, 240), (165, 170, 185)),
}


def ease_out(t):
    t = min(max(t, 0.0), 1.0)
    return 1 - (1 - t) ** 3


def blank():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def fade(im, k):
    im = im.copy()
    im.putalpha(im.getchannel("A").point(lambda v: int(v * k)))
    return im


def put_tl(cv, im, x, y):
    sx, sy = max(0, -x), max(0, -y)
    ex, ey = min(im.width, W - x), min(im.height, H - y)
    if ex <= sx or ey <= sy:
        return
    cv.alpha_composite(im.crop((sx, sy, ex, ey)), (x + sx, y + sy))


def put(cv, im, cx, cy, scale=1.0, alpha=1.0):
    if scale != 1.0:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.BICUBIC)
    if alpha < 1.0:
        im = fade(im, alpha)
    put_tl(cv, im, int(cx - im.width / 2), int(cy - im.height / 2))


@functools.lru_cache(maxsize=None)
def grad_text(s, size, pal="gold", outline=10):
    f = ImageFont.truetype(FONT, size)
    b = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), s, font=f)
    pad = outline * 2 + 20
    w, h = b[2] - b[0] + pad * 2, b[3] - b[1] + pad * 2
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((pad - b[0], pad - b[1]), s, font=f, fill=255)
    top, mid, bot = [np.array(c, float) for c in PAL[pal]]
    g = np.linspace(0, 1, h)[:, None, None]
    col = np.where(g < 0.5, top + (mid - top) * (g / 0.5), mid + (bot - mid) * ((g - 0.5) / 0.5))
    fill = Image.fromarray(np.broadcast_to(col, (h, w, 3)).astype(np.uint8), "RGB").convert("RGBA")
    fill.putalpha(m)
    ol = m.filter(ImageFilter.MaxFilter(outline * 2 + 1))
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    sh.putalpha(ol.filter(ImageFilter.GaussianBlur(5)).point(lambda v: int(v * 0.8)))
    out.alpha_composite(sh, (6, 8))
    ring = Image.new("RGBA", (w, h), (55, 6, 6, 255))
    ring.putalpha(ol)
    out.alpha_composite(ring)
    out.alpha_composite(fill)
    return out


def band(cv, y0, y1, alpha):
    y0, y1 = int(y0), int(y1)
    if y1 <= y0 or alpha <= 0:
        return
    arr = np.zeros((y1 - y0, W, 4), np.uint8)
    arr[..., 3] = alpha
    arr[::4, :, 3] = min(255, alpha + 45)
    put_tl(cv, Image.fromarray(arr, "RGBA"), 0, y0)


def flash(cv, a):
    if a > 0:
        cv.alpha_composite(Image.new("RGBA", (W, H), (255, 255, 255, int(a))))


def render(make_frame, n, out, audio, alpha=True):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            im = make_frame(i)
            if not alpha:
                im = im.convert("RGB")
            im.save(os.path.join(tmp, f"f{i:04d}.png"), compress_level=1)
        cmd = ["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png")]
        for p, _, _ in audio:
            cmd += ["-i", p]
        parts = [f"[{k + 1}:a]adelay={ms}:all=1,volume={vol}[a{k}]" for k, (_, ms, vol) in enumerate(audio)]
        if len(audio) == 1:
            fc = parts[0] + ";[a0]apad[a]"
        else:
            fc = ";".join(parts) + ";" + "".join(f"[a{k}]" for k in range(len(audio))) + f"amix=inputs={len(audio)}:normalize=0,apad[a]"
        cmd += ["-filter_complex", fc, "-map", "0:v", "-map", "[a]"]
        if alpha:
            cmd += ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le"]
        else:
            cmd += ["-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le"]
        cmd += ["-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{n / FPS:.3f}", out]
        subprocess.run(cmd, check=True)
    print("wrote", out)


# ---------- V1 rounds ----------
def round_frame(label, n=66):
    def f(i):
        cv = blank()
        k = ease_out(i / 5)
        out_k = 1 - max(0, i - (n - 8)) / 8
        band(cv, 540 - 160 * k, 540 + 160 * k, int(205 * out_k))
        if i < 30:
            s = 1 + 0.7 * (1 - ease_out(i / 6))
            dx = (12 - 3 * i) * (1 if i % 2 else -1) if i < 4 else 0
            put(cv, grad_text(label, 230, "gold"), 960 + dx, 540, s, out_k)
        else:
            j = i - 30
            s = 1 + 0.9 * (1 - ease_out(j / 6))
            dx = (16 - 3 * j) * (1 if j % 2 else -1) if j < 5 else 0
            put(cv, grad_text("FIGHT!", 290, "fire"), 960 + dx, 540, s, out_k)
            flash(cv, 120 - 40 * j if j < 3 else 0)
        return cv
    return f


def make_rounds(out):
    for r in (1, 2, 3):
        render(round_frame(f"ROUND {r}"), 66, os.path.join(out, f"Round {r}.mov"),
               [(GONG, 0, 1.0), (PUNCH_HARD, 1000, 1.0)])


# ---------- V2 versus ----------
def plate(text, color):
    w, h, sk = 840, 200, 46
    im = Image.new("RGBA", (w + 20, h + 20), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    poly = [(10 + sk, 10), (10 + w, 10), (10 + w - sk, 10 + h), (10, 10 + h)]
    d.polygon(poly, fill=color + (235,), outline=(255, 255, 255, 255), width=6)
    arr = np.asarray(im).copy()
    arr[10::5, :, :3] = (arr[10::5, :, :3] * 0.8).astype(np.uint8)
    im = Image.fromarray(arr, "RGBA")
    t = grad_text(text, 112, "white", 6)
    im.alpha_composite(t, ((im.width - t.width) // 2, (im.height - t.height) // 2))
    return im


def bolt(i):
    rng = np.random.default_rng(i)
    pts, x = [], 960
    for y in range(240, 841, 40):
        x = 960 + int(rng.integers(-42, 43))
        pts.append((x, y))
    glow = blank()
    ImageDraw.Draw(glow).line(pts, fill=(90, 190, 255, 255), width=22, joint="curve")
    glow = glow.filter(ImageFilter.GaussianBlur(10))
    core = blank()
    ImageDraw.Draw(core).line(pts, fill=(255, 255, 255, 255), width=7, joint="curve")
    glow.alpha_composite(core)
    return glow


def versus_frame(n=90):
    ww, kz = plate("WINTER WOLF", (30, 80, 190)), plate("KINGZ", (185, 28, 40))
    def f(i):
        cv = blank()
        out_k = 1 - max(0, i - (n - 10)) / 10
        k_in = ease_out(i / 9)
        k_out = ease_out((i - 76) / 10)
        off = (1 - k_in) * 900 + k_out * 900
        band(cv, 440, 640, int(150 * out_k))
        put(cv, ww, 480 - off, 540, 1, out_k)
        put(cv, kz, 1440 + off, 540, 1, out_k)
        if 10 <= i < 76:
            if (i // 2) % 3 != 2:
                cv.alpha_composite(bolt(i))
            j = i - 10
            s = 1 + 0.9 * (1 - ease_out(j / 6))
            put(cv, grad_text("VS", 250, "fire"), 960, 540, s)
            flash(cv, 110 - 40 * j if j < 3 else 0)
        return cv
    return f


def make_versus(out):
    render(versus_frame(), 90, os.path.join(out, "Versus.mov"),
           [(SIZZLE, 0, 0.8), (PUNCH_HARD, 330, 1.0)])


# ---------- V3 tags and health bars ----------
BAR_Y0, BAR_Y1, BAR_W = 82, 118, 700


def side_img(who, val, chip, flash_a, glow):
    cv = blank()
    d = ImageDraw.Draw(cv)
    left = who == "ww"  # Winter Wolf is on the left of the screen, KingZ on the right
    x0, x1 = (60, 760) if left else (1160, 1860)
    d.rectangle([x0 - 4, BAR_Y0 - 4, x1 + 4, BAR_Y1 + 4], fill=(10, 10, 14, 225), outline=(255, 255, 255, 255), width=3)

    def seg(a):
        return (x1 - BAR_W * a, x1) if left else (x0, x0 + BAR_W * a)

    if chip is not None and chip > val:
        a, b = seg(chip)
        d.rectangle([a, BAR_Y0, b, BAR_Y1], fill=(220, 30, 30, 255))
    a, b = seg(val)
    if b > a:
        col = (255, 215, 40, 255)
        d.rectangle([a, BAR_Y0, b, BAR_Y1], fill=col)
        d.rectangle([a, BAR_Y0, b, BAR_Y0 + 9], fill=(255, 245, 160, 255))
    if flash_a > 0:
        fc = (255, 255, 255) if not glow else (255, 230, 90)
        d.rectangle([x0 - 4, BAR_Y0 - 4, x1 + 4, BAR_Y1 + 4], fill=fc + (int(190 * flash_a),))
    label = "P1  WINTER WOLF" if left else "KINGZ  P2"
    t = grad_text(label, 46, "white", 5)
    cx = x0 + t.width / 2 - 16 if left else x1 - t.width / 2 + 16
    put(cv, t, cx, 52)
    return cv


def tags_img(kz=1.0, ww=1.0, chip_kz=None, chip_ww=None, fl_kz=0, fl_ww=0, dx_kz=0, dx_ww=0, glow=False, drop=0):
    cv = blank()
    put_tl(cv, side_img("kz", kz, chip_kz, fl_kz, glow), int(dx_kz), int(-drop))
    put_tl(cv, side_img("ww", ww, chip_ww, fl_ww, glow), int(dx_ww), int(-drop))
    put(cv, grad_text("KO", 58, "fire", 5), 960, 100 - drop)
    return cv


def hit_frames(who, old, new, other_state):
    def f(i):
        val, chip, fl, dx = old, None, 0, 0
        if 4 <= i < 8:
            val = old + (new - old) * ((i - 4) / 4)
            chip = old
            fl = 1.0 if i < 7 else 0.4
            dx = (10 - 2 * (i - 4)) * (1 if i % 2 else -1)
        elif 8 <= i < 16:
            val, chip = new, old
        elif 16 <= i < 30:
            val, chip = new, new + (old - new) * (1 - (i - 16) / 14)
        elif i >= 30:
            val = new
        kw = dict(kz=other_state if who == "ww" else val, ww=val if who == "ww" else other_state)
        if who == "ww":
            return tags_img(kz=other_state, ww=val, chip_ww=chip, fl_ww=fl, dx_ww=dx)
        return tags_img(kz=val, ww=other_state, chip_kz=chip, fl_kz=fl, dx_kz=dx)
    return f


def make_tags(out):
    # static states, drop them under the whole video and swap at each hit
    tags_img().save(os.path.join(out, "Tags 1 - Full.png"))
    tags_img(kz=0.65).save(os.path.join(out, "Tags 2 - KingZ 65.png"))
    tags_img(kz=0.65, ww=0.65).save(os.path.join(out, "Tags 3 - Both 65.png"))
    print("wrote tag state PNGs")
    render(lambda i: tags_img(drop=int(60 * (1 - ease_out(i / 10)))), 30, os.path.join(out, "Tags Intro.mov"),
           [(BLEEP, 0, 0.5)])
    render(hit_frames("kz", 1.0, 0.65, 1.0), 36, os.path.join(out, "Hit - KingZ (12-27).mov"), [(PUNCH, 133, 0.55)])
    render(hit_frames("ww", 1.0, 0.65, 0.65), 36, os.path.join(out, "Hit - Winter Wolf (15-17).mov"), [(PUNCH, 133, 0.55)])

    def banger(i):
        g = 0.5 + 0.5 * np.sin(i / 36 * np.pi * 4)
        return tags_img(fl_kz=g * 0.8, fl_ww=g * 0.8, glow=True)
    render(banger, 36, os.path.join(out, "Both Full Flash (03-32).mov"), [(BLEEP, 0, 0.5)])


# ---------- V5 combo ----------
def combo_frame(n=300):
    hits = [30, 120, 210]
    def f(i):
        cv = blank()
        out_k = 1 - max(0, i - (n - 10)) / 10
        if i < hits[0]:
            return cv
        if i >= 255:
            j = i - 255
            s = 1 + 0.8 * (1 - ease_out(j / 6))
            put(cv, grad_text("NOSTALGIA", 190, "gold"), 560, 340, s, out_k)
            put(cv, grad_text("COMBO!", 150, "fire"), 560, 530, s, out_k)
            flash(cv, 110 - 40 * j if j < 3 else 0)
            return cv
        c = sum(1 for h in hits if i >= h)
        j = i - hits[c - 1]
        s = 1 + 0.6 * (1 - ease_out(j / 5))
        dx = (12 - 3 * j) * (1 if j % 2 else -1) if j < 4 else 0
        put(cv, grad_text(f"{c} HIT" if c == 1 else f"{c} HITS", 230, "gold"), 520 + dx, 330, s, out_k)
        if c >= 2:
            put(cv, grad_text("COMBO!", 120, "fire"), 520 + dx, 520, s, out_k)
        return cv
    return f


def make_combo(out):
    render(combo_frame(), 300, os.path.join(out, "Combo Counter.mov"),
           [(PUNCH, 1000, 0.9), (PUNCH, 4000, 0.9), (PUNCH, 7000, 0.9), (GONG, 8500, 1.0)])


# ---------- V8 continue card ----------
def card_bg():
    bg = Image.new("RGB", (W, H), (6, 6, 10))
    d = ImageDraw.Draw(bg)
    for y in range(0, H, 4):
        d.line([(0, y), (W, y)], fill=(16, 16, 24))
    vign = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vign).ellipse([-300, -200, W + 300, H + 200], fill=255)
    vign = vign.filter(ImageFilter.GaussianBlur(120))
    return Image.composite(bg, Image.new("RGB", (W, H), (0, 0, 0)), vign).convert("RGBA")


def continue_frame(title, sub, n=240):
    bg = card_bg()
    titl = grad_text(title.upper(), 260, "gold", 12)
    if titl.width > 1650:
        titl = titl.resize((1650, int(titl.height * 1650 / titl.width)), Image.LANCZOS)
    def f(i):
        cv = bg.copy()
        if i < 135:
            put(cv, grad_text("CONTINUE?", 140, "gold"), 960, 150)
            d = 9 - i // 27
            j = i % 27
            s = 1 + 0.35 * (1 - ease_out(j / 5))
            put(cv, grad_text(str(d), 560, "fire", 14), 960, 560, s)
            if (i // 8) % 2 == 0:
                put(cv, grad_text("INSERT COIN", 72, "white", 6), 960, 960)
        else:
            j = i - 135
            put(cv, grad_text("CONTINUE!", 140, "gold"), 960, 120)
            put(cv, grad_text("NEXT UP", 90, "white", 6), 960, 330)
            s = 1 + 0.5 * (1 - ease_out((j - 5) / 6)) if j >= 5 else 0.01
            dx = (14 - 3 * (j - 5)) * (1 if j % 2 else -1) if 5 <= j < 10 else 0
            put(cv, titl, 960 + dx, 590, s)
            if sub and j >= 14:
                put(cv, grad_text(sub.upper(), 84, "gold", 6), 960, 830)
            put(cv, grad_text("CREDIT 01", 56, "white", 5), 1700, 990)
            flash(cv, 110 - 40 * (j - 5) if 5 <= j < 8 else 0)
        if i >= n - 12:
            cv = Image.blend(cv, Image.new("RGBA", (W, H), (0, 0, 0, 255)), (i - (n - 12)) / 12)
        return cv
    return f


def make_continue(out, title, sub, name):
    audio = [(BLEEP, int(k * 27 / FPS * 1000), 0.5) for k in range(5)]
    audio += [(COIN, int(135 / FPS * 1000), 1.0), (PUNCH_HARD, int(140 / FPS * 1000), 1.0)]
    render(continue_frame(title, sub), 240, os.path.join(out, f"{name}.mov"), audio, alpha=False)


# ---------- V10 fireball ----------
def sprite(sz=380):
    y, x = np.mgrid[0:sz, 0:sz]
    r = np.hypot(x - sz / 2, y - sz / 2) / (sz / 2)
    core = np.clip(1 - r / 0.25, 0, 1)
    mid = np.clip(1 - r / 0.55, 0, 1)
    out = np.clip(1 - r, 0, 1) ** 1.6
    arr = np.zeros((sz, sz, 4), np.float32)
    arr[..., 0] = np.clip(40 + 215 * core, 0, 255)
    arr[..., 1] = np.clip(120 + 160 * core + 40 * mid, 0, 255)
    arr[..., 2] = 255
    arr[..., 3] = 255 * np.clip(out * 1.1 + mid * 0.5 + core, 0, 1)
    return Image.fromarray(arr.astype(np.uint8), "RGBA")


def fireball_frame(n=30):
    sp = sprite()
    def f(i):
        cv = blank()
        def pos(t):
            return -250 + 2420 * (t / 24) ** 1.5, 560 - 70 * np.sin(min(t, 24) / 24 * np.pi)
        for back in range(40, -1, -1):
            t = i - back * 0.25
            if t < 0 or t > 24:
                continue
            x, y = pos(t)
            sc = 0.95 - 0.017 * back
            put(cv, sp, x, y, sc, max(0.03, 0.55 * (1 - back / 42)) if back else 1.0)
        return cv
    return f


def make_fireball(out):
    render(fireball_frame(), 30, os.path.join(out, "Fireball.mov"), [(WHOOSH, 0, 1.0)])


# ---------- V7 watch again ----------
def watch_again_frame(n=90):
    def f(i):
        cv = blank()
        k = ease_out(i / 5)
        out_k = 1 - max(0, i - (n - 8)) / 8
        band(cv, 540 - 190 * k, 540 + 190 * k, int(205 * out_k))
        s = 1 + 0.6 * (1 - ease_out(i / 6))
        put(cv, grad_text("WATCH AGAIN?", 190, "gold"), 960, 470, s, out_k)
        yes_on = i >= 36
        for label, cx in (("YES", 760), ("NO", 1160)):
            t = grad_text(label, 100, "fire" if (label == "YES" and yes_on) else "white", 6)
            if label == "YES" and yes_on and (i // 3) % 2 == 0:
                t = grad_text(label, 100, "gold", 6)
            put(cv, t, cx, 640, 1.0, out_k)
        if i >= 8:
            cx = 760 if yes_on else (760 if (i // 12) % 2 == 0 else 1160)
            ov = blank()
            ImageDraw.Draw(ov).rectangle([cx - 130, 590, cx + 130, 690], outline=(255, 255, 255, 255), width=5)
            cv.alpha_composite(fade(ov, out_k))
        flash(cv, 100 if 36 <= i < 38 else 0)
        return cv
    return f


def make_watch_again(out):
    render(watch_again_frame(), 90, os.path.join(out, "Watch Again.mov"),
           [(BLEEP, 250, 0.4), (COIN, 1200, 1.0), (BLEEP, 1200, 0.6)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=r"P:\WWD Kit\Street Fighter")
    ap.add_argument("--only", default="round,versus,tags,combo,continue,fireball")
    ap.add_argument("--title", default="CRYSTAL LAKE")
    ap.add_argument("--sub", default="SEASON 1 REVIEW")
    ap.add_argument("--name", default=None)
    a = ap.parse_args()
    todo = a.only.split(",")
    if "round" in todo: make_rounds(a.out)
    if "versus" in todo: make_versus(a.out)
    if "tags" in todo: make_tags(a.out)
    if "combo" in todo: make_combo(a.out)
    if "continue" in todo:
        make_continue(a.out, a.title, a.sub, a.name or f"Continue - {a.title.title()}")
    if "fireball" in todo: make_fireball(a.out)
    if "watch" in todo: make_watch_again(a.out)


if __name__ == "__main__":
    main()
