import re, glob, os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
from quotes import Q

T = {}
for f in glob.glob(r'D:/WKP/Shattered-Empire/third_draft/work/text/*.txt'):
    k = os.path.basename(f).replace('.txt', '')
    T[k] = open(f, encoding='utf-8', errors='replace').read()


def norm(s):
    s = (s.replace('\u2019', "'").replace('\u2018', "'").replace('\u201c', '"')
         .replace('\u201d', '"').replace('\u2026', '...'))
    return re.sub(r'\s+', ' ', s)


NT = {k: norm(v) for k, v in T.items()}
bad = 0
for ch, lst in Q.items():
    for q, c in lst:
        key = 'ch_00_prologue' if c == '00' else ('ch_99_epilogue' if c == '99' else 'ch_%02d' % int(c))
        nq = norm(q)
        hit = [k for k, v in NT.items() if nq in v]
        if key in hit:
            continue
        bad += 1
        print('MISS', ch, c, q[:70], '| found in', hit[:3])
print('misses', bad)
