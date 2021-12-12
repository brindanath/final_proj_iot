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





r = requests.get("http://192.168.1.188/wflexp.json")

windspeed = r.json()['windspd']
windspeed = float(windspeed)

while True:
    r = requests.get("http://192.168.1.188/wflexp.json")
    windspeed = r.json()['windspd']
    windspeed = float(windspeed)
    if windspeed < 1:
        print "light to no wind"
        sleep(2)
    elif windspeed > 1:
        print "wind gusts"
        
        dev = pb.get_device('Google Pixel 2 XL')
        push = dev.push_note("Alert!!", "wind is above 1 mph")
        push = pb.push_link("get currents", "https://" + ip + ":5000/")
        sleep(3600)


