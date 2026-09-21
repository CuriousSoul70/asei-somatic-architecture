# V3.0 Subdermal Implant Bill of Materials (BOM)

This is the theoretical component stack for the final subdermal chip[cite: 2].

| Subsystem | Component / Spec | Function |
| :--- | :--- | :--- |
| **Core MCU** | Ambiq Apollo4 Blue Lite OR Nordic nRF5340 WLCSP | Edge processing, sub-microamp deep sleep, ECDH-256 cryptography[cite: 2]. |
| **Power Harvesting** | STMicroelectronics ST25DV04K | Dynamic NFC tag. Harvests energy via a 13.56 MHz resonant RLC matched antenna[cite: 2]. |
| **PPG Front End** | Analog Devices ADPD4100 (or ADPD188GG) | Measures Heart Rate Variability (HRV) via ambient light cancellation TIA[cite: 2]. |
| **Optical LEDs** | Osram SFH 7050 | Green 525nm for microvascular pulse, NIR 940nm for tissue depth penetration[cite: 2]. |
| **EDA Front End** | Analog Devices AD5940 | Measures Skin Conductance (EDA) injecting 50 mVpp at 16 Hz (<0.5 µA) across Pt/Ir pads[cite: 2]. |
