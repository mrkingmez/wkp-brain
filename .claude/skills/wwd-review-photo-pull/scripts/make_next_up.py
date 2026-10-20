"""Render a 'NEXT UP: <TITLE>' end card as a drop-in clip with the punch sound baked in.

  python make_next_up.py --title "STREET FIGHTER" --out "P:\\WWD Kit\\Cards\\Next Up - Street Fighter.mov"
Plain Impact type on black with scanlines. Never use a film's own logo or font.
"""
import argparse, os, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS, N = 1920, 1080, 30, 120
FONT = r"C:\Windows\Fonts\impact.ttf"
PUNCH = r"P:\Sounds\Sound FX\punch-face-hard_f1oeQhNO.mp3"


def text_img(s, size, fill):
    f = ImageFont.truetype(FONT, size)
    b = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), s, font=f)
    im = Image.new("RGBA", (b[2] - b[0] + 20, b[3] - b[1] + 20), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((10 - b[0], 10 - b[1]), s, font=f, fill=fill, stroke_width=4, stroke_fill=(0, 0, 0))
    return im


def fighter_title(lines, size=330):
    """Arcade-fighter look: slanted heavy letters, rough brush edges, yellow-orange-red
    fire gradient, thick dark-red outline, staggered stacked lines. Evokes the style
    without copying any studio logo."""
    f = ImageFont.truetype(FONT, size)
    tmp = ImageDraw.Draw(Image.new("L", (1, 1)))
    boxes = [tmp.textbbox((0, 0), l, font=f) for l in lines]
    lw = [b[2] - b[0] for b in boxes]
    lh = max(b[3] - b[1] for b in boxes)
    step = int(lh * 0.92)
    stagger = int(size * 0.55)
    w = max(lw[i] + i * stagger for i in range(len(lines))) + 120
    h = step * (len(lines) - 1) + lh + 120
    m = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(m)
    for i, (l, b) in enumerate(zip(lines, boxes)):
        d.text((60 + i * stagger - b[0], 60 + i * step - b[1]), l, font=f, fill=255)
    # rough brush edges: jitter the mask with noise, then re-threshold
    rng = np.random.default_rng(3)
    n = Image.fromarray((rng.random((h // 6 + 1, w // 6 + 1)) * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
    blur = m.filter(ImageFilter.GaussianBlur(3))
    a = np.asarray(blur).astype(float) + (np.asarray(n).astype(float) - 128) * 0.45
    m = Image.fromarray(np.where(a > 128, 255, 0).astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    # slant
    sh = 0.28
    W2 = w + int(h * sh)
    m = m.transform((W2, h), Image.AFFINE, (1, sh, -h * sh, 0, 1, 0), Image.BICUBIC)
    # fire gradient fill
    g = np.linspace(0, 1, h)[:, None, None]
    top, mid, bot = np.array([255, 240, 90]), np.array([255, 150, 20]), np.array([215, 30, 20])
    col = np.where(g < 0.5, top + (mid - top) * (g / 0.5), mid + (bot - mid) * ((g - 0.5) / 0.5))
    fill = Image.fromarray(np.broadcast_to(col, (h, W2, 3)).astype(np.uint8), "RGB").convert("RGBA")
    fill.putalpha(m)
    # thick dark outline + drop shadow
    ol = m.filter(ImageFilter.MaxFilter(15))
    out = Image.new("RGBA", (W2 + 30, h + 30), (0, 0, 0, 0))
    shadow = Image.new("RGBA", (W2, h), (0, 0, 0, 255)); shadow.putalpha(ol.filter(ImageFilter.GaussianBlur(6)))
    out.alpha_composite(shadow, (18, 22))
    ring = Image.new("RGBA", (W2, h), (90, 8, 8, 255)); ring.putalpha(ol)
    out.alpha_composite(ring, (0, 0))
    out.alpha_composite(fill, (0, 0))
    return out.crop(out.getbbox())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--style", choices=["plain", "fighter"], default="plain")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    bg = Image.new("RGB", (W, H), (6, 6, 10))
    d = ImageDraw.Draw(bg)
    for y in range(0, H, 4):
        d.line([(0, y), (W, y)], fill=(16, 16, 24))
    vign = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vign).ellipse([-300, -200, W + 300, H + 200], fill=255)
    vign = vign.filter(ImageFilter.GaussianBlur(120))
    bg = Image.composite(bg, Image.new("RGB", (W, H), (0, 0, 0)), vign)
    small = text_img("NEXT UP", 70, (255, 255, 255))
    if a.style == "fighter":
        big = fighter_title(a.title.upper().split())
        if big.width > 1700:
            big = big.resize((1700, int(big.height * 1700 / big.width)), Image.LANCZOS)
    else:
        big = text_img(a.title.upper(), 210, (255, 196, 30))
    top = (H - (small.height + 30 + big.height)) // 2
    sy, by = top, top + small.height + 30
    hit = 6
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(N):
            f = bg.copy().convert("RGBA")
            f.alpha_composite(small, ((W - small.width) // 2, sy))
            if i < hit:
                s = 1.3 - 0.3 * (i / hit)
            else:
                s = 1.0
            bi = big.resize((int(big.width * s), int(big.height * s)), Image.BICUBIC)
            dx = 0
            if hit <= i < hit + 6:
                dx = (12 - 2 * (i - hit)) * (1 if i % 2 else -1)
            if i >= 1:
                f.alpha_composite(bi, ((W - bi.width) // 2 + dx, by - (bi.height - big.height) // 2))
            if i >= N - 12:
                k = (i - (N - 12)) / 12
                f = Image.blend(f, Image.new("RGBA", (W, H), (0, 0, 0, 255)), k)
            f.convert("RGB").save(os.path.join(tmp, f"f{i:04d}.png"))
        ms = int(hit / FPS * 1000)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png"), "-i", PUNCH,
                        "-filter_complex", f"[1:a]adelay={ms}|{ms},apad[a]", "-map", "0:v", "-map", "[a]",
                        "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le", "-c:a", "pcm_s16le", "-ar", "48000",
                        "-t", f"{N / FPS:.3f}", a.out], check=True)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
