from selenium import webdriver 
import time

request_url = input("Please enter the url:")	#获取url

driver = webdriver.Chrome()		#初始化浏览器

driver.maximize_window()		#浏览器最大化

time.sleep(5) 		#延迟

driver.get(request_url)		#跳转输入url