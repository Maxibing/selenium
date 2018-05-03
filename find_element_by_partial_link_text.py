#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_partial_link_text("推广").click()
	print("Test pass: element found by partial link text")
except Exception as e:
	print("Test error", format(e))

time.sleep(50
driver.quit()

'''
partial link text就是选取这个元素link text中一部分字段
'''