package com.wkp.sparkcapture.data

/**
 * Core note entity — placeholder shape only.
 *
 * Phase 2 will add Room annotations and real persistence. `tag` maps
 * to the project/world tagging mentioned as a paid-tier feature in the
 * handoff doc (Section 6) — e.g. "Shadowfall", "Shattered Empire", or
 * null for general/untagged notes.
 */
data class Note(
    val id: Long = 0L,
    val text: String,
    val createdAtEpochMillis: Long,
    val capturedViaWakeWord: Boolean,
    val tag: String? = null
)
