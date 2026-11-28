"""One-off freezer: copies the real prompt logs into tests/fixtures/ and writes MANIFEST.json.
Run it again only on purpose (it overwrites the frozen copies). Reads, never edits, the log files.
Paths come from the repo root found from this file's location."""
import json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
LOG = "data/firefly-prompt-log/"
FIX = os.path.join(HERE, "fixtures")


def rd(rel):
    return open(os.path.join(ROOT, rel), encoding="utf-8").read()


def paras(t):
    return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]


F = []   # failed + known_conflict entries


def add(id_, rel, kind, engine, start, flag, fail, text, note, setname="failed", allow_impact=False, end="no", extra=None):
    e = dict(id=id_, source=rel, kind=kind, engine=engine, start_frame=start, end_frame=end, allow_impact=allow_impact,
             text=text, zac_note=note, must_flag=flag, must_fail=fail, set=setname)
    if extra:
        e.update(extra)
    F.append(e)


singles = [
    ("G1", "Video one", "no", ["PF02", "R1"], ["R1"]),
    ("G2", "Video 2", "no", ["PF11"], ["PF11"]),
    ("G3", "Video 3", "no", ["PF11"], ["PF11"]),
    ("G4", "Video 4", "yes", ["R1"], ["R1"]),
    ("G5", "Video 5", "yes", ["R1"], []),
    ("G6", "Video 6", "no", ["PF04", "PF05", "PF06"], ["PF04", "PF05"]),
    ("G7", "video 7", "no", ["R1", "R2"], ["R1", "R2"]),
    ("G8", "video 8", "no", ["R1", "R2"], ["R1", "R2"]),
    ("G9", "video 9", "no", ["PF04"], ["PF04"]),
    ("G10", "video 10", "no", ["PF04"], ["PF04"]),
    ("G11", "video 11", "yes", ["PF12"], []),
    ("G12", "video 12", "no", ["R9", "PF03"], ["R9"]),
    ("G13", "Video 13", "no", ["R7", "PF13"], ["R7"]),
]
for gid, d, start, flag, fail in singles:
    rel = LOG + d + "/prompt and notes.txt"
    ps = paras(rd(rel))
    add(gid, rel, "video", "veo", start, flag, fail, ps[0], "\n\n".join(ps[1:]),
        setname="known_conflict" if gid == "G5" else "failed")

for jid, d in (("J2", "Video 2"), ("J3", "Video 3"), ("J4", "Video 4"), ("J5", "Video 5")):
    rel = LOG + "Joust opener/" + d + "/prompt and notes.txt"
    ps = paras(rd(rel))
    fail = ["R1", "PF10"] if jid == "J4" else ["R1"]
    add(jid, rel, "video", "veo", "no", ["PF10", "PF14", "R1"], fail, ps[0], "\n\n".join(ps[1:]), allow_impact=True)

bigrel = LOG + "Joust opener/prompt and notes for all the rest this was very time consuming.txt"
k, cur = 0, None
for p in paras(rd(bigrel)):
    if p.startswith("First-person") or p.startswith("Animate"):
        k += 1
        cur = dict(id="JS%d" % k, text=p, notes=[])
        F.append(dict(id=cur["id"], source=bigrel, kind="video", engine="veo", start_frame="yes", end_frame="no",
                      allow_impact=True, text=p, zac_note="", must_flag=["R1", "PF10", "PF14"], must_fail=["R1"], set="failed"))
        cur = F[-1]
    elif cur is not None:
        cur["zac_note"] = (cur["zac_note"] + "\n\n" + p).strip()
js2 = next(e for e in F if e["id"] == "JS2")
F.append(dict(id="JS2-nostart", source=bigrel, kind="video", engine="veo", start_frame="no", end_frame="no", allow_impact=True,
              text=js2["text"], zac_note="(synthetic: JS2 text with START_FRAME no, to exercise PF09)", must_flag=["PF09"],
              must_fail=["PF09"], set="failed"))

# good set: frozen copies
good = []
for rel, name in (("data/firefly-prompt-guide/REBUILT-PROMPTS-2026-11-22.md", "rebuilt-prompts.md"),
                  ("WWD/reports/PJ-Intro-Firefly-Prompts-2026-11-23.md", "pj-intro-prompts.md")):
    shutil.copyfile(os.path.join(ROOT, rel), os.path.join(FIX, "good", name))
    good.append(dict(file="good/" + name, source=rel, format="blocks"))
for d in ("R3b", "H1", "B1", "W1"):
    rel = LOG + "ian-%s/prompt.txt" % d
    name = "ian-%s-prompt.txt" % d
    shutil.copyfile(os.path.join(ROOT, rel), os.path.join(FIX, "good", name))
    good.append(dict(file="good/" + name, source=rel, format="ian"))
pb = rd("REFERENCE/PROMPTING-PLAYBOOK.md")
blk = re.search(r"```prompt\nID: PB-edit-pose.*?```", pb, re.S).group(0)
open(os.path.join(FIX, "good", "playbook-PB-edit-pose.md"), "w", encoding="utf-8", newline="\n").write(blk + "\n")
good.append(dict(file="good/playbook-PB-edit-pose.md", source="REFERENCE/PROMPTING-PLAYBOOK.md", format="blocks"))

json.dump(dict(failed=F, good=good), open(os.path.join(FIX, "MANIFEST.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=True)
print("wrote %d failed/known_conflict fixtures, %d good files" % (len(F), len(good)))
