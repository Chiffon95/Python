import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print("Button Pushed!")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_pin = 15

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while 1:
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button Pushed!")
    time.sleep(0.1)
