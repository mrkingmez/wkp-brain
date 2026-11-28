# Firefly prompt log (started 2026-11-18)

Drop one subfolder per clip. Name it `<project>-<shot>`, for example `ian-V4-ball-boot`.
Inside, put (only the first two are required):
1. `prompt.txt` : the exact prompt as typed, one file per attempt (`prompt-1.txt`, `prompt-2.txt`...).
2. The clips themselves, named to match (`attempt-1.mp4`...). Keep the ones that failed too.
3. `settings.txt` : model, resolution, aspect ratio, fps, duration, audio on/off, seed if shown, start frame used (yes/no, which file).
4. `notes.txt` : one line per attempt: what went wrong (wrong hand, ball hit the toe, face drifted) or "kept".
A screenshot of the Firefly panel works instead of settings.txt.
Do not worry about tidy. Jarvis and graphic-design read it and build the lessons into the prompting guide.

## Update 2026-11-22 (graphic-design): settings.txt now has a fixed format
Copy `D:\WKP\data\firefly-prompt-guide\SETTINGS-TEMPLATE.txt` into the shot folder for every attempt (`settings-1.txt`, `settings-2.txt`). It records engine and tier, resolution, aspect, fps, duration, audio, panel mode, start frame, end frame, references with role and strength, seed, the lint result, the credit readout copied from the Generate button (never estimated) and the result. The first 18 clips had none of it. New folders are named `<project>-<shot>`. Rebuilt prompts live in `D:\WKP\data\firefly-prompt-guide\REBUILT-PROMPTS-2026-11-22.md`, make the folder `joust-sting-v2`, `garage-GA`, and so on, one per card id.

## Zac's correction, 2026-11-22 (evidence gap closed)
- All clips were Veo 3.1 family. All joust clips EXCEPT the final three were Veo 3.1 Fast. The garage clips and the final three joust attempts were therefore full Veo 3.1 (Zac's wording: "all are veo 3.1", fast only on the joust except the last three).
- Other settings were as the agents suggested.
- The final three joust results were NOT downloaded (Zac's call, he will not download them). Do not ask again. Their notes stand without clips.
