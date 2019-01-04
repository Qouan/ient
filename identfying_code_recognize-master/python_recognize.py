from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get('https://zfw.xidian.edu.cn/')
print(browser.title)
