#!/usr/bin/env python
"""prompt-preflight: free, offline check of an image or video prompt BEFORE credits are spent.

Wraps the legacy lint (rules R1 to R13, imported by path, never copied) and adds rules PF01 to PF30.
Reads words only. It cannot predict what an engine draws. No network, no credits, stdlib only.

  python preflight.py FILE.md                 block file (```prompt blocks)
  python preflight.py prompt.txt              Ian format (MAIN PROMPT / NEGATIVE FIELD)
  python preflight.py --text "..." --kind video --engine veo
  python preflight.py --rules                 print the rule table
Exit code: 1 if any FAIL, 0 otherwise, 2 for a usage error. Full how-to: README.md
"""
import argparse
import datetime
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import rules as R            # noqa: E402
import checks as C           # noqa: E402

LINT_DIR = os.environ.get("PREFLIGHT_LINT_DIR") or os.path.join(R.ROOT, "data", "firefly-prompt-guide")
_lint = None


def lint_module():
    """Load prompt_lint.py by path. Bytecode is not written so the guide folder stays untouched."""
    global _lint
    if _lint is None:
        old = sys.dont_write_bytecode
        sys.dont_write_bytecode = True
        try:
            spec = importlib.util.spec_from_file_location("prompt_lint_legacy", os.path.join(LINT_DIR, "prompt_lint.py"))
            _lint = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(_lint)
        finally:
            sys.dont_write_bytecode = old
    return _lint


class Finding:
    def __init__(self, rule, sev, detail="", count=1):
        self.rule, self.sev, self.detail, self.count = rule, sev, detail, count
        row = R.RULE_BY_ID.get(rule, {})
        self.why, self.fix, self.tag = row.get("why", ""), row.get("fix", ""), row.get("tag", "")

    def as_dict(self):
        return dict(rule=self.rule, severity=self.sev, detail=self.detail, why=self.why, fix=self.fix,
                    tag=self.tag, count=self.count)


_MAP = {0x2014: "-", 0x2013: "-", 0x2019: "'", 0x2018: "'", 0x201c: '"', 0x201d: '"'}


def ascii_safe(s):
    return s.translate(_MAP).encode("ascii", "replace").decode("ascii")


# ------------------------------------------------------------------ meta and kind
VIDEO_WORDS = ("veo", "kling", "seedance", "runway", "luma", "flux")


def guess_kind(text, engine="other"):
    ss = C.sentences(text)
    first = ss[0] if ss else ""
    if re.match(r"\s*(change|replace|swap|fix|make|edit|relight|remove|add|straighten|match|soften|sharpen)\b", first, re.I) \
            and re.search(r"(^|\n|\.\s)\s*keep\b", text, re.I):
        return "edit"
    lint = lint_module()
    if re.search(r"\d\s*(to|-)\s*\d+(\.\d+)?\s*seconds|\[?\d{1,2}:\d{2}\s*-\s*\d{1,2}:\d{2}", text, re.I) \
            or lint.CAMERA.search(text) or engine in VIDEO_WORDS:
        return "video"
    return "still"


def _norm_meta(meta):
    m = {str(k).upper(): (v.strip() if isinstance(v, str) else v) for k, v in (meta or {}).items()}
    return m


VALID_KINDS = ("still", "video", "edit", "auto")
VALID_ENGINES = ("veo", "kling", "seedance", "runway", "luma", "flux", "firefly", "other")


def sanitize_meta(meta):
    """Return (meta copy with bad KIND or ENGINE values replaced by defaults, list of PF31 detail strings).
    A typo in a header must not silently switch rules off (tester finding), so each one is reported."""
    m = _norm_meta(meta)
    notes = []
    for key, valid, default in (("KIND", VALID_KINDS, "auto"), ("ENGINE", VALID_ENGINES, "other")):
        v = m.get(key)
        if isinstance(v, str) and v and v.lower() not in valid:
            notes.append("unknown %s value '%s' (allowed: %s); using %s instead, so rules that depend on it may not run"
                         % (key, v[:30], ", ".join(valid), default))
            m[key] = default
    allow = [x.strip().upper() for x in re.split(r"[,\s]+", m.get("ALLOW") or "") if x.strip()]
    bad = [x for x in allow if x not in R.RULE_BY_ID]
    if bad:
        notes.append("unknown rule id in ALLOW: %s (nothing is overridden by it)" % ", ".join(bad))
    return m, notes


