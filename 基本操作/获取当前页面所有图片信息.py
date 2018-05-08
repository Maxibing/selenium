#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://news.baidu.com")
time.sleep(1)

for image in driver.find_elements_by_css_selector(".item-image"):
	print(image.text)
	print(image.size)
	print(image.tag_name)