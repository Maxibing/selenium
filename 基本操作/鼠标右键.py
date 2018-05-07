#coding=utf-8
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

element = driver.find_element_by_css_selector(".qrcode-img")
actionchains = ActionChains(driver)
#actionchains.context_click(element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
actionchains.context_click(element).send_keys('i').perform() 


'''
在Selenium中，有一个ActionChains模块支持，右键，鼠标悬停，拖拽，双击等动作。
我们可以通过键盘向下箭头来选择查看图像这个菜单，然后点击就可以达到目的。
'''