import RPi.GPIO as GPIO
import time
def dec_to_bin(value):
    return [int(digit) for digit in bin(value)[2:].zfill(8)]


def adc():
    summ = 0
    for i in range(8):
        new_d = summ + 2**(7 - i)
        signals = dec_to_bin(new_d)
        GPIO.output(dac, signals)
        comp_val = GPIO.input(comp)
        if comp_val == 1:
            summ += 2**(7 - i)
    return summ


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp =  4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
try:
    while True:   
        volt = adc()
        print (f'Voltage = {volt/ 256 * 3.3} V')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
