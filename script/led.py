import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

while True:
    GPIO.output(17, 1)
    time.sleep(0.5)
    GPIO.output(17, 0)
    time.sleep(0.5)
