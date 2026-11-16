#!/usr/bin/env python3
"""safe_fixes.py - the SAFE FIXES tier of the WKP nightly system check.

Allowlist only. Four actions, nothing else:
  1. scratch    : delete files older than N days (default 14) under <repo>\\scratch
  2. temp       : delete files older than N days (default 7) in the user's %TEMP%, skipping locked files
  3. pycache    : delete .pyc files inside __pycache__ folders under <repo>, remove the emptied folders
  4. logrotate  : MOVE (never delete) logs\\system-check\\YYYY-MM-DD*.md older than N days (default 90)
                  into logs\\system-check\\archive\\

Safety rails (all enforced in code, not just config):
  - Off unless the machine block in machines.json has "safe_fixes": {"enabled": true}.
    An unconfigured machine falls back to "default", which has no safe_fixes block, so it is OFF.
  - Mode is "dry-run" (default, deletes nothing) or "live" (set in machines.json or --fixes-live).
  - Kill switch: the file <repo>\\data\\system-check-fixes.disabled stops every fix.
  - Hard cap per run: max_files and max_bytes (shared across all actions). Hitting a cap stops the run.
  - HARD NEVER: any path containing "adobe", drive E:, anything not under the allowed root of the
    action, junctions and symlinks (never followed), git folders, Defender/Malwarebytes folders.
  - No admin elevation: a permission error is reported as "skipped, locked or needs admin", never retried.
  - No env vars, scheduled tasks, services, registry or git history are touched. No git commands run.

Honesty: counts and bytes are what the OS reported for the files actually handled. In dry-run they are
"would free" numbers from the same scan, labelled as such.
"""
import datetime as dt
import os
import re
import shutil
import stat
import sys

NEVER_PARTS = ("adobe", "malwarebytes", "windows defender", "defender", "\\.git\\", "/.git/")
LIST_LIMIT = 40  # file lines shown per action; counts are always exact


DEFAULT_PROTECT = {
    "paths": ["ian"],  # relative to the action root (scratch\ian\)
    "name_contains": ["photo", "restore", "client", "ian", "dk", "salaries"],
    "markers": [".keep", ".protect"],  # a marker file protects its whole folder and everything below
    "match_filenames": True,  # also protect files whose own name contains a word above
}


class Protect:
    """PROTECTED list for the scratch action. Config in machines.json (safe_fixes.protect) is UNIONED with the
    defaults above, so a config edit can add protection but can never silently remove the built-in list."""

    def __init__(self, cfg, root):
        cfg = cfg or {}
        self.root = os.path.abspath(root)
        self.paths = sorted(set(x.lower().strip("\\/") for x in DEFAULT_PROTECT["paths"] + list(cfg.get("paths", []))))
        self.words = sorted(set(x.lower() for x in DEFAULT_PROTECT["name_contains"] + list(cfg.get("name_contains", []))))
        self.markers = sorted(set(DEFAULT_PROTECT["markers"] + list(cfg.get("markers", []))))
        self.match_files = bool(cfg.get("match_filenames", DEFAULT_PROTECT["match_filenames"]))
        self._mark = {}

    def _marker_in(self, d):
        if d not in self._mark:
            self._mark[d] = next((m for m in self.markers if os.path.exists(os.path.join(d, m))), None)
        return self._mark[d]

    def why(self, path):
        """Reason string if protected, else None."""
        rel = os.path.relpath(os.path.abspath(path), self.root)
        parts = rel.split(os.sep)
        low = rel.lower()
        for pp in self.paths:
            if low == pp or low.startswith(pp + os.sep):
                return "protected path %s\\" % pp
        cur = self.root
        chain = [cur]
        for d in parts[:-1]:
            cur = os.path.join(cur, d)
            chain.append(cur)
        for d in chain:
            mk = self._marker_in(d)
            if mk:
                return "marker %s in %s" % (mk, d)
        for d in parts[:-1]:
            for w in self.words:
                if w in d.lower():
                    return "folder name '%s' contains '%s'" % (d, w)
        if self.match_files:
            for w in self.words:
                if w in parts[-1].lower():
                    return "file name contains '%s'" % w
        return None


