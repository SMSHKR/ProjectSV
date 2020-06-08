import cv2

img = cv2.imread('test2.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 75
img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imwrite('test2_bw.jpg',img)