import cv2
import numpy as np

def noiseReduce(img):

    kernel = np.ones((5,5), np.uint8)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.dilate(img, kernel, iterations=1)

    return img