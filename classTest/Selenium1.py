# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
print "浏览器最大化",driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
time.sleep(3)

driver.set_window_size(480,800)
time.sleep(3)

first_url="http://www.baidu.com"
print "new access %s" %(first_url)
driver.get(first_url)
time.sleep(2)

second_url="http://news.baidu.com"
print "now access  %s" %(second_url)
driver.get(second_url)
time.sleep(2)
print "back to %s"%(first_url)
driver.back()
time.sleep(1)

print "forward  to %s" %(second_url)
driver.forward()
time.sleep(2)







driver.quit()