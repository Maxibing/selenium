#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)
#执行js脚本触发一个alert弹出框
#driver.execute_script("window.alert('这是一个alert弹框。');")	#这里的分号是英文分号

#控制浏览器竖向滚动条
driver.find_element_by_xpath("//*[@id='u1']/a[5]").click()
time.sleep(3)
target_elem = driver.find_element_by_link_text("地区")
driver.execute_script("return arguments[0].scrollIntoView();", target_elem) #使用目标元素进行拖动
#driver.execute_script("scroll[0,2400]")	#这种方法是大概拖动，比较粗劣