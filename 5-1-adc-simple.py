import RPi.GPIO as GPIO
import time
def dec_to_bin(value):
    return [int(digit) for digit in bin(value)[2:].zfill(8)]


def adc(dac, comp):
    for i in range(256):
        signal = dec_to_bin(i)
        volt = (i / 256) * 3.3
        GPIO.output(dac, signal) 
        time.sleep = (20)
        comp_val = GPIO.input(comp)
        if comp_val == 0:
            break

    return volt


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp =  4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
try:
    while True:   
        volt = adc(dac, comp)
        print (f'Voltage = {volt} V')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
