"""dk_own_build.py - one command for the DK own-numbers build: refresh, re-sim, our projections, our ownership ESTIMATE, 7 lineups.

python dk_own_build.py --week 11 --dk-salaries "D:\\Draft Kings\\Week 11\\DKSalaries.csv" --template "D:\\Draft Kings\\Week 11\\<entries>.csv"
                       --outdir "D:\\Draft Kings\\Week 11\\sat" [--no-refresh] [--out "Name One;Name Two"] [--drop-q] [--season 2026]

Steps (each prints; any failure stops the run):
  1. REFRESH (skip only with --no-refresh, e.g. a rerun minutes later): nflverse pbp + player stats + players + schedules,
     Odds API lines (ODDS_API_KEY), MFL roster pull (MFL_API_KEY), merged injury file (MFL, nflverse, ESPN, transactions).
     Then the starting-QB check: the sim's default QB per team is printed next to the dated qbs json. Fix any mismatch in
     overrides_<season>_wk<week>.json ("qbs" block) and qbs_confirmed_week<N>.json before trusting the build.
  2. RE-SIM: run_week.py and full_week.py at 20,000 sims (writes dfs_draws for this week).
  3. own_proj.py: percentiles dk_25..dk_99, DST, implied totals, status, DK IDs.
  4. dk_own.py predict: ownership ESTIMATE (full model, fit on the Week 10 reference).
  5. dk_gpp.py --own: 7 lineups under the friend's rules, template filled, dk_validate run on both files.
Decision support only. Never logs in, never enters, never spends. Every file it writes stays in D:\\Draft Kings\\.
"""
import argparse, datetime as dt, subprocess, sys
from pathlib import Path

PY = sys.executable
HERE = Path(__file__).resolve().parent
SIM = Path(r"D:\WKP\.claude\skills\ff-simulator\scripts")
NFLD = Path(r"D:\WKP\.claude\skills\nfl-data\scripts\nfl_data.py")


def run(args, cwd=None):
    print("\n>>", " ".join(str(x) for x in args), flush=True)
    r = subprocess.run([PY, "-I", *map(str, args)], cwd=cwd)
    if r.returncode != 0:
        raise SystemExit(f"step failed (exit {r.returncode}): {args[0]}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=2026); ap.add_argument("--week", type=int, required=True)
    ap.add_argument("--dk-salaries", required=True); ap.add_argument("--template", required=True); ap.add_argument("--outdir", required=True)
    ap.add_argument("--no-refresh", action="store_true"); ap.add_argument("--out", default=""); ap.add_argument("--drop-q", action="store_true")
    a = ap.parse_args()
    s, w = a.season, a.week
    wk = Path(rf"D:\Draft Kings\Week {w}")
    out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
    slate, qbs = wk / f"slate_week{w}.json", wk / f"qbs_confirmed_week{w}.json"
    odds = Path(rf"D:\WKP\data\fantasy-wk{w}-odds-{dt.date.today():%Y-%m-%d}-dk.json")
    mfl = Path(rf"D:\WKP\scratch\dk{w}own")
    stamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M")
    if not a.no_refresh:
        run([SIM / "fetch_pbp.py", s], cwd=SIM); run([SIM / "fetch_stats.py", s], cwd=SIM)
        run([NFLD, "get", "players", "players.parquet", "--season", s]); run([NFLD, "get", "schedules", "games.parquet"])
        run([SIM / "fetch_odds.py", odds], cwd=SIM)
        run([HERE / "mfl_roster_pull.py", w, mfl], cwd=HERE.parent / "dashboard")
        run([SIM / "build_injuries.py", s, w], cwd=SIM)
        print(f"\nREFRESH DONE {stamp} local time")
    elif not odds.exists():
        cands = sorted(Path(r"D:\WKP\data").glob(f"fantasy-wk{w}-odds-*.json"))
        odds = cands[-1]
        print(f"--no-refresh: using the newest odds file on disk, {odds.name}")
    run([HERE / "qb_check.py", s, w])     # default QB per team vs the named starters: read it, fix mismatches, rerun
    run([SIM / "run_week.py", s, w, "--odds", odds, "--sims", 20000], cwd=SIM)
    run([SIM / "full_week.py", s, w, "--odds", odds, "--sims", 20000, "--roster", mfl / "thu_roster.json",
         "--md", out / f"full_week_sim_{dt.date.today():%Y-%m-%d}.md"], cwd=SIM)
    proj = out / f"own_proj_week{w}.csv"; est = out / f"own_est_week{w}.csv"
    run([HERE / "own_proj.py", "--season", s, "--week", w, "--slate", slate, "--dk-salaries", a.dk_salaries, "--qbs", qbs, "--out", proj])
    run([HERE / "dk_own.py", "predict", "--table", proj, "--params", HERE / "dk_own_params_full.json", "--out", est])
    g = [HERE / "dk_gpp.py", "--own", est, "--dk-salaries", a.dk_salaries, "--template", a.template, "--slate", slate, "--outdir", out]
    if a.out:
        g += ["--out", a.out]
    if a.drop_q:
        g += ["--drop-q"]
    run(g)
    print(f"\nBUILD DONE. Data refresh: {'this run ' + stamp if not a.no_refresh else 'skipped (--no-refresh)'}. Read {out / 'build_report.txt'}: both checks must say RESULT: PASS.")


if __name__ == "__main__":
    main()