class Ctx:
    """Per-run state: the itemized list of every file touched or protected, and (for live runs) the approved plan."""

    def __init__(self, protect=None, approved=None):
        self.items = []  # dicts: action, status, path, size, age_days, note
        self.protect = protect
        self.approved = approved  # None = no gate (dry run). Set of (action, normcased path) for live runs.

    def add(self, action, status, path, size, mtime=None, note=""):
        age = round((dt.datetime.now().timestamp() - mtime) / 86400, 1) if mtime else ""
        self.items.append(dict(action=action, status=status, path=path, size=size, age_days=age, note=note))

    def allowed(self, action, path):
        return self.approved is None or (action, os.path.normcase(path)) in self.approved


def _is_reparse(path):
    """True for symlinks and junctions. Never descend into or delete through these."""
    try:
        st = os.lstat(path)
    except OSError:
        return True
    if stat.S_ISLNK(st.st_mode):
        return True
    return bool(getattr(st, "st_file_attributes", 0) & 0x400)  # FILE_ATTRIBUTE_REPARSE_POINT


def _forbidden(path):
    low = os.path.normcase(os.path.abspath(path)).lower()
    if os.path.splitdrive(low)[0].startswith("e:"):
        return "drive E: is off limits"
    for part in NEVER_PARTS:
        if part in low + "\\":
            return "path contains '%s'" % part.strip("\\/")
    return None


def _inside(path, root):
    p = os.path.normcase(os.path.realpath(path))
    r = os.path.normcase(os.path.realpath(root))
    return p == r or p.startswith(r + os.sep)


