package com.wkp.sparkcapture

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp

/**
 * Entry point / placeholder shell.
 *
 * This is repo scaffolding only — see docs/HANDOFF.md, Section 4.
 * Real navigation (Notes list / Capture / Settings) is Phase 2,
 * "Core app shell," and hasn't been built yet.
 */
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            SparkCaptureScaffold()
        }
    }
}

@Composable
fun SparkCaptureScaffold() {
    MaterialTheme {
        Surface(modifier = Modifier.fillMaxSize()) {
            Column(modifier = Modifier.padding(24.dp)) {
                Text(text = "Spark Capture — repo scaffold")
                Text(text = "Phase 2 (app shell) not yet built. See docs/HANDOFF.md.")
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun ScaffoldPreview() {
    SparkCaptureScaffold()
}
