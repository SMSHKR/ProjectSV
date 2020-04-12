import cv2
 
img = cv2.imread('test2.jpg', cv2.IMREAD_UNCHANGED)

height = 100
width = int(img.shape[1] * height / img.shape[0])
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
cv2.imwrite('test2_rs.jpg',resized)