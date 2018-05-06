#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)
ele = driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')	#发送按键Ctrl + t
time.sleep(1)