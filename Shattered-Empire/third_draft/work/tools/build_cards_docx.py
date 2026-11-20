# Builds edit card .docx files from edit_cards/*.md, matching the 2026-11-05 Ch 00 to 05 files
# (python-docx default template, H1/H2/H3, bold labels, Consolas code spans, List Bullet).
# Verifies FIND strings against work/text/<name>.txt. Does not alter card content.
import re, sys, json, os, docx
from docx.shared import Pt
BASE = r"D:/WKP/Shattered-Empire/third_draft"
CARDS = BASE + "/edit_cards"
TEXT = BASE + "/work/text"
DATE = "2026-11-19"

def label(stem):
    if stem == "ch_00_prologue": return "Ch 00 Prologue"
    if stem == "ch_99_epilogue": return "Ch 99 Epilogue"
    return "Ch " + stem.split("_")[1]

def inline(par, s):
    for i, seg in enumerate(re.split(r"`", s)):
        if i % 2 == 1:
            r = par.add_run(seg); r.font.name = "Consolas"
        else:
            for j, b in enumerate(re.split(r"\*\*", seg)):
                if b == "": continue
                r = par.add_run(b)
                if j % 2 == 1: r.bold = True

def parse(lines):
    cards, cur = [], None
    for ln in lines:
        m = re.match(r"### (CH \d+ ITEM \d+|.*ITEM (\d+))", ln)
        if ln.startswith("### "):
            cur = {"head": ln[4:], "lines": []}; cards.append(cur)
        elif cur is not None: cur["lines"].append(ln)
    return cards

def verify(stem, lines):
    txt = open(f"{TEXT}/{stem}.txt", encoding="utf-8").read()
    notes = []; ncards = 0
    for c in parse(lines):
        ncards += 1
        num = re.search(r"ITEM (\d+)", c["head"]); num = num.group(1) if num else c["head"]
        probs = []
        for ln in c["lines"]:
            m = re.match(r"\*\*FIND exactly:\*\* `(.*)`\s*$", ln)
            if m:
                n = txt.count(m.group(1))
                if n != 1: probs.append(f"FIND occurs {n} times")
            opts = []
            m = re.match(r"\*\*REPLACE WITH:\*\* `(.*)`\s*$", ln)
            if m: opts.append(m.group(1))
            m = re.match(r"- Option .*?, replace with `(.*)`\s*$", ln)
            if m: opts.append(m.group(1))
            for o in opts:
                if ":" in o: probs.append("colon in option text")
                if "\u2014" in o: probs.append("em dash in option text")
        body = "\n".join(c["lines"])
        if "\u2014" in c["head"] + body and "em dash in option text" not in probs:
            probs.append("em dash in card text")
        if probs: notes.append((num, sorted(set(probs)), probs))
    return ncards, notes

def build(stem, out):
    lines = open(f"{CARDS}/{stem}.md", encoding="utf-8").read().split("\n")
    ncards, notes = verify(stem, lines)
    d = docx.Document()
    started = False; pending_notes = bool(notes)
    for ln in lines:
        if not ln.strip(): continue
        if ln.startswith("# "):
            d.add_heading(ln[2:], 1)
            if notes:
                d.add_heading("VERIFY NOTES", 2)
                d.add_paragraph("These cards failed the automatic check before conversion. Card content was not changed. Check the words on the page before you edit.")
                for num, kinds, raw in notes:
                    cnt = {}
                    for k in raw: cnt[k] = cnt.get(k, 0) + 1
                    p = d.add_paragraph(style="List Bullet"); p.add_run(f"Item {num}: " + "; ".join(sorted(set(raw))))
            continue
        if ln.startswith("## "): d.add_heading(ln[3:], 2); continue
        if ln.startswith("### "): d.add_heading(ln[4:], 3); continue
        if ln.startswith("- "):
            inline(d.add_paragraph(style="List Bullet"), ln[2:]); continue
        inline(d.add_paragraph(), ln)
    d.save(out)
    return ncards, notes

if __name__ == "__main__":
    outdir = sys.argv[1]; stems = sys.argv[2:]
    res = {}
    for s in stems:
        out = f"{outdir}/{DATE} - Edit Cards - {label(s)}.docx"
        n, notes = build(s, out)
        res[s] = {"cards": n, "notes": [(a, b) for a, b, c in notes], "file": out}
    json.dump(res, open("D:/WKP/scratch/se-cards/result.json", "w"), indent=1)
