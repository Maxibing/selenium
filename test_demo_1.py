#coding=utf-8
from selenium import webdriver
import os
import time

# set little time stop and big time stop for viewing changes
little_time_stop = 1
big_time_stop =2
#默认广告数
ads_num_require = 20
#请求连接
req_url = "http://www.haosou.com/s?ie=utf-8&shb=1&src=360sou_newhome&q=%E9%B2%9C%E8%8A%B1"

#打开浏览器
browser = webdriver.Chrome()
#开始请求
browser.get(req_url)
#获取所有广告
all_ads_li = browser.find_elements_by_css_selector("#e_idea_pp li")
#当前广告数
ads_num_current = len(all_ads_li)
print("Has been got %d ads" % (ads_num_current))

#如果广告数与默认数不符
if ads_num_current < ads_num_require:
    print("The number of ads is not enough ( current : %d require: %d)" %(ads_num_current,ads_num_require))
    #exit()
#获取顶部链接
i = 0
for ads_li in all_ads_li:
    time.sleep(big_time_stop)
    i = i+1
    print("ads %d :" % i)
    try:
        mains = ads_li.find_elements_by_css_selector('h3 a')
    except:
        print("\  : ads %d cann't find" % i)
    else:
        k = 0
        for main in mains:
            k = k+1
            print("\tReady: visit ads %d" % k)
            main.click
            print("\tSuccess: visit ads %d" % k)
            time.sleep(little_time_stop)
    try:
        img_links = ads_li.find_elements_by_class_name('e_biyi_img')
    except:
        print("\tError : no img in ads %d" % i)
    else:
        h = 0
        for img_link in img_links:
            h = h+1
            print("\tReady : visit img_link %d" % i)
            img_link.click()
            print("\tSuccess : visit img_link %d" % i)
            time.sleep(little_time_stop)
    try:
        child_div = ads_li.find_elements_by_class_name('e_biyi_childLink')
    except:
        print("\tError : no child link in ads %d" % i)
    else:
        try:
            child_links = child_div.find_elements_by_css_selector('a')
        except:
            print("\tError : find child_link error")
        else:
            num_links = len(child_link)
            print("\t Success : there are %d child_link" % num_links)
            j = 0
            for child_link in child_links:
                j = j+1
                print("\t\tReady : visit child link %d in ads %d" %(j, i))
                child_link.click()
                print("\t\tSuccess : visit child link %d in ads %d" %(j, i))
                time.sleep(little_time_stop)
print("End and thanks for your using!")