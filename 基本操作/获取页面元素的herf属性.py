#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://news.baidu.com")
time.sleep(1)

for link in driver.find_elements_by_xpath("//*[@href]"):
	print(link.get_attribute('href'))	#打印所有herf的属性
driver.quit()

'''
如果需要其他元素的属性，也可以用这种方法
'''