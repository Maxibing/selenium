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

driver.quit()

'''
此处是百度首页输入框的代码
<input class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off" type="text">
'''