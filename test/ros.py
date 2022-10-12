import random
import time
import roslibpy


def connect_ros():
    client = roslibpy.Ros(host='192.168.0.17', port=9090)
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
    print(pos)

    time.sleep(5)
    return publish_method(topic, pos)

while True:
    send_lane_controllers(random.uniform(-5, 5))