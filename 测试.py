#-*- coding:utf-8 -*-
import os
import random
from appium import webdriver
import time
import logging as log
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import MySQLdb

from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://123.206.57.62:7000/ ")
browser.maximize_window()
browser.find_element_by_xpath('//FORM[@id="formID"]/P[1]/INPUT[1]').send_keys("18888888888")
browser.find_element_by_xpath('//FORM[@id="formID"]/P[2]/INPUT[1]').send_keys("123456")
browser.find_element_by_xpath('//FORM[@id="formID"]/P[3]/INPUT[1]').click()
username = browser.find_element_by_class_name("userListBox").text
quanxian = browser.find_elements_by_tag_name("span")
username1 = quanxian[0].text              #获取单独的协会角色名称
print u"登录信息：" + username + u"  "+ quanxian[1].text
browser.find_element_by_xpath('//DIV[@id="accordion"]/UL[1]/LI[8]/DIV[1]').click()
time.sleep(1)
r = browser.find_elements_by_class_name("submenu")
browser.find_element_by_link_text("资讯分类").click()
time.sleep(1)
y = browser.find_elements_by_tag_name('iframe')
browser.switch_to_frame(y[1])
fenye = browser.find_elements_by_css_selector("[aria-controls='example']")
print len(fenye) - 4
fenleititle = browser.find_elements_by_class_name("odd")
i=[]
a=0
b=0
tr=browser.find_elements_by_tag_name('tr')
for j in  tr:
    td=browser.find_elements_by_tag_name('td')
    a=+a
    for k in td:
        value=i.append(k.text)
        b=+b
        print i[a][b]
print i[1][2]
