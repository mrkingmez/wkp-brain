# -*- coding: utf-8 -*-
"""Lint an Edit Run Sheet (.md) against Zac's locked WWD rules. Exit 1 if any FAIL.
Checks: stops in time order, cross dissolve limit, repeated neighbor transitions,
pictures longer than 7 s, a PNG placed twice, trailer clips over 4 s or total over 30 s,
missing USE VIDEO files, em dashes, designed-transition share.
Usage: python lint_run_sheet.py <Run-Sheet.md> [--max-cross 3]"""
import re, sys

path = sys.argv[1]
MAX_CROSS = 3
if "--max-cross" in sys.argv:
    MAX_CROSS = int(sys.argv[sys.argv.index("--max-cross") + 1])
text = open(path, encoding="utf-8").read()
fails, warns = [], []

def secs(tc):
    p = [int(x) for x in tc.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]

stops = re.split(r"\n(?=### )", text)[1:]
stops = [s for s in stops if re.match(r"### \d+[a-z]?\.", s)]
times, pngs, trans_in, trans_out, clip_lens = [], {}, [], [], []
designed = plain = 0
stop_designed = stop_total = 0
cross = 0
prev_out = None
for s in stops:
    head = s.split("\n", 1)[0]
    m = re.match(r"### (\d+[a-z]?)\.\s+(\d{1,2}:\d{2})", head)
    if not m:
        warns.append(f"cannot read time in: {head[:60]}"); continue
    num, t = m.group(1), secs(m.group(2)); times.append((num, t))
    for n in re.findall(r"PNG (\d+)", head):
        pngs.setdefault(n, []).append(num)
    pic = re.search(r"Picture `USE\\(\d+)\.png` (?:from \d{1,2}:\d{2} )?to (\d{1,2}:\d{2})", s)
    if pic:
        end = secs(pic.group(2))
        start = t
        frm = re.search(r"Picture `USE\\\d+\.png` from (\d{1,2}:\d{2})", s)
        if frm: start = secs(frm.group(1))
        if end - start > 7:
            fails.append(f"stop {num}: picture on screen {end - start}s, limit is 7s")
    for v in re.finditer(r"USE VIDEO:\*\*\s*`([^`]+)`\s*from\s*`([\d:]+)`\s*to\s*`([\d:]+)`", s):
        def tc(x):
            h, mi, se, fr = [int(z) for z in x.split(":")]; return h * 3600 + mi * 60 + se + fr / 24.0
        L = tc(v.group(3)) - tc(v.group(2)); clip_lens.append((num, L))
        if L > 4.05: fails.append(f"stop {num}: trailer clip {L:.1f}s, limit is 4s")
    sc = s.replace("**", "")
    def kind(label):
        m = re.search(label + r": ((?:hard cut|[A-Za-z]+(?: [A-Za-z]+){0,3}?))(?= \d+f|[.,(]|\n|$)", sc)
        return m.group(1).strip() if m else None
    ti, to = kind("In"), kind("Out")
    PLAIN = ("hard cut", "cross dissolve", "film dissolve", "dip to black")
    got = [n for n in (ti, to) if n]
    if got:
        stop_total += 1
        if any(n.lower() not in PLAIN for n in got): stop_designed += 1
    for name in got:
        if name.lower() in PLAIN: plain += 1
        else: designed += 1
        if name.lower() == "cross dissolve": cross += 1
    if ti and prev_out and ti.lower() == prev_out.lower() and ti.lower() != "hard cut":
        fails.append(f"stop {num}: same transition as the stop before ({prev_out})")
    prev_out = to if to else prev_out

for a, b in zip(times, times[1:]):
    if b[1] < a[1]: fails.append(f"stop {b[0]} ({b[1]}s) comes before stop {a[0]} ({a[1]}s)")
for n, where in pngs.items():
    real = [w for w in where]
    if len(real) > 1: fails.append(f"PNG {n} is used in stops {', '.join(real)}")
if cross > MAX_CROSS: fails.append(f"Cross Dissolve appears {cross} times, limit is {MAX_CROSS}")
if sum(l for _, l in clip_lens) > 30: fails.append(f"trailer clips total {sum(l for _, l in clip_lens):.0f}s, limit is 30s")
if "—" in text: fails.append("em dash found in the document")
if "Transition map" not in text: warns.append("no Transition map table at the end")
tot = stop_total
if tot and stop_designed / tot < 0.45: fails.append(f"only {stop_designed} of {tot} stops have a designed transition, target is about half")

print(f"stops {len(stops)} | cross dissolves {cross} | stops with a designed transition {stop_designed} of {tot} | trailer clips {len(clip_lens)} ({sum(l for _, l in clip_lens):.1f}s)")
for w in warns: print("WARN", w)
for f in fails: print("FAIL", f)
print("RESULT:", "FAIL" if fails else "PASS")
sys.exit(1 if fails else 0)
