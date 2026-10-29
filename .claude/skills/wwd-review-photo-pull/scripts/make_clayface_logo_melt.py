"""Clayface logo sting: the Winter Wolf's Den logo turns into brown clay all at once, ripples, then melts
and drips off the bottom of the screen. Built from the logo PNG with code, no AI video, no credits (2026-10-25).

  python make_clayface_logo_melt.py [--logo PATH] [--out PATH]
Writes a 5 s 1920x1080 24 fps H.264 MP4 on black (silent) and a second MP4 with owned sounds mixed in.
"""
import argparse, os, subprocess, tempfile
import numpy as np
from PIL import Image, ImageFilter
from scipy.ndimage import map_coordinates, gaussian_filter, gaussian_filter1d

W, H, FPS, N = 1920, 1080, 24, 120
X0, X1 = 520, 1400                      # work band around the logo (logo spans 575..1345)
SFX = "P:\\Sounds\\Sound FX\\"
SOUNDS = [  # (file, start seconds, volume)
    (SFX + "low-long-background-rumble_fJ0TNBVO.mp3", 0.0, 0.25),
    (SFX + "Adobe\\Foley\\Foley Mud Suction Wet 01.wav", 1.0, 0.9),
    (SFX + "Adobe\\Horror\\Horror Scary Skin Peeling Off Slowly.wav", 1.7, 0.5),
    (SFX + "Adobe\\Foley\\Foley Mud Suction 01.wav", 2.6, 0.7),
    (SFX + "Adobe\\Household\\Household Sponge Squish Short 01.wav", 3.3, 0.5),
    (SFX + "Adobe\\Household\\Household Sponge Squish Short 01.wav", 3.7, 0.4),
    (SFX + "Adobe\\Household\\Household Sponge Squish Short 01.wav", 4.1, 0.3),
    (SFX + "Adobe\\Impacts\\Impact Body Hit Wet 01.wav", 4.4, 0.4),
]
rng = np.random.default_rng(11)


def smooth_noise(shape, sigma, seed):
    r = np.random.default_rng(seed)
    n = gaussian_filter(r.standard_normal(shape), sigma)
    return n / (np.abs(n).max() + 1e-9)


def clay_version(rgba):
    """Same shape, same layout, wet brown mud-clay look. rgba is float 0..1, shape (h, w, 4)."""
    rgb, a = rgba[..., :3], rgba[..., 3]
    lum = rgb @ np.array([0.30, 0.59, 0.11])
    lum = (lum - lum.min()) / (np.ptp(lum) + 1e-9)
    dark, mid, light = np.array([0.13, 0.07, 0.04]), np.array([0.36, 0.21, 0.11]), np.array([0.60, 0.40, 0.24])
    t = lum[..., None]
    col = np.where(t < 0.5, dark + (mid - dark) * (t / 0.5), mid + (light - mid) * ((t - 0.5) / 0.5))
    h, w = lum.shape
    # soft lumpy surface, lit from the top left, only a hint of fine grain
    bump = smooth_noise((h, w), 18, 3) * 0.85 + smooth_noise((h, w), 6, 4) * 0.15
    gy, gx = np.gradient(bump)
    shade = np.clip(1.0 + (-gx * 0.6 - gy * 0.9) * 55, 0.65, 1.35)
    col = dark + (col - dark) * 0.55 + (mid - dark) * 0.35      # flatter, more even mud so it reads as clay
    col = col * shade[..., None]
    # wet sheen: broad soft highlights, not sparkles
    spec = np.clip((shade - 1.12) * 3.0, 0, 1)
    spec = gaussian_filter(spec, 2.0)[..., None]
    col = col + spec * np.array([0.75, 0.62, 0.48]) * 0.45
    # keep the original silhouette, just slightly rounded
    a2 = np.clip((gaussian_filter(a, 1.2) - 0.25) * 1.9, 0, 1)
    return np.dstack([np.clip(col, 0, 1), a2])


