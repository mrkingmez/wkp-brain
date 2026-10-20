"""Two original 8-bit fighters trade blows, transparent background, hit sounds baked in.
  python make_pixel_fight.py [--out "P:\\WWD Kit\\Street Fighter\\Pixel Fight.mov"]
Own characters and moves (not any game's sprites). Drawn on a 240x135 grid, scaled up with nearest neighbor.
"""
import argparse, importlib.util, os
from PIL import Image, ImageDraw, ImageFont, ImageChops

LW, LH, GY = 240, 135, 125
spec = importlib.util.spec_from_file_location("ak", os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_arcade_kit.py"))
ak = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ak)

PA = dict(skin=(240, 190, 140), top=(30, 90, 220), pants=(235, 235, 235), hair=(40, 25, 15), band=(230, 40, 40), shoe=(200, 30, 30), belt=(20, 20, 20), eye=(0, 0, 0))
PB = dict(skin=(190, 130, 90), top=(200, 30, 40), pants=(35, 35, 50), hair=(250, 210, 60), band=(40, 200, 90), shoe=(240, 240, 240), belt=(240, 200, 40), eye=(0, 0, 0))

POSES = {
    "idle": dict(lean=0, fa=(8, -2), ba=(5, 3), ff=(7, 0), bf=(-6, 0)),
    "punchw": dict(lean=2, fa=(10, -1), ba=(4, 3), ff=(8, 0), bf=(-7, 0)),
    "punch": dict(lean=3, fa=(21, 0), ba=(4, 3), ff=(9, 0), bf=(-7, 0)),
    "kickw": dict(lean=-1, fa=(8, -3), ba=(4, 2), ff=(10, 6), bf=(-6, 0)),
    "kick": dict(lean=-3, fa=(6, -4), ba=(2, 3), ff=(25, 11), bf=(-6, 0)),
    "hit": dict(lean=-6, fa=(-3, 5), ba=(-5, 6), ff=(4, 0), bf=(-9, 0)),
    "air": dict(lean=-7, fa=(-4, 6), ba=(-6, 6), ff=(2, 4), bf=(-9, 6)),
    "victory": dict(lean=0, fa=(5, -15), ba=(-5, -15), ff=(6, 3), bf=(-6, 3)),
    "walka": dict(lean=0, fa=(8, -2), ba=(5, 3), ff=(7, 3), bf=(-6, 0)),
    "walkb": dict(lean=0, fa=(8, -2), ba=(5, 3), ff=(3, 0), bf=(-8, 3)),
}


def R(d, x0, y0, x1, y1, c):
    d.rectangle([int(round(min(x0, x1))), int(round(min(y0, y1))), int(round(max(x0, x1))), int(round(max(y0, y1)))], fill=c)


def fighter(d, cx, gy, face, pose, pal, flash=False):
    if flash:
        pal = {k: (255, 255, 255) for k in pal}
    S = lambda x: cx + face * x
    p = POSES[pose]
    ln = p["lean"]
    sh = (S(ln + 1), gy - 31)
    hip = (S(ln * 0.4), gy - 17)
    # back arm and back leg
    ba = (S(ln + 1 + p["ba"][0]), sh[1] + p["ba"][1])
    d.line([sh, ba], fill=pal["top"], width=4)
    R(d, ba[0] - 2, ba[1] - 2, ba[0] + 1, ba[1] + 1, pal["skin"])
    bf = (S(p["bf"][0]), gy - p["bf"][1] - 1)
    d.line([hip, bf], fill=pal["pants"], width=5)
    R(d, bf[0] - 3, bf[1] - 1, bf[0] + 3, bf[1] + 1, pal["shoe"])
    # torso
    d.polygon([(S(ln - 6), gy - 33), (S(ln + 6), gy - 33), (S(ln * 0.4 + 5), gy - 17), (S(ln * 0.4 - 5), gy - 17)], fill=pal["top"])
    R(d, S(ln * 0.4 - 5), gy - 19, S(ln * 0.4 + 5), gy - 17, pal["belt"])
    # front leg
    ff = (S(p["ff"][0]), gy - p["ff"][1] - 1)
    d.line([hip, ff], fill=pal["pants"], width=5)
    R(d, ff[0] - 3, ff[1] - 1, ff[0] + 3, ff[1] + 1, pal["shoe"])
    # head
    R(d, S(ln - 5), gy - 44, S(ln + 5), gy - 34, pal["skin"])
    R(d, S(ln - 5), gy - 46, S(ln + 5), gy - 42, pal["hair"])
    R(d, S(ln - 5), gy - 46, S(ln - 3), gy - 36, pal["hair"])
    R(d, S(ln - 5), gy - 42, S(ln + 5), gy - 40, pal["band"])
    R(d, S(ln + 2), gy - 39, S(ln + 3), gy - 37, pal["eye"])
    # front arm
    fa = (S(ln + 1 + p["fa"][0]), sh[1] + p["fa"][1])
    d.line([sh, fa], fill=pal["top"], width=4)
    R(d, fa[0] - 2, fa[1] - 2, fa[0] + 2, fa[1] + 2, pal["skin"])


