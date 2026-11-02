# PC Health Leftovers, 2026-11-01

Zac said "run the leftover PC health items". Claude Code is not running as admin, so anything needing admin is listed at the bottom with the exact command.

## Done today
- Startup: Epson Download Navigator (EPSDNMON) set to disabled. Reversible: Task Manager > Startup apps > Enable. Nothing deleted.
- Adobe: LEFT ALONE. Zac's call, Adobe is fine. An early change to CCXProcess was reverted the same day.
- Disk health on the USB drive (I:): Windows ran its volume checks on 10/31 at 2:13 PM and logged I: and E: as healthy. No disk error events (IDs 7, 11, 51, 55, 153) since 10/31.
- Freezes: zero Kernel-Power 41 (hard reset) events since the dev tools moved to C: on 10/31 midday.
- Premiere cache: media cache is on C: (23.6 GB media cache files, 3 GB peak files). C: has 243 GB free. Fine for now. Move it to D: (2.5 TB free) in Premiere > Settings > Media Cache if C: drops under 100 GB.
- RAM: 10.9 GB free of 31.6 GB with Claude, dashboard and Blender running.

## Could not do
- CPU temperature: Windows exposes no thermal sensor here and LibreHardwareMonitor shows none. Needs a motherboard-specific tool (HWiNFO is free) to read it.
- Stale N: drive entry: no network drive entry found for N, and no mapped N: drive exists, so nothing to remove. Likely a leftover from the old enclosure letter.

## Needs admin (Zac pastes in an Administrator PowerShell)
```
Disable-ScheduledTask -TaskName "Epson PowerENGAGE"
sfc /scannow
chkdsk I: /scan
```
Also in Administrator: Task Manager > Startup apps, disable "Epson Printer Connection Checker" if wanted (machine-wide entry).

## Still open
- Restart once so GPU scheduling takes effect (if not restarted since 10/31).
- Android Studio (3.3 GB) still on I:, paused with Spark Capture.
- Keep watching I: until about 11/14.
