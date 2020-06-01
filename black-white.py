# import cv2

# img_grey = cv2.imread('test2.jpg', cv2.IMREAD_GRAYSCALE)
# thresh = 95
# img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

# cv2.imwrite('test2_bw.jpg',img_binary) 

import cv2

thresh = 95
img_grey = cv2.imread('before.jpg', cv2.IMREAD_GRAYSCALE)
img_binary = cv2.adaptiveThreshold(img_grey, 255, thresh, cv2.THRESH_BINARY, 11, 2)

cv2.imwrite('after.jpg',img_binary) 