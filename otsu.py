import cv2
import numpy as np

def otsuCrop(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, img) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    points = np.argwhere(img == 0)
    points = np.fliplr(points)
    x, y, w, h = cv2.boundingRect(points)
    crop = img[y:y+h, x:x+w]

    (retval, img) = cv2.threshold(crop, thresh, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    return img