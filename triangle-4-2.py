import RPi.GPIO as GPIO
import time
def dec2bin(value):
    return [int(digit) for digit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    print('insert  signal period')
    period = int(input())
    h = 255
    GPIO.output(dac, dec2bin(h))
    while True:
        while h > 0:
            h -= 1
            GPIO.output(dac, dec2bin(h))
            time.sleep(period/510)
        while h < 255:
            h += 1
            GPIO.output(dac, dec2bin(h))
            time.sleep(period/510)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()