from flask import Flask, render_template, request
import json 
from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app) # This will enable CORS for all routes
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import subprocess
#from flask_ngrok import run_with_ngrok

# OSC support
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import argparse
import random
import time


import json

# Getting configuration params
with open('config.json') as json_data_file:
    conf = json.load(json_data_file)

client_ip = conf["client_ip"]

#run_with_ngrok(app)  # Start ngrok when app is run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default=client_ip,
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8050,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)

print("Osc server sending to : " + client_ip + " adress")

@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/api/volume/speaker_0',methods = ['POST'])
def speaker_0():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_0", int(message))
      #client.send_message("/speaker_1", 0)
      #client.send_message("/speaker_2", 0)
      client.send_message("/speaker_3", 0)
      client.send_message("/speaker_4", 0)


      return "HELLO"


@app.route('/api/volume/speaker_1',methods = ['POST'])
def speaker_1():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_1", int(message))


      return "HELLO"

@app.route('/api/volume/speaker_2',methods = ['POST'])
def speaker_2():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_2", int(message))


      return "HELLO"

@app.route('/api/volume/speaker_3',methods = ['POST'])
def speaker_3():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_3", int(message))


      return "HELLO"

@app.route('/api/volume/speaker_4',methods = ['POST'])
def speaker_4():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_4", int(message))


      return "HELLO"


speaker_0 = 0
speaker_1 = 50
speaker_2 = 100
speaker_3 = 150
speaker_4 = 200

speaker_0_Volume = 0
speaker_1_Volume = 0
speaker_2_Volume = 0
speaker_3_Volume = 0
speaker_4_Volume = 0

maxVolume = 200 ## distance?


@app.route('/api/volume/panPos',methods = ['POST'])
def panPos():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      position = int(message)
      print(message)
      speaker_0_Volume = maxVolume - abs(position - speaker_0)
      speaker_1_Volume = maxVolume - abs(position - speaker_1)
      speaker_2_Volume = maxVolume - abs(position - speaker_2)
      speaker_3_Volume = maxVolume - abs(position - speaker_3)
      speaker_4_Volume = maxVolume - abs(position - speaker_4)

      print("speaker_0 :" + str(speaker_0_Volume))
      print("speaker_1 :" + str(speaker_1_Volume))
      print("speaker_2 :" + str(speaker_2_Volume))
      print("speaker_3 :" + str(speaker_3_Volume))
      print("speaker_4 :" + str(speaker_4_Volume))


      client.send_message("/speaker_0", int(speaker_0_Volume))
      client.send_message("/speaker_1", int(speaker_1_Volume))
      client.send_message("/speaker_2", int(speaker_2_Volume))
      client.send_message("/speaker_3", int(speaker_3_Volume))
      client.send_message("/speaker_4", int(speaker_4_Volume))


      return "HELLO" 

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
   #app.run()
