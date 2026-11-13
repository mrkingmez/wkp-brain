#!/usr/bin/env python3
"""system_check.py - read-only system check of this machine (WKP nightly check).

Replaces the old "nightly rollup" as the machine-health half; the director-log
rollup half is kept as section 12 (logs touched in the last 24 hours, open
decisions). The checks are read-only. The only changes possible are the SAFE FIXES
tier (section 13, scripts/safe_fixes.py, allowlist of four, config-driven, off
unless enabled per machine, dry-run first). No installs, no setting changes, no scheduled
task registration, nothing under Adobe is touched (only an existence check on
the Premiere install folder, and Adobe scheduled tasks are never queried).

Usage:
    python system_check.py                 # check, write report, print one-line status
    python system_check.py --no-updates    # skip the Windows Update search (slow)
    python system_check.py --stdout        # also print the full report
    python system_check.py --fixes-dry-run # safe fixes: list only, delete nothing (overrides config)
    python system_check.py --fixes-live    # safe fixes: really run (only if enabled in machines.json)
    python system_check.py --fixes-only scratch   # limit safe fixes to named actions (scratch,temp,pycache,logrotate)

Output:
    D:\\WKP\\logs\\system-check\\YYYY-MM-DD.md   (full dated report)
    D:\\WKP\\logs\\system-check\\latest.txt      (the one-line status)
Exit code: 0 GREEN, 1 YELLOW, 2 RED.

Honesty rule: anything that could not be read is reported "not available" and
names why. Env vars are reported PRESENT/MISSING by name, never by value.
"""
import datetime as dt
import glob
import json
import os
import re
import shutil
import socket
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
CONFIG = os.path.join(os.path.dirname(HERE), "machines.json")

GREEN, YELLOW, RED = 0, 1, 2
NAMES = {GREEN: "GREEN", YELLOW: "YELLOW", RED: "RED"}

findings = []   # (level, section, text)
sections = []   # (title, [lines])


def add(level, section, text):
    findings.append((level, section, text))


def run(cmd, timeout=60, shell=False):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, shell=shell,
                           encoding="utf-8", errors="replace")
        return p.returncode, (p.stdout or "").strip(), (p.stderr or "").strip()
    except subprocess.TimeoutExpired:
        return 124, "", "timed out after %ss" % timeout
    except Exception as e:  # noqa
        return 125, "", str(e)


def ps(script, timeout=60):
    return run(["powershell", "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass",
                "-Command", script], timeout=timeout)


def ps_json(script, timeout=60):
    rc, out, err = ps(script + " | ConvertTo-Json -Compress -Depth 4", timeout)
    if rc != 0 or not out:
        return None, (err or "no output (rc=%s)" % rc)
    try:
        data = json.loads(out)
        if isinstance(data, dict):
            data = [data]
        return data, None
    except Exception as e:  # noqa
        return None, "bad json: %s" % e


def load_config():
    with open(CONFIG, encoding="utf-8") as f:
        cfg = json.load(f)
    name = socket.gethostname().upper()
    m = cfg["machines"].get(name)
    configured = m is not None
    if not configured:
        m = dict(cfg["default"])
    return name, configured, m


def _evdate(v):
    m_ = re.search(r"/Date\((-?\d+)\)/", str(v))
    if m_:
        return dt.datetime.fromtimestamp(int(m_.group(1)) / 1000.0)
    try:
        return dt.datetime.fromisoformat(str(v)[:19])
    except ValueError:
        return None


def fmt_gb(b):
    return "%.1f GB" % (b / 1024 ** 3)


# ---------------------------------------------------------------- sections
def sec_machine(name, configured, m, repo):
    L = ["Machine name: %s" % name, "Config label: %s" % m.get("label"),
         "Report time: %s" % dt.datetime.now().strftime("%Y-%m-%d %H:%M")]
    if not configured:
        add(YELLOW, "Machine", "No block for %s in machines.json, using defaults. Add one to get full checks." % name)
    lp = os.path.join(repo, "LOCAL-PATHS.md")
    heads = []
    try:
        with open(lp, encoding="utf-8", errors="replace") as f:
            heads = [l.strip() for l in f if l.startswith("## MACHINE:")]
    except OSError as e:
        add(YELLOW, "Machine", "LOCAL-PATHS.md not readable: %s" % e)
    L.append("LOCAL-PATHS.md machine sections: %s" % (", ".join(h[3:] for h in heads) or "none found"))
    sect = m.get("local_paths_section")
    if configured and sect and not any(sect.lower() in h.lower() for h in heads):
        add(YELLOW, "Machine", "machines.json says LOCAL-PATHS section '%s' but LOCAL-PATHS.md has no such header." % sect)
    sections.append(("1. Machine", L))


