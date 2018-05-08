#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.baidu.com")

driver.execute_script("window.alert('alert:测试');")
time.sleep(2)
driver.switch_to_alert().accept()	#点击弹出里面的确定按钮
#driver.switch_to_alert().dismiss()
#driver.switch_to_alert().text

'''
a.accept()   相当于点击确定，或者使用
a.dismiss()  相当于点击取消，或者使用
a.text       获取弹出框里的文字
'''