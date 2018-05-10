#coding=utf-8
import time

class GetTime(object):

    def get_system_time(self):
        print(time.time())  #time.time()方法获得的是1970年到现在的时间间隔，单位是秒
        print(time.localtime())
        format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #格式化时间，按照 2018-05-10 13:31:25的格式打印出来
        print(format_time)
        new_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
        print(new_time)


current_time = GetTime()
current_time.get_system_time()