class Budget:
    def __init__(self, max_files, max_bytes, parent=None):
        self.max_files, self.max_bytes = max_files, max_bytes
        self.files = self.bytes = 0
        self.hit = None
        self.parent = parent

    def child(self):
        """Each action may use at most half the run cap, so one big folder cannot starve the others."""
        return Budget(max(1, self.max_files // 2), max(1, self.max_bytes // 2), parent=self)

    def room_for(self, size):
        if self.parent is not None and not self.parent.room_for(size):
            self.hit = self.parent.hit
            return False
        if self.files + 1 > self.max_files:
            self.hit = "file cap (%d files)" % self.max_files
            return False
        if self.bytes + size > self.max_bytes:
            self.hit = "byte cap (%.1f GB)" % (self.max_bytes / 1024 ** 3)
            return False
        return True

    def spend(self, size):
        if self.parent is not None:
            self.parent.spend(size)
        self.files += 1
        self.bytes += size


def _fmt(b):
    if b >= 1024 ** 3:
        return "%.2f GB" % (b / 1024 ** 3)
    return "%.1f MB" % (b / 1024 ** 2)


def _free(path):
    try:
        return shutil.disk_usage(path).free
    except OSError:
        return None


def _scan_old_files(root, days, budget_probe=None, skip_dir_names=()):
    """Yield (path, size, newest_time) for regular files older than `days` under root. Never follows reparse points."""
    cutoff = dt.datetime.now().timestamp() - days * 86400
    for dirpath, dirs, files in os.walk(root, topdown=True, followlinks=False):
        keep = []
        for d in dirs:
            full = os.path.join(dirpath, d)
            if d.lower() in skip_dir_names or _is_reparse(full) or _forbidden(full):
                continue
            keep.append(d)
        dirs[:] = keep
        for fn in files:
            p = os.path.join(dirpath, fn)
            if _is_reparse(p) or _forbidden(p):
                continue
            try:
                st = os.lstat(p)
            except OSError:
                continue
            if not stat.S_ISREG(st.st_mode):
                continue
            # newest of modified/created must be older than the cutoff
            if max(st.st_mtime, st.st_ctime) < cutoff:
                yield p, st.st_size, max(st.st_mtime, st.st_ctime)


def _delete_action(title, root, days, budget, live, ctx, action, skip_dir_names=(), protect=None):
    """Shared engine for scratch and temp. Returns (report lines, summary dict)."""
    L = ["### %s" % title]
    res = dict(name=title, done=0, bytes=0, skipped=0, ok=True)
    if not root or not os.path.isdir(root):
        L.append("- target not found: %s (nothing done)" % root)
        res["ok"] = False
        return L, res
    why = _forbidden(root)
    if why:
        L.append("- REFUSED: %s (%s)" % (root, why))
        res["ok"] = False
        return L, res
    free_before = _free(root)
    L.append("- target: %s, older than %d days, mode: %s" % (root, days, "LIVE" if live else "DRY-RUN"))
    shown = 0
    skipped_locked = 0
    protected = 0
    for p, size, mt in _scan_old_files(root, days, skip_dir_names=skip_dir_names):
        if not _inside(p, root):
            continue
        if protect:
            why = protect.why(p)
            if why:
                protected += 1
                ctx.add(action, "PROTECTED", p, size, mt, why)
                continue
        if not ctx.allowed(action, p):
            ctx.add(action, "NOT-IN-APPROVED-PLAN", p, size, mt, "skipped, not in the dry-run log")
            continue
        if not budget.room_for(size):
            L.append("- STOPPED: hit %s. Remaining files wait for the next run." % budget.hit)
            res["hit"] = budget.hit
            break
        if live:
            try:
                os.remove(p)
            except OSError:  # locked, in use, or needs admin: left alone
                skipped_locked += 1
                ctx.add(action, "SKIPPED-LOCKED", p, size, mt)
                continue
        ctx.add(action, "deleted" if live else "would-delete", p, size, mt)
        budget.spend(size)
        res["done"] += 1
        res["bytes"] += size
        if shown < LIST_LIMIT:
            L.append("  - %s %s (%s)" % ("deleted" if live else "would delete", p, _fmt(size)))
            shown += 1
    if res["done"] > shown:
        L.append("  - ... and %d more (full count below)" % (res["done"] - shown))
    res["skipped"] = skipped_locked
    res["protected"] = protected
    if protect:
        L.append("- PROTECTED (older than the cutoff but never touched): %d file(s). Itemized in the run's item log." % protected)
    L.append("- RESULT: %d file(s), %s %s. Skipped as locked or protected: %d." % (
        res["done"], _fmt(res["bytes"]), "freed" if live else "would be freed", skipped_locked))
    free_after = _free(root)
    if free_before is not None and free_after is not None:
        L.append("- before/after free space on %s: %s -> %s" % (os.path.splitdrive(root)[0] or root, _fmt(free_before), _fmt(free_after)))
    return L, res


def _pycache_action(repo, budget, live, ctx):
    L = ["### pycache"]
    res = dict(name="pycache", done=0, bytes=0, skipped=0, ok=True)
    L.append("- target: __pycache__ folders under %s, mode: %s" % (repo, "LIVE" if live else "DRY-RUN"))
    folders = 0
    shown = 0
    stopped = False
    for dirpath, dirs, files in os.walk(repo, topdown=True, followlinks=False):
        dirs[:] = [d for d in dirs if d.lower() != ".git" and not _is_reparse(os.path.join(dirpath, d))
                   and not _forbidden(os.path.join(dirpath, d))]
        if os.path.basename(dirpath) != "__pycache__":
            continue
        if _forbidden(dirpath):
            continue
        emptied = True
        for fn in files:
            p = os.path.join(dirpath, fn)
            if not fn.lower().endswith(".pyc") or _is_reparse(p):
                emptied = False
                continue
            try:
                size = os.path.getsize(p)
            except OSError:
                emptied = False
                continue
            if not budget.room_for(size):
                L.append("- STOPPED: hit %s." % budget.hit)
                res["hit"] = budget.hit
                stopped = True
                emptied = False
                break
            if not ctx.allowed("pycache", p):
                ctx.add("pycache", "NOT-IN-APPROVED-PLAN", p, size)
                emptied = False
                continue
            if live:
                try:
                    os.remove(p)
                except OSError:
                    res["skipped"] += 1
                    emptied = False
                    continue
            ctx.add("pycache", "deleted" if live else "would-delete", p, size, os.path.getmtime(p) if not live else None)
            budget.spend(size)
            res["done"] += 1
            res["bytes"] += size
        if stopped:
            break
        if emptied and (live and not os.listdir(dirpath)):
            try:
                os.rmdir(dirpath)
            except OSError:
                pass
        if shown < LIST_LIMIT:
            L.append("  - %s %s" % ("cleared" if live else "would clear", dirpath))
            shown += 1
        folders += 1
    L.append("- RESULT: %d .pyc file(s) in %d folder(s), %s %s. Skipped: %d." % (
        res["done"], folders, _fmt(res["bytes"]), "freed" if live else "would be freed", res["skipped"]))
    return L, res


def _logrotate_action(repo, days, live, ctx):
    L = ["### logrotate"]
    res = dict(name="logrotate", done=0, bytes=0, skipped=0, ok=True)
    src = os.path.join(repo, "logs", "system-check")
    arc = os.path.join(src, "archive")
    L.append("- target: dated reports older than %d days in %s, moved (never deleted) to %s, mode: %s" % (
        days, src, arc, "LIVE" if live else "DRY-RUN"))
    if not os.path.isdir(src):
        L.append("- target not found (nothing done)")
        return L, res
    today = dt.date.today()
    for fn in sorted(os.listdir(src)):
        m = re.match(r"^(\d{4})-(\d{2})-(\d{2})(?:-[A-Za-z0-9_]+)?\.md$", fn)
        full = os.path.join(src, fn)
        if not m or not os.path.isfile(full) or _is_reparse(full):
            continue  # latest.txt, archive\, anything unexpected stays put
        try:
            age = (today - dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))).days
        except ValueError:
            continue
        if age <= days:
            continue
        size = os.path.getsize(full)
        if not ctx.allowed("logrotate", full):
            ctx.add("logrotate", "NOT-IN-APPROVED-PLAN", full, size, os.path.getmtime(full))
            continue
        ctx.add("logrotate", "moved" if live else "would-move", full, size, os.path.getmtime(full))
        if live:
            try:
                os.makedirs(arc, exist_ok=True)
                dest = os.path.join(arc, fn)
                if os.path.exists(dest):
                    res["skipped"] += 1
                    L.append("  - skipped %s (already in archive, not overwritten)" % fn)
                    continue
                shutil.move(full, dest)
            except OSError as e:
                res["skipped"] += 1
                L.append("  - skipped %s: %s" % (fn, e))
                continue
        res["done"] += 1
        res["bytes"] += size
        L.append("  - %s %s (%d days old)" % ("moved" if live else "would move", fn, age))
    L.append("- RESULT: %d report(s) %s, %s. Skipped: %d." % (
        res["done"], "moved" if live else "would be moved", _fmt(res["bytes"]), res["skipped"]))
    return L, res


