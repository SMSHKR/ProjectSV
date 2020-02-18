import cv2
import numpy as np

def adaptiveCrop(img, thresh):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.adaptiveThreshold(img, 255, thresh, cv2.THRESH_BINARY, 11, 2)

    points = np.argwhere(img == 0)
    points = np.fliplr(points)
    x, y, w, h = cv2.boundingRect(points)
    crop = img[y:y+h, x:x+w]

    img = cv2.adaptiveThreshold(crop, 255, thresh, cv2.THRESH_BINARY, 11, 2)

    return img