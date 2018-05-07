#coding=utf-8
from seleniu import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("http://news.baidu.com")
time.sleep(1)

try:
	driver.find_element_by_xpath("//*[@id='news']").is_selected()	#判断元素是否被选中
	print("Test pass")
except Exception as e:
	print("Test fail", format(e))
