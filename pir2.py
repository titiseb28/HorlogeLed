#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

def callback_up(channel):
    print("Up detected on channel %s" % channel)

PIR = 7
GPIO.setmode(GPIO. BCM)
GPIO.setup(PIR, GPIO.IN)

try:
    GPIO.add_event_detect(PIR, GPIO.RISING, callback=callback_up)
    while 1:
        time.sleep(100)
except KeyboardInterrupt:
    print(" Cleaning up the GPIO")
    GPIO.cleanup()
