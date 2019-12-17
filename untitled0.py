from PIL import Image
from PIL import ImageOps
import pytesseract
import sys
import cv2
from random import randint
import numpy as np

column = Image.open("5.png")
gray = column.convert('L')
im = gray.resize((900,300), Image.ANTIALIAS)
blackwhite = im.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save("code_bw.jpg")

#box – a 4-tuple defining the left, upper, right, and lower pixel coordinate.
cropped_image1 = blackwhite.crop((0, 0, 200, 300))
cropped_image1.save("cropped1.jpg")

cropped_image2 = blackwhite.crop((180, 0, 320, 300))
cropped_image2.save("cropped2.jpg")

cropped_image3 = blackwhite.crop((300, 0, 460, 300))
cropped_image3.save("cropped3.jpg")

cropped_image4 = blackwhite.crop((440, 0, 610, 300))
cropped_image4.save("cropped4.jpg")

cropped_image5 = blackwhite.crop((570, 0, 740, 300))
cropped_image5.save("cropped5.jpg")

cropped_image6 = blackwhite.crop((700, 0, 880, 300))
cropped_image6.save("cropped6.jpg")


"""
blackwhite = column.resize((900,300), Image.ANTIALIAS)
img_with_border = ImageOps.expand(blackwhite,border=15,fill='white')
#img_with_border.save("code_bw.jpg")
#img.save('sompic.jpg') 
"""

"""
img_with_border = ImageOps.expand(column,border=5,fill='white')
img_with_border.save('imaged-with-border.png')
gray = img_with_border.convert('L')
blackwhite = gray.point(lambda x: 0 if x < 200 else 255, '1')
blackwhite.save("code_bw.jpg")
"""

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
text1 = pytesseract.image_to_string("cropped1.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")
text2 = pytesseract.image_to_string("cropped2.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")
text3 = pytesseract.image_to_string("cropped3.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")
text4 = pytesseract.image_to_string("cropped4.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")
text5 = pytesseract.image_to_string("cropped5.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")                                                                                                                                                                                                       
text6 = pytesseract.image_to_string("cropped6.jpg", config="-c tessedit"
                                             "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                                             " --psm 10"
                                             " -l osd"
                                             " ")

#text = pytesseract.image_to_string("code_bw.jpg", lang = 'eng')
text = text1+text2+text3+text4+text5+text6
print(text)