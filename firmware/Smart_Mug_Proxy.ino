/*
 * ASEI V1.0 Hardware Proxy (Build in Public MVP)
 * 
 * Simulates the capacitive swipe of the Smart Mug and transmits 
 * a simulated biological payload to the Web Serial Dashboard.
 * Listens for actuation commands (e.g., 'F50' for 50% Fan Speed) 
 * to trigger physical feedback[cite: 2].
 */

const int buttonPin = 2;       // Simulates capacitive touch on the mug
const int actuatorPin = 9;     // Simulates room fan / relay (PWM capable)

int buttonState = 0;
int lastButtonState = 0;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  Serial.begin(115200);
  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(actuatorPin, OUTPUT);
  
  // Initialize actuator to off
  analogWrite(actuatorPin, 0);
}

void loop() {
  // 1. Read Trigger (Simulated Mug Swipe)
  int reading = digitalRead(buttonPin);
  
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      
      // If button is pressed (pulled low)
      if (buttonState == LOW) {
        // Dispatch simulated panic state metrics[cite: 2]
        Serial.println("{\"hrv\": 15, \"eda\": 85}");
      }
    }
  }
  lastButtonState = reading;

  // 2. Listen for Edge Broker Actuation Commands via Web Serial
  if (Serial.available() > 0) {
    String incomingCommand = Serial.readStringUntil('\n');
    incomingCommand.trim();
    
    // Parse Fan command (e.g., "F50" -> 50% fan speed)[cite: 2]
    if (incomingCommand.startsWith("F")) {
      String valueString = incomingCommand.substring(1);
      int percentage = valueString.toInt();
      
      // Constrain and map 0-100% to 0-255 PWM
      percentage = constrain(percentage, 0, 100);
      int pwmValue = map(percentage, 0, 100, 0, 255);
      
      analogWrite(actuatorPin, pwmValue);
    }
  }
}
