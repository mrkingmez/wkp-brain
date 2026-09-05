# Spark Capture (working title)

Hands-free, wake-word-triggered idea capture for Android. Full concept
and spec: [`docs/HANDOFF.md`](docs/HANDOFF.md). Module-to-phase mapping
and open decisions: [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

**Status: repo scaffolding only.** Nothing functional is built yet —
this is the project structure and package boundaries, ready to open in
Android Studio and start Phase 2 work.

## What's here

```
spark-capture/
├── app/
│   ├── build.gradle.kts          # Compose + Room deps pre-wired
│   ├── proguard-rules.pro
│   └── src/main/
│       ├── AndroidManifest.xml   # mic/foreground-service permissions declared
│       ├── java/com/wkp/sparkcapture/
│       │   ├── MainActivity.kt   # placeholder Compose screen
│       │   ├── ui/               # empty — Phase 2
│       │   ├── data/             # Note + NoteRepository — Phase 2
│       │   ├── wakeword/         # WakeWordEngine interface — Phase 3
│       │   ├── transcription/    # TranscriptionEngine interface — Phase 4
│       │   └── service/          # CaptureForegroundService stub — Phase 3
│       └── res/values/strings.xml
├── docs/
│   ├── HANDOFF.md                # original spec, copied in for reference
│   └── ARCHITECTURE.md
├── build.gradle.kts
├── settings.gradle.kts
├── gradle.properties
└── .gitignore
```

## Opening this project

1. Open the `spark-capture/` root folder in Android Studio (Koala or
   newer recommended).
2. Let Gradle sync — it'll pull the plugin/dependency versions pinned
   in `build.gradle.kts` and `app/build.gradle.kts`.
3. No Gradle wrapper JAR is checked in yet (binary file, not something
   to hand-author) — Android Studio will offer to generate one on
   first open, or run `gradle wrapper` locally if you have Gradle
   installed.

## What's deliberately NOT here yet

- Any real UI beyond a single placeholder screen
- Room annotations / actual persistence
- Any wake-word SDK integration (OpenWakeWord etc.)
- Any transcription integration
- Launcher icon / app theme (branding pass, per handoff doc Section 1)
- CI, tests beyond the default templates

## Suggested next step

Per the handoff doc's own recommendation (Section 8): build out the
`ui/` and `data/` packages next — note list, capture flow, settings,
real Room persistence — before touching `wakeword/`. The wake-word SDK
integration is flagged as native Android work, not vibe-codeable, so
it's worth having a working app shell to integrate it into first.
