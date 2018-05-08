#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://news.baidu.com")
time.sleep(4)

news_link = driver.find_element_by_xpath("//*[@id='pane-news']/div/ul/li[1]/strong/a")
page1_news_string = news_link.text	#得到页面1的新闻的标题
news_link.click()
time.sleep(1)
print(driver.current_window_handle)	#当前窗口的句柄
handles =driver.window_handles	#获取全部窗口的句柄
print(handles)	#输出句柄集合

for handle in  handles:	#该循环用于切换窗口
	if handle != driver.current_window_handle:
		print("Switch to second window")
		driver.close()	#关闭第一个窗口
		driver.switch_to_window(handle)	#切换到第二个窗口
	
page2_news_string = driver.find_element_by_css_selector("div.h-title").text	#得到页面2的新闻的标题

try:
	assert page1_news_string == page2_news_string	#断言页面1的标题和页面2的标题是否相同
	print("Test pass")
except Exception as e:
	print("Test fail", format(e))