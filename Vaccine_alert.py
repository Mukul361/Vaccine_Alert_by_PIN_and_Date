import requests
from urllib.request import urlopen,Request
import json
from datetime import datetime
import time
import winsound
pincode=input('Enter the pincode: ')
datetobe=input('Enter date in format dd-mm-yyyy: ')
param={'pincode':pincode, 'date':datetobe}
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 5000  # Set Duration To 1000 ms == 1 second
headerapi = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
rurl ="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?"
r=requests.get(rurl, params=param)
apirequest=Request(url=r.url, headers=headerapi)

while True:
    currenttime= datetime.now()
    apidata=urlopen(apirequest)
    data =apidata.read()
    jsondata=json.loads(data)
    jsoncenters=jsondata['centers']
    j=len(jsoncenters)
    for i in range(j):
        if int(jsoncenters[i]['sessions'][0]['available_capacity']) >0:
            print ( jsoncenters[i]['name']  ,":",jsoncenters[i]['sessions'][0]['available_capacity'])
            winsound.Beep(frequency, duration)
    time.sleep(60)
