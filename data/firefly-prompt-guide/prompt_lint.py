#!/usr/bin/env python
"""Firefly / video-model prompt lint (pre-flight step 1). Created 2026-11-22 by graphic-design.
Fuller checker (this lint plus rules PF01 to PF30, history, settings): D:\\WKP\\software\\prompt-preflight\\preflight.py

Mechanical checks only. Every rule maps to a rule id in STANDARD.md (R1..R14).
Usage:
  python prompt_lint.py --file REBUILT-PROMPTS.md          lint every ```prompt block
  python prompt_lint.py --audit-old                        lint Zac's 18 logged clips + joust prompts + 4 Ian stills
Exit code 1 if any FAIL. WARN does not fail.
Block format in a markdown file:
  ```prompt
  ID: J1-ride
  KIND: video          (video | still)
  ENGINE: veo          (veo | kling | seedance | runway | luma | flux | firefly)
  START_FRAME: yes     (yes | no)
  AUDIO: off           (on | off)
  ---
  <the prompt text exactly as it will be pasted>
  ```
"""
import re, sys, os, glob, json

NEG = re.compile(r"\b(no|not|never|without|nothing|nobody|none|don't|dont|doesn't|doesnt|does not|do not|cannot|can't|avoid|neither|nor)\b", re.I)
ABSTRACT = re.compile(r"\b(as if|seems?|feels?|mood|emotional|hesitat\w*|begins? to|starts? to|tries to|tried to|trying to|almost|somehow|vibrant|whimsical|hyper-?realistic|beautiful|stunning|amazing)\b", re.I)
CAMERA = re.compile(r"\b(static|locked|locked-off|dolly|push(es)? in|pull(s)? back|pan|tilt|track(ing)?|handheld|pov|first-person|crane|arc|close-up|wide shot|medium shot|low angle|eye-level|over-the-shoulder|camera)\b", re.I)
MOVE_BODY = re.compile(r"\b(rolls? out|sits? up|stands? up|crouch\w*|walks?|runs?|rides?|gallop\w*|charges?)\b", re.I)
CONTACT = re.compile(r"\b(bumps?|bounces?|slams?|smash\w*|collid\w*|taps?)\b", re.I)
IMPACT_OK = {"joust"}
CAPS = re.compile(r"\b[A-Z]{3,}\b")
CAPS_OK = {"SFX", "POV", "FPS", "RGB", "HDR", "USA", "BGM", "PHYSICS"}  # PHYSICS is the Kling 4.0 guide label (K1)

def words(s): return len(re.findall(r"[A-Za-z0-9'\-]+", s))

def lint(pid, text, kind="video", engine="veo", start="no", audio="off", allow_impact=False):
    fails, warns = [], []
    t = text.strip()
    # R1 negation in main prompt
    for m in NEG.finditer(t):
        ctx = t[max(0, m.start()-25): m.end()+30].replace("\n", " ")
        ok_audio = engine in ("kling", "seedance") and re.search(r"no (subtitles|bgm|background music)", ctx, re.I)
        if not ok_audio:
            fails.append(f"R1 negation word '{m.group(0)}' ... {ctx}")
    # R2 caps / exclamation
    for m in CAPS.finditer(t):
        if m.group(0) not in CAPS_OK:
            fails.append(f"R2 shouting caps '{m.group(0)}'")
    if "!" in t: fails.append("R2 exclamation mark")
    # R3 length
    n = words(t)
    # R3: Luma Ray says about 100 words (SOURCED). Other engines have no maker cap: warn at 100, fail at 150 (video) or 170 (still), PROPOSED.
    if kind == "video":
        hard = 100 if engine == "luma" else 150
        soft = 100
    else:
        hard, soft = 170, 125
    if n > hard: fails.append(f"R3 length {n} words, limit {hard}")
    elif n > soft: warns.append(f"R3 length {n} words, over the {soft} word target")
    # R4 abstract or mental words
    for m in ABSTRACT.finditer(t):
        fails.append(f"R4 abstract or banned word '{m.group(0)}'")
    # R5 em dash
    if "\u2014" in t or "\u2013" in t: fails.append("R5 em or en dash")
    # R6 double spaces, repeated words, stray punctuation (garbled grammar)
    if re.search(r"\s{2,}", t.replace("\n", " ")): warns.append("R6 double space")
    if re.search(r"\b(\w+) \1\b", t, re.I): fails.append("R6 repeated word: " + re.search(r"\b(\w+) \1\b", t, re.I).group(0))
    if re.search(r"[.,]\s*[.,]", t): fails.append("R6 stray punctuation")
    if kind == "video":
        # R7 camera sentence present
        if not CAMERA.search(t): fails.append("R7 no camera sentence")
        # R8 locked camera plus travelling body
        if re.search(r"\b(locked|static)\b", t, re.I) and MOVE_BODY.search(t) and not allow_impact:
            warns.append("R8 locked camera with travelling body: " + MOVE_BODY.search(t).group(0))
        # R9 contact verbs
        for m in CONTACT.finditer(t):
            if not allow_impact:
                fails.append(f"R9 impact verb '{m.group(0)}' (write a resting end state instead)")
        # R10 audio line
        if audio == "on" and engine in ("veo", "kling", "seedance", "flux") and not re.search(r"(SFX:|Ambient noise:|says|\")", t):
            fails.append("R10 audio on but no SFX/Ambient noise sentence")
        if audio == "off" and re.search(r"(SFX:|Ambient noise:)", t):
            warns.append("R10 audio off but prompt has SFX line (harmless, delete if the toggle is off)")
        # R11 start frame: re-describing geometry
        if start == "yes" and re.search(r"\b(left third|right third|left edge|right edge|nose (points|pointing))\b", t, re.I):
            warns.append("R11 start frame set but geometry also written in text; remove, the picture decides")
        # R12 timestamps: continuous
        ts = re.findall(r"\[?(\d{1,2}):(\d{2})\s*[-\u2013]\s*(\d{1,2}):(\d{2})\]?", t)
        prev = None
        for a, b, c, d in ts:
            s = int(a)*60+int(b); e = int(c)*60+int(d)
            if prev is not None and s != prev: fails.append(f"R12 timestamp gap or overlap at {s}s (previous ended {prev}s)")
            prev = e
        # R13 count of distinct actions (rough): sentences with verbs of motion
        sent = [x for x in re.split(r"(?<=[.])\s+", t) if x]
        if len(sent) > 9: warns.append(f"R13 {len(sent)} sentences, one action per clip? check")
    return fails, warns

