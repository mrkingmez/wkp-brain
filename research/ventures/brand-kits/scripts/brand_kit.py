"""Side business brand kit builder (graphic-design, 2026-11-10).

Pure Pillow, free, no credits, no network. Fonts: Poppins (SIL OFL) from the
wwd-review-pipeline assets folder.

Run:  python brand_kit.py            (builds both kits with the lead names)
      python brand_kit.py --name "Same Face" --sub "PHOTO RESTORATION" --kit photo
Change a name here and every asset rebuilds with it.
"""
import argparse, math, os, random
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FONT_DIR = r"D:\WKP\.claude\skills\wwd-review-pipeline\assets\fonts"
BOLD = os.path.join(FONT_DIR, "Poppins-Bold.ttf")
SEMI = os.path.join(FONT_DIR, "Poppins-SemiBold.ttf")
OUT = r"D:\WKP\research\ventures\brand-kits"

SS = 4  # supersample factor for the mark

KITS = {
    "photo": {
        "folder": "photo-restore",
        "name": "Same Face",
        "sub": "PHOTO RESTORATION",
        "tag": "Old family photos, cleaned up. Every face checked by hand.",
        "light": {"bg": (243, 236, 221), "ink": (35, 32, 28), "accent": (180, 83, 42), "soft": (214, 200, 170)},
        "dark":  {"bg": (28, 25, 22),   "ink": (243, 236, 221), "accent": (224, 128, 84), "soft": (92, 80, 64)},
    },
    "transcribe": {
        "folder": "transcription",
        "name": "Listen Twice",
        "sub": "TRANSCRIPTION",
        "tag": "Machine draft, human verified. Plain, accurate transcripts.",
        "light": {"bg": (246, 248, 249), "ink": (20, 38, 58), "accent": (31, 122, 140), "soft": (196, 214, 220)},
        "dark":  {"bg": (14, 26, 40),   "ink": (240, 246, 248), "accent": (74, 184, 204), "soft": (60, 84, 104)},
    },
}


def font(path, size):
    return ImageFont.truetype(path, int(size))


def text_w(draw, s, f, spacing=0):
    return sum(draw.textlength(c, font=f) + spacing for c in s) - spacing


def spaced(draw, xy, s, f, fill, spacing=0):
    x, y = xy
    for c in s:
        draw.text((x, y), c, font=f, fill=fill)
        x += draw.textlength(c, font=f) + spacing


# ---------------------------------------------------------------- marks
def mark_photo(size, c):
    """Print with two photo corners, split diagonal: faded half and clear half.
    Says before and after without a face."""
    S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pad = S * 0.12
    box = (pad, pad, S - pad, S - pad)
    r = S * 0.05
    # frame of the print
    d.rounded_rectangle(box, r, fill=c["soft"])
    inner = (pad + S * 0.07, pad + S * 0.07, S - pad - S * 0.07, S - pad - S * 0.07)
    # faded half (whole inner), then clear half clipped to the lower right triangle
    d.rectangle(inner, fill=tuple(int(v * 0.5 + 255 * 0.5) for v in c["soft"]))
    clear = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    cd = ImageDraw.Draw(clear)
    cd.rectangle(inner, fill=c["ink"])
    mask = Image.new("L", (S, S), 0)
    md = ImageDraw.Draw(mask)
    x0, y0, x1, y1 = inner
    md.polygon([(x1, y0), (x1, y1), (x0, y1)], fill=255)
    im.paste(clear, (0, 0), mask)
    # tiny head and shoulders cut across the diagonal, drawn as negative shape
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2 + S * 0.02
    hr = S * 0.085
    for col, region in ((c["ink"], "faded"), (c["bg"], "clear")):
        layer = Image.new("RGBA", (S, S), (0, 0, 0, 0))
        ld = ImageDraw.Draw(layer)
        ld.ellipse((cx - hr, cy - hr * 1.7, cx + hr, cy + hr * 0.3), fill=col)
        ld.pieslice((cx - hr * 2.2, cy + hr * 0.5, cx + hr * 2.2, cy + hr * 4.6), 180, 360, fill=col)
        m2 = Image.new("L", (S, S), 0)
        m2d = ImageDraw.Draw(m2)
        if region == "faded":
            m2d.polygon([(x0, y0), (x1, y0), (x0, y1)], fill=255)
            # keep faded half faint
            layer.putalpha(ImageChops.multiply(layer.split()[3], m2).point(lambda v: int(v * 0.35)))
            im.alpha_composite(layer)
        else:
            m2d.polygon([(x1, y0), (x1, y1), (x0, y1)], fill=255)
            layer.putalpha(ImageChops.multiply(layer.split()[3], m2))
            im.alpha_composite(layer)
    d = ImageDraw.Draw(im)
    # photo corners (accent triangles) top-left and bottom-right
    k = S * 0.26
    d.polygon([(pad, pad), (pad + k, pad), (pad, pad + k)], fill=c["accent"])
    d.polygon([(S - pad, S - pad), (S - pad - k, S - pad), (S - pad, S - pad - k)], fill=c["accent"])
    return im.resize((size, size), Image.LANCZOS)


