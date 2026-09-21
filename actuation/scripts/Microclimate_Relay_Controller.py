# V2.0 Microclimate & Olfaction Relay Controller
# Runs on a local edge server (e.g., Raspberry Pi) to control heavy AC loads[cite: 2].
# Listens for JSON actuation recipes and triggers physical SSRs for fans and scent pumps.

import socket
import json
import time
try:
    import RPi.GPIO as GPIO # Used for SSR control
except ImportError:
    pass # Fallback for testing on non-Pi hardware

# Configuration
UDP_IP = "0.0.0.0"
UDP_PORT = 5005
FAN_PIN = 17
SCENT_PIN_PINENE = 27
SCENT_PIN_GEOSMIN = 22

def setup_gpio():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FAN_PIN, GPIO.OUT)
        GPIO.setup(SCENT_PIN_PINENE, GPIO.OUT)
        GPIO.setup(SCENT_PIN_GEOSMIN, GPIO.OUT)
        # Create PWM instance for laminar airflow control[cite: 2]
        global fan_pwm
        fan_pwm = GPIO.PWM(FAN_PIN, 100) 
        fan_pwm.start(0)
    except NameError:
        print("GPIO not available. Running in simulation mode.")

def handle_actuation(recipe):
    fan_speed = int(recipe.get("fan", 0))
    scent = recipe.get("scent", "None")
    
    print(f"Applying Microclimate: Fan {fan_speed}%, Scent: {scent}")
    
    try:
        # Actuate laminar blower[cite: 2]
        fan_pwm.ChangeDutyCycle(fan_speed)
        
        # Trigger piezoelectric mesh atomization[cite: 2]
        GPIO.output(SCENT_PIN_PINENE, GPIO.HIGH if scent == "Pinene" else GPIO.LOW)
        GPIO.output(SCENT_PIN_GEOSMIN, GPIO.HIGH if scent == "Geosmin" else GPIO.LOW)
    except NameError:
        pass

def start_server():
    setup_gpio()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, UDP_PORT))
    print(f"Listening for Actuation Recipes on UDP port {UDP_PORT}...")

    while True:
        data, addr = sock.recvfrom(1024)
        try:
            recipe = json.loads(data.decode('utf-8'))
            handle_actuation(recipe)
        except json.JSONDecodeError:
            print("Invalid JSON received")

if __name__ == "__main__":
    start_server()
