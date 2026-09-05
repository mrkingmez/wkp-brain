plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

android {
    // Placeholder namespace/applicationId — doc flags "Spark Capture" as a
    // working title needing a branding pass (Section 1). Rename before
    // any real release build.
    namespace = "com.wkp.sparkcapture"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.wkp.sparkcapture"
        // minSdk 26 gives headroom below the Pixel 4 test device (ships
        // Android 10 / API 29); raise if the chosen wake-word SDK
        // requires a higher floor.
        minSdk = 26
        targetSdk = 34
        versionCode = 1
        versionName = "0.1.0-scaffold"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    kotlinOptions {
        jvmTarget = "17"
    }
    buildFeatures {
        compose = true
    }
    composeOptions {
        kotlinCompilerExtensionVersion = "1.5.14"
    }
}

dependencies {
    implementation("androidx.core:core-ktx:1.13.1")
    implementation("androidx.lifecycle:lifecycle-runtime-ktx:2.8.4")
    implementation("androidx.activity:activity-compose:1.9.1")
    implementation(platform("androidx.compose:compose-bom:2024.06.00"))
    implementation("androidx.compose.ui:ui")
    implementation("androidx.compose.ui:ui-graphics")
    implementation("androidx.compose.ui:ui-tooling-preview")
    implementation("androidx.compose.material3:material3")

    // Phase 2 (app shell) — local note storage. Annotation processor
    // (kapt/ksp) intentionally not wired up yet; add when Room entities
    // are actually written.
    implementation("androidx.room:room-runtime:2.6.1")
    implementation("androidx.room:room-ktx:2.6.1")

    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.2.1")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.6.1")
}