def run_checks(text, meta, negative=None, history=None):
    """Return a list of Finding (FAIL, WARN, OVERRIDDEN, PASS). meta keys are the block header keys."""
    m, pf31 = sanitize_meta(meta)
    text = text.strip()
    engine = (m.get("ENGINE") or "other").lower()
    kind = (m.get("KIND") or "auto").lower()
    if kind == "auto":
        kind = guess_kind(text, engine)
    start = (m.get("START_FRAME") or "no").lower()
    end = (m.get("END_FRAME") or "no").lower()
    audio = (m.get("AUDIO") or "off").lower()
    allow = set(x.strip().upper() for x in re.split(r"[,\s]+", m.get("ALLOW") or "") if x.strip())
    neg = negative if negative is not None else m.get("NEGATIVE")
    ctx = C.Ctx(text, kind, engine, start, end, audio, m.get("MASTER"), m.get("REFERENCE_TYPE"), m.get("SHOT"), neg, history,
                  m.get("END_FRAME_FILE"))

    out, applied = [], []
    for d in pf31:
        out.append(Finding("PF31", "WARN", d))
    # --- legacy lint, R1..R13
    lint = lint_module()
    fails, warns = lint.lint(m.get("ID", "?"), text, "video" if kind == "video" else "still", engine, start, audio,
                             allow_impact=(m.get("ALLOW_IMPACT", "no").lower() == "yes"))
    lint_ids = ["R%d" % i for i in range(1, 14)] if kind == "video" else ["R%d" % i for i in range(1, 7)]
    grouped = {}
    for sev, items in (("FAIL", fails), ("WARN", warns)):
        for s in items:
            rid = s.split(" ", 1)[0]
            grouped.setdefault((rid, sev), []).append(s.split(" ", 1)[1] if " " in s else "")
    for (rid, sev), items in grouped.items():
        detail = " | ".join(items[:3]) + (" (+%d more)" % (len(items) - 3) if len(items) > 3 else "")
        if rid == "R1" and kind == "video":      # PF27: extra context line, not a separate finding
            detail += "  [negatives failed on video 5 of 5 clips]"
        out.append(Finding(rid, sev, detail, len(items)))
    for rid in lint_ids:
        if not any(f.rule == rid for f in out):
            applied.append(rid)
    # --- new rules
    for rid, fn in C.CHECKS.items():
        if kind not in R.RULE_BY_ID[rid]["kinds"]:
            continue
        res = fn(ctx)
        if res is None:
            continue
        if not res:
            applied.append(rid)
        for sev, detail in res:
            out.append(Finding(rid, sev, detail))
    for rid in applied:
        out.append(Finding(rid, "PASS"))
    for f in out:
        if f.rule.upper() in allow and f.sev in ("FAIL", "WARN"):
            f.detail += "  [author override: ALLOW %s]" % f.rule
            f.sev = "OVERRIDDEN"
    order = {"FAIL": 0, "WARN": 1, "OVERRIDDEN": 2, "INFO": 3, "PASS": 4}
    out.sort(key=lambda f: (order[f.sev], f.rule))
    return out


def verdict(findings):
    if any(f.sev == "FAIL" for f in findings):
        return "FAIL"
    return "WARN" if any(f.sev == "WARN" for f in findings) else "PASS"


# ------------------------------------------------------------------ settings check (PF30)
def check_settings(path):
    with open(os.path.join(LINT_DIR, "SETTINGS-TEMPLATE.txt"), encoding="utf-8") as fh:
        tpl = fh.read().splitlines()
    start = next(i for i, l in enumerate(tpl) if l.startswith("--- AGENT BLOCK"))

    def key_of(line):
        k = line.split(":", 1)[0]
        return re.split(r"\s*\(", k)[0].strip().upper()
    want = [key_of(l) for l in tpl[start:] if ":" in l and not l.startswith("---")]
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    have = {key_of(l): l.split(":", 1)[1].strip() for l in lines if ":" in l and not l.startswith("---")}
    out = []
    missing = [k for k in want if k not in have]
    if missing:
        out.append(Finding("PF30", "FAIL", "missing fields: " + ", ".join(missing)))

    def empty(v):
        v = (v or "").strip()
        return (not v) or set(v) <= set("_ ") or v.upper() == "NOT SHOWN"
    credit = have.get("CREDIT READOUT BEFORE CLICK", "")
    if re.search(r"\d", credit) and empty(have.get("ENGINE AS SHOWN")):
        out.append(Finding("PF30", "WARN", "a credit number is typed but ENGINE AS SHOWN is empty: number typed without a panel readout?"))
    if not out:
        out.append(Finding("PF30", "PASS"))
    return out


