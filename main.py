import cv2
import numpy as np
from matplotlib import pyplot as plt
from utilidades import detection as dt
from utilidades import capture as cp
from utilidades import commands as cd
from utilidades import center as ce
from utilidades import lane as ln
from utilidades import warp as wp

image = cp.readVideo()
rosdasdass = cd.connect_ros()

# 1920x1080

def processImage(inpImage):
    hls = cv2.cvtColor(inpImage, cv2.COLOR_BGR2HLS)
    lower_white = np.array([0, 160, 10])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(inpImage, lower_white, upper_white)
    hls_result = cv2.bitwise_and(inpImage, inpImage, mask=mask)

    gray = cv2.cvtColor(hls_result, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
    blur = cv2.GaussianBlur(thresh, (3, 3), 0)
    canny = cv2.Canny(blur, 40, 60)

    # Display the processed images
    #    cv2.imshow("Image", inpImage)
    #    cv2.imshow("HLS Filtered", hls_result)
    #    cv2.imshow("Grayscale", gray)
    #    cv2.imshow("Thresholded", thresh)
    #    cv2.imshow("Blurred", blur)
    #    cv2.imshow("Canny Edges", canny)

    return image, hls_result, gray, thresh, blur, canny


while True:

    _, frame = image.read()

    birdView, birdViewL, birdViewR, minverse = wp.perspectiveWarp(frame)
    img, hls, grayscale, thresh, blur, canny = processImage(birdView)
    imgL, hlsL, grayscaleL, threshL, blurL, cannyL = processImage(birdViewL)
    imgR, hlsR, grayscaleR, threshR, blurR, cannyR = processImage(birdViewR)
    hist, leftBase, rightBase = wp.plotHistogram(thresh)
    plt.plot(hist)
    # print("HIST", hist)
    # print("THRESH", thresh)


    #try:
    #   slope, intercept = line_parameters
    #except TypeError:
    #    slope, intercept = 0.00001, 0.00001

    try:
        ploty, left_fit, right_fit, left_fitx, right_fitx = dt.slide_window_search(thresh, hist)
    except:
        continue

    # print("PLOTY", ploty)
    # print("LEFT FIT", left_fit)
    # print("LEFT_FITX", left_fitx)
    # print("RIGHT FIX", right_fit)
    # print("RIGHT FITX", right_fitx)

    plt.plot(left_fit)
    draw_info = dt.general_search(thresh, left_fit, right_fit)
    curveRad, curveDir = ln.measure_lane_curvature(ploty, left_fitx, right_fitx)
    meanPts, result = ln.draw_lane_lines(frame, thresh, minverse, draw_info)
    deviation, directionDev = ce.offCenter(meanPts, frame)
    finalImg = cd.addText(result, curveRad, curveDir, deviation, directionDev)
    cd.send_lane_controllers(rosdasdass, deviation)

    cv2.imshow("Apollo Autonomus Vehicle Detection", finalImg)

    if cv2.waitKey(1) == 13:
        break

image.release()
cv2.destroyAllWindows()
