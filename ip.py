from pushbullet import Pushbullet
import requests
from time import sleep
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
pb = Pushbullet("o.FcXCqJ1cIbkPUzVIXklatsiEv63R5PcU")
print(pb.devices)



dev = pb.get_device('Google Pixel 2 XL')
dev2 = pb.get_device('Chrome')
push = dev.push_note("Alert!!", "wind is above 1 mph")
push = dev.push_link("get currents", "https://" + ip + ":5000/")
push = dev2.push_note("Alert!!", "wind is above 1 mph")
push = dev2.push_link("get currents", "https://" + ip + ":5000/")
        