# ------------------------------------------------------------------ input parsing
HEADER_KEYS = ("ID", "KIND", "ENGINE", "START_FRAME", "END_FRAME", "END_FRAME_FILE", "AUDIO", "SHOT", "MASTER", "REFERENCE_TYPE",
               "MODE", "ALLOW", "ALLOW_IMPACT", "NEGATIVE")


def _is_header_line(line):
    mm = re.match(r"^([A-Z_]+):", line)
    return bool(mm and mm.group(1) in HEADER_KEYS)


def parse_blocks(text, notes=None):
    out = []
    for n, mm in enumerate(re.finditer(r"```prompt\n(.*?)```", text, re.S), 1):
        head, sep, prompt = mm.group(1).partition("\n---\n")
        if not sep:
            head, prompt = "", mm.group(1)
            lines = prompt.split("\n")
            if _is_header_line(lines[0]):
                k = 0
                while k < len(lines) and _is_header_line(lines[k]):
                    k += 1
                head, prompt = "\n".join(lines[:k]), "\n".join(lines[k:])
                if notes is not None:
                    notes.append("prompt block %d has a header but no line with only --- after it; "
                                 "the leading KEY: lines were taken as the header, not linted as prompt. "
                                 "Add a --- line after the header." % n)
        meta, last = {}, None
        for line in head.splitlines():
            kv = re.match(r"^([A-Z_]+):\s*(.*)$", line)
            if kv:
                last = kv.group(1)
                v = kv.group(2).strip()
                if last != "NEGATIVE":
                    v = re.sub(r"\s*\(.*\)\s*$", "", v)
                meta[last] = v
            elif last == "NEGATIVE" and line.strip():
                meta[last] += " " + line.strip()
        meta.setdefault("ENGINE", "veo")      # legacy block default, same as prompt_lint
        meta.setdefault("KIND", "video")
        out.append((meta, prompt.strip(), meta.get("NEGATIVE")))
    return out


def parse_ian(text, name):
    mm = re.search(r"^MAIN PROMPT[^\n]*\n(.*?)(?:\n\s*\n\s*NEGATIVE FIELD[^\n]*\n(.*))?\Z", text, re.S | re.M)
    main = mm.group(1).strip()
    neg = (mm.group(2) or "").strip().split("\n\n")[0].strip() or None
    return {"ID": name, "KIND": "still", "ENGINE": "firefly"}, main, neg


def load_input(path_or_text, from_stdin=False, notes=None):
    """Return list of (meta, prompt, negative). Appends human notes to `notes` if given."""
    if from_stdin or not os.path.isfile(path_or_text):
        text, label = path_or_text, "text"
    else:
        with open(path_or_text, encoding="utf-8") as fh:
            text = fh.read()
        p = os.path.abspath(path_or_text)
        label = os.path.basename(os.path.dirname(p)) if os.path.basename(p).lower() == "prompt.txt" \
            else os.path.splitext(os.path.basename(p))[0]
    if "```prompt" in text:
        return [(m, p, n) for m, p, n in parse_blocks(text, notes)]
    if re.search(r"^MAIN PROMPT", text, re.M):
        m, p, n = parse_ian(text, label)
        return [(m, p, n)]
    if notes is not None and not from_stdin and os.path.splitext(str(path_or_text))[1].lower() == ".md":
        notes.append("no prompt blocks found, treating the whole file as one prompt")
    return [({"ID": label}, text.strip(), None)]


# ------------------------------------------------------------------ output
def header_line(meta, prompt, findings, kind, engine):
    return "PREFLIGHT %s  (%s, %s, %d words, %d chars)   VERDICT: %s" % (
        meta.get("ID", "?"), engine, kind, lint_module().words(prompt), len(prompt.strip()), verdict(findings))


