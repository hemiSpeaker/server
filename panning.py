import time

# OSC support
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import argparse

speaker_1 = 0
speaker_2 = 0
speaker_3 = 0
speaker_4 = 0
speaker_5 = 0


i = True
position = 0


koukou
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
    speaker_1 = position
    speaker_2 = position + 1*40
    speaker_3 = position + 2*40
    speaker_4 = position + 3*40
    speaker_5 = position + 4*40
    print("speaker 1 : " + str(speaker_1))
    print("speaker_2 :" + str(speaker_2))
    print("speaker_3 :" + str(speaker_3))
    print("speaker_4 :" + str(speaker_4))
    print("speaker_5 :" + str(speaker_5))


    client.send_message("/speaker_1", int(speaker_1))
    client.send_message("/speaker_2", int(speaker_2))
    client.send_message("/speaker_3", int(speaker_3))
    client.send_message("/speaker_4", int(speaker_4))
    client.send_message("/speaker_5", int(speaker_5))

    #i += 1 
    if speaker_2 > 200  : 
        speaker_2 = speaker_2 - 200
        print("if speaker val : " + str(speaker_2))
        #i += 1 
        speaker_2 = 0
    if speaker_3 > 200  : 
        speaker_3 = speaker_3 - 200
        print("if speaker val : " + str(speaker_3))
        #i += 1 
        speaker_3 = 0
    if speaker_4 > 200  : 
        speaker_4 = speaker_4 - 200
        print("if speaker val : " + str(speaker_4))
        #i += 1 
        speaker_4 = 0
    if speaker_5 > 200  : 
        speaker_5 = speaker_5 - 200
        print("if speaker val : " + str(speaker_5))
        #i += 1 
        speaker_5 = 0
    time.sleep(0.4)