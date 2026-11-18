"""Perceptual twin check for a USE folder (wwd-pictures, STANDARDS addendum).
Usage: dup_check3.py <dir> [<dir2> ...]   (PNG/JPG, alpha padding is trimmed first)
Prints every pair with dHash (64-bit) Hamming distance < 14 OR 24x14 gray correlation > 0.85, plus the lowest distance and highest correlation seen.
Flagged pairs must be looked at by eye."""
import sys,os,numpy as np
from PIL import Image
def load(p):
    im=Image.open(p).convert('RGBA'); bb=im.getchannel('A').point(lambda v:255 if v>8 else 0).getbbox()
    if bb: im=im.crop(bb)
    return im.convert('RGB')
def feats(p):
    im=load(p); g=im.convert('L')
    a=np.asarray(g.resize((9,8),Image.LANCZOS),dtype=float); dh=(a[:,1:]>a[:,:-1]).flatten()
    c=np.asarray(g.resize((24,14),Image.LANCZOS),dtype=float).flatten(); c=(c-c.mean())/(c.std()+1e-6)
    return dh,c
F={}
for d in sys.argv[1:]:
    for f in sorted(os.listdir(d)):
        if f.lower().endswith(('.png','.jpg','.jpeg')): F[os.path.join(os.path.basename(d),f)]=feats(os.path.join(d,f))
K=list(F); flagged=[]; mind=999; maxc=-1
for i,a in enumerate(K):
    for b in K[i+1:]:
        dist=int((F[a][0]!=F[b][0]).sum()); cor=float((F[a][1]*F[b][1]).mean())
        mind=min(mind,dist); maxc=max(maxc,cor)
        if dist<14 or cor>0.85: flagged.append((a,b,dist,round(cor,3)))
for x in flagged: print("FLAG",x)
print("images",len(K),"pairs",len(K)*(len(K)-1)//2,"flagged",len(flagged),"min dHash dist",mind,"max corr",round(maxc,3))
