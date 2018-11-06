# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/10/16
describle:
"""
# from selenium import webdriver
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get("https://business.yucunkeji.com/v2/detail?c1Name=%E5%85%AC%E5%BC%80%E5%B8%82%E5%9C%BA&id=5b20fe408ceac61365c97083&name=%E4%B8%8A%E5%B8%82%E5%85%AC%E5%8F%B8%E4%BF%A1%E6%81%AF")
# driver.find_element_by_id('username').send_keys("cse@socialcredits.cn")
# driver.find_element_by_id('password').send_keys("12345678")
# driver.find_element_by_class_name('src-components-login-loginForm-___index__submit').click()
# s = driver.find_elements_by_css_selector('.src-components-v2-apiListDetail-detail-file-___index__file-html>table')
# y = s[0].find_elements_by_css_selector('tr>th')
# print(y)

# if的使用
spam = 0
if spam <5:
    print('hello world')
    spam = spam + 1
spam1 = 1
# while的使用
while spam1 < 5:
    print('hello world1')
    spam1 = spam1 + 1



name = ''
while name != 'hamioo':
    print(u'请输入你的名字')
    name = input()
print('恭喜输入正确的名字')

# break的使用
while True:
    print(u'请输入你的名字')
    name = input()
    if name == "hamioo66":
        break
print(u'恭喜名字正确')

# continue的使用
while True:
    print('who are you?')
    name = input()
    if name != 'joe':
        continue
    print('Hello,joe,what is the password?(It is a fish)')
    password = input()
    if password == 'fish':
        break
print('Access granted')

# for循环和range()函数
# 让一个代码块执行固定次数
total = 0
for num in range(101):
    total = total + num
print(total)

print('my name is ')
i = 0
while i < 5:
    print('times('+str(i)+')')
    i = i + 1

for i in range(5):
    print('times('+str(i)+')')


# 用sys.exit()提前结束程序
import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you typed '+response+'.')