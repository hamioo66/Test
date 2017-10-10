# -*- coding: UTF-8 -*-
import os
from appium import webdriver
import time


device='8ac7d424' #此处设备号
pack='com.yst.puhuimember' #此处是app的package名称
activity='com.yst.puhuimember.MainActivity'#此处是app的主activity

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'
desired_caps['browserName']=''
desired_caps['Version']='4.4.4'
desired_caps['deviceName']=device
#desired_caps['app']=PATH('D:\\jr.apk')
desired_caps['appPackage'] = pack
desired_caps['appActivity'] = activity
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)


wode = 'bt_my'
el = driver.find_element_by_id(wode)
el.click()   #点击我的
driver.implicitly_wait(10)
check1 = driver.find_element_by_id('tv_phone').text  #获取登录状态
if check1 == (u"登录/注册"):
    driver.find_element_by_id("tv_phone").click()    #点击注册
    driver.find_element_by_id('et_id').send_keys("15599155289")
    driver.find_element_by_id('et_password').send_keys("zhm811426")
    driver.find_element_by_id('bt_login').click()
    print(u"登录成功")
else:
    driver.find_element_by_id('bt_setting').click()
    driver.find_element_by_id('exit_login').click()
    driver.find_element_by_id('sure').click()
    #driver.find_element_by_id("tv_phone").click()    #点击注册
    driver.find_element_by_id('et_id').send_keys("15599155289")
    driver.find_element_by_id('et_password').send_keys("zhm811426")
    driver.find_element_by_id('bt_login').click()
    print(u"重新登录成功")

driver.find_element_by_id("bt_my").click()
driver.find_element_by_id('layout3').click()
s = driver.find_elements_by_id("layout_nocard")
if len(s) == 0:
    print("该用户已绑卡，正在执行清空绑卡操作...")
    driver.find_element_by_id("delete_crad").click()
    driver.find_element_by_id("sure").click()
    print("已清空用户绑卡信息")
    print("正在重新绑卡...")
    driver.find_element_by_id("bind_card").click()
    checkmember = driver.find_element_by_id("tv_name").text
    #s=checkmember.decode('utf-8').encode('gb18030')
   # print "当前用户为：" %s
    print (checkmember)
    driver.find_element_by_id('edit_bankcard').send_keys("6222022402014228130")
    checkbankname = driver.find_element_by_id("edit_bankname").text
    print (checkbankname)
    if checkbankname == (u"工商银行·银联IC普卡"):
        driver.find_element_by_id("bind_card").click()
        print("已重新绑定银行卡")
    else:
        print("银行卡所属银行获取错误")
if len(s) == 1:   #判断当前用户是否绑定银行卡
    print("该用户未绑卡，正在执行绑卡操作")
    driver.implicitly_wait(10)
    driver.find_element_by_id("bind_card").click()
    checkmember = driver.find_element_by_id("tv_name").text
    print "当前用户为%s" %checkmember
    print ()
    driver.find_element_by_id('edit_bankcard').send_keys("6222022402014228130")
    checkbankname = driver.find_element_by_id("edit_bankname").text
    print (checkbankname)
    if checkbankname == (u"工商银行·银联IC普卡"):
        driver.find_element_by_id("bind_card").click()
        print("绑卡已成功")
    else:
        print("银行卡所属银行获取错误")

