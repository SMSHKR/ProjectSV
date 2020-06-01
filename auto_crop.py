# https://stackoverflow.com/questions/14211340/automatically-cropping-an-image-with-python-pil

from PIL import Image
import numpy as np

def black_and_white_dithering(input_image_path,
    output_image_path,
    dithering=False):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert('1')  
    else:
        bw = color_image.convert('1',
    dither=Image.NONE)
    bw.save(output_image_path)
if __name__ == '__main__':
    black_and_white_dithering(
        'อุรชา/*.jpg',
        'อุรชา/*_bw.jpg')

# image=Image.open('test.jpg')
# image.load()

# image_data = np.asarray(image)
# image_data_bw = image_data.max(axis=2)
# non_empty_columns = np.where(image_data_bw.max(axis=0)>0)[0]
# non_empty_rows = np.where(image_data_bw.max(axis=1)>0)[0]
# cropBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))

# image_data_new = image_data[cropBox[0]:cropBox[1]+1, cropBox[2]:cropBox[3]+1 , :]

# new_image = Image.fromarray(image_data_new)
# new_image.save('test_cropped.jpg')