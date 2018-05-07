#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get("https://www.baidu.com")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@name='memberPass']")	#点击checkbox
time.sleep(1)
driver.find_element_by_xpath("//*[@name='memberPass']")	#再次点击chenckbox

'''
附上几个元素的代码：
第一个click：
<div id="u1"><a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a>
			<a href="http://www.hao123.com" name="tj_trhao123" class="mnav">hao123</a>
			<a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a>
			<a href="http://v.baidu.com" name="tj_trvideo" class="mnav">视频</a>
			<a href="http://tieba.baidu.com" name="tj_trtieba" class="mnav">贴吧</a>
			<a href="http://xueshu.baidu.com" name="tj_trxueshu" class="mnav">学术</a>
			<a href="https://passport.baidu.com/v2/?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2F&amp;sms=5" name="tj_login" class="lb" onclick="return false;" style="">登录</a>
			<a href="http://www.baidu.com/gaoji/preferences.html" name="tj_settingicon" class="pf">设置</a>
			<a href="http://www.baidu.com/more/" name="tj_briicon" class="bri" style="display: block;">更多产品</a>
</div>
第二个click：
<p class="tang-pass-footerBarULogin pass-link" title="用户名登录" data-type="normal" id="TANGRAM__PSP_10__footerULoginBtn" style="">用户名登录</p>
第三和第四个click：
<input id="TANGRAM__PSP_10__memberPass" name="memberPass" class="pass-checkbox-input pass-checkbox-memberPass" checked="checked" type="checkbox">
'''