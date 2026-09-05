# Format - FIRMWARE

## What this produces
Firmware plans and code for ESP32 and XIAO class boards.

## HARD BLOCKERS - refuse and queue a decision
Never spec a microphone into a device a person under 18 will touch.
Never spec an LLM, cloud call, or any data collection into a device a
person under 18 will touch.
Never put a credential or API token in firmware. NVS storage plus a
captive-portal setup page, always, including on Zac's own prototype.

## Sequence, in order
1. State machine written and tested on a PC. No hardware.
2. Board boots, wifi connects, static output.
3. API call, parse, map to state.
4. Port the tested state machine.
5. Animation and hardware output.
6. Persistence, sleep, power management.

Do not reorder this. Debugging a state machine over a serial cable is
misery, and skipping step 1 is how it happens.

## Rules
Task source is blocked by PAWS-001 until Zac resolves it. Do not assume
a provider and do not build the integration layer against a guess.
Data-capable USB cables only - state this wherever flashing is involved.
Note flash and RAM headroom against the target board.

## Output
firmware\ for code. docs\ for the plan.
