#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)
print(driver.capabilities['version'])	# 打印浏览器version的值
driver.quit()

'''
通过capabilities方法，打印version的值
'''