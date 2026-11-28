# -*- coding: utf-8 -*-
"""Perceptual duplicate check for a picture folder (wwd-pictures, 2026-11-23).
dHash (9x8 gradient, 64 bits) plus normalized correlation of a 32x32 grayscale thumbnail.
Flags pairs with hamming distance < 14 OR correlation > 0.85, for a look by eye.
Alpha is composited on mid grey so padded PNGs compare by picture content.
Usage: python picture_dup_check.py <folder> [<folder2> ...]   (also accepts jpg/png/webp)
Prints every flagged pair and the minimum distance / max correlation seen overall."""
import sys, os, glob, itertools
import numpy as np
from PIL import Image

def load(p):
    im = Image.open(p)
    if im.mode in ("RGBA", "LA"):
        bg = Image.new("RGBA", im.size, (128, 128, 128, 255)); bg.alpha_composite(im.convert("RGBA")); im = bg
    return im.convert("L")

def dhash(g):
    a = np.asarray(g.resize((9, 8), Image.LANCZOS), dtype=np.int16)
    return (a[:, 1:] > a[:, :-1]).flatten()

def corr(g):
    a = np.asarray(g.resize((32, 32), Image.LANCZOS), dtype=np.float64).flatten()
    a -= a.mean(); n = np.linalg.norm(a)
    return a / n if n else a

def main(folders):
    files = []
    for f in folders:
        for e in ("*.png", "*.jpg", "*.jpeg", "*.webp"):
            files += glob.glob(os.path.join(f, e))
    files = sorted(files)
    data = {}
    for p in files:
        g = load(p); data[p] = (dhash(g), corr(g))
    flagged = 0; mind = 99; maxc = -1
    for a, b in itertools.combinations(files, 2):
        d = int((data[a][0] != data[b][0]).sum()); c = float(data[a][1] @ data[b][1])
        mind = min(mind, d); maxc = max(maxc, c)
        if d < 14 or c > 0.85:
            flagged += 1
            print(f"FLAG d={d:2d} corr={c:.3f}  {os.path.basename(a)}  <>  {os.path.basename(b)}")
    print(f"{len(files)} files, {len(files)*(len(files)-1)//2} pairs, flagged {flagged}, min dHash {mind}, max corr {maxc:.3f}")

if __name__ == "__main__":
    main(sys.argv[1:])
