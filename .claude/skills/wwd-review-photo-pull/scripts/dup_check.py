"""dHash + downscaled correlation near-twin check. Usage: dup_check.py <set_dir> [<other_dir> ...]
First dir = the new set. Reports pairs within it and between it and the others. dHash dist <14 or corr >0.85."""
import sys, os, numpy as np
from PIL import Image
def load(d,tag):
    out={}
    for f in sorted(os.listdir(d), key=lambda x:(len(x),x)):
        if f.lower().endswith('.png'):
            im=Image.open(os.path.join(d,f)).convert('L')
            m=im.point(lambda v:255 if v>12 else 0); bb=m.getbbox()
            if bb and (bb[2]-bb[0])>200 and (bb[3]-bb[1])>200: im=im.crop(bb)
            a=np.asarray(im.resize((9,8),Image.LANCZOS),dtype=float)
            h=(a[:,1:]>a[:,:-1]).flatten()
            g=np.asarray(im.resize((32,18),Image.LANCZOS),dtype=float).flatten()
            g=(g-g.mean())/(g.std()+1e-6)
            out[(tag,f)]=(h,g)
    return out
dirs=sys.argv[1:]
sets=[load(d,'new' if i==0 else 'old%d'%i) for i,d in enumerate(dirs)]
new=sets[0]; keys=list(new)
def rep(a,b):
    d=int((new[a][0]!=(S[b][0])).sum()) if False else None
res=[]
allk={}
for s in sets: allk.update(s)
for i,a in enumerate(keys):
    for b in allk:
        if b==a: continue
        if b in new and keys.index(b)<=i: continue
        d=int((allk[a][0]!=allk[b][0]).sum()); c=float((allk[a][1]*allk[b][1]).mean())
        if d<14 or c>0.85: res.append((a,b,d,c))
print("images:",[len(s) for s in sets])
for a,b,d,c in res: print(a,b,"dist",d,"corr",round(c,3))
print("pairs flagged:",len(res))
