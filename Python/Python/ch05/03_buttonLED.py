import RPi.GPIO as GPIO
import time

def button_callback(channel):
	global light_on
	if light_on == False:
		GPIO.output(led_pin, 1)
		print("LED ON!")
		light_on = True
	else:
		GPIO.output(led_pin, 0)
		print("LED OFF!")
		light_on = False
		
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
button_pin = 15
led_pin = 4
light_on = False

GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

GPIO.add_event_detect(button_pin, GPIO.RISING, callback = button_callback, bouncetime = 300)

while 1:
	time.sleep(0.1)
