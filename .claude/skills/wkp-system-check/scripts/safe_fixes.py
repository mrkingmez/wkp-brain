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

NEVER_PARTS = ("adobe", "malwarebytes", "windows defender", "defender", "\\.git\\", "/.git/")
LIST_LIMIT = 40  # file lines shown per action; counts are always exact


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
    """Yield (path, size) for regular files older than `days` under root. Never follows reparse points."""
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
                yield p, st.st_size


def _delete_action(title, root, days, budget, live, skip_dir_names=()):
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
    for p, size in _scan_old_files(root, days, skip_dir_names=skip_dir_names):
        if not _inside(p, root):
            continue
        if not budget.room_for(size):
            L.append("- STOPPED: hit %s. Remaining files wait for the next run." % budget.hit)
            res["hit"] = budget.hit
            break
        if live:
            try:
                os.remove(p)
            except PermissionError:
                skipped_locked += 1  # locked, in use, or needs admin: left alone
                continue
            except OSError:
                skipped_locked += 1
                continue
        budget.spend(size)
        res["done"] += 1
        res["bytes"] += size
        if shown < LIST_LIMIT:
            L.append("  - %s %s (%s)" % ("deleted" if live else "would delete", p, _fmt(size)))
            shown += 1
    if res["done"] > shown:
        L.append("  - ... and %d more (full count below)" % (res["done"] - shown))
    res["skipped"] = skipped_locked
    L.append("- RESULT: %d file(s), %s %s. Skipped as locked or protected: %d." % (
        res["done"], _fmt(res["bytes"]), "freed" if live else "would be freed", skipped_locked))
    free_after = _free(root)
    if free_before is not None and free_after is not None:
        L.append("- before/after free space on %s: %s -> %s" % (os.path.splitdrive(root)[0] or root, _fmt(free_before), _fmt(free_after)))
    return L, res


def _pycache_action(repo, budget, live):
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
            if live:
                try:
                    os.remove(p)
                except OSError:
                    res["skipped"] += 1
                    emptied = False
                    continue
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


def _logrotate_action(repo, days, live):
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


def run_fixes(repo, m, force_live=False, force_dry=False, only=None):
    """Returns (report_lines, summary_line, proposals_lines, hard_error_text_or_None)."""
    cfg = m.get("safe_fixes") or {}
    L = []
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
    budget = Budget(int(cfg.get("max_files", 3000)), int(cfg.get("max_bytes", 5 * 1024 ** 3)))
    L.append("Mode: **%s**. Cap this run: %d files and %s (each action may use at most half). Kill switch file: %s (not present)." % (
        "LIVE" if live else "DRY-RUN (deletes nothing)", budget.max_files, _fmt(budget.max_bytes), kill))
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
            l, r = _delete_action("user TEMP", temp, int(a.get("older_than_days", 7)), budget.child(), live, skip_dir_names=("claude",))
            L += l + [""]
            results.append(r)
    if want("pycache"):
        l, r = _pycache_action(repo, budget.child(), live)
        L += l + [""]
        results.append(r)
    if want("logrotate"):
        a = acts.get("logrotate", {})
        l, r = _logrotate_action(repo, int(a.get("older_than_days", 90)), live)
        L += l + [""]
        results.append(r)
    if want("scratch"):
        a = acts.get("scratch", {})
        l, r = _delete_action("scratch (gitignored)", os.path.join(repo, "scratch"), int(a.get("older_than_days", 14)), budget.child(), live)
        L += l + [""]
        results.append(r)
    tf = sum(r["done"] for r in results)
    tb = sum(r["bytes"] for r in results)
    L.append("**TOTAL (real counts from this run): %d item(s), %s %s.**%s" % (
        tf, _fmt(tb), "freed or moved" if live else "would be freed or moved (nothing changed)",
        (" An action stopped early at its cap: " + "; ".join(sorted(set(r.get("hit") for r in results if r.get("hit")))) + ".") if any(r.get("hit") for r in results) else ""))
    summary = "fixes %s: %d item(s), %s" % ("LIVE" if live else "dry-run", tf, _fmt(tb))
    return L, summary, _proposal_lines(), None


def _proposal_lines():
    L = ["PROPOSAL ONLY. This check never runs any of these. Each needs Zac (and some need an elevated shell).", ""]
    for what, how, cmd in PROPOSALS:
        L.append("- %s: %s. Command: `%s`" % (what, how, cmd))
    L.append("")
    L.append("HARD NEVER, not even proposed as automatic: anything Adobe, drive E:, user files outside scratch, "
             "Defender or Malwarebytes settings, git history, env vars, scheduled tasks, anything needing admin.")
    return L
