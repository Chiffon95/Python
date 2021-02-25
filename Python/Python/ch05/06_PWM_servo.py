import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SERVO_PIN = 18
GPIO.setup(SERVO_PIN, GPIO.OUT)

p = GPIO.PWM(SERVO_PIN, 50)

p.start(0)

try:
	while True:
		p.ChangeDutyCycle(1.5) #0
		time.sleep(0.6)
		p.ChangeDutyCycle(3.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(4.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(5.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(6.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(7.5) #90
		time.sleep(0.1)
		p.ChangeDutyCycle(8.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(9.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(10.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(11.5)
		time.sleep(0.1)
		p.ChangeDutyCycle(12.5) #180
		time.sleep(0.1)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
