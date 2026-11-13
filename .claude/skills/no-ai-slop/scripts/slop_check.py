#!/usr/bin/env python3
"""slop_check.py - mechanical pass of the no-ai-slop gate.

Usage:
    python slop_check.py <file> [<file> ...]
    type draft.txt | python slop_check.py -        (stdin)
    python slop_check.py --json <file>             (machine-readable)

Flags, with line numbers and a suggestion:
  - em dashes and en dashes used as dashes (Rule 1)
  - double-hyphen dashes "--" used as a dash
  - banned words and phrases from SKILL.md (Rule 2)
  - rhetorical-question hooks
  - hedge words
Exit code 0 = clean, 1 = hits, 2 = usage or read error.

This is the MECHANICAL pass only. The judgment pass (is it generic, does it
sound like the actual person) is still done by the main session or
marketing-director. Read-only: never edits the file.
"""
import io
import json
import re
import sys

EM = "—"
EN = "–"
# mojibake forms of the em dash (file saved with the wrong encoding)
MOJI_EM = "â€”"

BANNED = [
    (r"\belevat(e|es|ed|ing)\b", "elevate", "say what actually improves"),
    (r"\bunlock(s|ed|ing)?\b", "unlock", "say what the reader gets"),
    (r"\bgame[- ]chang(er|ers|ing)\b", "game-changer", "name the real change"),
    (r"\btestament to\b", "testament to", "state the fact"),
    (r"\bpush(es|ed|ing)? (the )?boundar(y|ies)\b", "pushing boundaries", "name what was done"),
    (r"\bboundaries\b", "boundaries", "cut unless it is a literal boundary"),
    (r"\bunleash(es|ed|ing)?\b", "unleash", "plain verb"),
    (r"\bdiv(e|es|ed|ing) (deep )?into\b", "dive into", "start where the content starts"),
    (r"\bdelv(e|es|ed|ing) into\b", "delve into", "start where the content starts"),
    (r"\bin the realm of\b", "in the realm of", "cut"),
    (r"\bwhen it comes to\b", "when it comes to", "cut or rewrite directly"),
    (r"\bit'?s important to note\b", "it's important to note", "just say it"),
    (r"\bwhether you'?re\b.{0,60}\bor\b", "whether you're X or Y", "name the actual reader"),
    (r"\bnot just\b.{0,60}\bbut\b", "not just X but Y", "state the claim once"),
    (r"\bseamless(ly)?\b", "seamless(ly)", "say what works and how"),
    (r"\brobust\b", "robust", "name the actual strength"),
    (r"\bcutting[- ]edge\b", "cutting-edge", "name the actual feature"),
    (r"\bever[- ]evolving\b", "ever-evolving", "cut"),
    (r"\btapestry\b", "tapestry", "cut"),
    (r"\bjourney\b", "journey", "cut unless it is an actual trip"),
    (r"\bin today'?s (world|age|digital|fast)\b", "in today's world", "throat-clearing, start with the content"),
    (r"\blet'?s dive in\b", "let's dive in", "throat-clearing"),
    (r"\bwithout further ado\b", "without further ado", "throat-clearing"),
    (r"\bat the end of the day\b", "at the end of the day", "throat-clearing"),
    (r"\bgame[- ]chang", "game-changer", "name the real change"),
]

HEDGES = [
    (r"\bcould potentially\b", "could potentially"),
    (r"\bin some ways\b", "in some ways"),
    (r"\bmight\b", "might"),
    (r"\bperhaps\b", "perhaps"),
    (r"\bsomewhat\b", "somewhat"),
    (r"\bkind of\b", "kind of"),
    (r"\bsort of\b", "sort of"),
    (r"\bit seems like\b", "it seems like"),
    (r"\bpretty much\b", "pretty much"),
    (r"\bto some extent\b", "to some extent"),
]