PROPOSALS = [
    ("Disk cleanup beyond the four safe actions", "Windows Disk Cleanup, then pick categories by hand", "cleanmgr /d C:"),
    ("Windows Update (install pending updates)", "Settings > Windows Update > Install, or in an elevated shell", "UsoClient StartInstall"),
    ("Drive file-system scan (read-only), only if the I: watch shows errors", "elevated shell, read-only, no repair", "chkdsk I:"),
    ("System file check", "elevated shell, repairs Windows files, Zac decides", "sfc /scannow"),
    ("Startup items review", "Task Manager > Startup apps (Adobe stays as it is)", "taskmgr /0 /startup"),
    ("Power plan (check current)", "read-only view, any change is Zac's call", "powercfg /getactivescheme"),
    ("Defender quick scan", "Windows Security app, or", "Start-MpScan -ScanType QuickScan"),
    ("Driver updates (GPU)", "NVIDIA app or Windows Update, Zac clicks", "nvidia-smi --query-gpu=driver_version --format=csv"),
]


def _execute(repo, cfg, live, only, ctx):
    """Run (or list) the enabled actions. Returns (report lines, results)."""
    L = []
    budget = Budget(int(cfg.get("max_files", 3000)), int(cfg.get("max_bytes", 5 * 1024 ** 3)))
    L.append("Cap this run: %d files and %s (each action may use at most half)." % (budget.max_files, _fmt(budget.max_bytes)))
    if only:
        L.append("Only running: %s (command-line limit)." % ", ".join(sorted(only)))
    L.append("")
    results = []
    acts = cfg.get("actions", {})

    def want(name):
        return acts.get(name, {}).get("enabled", True) and (not only or name in only)

    if want("temp"):
        a = acts.get("temp", {})
        temp = os.environ.get("TEMP") or os.environ.get("TMP")
        home = os.path.normcase(os.path.expanduser("~"))
        if temp and not os.path.normcase(os.path.realpath(temp)).startswith(home + os.sep):
            L += ["### temp", "- REFUSED: %TEMP% (%s) is not under the user profile." % temp, ""]
        else:
            l, r = _delete_action("user TEMP", temp, int(a.get("older_than_days", 7)), budget.child(), live, ctx, "temp",
                                  skip_dir_names=("claude",))
            L += l + [""]
            results.append(r)
    if want("pycache"):
        l, r = _pycache_action(repo, budget.child(), live, ctx)
        L += l + [""]
        results.append(r)
    if want("logrotate"):
        a = acts.get("logrotate", {})
        l, r = _logrotate_action(repo, int(a.get("older_than_days", 90)), live, ctx)
        L += l + [""]
        results.append(r)
    if want("scratch"):
        a = acts.get("scratch", {})
        sroot = os.path.join(repo, "scratch")
        prot = Protect(cfg.get("protect"), sroot)
        L.append("Protect list for scratch: paths %s; folder/file names containing %s; marker files %s." % (
            prot.paths, prot.words, prot.markers))
        l, r = _delete_action("scratch (gitignored)", sroot, int(a.get("older_than_days", 14)), budget.child(), live, ctx,
                              "scratch", protect=prot)
        L += l + [""]
        results.append(r)
    return L, results


