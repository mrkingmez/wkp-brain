"""Vision Quest opener from Zac's Firefly clips (2026-10-23): boot panel clip -> world clip, my own VISIONQUEST title over the
world (Firefly garbled the title as BIOME, so title.mp4 is NOT used), beeps/sweep/whoosh, white flash out.

  python make_vq_firefly_opener.py [--dir <Firefly refs folder>] [--out "P:\\WWD Kit\\Vision Quest\\Opener - Firefly.mov"]
"""
import argparse
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_arcade_kit import W, H, FPS, put, ease_out  # noqa: E402
import make_wk_kit_cl_vq as kit  # noqa: E402

SFX = "P:\\Sounds\\Sound FX\\"
SWEEP = SFX + "jg-032316-sfx-sci-fi-sweep-1.mp3"
WHOOSH = SFX + "deep-fast-whoosh_GyZDnHNu.mp3"
DEFAULT_DIR = (r"L:\Winter Wolfs Den review show\Raw Footage\mass record crystal LAke Vision Quest"
               r"\Vision Quest ep 1 and 2\Firefly refs")
BOOT_LEN, XF, WORLD_LEN = 6.6, 0.6, 5.5   # OPERATION COMPLETE shows at about 5.0 s in the boot clip, so hold to 6.0 before the cut
TOTAL = BOOT_LEN + WORLD_LEN - XF          # 11.5 s
TITLE_AT, FLASH_AT = 8.4, TOTAL - 0.4
CYAN = (90, 225, 255)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=DEFAULT_DIR)
    ap.add_argument("--out", default=r"P:\WWD Kit\Vision Quest\Opener - Firefly.mov")
    a = ap.parse_args()
    boot = os.path.join(a.dir, "the4 boot panel.mp4")
    world = os.path.join(a.dir, "World.mp4")
    for p in (boot, world, SWEEP, WHOOSH):
        assert os.path.exists(p), p
    n = int(round(TOTAL * FPS))
    tfont = kit.font(kit.IMPACT, 200)
    with tempfile.TemporaryDirectory() as tmp:
        for i in range(n):
            t = i / FPS
            cv = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            if t >= TITLE_AT:
                ts = ease_out((t - TITLE_AT) / 0.8)
                flick = 1.0 if (i % 7) < 5 else 0.6
                ti = Image.new("RGBA", (1800, 280), (0, 0, 0, 0))
                ImageDraw.Draw(ti).text((900, 140), "VISIONQUEST", font=tfont, fill=CYAN + (int(255 * flick),), anchor="mm",
                                        stroke_width=5, stroke_fill=(0, 30, 50, 255))
                gl = ti.filter(ImageFilter.GaussianBlur(16))
                s = 0.7 + 0.3 * ts
                put(cv, gl, W / 2, 470, scale=s, alpha=min(1.0, ts))
                put(cv, ti, W / 2, 470, scale=s, alpha=min(1.0, ts))
            if t >= FLASH_AT:
                k = min(1.0, (t - FLASH_AT) / 0.3)
                cv.alpha_composite(Image.new("RGBA", (W, H), (255, 255, 255, int(255 * k))))
            cv.save(os.path.join(tmp, f"t{i:04d}.png"), compress_level=1)
        fc = (f"[0:v]trim=0:{BOOT_LEN},setpts=PTS-STARTPTS,fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1[b];"
              f"[1:v]trim=0:{WORLD_LEN},setpts=PTS-STARTPTS,fps={FPS},scale={W}:{H}:flags=lanczos,setsar=1[w];"
              f"[b][w]xfade=transition=pixelize:duration={XF}:offset={BOOT_LEN - XF}[bw];"
              f"[bw][2:v]overlay=format=auto[v];"
              f"[3:a]adelay=0:all=1,volume=0.5[a0];[4:a]adelay=1500:all=1,volume=0.35[a1];"
              f"[5:a]adelay={int((BOOT_LEN - XF - 0.6) * 1000)}:all=1,volume=0.8[a2];"
              f"[6:a]adelay={int(FLASH_AT * 1000 - 200)}:all=1,volume=0.9[a3];"
              f"[a0][a1][a2][a3]amix=inputs=4:normalize=0,apad[a]")
        cmd = ["ffmpeg", "-v", "error", "-y", "-i", boot, "-i", world,
               "-framerate", str(FPS), "-i", os.path.join(tmp, "t%04d.png"),
               "-i", kit.GLITCH, "-i", kit.COMP, "-i", SWEEP, "-i", WHOOSH,
               "-filter_complex", fc, "-map", "[v]", "-map", "[a]",
               "-c:v", "prores_ks", "-profile:v", "3", "-pix_fmt", "yuv422p10le",
               "-c:a", "pcm_s16le", "-ar", "48000", "-t", f"{TOTAL:.3f}", a.out]
        subprocess.run(cmd, check=True)
    print("wrote", a.out)


if __name__ == "__main__":
    main()
