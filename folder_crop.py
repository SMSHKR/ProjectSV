import cv2
import numpy as np

def crop(infile, outfile, thresh=127):

    originalImage = cv2.imread(infile)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, thresh, maxval=255, type=cv2.THRESH_BINARY)

    # find where the signature is and make a cropped region
    points = np.argwhere(blackAndWhiteImage==0) # find where the black pixels are
    points = np.fliplr(points) # store them in x,y coordinates instead of row,col indices
    x, y, w, h = cv2.boundingRect(points) # create a rectangle around those points
    crop = grayImage[y:y+h, x:x+w] # create a cropped region of the gray image

    # get the thresholded crop
    (retval, thresh_crop) = cv2.threshold(crop, thresh, maxval=255, type=cv2.THRESH_BINARY)

    # cv2.imshow('Cropped image', thresh_crop)
    cv2.imwrite(outfile, thresh_crop)
    
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


for index in range(1, 11):
    infile = str(index) + '.jpg'
    outfile = 'c' + infile
    crop(infile, outfile)