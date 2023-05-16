import RPi.GPIO as GPIO
import time
from matplotlib import pyplot

GPIO.setmode(GPIO.BCM)

leds=[21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)

dac=[26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.HIGH)

comp=4
troyka=17 
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        GPIO.output(dac, to_bin(k))
        time.sleep(0.005)
        if GPIO.input(comp)==0:
            k-=2**i
    return k

def to_bin(a):
    return [int (numb) for numb in bin(a)[2:].zfill(8)]

try:
    volt=0
    result_storage=[]
    time_start=time.time()
    count=0

    print('начало зарядки конденсатора')
    while volt<256*0.8:
        volt=adc()
        result_storage.append(volt)
        time.sleep(0)
        count+=1
        GPIO.output(leds, to_bin(volt))

    GPIO.setup(troyka,GPIO.OUT, initial=GPIO.LOW)

    print('начало разрядки конденсатора')
    while volt>256*0.02:
        volt=adc()
        result_storage.append(volt)
        time.sleep(0)
        count+=1
        GPIO.output(leds, to_bin(volt))

    time_experiment=time.time()-time_start

    print('запись данных в файл')
    with open('data.txt', 'w') as f:
        for i in result_storage:
            f.write(str(i) + '\n')
    with open('settings.txt', 'w') as f:
        f.write(str(1/time_experiment/count) + '\n')
        f.write('0.01289')

    print('общая продолжительность эксперимента {}, период одного измерения {}, средняя частота дискретизации {}, шаг квантования АЦП {}'.format(time_experiment, time_experiment/count, 1/time_experiment/count, 0.013))

    print('построение графиков')
    y=[i/256*3.3 for i in result_storage]
    x=[i*time_experiment/count for i in range(len(result_storage))]
    pyplot.plot(x, y)
    pyplot.xlabel('Time')
    pyplot.ylabel('Voltage')
    pyplot.show()

finally:
    GPIO.output(leds, 0)
    GPIO.output(dac, 0)
    GPIO.cleanup()