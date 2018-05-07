#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()	#全屏
driver.get("http://www.baidu.com")
time.sleep(1)
print(driver.get_window_size())	#获取当窗口大小

driver.set_window_size(1280, 800)	#设置分辨率为1280*800
time.sleep(1)
print(driver.get_window_size())

driver.set_window_size(1024, 768)	#设置分辨率为1024*768
time.sleep(1)
print(driver.get_window_size())