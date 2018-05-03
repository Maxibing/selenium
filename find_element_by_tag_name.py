#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https:www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_tag_name("form")
	print("Test pass: tag name found")
except Exception as e:
	print("Test error", format(e))

driver.quit()