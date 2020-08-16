import time
import matplotlib.pyplot as plt 

# OSC support
from pythonosc import dispatcher
from pythonosc import osc_server
from pythonosc import udp_client

import math
import argparse


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
distance = 1
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
i = 0
x = []

speaker_0_Volume_Tabl = []
speaker_1_Volume_Tabl = []
speaker_2_Volume_Tabl = []
speaker_3_Volume_Tabl = []
speaker_4_Volume_Tabl = []

spread = 0

while i < 30 :
    
    position += 1
    if position == 200:
        position = 0
    if i >= 10 :
        spread += 0.001
    if i >= 20 :
        distance -= 0.001
        if distance <= 0 :
            distance = 1
    

    speaker_0_Volume =  math.sin(i ) * distance
    speaker_1_Volume =  math.sin(i + spread) * distance
    speaker_2_Volume =  math.sin(i + spread * 2) * distance
    speaker_3_Volume =  math.sin(i + spread * 3) * distance
    speaker_4_Volume =  math.sin(i + spread * 4) * distance
    x.append(i)
    speaker_0_Volume_Tabl.append(speaker_0_Volume)
    speaker_1_Volume_Tabl.append(speaker_1_Volume)
    speaker_2_Volume_Tabl.append(speaker_2_Volume)
    speaker_3_Volume_Tabl.append(speaker_3_Volume)
    speaker_4_Volume_Tabl.append(speaker_4_Volume)
    

    print("speaker_0 :" + str(speaker_0_Volume))
    print("speaker_1 :" + str(speaker_1_Volume))
    print("speaker_2 :" + str(speaker_2_Volume))
    print("speaker_3 :" + str(speaker_3_Volume))
    print("speaker_4 :" + str(speaker_4_Volume))

    print("pedistance :" + str(distance))


    client.send_message("/speaker_0", int(speaker_0_Volume))
    client.send_message("/speaker_1", int(speaker_1_Volume))
    client.send_message("/speaker_2", int(speaker_2_Volume))
    client.send_message("/speaker_3", int(speaker_3_Volume))
    client.send_message("/speaker_4", int(speaker_4_Volume))
    i += 0.01



    #time.sleep(0.1)
plt.plot(x, speaker_0_Volume_Tabl, label = "speaker_0_Volume")
plt.plot(x, speaker_1_Volume_Tabl, label = "speaker_1_Volume")
plt.plot(x, speaker_2_Volume_Tabl, label = "speaker_2_Volume")
plt.plot(x, speaker_3_Volume_Tabl, label = "speaker_3_Volume")
plt.plot(x, speaker_4_Volume_Tabl, label = "speaker_4_Volume")
plt.show() 
