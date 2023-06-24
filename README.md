# Distance Based Buzzer Intensity Control

The "Distance Based Buzzer Intensity Control" repository contains Python code that allows you to control the intensity of a buzzer based on the distance measured by an HC-SR04 ultrasonic sensor. The script `code.py` uses the RPi.GPIO Python library to control GPIO pins of a Raspberry Pi.

Key Features:

1. **Ultrasonic Distance Measurement**: This script uses an HC-SR04 ultrasonic sensor, connected to the Raspberry Pi, to measure the distance to an object. It sends an ultrasonic signal, waits for the signal to bounce back, and calculates the time difference between sending and receiving the signal to determine the distance to the object.

2. **Buzzer Intensity Control**: The script connects to a buzzer using a Pulse Width Modulation (PWM) pin on the Raspberry Pi. The intensity of the buzzer sound is inversely proportional to the measured distance, i.e., as the distance increases, the buzzer intensity decreases and vice versa.

3. **Real-Time Operation**: The script operates in a continuous while loop, constantly measuring distance and adjusting the buzzer intensity in real-time.

This project is an excellent resource for those interested in learning about ultrasonic sensors, PWM control, and the physical computing capabilities of Raspberry Pi. It could be particularly useful for robotic projects involving obstacle detection and avoidance or for creating interactive installations.
