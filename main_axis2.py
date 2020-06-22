# https://stackoverflow.com/questions/43863931/contour-axis-for-image

import cv2
import numpy as np
import math
from scipy import ndimage

#loading our BW image
img = cv2.imread("test2_at_ed.jpg", 0)
h, w = img.shape

#From a matrix of pixels to a matrix of coordinates of non-black points.
#(note: mind the col/row order, pixels are accessed as [row, col]
#but when we draw, it's (x, y), so have to swap here or there)
mat = np.argwhere(img != 255)
mat[:, [0, 1]] = mat[:, [1, 0]]
mat = np.array(mat).astype(np.float32) #have to convert type for PCA

#mean (e. g. the geometrical center) 
#and eigenvectors (e. g. directions of principal components)
m, e = cv2.PCACompute(mat, mean = np.array([]))

#now to draw: let's scale our primary axis by 100, 
#and the secondary by 50
center = tuple(m[0])
endpoint1 = tuple(m[0] + e[0]*100)
endpoint2 = tuple(m[0] + e[1]*100)

print(center)
print(endpoint1)

cv2.circle(img, center, 5, 128)
# cv2.line(img, center, right, 128)
cv2.line(img, center, endpoint1, 0)
cv2.line(img, center, endpoint2, 128)

delta0 = endpoint1[0]-center[0]
delta1 = endpoint1[1]-center[1]
print(delta0)
print(delta1)
angle = math.atan2(delta0, delta1)
angle = angle*180/math.pi
print(angle)
inv = cv2.bitwise_not(img)
rotated = ndimage.rotate(inv, 90-angle)
inv = cv2.bitwise_not(rotated)
img = inv

cv2.imwrite("test2_at_ed_ma.jpg", img)