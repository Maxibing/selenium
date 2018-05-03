#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

try:
	driver.find_element_by_tag_name("form")
	print("Test pass: tag name found")
except Exception as e:
	print("Test error", format(e))

driver.quit()

'''
此处是百度首页输入框，包括tag name为"form"的代码
<form name="f" id="form" action="/s" class="fm" onsubmit="javascript:F.call('ps/sug','pssubmit');">
<span id="s_kw_wrap" class="bg s_ipt_wr quickdelete-wrap">
	<span class="soutu-btn"></span>
	<input class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off" type="text">
	......
'''