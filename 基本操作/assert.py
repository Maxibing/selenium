#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://www.baidu.com")
time.sleep(1)

try:
	assert u"百度一下，你就知道" in driver.title	#断言判断。此处u是unicode
	print("Asserttion test pass")
except Exception as e:
	print("Assertion test error", fromat(e))