def sec_disks(m):
    L = []
    data, err = ps_json("Get-Volume | Where-Object DriveLetter | Select-Object DriveLetter,FileSystemLabel,Size,SizeRemaining,HealthStatus,OperationalStatus")
    if data is None:
        L.append("Get-Volume not available: %s" % err)
        add(YELLOW, "Disk space", "Could not read volumes: %s" % err)
        sections.append(("2. Disk space (all drives)", L))
        return
    byl = {str(d["DriveLetter"]).upper(): d for d in data}
    warn, red = m.get("disk_warn_free_pct", 15), m.get("disk_red_free_pct", 5)
    L.append("| Drive | Label | Free | Total | Free % | Health |")
    L.append("|---|---|---|---|---|---|")
    for dl in m.get("drives", []):
        d = byl.get(dl.upper())
        if not d:
            L.append("| %s: | not mounted | | | | |" % dl)
            add(YELLOW, "Disk space", "%s: not mounted or not visible" % dl)
            continue
        size, free = d.get("Size") or 0, d.get("SizeRemaining") or 0
        pct = (100.0 * free / size) if size else 0
        L.append("| %s: | %s | %s | %s | %.1f%% | %s |" % (dl, d.get("FileSystemLabel") or "", fmt_gb(free), fmt_gb(size), pct, d.get("HealthStatus")))
        if dl.upper() in [x.upper() for x in m.get("info_only_drives", [])]:
            if pct < warn:
                L.append("  (%s: is info-only in machines.json: %s)" % (dl, m.get("info_only_note", "not scored")))
        elif pct < red and free < 100 * 1024 ** 3:
            add(RED, "Disk space", "%s: only %.1f%% free (%s)" % (dl, pct, fmt_gb(free)))
        elif pct < warn and free < 250 * 1024 ** 3:
            add(YELLOW, "Disk space", "%s: %.1f%% free (%s)" % (dl, pct, fmt_gb(free)))
        if str(d.get("HealthStatus")).lower() not in ("healthy", "0", "none", "null"):
            add(YELLOW, "Disk space", "%s: volume HealthStatus = %s" % (dl, d.get("HealthStatus")))
    sections.append(("2. Disk space (all drives)", L))


def sec_drive_watch(m):
    L = []
    days = int(m.get("event_days", 14))
    for dl in m.get("watch_drives", []):
        L.append("Watching %s: (disk/NTFS/volmgr error events, last %d days)" % (dl, days))
        # Disk and file-system error events. 7 bad block, 11 controller error, 15 not ready, 51 paging error,
        # 55 corrupt file system, 98 volume check, 129 reset, 153 retried IO, 140 NTFS flush failed, 137 etc.
        script = ("$s=(Get-Date).AddDays(-%d); Get-WinEvent -FilterHashtable @{LogName='System';StartTime=$s;"
                  "ProviderName='disk','Ntfs','volmgr','stornvme','storahci','Microsoft-Windows-Ntfs'} -ErrorAction SilentlyContinue "
                  "| Where-Object { $_.LevelDisplayName -in 'Error','Warning','Critical' } "
                  "| Select-Object TimeCreated,Id,ProviderName,LevelDisplayName,@{n='Msg';e={($_.Message -split \"`n\")[0]}}" % days)
        data, err = ps_json(script, timeout=90)
        if data is None:
            # Get-WinEvent returns nothing when there are no events; empty output is not an error
            rc, out, e2 = ps(script, timeout=90)
            if rc == 0 and not out:
                data = []
            else:
                L.append("Event log not available: %s" % err)
                add(YELLOW, "I: watch", "Event log read failed: %s" % err)
                continue
        all_ev = data
        mine = [e for e in all_ev if re.search(r"\b%s:|\\Device\\Harddisk|Harddisk" % dl, str(e.get("Msg")), re.I) or True]
        # Event messages rarely name the drive letter, so report all disk-class events and flag by volume match where possible
        tagged = [e for e in all_ev if re.search(r"(^|[^A-Za-z])%s:" % dl, str(e.get("Msg")), re.I)]
        L.append("Disk/NTFS error or warning events in window: %d total, %d naming %s:" % (len(all_ev), len(tagged), dl))
        groups = {}
        for e in all_ev:
            k = (e.get("Id"), e.get("ProviderName"), str(e.get("Msg"))[:90])
            g = groups.setdefault(k, [0, None])
            g[0] += 1
            t = _evdate(e.get("TimeCreated"))
            if t and (g[1] is None or t > g[1]):
                g[1] = t
        for (eid, prov, msg), (cnt, last) in sorted(groups.items(), key=lambda kv: -kv[1][0])[:8]:
            L.append("  - id %s %s x%d, latest %s: %s" % (eid, prov, cnt, last.strftime("%Y-%m-%d %H:%M") if last else "n/a", msg))
        if tagged:
            add(RED if len(tagged) >= 3 else YELLOW, "I: watch", "%d disk/NTFS events name %s: in the last %d days" % (len(tagged), dl, days))
        elif all_ev:
            add(YELLOW, "I: watch", "%d disk-class error/warning events in last %d days (none name %s: directly, see report)" % (len(all_ev), days, dl))
        # dirty bit (needs admin, may fail)
        rc, out, err2 = run(["fsutil", "dirty", "query", "%s:" % dl], timeout=20)
        if rc == 0 and out:
            L.append("fsutil dirty query %s: -> %s" % (dl, out.splitlines()[0]))
            if "NOT Dirty" not in out and "is Dirty" in out:
                add(RED, "I: watch", "%s: volume is marked dirty (chkdsk pending)" % dl)
        else:
            L.append("Dirty bit not available (fsutil needs an elevated shell): %s" % (err2 or out or "rc=%s" % rc))
        L.append("Note: 'chkdsk' and any repair are Zac's call, this check never runs them.")
    if not m.get("watch_drives"):
        L.append("No watch drives configured.")
    sections.append(("3. I: errors watch", L))