def parse_blocks(path):
    txt = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"```prompt\n(.*?)```", txt, re.S):
        body = m.group(1)
        head, _, prompt = body.partition("\n---\n")
        meta = dict(re.findall(r"^(\w+):\s*(.*?)\s*(?:\(.*\))?$", head, re.M))
        out.append((meta, prompt))
    return out

def run_blocks(path):
    bad = 0
    for meta, prompt in parse_blocks(path):
        f, w = lint(meta.get("ID", "?"), prompt, meta.get("KIND", "video"), meta.get("ENGINE", "veo").lower(),
                    meta.get("START_FRAME", "no").lower(), meta.get("AUDIO", "off").lower(),
                    allow_impact=meta.get("ALLOW_IMPACT", "no").lower() == "yes")
        status = "FAIL" if f else ("WARN" if w else "PASS")
        print(f"[{status}] {meta.get('ID','?')} ({meta.get('ENGINE','?')}, {words(prompt)} words)")
        for x in f: print("   FAIL", x)
        for x in w: print("   WARN", x)
        bad += 1 if f else 0
    return bad

def audit_old(root):
    items = []
    names = {"Video one": "G1", "Video 2": "G2", "Video 3": "G3", "Video 4": "G4", "Video 5": "G5", "Video 6": "G6",
             "video 7": "G7", "video 8": "G8", "video 9": "G9", "video 10": "G10", "video 11": "G11", "video 12": "G12", "Video 13": "G13"}
    for d, gid in names.items():
        p = os.path.join(root, d, "prompt and notes.txt")
        para = open(p, encoding="utf-8").read().strip().split("\n\n")[0]
        items.append((gid, para, "video", "yes" if gid in ("G4", "G5", "G11") else "no", "veo", False))
    for d, jid in {"Video 2": "J2", "Video 3": "J3", "Video 4": "J4", "Video 5": "J5"}.items():
        p = os.path.join(root, "Joust opener", d, "prompt and notes.txt")
        para = open(p, encoding="utf-8").read().strip().split("\n\n")[0]
        items.append((jid, para, "video", "no", "veo", True))
    big = open(os.path.join(root, "Joust opener", "prompt and notes for all the rest this was very time consuming.txt"), encoding="utf-8").read()
    paras = [x.strip() for x in re.split(r"\n\s*\n", big) if x.strip()]
    k = 0
    for para in paras:
        if para.startswith("First-person") or para.startswith("Animate"):
            k += 1
            items.append((f"JS{k}", para, "video", "yes" if k >= 1 else "no", "veo", True))
    # Ian stills
    for d in ("ian-R3b", "ian-H1", "ian-B1", "ian-W1"):
        t = open(os.path.join(root, d, "prompt.txt"), encoding="utf-8").read()
        m = re.search(r"MAIN PROMPT[^\n]*\n(.*?)\n\s*\nNEGATIVE FIELD", t, re.S)
        items.append((d.replace("ian-", "STILL-"), m.group(1).strip(), "still", "no", "firefly", False))
    rows = []
    for pid, text, kind, start, eng, imp in items:
        f, w = lint(pid, text, kind, eng, start, "off", allow_impact=imp)
        # joust impact words are allowed to exist, still report negation etc.
        rows.append((pid, words(text), f, w))
        print(f"[{'FAIL' if f else 'WARN' if w else 'PASS'}] {pid} ({words(text)} words) fails={len(f)} warns={len(w)}")
        for x in f: print("   FAIL", x)
        for x in w: print("   WARN", x)
    return rows

if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["--audit-old"]:
        audit_old(r"D:\WKP\data\firefly-prompt-log")
    elif a[:1] == ["--file"]:
        sys.exit(1 if run_blocks(a[1]) else 0)
    else:
        print(__doc__)
