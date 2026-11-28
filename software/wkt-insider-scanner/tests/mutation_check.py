"""Mutation check: break one key line at a time in a scratch COPY and confirm the tests fail.
Run: python -I tests\\mutation_check.py   (the real source is never touched)."""
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = r"D:\WKP\scratch"

MUTATIONS = [
    ("P-only filter off", "insider/form4.py", 'if t["code"] not in kept_codes:', "if False:"),
    ("distinct by accession, not owner", "insider/cluster.py", "s |= _counted(p, cfg)", 's |= {p["accession"] + c for c in _counted(p, cfg)}'),
    ("window one day too wide", "insider/cluster.py", "lo = e - dt.timedelta(days=n - 1)", "lo = e - dt.timedelta(days=n)"),
    ("amendment never supersedes", "insider/cluster.py", 'dead.setdefault(o["accession"], a["accession"])', "pass"),
    ("unknown type passes as officer", "insider/classify.py", '"type": roles[0] if roles else "UNKNOWN"', '"type": roles[0] if roles else "officer"'),
    ("fail status removed", "insider/cluster.py", 'if tier == "COUNTED" and unknown:', "if False:"),
    ("host allowlist off", "insider/guards.py", "if p.hostname not in hosts:", "if False:"),
    ("missing user agent allowed", "insider/guards.py", "if v is None or not v.strip():", "if False:"),
    ("lag sign flipped", "insider/classify.py", "(dt.date.fromisoformat(filing_date) - dt.date.fromisoformat(txn_date)).days", "(dt.date.fromisoformat(txn_date) - dt.date.fromisoformat(filing_date)).days"),
    ("entry on filing day", "insider/forward.py", 'if r["d"] > date:', 'if r["d"] >= date:'),
    ("429 not a stop", "insider/sec_client.py", "if status in (403, 429):", "if status in (403,):"),
    ("403 not a stop", "insider/sec_client.py", "if status in (403, 429):", "if status in (429,):"),
    ("haircut ignored", "insider/forward.py", "fe = o * (1 + bps / 1e4)", "fe = o"),
    ("cache ignored", "insider/sec_client.py", "if use_cache and os.path.exists(body_p)", "if False and os.path.exists(body_p)"),
    ("rate ceiling raised", "insider/guards.py", "HARD_MAX_RPS = 2.0", "HARD_MAX_RPS = 50.0"),
    ("doctype allowed", "insider/form4.py", 'if "<!doctype" in low or "<!entity" in low:', "if False:"),
    ("no-verdict banner removed", "insider/scorecard.py", "if n < f[\"min_counted_for_verdict\"]:", "if False:"),
    ("old config hash counted", "insider/scorecard.py", 'if r.get("config_hash") != chash:', "if False:"),
    ("multi change allowed", "insider/config.py", "if last and len(keys) > 1 and not (allow_multi and reason):", "if False:"),
    ("counts flag ignored (all owners count)", "insider/cluster.py", 'return {c for c, o in p["owners"].items() if o["counts"]}', 'return set(p["owners"])'),
    # ---- added 2026-11-27 for the devils-advocate ruling changes
    ("signal sees later filings (look-ahead)", "insider/cluster.py", "seen = [p for p in members if acc[id(p)][0] <= t]", "seen = list(members)"),
    ("late filings kept", "insider/cluster.py", "        if late:\r\n            rows = [r for r in rows if r not in late]", "        if False:\r\n            rows = [r for r in rows if r not in late]"),
    ("always same-day entry", "insider/forward.py", "if t.time() <= dt.time(int(hh), int(mm), 0):", "if True:"),
    ("ten percent owner counts", "insider/classify.py", 'if not (set(owner["roles"]) & set(cl["count_roles"])):', "if False:"),
    ("entity owner counts", "insider/classify.py", 'if cl["exclude_entity_owners"] and owner["entity_name_heuristic"]:', "if False:"),
    ("fund issuer kept", "insider/cluster.py", 'if fund and cfg["cluster"]["exclude_fund_issuers"]:', "if False:"),
    ("10b5-1 purchase kept", "insider/cluster.py", 'if cfg["filing"]["exclude_10b5_1"] and f.get("rule_10b5_1") is True:', "if False:"),
    ("offering group kept", "insider/cluster.py", "        if kws:\r\n", "        if False:\r\n"),
    ("unreadable footnote passes", "insider/cluster.py", 'elif not all(purchases[i]["fn_readable"] for i in idx):', "elif False:"),
    ("cost floor ignored", "insider/forward.py", "return max(floor, half), (", "return floor, ("),
    ("fill window ignored", "insider/forward.py", 'if mins > cfg["forward"]["fill_window_minutes"]:', "if False:"),
    ("ended bars dropped not marked", "insider/forward.py", 'if xb is None and stock and stock[-1]["d"] < exit_d:', "if False:"),
    ("new listing seasoned", "insider/forward.py", 'if age >= f["min_listing_age_trading_days"]:', "if True:"),
    ("best case label removed", "insider/scorecard.py", "if n and pct > lim:", "if False:"),
    ("both benchmarks not required", "insider/scorecard.py", "if all(b in ex for b in benches):", "if any(b in ex for b in benches):"),
    ("K1 never fires", "insider/scorecard.py", 'hit = mm <= k["mean_at_or_below"] and md <= k["median_at_or_below"]', "hit = False"),
    ("freeze ignored", "insider/runner.py", 'if dt.datetime.fromisoformat(c["signal"]["instant_et"]) <= fz:', "if False:"),
    ("watcher file names writable", "insider/logio.py", 'if os.path.basename(path).lower() in ("decisions.jsonl"', 'if False and os.path.basename(path).lower() in ("decisions.jsonl"'),
    ("isolation flags unchecked", "insider/config.py", 'iso["writes_to_watcher"] is not False or iso["feeds_watcher_score"] is not False', "False"),
    ("excess vs SPY only reported as primary", "insider/scorecard.py", 'out["vals"][b].append(ex[b])', 'out["vals"][b].append(ex["SPY"])'),
    ("redirect host unchecked", "insider/sec_client.py", "cur = guards.assert_allowed_url(urllib.parse.urljoin(cur, loc), self.hosts)", "cur = urllib.parse.urljoin(cur, loc)"),
]


def main():
    os.makedirs(SCRATCH, exist_ok=True)
    base = tempfile.mkdtemp(prefix="mut-", dir=SCRATCH)
    survived, rows = [], []
    for name, rel, old, new in MUTATIONS:
        dst = os.path.join(base, "copy")
        if os.path.exists(dst):
            shutil.rmtree(dst)
        shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns("__pycache__", "demo-out", "cache"))
        p = os.path.join(dst, rel.replace("/", os.sep))
        with open(p, encoding="utf-8", newline="") as f:
            s = f.read()
        if old not in s:
            rows.append((name, "MUTATION TEXT NOT FOUND"))
            survived.append(name)
            continue
        with open(p, "w", encoding="utf-8", newline="") as f:
            f.write(s.replace(old, new, 1))
        r = subprocess.run([sys.executable, "-I", "-W", "ignore", os.path.join(dst, "tests", "test_insider.py")], capture_output=True, text=True, timeout=300)
        killed = r.returncode != 0
        rows.append((name, "KILLED" if killed else "SURVIVED"))
        if not killed:
            survived.append(name)
    shutil.rmtree(base, ignore_errors=True)
    for n, v in rows:
        print("%-36s %s" % (n, v))
    print("\n%d mutations, %d killed, %d survived" % (len(rows), len(rows) - len(survived), len(survived)))
    return 1 if survived else 0


if __name__ == "__main__":
    sys.exit(main())
