
from PIL.Image import open, new
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale

img = open("./grey_img01.bmp")
pixelVal = list(img.getdata())
print pixelVal