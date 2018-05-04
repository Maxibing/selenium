#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

ele_news = driver.find_element_by_link_text("新闻")
ele_news.click()	#点击进入百度新闻
time.sleep(2)
driver.back()	#返回上一个页面（百度首页）
time.sleep(2)
driver.forward()	#前进到下一个页面（百度新闻）
time.sleep(2)

driver.quit()

'''
利用webdriver中的方法，实现前进和后退
'''