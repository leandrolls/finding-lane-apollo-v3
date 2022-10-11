import cv2
import json
import requests
import random
import roslibpy
import time


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

################## FOR HTTP REQUESTS #####################

""" def send_direction(deviation, direcao):
    print(direcao)
    print(deviation)
    dev = (deviation*5)*random.uniform(-1, 1)
    path = "lane"
    data = {'pos': dev}
    print(dev)
    return post_method(path, data) """

"""  def post_method(path, data):
    url = "http://192.168.0.100:5000/" + path
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    try:
        requests.post(url, data=json.dumps(data), headers=headers)
    except Exception:
        print("Http error") """

###########################################################

def connect_ros():
    client = roslibpy.Ros(host='192.168.0.107', port=9090)
    try:
        client.run()
        print('Is ROS connected?', client.is_connected)
    except Exception:
        print("ROS Connection Error")
        client.terminate()
    return client

def publish_method(topic, data):
    ros_topic = roslibpy.Topic(connect_ros(), topic, 'std_msgs/Int16')
    try:
        return ros_topic.publish(roslibpy.Message({'data': data}))
    except Exception:
        print("Http error")

def send_lane_controllers(pos):
    topic = "controllers"
    data = 55 + int(pos * random.uniform(1.0, 5.0))
    if data < 41:
        data = 41
    elif data > 69:
        data = 69

    time.sleep(3)
    print(data)
    return publish_method(topic, data)