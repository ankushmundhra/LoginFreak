
from PIL import Image
from PIL import ImageEnhance
#from pytesser import *
import pytesseract
#from pytesseract import pytesser
from pytesseract import image_to_string

im = Image.open("5.png")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
nx, ny = im.size
im2 = im.resize((int(nx*5), int(ny*5)), Image.BICUBIC)
im2.save("temp2.png")
enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
 
imgx = Image.open('temp2.png')
imgx = imgx.convert("RGBA")
pix = imgx.load()
for y in range(imgx.size[1]):
    for x in range(imgx.size[0]):
        if pix[x, y] != (0, 0, 0, 255):
            pix[x, y] = (255, 255, 255, 255)
imgx.save("bw.gif", "GIF")
original = Image.open('bw.gif')
bg = original.resize((116, 56), Image.NEAREST)
ext = ".tif"
bg.save("input-NEAREST" + ext)
image = Image.open('input-NEAREST.tif')
print (image_to_string(image))

"""
from PIL import Image
import json

image = Image.open("2.png").convert("L") # Grayscale conversion
pixel_matrix = image.load()

#box – a 4-tuple defining the left, upper, right, and lower pixel coordinate.
#cropping the image into 6 different parts as there are 6 characters
cropped_image = image.crop((6, 0, 28.5, 40))
cropped_image.save("cropped_image1.png")

cropped_image = image.crop((25, 0, 47.5, 40))
cropped_image.save("cropped_image2.png")

cropped_image = image.crop((45, 0, 67.5, 40))
cropped_image.save("cropped_image3.png")

cropped_image = image.crop((65, 0, 87.5, 40))
cropped_image.save("cropped_image4.png")

cropped_image = image.crop((88, 0, 110.5, 40))
cropped_image.save("cropped_image5.png")

cropped_image = image.crop((107.5, 0, 130, 40))
cropped_image.save("cropped_image6.png")

# thresholding
for column in range(0, image.height):
    for row in range(0, image.width):
        if pixel_matrix[row, column] != 0:
            pixel_matrix[row, column] = 255
"""

"""
from PIL import Image
from PIL import ImageOps
import pytesseract
import sys
import cv2
from random import randint
import numpy as np

column = Image.open("3.png")
img_with_border = ImageOps.expand(column,border=5,fill='white')
img_with_border.save('imaged-with-border.png')
gray = img_with_border.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save("code_bw.jpg")

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text = pytesseract.image_to_string("code_bw.jpg", lang = 'eng')
print(text)

"""