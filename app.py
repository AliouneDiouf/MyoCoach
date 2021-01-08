from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import serial
from time import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0', 9600)


@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/tutorials')
def tutorials():
  return render_template("tutorials.html")

@app.route('/gaming')
def gaming():
  return render_template("gaming.html")


@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/")
def main():
  return render_template("template.html")


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Sensor_EMG1, Sensor_EMG2]
   
    
    line = ser.readline()
    
    line = ser.readline().decode("utf-8").strip('\n').strip('\r')  # remove newline and carriage return characters
    print "Received: '{}'".format(line)
    dataEMG = line.split(':')
    for i in range(len(dataEMG)):
        print "data[{}]".format(i), dataEMG[i]
   
   
    
    Sensor_EMG1 = float(dataEMG[0])
    Sensor_EMG2 = float(dataEMG[1])
    

    data = [time() * 1000, Sensor_EMG1, Sensor_EMG2]
    
    print("DataEMGs= ", data)

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
  app.run(host='192.168.1.115', port=5000)
    