def render(meta, prompt, findings, kind, engine, quiet=False, checklist=True):
    lines = [header_line(meta, prompt, findings, kind, engine)]
    passed = []
    for f in findings:
        if f.sev == "PASS":
            passed.append(f.rule)
            continue
        lines.append("[%s] %s   %s   WHY: %s   FIX: %s   (%s)" % (f.sev, f.rule, f.detail, f.why, f.fix, f.tag))
    if passed and not quiet:
        lines.append("[PASS] " + " ".join(passed))
    if kind == "video" and checklist:
        lines.append("NINE-POINT START-FRAME CHECK (PROMPTING-PLAYBOOK D3, plus our extras 10 to 12):")
        lines += ["  " + p for p in R.NINE_POINTS + R.EXTRA_POINTS]
        lines.append(R.RETRY_RULE)
    lines.append(R.LIMIT)
    return ascii_safe("\n".join(lines))


def rules_text():
    rows = ["%-5s %-12s %-22s %s" % (r["id"], r["severity"][:12], r["tag"][:22], r["name"]) for r in R.RULES]
    return ascii_safe("RULE TABLE (full evidence in RULE-TABLE.md)\n" + "\n".join(rows))


# ------------------------------------------------------------------ history
def read_history(path):
    """Return (rows, skipped). Damaged, binary or non-object lines are skipped and counted, never raised."""
    rows, skipped = [], 0
    if path and os.path.isfile(path):
        with open(path, "rb") as fh:
            for raw in fh:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    row = json.loads(raw.decode("utf-8"))
                except (ValueError, UnicodeDecodeError):
                    skipped += 1
                    continue
                if isinstance(row, dict):
                    rows.append(row)
                else:
                    skipped += 1
    return rows, skipped


def history_path_problem(path, need_write):
    """Return a plain-words problem string for a bad --history path, or None."""
    if os.path.isdir(path):
        return "--history is a folder, not a file: " + path
    folder = os.path.dirname(os.path.abspath(path))
    if not os.path.isdir(folder):
        return "--history folder does not exist: " + folder
    if os.path.exists(path) and not os.access(path, os.R_OK):
        return "--history file cannot be read: " + path
    if need_write:
        if os.path.exists(path) and not os.access(path, os.W_OK):
            return "--history file is not writable: " + path
        if not os.path.exists(path) and not os.access(folder, os.W_OK):
            return "--history folder is not writable: " + folder
    return None


def record_try(path, shot, text, history):
    n = len([h for h in history if str(h.get("shot", "")).lower() == shot.lower()])
    row = {"shot": shot, "attempt": n + 1, "date": datetime.date.today().isoformat(), "text": text}
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=True) + "\n")
    history.append(row)


# ------------------------------------------------------------------ CLI
def build_parser():
    ap = argparse.ArgumentParser(prog="preflight.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?", help="file path, or - for stdin")
    ap.add_argument("--text")
    ap.add_argument("--kind", choices=["still", "video", "edit", "auto"])
    ap.add_argument("--engine", choices=["veo", "kling", "seedance", "runway", "luma", "flux", "firefly", "other"])
    ap.add_argument("--start-frame", choices=["yes", "no"])
    ap.add_argument("--end-frame", choices=["yes", "no"])
    ap.add_argument("--audio", choices=["on", "off"])
    ap.add_argument("--master")
    ap.add_argument("--ref-type", choices=["composition", "style", "none"])
    ap.add_argument("--shot")
    ap.add_argument("--history")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--record-anyway", action="store_true", help="record the try even when the verdict is FAIL")
    ap.add_argument("--allow")
    ap.add_argument("--settings")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--rules", action="store_true")
    ap.add_argument("--no-checklist", action="store_true")
    return ap


