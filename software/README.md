# ASEI Software Repository (Logic Broker & Digital Twin)

This directory contains the Edge Broker MVP for the Adaptive Somato-Environmental Interface (ASEI)[cite: 2]. 

For this prototype phase, we built a serverless "Digital Twin" dashboard that runs entirely in the browser[cite: 2]. It bridges the physical hardware proxy with the generative AI model to simulate real-time room morphing.

## Architecture
1.  **Hardware Connection:** Uses the **Web Serial API** to connect directly to the Arduino Smart Mug proxy via USB[cite: 2].
2.  **Data Ingestion:** Reads the incoming simulated biological JSON payloads (HRV, EDA)[cite: 2].
3.  **Affective Engine:** Pings the **Gemini 1.5 Flash API** acting as our contextual AI broker[cite: 2]. Gemini maps the biometric vector to the Circumplex Model of Affect and generates a strict JSON actuation recipe[cite: 2].
4.  **Actuation:** Dynamically updates the browser UI (simulating visual/audio room shifts) and sends hardware commands (e.g., `F50` for fan speed) back down the serial port to trigger physical relays[cite: 2].

## Setup Instructions
1. Open `ASEI_Dashboard.html` in a Chromium-based browser (Chrome, Edge, Brave) to support the Web Serial API.
2. Insert your Google Gemini API Key on line 87.
3. Click "Connect Hardware" and select your Arduino COM port.
4. Press the physical button on your Arduino to trigger the cybernetic loop.
