"""Crystal Lake opening, Option 1 (fully built, no AI video): night lake, girl in a canoe,
the show poster erupts from the water and drags her under. 19.0 s, 1920x1080, 30 fps.
Owned sounds only, no music bed.

  python make_cl_opening.py --stills 2,8,12.4,13.6,14.4,15.2,18      (preview frames only)
  python make_cl_opening.py                                          (full render)
"""
import argparse, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

W, H, FPS, DUR = 1920, 1080, 30, 19.0
HORIZON = 560
WATERLINE = 800            # poster and girl are hidden below this y (they come out of / sink into the water)
CANOE = (700, 735)         # canoe centre
POSTER_SRC = r"L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\Crystal Lake\USE\1.png"
OUT = r"P:\WWD Kit\Crystal Lake\Opening - Lake Scare (Option 1).mov"
SFX = r"P:\Sounds\Sound FX"
ADOBE = SFX + r"\Adobe\Ambience_2"

# event times
T_ERUPT, T_GRAB, T_SINK = 12.2, 13.4, 14.95


def ease(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def lerp(a, b, x):
    return a + (b - a) * x


# ---------- static layers ----------
def build_static():
    rng = random.Random(13)
    sky = np.zeros((HORIZON, W, 3), np.float32)
    top, bot = np.array([4, 7, 17]), np.array([24, 42, 56])
    for y in range(HORIZON):
        k = (y / HORIZON) ** 1.6
        sky[y] = top + (bot - top) * k
    water = np.zeros((H - HORIZON, W, 3), np.float32)
    wt, wb = np.array([26, 44, 58]), np.array([5, 10, 16])
    for y in range(H - HORIZON):
        k = (y / (H - HORIZON)) ** 0.7
        water[y] = wt + (wb - wt) * k
    img = Image.fromarray(np.vstack([sky, water]).astype(np.uint8), "RGB")
    # moon with glow
    glow = Image.new("RGB", (W, H), (0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse((1380 - 260, 210 - 260, 1380 + 260, 210 + 260), fill=(40, 60, 80))
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    img = Image.fromarray(np.clip(np.asarray(img, np.int16) + np.asarray(glow, np.int16), 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(img)
    d.ellipse((1380 - 70, 210 - 70, 1380 + 70, 210 + 70), fill=(214, 226, 232))
    d.ellipse((1380 - 70, 210 - 70, 1380 + 70, 210 + 70), outline=(240, 246, 250), width=2)
    for cx, cy, r in ((1352, 190, 14), (1405, 232, 10), (1378, 160, 7)):
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(190, 204, 212))
    # tree line, two depths
    for base, col, hmin, hmax, step in ((HORIZON + 4, (7, 11, 15), 40, 110, 22), (HORIZON + 6, (2, 3, 5), 70, 190, 34)):
        x = -20
        while x < W + 40:
            h = rng.randint(hmin, hmax)
            wd = step + rng.randint(-6, 10)
            d.polygon([(x, base), (x + wd / 2, base - h), (x + wd, base)], fill=col)
            x += wd * 0.62
        d.rectangle((0, base - 4, W, base + 6), fill=col)
    # near shore reeds, lower left and right
    for sx in (list(range(0, 260, 14)) + list(range(1700, 1920, 14))):
        h = rng.randint(70, 200)
        d.line((sx, H, sx + rng.randint(-14, 14), H - h), fill=(2, 3, 4), width=5)
    return img


def build_mist():
    rng = np.random.default_rng(5)
    small = rng.random((14, 40)).astype(np.float32)
    m = Image.fromarray((small * 255).astype(np.uint8)).resize((W * 2, 300), Image.BICUBIC).filter(ImageFilter.GaussianBlur(24))
    a = np.asarray(m, np.float32) / 255.0
    a = np.clip((a - 0.35) * 1.8, 0, 1)
    band = np.ones((300, 1), np.float32)
    ramp = np.sin(np.linspace(0, math.pi, 300))[:, None] ** 1.3
    return (a * ramp * 95).astype(np.uint8)  # alpha 0..95


def build_vignette():
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    return np.clip(1.08 - 0.42 * r ** 1.8, 0.35, 1.0)[..., None]


# ---------- sprites ----------
INK, RIM = (3, 4, 7, 255), (62, 84, 100, 255)


def canoe_sprite():
    s = Image.new("RGBA", (760, 260), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    ox, oy = 380, 90
    hull = [(-300, -36), (-210, -12), (0, 2), (210, -12), (300, -36), (250, 22), (120, 44), (0, 50), (-120, 44), (-250, 22)]
    d.polygon([(ox + x, oy + y) for x, y in hull], fill=INK)
    d.line([(ox + x, oy + y) for x, y in hull[:5]], fill=RIM, width=3)
    return s


def girl_sprite(head_dx=0.0, lean=0.0, arms_up=0.0):
    s = Image.new("RGBA", (360, 440), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    ox, oy = 180, 400  # hip anchor
    sh = (ox + lean * 20, oy - 190)
    # torso
    d.polygon([(ox - 46, oy), (ox + 46, oy), (sh[0] + 40, sh[1] + 12), (sh[0] - 40, sh[1] + 12)], fill=INK)
    d.ellipse((sh[0] - 46, sh[1] - 4, sh[0] + 46, sh[1] + 40), fill=INK)
    # neck and head
    hx, hy = sh[0] + head_dx + lean * 6, sh[1] - 40
    d.rectangle((sh[0] - 9 + head_dx / 2, sh[1] - 30, sh[0] + 9 + head_dx / 2, sh[1] + 6), fill=INK)
    d.ellipse((hx - 30, hy - 32, hx + 30, hy + 34), fill=INK)
    d.ellipse((hx - 30, hy - 32, hx + 30, hy + 34), outline=RIM, width=2)
    # ponytail swings opposite the head turn
    px = hx - 26 - head_dx * 0.6
    d.polygon([(hx - 14, hy - 22), (px - 18, hy + 18), (px - 34, hy + 94 + arms_up * 20), (px + 4, hy + 62), (hx - 6, hy + 8)], fill=INK)
    # arms
    if arms_up > 0.01:
        a = arms_up
        d.line([(sh[0] - 36, sh[1] + 20), (sh[0] - 70 - 30 * a, sh[1] - 40 - 110 * a)], fill=INK, width=20)
        d.line([(sh[0] + 36, sh[1] + 20), (sh[0] + 78 + 30 * a, sh[1] - 30 - 120 * a)], fill=INK, width=20)
        d.ellipse((sh[0] - 90 - 30 * a, sh[1] - 66 - 110 * a, sh[0] - 54 - 30 * a, sh[1] - 28 - 110 * a), fill=INK)
        d.ellipse((sh[0] + 62 + 30 * a, sh[1] - 58 - 120 * a, sh[0] + 98 + 30 * a, sh[1] - 20 - 120 * a), fill=INK)
    else:
        d.line([(sh[0] - 36, sh[1] + 22), (sh[0] - 70, sh[1] + 90)], fill=INK, width=20)
        d.line([(sh[0] + 36, sh[1] + 22), (sh[0] + 120, sh[1] + 70)], fill=INK, width=20)
    return s


def paddle_sprite():
    s = Image.new("RGBA", (560, 120), (0, 0, 0, 0))
    d = ImageDraw.Draw(s)
    d.line((30, 30, 440, 96), fill=INK, width=8)
    d.polygon([(430, 80), (520, 96), (500, 118), (420, 104)], fill=INK)
    return s


def load_poster():
    im = Image.open(POSTER_SRC).convert("RGBA")
    return im.crop(im.getchannel("A").getbbox())


def place(canvas, sprite, cx, cy, rot=0.0, scale=1.0, cut_y=None):
    sp = sprite
    if scale != 1.0:
        sp = sp.resize((max(1, int(sp.width * scale)), max(1, int(sp.height * scale))), Image.BILINEAR)
    if rot:
        sp = sp.rotate(rot, resample=Image.BILINEAR, expand=True)
    x0, y0 = int(cx - sp.width / 2), int(cy - sp.height / 2)
    if cut_y is not None:
        keep = cut_y - y0
        if keep <= 0:
            return
        if keep < sp.height:
            arr = np.array(sp)
            arr[keep:, :, 3] = 0
            sp = Image.fromarray(arr, "RGBA")
    if x0 >= W or y0 >= H or x0 + sp.width <= 0 or y0 + sp.height <= 0:
        return
    sx, sy = max(0, -x0), max(0, -y0)
    sp = sp.crop((sx, sy, min(sp.width, W - x0), min(sp.height, H - y0)))
    canvas.alpha_composite(sp, (max(0, x0), max(0, y0)))


# ---------- spray (stateless) ----------
def make_spray():
    rng = random.Random(77)
    ps = []
    for te, n, x0, spread, vmax in ((T_ERUPT, 120, 1030, 180, 1000), (T_SINK, 220, 800, 260, 1300), (T_ERUPT + 0.05, 40, 1030, 60, 1500)):
        for _ in range(n):
            ps.append((te, x0 + rng.uniform(-spread, spread), WATERLINE + rng.uniform(-6, 6),
                       rng.uniform(-380, 380), -rng.uniform(250, vmax), rng.uniform(2, 6.5)))
    return ps


SPRAY = make_spray()


def ripple_events():
    ev = []
    t = 1.4
    while t < 8.0:
        ev.append((t, CANOE[0] + random.Random(int(t * 10)).uniform(-40, 40), CANOE[1] + 62, 70, 0.30 * 200))
        t += 2.1
    t = 8.0
    while t < T_ERUPT - 0.2:
        ev.append((t, 1030, WATERLINE + 8, 120 + (t - 8) * 12, 130 + (t - 8) * 18))
        t += 0.9
    for k in range(4):
        ev.append((T_ERUPT + k * 0.16, 1030, WATERLINE + 6, 420 + k * 70, 190 - k * 25))
    for k in range(5):
        ev.append((T_SINK + k * 0.2, 800, WATERLINE + 6, 520 + k * 80, 210 - k * 20))
    t = 16.6
    while t < 18.6:
        ev.append((t, CANOE[0], CANOE[1] + 62, 120, 90))
        t += 0.8
    return ev


RIPPLES = ripple_events()


# ---------- the frame ----------
class Scene:
    def __init__(self):
        self.bg = build_static()
        self.mist = build_mist()
        self.vig = build_vignette()
        self.canoe = canoe_sprite()
        self.paddle = paddle_sprite()
        self.poster_full = load_poster()
        ph = 700
        self.poster = self.poster_full.resize((int(self.poster_full.width * ph / self.poster_full.height), ph), Image.LANCZOS)
        self.girls = {}

    def girl(self, head_dx, lean, arms_up):
        k = (round(head_dx), round(lean * 4), round(arms_up * 10))
        if k not in self.girls:
            self.girls[k] = girl_sprite(head_dx, lean, arms_up)
        return self.girls[k]

    def render(self, t):
        f = self.bg.convert("RGBA")
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        # moon reflection column
        rr = random.Random(int(t * 15))
        for i in range(70):
            y = HORIZON + 8 + i * 6.2
            hw = 6 + i * 1.5 + rr.uniform(-3, 3)
            x = 1380 + 14 * math.sin(t * 2.2 + i * 0.7)
            a = int(max(0, 150 - i * 1.7))
            od.line((x - hw, y, x + hw, y), fill=(210, 224, 232, a), width=2)
        # wave glints
        for i in range(34):
            r2 = random.Random(i * 31)
            y = HORIZON + 30 + r2.uniform(0, 420) ** 1.0
            x = (r2.uniform(0, W) + t * r2.uniform(8, 22)) % (W + 200) - 100
            od.line((x, y, x + r2.uniform(30, 90), y), fill=(120, 150, 170, 60), width=1)
        f.alpha_composite(ov)
        # back mist
        off = int(t * 14) % W
        m = Image.fromarray(self.mist[:, off:off + W], "L")
        mist_rgba = Image.new("RGBA", (W, 300), (150, 170, 185, 0))
        mist_rgba.putalpha(m)
        f.alpha_composite(mist_rgba, (0, 440))

        # canoe motion
        calm = 1.0 if t < T_GRAB - 0.3 else 0.0
        bob = 7 * math.sin(t * 1.5) + 3 * math.sin(t * 2.7)
        tilt = 2.2 * math.sin(t * 1.2)
        if t >= 8.5:
            tilt += 1.2 * math.sin(t * 5) * ease((t - 8.5) / 3)
        if T_GRAB <= t < T_SINK + 0.9:
            u = t - T_GRAB
            tilt = -16 * ease(u / 0.35) * math.exp(-u * 0.35) + 9 * math.sin(u * 14) * math.exp(-u * 0.55)
            bob = 14 * math.sin(u * 11) * math.exp(-u * 0.4)
        elif t >= T_SINK + 0.9:
            u = t - (T_SINK + 0.9)
            tilt = 11 * math.sin(u * 4.2) * math.exp(-u * 0.55)
            bob = 8 * math.sin(u * 3.4) * math.exp(-u * 0.5) + 3
        cx, cy = CANOE[0], CANOE[1] + bob
        # shadow on water
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(sh).ellipse((cx - 300, cy + 36, cx + 300, cy + 78), fill=(0, 0, 0, 120))
        f.alpha_composite(sh.filter(ImageFilter.GaussianBlur(10)))
        place(f, self.canoe, cx, cy, tilt)

        # girl, before the grab she sits in the canoe
        head_dx = 0.0
        if t > 8.8:
            head_dx = -14 * ease((t - 8.8) / 1.4) + (6 * math.sin(t * 3) if t > 10 else 0)
        lean = -0.4 * ease((t - 11.0) / 1.2) if t < T_GRAB else 0
        # ripples
        ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        od = ImageDraw.Draw(ov)
        for (te, x, y, maxr, amax) in RIPPLES:
            u = t - te
            if 0 <= u < 2.6:
                r = maxr * (1 - math.exp(-u * 1.7))
                a = int(max(0, min(255, amax * (1 - u / 2.6))))
                od.ellipse((x - r, y - r * 0.2, x + r, y + r * 0.2), outline=(170, 196, 210, a), width=2)
        f.alpha_composite(ov)

        # girl sprite placement
        gx, gy, grot, gscale, garms = cx - 20, cy - 190, tilt * 0.5, 1.0, 0.0
        girl_cut = None
        # poster motion
        pshow = T_ERUPT <= t
        if pshow:
            if t < 12.95:
                u = 1 - (1 - min(1.0, (t - T_ERUPT) / 0.75)) ** 2
                px, py, prot, pscale = 1030, lerp(1250, 430, u), -6, 1.0
            elif t < T_SINK:
                u = ease((t - 12.95) / 0.9)
                px = lerp(1030, 880, u) + (6 * math.sin(t * 40) if t > T_GRAB else 0)
                py = lerp(430, 440, u)
                prot = lerp(-6, 7, u) + (2 * math.sin(t * 33) if t > T_GRAB else 0)
                pscale = lerp(1.0, 1.15, u)
            else:
                u = ease((t - T_SINK) / 0.7)
                px, py, prot, pscale = 880, lerp(440, 1500, u), 7, 1.15
            # foam at the waterline
            if t < 16.0:
                foam = Image.new("RGBA", (W, H), (0, 0, 0, 0))
                fw = 180 * pscale
                fa = int(200 * max(0, 1 - max(0, (t - T_ERUPT)) / 3.2)) if t < T_SINK else int(220 * max(0, 1 - (t - T_SINK) / 1.0))
                ImageDraw.Draw(foam).ellipse((px - fw, WATERLINE - 12, px + fw, WATERLINE + 16), fill=(205, 222, 232, fa))
                f.alpha_composite(foam.filter(ImageFilter.GaussianBlur(6)))
            place(f, self.poster, px, py, prot, pscale, cut_y=WATERLINE)
            # girl is yanked toward the poster
            if t >= T_GRAB:
                k = ease((t - T_GRAB) / 0.55)
                gx = lerp(gx, px - 190, k)
                gy = lerp(gy, py - 30, k)
                grot = lerp(grot, -28, k) + 8 * math.sin(t * 22) * k
                garms = k
                gscale = lerp(1.0, 1.15, k)
                girl_cut = WATERLINE
        if t < T_GRAB:
            place(f, self.paddle, cx + 30, cy - 66, tilt * 0.8)
        place(f, self.girl(head_dx, lean, garms), gx, gy - 90 * (gscale - 1), grot, gscale, cut_y=girl_cut)

        # spray
        sp = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sp)
        for (te, x0, y0, vx, vy, sz) in SPRAY:
            u = t - te
            if 0 <= u < 1.1:
                x = x0 + vx * u
                y = y0 + vy * u + 0.5 * 1700 * u * u
                if y < WATERLINE + 10:
                    a = int(230 * (1 - u / 1.1))
                    sd.ellipse((x - sz, y - sz * 1.3, x + sz, y + sz * 1.3), fill=(205, 224, 236, a))
        f.alpha_composite(sp)
        # front mist, thinner, over the water line
        front = Image.new("RGBA", (W, 300), (150, 170, 185, 0))
        front.putalpha(Image.fromarray((np.asarray(m, np.float32) * 0.45).astype(np.uint8), "L"))
        f.alpha_composite(front, (0, 660))

        # camera: slow push in, shake on impacts
        z = 1.0 + 0.06 * (t / DUR)
        shake = 0.0
        for te in (T_ERUPT, T_GRAB, T_SINK):
            u = t - te
            if 0 <= u < 0.6:
                shake = max(shake, 16 * math.exp(-u * 7))
        sx = random.Random(int(t * 60) + 1).uniform(-1, 1) * shake
        sy = random.Random(int(t * 60) + 2).uniform(-1, 1) * shake
        bw, bh = W / z, H / z
        x0 = (W - bw) / 2 + sx
        y0 = (H - bh) / 2 + sy - 14 * (t / DUR)
        fr = f.convert("RGB").resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + bw, y0 + bh))
        a = np.asarray(fr, np.float32) * self.vig
        # flash and fades
        fl = 0.0
        for te in (T_ERUPT, T_SINK):
            u = t - te
            if 0 <= u < 0.12:
                fl = max(fl, 0.5 * (1 - u / 0.12))
        a = a * (1 - fl) + 255 * fl
        fade = min(1.0, t / 1.0) * min(1.0, max(0.0, (DUR - t) / 0.5))
        a = a * fade
        return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGB")


def audio_args():
    ins = [
        (ADOBE + r"\Ambience Nature Near Water 01.wav", 0, 0.38, 19.0),
        (ADOBE + r"\Ambience Night Crickets And A Bullfrog 01.wav", 0, 0.16, 19.0),
        (SFX + r"\nightmare-passing_G14eXH4u.mp3", 7.6, 0.45, 6.0),
        (SFX + r"\jump-into-water-splashes_MyjdEHNd.mp3", T_ERUPT - 0.05, 1.0, 3.0),
        (SFX + r"\jg-032316-sfx-frightening-cymbal-stab-1.mp3", T_ERUPT, 0.75, 4.0),
        (SFX + r"\scary-girl-screams-very-loud_zy9HEB4d.mp3", T_GRAB - 0.1, 0.8, T_SINK - T_GRAB + 0.1),
        (SFX + r"\hit-thud-dark_GkAfpDV_.mp3", T_SINK - 0.02, 1.0, 3.0),
        (SFX + r"\jump-into-water-splashes_MyjdEHNd.mp3", T_SINK, 1.0, 3.0),
    ]
    args, chains, labels = [], [], []
    for i, (p, delay, vol, dur) in enumerate(ins, start=1):
        args += ["-i", p]
        ms = int(delay * 1000)
        fx = f"[{i}:a]atrim=0:{dur},asetpts=PTS-STARTPTS"
        if i == 1:
            fx += ",afade=t=in:d=1.2"
        if i == 6:
            fx += ",afade=t=out:st=%.2f:d=0.12" % max(0.1, dur - 0.14)
        fx += f",volume={vol},adelay={ms}|{ms}[a{i}]"
        chains.append(fx)
        labels.append(f"[a{i}]")
    mix = "".join(labels) + f"amix=inputs={len(ins)}:normalize=0,alimiter=limit=0.95,atrim=0:{DUR},afade=t=out:st={DUR-0.5}:d=0.5[aout]"
    return args, ";".join(chains + [mix])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stills", default="")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    sc = Scene()
    if a.stills:
        d = r"D:\WKP\scratch\cl_opening"
        os.makedirs(d, exist_ok=True)
        for s in a.stills.split(","):
            t = float(s)
            sc.render(t).save(os.path.join(d, f"t{t:05.2f}.png"))
            print("wrote", t)
        return
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    aargs, filt = audio_args()
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + aargs + \
          ["-filter_complex", filt, "-map", "0:v", "-map", "[aout]", "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
           "-c:a", "pcm_s16le", "-t", str(DUR), a.out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(DUR * FPS)
    for i in range(n):
        p.stdin.write(sc.render(i / FPS).tobytes())
        if i % 60 == 0:
            print(f"frame {i}/{n}", flush=True)
    p.stdin.close()
    p.wait()
    print("done", a.out, "rc", p.returncode)


if __name__ == "__main__":
    main()
