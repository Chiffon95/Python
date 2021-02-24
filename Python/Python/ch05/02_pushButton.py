import RPi.GPIO as GPIO
import time

def button_callback(channel):
    print("Button Pushed!")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_pin = 15

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(button_pin, GPIO.RISING, callback = button_callback)

while 1:
    time.sleep(0.1)