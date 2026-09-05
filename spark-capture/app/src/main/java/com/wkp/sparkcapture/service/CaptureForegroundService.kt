package com.wkp.sparkcapture.service

import android.app.Service
import android.content.Intent
import android.os.IBinder

/**
 * Always-listening background service — Phase 3.
 *
 * Hosts the WakeWordEngine so detection can run while the app isn't in
 * the foreground. Wake-word detection is lightweight vs. full always-on
 * ASR (handoff doc Section 3), so battery impact should stay low — but
 * that needs real-world validation in Phase 5 QA, not an assumption.
 *
 * Unimplemented — scaffolding only.
 */
class CaptureForegroundService : Service() {
    override fun onBind(intent: Intent?): IBinder? = null

    override fun onStartCommand(intent: Intent?, flags: Int, startId: Int): Int {
        // TODO(Phase 3): promote to foreground with a persistent
        // notification, initialize WakeWordEngine, wire the detection
        // callback into the capture flow.
        return super.onStartCommand(intent, flags, startId)
    }
}
