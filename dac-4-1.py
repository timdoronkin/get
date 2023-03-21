import RPi.GPIO as GPIO
def dec_to_bin(value):
    return [int(digit) for digit in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    t = 0
    while t == 0:
        print('Insert your value')
        number = input()
        if number == 'q':
            t += 1
            continue
        try:
            number = int(number)
            if number > 255:
                print('value above allowed')
                continue
            elif  number < 0:
                print('value below zero')
                continue
            else:
                GPIO.output(dac, dec_to_bin(number))
                u_total = 0
                for i in range(8):
                    u_total += 2**(7-i)*dec_to_bin(number)[i]
                print(f'U = {u_total/255*3.3} V')
        except:
            print('wrong arg type')
            continue
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()