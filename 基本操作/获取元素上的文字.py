#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(1)
driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
#方法一
try:
	driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error' and text()='请您输入手机/邮箱/用户名']").is_displayed()
	print("Test pass, error message is displayed.")
except Exception as e:
	print("Test fail", format(e))
#方法二，推荐使用
err_msg = driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__error']").text	#获取元素上的文字
try:
	assert err_msg == "请您输入手机/邮箱/用户名"
	print("Test pass, error message is right.")
except Exception as e:
	print("Test fail", format(e))