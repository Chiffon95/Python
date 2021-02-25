import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)

p.start(50)

try:
	while 1:
		for dc in range(0, 101, 5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.01)
		for dc in range(100, -1, -5):
			p.ChangeDutyCycle(dc)
			time.sleep(0.01)
except KeyboardInterrupt:
	pass
	
p.stop()
GPIO.cleanup()
