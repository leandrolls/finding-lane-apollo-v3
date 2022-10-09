import time
import json
import requests
import random

def master():
    deviation = random.uniform(-4.0, 4.0)
    path = "lane"
    data = {'pos': deviation}

    time.sleep(2)

    print("sent", deviation)
    return wheeler(path, data)

def wheeler(path, data):
    url = "http://192.168.0.100:5000/" + path
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    try:
        return requests.post(url, data=json.dumps(data), headers=headers)
    except Exception:
        print("HTTP error")

while True:
    master()