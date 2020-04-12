# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_morphological_ops/py_morphological_ops.html
import cv2
import numpy as np

img = cv2.imread('test.jpg',0)
kernel = np.ones((3,3),np.uint8)

# ย่อ
dilation = cv2.dilate(img,kernel,iterations = 1)

# ขยาย
erosion = cv2.erode(dilation,kernel,iterations = 1)

# # ลบ noise ข้างนอกเส้น
# opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# ลบ noise ข้างในเส้น
# closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('test_ed.jpg',erosion)