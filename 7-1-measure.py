import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

def dec_to_bin(value):  #binary representation of number
    return [int(digit) for digit in bin(value)[2:].zfill(8)]


def display(leds, volt):  #displaying voltage on LEDS panel
    value = round(volt * 256 / 3.3)
    bin_repres = dec_to_bin(value)
    GPIO.output(leds, bin_repres)
    return


def troyka_measure(comp, dac):  #measuring voltage on TROYKA module
    for i in range(256):
        signal = dec_to_bin(i)
        volt = (i / 256) * 3.3
        GPIO.output(dac, signal) 
        time.sleep = (20)
        comp_val = GPIO.input(comp)
        if comp_val == 0:
            break
    return volt


leds = [21, 20, 16, 12, 7, 8, 25, 24]  #ports' settings
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT)
try:
    values = []  #a list of voltage values
    start = time.time()  #moment when capacitor started charging
    GPIO.output(troyka, 1)  #initialize charging
    volt = 0
    while (volt / 3.3) < 0.97:
        volt = troyka_measure(comp, dac)
        display(leds, volt)
        if volt != 0:
            values.append(volt)
        time.sleep = 2
    GPIO.output(troyka, 0)  #interupt charging
    volt = 3.3
    while (volt / 3.3) > 0.02:
        volt = troyka_measure(comp, dac)
        display(leds, volt)
        if volt != 0:
            values.append(volt)
        time.sleep = 2
    end = time.time() - start  #time elapsed in total
    print(f'Общаяя продожительность эксперимента - {end} секунд')
    plt.plot(values)
    plt.show()
finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()