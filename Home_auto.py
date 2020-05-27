import requests
import RPi.GPIO as r
r.setmode(r.BOARD)
r.setup(7,r.OUT)
#r.setup(3,r.OUT)
while(1):
    a=requests.get("https://api.thingspeak.com/channels/804611/feeds.json?api_key=JIHJ8WHJRM4SKPWD&results=1")
    a=a.json()

    b=a['feeds'][0]["field1"]
    print(b)
    if b=='on':
        r.output(7,1)
        #r.output(3,0)
    elif b=='off':
        r.output(7,0)
        #r.output(3,1)