def sec_smart():
    L = []
    data, err = ps_json("Get-PhysicalDisk | Select-Object FriendlyName,MediaType,BusType,HealthStatus,OperationalStatus,@{n='SizeGB';e={[math]::Round($_.Size/1GB)}}")
    if data is None:
        L.append("Get-PhysicalDisk not available: %s" % err)
        add(YELLOW, "Drive health", "Get-PhysicalDisk failed: %s" % err)
    else:
        L.append("| Disk | Type | Bus | Size GB | Health | Operational |")
        L.append("|---|---|---|---|---|---|")
        for d in data:
            L.append("| %s | %s | %s | %s | %s | %s |" % (d.get("FriendlyName"), d.get("MediaType"), d.get("BusType"), d.get("SizeGB"), d.get("HealthStatus"), d.get("OperationalStatus")))
            h = str(d.get("HealthStatus"))
            if h not in ("Healthy", "0"):
                add(RED if h in ("Unhealthy", "2") else YELLOW, "Drive health", "%s HealthStatus = %s" % (d.get("FriendlyName"), h))
    rel, err = ps_json("Get-PhysicalDisk | Get-StorageReliabilityCounter | Select-Object DeviceId,Temperature,Wear,ReadErrorsTotal,WriteErrorsTotal,PowerOnHours")
    if rel is None:
        L.append("SMART counters (Get-StorageReliabilityCounter) not available, usually needs an elevated shell: %s" % (err or "").splitlines()[0:1])
    else:
        L.append("SMART counters:")
        for r in rel:
            L.append("  - disk %s: temp %s C, wear %s, read errs %s, write errs %s, power-on %s h" % (r.get("DeviceId"), r.get("Temperature"), r.get("Wear"), r.get("ReadErrorsTotal"), r.get("WriteErrorsTotal"), r.get("PowerOnHours")))
            for k in ("ReadErrorsTotal", "WriteErrorsTotal"):
                if (r.get(k) or 0) > 0:
                    add(YELLOW, "Drive health", "disk %s %s = %s" % (r.get("DeviceId"), k, r.get(k)))
    sections.append(("4. Drive health (SMART via Get-PhysicalDisk)", L))


def sec_gpu_ram_cpu():
    L = []
    smi = shutil.which("nvidia-smi")
    if not smi:
        L.append("nvidia-smi not found: GPU/CUDA not visible.")
        add(RED, "GPU", "nvidia-smi not found, GPU/CUDA not visible")
    else:
        rc, out, err = run([smi, "--query-gpu=name,driver_version,memory.used,memory.total,temperature.gpu,utilization.gpu", "--format=csv,noheader"], 20)
        if rc != 0 or not out:
            L.append("nvidia-smi failed: %s" % (err or rc))
            add(RED, "GPU", "nvidia-smi failed: %s" % (err or rc))
        else:
            L.append("GPU: " + out.splitlines()[0])
            parts = [p.strip() for p in out.splitlines()[0].split(",")]
            try:
                t = int(parts[4])
                if t >= 85:
                    add(RED, "GPU", "GPU temp %s C" % t)
                elif t >= 75:
                    add(YELLOW, "GPU", "GPU temp %s C" % t)
            except (ValueError, IndexError):
                pass
        rc, out, err = run([smi], 20)
        m = re.search(r"CUDA (?:UMD )?Version:\s*([\d.]+)", out or "")
        L.append("CUDA runtime reported by driver: %s" % (m.group(1) if m else "not available"))
        if not m:
            add(YELLOW, "GPU", "CUDA version not reported by nvidia-smi")
    ram, err = ps_json("Get-CimInstance Win32_OperatingSystem | Select-Object TotalVisibleMemorySize,FreePhysicalMemory")
    if ram:
        tot, free = ram[0]["TotalVisibleMemorySize"] * 1024, ram[0]["FreePhysicalMemory"] * 1024
        pct = 100.0 * free / tot
        L.append("RAM: %s free of %s (%.0f%% free)" % (fmt_gb(free), fmt_gb(tot), pct))
        if pct < 5:
            add(RED, "RAM", "Only %.0f%% RAM free" % pct)
        elif pct < 12:
            add(YELLOW, "RAM", "Only %.0f%% RAM free (close big apps before transcribing)" % pct)
    else:
        L.append("RAM not available: %s" % err)
        add(YELLOW, "RAM", "Could not read RAM: %s" % err)
    cpu, err = ps_json("Get-CimInstance Win32_Processor | Select-Object Name,LoadPercentage")
    if cpu:
        L.append("CPU: %s, load %s%%" % (cpu[0].get("Name"), cpu[0].get("LoadPercentage")))
    temp, err = ps_json("Get-CimInstance -Namespace root/wmi -ClassName MSAcpi_ThermalZoneTemperature -ErrorAction Stop | Select-Object CurrentTemperature")
    if temp:
        c = temp[0]["CurrentTemperature"] / 10.0 - 273.15
        L.append("CPU/ACPI thermal zone: %.0f C" % c)
        if c >= 90:
            add(RED, "CPU", "ACPI temp %.0f C" % c)
        elif c >= 80:
            add(YELLOW, "CPU", "ACPI temp %.0f C" % c)
    else:
        L.append("CPU temp not available (no ACPI thermal zone exposed; needs a sensor tool, still open in TASKS.md PC health row).")
    sections.append(("5. GPU/CUDA, RAM, CPU", L))


