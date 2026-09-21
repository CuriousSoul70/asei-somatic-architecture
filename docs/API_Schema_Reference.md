# API Schema Reference

This defines the strict JSON structures required for communication between the hardware proxy, the edge broker, and the Affective Engine.

### 1. Hardware Telemetry Payload (Input)
Dispatched via Web Serial from the edge device.
```json
{
  "hrv": 45,       // Root Mean Square of Successive Differences (ms)
  "eda": 12,       // Skin Conductance Level / Phasic Peaks
  "timestamp": "1719045620"
}
