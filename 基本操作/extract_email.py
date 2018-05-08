#coding=utf-8
from selenium import webdriver
import re
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("http://home.baidu.com/contact.html")

time.sleep(3)
doc = driver.page_source	#获得页面源码

emails = re.findall(r"\w+@\w+.\w+", doc)	#利用正则表达式，找出xxx@xxx.xxx的字段，保存到emails

for email in emails:	#循环打印email
	print(email)


