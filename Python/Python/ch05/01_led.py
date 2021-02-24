import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 8

GPIO.setup(led_pin, GPIO.OUT)

for i in range(10):
    GPIO.output(led_pin, 1)
    time.sleep(1)
    GPIO.output(led_pin, 0)
    time.sleep(1)

GPIO.cleanup()