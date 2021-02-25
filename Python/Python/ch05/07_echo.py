import PRi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG = 23
ECHO = 24

print("Distance measurement in progress")
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

print("Waiting for sensor to settle")
GPIO.output(TRIG, False)
time.sleep(2)

try:
	while True:
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)
		
		while GPIO.input(ECHO) == 0:
			start = time.time()
		while GPIO.input(ECHO) == 1:
			stop = time.time()
			
		check_time = stop-start
		distance = check_time * 34300/2
		print
