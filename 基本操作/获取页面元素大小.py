#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)
serch_button = driver.find_element_by_id("su")	#选中百度一下
print(serch_button.size)	#打印大小

'''
附上百度一下的代码
<input id="su" value="百度一下" class="bg s_btn" type="submit">
'''