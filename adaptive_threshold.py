# https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html

import cv2
import numpy as np

img = cv2.imread('test2.jpg',0)
img = cv2.medianBlur(img,5)

img = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imwrite('test2_at.jpg',img)