from pushbullet import Pushbullet
import requests
from time 
from time import sleep
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
pb = Pushbullet("o.FcXCqJ1cIbkPUzVIXklatsiEv63R5PcU")
print(pb.devices)


t = 0
tme = 0
while True:
    r = requests.get("http://192.168.1.188/wflexp.json")
    windspeed = r.json()['windavg2'] #GET AVERGAE WIND SPEED FOR THE LAST 2 MINS
    windspeed = float(windspeed)
    if windspeed < 1:
        print "light to no wind"
        sleep(2)

    elif windspeed > 1 and t == 0:

        print "wind gusts"
        
        dev = pb.get_device('Google Pixel 2 XL')
        push = dev.push_note("Alert!!", "wind is above 1 mph")
        push = pb.push_link("get currents", "https://" + ip + ":5000/")
        t =+ 1
        tme = time.perf_counter()

    elif windspeed > 1 and (tme - time.perf_counter()) > 3600:  #ENSURE AN HOUR HAS GONE PAST BEFORE SENDING ANOTHER UPDATE

        print "wind gusts"
        
        dev = pb.get_device('Google Pixel 2 XL')
        push = dev.push_note("Alert!!", "wind is above 1 mph")
        push = pb.push_link("get currents", "https://" + ip + ":5000/")
        tme = time.perf_counter() #RESET HOUR COUNTER

