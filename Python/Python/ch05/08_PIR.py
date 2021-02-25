import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_R = 20
led_Y = 21
sensor = 17

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_Y, GPIO.OUT)
GPIO.setup(sensor, GPIO.IN)

print("PIR Ready.....")
time.sleep(2)

try:
	while True:
		if GPIO.input(sensor) == 1:
			GPIO.output(led_Y, 1)
			GPIO.output(led_R, 0)
			print("Motion Detected !")
			time.sleep(0.1)
		if GPIO.input(sensor) == 0:
			GPIO.output(led_Y, 0)
			GPIO.output(led_R, 1)
			time.sleep(0.1)
except KeyboardInterrupt:
	print("Stopped by User")
	GPIO.cleanup()
