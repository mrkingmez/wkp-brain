package com.wkp.sparkcapture.wakeword

/**
 * Wake-word detection boundary — Phase 3, the non-vibe-codeable piece
 * flagged in the handoff doc (Section 8). This is the app's core
 * technical risk (Section 2).
 *
 * MVP target: OpenWakeWord — free, open-source, self-trained models.
 * Fallback/upgrade path if scaling past free-tier limits:
 *   - Picovoice Porcupine (free tier caps at 3 active users/mo;
 *     commercial scale ~$6,000/yr+)
 *   - Outspoken (~$1/model, newer/smaller vendor)
 *
 * Kept as an interface so the underlying engine is swappable without
 * touching the rest of the app.
 */
interface WakeWordEngine {
    /** Begin listening for the configured wake phrase(s). */
    fun start()

    /** Stop listening. */
    fun stop()

    /** Register a callback fired when the wake word is detected. */
    fun onWakeWordDetected(callback: () -> Unit)
}
