import threading
import time
import smbus2
import RPi.GPIO as GPIO

# GPIO Settings
GPIO.setmode(GPIO.BCM)
MOTION_SENSOR_PIN = 17
LED_PIN = 27
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

# BH1750 Settings
BH1750_ADDR = 0x23
BH1750_CMD = 0x10
bus = smbus2.SMBus(1)

# Global Variables
motion_detected = False
light_level = 0


# Task: Reading data from BH1750
def task_read_light():
    global light_level
    while True:
        try:
            data = bus.read_i2c_block_data(BH1750_ADDR, BH1750_CMD, 2)
            light_level = (data[0] << 8 | data[1]) / 1.2
        except Exception as e:
            print(f"BH1750 Error: {e}")
        time.sleep(2)  # Execute every 2 seconds


# Task: Handling data from HC-SR501
def task_motion_sensor():
    global motion_detected
    while True:
        motion_detected = GPIO.input(MOTION_SENSOR_PIN)
        time.sleep(0.5)  # Check every 0.5 seconds


# Task: LED Control
def task_led_control():
    while True:
        if motion_detected and light_level < 50:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)  # Update every 100 ms


# Start RTOS Threads
try:
    threading.Thread(target=task_read_light, daemon=True).start()
    threading.Thread(target=task_motion_sensor, daemon=True).start()
    threading.Thread(target=task_led_control, daemon=True).start()

    # Main Thread
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("\nExiting the program...")
finally:
    GPIO.cleanup()