def sec_security(skip_updates):
    L = []
    d, err = ps_json("Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureAge,QuickScanAge")
    av, _e = ps_json("Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntiVirusProduct | Select-Object displayName,productState")
    others = []
    for a_ in (av or []):
        st = int(a_.get("productState") or 0)
        on = ((st >> 12) & 0xF) == 1
        others.append("%s (%s)" % (a_.get("displayName"), "on" if on else "off/unknown"))
    if d:
        d = d[0]
        sig = d.get("AntivirusSignatureAge")
        qs = d.get("QuickScanAge")
        sig_t = "n/a" if (sig is None or sig >= 65535) else "%s day(s)" % sig
        qs_t = "n/a" if (qs is None or qs >= 4000000) else "%s day(s) ago" % qs
        L.append("Defender: AV enabled=%s, real-time=%s, signature age=%s, last quick scan %s" % (d.get("AntivirusEnabled"), d.get("RealTimeProtectionEnabled"), sig_t, qs_t))
        L.append("Security Center AV products: %s" % ("; ".join(others) or "none reported"))
        if not d.get("RealTimeProtectionEnabled"):
            other_on = [o for o in others if "Defender" not in o and "(on)" in o]
            if other_on:
                L.append("Defender real-time is off because another AV is active: %s." % ", ".join(other_on))
            else:
                add(RED, "Defender", "Real-time protection is OFF and no other active AV is reported")
        else:
            if sig is not None and 7 < sig < 65535:
                add(YELLOW, "Defender", "Signatures %s days old" % sig)
            if qs is not None and 14 < qs < 4000000:
                add(YELLOW, "Defender", "Last quick scan %s days ago" % qs)
    else:
        L.append("Defender status not available: %s" % err)
        add(YELLOW, "Defender", "Get-MpComputerStatus failed (third-party AV, or no permission): %s" % err)
    reboot, _ = ps_json("$r=@(); if(Test-Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\RebootRequired'){$r+='WindowsUpdate'}; if(Test-Path 'HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Component Based Servicing\\RebootPending'){$r+='CBS'}; [pscustomobject]@{Pending=($r -join ',')}")
    if reboot is not None:
        p = reboot[0].get("Pending")
        L.append("Pending reboot: %s" % (p or "no"))
        if p:
            add(YELLOW, "Windows Update", "Reboot pending (%s)" % p)
    if skip_updates:
        L.append("Windows Update search skipped (--no-updates).")
    else:
        script = ("$s=New-Object -ComObject Microsoft.Update.Session; $q=$s.CreateUpdateSearcher(); "
                  "$r=$q.Search('IsInstalled=0 and IsHidden=0'); "
                  "$r.Updates | ForEach-Object { [pscustomobject]@{Title=$_.Title;Sec=($_.MsrcSeverity)} }")
        rc, out, err = ps(script + " | ConvertTo-Json -Compress", timeout=120)
        if rc == 124:
            L.append("Windows Update search not available: timed out.")
            add(YELLOW, "Windows Update", "Update search timed out")
        elif rc != 0:
            L.append("Windows Update search not available: %s" % err[:150])
            add(YELLOW, "Windows Update", "Update search failed")
        else:
            try:
                ups = json.loads(out) if out else []
                if isinstance(ups, dict):
                    ups = [ups]
            except Exception:  # noqa
                ups = []
            L.append("Pending Windows updates: %d" % len(ups))
            for u in ups[:8]:
                L.append("  - %s [%s]" % (u.get("Title"), u.get("Sec") or "unrated"))
            crit = [u for u in ups if str(u.get("Sec")) in ("Critical", "Important")]
            if crit:
                add(YELLOW, "Windows Update", "%d Critical/Important update(s) pending" % len(crit))
            elif len(ups) > 10:
                add(YELLOW, "Windows Update", "%d updates pending" % len(ups))
    sections.append(("6. Windows Update and Defender", L))


