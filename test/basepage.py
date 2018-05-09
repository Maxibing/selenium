#coding=utf-8
from selenium import webdriver

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

    def forwad(self):
        '''
        浏览器前进操作
        :return:
        '''
        self.driver.forwad()

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