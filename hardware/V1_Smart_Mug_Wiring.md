# V1.0 MVP Wiring Pinout

Connect these components to your Arduino to interface with `Smart_Mug_Proxy.ino`[cite: 2].

| Component | Arduino Pin | Description |
| :--- | :--- | :--- |
| **Push Button (Leg 1)** | Digital Pin 2 | Pulls to GND when pressed. Simulates the capacitive mug swipe[cite: 2]. |
| **Push Button (Leg 2)** | GND | Ground connection. |
| **LED / Motor (+)** | Digital Pin 9 (PWM) | Simulates the room fan or microclimate actuator[cite: 2]. |
| **LED / Motor (-)** | GND (via resistor) | Ground connection. |