def lying(d, cx, gy, face, pal):
    S = lambda x: cx + face * x
    R(d, S(8), gy - 8, S(26), gy - 2, pal["pants"])
    R(d, S(25), gy - 6, S(29), gy - 1, pal["shoe"])
    R(d, S(-18), gy - 9, S(8), gy - 1, pal["top"])
    R(d, S(-28), gy - 11, S(-17), gy - 1, pal["skin"])
    R(d, S(-28), gy - 11, S(-24), gy - 1, pal["hair"])
    R(d, S(-24), gy - 11, S(-22), gy - 1, pal["band"])


def spark(d, x, y, big):
    r = 7 if big else 4
    c, w = (255, 240, 120), (255, 255, 255)
    R(d, x - 1, y - r, x + 1, y + r, c)
    R(d, x - r, y - 1, x + r, y + 1, c)
    for k in range(2, r):
        for sx in (-1, 1):
            for sy in (-1, 1):
                d.point((x + sx * k, y + sy * k), fill=c)
    R(d, x - 1, y - 1, x + 1, y + 1, w)


A_T = {8: "punchw", 9: "punch", 10: "punch", 15: "hit", 16: "hit", 19: "kickw", 20: "kick", 21: "kick",
       25: "hit", 26: "hit", 27: "punchw", 28: "punch", 29: "punch", 30: "kickw", 31: "kick", 32: "kick"}
B_T = {10: "hit", 11: "hit", 13: "punchw", 14: "punch", 15: "punch", 21: "hit", 22: "hit", 23: "kickw",
       24: "kick", 25: "kick", 27: "punchw", 28: "punch", 29: "punch"}
SPARKS = {10: (-30, False), 15: (-30, False), 21: (-19, False), 25: (-19, False), 28: (-30, True), 32: (-20, True)}
HITS = [(10, ak.PUNCH, 1.0), (15, ak.PUNCH, 1.0), (21, ak.SFX + "Adobe\\Impacts\\Impact Body Punch 01.wav", 1.0),
        (25, ak.SFX + "Adobe\\Impacts\\Impact Body Punch 01.wav", 1.0), (28, ak.PUNCH_HARD, 1.0), (32, ak.PUNCH_HARD, 1.0),
        (36, ak.GONG, 0.5)]
FONT_KO = ImageFont.load_default(size=30)


def frame(i):
    t = min(i * 12 // 30, 47)
    im = Image.new("RGBA", (LW, LH), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.fontmode = "1"
    d.fontmode = "1"
    # positions
    ax = 60 + 44 * min(t, 5) / 5
    bx = 180 - 44 * min(t, 5) / 5
    pa = A_T.get(t) or ("walka" if t < 6 and t % 2 else "walkb" if t < 6 else "idle")
    pb = B_T.get(t) or ("walka" if t < 6 and t % 2 else "walkb" if t < 6 else "idle")
    ya = yb = 0
    if pa == "hit":
        ax -= 4 if t in (15, 25) else 2
    if pb == "hit":
        bx += 4 if t in (10, 21) else 2
    if 28 <= t <= 29:
        ax -= 2
        bx += 2
    flash_a, flash_b = pa == "hit" and t in (15, 25), pb == "hit" and t in (10, 21)
    ko = False
    if 32 <= t <= 35:
        pb = "air"
        bx += 8 * (t - 31)
        yb = [10, 16, 12, 4][t - 32]
        flash_b = t == 32
    elif t >= 36:
        ko = True
        bx += 8 * 4
    if t >= 37:
        pa = "victory"
        ya = [6, 12, 16, 12, 6, 0, 6, 12, 16, 12, 6, 0][(t - 37) % 12]
    fighter(d, ax, GY - ya, 1, pa, PA, flash_a)
    if ko:
        lying(d, bx, GY, -1, PB)
    else:
        fighter(d, bx, GY - yb, -1, pb, PB, flash_b)
    if t in SPARKS and (i * 12 // 30 == t):
        dy, big = SPARKS[t]
        first = (i * 12 % 30) < 15 or True
        spark(d, int((ax + bx) / 2), GY + dy, big)
    if t >= 36:
        d.text((LW // 2, 30), "K.O.", font=FONT_KO, fill=(255, 230, 60), anchor="mm")
    if 32 <= t <= 34:
        im = ImageChops.offset(im, 2 if t % 2 else -2, 0)
    return im.resize((1920, 1080), Image.NEAREST)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=r"P:\WWD Kit\Street Fighter\Pixel Fight.mov")
    a = ap.parse_args()
    audio = [(p, int(tk * 1000 / 12), v) for tk, p, v in HITS]
    ak.render(frame, 120, a.out, audio)


if __name__ == "__main__":
    main()
