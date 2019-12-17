from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = '1847213'
passwordStr = '43501042'

browser = webdriver.Chrome()
browser.get(('http://192.168.100.100:8090/'))

# fill in username and hit the next button
username = browser.find_element_by_id('username')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('password')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "password")))
password.send_keys(passwordStr)

signInButton = browser.find_element_by_id('loginbutton')
signInButton.click()