from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask (__name__)

LED = 8
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/led")
def led():
    state = request.args.get("state", "error")
    if state == "on":
        GPIO.output(LED, GPIO.HIGH)
        return "LED" + state
    elif state == "off":
        GPIO.output(LED, GPIO.LOW)
    elif state == "error":
        return "query string state send fail"
    else:
        return "wron query string sended"
    return "LED " + state


@app.route("/gpio/cleanup")
def gpio_cleanup():
    GPIO.cleanup()
    return "GPIO Cleanup"

if __name__ == "__main__":
    app.run (host = "0.0.0.0")