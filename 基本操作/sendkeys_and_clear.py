#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("Selenium")	#调用send_keys()
time.sleep(3)

try:
	driver.find_element_by_xpath("//*[@id='kw']").clear()	#调用clear()
	print("Test pass: clean successful")
except Exception as e:
	print("Test error", format(e))
