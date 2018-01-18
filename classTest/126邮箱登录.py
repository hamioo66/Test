# -*- coding=UTF-8 -*-
#验证数据驱动
from selenium import webdriver

driver=webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.126.com")
#初始化参数
class Account(object):
    """docstring for account"""
    def __init__(self,username='', password=''):
        self.username = username
        self.password = password

    #登录方法
    def do_login_as(user_info):
        driver.find_element_by_id("loginBlock")
        driver.find_element_by_id('account-box').click()
        driver.find_element_by_css_selector("input[placeholder='邮箱帐号或手机号']").clear()
        driver.find_element_by_css_selector("input[placeholder='邮箱帐号或手机号']").send_keys(user_info.username)
        driver.find_element_by_css_selector("input[placeholder='密码']").clear()
        driver.find_element_by_css_selector("input[placeholder='密码']").send_keys(user_info.password)
        driver.find_element_by_id("dologin").click()


#实例化登录信息
admin = Account(username='zhm200701@126.com', password='zhm811426')

#调用登录函数
Account.do_login_as(admin)