def _active_actions(cfg, only):
    acts = cfg.get("actions", {})
    return sorted(n for n in ("temp", "pycache", "logrotate", "scratch")
                  if acts.get(n, {}).get("enabled", True) and (not only or n in only))


def write_item_log(repo, ctx, live, actions):
    """Itemized log of every file: path, size, age. Unique timestamped name, created with 'x' so it can never overwrite."""
    d = os.path.join(repo, "logs", "system-check")
    os.makedirs(d, exist_ok=True)
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    n = 0
    while True:
        name = "fixes-items-%s-%s%s.tsv" % (stamp, "live" if live else "dry", ("-%d" % n) if n else "")
        path = os.path.join(d, name)
        try:
            f = open(path, "x", encoding="utf-8", newline="\n")
            break
        except FileExistsError:
            n += 1
    with f:
        f.write("# wkp safe-fixes item log\n# date: %s\n# mode: %s\n# actions: %s\n" % (
            dt.date.today().isoformat(), "live" if live else "dry-run", ",".join(actions)))
        f.write("# columns: action<TAB>status<TAB>path<TAB>size_bytes<TAB>age_days<TAB>note\n")
        for it in ctx.items:
            f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (it["action"], it["status"], it["path"], it["size"], it["age_days"], it["note"]))
    return path


def _plan_set(ctx):
    return set((it["action"], os.path.normcase(it["path"])) for it in ctx.items if it["status"].startswith("would"))


def _latest_dry_log_today(repo, actions):
    """Newest dry-run item log from today whose actions match. Returns (path, set of (action, path)) or (None, None)."""
    d = os.path.join(repo, "logs", "system-check")
    prefix = "fixes-items-%s-" % dt.date.today().strftime("%Y%m%d")
    if not os.path.isdir(d):
        return None, None
    for fn in sorted((x for x in os.listdir(d) if x.startswith(prefix) and "-dry" in x and x.endswith(".tsv")), reverse=True):
        full = os.path.join(d, fn)
        try:
            lines = open(full, encoding="utf-8").read().splitlines()
        except OSError:
            continue
        hdr = {}
        for l in lines:
            if l.startswith("# ") and ": " in l and not l.startswith("# columns"):
                k, v = l[2:].split(": ", 1)
                hdr[k] = v
        if hdr.get("mode") != "dry-run" or hdr.get("date") != dt.date.today().isoformat():
            continue
        if sorted(hdr.get("actions", "").split(",")) != sorted(actions):
            continue
        plan = set()
        for l in lines:
            if l.startswith("#") or not l.strip():
                continue
            c = l.split("\t")
            if len(c) >= 3 and c[1].startswith("would"):
                plan.add((c[0], os.path.normcase(c[2])))
        return full, plan
    return None, None


