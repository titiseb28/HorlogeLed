#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
PIR = 7
GPIO.setup(PIR, GPIO.IN)

try:
    print("PIR Module Test")
    print(" (CTRL+C to exit)")
    time.sleep(2)
    print "Ready"
    while True:
        if GPIO.input(PIR):
            print("Motion detected! ")
        time.sleep(1)
except KeyboardInterrupt:
    print("Quitting")
    GPIO.cleanup()
