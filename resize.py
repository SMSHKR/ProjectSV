import PIL
from PIL import Image

baseheight = 300
img = Image.open('อุรชา/10_bw.jpg')
hpercent = (baseheight / float(img.size[1]))
wsize = int((float(img.size[0]) * float(hpercent)))
img = img.resize((wsize, baseheight), PIL.Image.ANTIALIAS)
img.save('อุรชา/10_bw_rs.jpg')