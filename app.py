"""MyoCoach - Flask web application serving EMG visualisation and games.

Reads two EMG channels streamed by an Arduino board over USB serial and
exposes them as JSON to the browser-based interface.
"""

import json
import os
from time import time

import serial
from flask import Flask, make_response, render_template

# Must match the baud rate set in myocoach.ino
SERIAL_PORT = os.environ.get("MYOCOACH_PORT", "/dev/ttyACM0")
BAUD_RATE = int(os.environ.get("MYOCOACH_BAUD", "115200"))

app = Flask(__name__)

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except serial.SerialException:
    ser = None
    print(f"[MyoCoach] No board on {SERIAL_PORT} - serving zeros instead.")


@app.route("/")
def main():
    return render_template("template.html")


@app.route("/index", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/gaming")
def gaming():
    return render_template("gaming.html")


@app.route("/level1")
def level1():
    return render_template("level1.html")


@app.route("/level2")
def level2():
    return render_template("level2.html")


@app.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")


def read_emg():
    """Return the latest (EMG0, EMG1) pair in volts, or (0.0, 0.0)."""
    if ser is None:
        return 0.0, 0.0
    try:
        line = ser.readline().decode("utf-8").strip()
        emg0, emg1 = (float(value) for value in line.split(":"))
        return emg0, emg1
    except (ValueError, UnicodeDecodeError, serial.SerialException):
        return 0.0, 0.0


@app.route("/data", methods=["GET", "POST"])
def data():
    """Data format: [timestamp_ms, EMG0, EMG1]."""
    emg0, emg1 = read_emg()
    payload = [time() * 1000, emg0, emg1]

    response = make_response(json.dumps(payload))
    response.content_type = "application/json"
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
