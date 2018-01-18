# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:
"""
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


# device = '8ac7d424' #此处设备号
# pack='com.yiyaotong.hurryfirewholesale' #此处是app的package名称
# activity='com.yiyaotong.hurryfirewholesale.ui.GuideActivity'#此处是app的主activity
#
# PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
# desired_caps = {}
# desired_caps['device'] = 'android'
# desired_caps['platformName'] = 'Android'
# desired_caps['browserName'] = ''
# desired_caps['Version'] = '4.4.4'
# desired_caps['deviceName'] = device
# desired_caps['appPackage'] = pack
# desired_caps['appActivity'] = activity
# desired_caps['unicodeKeyboard'] = True
# desired_caps['resetKeyboard'] = True
# desired_caps['utomationName'] = 'Uiautomator2'
# desired_caps['noReset'] = True

desired_caps = {
               'platformName': 'Android',
               'deviceName': '8ac7d424',
               # 'deviceName': 'PBV7N16C20000414',
               'platformVersion': '4.4.4',
               'appPackage': 'com.yiyaotong.hurryfirewholesale',
               'appActivity': 'com.yiyaotong.hurryfirewholesale.ui.GuideActivity',
               'noReset': 'true',
               'automationName': 'Uiautomator2'
               }


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # 等主页面activity出现
# driver.wait_activity(".base.ui.MainActivity", 10)

def find_toast(message):
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(toast_loc))
        return True
    except:
        return False
if __name__ == "__main__":
    driver.find_element_by_name(u'我的').click()
    driver.find_element_by_id("tv_login").click()
    # a = find_toast(u"请输入正确的账号")
    # print a
    toast_loc = ("xpath", ".//*[contains(@text,'请输入正确的账号')]")
    t = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located(toast_loc))
    print t


