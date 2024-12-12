# Smart-Light-Control-with-Motion-and-Light-Sensors-using-Raspberry-Pi-and-RTOS
## Project Overview
This project demonstrates a smart lighting system using a Raspberry Pi, RTOS, and various sensors.
The system uses a motion sensor (HC-SR501) and a light sensor (BH1750) to control an LED light based on environmental conditions automatically. The project showcases real-time multitasking and sensor integration in an embedded system environment.
## Features 
- Automatic control of an LED based on motion detection and ambient light levels.
- Real-time multitasking is implemented using RTOS principles.
- Optimized GPIO handling for sensor input and LED output.
- Configurable light threshold for triggering the LED.

## Components Used
1. Raspberry Pi (Model B or similar)
2. HC-SR501 Motion Sensor
3. BH1750 Light Sensor
4. LED
5. Resistor 
6. Breadboard and jumper wires

## System Architecture
The project is structured using RTOS principles, with the following tasks:
1. Light Sensor Task: Reads data from the BH1750 and updates the ambient light level.
2. Motion Sensor Task: Monitors the HC-SR501 for motion detection.
3. LED Control Task: Controls the LED state based on sensor inputs.

## Task Priorities
- High Priority: Motion Sensor Task (to ensure immediate response to motion).
- Medium Priority: Light Sensor Task (periodic ambient light updates).
- Low Priority: LED Control Task (acts based on sensor data).

## Wiring Diagram
1. HC-SR501:
  - VCC: Connect to Raspberry Pi 5V.
  - OUT: Connect to GPIO17.
  - GND: Connect to Raspberry Pi GND.
2. BH1750:
- VCC: Connect to Raspberry Pi 3.3V.
- SDA: Connect to GPIO2 (SDA).
- SCL: Connect to GPIO3 (SCL).
- GND: Connect to Raspberry Pi GND.
3. LED:
- Anode: Connect to GPIO27 through a 220-ohm resistor.
- Cathode: Connect to GND.

## Example Output
The LED turns on when motion is detected and the light level is below the threshold. Otherwise, it remains off.
## License
This project is open-source and available under the MIT License.
