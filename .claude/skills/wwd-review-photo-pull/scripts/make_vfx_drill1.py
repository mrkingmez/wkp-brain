r"""wwd-vfx leveling drill 1 (2026-11-22). Free build: 12 s end card + 6 s title sting. No generation, no credits.
Code only (Pillow, numpy, ffmpeg). Owned sound only: P:\Sounds\Sound FX\Adobe\Impacts. Original look (frost grid,
cyan/white/gold). No studio logo or font. 1920x1080, 30 fps, H.264 yuv420p, AAC.

  python make_vfx_drill1.py [--outdir D:\WKP\scratch\wwd-vfx-level\drill1]

Prints every text bounding box extent so the 90 percent margin (x 96..1824, y 54..1026) can be checked, and the
end-screen zone geometry so the overlap check can be re-run.
"""
import argparse, os, subprocess, sys, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1920, 1080, 30
IMPACT = r"C:\Windows\Fonts\impact.ttf"
SERIF = r"C:\Windows\Fonts\constanb.ttf"
SERIFI = r"C:\Windows\Fonts\constani.ttf"
SND = r"P:\Sounds\Sound FX\Adobe\Impacts\Impact Sword Impact On Metal Shield 01.wav"
assert os.path.exists(SND), SND
CYAN, WHITE, GOLD = (90, 225, 255), (255, 255, 255), (255, 200, 40)
SAFE = (96, 54, 1824, 1026)
TILES = [(190, 420, 830, 780), (1090, 420, 1730, 780)]     # 640x360 = 16:9
RING = (960, 600, 90)
BOXES = []                                                  # (label, bbox) of every text drawn


def f(p, s):
    return ImageFont.truetype(p, s)


def text(d, xy, s, font, fill, **kw):
    b = d.textbbox(xy, s, font=font, anchor="mm", stroke_width=kw.get("stroke_width", 0))
    BOXES.append((s, b))
    d.text(xy, s, font=font, fill=fill, anchor="mm", **kw)


def bg(i):
    yy, xx = np.mgrid[0:H, 0:W]
    v = (1 - 0.55 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2) / 2)
    base = np.zeros((H, W, 3), float)
    base[...] = (6, 16, 26)
    grid = (((xx + i) % 120 < 2) | ((yy % 120) < 2)) * 10.0       # faint frost grid, slow drift
    base += grid[..., None] * np.array([0.3, 0.8, 1.0])
    return Image.fromarray(np.clip(base * v[..., None], 0, 255).astype(np.uint8)).convert("RGBA")


