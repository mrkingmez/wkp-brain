# cfb-espn-snapshot
Weekly ESPN college football snapshot for the pick'em card (decision SW-2026-11-11-01 A).
Builds on Fantasy-Football\tracker\cfb_snapshot.py (imports it). Free, keyless, read-only, about 12 calls a run.
Saves D:\WKP\data\cfb\espn\YYYY-MM-DD\HHMM.json and a rolling D:\WKP\data\cfb\espn\line_history.json
(keeps each game's lines after ESPN deletes odds at the final). No injury data exists in this feed.
Run: C:\Users\kingz\AppData\Local\Programs\Python\Python312\python.exe D:\WKP\software\cfb-espn-snapshot\espn_snapshot.py
Test: cd to this folder, python -m unittest test_espn_snapshot -v
Limits: unofficial ESPN API, no published terms for it, can change without notice. Raw data is private, never publish.
