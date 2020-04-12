import cv2
import numpy as np
import math
from scipy import ndimage
import functools

# black-white.py
img_grey = cv2.imread('test2.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 150
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# erosion-dilation.py
kernel = np.ones((3,3),np.uint8)
dilation = cv2.dilate(img_binary,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)

# main_axis2.py
h, w = erosion.shape
mat = np.argwhere(erosion != 0)
mat[:, [0, 1]] = mat[:, [1, 0]]
mat = np.array(mat).astype(np.float32)
m, e = cv2.PCACompute(mat, mean = np.array([]))
center = tuple(m[0])
endpoint1 = tuple(m[0] + e[0]*100)
endpoint2 = tuple(m[0] + e[1]*100)
cv2.circle(erosion, center, 5, 128)
cv2.line(erosion, center, endpoint2, 128)
delta0 = endpoint1[0]-center[0]
delta1 = endpoint1[1]-center[1]
angle = math.atan2(delta0, delta1)
angle = angle*180/math.pi
print(angle)
inv = cv2.bitwise_not(erosion)
rotated = ndimage.rotate(inv, -angle)
inv = cv2.bitwise_not(rotated)

# auto_crop2.py
points = np.argwhere(inv==0)
points = np.fliplr(points)
x, y, w, h = cv2.boundingRect(points)
crop = inv[y:y+h, x:x+w]

# resize2.py
height = 100
width = int(crop.shape[1] * height / crop.shape[0])
dim = (width, height)
resize = cv2.resize(crop, dim, interpolation = cv2.INTER_AREA)

# add_white.py
desired_size = 500
old_size = resize.shape[:2]
old_size_int = functools.reduce(lambda sub, ele: sub * 10 + ele, old_size)
top = bottom = left = 0
right = desired_size - old_size[0]
color = [255, 255, 255]
white = cv2.copyMakeBorder(resize, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

cv2.imwrite('test2_all.jpg',white)