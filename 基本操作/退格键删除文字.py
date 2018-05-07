#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

drvier = webdriver.Firefox()
drvier.maximize_window()
drvier.implicitly_wait(8)
drvier.get("https:www.baidu.com")

element = drvier.find_element_by_id('kw')	#搜索框
time.sleep(1)
element.send_keys('Vincent')	#搜索框中输入蚊子
time.sleep(1)
element.send_keys(Keys.CONTROL + 'a')	#全选蚊子
element.send_keys(Keys.BACKSPACE)	#退格键删除
