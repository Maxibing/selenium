#coding=utf-8
from selenium import webdriver
import os
import time

from test1.logger import Logger 

mylog = Logger(logger='BasePage').getlog()  


class BasePage(object):
    '''
    把selenium中常用的几个方法封装起来
    back()
    forward()
    get()
    quit()
    '''
    def __init__(self,driver):
        '''
        写一个构造函数，有一个参数driver
        :param driver:
        '''
        self.driver = driver

    def back(self):
        '''
        浏览区后退操作
        :return:
        '''
        self.driver.back()

    def forward(self):
        '''
        浏览器前进操作
        :return:
        '''
        self.driver.forward()

    def open_url(self,url):
        '''
        打开url站点
        :return:
        '''
        self.driver.get(url)

    def quit_browser(self):
        '''
        关闭并停止浏览器服务
        :return:
        '''
        self.driver.quit()
		
    def screenshot(self):
        '''
		截图并保存到Screenshots文件夹下
		'''
        file_path = os.path.dirname(os.getcwd()) + '\Screenshots\\'
        rq = time.strftime('%Y-%m-%d %H:%M:%S')
        screen_name = file_path + rq + '.png'
        print(screen_name)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            mylog.info("开始截图并保存")
        except Exception as e:
            mylog.error("出现异常", format(e))