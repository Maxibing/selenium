#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)

driver.get_screenshot_as_file("D://baidu.png")	#get_screenshot_as_file方法截图并保存，路径要用//
driver.quit()
