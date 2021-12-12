import socket
from requests.exceptions import ConnectionError
from time import sleep
from pushbullet import Pushbullet
import requests
from time import sleep
import socket
sa = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sa.connect(("8.8.8.8", 80))
ip = sa.getsockname()[0]
sa.close()



HOST = "192.168.1.133" # IP address of your Raspberry PI
PORT = 65432          # The port used by the server




t=0


while True:

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

            s.connect((HOST, PORT))
            sleep(10)
    
    except ConnectionRefusedError as e:    # This is the correct syntax
       print("no connection")
       t = t + 1
       print(t)
       sleep(5)
    finally:
       print(t)
       if t  > 2:
            break
            print(t)
            pb = Pushbullet("o.FcXCqJ1cIbkPUzVIXklatsiEv63R5PcU")
            dev = pb.get_device('Google Pixel 2 XL')
            push = dev.push_note("Alert!!", "The power is out")
       

print("hello")