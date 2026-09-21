# ASEI Actuation Repository

This directory houses the logic and media assets for the physical room morphing (Visuals, Audio, Microclimate, Olfaction)[cite: 2]. 

For the MVP pitch, the web dashboard handles basic fan control directly via Web Serial[cite: 2]. This folder contains the architectural blueprints and scripts for the full room scale integration.

## Directory Structure
*   **/audio**: Place your binaural stems here (e.g., `432Hz_pink_noise.wav`, `14Hz_rustling_leaves.wav`, `binaural_waterfall.wav`)[cite: 2].
*   **/visuals**: Place your TouchDesigner (`.toe`) or Unreal Engine (`.uproject`) files here. These systems will use Time-of-Flight (ToF) cameras for 120 Hz real-time parallax rendering[cite: 2].
*   **/scripts**: Contains the bridging logic to connect the Affective Engine's output to high-voltage Solid State Relays (SSRs) and projection mapping software[cite: 2].
