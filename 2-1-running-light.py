import RPi.GPIO as GPIO
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)

for i in range(len(leds) * 3):
    GPIO.output(leds[i % len(leds)], 1)
    time.sleep(0.2)
    GPIO.output(leds[i % len(leds)], 0)

GPIO.output(leds, 0)
GPIO.cleanup()