import time

# OSC support
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import argparse

def distance(x, y):
    if x >= y:
        result = x - y
    else:
        result = y - x
    return result

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

i = True
position = 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="192.168.1.18",
        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8050,
        help="The port the OSC server is listening on")
    args = parser.parse_args()

    client = udp_client.SimpleUDPClient(args.ip, args.port)



while i == True :
    position += 1
    if position == 200:
        position = 0

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

    time.sleep(0.01)
