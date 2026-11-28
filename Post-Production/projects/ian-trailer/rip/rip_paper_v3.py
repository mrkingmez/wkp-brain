"""Paper rip v3: a printed photo ripped in half down the middle, with real 3D bending.
Method: each half is a subdivided mesh (paper coordinates s,y). Per row the half rotates about its OUTER
vertical hinge by theta(y); theta ramps from 0 at the crack tip to full above it, so the top fans open into a V
while the bottom is still joined. Along s the paper also curls toward the camera (bend angle grows toward the tear
edge). Vertices are perspective projected, the texture (with torn white fibre edge, different noise per side,
paper grain) is rasterised triangle by triangle with cv2, lit per vertex from the mesh normals (diffuse + gloss).
Free tools only: Python, numpy, opencv-python-headless, Pillow, ffmpeg.

Usage: python rip_paper_v3.py --a A.png --b B.png --out out.mp4 [--frames-dir DIR] [--only 1.2 2.5]
Timing: hold A 1.2 s | tremor 0.2 s | tear travel 0.57 s | tension 0.03 s | snap and exit 0.45 s | B settles to 3.0 s.
"""
import argparse, subprocess, os, math, sys
import numpy as np, cv2
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rip import W, H, FFMPEG, contain, smooth_noise, tear_path, PAPER

FOCAL = 2300.0
RAMP_L = 430.0
TH_TOP = math.radians(46)
LIGHT = np.array([-0.35, -0.45, 0.82]); LIGHT /= np.linalg.norm(LIGHT)
CX, CY = W / 2, H / 2


def ss(x):
    x = np.clip(x, 0, 1)
    return x * x * (3 - 2 * x)


def interp_matrix(npix, ngrid, extent):
    f = (np.arange(npix) + 0.5) / (extent / ngrid)
    f = np.clip(f, 0, ngrid - 1e-6)
    i0 = f.astype(int); w = f - i0
    M = np.zeros((npix, ngrid + 1), np.float32)
    M[np.arange(npix), i0] = 1 - w
    M[np.arange(npix), i0 + 1] = w
    return M


