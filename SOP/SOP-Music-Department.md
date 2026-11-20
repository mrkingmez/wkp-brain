# SOP: Music Department

Created 2026-11-19 (system reset). Boss: **music** (shared department, open to every director). New bench: **music-researcher**.

## Zac's questions, answered

| Question | Answer before 2026-11-19 | Now |
|---|---|---|
| Does the music agent have a research partner? | No. Bench was "(none)" in AGENT-NETWORK.md. It did its own web searches | Yes. `music-researcher` (spec `.claude\agents\music-researcher.md`) researches tool terms, licenses, free libraries, genre craft and reference tempos, and keeps `_spec\music-reference.md` current |
| Does it know the music we own? | Partly. Its spec pointed at the raw P: file index (27,000 rows, no durations, no music summary). It never found the channel theme on L: and A Knight's Tale reported "intro/outro music not found" | Yes. `D:\WKP\data\assets\music-catalog.md` plus `.csv` (5,450 audio files after removing macOS zip junk, durations for full tracks and WWD audio, source guess per file), built read-only by `build_music_catalog.py`. music reads it first on every job |
| Can it create its own music? | Prompts only (Suno, ElevenLabs). It cannot generate audio itself | Same, stated plainly below. It can also cut and measure owned music for free with ffmpeg (6 s stings, outros) |

## What music can make for free, and what it cannot

| Free, no approval | Needs Zac's yes (money or credits) | Cannot do |
|---|---|---|
| Pick from the owned catalog, cut stings and outros from owned tracks with ffmpeg, measure loudness, copy the pick into `P:\WWD Kit\<Show>\Sounds\` | Any ElevenLabs Music generation (credits) | Hear audio. Every mood claim is from file names or measurements, labeled so. Zac auditions |
| Write ready-to-paste prompts for Suno, ElevenLabs Music and YouTube Create | Suno renewal (plan lapsed 2026-10-26; free-tier output is non-commercial) | Clear a track it cannot trace to a license |
| Find tracks in free libraries (YouTube Audio Library, Pixabay, Free Music Archive) with the license recorded per track | Any paid library or plugin | Rip or reuse commercial music, prompt for a named artist or song |

## Job flow

1. Read `memory\MEMORY.md`, `memory\agents\music.md`, `data\assets\music-catalog.md`, `_spec\music-reference.md`.
2. Owned first: 3 ranked picks (safe, bolder, outside-library if the library has nothing), each with path, seconds, loudness, license status.
3. WWD: intro sting 6 s max, outro length stated, no bed under talk, match the movie's tone.
4. If a new track is needed: prompts (Suno and ElevenLabs), plus a spend line queued in DECISIONS.md with the exact credit cost. An owned fallback cut is always delivered so the job never waits on the spend.
5. Research questions (terms changed? which free library has X? reference tempo?) go to music-researcher with a handoff note. It returns a sourced brief and updates the reference.
6. Deliver per Output SOP: .md `WWD\reports\<Movie>-Music.md`, .docx `D:\WKP Reports\Music Prompts\`, chosen file copied to the show's kit Sounds folder.
7. Log: `logs\agent-runs.md` row, `logs\wwd-director.md` line for WWD jobs, one lesson in `memory\agents\music.md`.

## Catalog upkeep

media-manager reruns `python D:\WKP\.claude\skills\media-manager\scripts\build_music_catalog.py` when music lands on P: or L: (read-only scan, writes only `data\assets\music-catalog.*`). music reports any track it learns about (measured loudness, Zac's verdict after audition) into `_spec\music-reference.md` "Owned library notes".