def git(repo, *args, timeout=60):
    return run(["git", "-C", repo] + list(args), timeout=timeout)


def sec_backups(m, repo):
    L = []
    rd = m.get("reports_dir")
    rd = os.path.normpath(rd) if rd else rd
    if rd:
        if os.path.isdir(rd):
            n, newest = 0, 0.0
            for root, dirs, files in os.walk(rd):
                dirs[:] = [d for d in dirs if d != "_Archive"]
                for fn in files:
                    n += 1
                    try:
                        newest = max(newest, os.path.getmtime(os.path.join(root, fn)))
                    except OSError:
                        pass
            age = (dt.datetime.now().timestamp() - newest) / 86400 if newest else None
            L.append("%s: %d files, newest edit %s" % (rd, n, ("%.1f days ago" % age) if age is not None else "n/a"))
            inside_repo = os.path.normcase(os.path.abspath(rd)).startswith(os.path.normcase(os.path.abspath(repo)) + os.sep)
            L.append("Is it inside a git repo (backed up by push)? %s. It is NOT in git: a second copy does not exist unless Zac makes one." % ("yes" if inside_repo else "no"))
            if not inside_repo:
                add(YELLOW, "Backups", "%s (%d deliverable files) is not in git and has no second copy" % (rd, n))
        else:
            L.append("%s not found." % rd)
            add(YELLOW, "Backups", "%s not found" % rd)
    rc, out, err = git(repo, "status", "--porcelain")
    if rc != 0:
        L.append("git status failed: %s" % err)
        add(RED, "Backups", "git status failed: %s" % err)
    else:
        lines = out.splitlines()
        mod = sum(1 for l in lines if not l.startswith("??"))
        unt = sum(1 for l in lines if l.startswith("??"))
        L.append("git working tree: %d modified/staged, %d untracked" % (mod, unt))
        if mod + unt > 150:
            add(RED, "Backups", "%d uncommitted changes, commit and push soon" % (mod + unt))
        elif mod + unt > 40:
            add(YELLOW, "Backups", "%d uncommitted changes" % (mod + unt))
    rc, out, err = git(repo, "rev-list", "--left-right", "--count", "origin/main...HEAD")
    if rc == 0 and out:
        behind, ahead = out.split()
        L.append("vs origin/main (last fetched state): %s behind, %s ahead (unpushed commits)" % (behind, ahead))
        if int(ahead) > 0:
            add(YELLOW, "Backups", "%s unpushed commit(s)" % ahead)
    rc, out, err = git(repo, "log", "-1", "--format=%cI|%s")
    if rc == 0 and out:
        L.append("Last commit: %s" % out.replace("|", " | "))
    rc, out, err = git(repo, "log", "-1", "--format=%cI|%s", "origin/main")
    last_push = None
    if rc == 0 and out:
        L.append("Last commit on origin/main (what GitHub holds, as of last fetch): %s" % out.replace("|", " | "))
        try:
            last_push = dt.datetime.fromisoformat(out.split("|")[0])
        except ValueError:
            pass
    rc, out, err = git(repo, "reflog", "show", "origin/main", "-1", "--date=iso", "--format=%gd %gs")
    if rc == 0 and out:
        L.append("Remote ref last updated (push/fetch): %s" % out)
    if last_push:
        age = (dt.datetime.now(last_push.tzinfo) - last_push).total_seconds() / 86400
        if age > 7:
            add(RED, "Backups", "Nothing pushed to origin/main for %.0f days" % age)
        elif age > 3:
            add(YELLOW, "Backups", "Last commit on origin/main is %.0f days old" % age)
    else:
        add(YELLOW, "Backups", "Last push date not available")
    sections.append(("7. Backups", L))


