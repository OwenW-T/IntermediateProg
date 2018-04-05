"""
Project:      hw09-cartoon_art.py

Description:

Name:

Date:

Notes:        Install the following libraries. In an SSH Terminal enter
              the following:

              sudo apt-get install libjpeg8-dev
              sudo apt-get install zlib1g-dev
              sudo pip install Pillow

              You may need to update pip in order to uninstall Pillow. In terminal do the following:
              sudo pip install --upgrade pip
"""
# -------------------------------------------------------------------------------


from PIL.Image import open, new
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale


class CartoonArt:

    def __init__(self):
        self.spacing = 4  # spacing for dots and lines
        self.palette = []
        self.colors = []
        self.color_palette = ["D46A6A", "FFAAAA", "801515", "550000", "AA3939"]

    def hex_to_rgb(self, hex):
        """ Convert a given color from a hexadecimal value to a rgb tuple. For
            example a hex value of "C9A814" would get converted to (201, 168, 20).
            Returns the tuple value as a string.
            Parameters:
            [In] hex - the hexidecimal code (string) representing a color value.
        """
        # print '#' + hex, "  ", getrgb('#' + hex)
        return getrgb('#' + hex)  # convert to hex value

    def rgb_to_hex(self, rgb):
        """ Convert a given color from a rgb tuple to a hexadecimal value. For
            example a rgb value of (201, 168, 20) would get converted to C9A814.
            It returns the hexadecimal value as a string.
            Parameters:
            [In] rgb - a tubple representing an rgb value.
        """
        hexValue = '%02x%02x%02x' % rgb
        # print rgb, "  ", hexValue.upper()
        return hexValue.upper()

    def make_cartoon_pic(self, pixels, palette): #palette is a list of 5 values
        new_pixels = []

        #print pixels

        for p in pixels: #theoretically, pixels would be the list of greyscale pixels #do i need to say length of pixels? should pixels be in list or internal data structure?
            #print p
            if p <= 49: #if pixels[p] <= 49:
                new_pixels.append(self.hex_to_rgb(palette[0]))
                #print "0"
            elif p >= 50 and p <= 99: #elif pixels[p] >= 50 and pixels[p] <= 99:
                new_pixels.append(self.hex_to_rgb(palette[1]))
                #print "1"
            elif p >= 100 and p <= 149: # elif pixels[p] >= 100 and pixels[p] <= 149:
                new_pixels.append(self.hex_to_rgb(palette[2]))
                #print "2"
            elif p >= 150 and p <= 199: #elif pixels[p] >= 150 and pixels[p] <= 199:
                new_pixels.append(self.hex_to_rgb(palette[3]))
                #print "3"
            elif p >= 200: #elif pixels[p] >= 200:
                new_pixels.append(self.hex_to_rgb(palette[4]))
                #print "4"

        return new_pixels

    def make_pattern(self, image, hex_color, pattern_color): #IS THIS CORRECT, I FEEL LIKE IT ISNT

        w,h = image.size
        #print("width:", w, " / height:", h)
        #color = self.hex_to_rgb(hex_color)

        #img.putpixel((50,50), color)
        #img.putpixel((50, 51), color)
        #img.putpixel((50, 52), color)
        #img.putpixel((51, 50), color)
        #img.putpixel((51, 51), color)
        #img.putpixel((51, 52), color)
        #img.putpixel((52, 50), color)
        #img.putpixel((52, 51), color)
        #img.putpixel((52, 52), color)

        color = pattern_color

        for y in range(6, h-6, 8):
            for x in range(6, w-6, 8):
               # print("x is", x)
                #print("y is", y)
                p = image.getpixel((x,y))
                p = self.rgb_to_hex(p)
                #print(p)
                #print(hex_color)
                if p == hex_color:
                    image.putpixel((x,y), color)
                    image.putpixel((x+1,y), color)
                    image.putpixel((x + 2, y), color)
                    image.putpixel((x-1, y), color)
                    image.putpixel((x - 2, y), color)
                    image.putpixel((x,y+1), color)
                    image.putpixel((x, y + 2), color)
                    image.putpixel((x, y-1), color)
                    image.putpixel((x, y - 2), color)
        return image
        #image.save("./" + "testPlus.bmp")

    def make_lines(self, image, hex_color, line_color):

        w,h = image.size
        color = line_color

        for y in range(0,h,1):
            for x in range(0,w,6):
                p = image.getpixel((x, y))
                p = self.rgb_to_hex(p)
                #print(p)
                #print(hex_color)
                if p == hex_color:
                    image.putpixel((x,y), color)
        return image
        #image.save("./" + "testLines.bmp")

    def make_rect (self, image, hex_color, rect_color):

        w, h = image.size
        color = rect_color

        for y in range(6, h - 6, 8):
            for x in range(6, w - 6, 8):
                p = image.getpixel((x, y))
                p = self.rgb_to_hex(p)
                if p == hex_color:
                    image.putpixel((x-1, y-1), color)
                    image.putpixel((x, y-1), color)
                    image.putpixel((x+1, y-1), color)
                    image.putpixel((x+1, y), color)
                    image.putpixel((x+1, y+1), color)
                    image.putpixel((x, y+1), color)
                    image.putpixel((x-1, y-1), color)
                    image.putpixel((x-1, y), color)
                    image.putpixel((x-1, y-1), color)
        return image

    def process_image(self):
        """
        """
        img = open("./clown.bmp")  # !
        # print img.format, img.size, img.mode     # view image attributes
        gray_img = grayscale(img)
        gray_pixels = list(gray_img.getdata())
        gray_img.save("./" + "grey_img01.bmp")

        new_img_pixels = self.make_cartoon_pic(gray_pixels, self.color_palette)
        new_img = new("RGB", img.size)
        new_img.putdata(new_img_pixels)
        new_img = self.make_pattern(new_img, self.color_palette[2], (0,255,0))
        new_img = self.make_lines(new_img, self.color_palette[4], (0,255,255))
        new_img = self.make_rect(new_img, self.color_palette[1], (255,255,255))
        new_img.save("./"+"final_img.bmp")

        #for i in range(10):
            #print gray_pixels[i],
        #img = self.make_pattern(img, 'FFFF00')
        #img.save("./" + "testPlus.bmp") #FOR SOME REASON THIS DOESNT WORK... I NEED TO USE image.save() IN THE MAKE PATTERN FUNCTION
        #img = self.make_lines(img, '99FFFF')
        #img.save("./" + "testLines.bmp")
        #new_img_pixels = self.make_cartoon_pic(gray_pixels, self.color_palette)
        #w, h = img.size
        #print "img total pixels:", w * h
        #print "new_img total pixels:", len(new_img_pixels)
        #assert (w * h == len(new_img_pixels))


if __name__ == '__main__':  # run the program only if this is the code file we're working on
    cartoon = CartoonArt()
    cartoon.process_image()
    #cartoon.make_pattern()