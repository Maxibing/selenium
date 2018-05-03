#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_css_selector("#su")
	print("Test pass: element found by css selector")
except Exception as e:
	print("Test error", format())

driver.quit()

'''
一定要掌握好XPath或者css来定位元素，其他的几种了解就可以。
毕竟在实际项目开发脚本阶段，很多元素是无法通过id ,css, text, name来直接定位这个网页元素，更多的还是根据XPath或者css表达式去定位。
通过css selector查找百度一下，元素代码如下
<input value="百度一下" id="su" class="btn self-btn bg s_btn" type="submit">
'''