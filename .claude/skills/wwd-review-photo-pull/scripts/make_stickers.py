"""Render the WWD reusable sticker kit as drop-in clips.

Each sticker is a 1920x1080 ProRes 4444 .mov with alpha and its sound baked in,
plus a still PNG. Drop the .mov on the top video track; no keyframing needed.

  python make_stickers.py --out "P:\\WWD Kit\\Stickers"
"""
import argparse, math, os, shutil, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

W, H, FPS = 1920, 1080, 30
FONT = r"C:\Windows\Fonts\impact.ttf"
SERIF_B = r"C:\Windows\Fonts\georgiab.ttf"
AWARD = r"L:\Winter Wolfs Den review show\Frost-Cast\Award Show stuff"
TROPHY = os.path.join(AWARD, "a0abcc10-5a63-43d0-bc40-e2cd18ce48a1_0.png")  # front view (Zac 2026-10-17)
FANFARE = os.path.join(AWARD, "204015041-fanfare-winners.wav")
THUD = r"P:\Sounds\Sound FX\Adobe\Foley\Foley Table Fist Hits Wood Table 01.wav"
FIRE = r"P:\Sounds\Sound FX\Adobe\Production Elements\Production Element Title Transition Whoosh Fire 01.wav"

STAMPS = {
    "Recommend Watch": (["RECOMMEND", "WATCH"], (24, 140, 62)),
    "Save Yourself the Time": (["SAVE YOURSELF", "THE TIME"], (232, 112, 12)),
    "Dumpster Fire": (["DUMPSTER", "FIRE"], (206, 20, 30)),
}
STAMP_CENTER = (1560, 250)  # upper right, clear of faces


def ease_out(t):
    return 1 - (1 - t) ** 3


