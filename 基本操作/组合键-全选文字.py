#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)
driver.get("https://www.baidu.com")

element = driver.find_element_by_tag_name("body")	#选中tag name为body的元素
element.send_keys(Keys.CONTROL + 'a')	#全选