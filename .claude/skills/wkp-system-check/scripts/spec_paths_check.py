"""spec_paths_check.py - find file paths named in agent specs and skills that do not exist.

Read-only. Scans D:\\WKP\\.claude\\agents\\**\\*.md and D:\\WKP\\.claude\\skills\\**\\*.md
(SKILL.md plus references), pulls out every absolute Windows path (C:, D:, L:, P:, N: ...)
and every backticked repo-relative path, and checks it exists on disk.

Paths with template parts (<movie>, YYYY, nnn, *, {x}, ...) are skipped as patterns.
Paths with spaces are handled by trying space-joined prefixes; a shorter prefix only
counts as the end of the path when the next word has no backslash in it.

Usage:
  python spec_paths_check.py            # report misses
  python spec_paths_check.py --json out.json
  python spec_paths_check.py --allow allow.txt   # lines "path<TAB>reason" to list as known

Exit 0 when no unexplained misses, 1 otherwise.
Built 2026-11-19 (readiness pass).
"""
import json
import os
import re
import sys
from pathlib import Path

REPO = Path(r"D:\WKP")
SCAN = [REPO / ".claude" / "agents", REPO / ".claude" / "skills"]
SKIP_DIRS = {"node_modules", ".git", "__pycache__", "_archive", "vendor", "dist", ".venv"}
# third-party skills copied in whole; their internal paths are not WKP paths
THIRD_PARTY_SKILLS = {"last30days", "design-taste-frontend", "impeccable", "remotion-motion-graphics", "task-observer"}

ABS_RE = re.compile(r"(?<![A-Za-z0-9])([A-Za-z]:\\[^\n`\"|]*)")
TICK_RE = re.compile(r"`([^`\n]+)`")
TEMPLATE_RE = re.compile(
    r"(<[^>]*>|\{[^}]*\}|\*|\?|YYYY|yyyy|MM-DD|nnn|NNN|\.\.\.|%[A-Za-z]+%|\$\{|\$[A-Za-z_]|xxx|XXX|\[[^\]]*\])"
)
DRIVE_OK = re.compile(r"^[A-Za-z]:\\")
TRAIL = ".,;:)]`'\"!"


def is_template(p: str) -> bool:
    return bool(TEMPLATE_RE.search(p))


def candidates(raw: str):
    """Yield space-joined prefixes that could be the real end of a path."""
    raw = raw.strip().replace("\\\\", "\\")
    # a second drive path or a comma list ends this path
    raw = re.split(r" (?=[A-Za-z]:\\)|, ", raw)[0]
    toks = raw.split(" ")
    out = []
    for k in range(min(len(toks), 10)):
        nxt = toks[k + 1] if k + 1 < len(toks) else ""
        if "\\" in nxt and k + 1 < len(toks):
            continue  # path continues past this space
        cand = " ".join(toks[: k + 1]).rstrip(TRAIL)
        if cand:
            out.append(cand)
    return out


def exists(p: str) -> bool:
    try:
        return os.path.exists(p)
    except OSError:
        return False


def check_abs(raw: str):
    cands = candidates(raw)
    if not cands:
        return None
    # template check on the shortest plausible candidate
    if any(is_template(c) for c in cands[:4]) or cands[0].endswith(("-", "_")):
        return ("template", cands[0])
    if cands[0].lower().startswith(str(REPO / "scratch").lower()):
        return ("runtime", cands[0])
    for c in cands:
        if exists(c):
            return ("ok", c)
    # report the shortest candidate (first word chain) as the miss
    return ("miss", cands[0])


def check_rel(raw: str, top_dirs, src: Path = None):
    s = raw.strip().rstrip(TRAIL)
    if " " in s and "\\" not in s.split(" ")[0] and "/" not in s.split(" ")[0]:
        return None
    if DRIVE_OK.match(s):
        return None  # handled by abs
    s2 = s.replace("/", "\\")
    first = s2.split("\\")[0]
    if "\\" not in s2 or " " in s2.split("\\")[0]:
        return None
    if is_template(s2) or s2.endswith(("-", "_")):
        return ("template", s2)
    bases = [REPO]
    if src is not None:
        bases += [src.parent] + [b for b in src.parents if str(b).lower().startswith(str(REPO / ".claude" / "skills").lower())]
    for b in bases:
        if exists(str(b / s2)):
            return ("ok", str(b / s2))
    if first not in top_dirs and not (src is not None and first in ("scripts", "references", "assets")):
        return None
    return ("miss", str(REPO / s2) if first in top_dirs else str(src.parent / s2))


def main():
    allow = {}
    ap = Path(__file__).with_name("spec_paths_allow.txt")
    if "--allow" in sys.argv:
        ap = Path(sys.argv[sys.argv.index("--allow") + 1])
    if True:
        if ap.exists():
            for line in ap.read_text(encoding="utf-8").splitlines():
                if "\t" in line and not line.startswith("#"):
                    a, b = line.split("\t", 1)
                    allow[a.strip().lower()] = b.strip()
    top_dirs = {p.name for p in REPO.iterdir() if p.is_dir()} | {p.name for p in REPO.iterdir() if p.is_file()}
    top_dirs.discard("scratch")
    results = []
    files = []
    for root in SCAN:
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in SKIP_DIRS]
            rel_parts = Path(dp).relative_to(REPO / ".claude").parts
            if len(rel_parts) >= 2 and rel_parts[0] == "skills" and rel_parts[1] in THIRD_PARTY_SKILLS:
                continue
            for fn in fns:
                if fn.lower().endswith(".md"):
                    files.append(Path(dp) / fn)
    for f in files:
        text = f.read_text(encoding="utf-8", errors="replace")
        for ln, line in enumerate(text.splitlines(), 1):
            seen = set()
            for m in ABS_RE.finditer(line):
                r = check_abs(m.group(1))
                if r and r[1] not in seen:
                    seen.add(r[1])
                    results.append({"file": str(f), "line": ln, "status": r[0], "path": r[1]})
            for m in TICK_RE.finditer(line):
                r = check_rel(m.group(1), top_dirs, f)
                if r and r[1] not in seen:
                    seen.add(r[1])
                    results.append({"file": str(f), "line": ln, "status": r[0], "path": r[1]})
    misses = [r for r in results if r["status"] == "miss"]
    known, unknown = [], []
    for r in misses:
        reason = allow.get(r["path"].lower())
        (known if reason else unknown).append({**r, "reason": reason})
    ok = sum(1 for r in results if r["status"] == "ok")
    tmpl = sum(1 for r in results if r["status"] in ("template", "runtime"))
    print(f"files scanned: {len(files)}  paths: {len(results)}  ok: {ok}  template: {tmpl}  miss: {len(misses)} (known {len(known)}, unexplained {len(unknown)})")
    for r in unknown:
        print(f"MISS  {r['path']}\n      in {r['file']}:{r['line']}")
    for r in known:
        print(f"KNOWN {r['path']}  ({r['reason']})\n      in {r['file']}:{r['line']}")
    if "--json" in sys.argv:
        Path(sys.argv[sys.argv.index("--json") + 1]).write_text(json.dumps(results, indent=1), encoding="utf-8")
    sys.exit(1 if unknown else 0)


if __name__ == "__main__":
    main()