def stamp_art(lines, color, seed):
    """Flat stamp with double border and worn ink, on transparent."""
    rng = np.random.default_rng(seed)
    pad, gap = 46, 14
    sizes = [110 if len(l) <= 9 else 84 for l in lines]
    fonts = [ImageFont.truetype(FONT, s) for s in sizes]
    tmp = ImageDraw.Draw(Image.new("L", (10, 10)))
    boxes = [tmp.textbbox((0, 0), l, font=f) for l, f in zip(lines, fonts)]
    tw = max(b[2] - b[0] for b in boxes)
    th = sum(b[3] - b[1] for b in boxes) + gap * (len(lines) - 1)
    w, h = tw + pad * 2, th + pad * 2
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([4, 4, w - 5, h - 5], radius=26, outline=255, width=11)
    d.rounded_rectangle([22, 22, w - 23, h - 23], radius=16, outline=255, width=4)
    y = pad
    for l, f, b in zip(lines, fonts, boxes):
        lw = b[2] - b[0]
        d.text(((w - lw) // 2 - b[0], y - b[1]), l, font=f, fill=255)
        y += (b[3] - b[1]) + gap
    # worn ink: speckle holes + soft blotches
    a = np.asarray(m).astype(float) / 255
    noise = rng.random((h, w))
    blot = np.asarray(Image.fromarray((rng.random((h // 12 + 1, w // 12 + 1)) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)).astype(float) / 255
    a *= (noise > 0.05).astype(float)
    a *= np.clip(0.80 + blot * 0.35, 0, 1)
    a = np.clip(a * 0.97, 0, 1)
    alpha = Image.fromarray((a * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.6))
    ink = Image.new("RGBA", (w, h), color + (255,))
    ink.putalpha(alpha)
    # soft dark edge so the stamp reads on busy backgrounds
    sh = Image.new("RGBA", (w + 24, h + 24), (0, 0, 0, 0))
    blk = Image.new("RGBA", (w, h), (0, 0, 0, 255))
    blk.putalpha(alpha.filter(ImageFilter.MaxFilter(5)).point(lambda v: int(v * 0.75)))
    sh.alpha_composite(blk, (14, 16))
    sh = sh.filter(ImageFilter.GaussianBlur(5))
    sh.alpha_composite(ink, (12, 12))
    return sh.rotate(-8, resample=Image.BICUBIC, expand=True)


def stamp_frames(art, n):
    frames = []
    hit = 6  # frame the stamp lands
    for i in range(n):
        f = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        if i < hit:
            t = ease_out(i / hit)
            s = 2.4 - 1.4 * t
            op = 0.25 + 0.75 * t
            blur = 6 * (1 - t)
        elif i < hit + 4:
            s = [0.93, 0.97, 1.01, 1.0][i - hit]
            op, blur = 1.0, 0
        else:
            s, op, blur = 1.0, 1.0, 0
        fade = n - 9
        if i >= fade:
            op *= 1 - (i - fade) / 9
        a = art.resize((max(1, int(art.width * s)), max(1, int(art.height * s))), Image.BICUBIC)
        if blur:
            a = a.filter(ImageFilter.GaussianBlur(blur))
        if op < 1:
            a.putalpha(a.getchannel("A").point(lambda v: int(v * op)))
        dx = dy = 0
        if hit <= i < hit + 5:  # small shake on impact
            k = (hit + 5 - i) * 2
            dx, dy = (k if i % 2 else -k), (-k // 2 if i % 2 else k // 2)
        cx, cy = STAMP_CENTER
        f.alpha_composite(a, (cx - a.width // 2 + dx, cy - a.height // 2 + dy))
        frames.append(f)
    return frames, hit


def trophy_cutout():
    """Remove the gray studio background: flood from the border through low-saturation pixels."""
    from scipy import ndimage
    im = Image.open(TROPHY).convert("RGBA")
    rgb = np.asarray(im)[..., :3].astype(float) / 255
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    def mask(sat_lim, dark_lim):
        bgish = (sat < sat_lim) & (mx > dark_lim)
        lab, _ = ndimage.label(bgish)
        edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
        return ~np.isin(lab, edge[edge > 0])
    h = rgb.shape[0]
    rows = np.arange(h)[:, None]
    tight = mask(0.34, 0.13)  # crystal figure, no gray glow
    loose = mask(0.22, 0.16)  # keeps the black base and its plaque
    keep = tight | (loose & (rows > 0.725 * h) & (rows < 0.93 * h))
    keep = ndimage.binary_opening(keep, iterations=2)
    lab2, n = ndimage.label(keep)
    if n > 1:
        sizes = ndimage.sum(keep, lab2, range(1, n + 1))
        keep = lab2 == (np.argmax(sizes) + 1)
    a = Image.fromarray((keep * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.5))
    im.putalpha(a)
    return im.crop(im.getbbox())

def gold_text(text, size):
    f = ImageFont.truetype(SERIF_B, size)
    b = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), text, font=f)
    w, h = b[2] - b[0] + 8, b[3] - b[1] + 8
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).text((4 - b[0], 4 - b[1]), text, font=f, fill=255)
    g = np.linspace(0, 1, h)[:, None, None]
    top, mid, bot = np.array([255, 245, 190]), np.array([240, 190, 70]), np.array([200, 140, 40])
    col = np.where(g < 0.5, top + (mid - top) * (g / 0.5), mid + (bot - mid) * ((g - 0.5) / 0.5))
    col = np.broadcast_to(col, (h, w, 3)).astype(np.uint8)
    t = Image.fromarray(col, "RGB").convert("RGBA")
    t.putalpha(m)
    return t


def nominee_art():
    """Trophy over a soft gold halo with WOLFIE AWARD / NOMINEE beneath."""
    tro = trophy_cutout()
    tro = tro.resize((int(tro.width * 430 / tro.height), 430), Image.LANCZOS)
    t1, t2 = gold_text("WOLFIE AWARD", 78), gold_text("N O M I N E E", 50)
    w = max(tro.width, t1.width, t2.width) + 80
    h = tro.height + t1.height + t2.height + 70
    art = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    halo = Image.new("L", (w, h), 0)
    ImageDraw.Draw(halo).ellipse([w * 0.25, 40, w * 0.75, tro.height - 20], fill=90)
    halo = halo.filter(ImageFilter.GaussianBlur(40))
    glow = Image.new("RGBA", (w, h), (120, 200, 255, 255))
    glow.putalpha(halo)
    art.alpha_composite(glow)
    plate = Image.new("L", (w, h), 0)
    ImageDraw.Draw(plate).rounded_rectangle([12, tro.height + 6, w - 12, h - 4], radius=18, fill=175)
    plate = plate.filter(ImageFilter.GaussianBlur(10))
    pl = Image.new("RGBA", (w, h), (8, 10, 18, 255)); pl.putalpha(plate)
    art.alpha_composite(pl)
    art.alpha_composite(tro, ((w - tro.width) // 2, 10))
    y = tro.height + 24
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for t, yy in ((t1, y), (t2, y + t1.height + 10)):
        s = Image.new("RGBA", t.size, (0, 0, 0, 200))
        s.putalpha(t.getchannel("A").point(lambda v: int(v * 0.8)))
        shadow.alpha_composite(s, ((w - t.width) // 2 + 3, yy + 4))
    shadow = shadow.filter(ImageFilter.GaussianBlur(4))
    art.alpha_composite(shadow)
    line_y = y + t1.height + 3
    d = ImageDraw.Draw(art)
    d.line([(w * 0.18, line_y), (w * 0.82, line_y)], fill=(222, 175, 70, 230), width=2)
    art.alpha_composite(t1, ((w - t1.width) // 2, y))
    art.alpha_composite(t2, ((w - t2.width) // 2, y + t1.height + 10))
    return art, (y, y + t1.height + t2.height + 12)


def nominee_frames(n):
    art, (ty0, ty1) = nominee_art()
    cx, cy = 1530, 385
    start = 18  # lands with the fanfare swell
    frames = []
    for i in range(n):
        f = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        if i >= start:
            t = min(1, (i - start) / 18)
            e = ease_out(t)
            s = 0.82 + 0.18 * e
            op = e
            fade = n - 15
            if i >= fade:
                op *= 1 - (i - fade) / 15
            a = art.resize((int(art.width * s), int(art.height * s)), Image.LANCZOS)
            # light sweep across the text after it settles
            sw = (i - start - 22) / 20
            if 0 <= sw <= 1:
                band = Image.new("L", a.size, 0)
                x = int(-120 + sw * (a.width + 240))
                ImageDraw.Draw(band).polygon([(x, 0), (x + 70, 0), (x - 50, a.height), (x - 120, a.height)], fill=170)
                band = band.filter(ImageFilter.GaussianBlur(14))
                band = ImageChops.multiply(band, a.getchannel("A"))
                shine = Image.new("RGBA", a.size, (255, 250, 225, 255))
                shine.putalpha(band)
                a = a.copy()
                a.alpha_composite(shine)
            if op < 1:
                a.putalpha(a.getchannel("A").point(lambda v: int(v * op)))
            f.alpha_composite(a, (cx - a.width // 2, cy - a.height // 2 + int(30 * (1 - e))))
        frames.append(f)
    return frames, art


def render(frames, audio_args, out_mov, tmp):
    for k, fr in enumerate(frames):
        fr.save(os.path.join(tmp, f"f{k:04d}.png"))
    dur = len(frames) / FPS
    cmd = ["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png")]
    cmd += audio_args(dur)
    cmd += ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{dur:.3f}", out_mov]
    subprocess.run(cmd, check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--only", help="render just this sticker name")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)
    for seed, (name, (lines, color)) in enumerate(STAMPS.items()):
        if args.only and args.only != name:
            continue
        art = stamp_art(lines, color, seed + 7)
        frames, hit = stamp_frames(art, 4 * FPS)
        still = Image.new("RGBA", art.size, (0, 0, 0, 0)); still.alpha_composite(art)
        still.save(os.path.join(args.out, f"{name}.png"))
        delay = int(hit / FPS * 1000)
        def audio(dur, name=name, delay=delay):
            a = ["-i", THUD]
            filt = f"[1:a]adelay={delay}|{delay},volume=1.6,apad[a1]"
            if name == "Dumpster Fire":
                a += ["-i", FIRE]
                filt = f"[1:a]adelay={delay}|{delay},volume=1.6[t];[2:a]volume=0.7[fw];[t][fw]amix=inputs=2:normalize=0,apad[a1]"
            return a + ["-filter_complex", filt, "-map", "0:v", "-map", "[a1]"]
        with tempfile.TemporaryDirectory(dir=args.out) as tmp:
            render(frames, audio, os.path.join(args.out, f"{name}.mov"), tmp)
        print("done", name)
    if args.only and args.only != "Wolfie Award Nominee":
        return
    frames, art = nominee_frames(6 * FPS)
    art.save(os.path.join(args.out, "Wolfie Award Nominee.png"))
    def faudio(dur):
        return ["-ss", "1.0", "-i", FANFARE, "-filter_complex", f"[1:a]atrim=0:{dur},afade=t=in:d=0.3,afade=t=out:st={dur-1.3}:d=1.3,volume=0.9[a1]", "-map", "0:v", "-map", "[a1]"]
    with tempfile.TemporaryDirectory(dir=args.out) as tmp:
        render(frames, faudio, os.path.join(args.out, "Wolfie Award Nominee.mov"), tmp)
    print("done Wolfie Award Nominee")


if __name__ == "__main__":
    main()
