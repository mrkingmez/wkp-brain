# Format - ENCLOSURE

## What this produces
Enclosure design specs and print jobs.

## HARD RULE
Never spec resin for an enclosure. Resin cracks at snap fits and yellows
under UV. Elegoo Mars is for the character figure, decorative bezels,
and fine detail parts only.
Enclosures are PETG on FDM, printed out of house or on a second printer.

## Per enclosure, capture
Internal dimensions with clearance for every component, stated.
Screen cutout dimensions - spell out as "240 by 280", no symbols.
Port access - USB, power, reset.
Ventilation if anything runs warm.
Assembly method - screws, snap fit, or friction.
Wall thickness and why.
Print orientation and whether supports are needed.
Estimated print time and material.

## Rules
Elegoo Mars generation is unresolved - PAWS-003. Do not assume a build
volume. If a part might need splitting, say so and queue it.
Spell out symbols that break text to speech. Millimeters, degrees,
microfarads written as words.

## Output
docs\ for the spec. Model files referenced by path, not embedded.
