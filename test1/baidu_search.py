#coding=utf-8
from selenium import webdriver
import time

class BaiduSearch(object):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(8)

    def open_baidu(self):
        self.driver.get("https://www.baidu.com")
        time.sleep(1)

    def test_search(self, text):
        self.text = text
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys(self.text)
        time.sleep(1)
        print(self.driver.title)

        try:
            assert text in self.driver.title
            print("Test pass")
        except Exception as e:
            print("Test fail", format(e))
        #self.driver.quit()

instance = Baidusearch()
instance.open_baidu()
instance.test_search("天气")