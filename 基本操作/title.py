#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)
driver.find_element_by_link_text("新闻").click()
time.sleep(1)
print(driver.title) #title方法可以获取当前页面的标题显示的字段
driver.quit()