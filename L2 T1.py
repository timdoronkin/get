import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
k = 0
while k < 3:
    for i in range(8):
        GPIO.output(leds[i], 1)
        if i > 0:
            GPIO.output(leds[i - 1], 0)
        time.sleep(0.1)
    GPIO.output(24, 0)
    k += 1
GPIO.output(leds, 0)
GPIO.cleanup()