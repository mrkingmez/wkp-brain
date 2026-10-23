"""Crystal Lake opening, Option 2: five Firefly plates plus the real poster composited on top.
19.0 s, 1920x1080, 30 fps. Owned sounds only, no music bed.

Timeline (s): plate1 0-5, plate2 5-8.5, plate3 8.5-12 (burst at 9.0), poster erupts 9.15,
lunges over the girl 9.95-10.55, held and shaking to 12.0, hard cut + flash + splash,
plate4 12-15.5 (empty canoe thrashing), plate5 15.5-19 (settles).

  python make_cl_opening_firefly.py --stills 9.5,10.3,11.5
  python make_cl_opening_firefly.py
"""
import argparse, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_cl_opening import load_poster, place, ease, lerp, build_mist, SFX, ADOBE  # noqa: E402

W, H, FPS, DUR = 1920, 1080, 30, 19.0
PLATES = r"L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest\Crystal Lake\opening pates"
OUT = r"P:\WWD Kit\Crystal Lake\Opening - Lake Scare (Option 2 Firefly).mov"

# (file, trim start, trim end) in plate seconds, played back to back
SEGS = [("plate 1.mp4", 0.0, 5.0), ("plate 2.mp4", 0.5, 4.0), ("PLATE 3.mp4", 0.5, 4.0),
        ("PLATE 4.mp4", 0.3, 3.8), ("PLATE 5.mp4", 0.4, 4.0)]

T_BURST, T_RISE, T_LUNGE, T_GRAB, T_CUT = 9.0, 9.15, 9.95, 10.55, 12.0
WL = 665          # waterline for the poster, below the canoe so the poster reads as in front of it
PH = 520          # poster height in px


MIST = build_mist()                    # alpha 0..95, 300 x 2W
LIVE = [(0.0, 5.0, 0.22, 1.0), (15.5, 19.0, 0.10, 0.35)]   # plates that barely move in the Firefly clip: (start, end, zoom, rock amount)
WATER_Y0, WATER_Y1 = 500, 880


def live_plate(base, t):
    """Adds motion to a near-still plate: rippling water, drifting mist, slow push-in on the canoe."""
    seg = next(((a, b, z, r) for a, b, z, r in LIVE if a <= t < b), None)
    if not seg:
        return base
    a, b, zmax, rock = seg
    u = (t - a) / (b - a)
    arr = np.asarray(base).astype(np.float32)
    ys = np.arange(WATER_Y0, WATER_Y1)
    k = (ys - WATER_Y0) / float(WATER_Y1 - WATER_Y0)
    dx = (2.5 + 7.0 * k) * np.sin(ys * 0.085 - t * 2.6) + (1.2 + 3.0 * k) * np.sin(ys * 0.21 + t * 3.6)
    xs = np.clip(np.arange(W)[None, :] + dx[:, None], 0, W - 1)
    x0 = np.floor(xs).astype(np.int32)
    x1 = np.minimum(x0 + 1, W - 1)
    fr = (xs - x0)[..., None]
    rows = arr[WATER_Y0:WATER_Y1]
    ri = np.arange(rows.shape[0])[:, None]
    arr[WATER_Y0:WATER_Y1] = rows[ri, x0] * (1 - fr) + rows[ri, x1] * fr
    off = int(t * 26) % W
    m = MIST[:, off:off + W].astype(np.float32)[..., None] / 255.0 * 1.15
    y0 = 470
    arr[y0:y0 + 300] = arr[y0:y0 + 300] * (1 - m) + np.array([150, 170, 185], np.float32) * m
    img = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8), "RGB")
    # canoe, girl and reflection rock and bob together, feathered into the water around them
    bx0, by0, bx1, by1 = 560, 470, 1440, 720
    box = img.crop((bx0, by0, bx1, by1))
    ang = rock * (1.6 * math.sin(t * 1.9) + 0.6 * math.sin(t * 3.1 + 1.0))
    dyb = rock * (6 * math.sin(t * 1.5 + 0.8) + 2 * math.sin(t * 2.9))
    box = box.rotate(ang, resample=Image.BILINEAR, translate=(0, dyb))
    mk = Image.new("L", box.size, 0)
    ImageDraw.Draw(mk).rectangle((70, 50, box.width - 70, box.height - 50), fill=255)
    img.paste(box, (bx0, by0), mk.filter(ImageFilter.GaussianBlur(40)))
    z = 1.0 + zmax * u   # linear, so it never eases to a stop
    fx, fy = 930, 600
    bw, bh = W / z, H / z
    l, tp = fx * (1 - 1 / z), fy * (1 - 1 / z)
    return img.resize((W, H), Image.BILINEAR, box=(l, tp, l + bw, tp + bh))


def poster_state(t):
    """x, y centre, rotation, scale, or None when hidden."""
    if t < T_RISE or t >= T_CUT:
        return None
    if t < T_LUNGE:
        u = ease((t - T_RISE) / (T_LUNGE - T_RISE))
        return 1090, lerp(WL + PH / 2 + 20, WL - PH / 2 - 10, u), -5, 1.0
    if t < T_GRAB:
        u = ease((t - T_LUNGE) / (T_GRAB - T_LUNGE))
        return lerp(1090, 975, u), lerp(WL - PH / 2 - 10, WL - PH / 2 - 16, u), lerp(-5, 6, u), lerp(1.0, 1.14, u)
    k = t - T_GRAB
    return 975 + 7 * math.sin(k * 41), WL - PH / 2 - 16 + 4 * math.sin(k * 29), 6 + 2.2 * math.sin(k * 33), 1.14


