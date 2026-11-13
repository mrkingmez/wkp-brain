"""Kickoff weather for every outdoor NFL game in a week. Built 2026-11-12 (Zac's rule 2026-10-22: wind, rain and snow all matter
unless the game is indoors). Source: Open-Meteo forecast API, free, no key, non-commercial use allowed. About 8 calls a week.

    python weather.py <season> <week> [--out csv]

Reads the local nflverse schedule (roof, stadium, kickoff in US Eastern). Prints one line per game and a FLAG when sustained
wind is 15 mph or more (the tested signal: 649 games, totals 2.1 points under the closing number), gusts 25 or more, or
precipitation chance 50 percent or more. Forecasts only reach about 16 days out, and they change: rerun the day of the game.
It does not change any projection. It is a flag for totals, passing and kickers.
"""
import sys

import pandas as pd
import requests

XY = {"ARI": (33.5276, -112.2626), "ATL": (33.7554, -84.4008), "BAL": (39.2780, -76.6227), "BUF": (42.7738, -78.7870), "CAR": (35.2258, -80.8528),
      "CHI": (41.8623, -87.6167), "CIN": (39.0955, -84.5161), "CLE": (41.5061, -81.6995), "DAL": (32.7473, -97.0945), "DEN": (39.7439, -105.0201),
      "DET": (42.3400, -83.0456), "GB": (44.5013, -88.0622), "HOU": (29.6847, -95.4107), "IND": (39.7601, -86.1639), "JAX": (30.3239, -81.6373),
      "KC": (39.0489, -94.4839), "LV": (36.0909, -115.1833), "LAC": (33.9535, -118.3392), "LA": (33.9535, -118.3392), "MIA": (25.9580, -80.2389),
      "MIN": (44.9737, -93.2575), "NE": (42.0909, -71.2643), "NO": (29.9511, -90.0812), "NYG": (40.8135, -74.0745), "NYJ": (40.8135, -74.0745),
      "PHI": (39.9008, -75.1675), "PIT": (40.4468, -80.0158), "SF": (37.4032, -121.9698), "SEA": (47.5952, -122.3316), "TB": (27.9759, -82.5033),
      "TEN": (36.1665, -86.7713), "WAS": (38.9076, -76.8645)}
ABROAD = {"munich": (48.2188, 11.6247), "bayern": (48.2188, 11.6247), "tottenham": (51.6043, -0.0665), "wembley": (51.5560, -0.2796),
          "frankfurt": (50.0686, 8.6455), "bernab": (40.4531, -3.6883), "corinthians": (-23.5453, -46.4742), "croke": (53.3607, -6.2511),
          "olympiastadion": (52.5147, 13.2395), "azteca": (19.3029, -99.1505), "melbourne": (-37.8200, 144.9834)}


def main():
    season, week = int(sys.argv[1]), int(sys.argv[2])
    g = pd.read_parquet(r"D:\WKP\data\nfl\schedules\games.parquet")
    g = g[(g.season == season) & (g.week == week)]
    rows = []
    for r in g.itertuples():
        game = f"{r.away_team}@{r.home_team}"
        roof = str(r.roof) if r.roof == r.roof and r.roof else "unknown"
        std = str(r.stadium).lower()
        xy = next((v for k, v in ABROAD.items() if k in std), None) if str(r.location) == "Neutral" else XY.get(r.home_team)
        if roof in ("dome", "closed") and str(r.location) != "Neutral":
            rows.append(dict(game=game, where=roof, flag="")); continue
        if xy is None:
            rows.append(dict(game=game, where=f"{r.stadium}: location not in the table", flag="NOT AVAILABLE")); continue
        try:
            j = requests.get("https://api.open-meteo.com/v1/forecast", timeout=30, params=dict(
                latitude=xy[0], longitude=xy[1], timezone="America/New_York", forecast_days=16, temperature_unit="fahrenheit",
                wind_speed_unit="mph", precipitation_unit="inch",
                hourly="temperature_2m,precipitation_probability,precipitation,snowfall,wind_speed_10m,wind_gusts_10m")).json()
            h = pd.DataFrame(j["hourly"]); h["time"] = pd.to_datetime(h.time)
        except Exception as e:
            rows.append(dict(game=game, where=roof, flag=f"NOT AVAILABLE ({type(e).__name__})")); continue
        k = pd.Timestamp(f"{r.gameday} {r.gametime}")
        w = h[(h.time >= k) & (h.time < k + pd.Timedelta(hours=3.5))].dropna(subset=["wind_speed_10m"])
        if not len(w):
            rows.append(dict(game=game, where=roof, flag="NOT AVAILABLE (kickoff outside the forecast window)")); continue
        d = dict(game=game, where=("open or retractable, check on game day" if roof in ("open", "retractable", "unknown") else roof) + (", neutral site" if str(r.location) == "Neutral" else ""),
                 kick_et=str(k)[:16], temp_f=round(w.temperature_2m.mean()), wind_mph=round(w.wind_speed_10m.max()), gust_mph=round(w.wind_gusts_10m.max()),
                 rain_chance=int(w.precipitation_probability.max()), rain_in=round(float(w.precipitation.sum()), 2), snow_in=round(float(w.snowfall.sum()) / 2.54, 2))
        f = []
        if d["wind_mph"] >= 15: f.append("WIND 15+ (totals ran 2 points under)")
        if d["gust_mph"] >= 25: f.append("GUSTS 25+")
        if d["rain_chance"] >= 50: f.append("RAIN LIKELY")
        if d["snow_in"] > 0: f.append("SNOW")
        d["flag"] = "; ".join(f)
        rows.append(d)
    out = pd.DataFrame(rows)
    pd.set_option("display.width", 240)
    print(out.fillna("").to_string(index=False))
    dst = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else rf"D:\WKP\data\ff-play-sim\weather_{season}_wk{week}.csv"
    out.to_csv(dst, index=False)
    print("saved", dst)


if __name__ == "__main__":
    main()