def sec_tasks(m):
    L = []
    prefs = m.get("task_prefixes", ["WKP"])
    cond = " -or ".join("$_.TaskName -like '%s*'" % p for p in prefs)
    data, err = ps_json("Get-ScheduledTask | Where-Object { (%s) -and $_.TaskPath -eq '\\' } | ForEach-Object { $i=Get-ScheduledTaskInfo $_; [pscustomobject]@{Name=$_.TaskName;State=[string]$_.State;Last=[string]$i.LastRunTime;Result=$i.LastTaskResult;Next=[string]$i.NextRunTime} }" % cond)
    if data is None:
        rc, out, _ = ps("Get-ScheduledTask | Where-Object { (%s) } | Measure-Object | Select -Expand Count" % cond)
        if rc == 0 and out.strip() == "0":
            L.append("No scheduled tasks with prefix %s." % prefs)
            add(YELLOW, "Scheduled tasks", "No WKP scheduled tasks found")
        else:
            L.append("Scheduled tasks not available: %s" % err)
            add(YELLOW, "Scheduled tasks", "Could not read: %s" % err)
    else:
        L.append("| Task | State | Last run | Last result | Next run |")
        L.append("|---|---|---|---|---|")
        for t in data:
            L.append("| %s | %s | %s | %s | %s |" % (t["Name"], t["State"], t["Last"], t["Result"], t["Next"]))
            res = t.get("Result")
            acc = m.get("accepted_task_failures", {}).get(t["Name"])
            if res not in (0, None, 267011, 267009, 267010):
                if acc and str(t["Last"]).startswith(acc):
                    L.append("  (%s last result %s on %s is an ACCEPTED failure, Zac 2026-11-12: acceptable occasionally)" % (t["Name"], res, acc))
                else:
                    add(YELLOW, "Scheduled tasks", "%s last result %s (nonzero, last run %s)" % (t["Name"], res, t["Last"]))
            if t["Name"] in m.get("retired_tasks", []) and t["State"] != "Disabled":
                add(YELLOW, "Scheduled tasks", "%s is RETIRED but still enabled (Zac approves the disable command)" % t["Name"])
            if t["State"] == "Disabled":
                L.append("  (%s is Disabled)" % t["Name"])
        L.append("Adobe tasks are deliberately not queried (Adobe is off limits).")
    sections.append(("8. Scheduled tasks (WKP only)", L))


def sec_tools(m):
    L = []
    for name, path in m.get("tools", {}).items():
        if path.startswith("glob:"):
            hits = glob.glob(path[5:])
            ok = bool(hits)
            shown = ", ".join(os.path.basename(h) for h in hits) if hits else path[5:]
        else:
            ok = os.path.exists(path)
            shown = path
        L.append("%s %s: %s" % ("OK     " if ok else "MISSING", name, shown))
        if not ok:
            add(RED if name in ("python", "ffmpeg") else YELLOW, "Key tools", "%s not found at %s" % (name, shown))
    # python version actually runs
    py = m.get("tools", {}).get("python")
    if py and os.path.exists(py):
        rc, out, err = run([py, "--version"], 15)
        L.append("python --version -> %s" % (out or err))
    ff = m.get("tools", {}).get("ffmpeg")
    if ff and os.path.exists(ff):
        rc, out, err = run([ff, "-version"], 15)
        L.append("ffmpeg -> %s" % (out.splitlines()[0] if out else err))
    sections.append(("9. Key tools (installed paths exist)", L))


def sec_env(m):
    L = ["Names only. Values are never read into this report."]
    names = list(m.get("env_names", []))
    for n in names:
        present = bool(os.environ.get(n))
        if not present:
            rc, out, _ = ps("[Environment]::GetEnvironmentVariable('%s','User')" % n)
            present = bool(out.strip())
        L.append("%s %s" % ("PRESENT" if present else "MISSING", n))
        if not present:
            add(YELLOW, "Env vars", "%s is MISSING" % n)
    for pre in m.get("env_prefixes", []):
        rc, out, _ = ps("[Environment]::GetEnvironmentVariables('User').Keys | Where-Object { $_ -like '%s*' } | Sort-Object" % pre)
        got = [x for x in out.splitlines() if x.strip()]
        got += [k for k in os.environ if k.startswith(pre) and k not in got]
        L.append("%s* : %d present (%s)" % (pre, len(got), ", ".join(sorted(set(got))) or "none"))
    sections.append(("10. Environment variables (PRESENT/MISSING)", L))


