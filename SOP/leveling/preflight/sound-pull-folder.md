# Pre-flight: Sound pull folder (P:\WWD Kit\<Movie>\Sounds\ and the pull sheet)

Created 2026-11-22.

1. [ ] Source list is the run sheet's Sound lines plus the wwd-sound plan, parsed by script (header can be a range 'TC - TC').
2. [ ] Every source path exists before copy (os.path.exists). Missing ones are listed, never skipped.
3. [ ] Files are COPIED, never moved. Source mtime and size unchanged (spot check 3).
4. [ ] One folder per stop named `NN HH-MM picture`, plus `Spares` and `Music candidates`.
5. [ ] File count in stop folders equals the number of Sound lines. Unique-source count stated.
6. [ ] Each file has a license note: Adobe SFX library (owned via subscription, per media-map, verify before client use), loose mp3 with NO license on file is named and flagged.
7. [ ] One-page `.docx` pull sheet (stop, time, file, license) in `D:\WKP Reports\Sound Pulls\`, .md kept in the repo.
8. [ ] Levels (dB) on Sound lines are tagged PROPOSED unless Zac used them in a finished cut (cite the cut). Nothing says a sound was heard.
9. [ ] Updated when the run sheet changed (date of last run sheet revision written on the pull sheet).
10. [ ] Zero em dashes. Ledger row and lesson written.