def run_fixes(repo, m, force_live=False, force_dry=False, only=None):
    """Returns (report_lines, summary_line, proposals_lines, hard_error_text_or_None)."""
    cfg = m.get("safe_fixes") or {}
    if not cfg.get("enabled"):
        return (["Safe fixes are OFF for this machine (no enabled safe_fixes block in machines.json). Nothing was changed."],
                "fixes OFF", _proposal_lines(), None)
    kill = os.path.join(repo, "data", "system-check-fixes.disabled")
    if os.path.exists(kill):
        return (["KILL SWITCH ACTIVE: %s exists. No fixes ran. Delete that file to re-enable." % kill],
                "fixes STOPPED by kill switch", _proposal_lines(), None)
    live = (cfg.get("mode", "dry-run") == "live") and not force_dry
    if force_live:
        live = True
    if force_dry:
        live = False
    actions = _active_actions(cfg, only)
    L = ["Mode: **%s**. Kill switch file: %s (not present)." % ("LIVE" if live else "DRY-RUN (deletes nothing)", kill)]
    approved = None
    if live:
        # HARD RULE: a live run needs today's matching dry-run log, and the plan must match it exactly.
        plan_ctx = Ctx()
        _execute(repo, cfg, False, only, plan_ctx)  # planning pass, deletes nothing, not logged as a run
        plan = _plan_set(plan_ctx)
        logp, logged = _latest_dry_log_today(repo, actions)
        if logp is None:
            return (L + ["**LIVE RUN REFUSED.** No dry-run item log from today for actions %s in logs\\system-check\\. "
                         "Run a dry run first (--fixes-dry-run), read the log, then run live the same day. Nothing was changed." % ",".join(actions)],
                    "fixes LIVE REFUSED: no dry-run log today", _proposal_lines(), None)
        if plan != logged:
            extra, gone = plan - logged, logged - plan
            ex = ["  - now planned but not in the dry-run log: %s" % x[1] for x in sorted(extra)[:10]]
            ex += ["  - in the dry-run log but not planned now: %s" % x[1] for x in sorted(gone)[:10]]
            return (L + ["**LIVE RUN REFUSED.** The planned deletions do not match %s (%d planned now, %d in the log; %d new, %d gone). "
                         "Run a fresh dry run, read it, then go live. Nothing was changed." % (
                             os.path.basename(logp), len(plan), len(logged), len(extra), len(gone))] + ex,
                    "fixes LIVE REFUSED: plan does not match dry-run log", _proposal_lines(), None)
        L.append("Live gate passed: plan matches %s (%d items)." % (os.path.basename(logp), len(plan)))
        approved = plan
    ctx = Ctx(approved=approved)
    l, results = _execute(repo, cfg, live, only, ctx)
    L += l
    itempath = write_item_log(repo, ctx, live, actions)
    prot = sum(1 for it in ctx.items if it["status"] == "PROTECTED")
    L.append("**Itemized log (every file, path, size, age): %s**" % itempath)
    tf = sum(r["done"] for r in results)
    tb = sum(r["bytes"] for r in results)
    L.append("**TOTAL (real counts from this run): %d item(s), %s %s.** Protected and left alone: %d file(s).%s" % (
        tf, _fmt(tb), "freed or moved" if live else "would be freed or moved (nothing changed)", prot,
        (" An action stopped early at its cap: " + "; ".join(sorted(set(r.get("hit") for r in results if r.get("hit")))) + ".") if any(r.get("hit") for r in results) else ""))
    summary = "fixes %s: %d item(s), %s, %d protected" % ("LIVE" if live else "dry-run", tf, _fmt(tb), prot)
    return L, summary, _proposal_lines(), None


def _proposal_lines():
    L = ["PROPOSAL ONLY. This check never runs any of these. Each needs Zac (and some need an elevated shell).", ""]
    for what, how, cmd in PROPOSALS:
        L.append("- %s: %s. Command: `%s`" % (what, how, cmd))
    L.append("")
    L.append("HARD NEVER, not even proposed as automatic: anything Adobe, drive E:, user files outside scratch, "
             "Defender or Malwarebytes settings, git history, env vars, scheduled tasks, anything needing admin.")
    return L
