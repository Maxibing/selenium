#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://news.baidu.com")
time.sleep(1)
eles = driver.find_elements_by_xpath("//*/input[@type='radio']")	#find_elements_by***找一组元素，返回的是一个列表
for ele in eles:	#循环这个列表，点击所有的单选按钮
	ele.click()