def mark_transcribe(size, c):
    """Waveform bars on the left resolve into text lines on the right, inside a rounded tile."""
    S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    pad = S * 0.08
    d.rounded_rectangle((pad, pad, S - pad, S - pad), S * 0.12, fill=c["ink"])
    # waveform: 5 bars
    heights = [0.22, 0.44, 0.62, 0.36, 0.18]
    bw = S * 0.05
    gap = S * 0.035
    x = S * 0.16
    cy = S / 2
    for h in heights:
        hh = S * h
        d.rounded_rectangle((x, cy - hh / 2, x + bw, cy + hh / 2), bw / 2, fill=c["accent"])
        x += bw + gap
    # text lines
    lx = S * 0.585
    lw = [0.24, 0.2, 0.24, 0.13]
    ly = S * 0.33
    lh = S * 0.052
    for w in lw:
        d.rounded_rectangle((lx, ly, lx + S * w, ly + lh), lh / 2, fill=c["bg"])
        ly += S * 0.115
    return im.resize((size, size), Image.LANCZOS)


MARKS = {"photo": mark_photo, "transcribe": mark_transcribe}


# ---------------------------------------------------------------- lockups
def wordmark(kit, c, height, name=None, sub=None):
    """Horizontal lockup, transparent background, height in px."""
    name = name or kit["name"]
    sub = sub or kit["sub"]
    key = kit["key"]
    mk = MARKS[key](height, c)
    f1 = font(BOLD, height * 0.40)
    f2 = font(SEMI, height * 0.15)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    sp = height * 0.035
    w1 = tmp.textlength(name, font=f1)
    w2 = text_w(tmp, sub, f2, sp)
    gap = height * 0.22
    W = int(height + gap + max(w1, w2) + height * 0.05)
    im = Image.new("RGBA", (W, height), (0, 0, 0, 0))
    im.alpha_composite(mk, (0, 0))
    d = ImageDraw.Draw(im)
    x = height + gap
    d.text((x, height * 0.20), name, font=f1, fill=c["ink"])
    spaced(d, (x + height * 0.01, height * 0.20 + height * 0.40 * 1.28), sub, f2, c["accent"], sp)
    return im


