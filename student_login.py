from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import urllib.request
import requests
import time

usernameStr = '1847213'
passwordStr = '43501042'
browser = webdriver.Chrome()
browser.get(('https://kp.christuniversity.in/KnowledgePro/StudentLogin.do'))

def downloadcaptcha():
    images = browser.find_elements_by_id('captcha_img')
    lst = []
    for image in images:
        lst.append(image.get_attribute('src'))
    src = lst[-1]
    filename = "sample.png"
    time.sleep(1)
    r = requests.get(src, allow_redirects=True)
    down_path = ''+filename
    open(down_path, 'wb').write(r.content)
    column = Image.open("sample.png")

    # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    # text = pytesseract.image_to_string(im, lang = 'eng')
    # print(text)

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
    if (text1 == 'l'):
        text1 = '1'
    elif(text2 == 'l'):
        text2 = '1'
    elif(text3 == 'l'):
        text3 = '1'
    elif(text4 == 'l'):
        text4 = '1'
    elif(text5 == 'l'):
        text5 = '1'
    elif(text6 == 'l'):
        text6 = '1'

    if (text1 == 'r'):
        text1 = 'f'
    elif(text2 == 'r'):
        text2 = 'f'
    elif(text3 == 'r'):
        text3 = 'f'
    elif(text4 == 'r'):
        text4 = 'f'
    elif(text5 == 'r'):
        text5 = 'f'
    elif(text6 == 'r'):
        text6 = 'f'

    text = text1+text2+text3+text4+text5+text6
    return text

# fill in username and hit the next button
username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('password')
nextButton.click()

# wait for transition then continue to fill items
password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys(passwordStr)

gotocaptcha = browser.find_element_by_id('captchaBox')
gotocaptcha.click()

captcha = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "enteredCaptcha")))
captchaStr = downloadcaptcha()
captcha.send_keys(captchaStr)

signInButton = browser.find_element_by_id('Login')
signInButton.click()