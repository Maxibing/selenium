#coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()	#打开firefox
driver.maximize_window	#最大化浏览器窗口
driver.implicitly_wait(2)	#设置隐式时间等待

driver.get("https://www.baidu.com")	#地址栏输入百度地址
driver.find_element_by_xpath("//*[@id='kw']").send_keys("selenium")	#搜索输入框输入selenium
driver.find_element_by_xpath("//*[@id='su']").click()	#点击百度按钮

time.sleep(3)	#导入time模块，等待3秒

#这里通过xpath表达式来确定该元素是否显示在结果列表，从而判断Selenium官网这个链接是否显示在结果列表
#这里采用相对元素定位方法/../
#通过selenium方法is_displayed()来判断我们的目标是否在页面显示
driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a/em[text()='Selenium']").is_displayed()

#第二个判断方法
ele_string = driver.find_element_by_xpath("//div/h3/a[text()='官网']/../a").text
if ele_string == u"Selenium - Web Browser Automation":
	print("测试成功，结果和预期结果匹配")
time.sleep(5)
driver.quit()