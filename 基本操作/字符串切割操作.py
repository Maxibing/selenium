# coding=utf-8
from selenium import webdriver
import time


class GetSubString(object):

    def get_search_result(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        driver.find_element_by_xpath("//*[@id='kw']").send_keys("天气")
        time.sleep(1)
        search_result_string = driver.find_element_by_xpath("//*/div[@class='nums']").text
        print(search_result_string)

        new_string = search_result_string.split('约')[1] #第一次切割得到约后面的字符串
        print(new_string)
        last_string = new_string.split('个')[0]  #第二次切割得到个前面的字符串
        print(last_string)


getstring = GetSubString()
getstring.get_search_result()