class Half:
    def __init__(self, side, A, base_path, seed):
        self.side = side
        rng = np.random.RandomState(seed)
        extra = smooth_noise(rng, H, 310, 7) + smooth_noise(rng, H, 64, 4.5) + smooth_noise(rng, H, 19, 2.0)
        ys = np.arange(H, dtype=np.float32)
        for _ in range(12):
            c = rng.uniform(0, H); w = rng.uniform(8, 30); a = rng.uniform(-1, 1) * 9
            extra += a * np.clip(1 - np.abs(ys - c) / w, 0, 1)
        micro = smooth_noise(rng, H, 5, 3.0) + smooth_noise(rng, H, 2, 1.6)
        edge = (base_path + extra + micro).astype(np.float32)
        Aor = A
        if side == "R":
            Aor = A[:, ::-1]
            edge = (W - 1) - edge
        self.xL = xL = int(min(W, math.ceil(edge.max()) + 24))
        self.Aor = np.ascontiguousarray(Aor[:, :xL])
        xs = np.arange(xL, dtype=np.float32)[None, :]
        d = edge[:, None] - xs
        wband = (12 + smooth_noise(rng, H, 40, 6) + smooth_noise(rng, H, 8, 3)).clip(3, 26)[:, None]
        fib = rng.uniform(0, 1, (H, xL)).astype(np.float32)
        ragged = d + (fib - .5) * 8 + smooth_noise(rng, H, 3, 2.8)[:, None]
        self.ragged = ragged.astype(np.float32)
        t1 = np.clip((wband - d) / 3.5 + (fib - .5) * 1.0, 0, 1)
        t2 = np.clip((wband * 1.9 - d) / 11.0 + (fib - .5) * 1.2, 0, 1) * .6
        white = np.clip(np.maximum(t1, t2), 0, 1)[..., None]
        # paper grain: fine noise, soft blotches, horizontal fibres
        n1 = rng.normal(0, 1, (H, xL)).astype(np.float32)
        n2 = cv2.GaussianBlur(rng.normal(0, 1, (H, xL)).astype(np.float32), (0, 0), 7); n2 /= n2.std()
        n3 = cv2.GaussianBlur(rng.normal(0, 1, (H, xL)).astype(np.float32), (0, 0), sigmaX=16, sigmaY=0.8); n3 /= n3.std()
        grain = (1 + 0.010 * n1 + 0.012 * n2 + 0.010 * n3)[..., None].astype(np.float32)
        paper = PAPER * (0.94 + 0.06 * rng.uniform(0, 1, (H, xL, 1)).astype(np.float32))
        self.torn_rgb = (self.Aor * (1 - white) + paper * white) * grain
        self.plain_rgb = self.Aor * grain
        self.nx = max(8, xL // 32); self.ny = H // 30
        self.sg = np.linspace(0, xL, self.nx + 1)
        self.yg = np.linspace(0, H, self.ny + 1)
        self.Wx = interp_matrix(xL, self.nx, xL)
        self.Wy = interp_matrix(H, self.ny, H)

    def render(self, st):
        xL, nx, ny = self.xL, self.nx, self.ny
        yg, sg = self.yg, self.sg
        o = ss((st["tip"] - np.arange(H)) / 50.0).astype(np.float32)[:, None, None]
        rgb = self.plain_rgb + (self.torn_rgb - self.plain_rgb) * o
        al = np.clip(self.ragged + .5 + (1 - o[..., 0]) * 14, 0, 1)
        # mesh geometry
        ramp = ss((st["tip"] - yg) / RAMP_L)
        ramp = ramp * (1 - st["r"]) + st["r"]
        th = st["thtop"] * ramp + st["trem"] * (1 - yg / H)
        alpha = th[:, None] * (0.4 + 0.6 * sg[None, :] / xL)
        ds = np.diff(sg)[None, :]
        X = np.concatenate([np.zeros((ny + 1, 1)), np.cumsum(0.5 * (np.cos(alpha[:, :-1]) + np.cos(alpha[:, 1:])) * ds, 1)], 1)
        Z = np.concatenate([np.zeros((ny + 1, 1)), np.cumsum(0.5 * (np.sin(alpha[:, :-1]) + np.sin(alpha[:, 1:])) * ds, 1)], 1)
        Ti = st["Tbase"] * ramp
        Xw = X - Ti[:, None]
        Yw = np.repeat(yg[:, None], nx + 1, 1)
        # normals and lighting
        dPds = np.stack([np.gradient(Xw, sg, axis=1), np.gradient(Yw, sg, axis=1), np.gradient(Z, sg, axis=1)], -1)
        dPdy = np.stack([np.gradient(Xw, yg, axis=0), np.gradient(Yw, yg, axis=0), np.gradient(Z, yg, axis=0)], -1)
        n = np.cross(dPds, dPdy); n /= np.linalg.norm(n, axis=-1, keepdims=True) + 1e-9
        lx = -0.35 if self.side == "L" else 0.35
        Lv = np.array([lx, -0.45, 0.82]); Lv /= np.linalg.norm(Lv)
        diff = np.clip(n @ Lv, 0, 1) / Lv[2]
        shade = 0.60 + 0.40 * np.clip(diff, 0, 1.15)
        Hv = Lv + np.array([0, 0, 1.0]); Hv /= np.linalg.norm(Hv)
        spec = np.clip(n @ Hv, 0, 1) ** 28 - (Hv[2] ** 28)
        spec = np.clip(spec, 0, None) * 0.55
        shade_f = (self.Wy @ shade.astype(np.float32) @ self.Wx.T)[..., None]
        spec_f = (self.Wy @ spec.astype(np.float32) @ self.Wx.T)[..., None]
        out_rgb = np.clip(rgb * shade_f + 255 * spec_f * 0.8, 0, 255)
        tex = np.concatenate([out_rgb * al[..., None], al[..., None] * 255], -1).astype(np.float32)
        P = 2
        tex = cv2.copyMakeBorder(tex, P, P, P, P, cv2.BORDER_CONSTANT, value=(0, 0, 0, 0))
        # projection
        k = FOCAL / np.clip(FOCAL - Z, 200, None)
        SX = CX + (Xw - CX) * k
        SY = CY + (Yw - CY) * k
        if st["psi"]:
            c, s_ = math.cos(st["psi"]), math.sin(st["psi"])
            cxh = W / 4 - st["Tbase"] * 0.5
            dx, dy = SX - cxh, SY - CY
            SX = cxh + c * dx - s_ * dy
            SY = CY + s_ * dx + c * dy
        canvas = np.zeros((H, W, 4), np.float32)
        TXs = sg + P
        TYs = yg + P
        for i in range(ny):
            for j in range(nx):
                q = [(i, j), (i, j + 1), (i + 1, j + 1), (i + 1, j)]
                for tri in ((0, 1, 2), (0, 2, 3)):
                    idx = [q[m] for m in tri]
                    dst = np.array([[SX[a, b], SY[a, b]] for a, b in idx], np.float32)
                    x0 = int(math.floor(dst[:, 0].min())) - 2; x1 = int(math.ceil(dst[:, 0].max())) + 3
                    y0 = int(math.floor(dst[:, 1].min())) - 2; y1 = int(math.ceil(dst[:, 1].max())) + 3
                    x0c, y0c, x1c, y1c = max(x0, 0), max(y0, 0), min(x1, W), min(y1, H)
                    if x1c <= x0c or y1c <= y0c:
                        continue
                    src = np.array([[TXs[b], TYs[a]] for a, b in idx], np.float32)
                    M = cv2.getAffineTransform(src, dst - np.array([x0c, y0c], np.float32))
                    w_, h_ = x1c - x0c, y1c - y0c
                    patch = cv2.warpAffine(tex, M, (w_, h_), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
                    cen = dst.mean(0)
                    v = dst - cen
                    nv = np.linalg.norm(v, axis=1, keepdims=True) + 1e-6
                    ex = (cen + v + 0.9 * v / nv - np.array([x0c, y0c])) * 16
                    mask = np.zeros((h_, w_), np.uint8)
                    cv2.fillConvexPoly(mask, ex.astype(np.int32), 1, lineType=cv2.LINE_8, shift=4)
                    m = mask.astype(bool)
                    sub = canvas[y0c:y1c, x0c:x1c]
                    sub[m] = patch[m]
        if self.side == "R":
            canvas = canvas[:, ::-1]
        return np.ascontiguousarray(canvas), float(Z.max())


def params(t, hold=1.2):
    tp = t - hold
    st = dict(tip=-2000.0, thtop=TH_TOP, r=0.0, Tbase=0.0, psi=0.0, trem=0.0, active=True, shake=(0.0, 0.0), bscale=1.0, jx=0.0)
    if tp <= 0:
        return st
    if tp < 0.2:  # hands grab: tiny flutter and slight bend of the top
        env = ss(tp / 0.05)
        st["trem"] = math.radians(2.6) * env * (0.55 + 0.45 * math.sin(2 * math.pi * 26 * tp))
        st["jx"] = 1.0 * env
        return st
    ph = (tp - 0.2) / 0.57
    if tp < 0.77:
        u = min(ph, 1.0) ** 1.25
        st["tip"] = -30 + (H + 60) * u
        st["thtop"] = TH_TOP * float(ss(ph / 0.9))
        st["Tbase"] = 70 * float(ss(ph))
        st["trem"] = math.radians(2.6) * (1 - float(ss(ph * 4)))
        st["jx"] = 0.0
        return st
    if tp < 0.80:  # tension, last fibres
        st["tip"] = H + 30 + (tp - 0.77) * 150
        st["Tbase"] = 70 + 8 * (tp - 0.77) / 0.03
        st["thtop"] = TH_TOP
        return st
    s = tp - 0.80
    if s > 0.5:
        st["active"] = False
        st["bscale"] = 1.0 + 0.02 * (1 - float(ss(s / 0.9))) * 1.0
        return st
    st["tip"] = H + 200
    st["r"] = float(ss(s / 0.08))
    jerk = -math.radians(4) * math.sin(math.pi * min(s / 0.05, 1)) if s < 0.05 else 0.0
    st["thtop"] = TH_TOP + math.radians(30) * float(ss(s / 0.4)) + jerk
    st["Tbase"] = 78 + 1500 * (s / 0.45) ** 2
    st["psi"] = math.radians(7) * float(ss(s / 0.4))
    st["trem"] = 0.0
    st["bscale"] = 1.0 + 0.02 * (1 - float(ss(s / 0.9)))
    if s < 0.10:
        env = math.exp(-s / 0.03)
        st["shake"] = (5 * env, 4 * env)
    return st


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True); ap.add_argument("--b", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--tear-x", type=float, default=0.5)
    ap.add_argument("--fps", type=int, default=24)
    ap.add_argument("--total", type=float, default=3.0)
    ap.add_argument("--frames-dir", default=None)
    ap.add_argument("--only", type=float, nargs=2, default=None)
    a = ap.parse_args()
    A, B = contain(a.a), contain(a.b)
    base = tear_path(np.random.RandomState(a.seed), a.tear_x, 0.0, 14)
    halves = {"L": Half("L", A, base, a.seed + 1), "R": Half("R", A, base, a.seed + 2)}
    Bf = np.ascontiguousarray(B.astype(np.float32))
    cache = {}

    def comp_one(t):
        st = params(t)
        M = np.array([[st["bscale"], 0, CX * (1 - st["bscale"])], [0, st["bscale"], CY * (1 - st["bscale"])]], np.float32)
        frame = cv2.warpAffine(Bf, M, (W, H), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE) if st["bscale"] != 1.0 else Bf.copy()
        if st["active"]:
            res = {s: halves[s].render(st) for s in ("L", "R")}
            lift = max(0.0, min(1.0, max(res["L"][1], res["R"][1]) / 450.0))
            for s in ("L", "R"):
                cv = res[s][0]
                sh = cv2.GaussianBlur(cv[..., 3] / 255.0, (0, 0), 24)
                M2 = np.float32([[1, 0, (22 if s == "R" else -10) * (0.4 + lift)], [0, 1, 30 * (0.4 + lift)]])
                sh = cv2.warpAffine(sh, M2, (W, H)) * 0.5 * min(1.0, lift * 2)
                frame = frame * (1 - sh[..., None])
            for s in ("L", "R"):
                cv = res[s][0]
                frame = cv[..., :3] + (1 - cv[..., 3:4] / 255.0) * frame
        sx, sy = st["shake"]
        sx += st["jx"] * np.random.RandomState(int(t * 1000)).uniform(-1, 1)
        if sx or sy:
            frame = cv2.warpAffine(frame, np.float32([[1, 0, sx], [0, 1, sy]]), (W, H), borderMode=cv2.BORDER_REPLICATE)
        return frame

    n = int(round(a.total * a.fps))
    if a.frames_dir:
        os.makedirs(a.frames_dir, exist_ok=True)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    ff = subprocess.Popen([FFMPEG, "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(a.fps),
                           "-i", "-", "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p", "-r", str(a.fps),
                           "-movflags", "+faststart", a.out], stdin=subprocess.PIPE)
    for f in range(n):
        t = f / a.fps
        if a.only and not (a.only[0] <= t <= a.only[1]):
            frame = comp_one(1.0)
        elif t < 1.2:
            if "hold" not in cache:
                cache["hold"] = comp_one(1.0)
            frame = cache["hold"]
        else:
            if 1.2 + 0.77 - 1 / 24 <= t <= 1.2 + 0.80 + 0.5:  # snap: shutter blur, 20 sub-samples over 0.6 frame
                subs = [t - (0.6 / 24) * (1 - (k + 0.5) / 20) for k in range(20)]
                frame = np.mean([comp_one(x) for x in subs], 0)
            else:
                frame = comp_one(t)
        out = np.clip(frame, 0, 255).astype(np.uint8)
        if a.frames_dir:
            cv2.imwrite(os.path.join(a.frames_dir, f"f{f:03d}.png"), out[..., ::-1])
        ff.stdin.write(out.tobytes())
        print("frame", f, flush=True)
    ff.stdin.close(); ff.wait()
    print("rendered", a.out, n)


if __name__ == "__main__":
    main()