def warp(img, dx, dy):
    """Backward-map warp of an (h, w, 4) image by displacement fields (sample from x+dx, y+dy)."""
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    out = np.empty_like(img)
    for c in range(4):
        out[..., c] = map_coordinates(img[..., c], [yy + dy, xx + dx], order=1, mode="constant", cval=0.0)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--logo", default=r"L:\Winter Wolfs Den review show\Pictures\logo.png")
    ap.add_argument("--out", default=r"P:\WWD Kit\Clayface\Clayface Logo Melt.mp4")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)

    logo = np.asarray(Image.open(a.logo).convert("RGBA")).astype(np.float32) / 255.0
    band = logo[:, X0:X1]                       # (1080, 880, 4)
    h, w, _ = band.shape
    clay = clay_version(band)
    # keep the original cyan glow behind the logo for the still first second
    glow = np.asarray(Image.fromarray((band * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(22))).astype(np.float32) / 255.0

    # per-column drip lengths: smooth so the drips are thick strands, not zigzags
    col_len = gaussian_filter1d(np.abs(rng.standard_normal(w)), 38)
    col_len = 0.45 + 1.1 * (col_len - col_len.min()) / (np.ptp(col_len) + 1e-9)
    ripple_a = smooth_noise((h, w), 60, 21)
    ripple_b = smooth_noise((h, w), 60, 22)

    def ease(t):
        t = min(max(t, 0.0), 1.0)
        return t * t * (3 - 2 * t)

    with tempfile.TemporaryDirectory() as tmp:
        for i in range(N):
            t = i / FPS
            # stage weights
            to_clay = ease((t - 1.0) / 0.5)                 # 1.0 to 1.5 s: whole logo turns clay at once
            ripple = ease((t - 1.3) / 0.5) * (1 - ease((t - 2.6) / 0.6))   # 1.3 to 3.2 s: skin ripples
            melt = max(0.0, (t - 2.4) / 2.1)                # 2.4 to 4.5 s: sag, drip, fall

            base = band.copy()
            frame_rgb = band[..., :3] * (1 - to_clay) + clay[..., :3] * to_clay
            frame_a = band[..., 3] * (1 - to_clay) + clay[..., 3] * to_clay
            img = np.dstack([frame_rgb, frame_a]).astype(np.float32)

            # ripple: slow shape-shifting skin wobble
            ph = t * 2.2
            dx = ripple * 22 * (ripple_a * np.cos(ph) + ripple_b * np.sin(ph))
            dy = ripple * 16 * (ripple_b * np.cos(ph + 1) - ripple_a * np.sin(ph + 1))
            # melt: the clay stretches downward from the top (like melting wax), then slides off the bottom
            yy = np.arange(h, dtype=np.float32)[:, None]
            stretch = np.clip(melt * 1.9, 0, 0.93) * col_len[None, :] / 1.55
            slide = (max(0.0, melt - 0.35) ** 1.5) * col_len[None, :] * (H * 1.9)
            dy = dy - (yy * stretch) - slide
            dx = dx + melt * 8 * ripple_a * (1 - melt)
            img = warp(img, dx.astype(np.float32), dy.astype(np.float32))
            if melt > 0:
                # thinning clay: edges stay soft, lower parts get thin and drop away
                al = gaussian_filter(img[..., 3], 1.2)
                img[..., 3] = np.clip((al - 0.25) * 1.9, 0, 1)
                yv = np.arange(h, dtype=np.float32)[:, None] / h
                img[..., 3] *= np.clip(1.0 - 0.9 * melt ** 2 * yv, 0, 1)

            # compose on black with the cyan glow fading as the clay takes over
            canvas = np.zeros((H, W, 3), np.float32)
            gl = (1 - to_clay) * 0.55
            canvas[:, X0:X1] += glow[..., :3] * glow[..., 3:4] * gl
            al = img[..., 3:4]
            canvas[:, X0:X1] = canvas[:, X0:X1] * (1 - al) + img[..., :3] * al
            # fade the final bit to pure black
            fade = 1.0 - ease((t - 4.55) / 0.4)
            canvas *= fade
            Image.fromarray((np.clip(canvas, 0, 1) * 255).astype(np.uint8)).save(os.path.join(tmp, f"f{i:04d}.png"), compress_level=1)

        silent = a.out
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-framerate", str(FPS), "-i", os.path.join(tmp, "f%04d.png"),
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-an", silent], check=True)
        print("wrote", silent)
        sound = silent.replace(".mp4", " (with sound).mp4")
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", silent]
        for p, _, _ in SOUNDS:
            assert os.path.exists(p), p
            cmd += ["-i", p]
        parts = [f"[{k + 1}:a]adelay={int(s * 1000)}:all=1,volume={v}[a{k}]" for k, (_, s, v) in enumerate(SOUNDS)]
        mix = ";".join(parts) + ";" + "".join(f"[a{k}]" for k in range(len(SOUNDS))) + f"amix=inputs={len(SOUNDS)}:normalize=0,atrim=0:5,apad[a]"
        cmd += ["-filter_complex", mix, "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", "5", sound]
        subprocess.run(cmd, check=True)
        print("wrote", sound)


if __name__ == "__main__":
    main()