def sec_repo(repo):
    L = []
    rc, out, err = git(repo, "grep", "-l", "-E", "^(<<<<<<< |>>>>>>> )", "--", "*.md", "*.py", "*.json", ":(exclude)_archive", ":(exclude)scratch")
    files = [f for f in out.splitlines() if f.strip()]
    L.append("Merge-conflict markers in tracked files: %d" % len(files))
    for f in files[:6]:
        L.append("  - %s" % f)
    if files:
        add(RED, "Repo hygiene", "%d tracked file(s) contain merge-conflict markers: %s" % (len(files), ", ".join(files[:3])))
    if os.path.exists(os.path.join(repo, ".git", "index.lock")):
        L.append("index.lock exists (a git process died or is running).")
        add(YELLOW, "Repo hygiene", ".git/index.lock present")
    # large untracked, non-ignored files
    rc, out, err = git(repo, "ls-files", "-o", "--exclude-standard")
    big = []
    for rel in out.splitlines():
        p = os.path.join(repo, rel)
        try:
            sz = os.path.getsize(p)
        except OSError:
            continue
        if sz > 50 * 1024 * 1024:
            big.append((sz, rel))
    L.append("Untracked, not-ignored files over 50 MB: %d" % len(big))
    for sz, rel in sorted(big, reverse=True)[:5]:
        L.append("  - %s (%s)" % (rel, fmt_gb(sz)))
    if big:
        add(YELLOW, "Repo hygiene", "%d large untracked file(s) that would be committed by 'git add -A' (e.g. %s)" % (len(big), big[0][1]))
    # secrets-shaped filenames tracked
    rc, out, err = git(repo, "ls-files")
    risky = [f for f in out.splitlines() if re.search(r"(^|/)(\.env|.*secret.*|.*credentials.*|.*\.pem|.*\.key)$", f, re.I)]
    L.append("Tracked files with secret-shaped names: %d" % len(risky))
    for f in risky[:5]:
        L.append("  - %s" % f)
    if risky:
        add(YELLOW, "Repo hygiene", "%d tracked file(s) have secret-shaped names (check, names only): %s" % (len(risky), ", ".join(risky[:3])))
    # scratch size
    scratch = os.path.join(repo, "scratch")
    if os.path.isdir(scratch):
        tot = 0
        for root, dirs, files in os.walk(scratch):
            for fn in files:
                try:
                    tot += os.path.getsize(os.path.join(root, fn))
                except OSError:
                    pass
        L.append("scratch\\ size: %s (gitignored)" % fmt_gb(tot))
        if tot > 20 * 1024 ** 3:
            add(YELLOW, "Repo hygiene", "scratch\\ is %s, clean it" % fmt_gb(tot))
    # CLAUDE.md @-imports resolve
    try:
        with open(os.path.join(repo, "CLAUDE.md"), encoding="utf-8-sig", errors="replace") as f:
            imps = re.findall(r"^@\./(\S+)", f.read(), re.M)
        missing = [i for i in imps if not os.path.exists(os.path.join(repo, i))]
        L.append("CLAUDE.md @-imports: %d, missing %d" % (len(imps), len(missing)))
        if missing:
            add(RED, "Repo hygiene", "CLAUDE.md imports missing: %s" % ", ".join(missing))
    except OSError:
        pass
    rc, out, err = git(repo, "count-objects", "-vH")
    sz = re.search(r"size-pack: (.+)", out or "")
    if sz:
        L.append("git pack size: %s" % sz.group(1))
    sections.append(("11. Repo hygiene", L))


def sec_rollup(repo):
    """Kept from the old nightly rollup: what the director logs did in the last 24 h, open decisions."""
    L = []
    cutoff = dt.datetime.now().timestamp() - 86400
    logs = os.path.join(repo, "logs")
    recent = []
    for p in glob.glob(os.path.join(logs, "*.md")):
        if os.path.getmtime(p) >= cutoff:
            recent.append(os.path.basename(p))
    L.append("Logs touched in the last 24 hours: %s" % (", ".join(sorted(recent)) or "none"))
    dec = os.path.join(logs, "DECISIONS.md")
    try:
        txt = open(dec, encoding="utf-8", errors="replace").read()
        entries = re.split(r"\n(?=## )", txt)
        openn = 0
        for e in entries:
            if not e.startswith("## "):
                continue
            m2 = re.search(r"\*\*Status:\*\*\s*(\S+)", e)
            if m2 and m2.group(1).upper().startswith("OPEN"):
                openn += 1
        L.append("DECISIONS.md: %d entries with Status OPEN (Zac clears them)" % openn)
    except OSError as e:
        L.append("DECISIONS.md not readable: %s" % e)
    rc, out, err = git(repo, "log", "--since=24 hours ago", "--oneline")
    L.append("Commits in the last 24 hours: %d" % len([l for l in out.splitlines() if l.strip()]))
    L.append("Blocked-item queueing and new work stay out of this check, as in the old rollup (read-only).")
    sections.append(("12. Director-log rollup (kept from the old nightly rollup)", L))


