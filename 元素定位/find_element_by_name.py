#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_name("wd")
	print("Test pass: element found by name")
except Exception as e:
	print("Test error", format(e))

driver.minimize_window()
driver.quit()

'''
name这个属性不是所有的节点都有，如果有建议采用name的值来定位，就和by_id, by_class一样的效果。
'''