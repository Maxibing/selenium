#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")

try:
	driver.find_element_by_id("kw")
	print("test id is found")
except Exception as e:
	print("Exception found", format(e))
	