# ---------------------------------------------------------------- main
def main(argv):
    skip_updates = "--no-updates" in argv
    show = "--stdout" in argv
    name, configured, m = load_config()
    repo = os.path.normpath(m.get("repo", "D:\\WKP"))
    steps = [
        lambda: sec_machine(name, configured, m, repo),
        lambda: sec_disks(m),
        lambda: sec_drive_watch(m),
        sec_smart,
        sec_gpu_ram_cpu,
        lambda: sec_security(skip_updates),
        lambda: sec_backups(m, repo),
        lambda: sec_tasks(m),
        lambda: sec_tools(m),
        lambda: sec_env(m),
        lambda: sec_repo(repo),
        lambda: sec_rollup(repo),
    ]
    for s in steps:
        try:
            s()
        except Exception as e:  # noqa
            add(YELLOW, "Checker", "a check crashed: %r" % e)
    fix_summary = "fixes not run"
    try:
        import safe_fixes
        only = None
        if "--fixes-only" in argv:
            i = argv.index("--fixes-only")
            only = set(x.strip() for x in argv[i + 1].split(",")) if i + 1 < len(argv) else None
        fl, fix_summary, fprop, _err = safe_fixes.run_fixes(repo, m, force_live="--fixes-live" in argv,
                                                           force_dry="--fixes-dry-run" in argv, only=only)
        if fix_summary != "fixes OFF" and not fix_summary.startswith("fixes STOPPED"):
            # append-only history so a rerun of the day's report never erases what a fix run did
            hist = os.path.join(repo, "logs", "system-check", dt.date.today().isoformat() + "-fixes.md")
            os.makedirs(os.path.dirname(hist), exist_ok=True)
            with open(hist, "a", encoding="utf-8", newline="\n") as hf:
                hf.write("## %s  (%s)\n\n%s\n\n" % (dt.datetime.now().strftime("%H:%M:%S"), fix_summary, "\n".join(fl)))
        sections.append(("13. Safe fixes (allowlist tier, logged with counts)", fl))
        sections.append(("14. Proposals (never run by this check)", fprop))
    except Exception as e:  # noqa
        add(YELLOW, "Safe fixes", "safe fixes crashed, nothing further attempted: %r" % e)
    level = max([f[0] for f in findings] or [GREEN])
    reds = [f for f in findings if f[0] == RED]
    yels = [f for f in findings if f[0] == YELLOW]
    reasons = [("%s: %s" % (f[1], f[2])) for f in (reds + yels)]
    one = "%s | %s | %s" % (NAMES[level], name, dt.date.today().isoformat())
    if reasons:
        one += " | " + "; ".join(reasons[:4]) + (" (+%d more)" % (len(reasons) - 4) if len(reasons) > 4 else "")
    else:
        one += " | all checks passed"
    today = dt.date.today().isoformat()
    outdir = os.path.join(repo, "logs", "system-check")
    os.makedirs(outdir, exist_ok=True)
    body = ["# System check %s" % today, "", "**STATUS: %s**" % one, ""]
    body.append("Checks are read-only. Only change possible: the safe-fixes allowlist (section 13). Result: %s. Adobe untouched." % fix_summary)
    body.append("")
    if reasons:
        body.append("## Reasons")
        for f in reds:
            body.append("- RED: %s: %s" % (f[1], f[2]))
        for f in yels:
            body.append("- YELLOW: %s: %s" % (f[1], f[2]))
        body.append("")
    for title, lines in sections:
        body.append("## " + title)
        body.append("")
        tablish = any(l.startswith("|") for l in lines)
        for l in lines:
            raw = tablish or l.startswith("  ") or l.startswith("#") or not l.strip() or title.startswith(("13.", "14."))
            body.append(l if raw else "- " + l)
        body.append("")
    body.append("## Scheduling (needs Zac's yes, NOT registered by this script)")
    body.append("")
    body.append("Run by hand any time: `python D:\\WKP\\.claude\\skills\\wkp-system-check\\scripts\\system_check.py` (add `--no-updates` to skip the 1-minute Windows Update search, `--stdout` to print the report).")
    body.append("")
    body.append("To run it nightly at 11:30 PM (wrapper `D:\\WKP\\scripts\\nightly-system-check.bat` = pull, system check, the old log rollup, commit, push):")
    body.append("")
    body.append("    schtasks /Create /TN \"WKP-System-Check\" /TR \"cmd.exe /c D:\\WKP\\scripts\\nightly-system-check.bat\" /SC DAILY /ST 23:30")
    body.append("")
    body.append("To disable the retired daily brief task: `schtasks /Change /TN \"WKP-daily-brief\" /DISABLE`")
    body.append("")
    body.append("To add the Saturday wrap at 5:30 AM: `schtasks /Create /TN \"WKP-Saturday-Wrap\" /TR \"cmd.exe /c cd /d D:\\WKP && claude -p \\\"run wkp-saturday-wrap\\\"\" /SC WEEKLY /D SAT /ST 05:30`")
    path = os.path.join(outdir, today + ("" if m.get("primary") else "-" + name) + ".md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(body) + "\n")
    with open(os.path.join(outdir, "latest.txt" if m.get("primary") else "latest-%s.txt" % name), "w", encoding="utf-8", newline="\n") as f:
        f.write(one + "\n")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:  # noqa
        pass
    if show:
        print("\n".join(body))
    print(one)
    print(fix_summary)
    print("report: " + path)
    return level


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