def stacked(kit, c, width, name=None, sub=None):
    """Stacked lockup (mark over name), for square profile use."""
    name = name or kit["name"]
    sub = sub or kit["sub"]
    key = kit["key"]
    ms = int(width * 0.52)
    mk = MARKS[key](ms, c)
    f1 = font(BOLD, width * 0.115)
    f2 = font(SEMI, width * 0.05)
    sp = width * 0.012
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    w1 = tmp.textlength(name, font=f1)
    # shrink name if too wide
    while w1 > width * 0.9:
        f1 = font(BOLD, f1.size - 2)
        w1 = tmp.textlength(name, font=f1)
    w2 = text_w(tmp, sub, f2, sp)
    H = int(ms + width * 0.07 + f1.size * 1.25 + f2.size * 1.6)
    im = Image.new("RGBA", (width, H), (0, 0, 0, 0))
    im.alpha_composite(mk, ((width - ms) // 2, 0))
    d = ImageDraw.Draw(im)
    y = ms + width * 0.05
    d.text(((width - w1) / 2, y), name, font=f1, fill=c["ink"])
    spaced(d, ((width - w2) / 2, y + f1.size * 1.3), sub, f2, c["accent"], sp)
    return im


def on_bg(img, bg):
    base = Image.new("RGBA", img.size, bg + (255,))
    base.alpha_composite(img)
    return base


def fit_height(img, h):
    w = int(img.width * h / img.height)
    return img.resize((w, h), Image.LANCZOS)


# ---------------------------------------------------------------- assets
def build_logos(kit, out):
    for mode in ("light", "dark"):
        c = kit[mode]
        wm = wordmark(kit, c, 600)
        wm.save(os.path.join(out, f"logo-horizontal-{mode}-transparent.png"))
        on_bg(wm.resize((wm.width, wm.height)), c["bg"]).crop((0, 0, wm.width, wm.height)).save(
            os.path.join(out, f"logo-horizontal-{mode}.png"))
        mk = MARKS[kit["key"]](1000, c)
        mk.save(os.path.join(out, f"logo-mark-{mode}-transparent.png"))
        # padded lockup on its own background for easy preview
        pad = 160
        W, H = wm.width + pad * 2, wm.height + pad * 2
        canvas = Image.new("RGBA", (W, H), c["bg"] + (255,))
        canvas.alpha_composite(wm, (pad, pad))
        canvas.convert("RGB").save(os.path.join(out, f"logo-horizontal-{mode}-padded.png"))
        st = stacked(kit, c, 1000)
        canvas = Image.new("RGBA", (1400, st.height + 400), c["bg"] + (255,))
        canvas.alpha_composite(st, (200, 200))
        canvas.convert("RGB").save(os.path.join(out, f"logo-stacked-{mode}.png"))


def build_profile(kit, out):
    for mode in ("light", "dark"):
        c = kit[mode]
        S = 640
        im = Image.new("RGBA", (S, S), c["bg"] + (255,))
        mk = MARKS[kit["key"]](int(S * 0.70), c)
        im.alpha_composite(mk, ((S - mk.width) // 2, (S - mk.height) // 2))
        im.convert("RGB").save(os.path.join(out, f"facebook-profile-640-{mode}.png"))
        im.convert("RGB").resize((320, 320), Image.LANCZOS).save(os.path.join(out, f"facebook-profile-320-{mode}.png"))
        # circle preview, Facebook crops the profile picture to a circle
        circ = im.convert("RGB").resize((320, 320), Image.LANCZOS)
        m = Image.new("L", (320, 320), 0)
        ImageDraw.Draw(m).ellipse((0, 0, 319, 319), fill=255)
        prev = Image.new("RGBA", (320, 320), (128, 128, 128, 255))
        prev.paste(circ, (0, 0), m)
        prev.convert("RGB").save(os.path.join(out, f"facebook-profile-circle-preview-{mode}.png"))


def build_banner(kit, out):
    """Facebook Page cover: 851x315 (OBSERVED on Meta help page). Also built at 2x.
    Mobile shows a taller crop (640x360, SECONDARY) so the content stays in the centre band."""
    for mode in ("light", "dark"):
        c = kit[mode]
        for scale in (1, 2):
            W, H = 851 * scale, 315 * scale
            im = Image.new("RGBA", (W, H), c["bg"] + (255,))
            d = ImageDraw.Draw(im)
            # soft stripe band along the bottom for structure
            d.rectangle((0, int(H * 0.90), W, H), fill=c["accent"])
            wm = wordmark(kit, c, int(H * 0.40))
            # safe zone: centred, left-weighted block
            x = int(W * 0.08)
            y = int(H * 0.17)
            im.alpha_composite(wm, (x, y))
            f = font(SEMI, H * 0.068)
            d.text((x, y + wm.height + H * 0.07), kit["tag"], font=f, fill=c["ink"])
            # right side: faint large mark
            big = MARKS[kit["key"]](int(H * 0.62), c)
            big.putalpha(big.split()[3].point(lambda v: int(v * 0.16)))
            im.alpha_composite(big, (W - big.width - int(W * 0.05), int((H - big.height) / 2 - H * 0.03)))
            rgb = im.convert("RGB")
            suffix = "" if scale == 1 else "-2x"
            rgb.save(os.path.join(out, f"facebook-cover-851x315{suffix}-{mode}.png"))
            if scale == 1:
                rgb.save(os.path.join(out, f"facebook-cover-851x315-{mode}.jpg"), quality=90, optimize=True)


def build_gig(kit, out):
    """Fiverr gig image 1280x769 (from Fiverr help via search summary, direct fetch 403)."""
    for mode in ("light", "dark"):
        c = kit[mode]
        W, H = 1280, 769
        im = Image.new("RGBA", (W, H), c["bg"] + (255,))
        d = ImageDraw.Draw(im)
        d.rectangle((0, H - 26, W, H), fill=c["accent"])
        if kit["key"] == "photo":
            head = "I will restore your old family photo"
            lines = ["Scratches, creases, fading, stains", "Every face checked by hand", "Original always returned untouched"]
        else:
            head = "I will transcribe your audio"
            lines = ["Machine draft, human verified", "Speaker labels and timestamps", "Plain English, fast turnaround"]
        # headline, wrapped to the left 62 percent
        f = font(BOLD, 70)
        words = head.split()
        rows, cur = [], ""
        for w in words:
            t = (cur + " " + w).strip()
            if d.textlength(t, font=f) > W * 0.47 and cur:
                rows.append(cur)
                cur = w
            else:
                cur = t
        rows.append(cur)
        y = 150
        for r in rows:
            d.text((70, y), r, font=f, fill=c["ink"])
            y += 88
        y += 22
        fb = font(SEMI, 36)
        for ln in lines:
            d.ellipse((74, y + 15, 92, y + 33), fill=c["accent"])
            d.text((112, y), ln, font=fb, fill=c["ink"])
            y += 56
        # brand strip top-left
        wm = wordmark(kit, c, 84)
        im.alpha_composite(wm, (70, 40))
        # right side artwork
        if kit["key"] == "photo":
            art = polaroid_art(c, 430)
        else:
            art = transcript_art(c, 430)
        im.alpha_composite(art, (W - art.width - 70, (H - art.height) // 2 - 20))
        im.convert("RGB").save(os.path.join(out, f"fiverr-gig-cover-1280x769-{mode}.png"))


def polaroid_art(c, size):
    """Code-drawn illustration of a worn print with photo corners. Not a result claim."""
    S = size * 2
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    # shadow
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((S * .14, S * .16, S * .90, S * .94), 14, fill=(0, 0, 0, 90))
    sh = sh.filter(ImageFilter.GaussianBlur(S * 0.02))
    im.alpha_composite(sh)
    d.rounded_rectangle((S * .10, S * .10, S * .86, S * .90), 10, fill=(250, 246, 236), outline=c["soft"], width=4)
    inner = (S * .16, S * .16, S * .80, S * .72)
    d.rectangle(inner, fill=(176, 160, 132))
    x0, y0, x1, y1 = inner
    # silhouette, no face detail
    cx = (x0 + x1) / 2
    d.ellipse((cx - S * .08, y0 + S * .10, cx + S * .08, y0 + S * .26), fill=(120, 104, 84))
    d.pieslice((cx - S * .19, y0 + S * .24, cx + S * .19, y0 + S * .62), 180, 360, fill=(120, 104, 84))
    # crease and scratches
    rnd = random.Random(7)
    d.line((x0, (y0 + y1) / 2, x1, (y0 + y1) / 2 + S * .02), fill=(238, 230, 214), width=7)
    for _ in range(14):
        a = rnd.uniform(x0, x1)
        b = rnd.uniform(y0, y1)
        d.line((a, b, a + rnd.uniform(-60, 60), b + rnd.uniform(10, 70)), fill=(236, 228, 210), width=2)
    # corners
    k = S * .13
    for (px, py, dx, dy) in ((S * .10, S * .10, 1, 1), (S * .86, S * .90, -1, -1)):
        d.polygon([(px, py), (px + dx * k, py), (px, py + dy * k)], fill=c["accent"])
    return im.resize((size, size), Image.LANCZOS)


def transcript_art(c, size):
    S = size * 2
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sh = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((S * .10, S * .12, S * .92, S * .92), 22, fill=(0, 0, 0, 80))
    sh = sh.filter(ImageFilter.GaussianBlur(S * 0.02))
    im.alpha_composite(sh)
    d.rounded_rectangle((S * .08, S * .08, S * .88, S * .88), 22, fill=c["ink"])
    # waveform strip
    rnd = random.Random(3)
    x = S * .14
    cy = S * .26
    while x < S * .80:
        h = rnd.uniform(.03, .13) * S
        d.rounded_rectangle((x, cy - h / 2, x + S * .014, cy + h / 2), 4, fill=c["accent"])
        x += S * .028
    # transcript lines with speaker tags
    y = S * .42
    for i, (tag, w) in enumerate((("A", .50), ("B", .42), ("A", .56), ("B", .30))):
        d.rounded_rectangle((S * .14, y, S * .22, y + S * .05), 8, fill=c["accent"])
        d.rounded_rectangle((S * .26, y + S * .012, S * .26 + S * w * .75, y + S * .038), 8, fill=c["bg"])
        y += S * .105
    return im.resize((size, size), Image.LANCZOS)


# ---------------------------------------------------------------- before/after
def sample_photo(w, h, damaged):
    """Code drawn stand-in so the template previews. Not a real restoration."""
    im = Image.new("RGB", (w, h), (196, 178, 148) if damaged else (210, 196, 172))
    d = ImageDraw.Draw(im)
    cx = w / 2
    d.ellipse((cx - w * .09, h * .22, cx + w * .09, h * .22 + w * .19), fill=(110, 94, 76))
    d.pieslice((cx - w * .21, h * .22 + w * .15, cx + w * .21, h * .22 + w * .15 + w * .5), 180, 360, fill=(110, 94, 76))
    if damaged:
        rnd = random.Random(11)
        d.line((0, h * .5, w, h * .53), fill=(240, 232, 216), width=max(4, w // 90))
        for _ in range(40):
            a, b = rnd.uniform(0, w), rnd.uniform(0, h)
            d.line((a, b, a + rnd.uniform(-w * .05, w * .05), b + rnd.uniform(h * .02, h * .09)), fill=(238, 230, 212), width=2)
        for _ in range(9):
            a, b = rnd.uniform(0, w), rnd.uniform(0, h)
            r = rnd.uniform(w * .02, w * .06)
            d.ellipse((a - r, b - r, a + r, b + r), fill=(160, 138, 104))
        im = Image.blend(im, Image.new("RGB", (w, h), (214, 204, 186)), 0.3)
    return im


def contain(img, box_w, box_h):
    r = min(box_w / img.width, box_h / img.height)  # contain, never crop (Zac rule)
    return img.resize((max(1, int(img.width * r)), max(1, int(img.height * r))), Image.LANCZOS)


def before_after(kit, mode, before, after, W, H, tagline=True, placeholder=False, watermark=False):
    c = kit[mode]
    im = Image.new("RGB", (W, H), c["bg"])
    d = ImageDraw.Draw(im)
    m = int(W * 0.04)
    top = int(H * 0.17)
    bottom = int(H * 0.13)
    gap = int(W * 0.03)
    bw = (W - 2 * m - gap) // 2
    bh = H - top - bottom
    wm = wordmark(kit, c, int(H * 0.085))
    im.paste(wm, (m, int(H * 0.04)), wm)
    for i, (label, src) in enumerate((("BEFORE", before), ("AFTER", after))):
        x = m + i * (bw + gap)
        d.rounded_rectangle((x, top, x + bw, top + bh), 12, fill=c["soft"])
        pic = contain(src.convert("RGB"), bw - 24, bh - 24)
        px = x + (bw - pic.width) // 2
        py = top + (bh - pic.height) // 2
        im.paste(pic, (px, py))
        f = font(BOLD, H * 0.038)
        tw = d.textlength(label, font=f)
        pill = (x + 16, top + 16, x + 16 + tw + 36, top + 16 + H * 0.06)
        d.rounded_rectangle(pill, 10, fill=c["accent"] if label == "AFTER" else c["ink"])
        d.text((x + 34, top + 16 + H * 0.008), label, font=f, fill=c["bg"] if label == "BEFORE" else (255, 255, 255))
    if tagline:
        line = "AI-assisted. Every face checked by hand. Original returned untouched."
        fs = H * 0.034
        f = font(SEMI, fs)
        while d.textlength(line, font=f) > W - 2 * m:
            fs -= 1
            f = font(SEMI, fs)
        d.text((m, H - bottom + int(H * 0.035)), line, font=f, fill=c["ink"])
    if placeholder:
        f = font(SEMI, H * 0.03)
        msg = "TEMPLATE SAMPLE ART, SWAP IN REAL PHOTOS" if W > H else "TEMPLATE SAMPLE ART"
        d.text((W - m - d.textlength(msg, font=f), int(H * 0.06)), msg, font=f, fill=c["accent"])
    if watermark:
        wmk = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        wd = ImageDraw.Draw(wmk)
        fw = font(BOLD, H * 0.09)
        for yy in range(-H, H * 2, int(H * 0.28)):
            for xx in range(-W, W * 2, int(W * 0.40)):
                wd.text((xx, yy), "PREVIEW", font=fw, fill=(255, 255, 255, 70))
        wmk = wmk.rotate(24, resample=Image.BICUBIC)
        base = im.convert("RGBA")
        base.alpha_composite(wmk)
        im = base.convert("RGB")
    return im


def build_before_after(kit, out):
    for mode in ("light", "dark"):
        for (W, H, tag) in ((1920, 1080, "landscape-1920x1080"), (1080, 1080, "square-1080x1080")):
            sz = (900, 1200) if tag.startswith("square") else (1200, 900)
            b = sample_photo(*sz, damaged=True)
            a = sample_photo(*sz, damaged=False)
            before_after(kit, mode, b, a, W, H, placeholder=True).save(
                os.path.join(out, f"before-after-template-{tag}-{mode}-SAMPLE.png"))


def write_before_after_tool(out_dir):
    path = os.path.join(out_dir, "make_before_after.py")
    code = '''"""Compose a real before/after image (contain-fit, never crops). Photo restore only.
python make_before_after.py --before B.jpg --after A.jpg --out out.png [--mode light|dark]
       [--shape landscape|square] [--preview]   (--preview adds a diagonal PREVIEW watermark)
Reads the look from brand_kit.py in the same folder. Use only photos Zac may show."""
import argparse, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brand_kit as bk
from PIL import Image
ap = argparse.ArgumentParser()
ap.add_argument("--before", required=True); ap.add_argument("--after", required=True)
ap.add_argument("--out", required=True); ap.add_argument("--mode", default="light")
ap.add_argument("--shape", default="landscape"); ap.add_argument("--preview", action="store_true")
a = ap.parse_args()
kit = dict(bk.KITS["photo"]); kit["key"] = "photo"
W, H = (1920, 1080) if a.shape == "landscape" else (1080, 1080)
im = bk.before_after(kit, a.mode, Image.open(a.before), Image.open(a.after), W, H, watermark=a.preview)
im.save(a.out); print("saved", a.out)
'''
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(code)


def contact_sheet(kit, out):
    files = [f for f in sorted(os.listdir(out)) if f.endswith(".png") and f.startswith(("logo-horizontal", "fiverr", "facebook-cover", "facebook-profile-640"))
             and "transparent" not in f and "padded" not in f and "2x" not in f]
    thumbs = []
    for f in files:
        im = Image.open(os.path.join(out, f)).convert("RGB")
        im.thumbnail((620, 380))
        thumbs.append(im)
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 640 + 20, rows * 400 + 20), (120, 120, 120))
    for i, t in enumerate(thumbs):
        sheet.paste(t, (20 + (i % cols) * 640, 20 + (i // cols) * 400))
    sheet.save(os.path.join(out, "_contact-sheet.png"))


def build(key, name=None, sub=None):
    kit = dict(KITS[key])
    kit["key"] = key
    if name:
        kit["name"] = name
    if sub:
        kit["sub"] = sub
    out = os.path.join(OUT, kit["folder"])
    os.makedirs(out, exist_ok=True)
    build_logos(kit, out)
    build_profile(kit, out)
    build_banner(kit, out)
    build_gig(kit, out)
    if key == "photo":
        build_before_after(kit, out)
        write_before_after_tool(os.path.join(OUT, "scripts"))
    contact_sheet(kit, out)
    print("built", key, kit["name"], "->", out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--kit", choices=["photo", "transcribe"])
    ap.add_argument("--name")
    ap.add_argument("--sub")
    a = ap.parse_args()
    if a.kit:
        build(a.kit, a.name, a.sub)
    else:
        build("photo")
        build("transcribe")
