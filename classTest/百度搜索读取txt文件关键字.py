# -*- coding=UTF-8 -*-
#验证数据驱动

from selenium import webdriver
import time
file_info=open('info.txt','r')
values=file_info.readlines()
print values
file_info.close()

for search in values:
    driver=webdriver.Firefox()
    time.sleep(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.quit()
