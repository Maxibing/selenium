#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.refresh()	#刷新方法refresh
	print("Test pass: refresh successful")
except Exception as e:
	print("Test error", format(e))
driver.quit()

'''
利用webdriver中的方法，实现页面刷新
'''