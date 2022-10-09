import cv2
import matplotlib.pyplot as plt
import numpy as np

def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny_img = cv2.Canny(blur, 50, 150)
    return canny_img

imag = cv2.imread("teste-fiap-0510-1.jpg")
lane_image = np.copy(imag)
canny_image = canny(lane_image)

plt.imshow(canny_image)
plt.show()