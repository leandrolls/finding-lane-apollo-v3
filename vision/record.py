import cv2


webcam = cv2.VideoCapture(1)
video = cv2.VideoWriter('webcam-0510-1.mp4', cv2.VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))


while True:
    stream_ok, frame = webcam.read()
    if stream_ok:
        cv2.imshow('GRAVANDO WEBCAM', frame)
        video.write(frame)

    if cv2.waitKey(1) & 0xFF == 27: break


cv2.destroyAllWindows()

webcam.release()
video.release()







