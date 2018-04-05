from PIL.Image import open, new
from PIL import Image
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale


for i in range(1,65,1):
    #print i
    #img = open('./ManuOralImages/Abnormal/%d.jpg' % i)
    #img.convert('RGB')
    #new_img = img.resize((128,128))
    #new_img.save('./ManuOralImages/resizeAbnormal/resizedA%d.jpg' % i)

    img = Image.open('./ManuOralImages/resizeNormalpng/resizedN%d.png' % i)
    img.save('./ManuOralImages/resizeNormaljpg/resizedN%d.jpg' % i, 'jpeg')