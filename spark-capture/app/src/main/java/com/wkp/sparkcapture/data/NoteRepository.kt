package com.wkp.sparkcapture.data

/**
 * Storage boundary for notes — Phase 2 work.
 *
 * Defined as an interface from the start so the wake-word (Phase 3) and
 * transcription (Phase 4) layers can be built and tested against a fake
 * implementation before real Room persistence exists.
 */
interface NoteRepository {
    suspend fun save(note: Note): Long
    suspend fun getAll(): List<Note>
    suspend fun delete(id: Long)
}
