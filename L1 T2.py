import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(14, GPIO.IN)
GPIO.output(22, GPIO.input(14))
