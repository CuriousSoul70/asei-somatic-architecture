# ASEI Firmware Repository

This directory contains the edge-device firmware for the Adaptive Somato-Environmental Interface (ASEI)[cite: 2]. 

Due to the constraints of the 3-day Build in Public hackathon, this folder is divided into two distinct development tracks:

1.  **V1.0 MVP (The Hardware Proxy):** `Smart_Mug_Proxy.ino` is a functional Arduino C++ script designed specifically for today's pitch. It uses a physical push-button to simulate a user gripping the capacitive Smart Mug[cite: 2]. It communicates directly with our Web Serial dashboard, dispatching simulated biological JSON payloads and receiving physical actuation commands (like fan speed) back down the wire[cite: 2].
2.  **V3.0 Roadmap (The Implant):** `Subdermal_V3_Stub.cpp` outlines the theoretical C++ architecture required for the final Active Implantable Medical Device (AIMD). It highlights the necessary low-power states for the Ambiq Apollo4 MCU and data acquisition from the ADPD4100 and AD5940 sensors[cite: 2].

## Hardware Requirements (MVP Proxy)
*   Arduino Uno or Nano (or any USB-serial capable MCU)
*   Momentary Push Button (Connected to Pin 2)
*   LED / Small DC Motor (Connected to PWM Pin 9)
