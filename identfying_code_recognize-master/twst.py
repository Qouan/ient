import cv2
import pyautogui as ctr
import time
from selenium import webdriver
import requests
import experiment3
from PIL import Image
url='https://zfw.xidian.edu.cn/'
userElementId='loginform-username'
passwordElementId='loginform-password'
verifyCodeId='loginform-verifycode'
verifyCodeFresh='loginform-verifycode-image'
submitButtonName='login-button'

userName='15020510006'
password='qouanmxx'
browser = webdriver.Chrome()
#browser.maximize_window()

browser.get(url)

time.sleep(2)
browser.find_element_by_id(userElementId).send_keys(userName)
browser.find_element_by_id(passwordElementId).send_keys(password)
element=browser.find_element_by_id(verifyCodeFresh)

while True:
    browser.get_screenshot_as_file('CrawlResult/screenshot.png')
    left = int(element.location['x'])
    top = int(element.location['y'])
    print(left,top)
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])
    im = Image.open('CrawlResult/screenshot.png')
    im = im.crop((left, top, right, bottom))
    im.save('CrawlResult/code.png')

    res=experiment3.recognize()

    verification=browser.find_element_by_id(verifyCodeId)
    verification.send_keys(res)

    browser.find_element_by_name(submitButtonName).click()
    time.sleep(2)
    print(browser.title)
    if(browser.title!='登录'):
        break;
    verification.clear()
    element.click()


