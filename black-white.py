import cv2

img_grey = cv2.imread('test2.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 95
img_binary = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('test2_bw.jpg',img_binary) 