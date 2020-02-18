import cv2
from noizri import noiseReduce
from otsu import otsuCrop
from threshold import threshCrop
from adaptive import adaptiveCrop

for index in range(1, 11):

    infile = str(index) + '.jpg'
    outfile = 'c' + infile

    img = cv2.imread(infile)
    img = noiseReduce(img)

    # img = threshCrop(img)
    img = otsuCrop(img)
    # img = adaptiveCrop(img, cv2.ADAPTIVE_THRESH_MEAN_C)
    # img = adaptiveCrop(img, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)

    cv2.imwrite(outfile, img)