def main(argv=None):
    ap = build_parser()
    try:
        a = ap.parse_args(argv)
    except SystemExit as e:
        return 2 if e.code else 0
    if a.rules:
        print(rules_text())
        return 0
    if a.record and not a.history:
        print("usage error: --record needs --history FILE")
        return 2
    results, exit_code = [], 0
    if a.settings:
        if not os.path.isfile(a.settings):
            print("usage error: settings file not found: " + a.settings)
            return 2
        f = check_settings(a.settings)
        results.append(("SETTINGS " + os.path.basename(os.path.dirname(os.path.abspath(a.settings))), None, None, f, None, None))
    notes = []
    if a.history:
        problem = history_path_problem(a.history, a.record)
        if problem:
            print("usage error: " + problem)
            return 2
    items = []
    if a.text is not None:
        items = load_input(a.text, from_stdin=True, notes=notes)
    elif a.source == "-":
        items = load_input(sys.stdin.read(), from_stdin=True, notes=notes)
    elif a.source:
        if not os.path.isfile(a.source):
            print("usage error: file not found: " + a.source)
            return 2
        try:
            items = load_input(a.source, notes=notes)
        except (UnicodeDecodeError, OSError) as e:
            print("usage error: cannot read %s as UTF-8 text (%s)" % (a.source, type(e).__name__))
            return 2
    elif not a.settings:
        ap.print_usage()
        print("usage error: give a file, --text, - for stdin, --settings or --rules")
        return 2
    history = None
    if a.history:
        history, skipped = read_history(a.history)
        if skipped:
            notes.append("skipped %d unreadable history lines" % skipped)
    flags = {"KIND": a.kind, "ENGINE": a.engine, "START_FRAME": a.start_frame, "END_FRAME": a.end_frame, "AUDIO": a.audio,
             "MASTER": a.master, "REFERENCE_TYPE": a.ref_type, "SHOT": a.shot, "ALLOW": a.allow}
    empty = 0
    for meta, prompt, neg in items:
        meta = dict(meta)
        meta.update({k: v for k, v in flags.items() if v})
        if not (prompt or "").strip():
            print("usage error: no prompt text (%s)" % meta.get("ID", "?"))
            empty += 1
            continue
        clean, _ = sanitize_meta(meta)     # bad KIND or ENGINE values are reported as PF31 inside run_checks
        clean.setdefault("ENGINE", "other")
        kind = (clean.get("KIND") or "auto").lower()
        if kind == "auto":
            kind = guess_kind(prompt, clean["ENGINE"].lower())
            guess_note = "(kind guessed: %s)" % kind
        else:
            guess_note = ""
        if (meta.get("KIND") or "auto").lower() == "auto":
            meta["KIND"] = kind
        meta.setdefault("ENGINE", clean["ENGINE"])
        f = run_checks(prompt, meta, neg, history)
        clean["KIND"] = kind
        results.append((clean, prompt, kind, f, neg, guess_note))
        if a.record:
            if not clean.get("SHOT"):
                notes.append("not recorded: no SHOT given (use --shot or SHOT: in the header)")
            elif verdict(f) == "FAIL" and not a.record_anyway:
                notes.append("not recorded: verdict FAIL for %s (add --record-anyway to log it anyway)" % clean.get("ID", "?"))
            else:
                try:
                    record_try(a.history, clean["SHOT"], prompt, history)
                except OSError as e:
                    print("usage error: cannot write --history file: %s (%s)" % (a.history, type(e).__name__))
                    return 2
    for n in notes:
        print("NOTE: " + n, file=sys.stderr if a.json else sys.stdout)
    if a.json:
        print(json.dumps([{"id": m.get("ID", "?") if isinstance(m, dict) else m, "kind": k,
                           "verdict": verdict(f), "findings": [x.as_dict() for x in f]} for m, p, k, f, n, g in results], indent=1))
    else:
        for m, p, k, f, n, g in results:
            if p is None:
                print(ascii_safe("PREFLIGHT %s   VERDICT: %s" % (m, verdict(f))))
                for x in f:
                    if x.sev != "PASS":
                        print(ascii_safe("[%s] %s   %s   WHY: %s   FIX: %s   (%s)" % (x.sev, x.rule, x.detail, x.why, x.fix, x.tag)))
                    elif not a.quiet:
                        print("[PASS] PF30")
                continue
            print(render(m, p, f, k, m.get("ENGINE", "other").lower(), a.quiet, not a.no_checklist))
            if g:
                print(g)
            print()
    if empty:
        return 2
    if any(x.sev == "FAIL" for r in results for x in r[3]):
        exit_code = 1
    return exit_code


if __name__ == "__main__":
    sys.exit(main())
