import cv2


def readVideo():
    # input = cv2.VideoCapture('static/video_test.mp4')
    #input = cv2.VideoCapture(1)
    input = cv2.VideoCapture('http://192.168.0.102:5000/stream.mjpg')

    return input
