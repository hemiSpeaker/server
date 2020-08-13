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
#run_with_ngrok(app)  # Start ngrok when app is run

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.18",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8050,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)



@app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)

@app.route('/api/volume/speaker_1',methods = ['POST'])
def speaker_1():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_1", int(message))
      #client.send_message("/speaker_2", 0)
      #client.send_message("/speaker_3", 0)
      client.send_message("/speaker_4", 0)
      client.send_message("/speaker_5", 0)


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

@app.route('/api/volume/speaker_5',methods = ['POST'])
def speaker_5():
   if request.method == 'POST':
      message = request.form.get("value")
      #message = message["message"]
      print(message)
      client.send_message("/speaker_5", int(message))


      return "HELLO"
        

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000)
   #app.run()
