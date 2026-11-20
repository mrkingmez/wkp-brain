"""python qb_check.py <season> <week>   (2026-11-19)
Which QB does the sim pick by default per team, old rule vs new rule, against the overrides file. Read-only."""
import sys, json
sys.path.insert(0, r"D:\WKP\.claude\skills\ff-simulator\scripts")
import run_week as rw, simulate as sm, coach_model as cm
season, week = int(sys.argv[1]), int(sys.argv[2])
tg, lg, pw, defs, lg_def, sched = rw.load_all(season, week)
drops, quest = rw.injury_sets(season, week)
named = rw.qb_starts(season, week)
team_now = rw.current_teams(season, week)
latest = pw.sort_values("order").groupby("player_id").team.last().to_dict(); latest.update(team_now)
wk = sched[(sched.season == season) & (sched.week == week)]
for _, g in wk.iterrows():
    for team in (g.away_team, g.home_team):
        m = sm.TeamModel(team, pw, tg, None, season * 100 + week, latest)
        m.drop(drops)
        pl = m.players
        old = sorted([k for k in pl if pl[k]["group"] == "QB" and pl[k]["att_total"] > 15], key=lambda k: -pl[k]["att_total"])[:1]
        new = sm.qb_order(pl)[:1]
        nm = lambda l: pl[l[0]]["name"] if l else "-"
        nq = named.get(team, (None, ""))[1]
        flag = "" if (not nq or nq == nm(new)) else "  <-- new rule differs from named"
        print(f"{team:4} old {nm(old):22} new {nm(new):22} named {nq}{flag}" + (f"  (Q {quest.get(new[0])})" if new and new[0] in quest else ""))

