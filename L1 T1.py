import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
i = 0
while True:
    GPIO.output(22, i % 2)
    time.sleep(1)
    i += 1