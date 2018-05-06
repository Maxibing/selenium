#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element_by_link_text("新闻").click()
time.sleep(2)
print(driver.current_url)	#current_url这个方法可以获取当前页面的url
driver.quit()

'''
一般URL可以帮助我们判断跳转的页面是否正确，或者URL中部分字段可以作为我们自动化测试脚本期待结果的一部分
'''