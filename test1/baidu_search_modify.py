#coding=utf-8
from selenium import webdriver
from basepage import BasePage
import time

class BaiduSearch(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(8)
    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url('https://www.baidu.com')
        time.sleep(1)

    def test_search(self, text):
        self.text = text
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys(self.text)
        time.sleep(1)
        self.basepage.forward()
        self.basepage.back()
        self.basepage.quit_browser()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search("天气")