def end_frame(i):
    im = bg(i)
    d = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in TILES:                          # zones visible from frame 0
        d.rectangle((x0, y0, x1, y1), fill=(6, 18, 26, 255), outline=CYAN + (255,), width=4)
    cx, cy, r = RING
    rr = int(r * (1 + 0.04 * np.sin(i * 0.22)))
    d.ellipse((cx - rr, cy - rr, cx + rr, cy + rr), outline=CYAN + (255,), width=6)
    for (x0, y0, x1, y1), lab in zip(TILES, ["LATEST UPLOAD", "BEST FOR YOU"]):
        text(d, ((x0 + x1) // 2, y0 - 50), lab, f(SERIF, 34), CYAN + (255,))
    text(d, (cx, cy + r + 42), "SUBSCRIBE", f(SERIF, 36), CYAN + (255,))
    if i >= 10:
        k = min(1.0, (i - 10) / 10)
        text(d, (960, 235), "THANKS FOR WATCHING", f(IMPACT, 104), tuple(int(v * k) for v in WHITE) + (255,),
             stroke_width=5, stroke_fill=(50, 30, 0, int(255 * k)))
    if i >= 60:
        k = min(1.0, (i - 60) / 12)
        text(d, (960, 905), "NEXT: FROSTCAST, EVERY WEDNESDAY 9 PM ET", f(SERIF, 50), tuple(int(v * k) for v in WHITE) + (255,))
    if i >= 100:
        k = min(1.0, (i - 100) / 12)
        text(d, (960, 972), "THE WINTER WOLF'S DEN", f(SERIFI, 40), tuple(int(v * k) for v in GOLD) + (255,))
    return im.convert("RGB")


def sting_frame(i):
    im = bg(i * 3)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    t = i / FPS
    sweep = int((min(t, 0.9) / 0.9) * (W + 400)) - 200       # cyan blade sweeps left to right before the hit
    if t < 1.2:
        d.polygon([(sweep, 0), (sweep + 40, 0), (sweep - 120, H), (sweep - 160, H)], fill=CYAN + (200,))
    if t >= 0.9:
        k = min(1.0, (t - 0.9) / 0.25)
        sc = 1 + 0.35 * (1 - k)
        lay = Image.new("RGBA", (W, 360), (0, 0, 0, 0))
        ld = ImageDraw.Draw(lay)
        ld.text((960, 180), "WINTER WOLF'S DEN", font=f(IMPACT, 150), anchor="mm", fill=WHITE + (int(255 * k),),
                stroke_width=6, stroke_fill=(50, 30, 0, int(255 * k)))
        lay = lay.resize((int(W * sc), int(360 * sc)), Image.LANCZOS)
        ov.alpha_composite(lay, (960 - lay.width // 2, 500 - lay.height // 2))
        ft = f(IMPACT, 150)
        wd = ImageDraw.Draw(Image.new("L", (1, 1))).textlength("WINTER WOLF'S DEN", font=ft) + 12
        BOXES.append(("WINTER WOLF'S DEN (final scale)", (960 - wd / 2, 500 - 90, 960 + wd / 2, 500 + 90)))
    if t >= 1.4:
        k = min(1.0, (t - 1.4) / 0.4)
        text(d, (960, 660), "A REVIEW SHOW", f(SERIFI, 56), tuple(int(v * k) for v in CYAN) + (255,))
        d.line((560, 720, 1360, 720), fill=tuple(int(v * k) for v in GOLD) + (255,), width=4)
    out = Image.alpha_composite(im, ov)
    if t > 5.5:
        out = Image.eval(out.convert("RGB"), lambda v: int(v * max(0, (6.0 - t) / 0.5)))
    return out.convert("RGB")


def render(fn, n, out, audio_filter):
    cmd = ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", SND, "-filter_complex", audio_filter, "-map", "0:v", "-map", "[a]",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-r", str(FPS), "-c:a", "aac", "-b:a", "192k",
           "-frames:v", str(n), out]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(n):
        p.stdin.write(np.asarray(fn(i).convert("RGB")).tobytes())
    p.stdin.close()
    assert p.wait() == 0


def uniq(boxes):
    seen, out = set(), []
    for s, b in boxes:
        k = (s, tuple(round(float(x)) for x in b))
        if k not in seen:
            seen.add(k)
            out.append((s, b))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--outdir", default=r"D:\WKP\scratch\wwd-vfx-level\drill1")
    a = ap.parse_args()
    os.makedirs(a.outdir, exist_ok=True)
    render(end_frame, 360, os.path.join(a.outdir, "drill1-end-card-12s.mp4"),
           "[1:a]adelay=300|300,volume=0.6,apad=whole_dur=12,atrim=0:12[a]")
    end_boxes = uniq(BOXES)
    BOXES.clear()
    render(sting_frame, 180, os.path.join(a.outdir, "drill1-sting-6s.mp4"),
           "[1:a]adelay=850|850,apad=whole_dur=6,atrim=0:6,afade=t=out:st=5.3:d=0.7[a]")
    sting_boxes = uniq(BOXES)
    labels = ("LATEST UPLOAD", "BEST FOR YOU", "SUBSCRIBE")
    zones = list(TILES) + [(RING[0] - RING[2] - 4, RING[1] - RING[2] - 4, RING[0] + RING[2] + 4, RING[1] + RING[2] + 4)]
    for name, boxes in (("end card", end_boxes), ("sting", sting_boxes)):
        bad = [(s, b) for s, b in boxes if b[0] < SAFE[0] or b[1] < SAFE[1] or b[2] > SAFE[2] or b[3] > SAFE[3]]
        print(name, "text boxes:")
        for s, b in boxes:
            print("   ", s, [round(float(x)) for x in b])
        print(name, "outside safe", SAFE, ":", bad)
    overl = []
    for s, b in end_boxes:
        for z in zones:
            hit = not (b[2] < z[0] or b[0] > z[2] or b[3] < z[1] or b[1] > z[3])
            if hit:
                overl.append((s, b, z))
    print("end card text touching a zone (zone labels sit above/below, must not touch):", overl)
    json.dump({"tiles": TILES, "ring": RING, "end": [(s, [float(x) for x in b]) for s, b in end_boxes],
               "sting": [(s, [float(x) for x in b]) for s, b in sting_boxes]},
              open(os.path.join(a.outdir, "geometry.json"), "w"))


if __name__ == "__main__":
    main()
