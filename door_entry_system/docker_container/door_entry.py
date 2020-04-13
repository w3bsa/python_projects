import RPi.GPIO as GPIO
import time
from flask import Flask, jsonify

def init_gpio_pins():
    GPIO.setmode(GPIO.BCM)
    pinlist = [2, 3]
    for i in pinlist:
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.HIGH)

def unlock(duration):
    GPIO.output(relay_1, GPIO.LOW)
    time.sleep(duration)
    GPIO.output(relay_1, GPIO.HIGH)
    GPIO.cleanup()

#GPIO pin mappings
relay_1 = 2 #Door strike (normally open)
relay_2 = 3 #Unused

#Set relay close timer
unlock_duration = 5 #Number of seconds to keep door unlocked

#API endpoint to unlock door strike
app = Flask(__name__)

@app.route("/unlock")
def home():
    init_gpio_pins()
    return jsonify({"status":"door was unlocked for 5 seconds"}), 200
    unlock(unlock_duration)
    #return jsonify({"status":"door was unlocked for 5 seconds"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')