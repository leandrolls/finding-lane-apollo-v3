import cv2
import json
import requests
import random

def addText(img, radius, direction, deviation, devDirection):
    text = "APOLLO AUTONOMUS VEHICLE"
    font = cv2.FONT_HERSHEY_SIMPLEX

    if (direction != 'Reta'):
        text1 = 'Raio de curvatura: ' + '{:04.0f}'.format(radius) + 'm'
        text2 = 'Direcao da curva: ' + (direction)

    else:
        text1 = 'Raio de curvatura: ' + 'N/A'
        text2 = 'Direcao da curva: ' + (direction)

    cv2.putText(img, text, (50, 100), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, text1, (50, 150), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(img, text2, (50, 200), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    deviation_text = 'Desalinhado ' + str(round(abs(deviation), 3)) + 'm' + ' para ' + devDirection
    cv2.putText(img, deviation_text, (50, 250), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    return img

def send_direction(deviation, direcao):
    print(direcao)
    print(deviation)

    dev = (deviation*5)*random.uniform(-1, 1)

    path = "lane"
    data = {'pos': dev}


    print(dev)

    return post_method(path, data)

def post_method(path, data):
    data2 = {}
    url = "http://192.168.0.100:5000/" + path
    #url2 = "http://192.168.0.100:5000/controllers/handle-motor"
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    try:
        #return requests.post(url, data=json.dumps(data), headers=headers)
        requests.post(url, data=json.dumps(data), headers=headers)
        #requests.post(url2, data=json.dumps(data2), headers=headers)
    except Exception:
        print("Http error")