# Rhetorical question openers (the hook pattern)
Q_HOOKS = [
    r"^\s*(ever|have you ever)\s+(wonder|wondered|thought|asked|noticed)\b.*\?",
    r"^\s*what if (i|you|we) told you\b.*\?",
    r"^\s*(did|do) you (know|ever)\b.*\?",
    r"^\s*(why|how) (do|does|did|is|are)\b[^.?!]{0,120}\?\s*$",
    r"^\s*(ready|want) to\b[^.?!]{0,100}\?",
    r"^\s*(what|who|where) (if|would|could)\b[^.?!]{0,120}\?\s*$",
    r"^\s*(sound|looks?) familiar\?",
    r"^\s*(tired of|sick of)\b.*\?",
]


def scan_line(no, line):
    hits = []
    for ch, label in ((EM, "em dash"), (EN, "en dash used as a dash"), (MOJI_EM, "em dash (garbled encoding)")):
        for m in re.finditer(re.escape(ch), line):
            if ch == EN and re.search(r"\d\s*" + EN + r"\s*\d", line[max(0, m.start() - 3):m.end() + 3]):
                continue  # numeric range like 9-11
            hits.append((no, m.start() + 1, "DASH", label,
                         "Rule 1: split into two sentences, use a comma, colon or parentheses, or rewrite"))
    for m in re.finditer(r"(?:(?<=\s)--(?=\s)|(?<=\w)--(?=\w))", line):
        hits.append((no, m.start() + 1, "DASH", "double hyphen used as a dash",
                     "Rule 1: restructure the sentence, do not swap in a comma if the meaning changes"))
    low = line.lower()
    seen = set()
    for pat, label, sug in BANNED:
        for m in re.finditer(pat, low):
            key = (label, m.start())
            if key in seen:
                continue
            seen.add(key)
            hits.append((no, m.start() + 1, "BANNED", label, sug))
    for pat in Q_HOOKS:
        if re.search(pat, line, re.I):
            hits.append((no, 1, "QHOOK", "rhetorical-question hook",
                         "open with the actual content, unless the real hosts would say it on camera"))
            break
    for pat, label in HEDGES:
        for m in re.finditer(pat, low):
            hits.append((no, m.start() + 1, "HEDGE", label, "say the thing, cut the hedge"))
    return hits


def read_source(arg):
    if arg == "-":
        return "stdin", sys.stdin.read()
    with io.open(arg, "r", encoding="utf-8-sig", errors="replace") as f:
        return arg, f.read()


def main(argv):
    as_json = False
    args = []
    for a in argv:
        if a == "--json":
            as_json = True
        elif a in ("-h", "--help"):
            print(__doc__)
            return 0
        else:
            args.append(a)
    if not args:
        print("usage: slop_check.py [--json] <file>|- ...", file=sys.stderr)
        return 2
    total = 0
    report = []
    for a in args:
        try:
            name, text = read_source(a)
        except OSError as e:
            print("cannot read %s: %s" % (a, e), file=sys.stderr)
            return 2
        in_code = False
        file_hits = []
        for i, line in enumerate(text.splitlines(), 1):
            if line.strip().startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            file_hits.extend(scan_line(i, line))
        file_hits.sort(key=lambda h: (h[0], h[1]))
        total += len(file_hits)
        report.append((name, file_hits))
    if as_json:
        print(json.dumps([{"file": n, "hits": [dict(line=h[0], col=h[1], kind=h[2], found=h[3], suggestion=h[4]) for h in hs]} for n, hs in report], indent=2))
    else:
        out = io.StringIO()
        for name, hs in report:
            for ln, col, kind, found, sug in hs:
                out.write("%s:%d:%d  [%s] %s -> %s\n" % (name, ln, col, kind, found, sug))
        summary = "slop_check: %d hit(s) in %d file(s)" % (total, len(report)) if total else "slop_check: clean (mechanical pass only, judgment pass still needed)"
        out.write(summary + "\n")
        sys.stdout.write(out.getvalue())
    return 1 if total else 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main(sys.argv[1:]))