def shake(t):
    if T_BURST <= t < T_CUT:
        a = 3 + 9 * (1 if t >= T_GRAB else 0.5)
        fade = min(1.0, (t - T_BURST) / 0.2) * (1 if t < T_CUT - 0.2 else 0.6)
        return a * fade * math.sin(t * 61), a * fade * 0.7 * math.sin(t * 47 + 1.3)
    return 0.0, 0.0


def make_frame(base, t, poster, foam_cache):
    f = live_plate(base, t).convert("RGBA")
    ps = poster_state(t)
    if ps:
        px, py, prot, pscale = ps
        # foam at the waterline
        fa = int(210 * max(0.0, 1 - (t - T_RISE) / 2.2))
        if fa > 0:
            fo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            fw = 190 * pscale
            ImageDraw.Draw(fo).ellipse((px - fw, WL - 12, px + fw, WL + 18), fill=(205, 222, 232, fa))
            f.alpha_composite(fo.filter(ImageFilter.GaussianBlur(7)))
        place(f, poster, px, py, prot, pscale, cut_y=WL)
    dx, dy = shake(t)
    if dx or dy:
        z = 1.025
        big = f.resize((int(W * z), int(H * z)), Image.BILINEAR)
        x0 = int((big.width - W) / 2 + dx)
        y0 = int((big.height - H) / 2 + dy)
        f = big.crop((x0, y0, x0 + W, y0 + H))
    a = np.asarray(f.convert("RGB")).astype(np.float32)
    fl = 0.0
    for te, peak, dur in ((T_BURST + 0.12, 0.35, 0.12), (T_CUT, 0.6, 0.14)):
        u = t - te
        if 0 <= u < dur:
            fl = max(fl, peak * (1 - u / dur))
    a = a * (1 - fl) + 255 * fl
    fade = min(1.0, t / 1.0) * min(1.0, max(0.0, (DUR - t) / 0.5))
    return Image.fromarray(np.clip(a * fade, 0, 255).astype(np.uint8), "RGB")


def audio_args():
    ins = [
        (ADOBE + r"\Ambience Nature Near Water 01.wav", 0, 0.38, DUR),
        (ADOBE + r"\Ambience Night Crickets And A Bullfrog 01.wav", 0, 0.16, DUR),
        (SFX + r"\nightmare-passing_G14eXH4u.mp3", 5.2, 0.45, 4.0),
        (SFX + r"\jump-into-water-splashes_MyjdEHNd.mp3", T_BURST - 0.05, 1.0, 3.0),
        (SFX + r"\jg-032316-sfx-frightening-cymbal-stab-1.mp3", T_BURST + 0.15, 0.75, 4.0),
        (SFX + r"\scary-girl-screams-very-loud_zy9HEB4d.mp3", T_GRAB - 0.1, 0.8, T_CUT - T_GRAB + 0.1),
        (SFX + r"\hit-thud-dark_GkAfpDV_.mp3", T_CUT - 0.02, 1.0, 3.0),
        (SFX + r"\jump-into-water-splashes_MyjdEHNd.mp3", T_CUT, 1.0, 3.0),
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


def base_reader():
    ins, parts, labs = [], [], []
    for i, (fn, a, b) in enumerate(SEGS):
        ins += ["-i", os.path.join(PLATES, fn)]
        parts.append(f"[{i}:v]trim={a}:{b},setpts=PTS-STARTPTS,fps={FPS},scale={W}:{H},setsar=1[v{i}]")
        labs.append(f"[v{i}]")
    filt = ";".join(parts) + ";" + "".join(labs) + f"concat=n={len(SEGS)}:v=1:a=0[out]"
    cmd = ["ffmpeg", "-loglevel", "error"] + ins + ["-filter_complex", filt, "-map", "[out]",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    return subprocess.Popen(cmd, stdout=subprocess.PIPE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stills", default="")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    poster = load_poster()
    ph = poster.height
    poster = poster.resize((int(poster.width * PH / ph), PH), Image.LANCZOS)
    n = int(DUR * FPS)
    rd = base_reader()
    want = {int(round(float(s) * FPS)): float(s) for s in a.stills.split(",")} if a.stills else {}
    frames = {}
    enc = None
    if not want:
        os.makedirs(os.path.dirname(a.out), exist_ok=True)
        aargs, filt = audio_args()
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-"] + aargs + \
              ["-filter_complex", filt, "-map", "0:v", "-map", "[aout]", "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
               "-c:a", "pcm_s16le", "-t", str(DUR), a.out]
        enc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    size = W * H * 3
    d = r"D:\WKP\scratch\cl_opening_fx"
    os.makedirs(d, exist_ok=True)
    for i in range(n):
        raw = rd.stdout.read(size)
        if len(raw) < size:
            print("base ran short at frame", i)
            break
        t = i / FPS
        if want and i not in want:
            continue
        base = Image.frombuffer("RGB", (W, H), raw, "raw", "RGB", 0, 1)
        fr = make_frame(base, t, poster, frames)
        if want:
            fr.save(os.path.join(d, f"t{t:05.2f}.png"))
            print("wrote", t)
        else:
            enc.stdin.write(fr.tobytes())
            if i % 60 == 0:
                print(f"frame {i}/{n}", flush=True)
    rd.stdout.close()
    rd.terminate()
    if enc:
        enc.stdin.close()
        enc.wait()
        print("done", a.out, "rc", enc.returncode)


if __name__ == "__main__":
    main()
