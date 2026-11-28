# ESP32 hobby: ecosystem, compatibility and projects (angle C)
Researched 2026-11-22. READ-ONLY desk research, nothing bought or signed up. "Verified" means I fetched the page this session. Anything else is labeled NOT VERIFIED. No prices were retrieved; dollar figures are my estimates.

## 0. The short answer
- PATH: Arduino IDE 2.x with the Espressif ESP32 core pinned to the last 3.x release (3.3.13). Board: an ESP32-S3 dev board with PSRAM (one board does display, camera, USB, Wi-Fi).
- SECOND STEP (after about 4 weeks): ESPHome (YAML config, over-the-air updates, plugs into Home Assistant later if he wants it).
- Why: nearly every tutorial, library and camera example is Arduino C++; quick wins exist in an hour; the IDE is a normal Windows app.

## 1. Ecosystem map

### Current core version and what broke (VERIFIED)
- arduino-esp32 releases page (fetched 2026-11-22): newest stable is 4.0.0, tagged 19 Nov (year not printed, asset stamps point to 2026), based on ESP-IDF v6.1.1. Previous: 3.3.13 (17 Nov), 3.3.12 (18 Sep). https://github.com/espressif/arduino-esp32/releases
- 4.0.0 is three days old. I did NOT find its breaking-change list (page links out). Recommendation: install 3.3.13 for the first month because tutorials and libraries lag. Judgment, not a verified incompatibility.
- 2.x to 3.0 breaking changes (VERIFIED, https://docs.espressif.com/projects/arduino-esp32/en/latest/migration_guides/2.x_to_3.0.html):
  - LEDC (PWM, dimming, servos): ledcSetup and ledcAttachPin replaced by ledcAttach (first argument is now the pin). Old tutorials fail to compile.
  - Timers: timerBegin takes only a frequency; timerAttachInterrupt lost the edge argument.
  - I2S (mic and speaker amp): driver redesigned, old I2S code needs rewriting.
  - RMT changed; hallRead removed; BLE API uses Arduino String and pointers; UART default pins changed on ESP32; WiFiServer available() deprecated for accept().
  - Reader reports (NOT verified by me): RNT HTTP tutorial comment says GET returns -1 after 3.x; RNT ESP32Servo tutorial comments report compile errors with newer library plus 3.x.

### Path comparison
| Path | Beginner fit | Notes |
|---|---|---|
| Arduino IDE 2.x (C++) | BEST first path | Largest tutorial base (Random Nerd Tutorials, Adafruit). Pitfall: 3.x API changes above. |
| MicroPython + Thonny | Good, gentle | Official docs: download .bin from micropython.org, generic ESP32, C3, S3 builds work. Docs name no IDE; Thonny not verified here. Camera support NOT verified. https://docs.micropython.org/en/latest/esp32/tutorial/intro.html |
| ESPHome | BEST second step | YAML config. First flash over USB, then wireless updates. Device Builder can run standalone via pip; HA auto-discovers devices. https://esphome.io/guides/getting_started_hassio.html |
| Home Assistant | Not a first step | Needs its own host. ESPHome integration is "Local Push", encrypted API (noise_psk key). https://www.home-assistant.io/integrations/esphome/ |
| PlatformIO / pioarduino | Intermediate | More setup. A community thread blames broken PlatformIO for new-user ESPHome failures: https://community.home-assistant.io/t/new-esphome-user-hard-time-with-initial-config/995474 . pioarduino specifics NOT verified. |
| ESP-IDF | Advanced | Not for relaxing. Skip. |
| CircuitPython | Nice on S3 | Native-USB boards (S2/S3) can be edited as a drive; original ESP32 is more awkward. https://learn.adafruit.com/circuitpython-with-esp32-quick-start |
| Meshtastic / LoRa | Different hobby | Needs a LoRa radio (SX126x recommended); a plain ESP32 cannot mesh. Regional radio rules NOT verified. https://meshtastic.org/docs/hardware/devices/ |
| M5Stack UiFlow | Block coding | M5 hardware only; NOT verified, not fetched. |

## 2. Compatibility matrix

### ESP32 variants
Sources: web search summary of JLCPCB and Espressif techpedia (https://jlcpcb.com/blog/esp32-versions-guide, https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/get-started/board-selection.html); camera info from ESPHome esp32_camera docs. Good, not datasheet-grade.
| Chip | Wi-Fi | Bluetooth | Native USB | Camera | Verdict |
|---|---|---|---|---|---|
| ESP32 classic | Wi-Fi 4 | Classic + BLE | No (USB-UART chip) | Yes (ESP32-CAM, Ai-Thinker pinout in ESPHome docs) | Most tutorials; pins fussy |
| S2 | Wi-Fi 4 | None | Yes | NOT verified | Skip |
| S3 | Wi-Fi 4 | BLE 5 | Yes | Yes (XIAO S3 Sense, Freenove S3, AtomS3R-CAM in ESPHome docs) | PICK |
| C3 | Wi-Fi 4 | BLE 5 | USB serial/JTAG only | NOT verified | Cheap sensor/LED node |
| C6 | Wi-Fi 6 | BLE 5 + Thread/Zigbee | USB serial/JTAG only | No | Later |
| H2 | None | BLE 5 + 802.15.4 | not listed | No | Not for him |
| P4 | None (pairs with C6) | None | Yes | Yes (NOT deep-verified) | Too advanced |

### Camera modules
- OV2640 (2 MP): stock ESP32-CAM camera; ESPHome lists it supported.
- OV5640 (5 MP): ESPHome lists it supported; ships on Seeed XIAO ESP32S3 Sense expansion board (some units may ship OV3660 during transition; https://wiki.seeedstudio.com/xiao_esp32s3_getting_started/).
- GC2145: NOT in the ESPHome list I fetched, Arduino support NOT verified. Do not buy it as a first camera.
- Camera needs PSRAM; frame buffers default to PSRAM (ESPHome docs). On Ai-Thinker, GPIO16 is tied to PSRAM and misuse can trip the watchdog (https://esphome.io/components/esp32_camera/).
- Camera eats 12+ GPIOs: 8 data, VSYNC, HREF, PCLK, XCLK, plus an I2C pair. Ai-Thinker pins (ESPHome): data 5,18,19,21,36,39,34,35; VSYNC 25; HREF 23; PCLK 22; XCLK 0; I2C 26/27; power-down 32. Hence ESP32-CAM has almost no free pins and uses microSD in 1-bit mode to free some (RNT PIR tutorial).
- Classic ESP32-CAM has no USB: needs an FTDI adapter with GPIO0 to GND to flash (verified in RNT tutorials). Reason to start on a USB S3 board.

### Sensors, displays, actuators
I2C addresses and 5V notes are from my general datasheet knowledge, NOT fetched (Adafruit's I2C list page only links GitHub tables). Run an I2C scanner first. Verified items marked.
| Part | Bus | Typical address | Voltage and notes |
|---|---|---|---|
| DHT11/DHT22 | 1-wire | n/a | 3.3 to 5V; pull-up if bare. DHT22 better. |
| BME280 | I2C | 0x76 or 0x77 (sketch uses 0x76, verified RNT; clones vary per comments) | 3.3V. BMP280 is same minus humidity; cheap "BME280" listings are often BMP280. |
| MPU6050 | I2C | 0x68 / 0x69 | 3.3V fine |
| ADXL345 | I2C/SPI | 0x53 / 0x1D | 3.3V |
| INA219 | I2C | 0x40 to 0x4F | low-voltage current only, never mains |
| MAX30102 | I2C | 0x57 | 3.3V, finicky, not medical |
| SSD1306 OLED | I2C | 0x3C (verified RNT; 0x3D on some) | 3.3V works. SH1106 clones need a different library. |
| BH1750 light | I2C | 0x23 / 0x5C | easier than an LDR |
| ST7789 / ILI9341 TFT | SPI | n/a | 3.3V logic, 4 to 6 pins plus backlight |
| E-paper | SPI | n/a | 3.3V, slow refresh, great for status boards |
| HC-SR04 | 2 GPIO | n/a | 5V part, ECHO is 5V: use a resistor divider or the 3.3V HC-SR04P |
| PIR HC-SR501 | 1 GPIO | n/a | 5V power, 3.3V output OK |
| Soil moisture | analog | n/a | Buy CAPACITIVE (resistive corrodes). ADC1 pin. |
| LDR | analog | n/a | divider resistor, ADC1 |
| GPS NEO-6M | UART | n/a | needs sky view, slow first fix |
| RFID RC522 | SPI | n/a | 3.3V ONLY |
| I2S mic (INMP441) + MAX98357 amp | I2S | n/a | I2S code changed in core 3.x. Amp wants 5V for volume. |
| Servo SG90 | PWM | n/a | 5V external supply, shared ground; ESP32Servo library |
| Relay module | GPIO | n/a | use 3.3V-trigger type; low-voltage loads only, no mains for a beginner |
| Stepper 28BYJ-48 + ULN2003 | 4 GPIO | n/a | 5V external |
| NeoPixel WS2812B | 1 GPIO | n/a | 5V power from its own supply; 330 ohm on data, 1000uF across supply; level shifter only for long runs |

### I2C clash guide
- 0x3C OLED, 0x76 BME280, 0x68 MPU6050, 0x57 MAX30102, 0x40 INA219, 0x23 BH1750, 0x53 ADXL345 do not collide (datasheet memory, scan to confirm).
- Clashes: BME280/BMP280/BME680 share 0x76/0x77; two OLEDs share 0x3C (use a 0x3D jumper or a TCA9548A mux).
- Classic ESP32 default I2C: SDA 21, SCL 22 (verified RNT). Some S3 boards lack GPIO 22 (RNT comment); use Wire.begin(SDA, SCL) with your board's pins.

### Pin pitfalls (VERIFIED, https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)
- Strapping pins, classic ESP32: 0, 2, 4, 5, 12, 15. GPIO0 low = flash mode; GPIO12 must be low at boot.
- Input-only: 34, 35, 36, 39.
- GPIO 6 to 11 are tied to flash: never use.
- ADC2 cannot be read while Wi-Fi is on (classic ESP32); use ADC1 (GPIO 32 to 39). Espressif confirms ADC2 is shared with Wi-Fi and reads can time out: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/peripherals/adc/adc_oneshot.html . Other chips NOT verified.

## 3. Parts bin that grows
Dollar figures are MY ESTIMATES, no prices retrieved. Vendors are in angle A.
### Phase 1 (about $40 to $50 est.)
- 1 ESP32-S3 USB-C board with PSRAM, ideally a camera board (XIAO ESP32S3 Sense: 8MB PSRAM, 8MB flash, OV5640, SD slot, USB-C charging, verified on Seeed wiki).
- 1 SSD1306 0.96in I2C OLED, 1 BME280 breakout, 1 half-size breadboard, Dupont jumper set, 2 DATA-capable USB-C cables.
### Phase 2 (add about $20 est.)
- SG90 servo, capacitive soil sensor, PIR HC-SR501, WS2812B stick or ring, 330 ohm resistors, 1000uF capacitor, 5V 2A charger as external supply.
### Phase 3 (add about $30 est.)
- Second board (classic ESP32 or C3) as a dedicated node, 2.4in ST7789 or e-paper module, INMP441 + MAX98357 + small speaker, 28BYJ-48 stepper, MPU6050, 1m WS2812B strip + 5V 3A supply.
### Tools
- Multimeter (cheap is fine: continuity and DC volts). Wire strippers. Soldering iron not needed in Phase 1 with pre-soldered headers; buy a basic temperature-controlled one at Phase 3. Half-size plus mini breadboards. USB data cables. Power bank (check it does not auto-shutoff at low draw, NOT verified). Magnifier lamp.

## 4. Twelve projects (ranked by calm payoff vs build time)
Verified links are pages I fetched. "Search:" means no verified link yet.
1. OLED hello + I2C scanner (30 min, easy, Phase 1). Learn wiring, libraries, serial monitor. https://randomnerdtutorials.com/esp32-ssd1306-oled-display-arduino-ide/ (verified; 2019 page; Adafruit SSD1306/GFX; 0x3C; comments report some code fails on new library versions).
2. BME280 weather readout on the OLED (1 hr, easy). https://randomnerdtutorials.com/esp32-bme280-arduino-ide-pressure-temperature-humidity/ (verified, updated 2026, uses 0x76).
3. Desk clock + weather (2 to 3 hr, medium). Learn Wi-Fi, NTP, JSON. Base: https://randomnerdtutorials.com/esp32-http-get-post-arduino/ (verified but 2020, HTTP only; HTTPS and 3.x need adapting). Weather API terms NOT verified.
4. Sensor logger to a local web page (2 hr, medium). Search: "Random Nerd Tutorials ESP32 BME280 web server" (the BME280 page links a weather station project, not separately verified).
5. Camera live stream on home Wi-Fi (1 to 2 hr, medium). https://randomnerdtutorials.com/esp32-cam-video-streaming-web-server-camera-home-assistant/ (verified; written for ESP32-CAM OV2640 + FTDI, AI Thinker model; adapt the camera pin model for an S3 board).
6. Motion-triggered snapshot to SD (3 hr, medium). https://randomnerdtutorials.com/esp32-cam-pir-motion-detector-photo-capture/ (verified; comments report wrong schematic, false triggers, wants a 10k pull-up and stable power).
7. Time-lapse (window or plant) (2 hr, medium). Search: "ESP32-CAM time lapse SD card". Reuses the SD code from #6.
8. Plant monitor: soil sensor + OLED + log (3 hr, medium, Phase 2). Search: "ESP32 capacitive soil moisture Arduino". Use an ADC1 pin.
9. Servo desk toy or pan-tilt mount (2 hr, medium). https://randomnerdtutorials.com/esp32-servo-motor-web-server-arduino-ide/ (verified; comments report library/3.x friction, use ESP32Servo and check for updates).
10. NeoPixel mood lamp, sci-fi desk glow tied to a web slider (2 hr, easy to medium, Phase 2). Search: "ESP32 WS2812B FastLED". No verified link.
11. Desk status display for fantasy football or WKP dashboard (4 to 6 hr, medium to hard, Phase 3). TFT or e-paper that GETs a small JSON endpoint from a script on his own PC over the home network, so no keys live on the device. Learn HTTP GET and JSON (same base as #3). Public score API terms NOT verified.
12. Hobby tie-in: sci-fi "airlock" door sensor with sound (reed switch + MAX98357 clip, hard, Phase 3, I2S needs 3.x-ready code), or a Blender-designed printed or hand-built enclosure for any project above. Search: "ESP32 I2S MAX98357 play wav core 3" and confirm it is 3.x-ready before following. Meshtastic pair is an optional later toy.
Recommended order for ADHD quick wins: 1, 2, 5, 3, 10, 8, 6, 9, 4, 7, 11, 12.

## 5. Home Wi-Fi only: simple security
- Change every default password. Put cameras and gadgets on a guest or IoT network if the router allows (his router NOT verified).
- No port forwarding, ever. RNT's servo tutorial notes access is local unless you forward ports; do not.
- The RNT stream sketch serves plain HTTP on port 80 with no password (fetched note). Treat it as visible to anyone on the LAN: point it away from bedrooms and screens, add a lens cover, unplug it when guests visit, tell his wife where it points.
- ESPHome API supports an encryption key (noise_psk); the old API password is deprecated (HA docs, verified). Turn on the OTA password and API key.
- Never paste Wi-Fi passwords or API keys into chats or git. Keep them in a secrets.h that is gitignored.

## Not verified / gaps
Arduino core 4.0.0 breaking-change list; GC2145 support; Thonny and UiFlow details; I2C addresses and 5V needs (datasheet memory, scan to confirm); all prices; router IoT-network options; terms of any weather or sports API; Meshtastic legal limits by region.
