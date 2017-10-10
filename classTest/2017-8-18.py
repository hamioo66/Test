#coding=utf-8
#登录126邮箱，发送邮件
from selenium import webdriver
import time
driver=webdriver.Firefox()
driver.implicitly_wait(20)
driver.get(r'http://www.126.com/')
time.sleep(3)
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').send_keys('zhm200701@126.com')
driver.find_element_by_name('password').send_keys('zhm811426')
time.sleep(3)
driver.find_element_by_id('un-login').click()
driver.find_element_by_id('dologin').click()
time.sleep(3)
driver.switch_to.default_content()
driver.find_element_by_xpath("//span[contains(text(),'写 信')]").click()
driver.find_element_by_class_name('nui-editableAddr-ipt').send_keys('86263137@qq.com')
driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @maxlength='256']").send_keys(u"测试发送邮件")
driver.switch_to_frame(driver.find_element_by_id('APP-editor-iframe'))
emailcontext=driver.find_element_by_class_name('nui-scroll')
emailcontext.send_keys(u'测试内容测试内容测试内容测试内容测试内容')
driver.switch_to.default_content()
time.sleep(3)
sendemails=driver.find_element_by_xpath("//span[contain(text(),'发送') and @class='nui-btn-text']")
time.sleep(3)
try:
    assert '发送成功' in driver.page_source
except AssertionError:
    print '邮件发送成功'
else:
    print '邮件发送失败'
