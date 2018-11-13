# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/13
describle:火狐无界面浏览的使用
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Google无界面浏览器
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver1 = webdriver.Chrome(executable_path='../classTest/driver/chromedriver.exe',chrome_options=chrome_options)
# driver1.get("https://www.baidu.com")
# print(driver1.page_source)
# driver1.close()

# 火狐无界面浏览器
options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(firefox_options=options)
"""selenium已经放弃PhantomJS，建议使用火狐或谷歌无界面浏览器"""
#driver = webdriver.PhantomJS(executable_path=r'E:\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://www.lottery.gov.cn/')
#driver.implicitly_wait(5)
a = driver.find_element_by_id('kj_1')
b = driver.find_element_by_id('index_plw_term')
print(a)
print(b)