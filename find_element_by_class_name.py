#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_class_name("s_ipt")
	print("Test pass: element found by class name")
except Exception as e:
	print("Test error", format(e))

time.sleep(5)
driver.quit()

'''
通过元素节点中class name的值来定位页面元素，页面代码如下
<input class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off" type="text">
'''