import random
import time
import roslibpy


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
    ros_topic = roslibpy.Topic(connect_ros(), topic, 'std_msgs/Float64')
    try:
        return ros_topic.publish(roslibpy.Message({'data': data}))
    except Exception:
        print("Http error")


def send_lane_controllers(pos):
    topic = "lanes"
    #data = 55 + int(pos * random.uniform(1.0, 5.0))
    #if data < 41:
    #    data = 41
    #elif data > 69:
    #    data = 69

    #time.sleep(3)
    #print(data)
    data = pos*10
    print(data)

    time.sleep(5)
    return publish_method(topic, pos)


while True:
    random_pos = random.uniform(-20.0, 20.0)
    send_lane_controllers(random_pos)
