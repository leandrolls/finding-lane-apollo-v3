import cv2
import numpy as np
from matplotlib import pyplot as plt


def perspectiveWarp(input):
    img_size = (input.shape[1], input.shape[0])

    # Up Left (x, y)
    # Up Right (x, y)
    # Down Left (x, y)
    # Down Right (x, y)

    # Closer
    #src = np.float32([[135, 200],
     #                  [405, 200],
      #                 [0, 350],
       #                [520, 350]])

    ## Default vision
    #src = np.float32([[195, 100],
     #                 [350, 100],
      #                [0, 350],
       #               [520, 350]])

    src = np.float32([[210, 300],
                     [600, 300],
                     [0, 600],
                     [600, 600]])

    # Video Resolution Cut
    dst = np.float32([[0, 0],
                     [640, 0],
                     [0, 480],
                     [640, 480]])

    ######################################
    # VIDEO TEST

    #src = np.float32([[590, 440],
     #                 [690, 440],
      #                [200, 640],
       #               [1000, 640]])

    # Window to be shown
    #dst = np.float32([[200, 0],
     #                 [1200, 0],
      #                [200, 710],
       #               [1200, 710]])

    ##################

    matrix = cv2.getPerspectiveTransform(src, dst)

    minv = cv2.getPerspectiveTransform(dst, src)
    birdseye = cv2.warpPerspective(input, matrix, img_size)

    height, width = birdseye.shape[:2]

    birdseyeLeft = birdseye[0:height, 0:width // 2]
    birdseyeRight = birdseye[0:height, width // 2:width]

    ## If you want to see the bird view, just uncomment the three lines above.
    cv2.imshow("Birdseye" , birdseye)
    cv2.imshow("Birdseye Left" , birdseyeLeft)
    cv2.imshow("Birdseye Right", birdseyeRight)

    return birdseye, birdseyeLeft, birdseyeRight, minv


def plotHistogram(input):
    histogram = np.sum(input[input.shape[0] // 2:, :], axis=0)

    midpoint = np.int_(histogram.shape[0] / 2)
    leftxBase = np.argmax(histogram[:midpoint])
    rightxBase = np.argmax(histogram[midpoint:]) + midpoint

    plt.xlabel("Image X Coordenadas")
    plt.ylabel("Número de Pixels brancos")

    return histogram, leftxBase, rightxBase
