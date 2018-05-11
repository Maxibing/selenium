#coding=utf-8
from selenium import webdriver
import unittest
import time


class BaiduSearch(unittest.TestCase):

    def setUp(self):
        '''
        测试固件的setUp()的代码，测试前准备工作
        :return:
        '''
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://www.baidu.com")
        time.sleep(1)

    def tearDown(self):
        '''
        测试结束后，回收测试资源
        :return:
        '''
        time.sleep(2)
        self.driver.quit()

    def test_baidu_search(self):
        '''
        这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里
        :return:
        '''
        self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气")
        time.sleep(1)
        try:
            assert "天气" in self.driver.title
            print("Test pass")
        except Exception as e:
            print("Test fail", format(e))

        if __name__ == '__main__': #添加这个，是支持在cmd中，可以使用python 脚本.py执行
            unittest.main()
