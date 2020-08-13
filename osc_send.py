# OSC support
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import argparse
import random
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.18",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8050,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)


i = 1
while i < 6:
    print(i)
    for x in range(127):
        client.send_message("/speaker_1", x)
        client.send_message("/speaker_2", x)
        client.send_message("/speaker_3", x)
        client.send_message("/speaker_4", x)
        client.send_message("/speaker_5", x)
        time.sleep(0.1)
    x = 0
        
