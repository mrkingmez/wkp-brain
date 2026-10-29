"""Crop-tolerant twin check: trims black bars by row/col mean, then compares 24x14 gray + RGB hist.
Usage: dup_check2.py <new_dir> [<old_dir>...]. Flags corr>0.9 on trimmed gray thumbs OR hist-intersection>0.9 with corr>0.6."""
import sys,os,numpy as np
from PIL import Image
def trim(im):
    a=np.asarray(im.convert('L'),dtype=float)
    r=np.where(a.mean(1)>10)[0]; c=np.where(a.mean(0)>10)[0]
    if len(r)>50 and len(c)>50: im=im.crop((c[0],r[0],c[-1]+1,r[-1]+1))
    return im
def feat(p):
    im=trim(Image.open(p).convert('RGB'))
    g=np.asarray(im.convert('L').resize((24,14),Image.LANCZOS),dtype=float).flatten()
    g=(g-g.mean())/(g.std()+1e-6)
    h=np.histogram(np.asarray(im.resize((64,36))).reshape(-1,3).mean(1),bins=16,range=(0,256))[0].astype(float); h/=h.sum()
    return g,h
F={}
for i,d in enumerate(sys.argv[1:]):
    for f in os.listdir(d):
        if f.endswith('.png'): F[('new' if i==0 else 'old%d'%i,f)]=feat(os.path.join(d,f))
K=list(F); out=[]
for i,a in enumerate(K):
    for b in K[i+1:]:
        if a[0]!='new' and b[0]!='new': continue
        c=float((F[a][0]*F[b][0]).mean()); hi=float(np.minimum(F[a][1],F[b][1]).sum())
        if c>0.9 or (c>0.7 and hi>0.9): out.append((a,b,round(c,3),round(hi,3)))
for o in out: print(o)
print("flagged",len(out),"of",len(K),"images")
