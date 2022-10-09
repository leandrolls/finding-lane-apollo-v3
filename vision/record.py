################################
#
#   Record video from webcam
#
#             by
#
#      Code Monkey King
#
################################

# packages
import cv2

# open the webcam video stream
webcam = cv2.VideoCapture(1)

# open output video file stream
video = cv2.VideoWriter('webcam-0510-1.mp4', cv2.VideoWriter_fourcc(*'MP42'), 25.0, (640, 480))

# main loop
while True:
    # get the frame from the webcam
    stream_ok, frame = webcam.read()

    # if webcam stream is ok
    if stream_ok:
        # display current frame
        cv2.imshow('GRAVANDO WEBCAM', frame)

        # write frame to the video file
        video.write(frame)

    # escape condition
    if cv2.waitKey(1) & 0xFF == 27: break

# clean ups
cv2.destroyAllWindows()

# release web camera stream
webcam.release()

# release video output file stream
video.release()







