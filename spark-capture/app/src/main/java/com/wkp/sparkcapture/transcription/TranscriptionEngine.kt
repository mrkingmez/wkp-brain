package com.wkp.sparkcapture.transcription

/**
 * Transcription boundary — Phase 4.
 *
 * On-device vs. cloud transcription is still an open decision (handoff
 * doc Section 3). Defined as an interface first so that choice doesn't
 * have to be locked in before Phases 2–3 are underway.
 */
interface TranscriptionEngine {
    suspend fun transcribe(audioFilePath: String): String
}
