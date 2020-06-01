# https://stackoverflow.com/questions/43391205/add-padding-to-images-to-get-them-into-the-same-shape
import cv2
import functools

desired_size = 1000

im = cv2.imread('test2_all.jpg')
old_size = im.shape[:2] # old_size is in (height, width) format

# convert tuple to int
old_size_int = functools.reduce(lambda sub, ele: sub * 10 + ele, old_size)

# ratio = float(desired_size)/max(old_size)
# new_size = tuple([int(x*ratio) for x in old_size])

# new_size should be in (width, height) format

# im = cv2.resize(im, (new_size[1], new_size[0]))
 
top = bottom = left = 0
right = desired_size - old_size[0]

color = [255, 255, 255]
new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)

cv2.imwrite('test2_aw.jpg',new_im)

# cv2.imshow("image", new_im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()