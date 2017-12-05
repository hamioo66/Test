# coding: utf-8
import unittest
import time
from selenium import webdriver
import HTMLTestRunner
from util.log import Logger
class Web_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Chrome()
        cls.browser.maximize_window()
        cls.base_url = 'http://123.206.57.62:17000/login'
        cls.browser.get(cls.base_url)

    def login_index(self,login_index,username,password):
        # 登录方法：1管理员2批发商3代理商
        browser = self.browser
        browser.find_element_by_css_selector('[class="selectpicker validate[required]"]').click()
        a = browser.find_elements_by_tag_name("option")
        a[login_index - 1].click()
        time.sleep(1)
        browser.find_element_by_css_selector('[name="telphone"]').clear()
        browser.find_element_by_css_selector('[name="telphone"]').send_keys(username)
        browser.find_element_by_css_selector('[name="password"]').clear()
        browser.find_element_by_css_selector('[name="password"]').send_keys(password)
        time.sleep(1)
        browser.find_element_by_class_name("loginBtn").click()
        time.sleep(1)
        b = browser.find_elements_by_class_name("userListBox")
        if len(b) != 0:
            loginname = browser.find_element_by_class_name("userListBox").text
            quanxian1 = browser.find_elements_by_tag_name("span")
            quanxian = quanxian1[1].text
            # logg(u"登录信息：" + loginname + u"  " + quanxian)
    def test_1(self):
        '用户名为空，登录'
        browser = self.browser
        self.login_index(1,'','123456')
        title = browser.title
        self.assertEqual(u"集鲜丰后台登录",title)
    def test_2(self):
        '密码为空，登录'
        browser = self.browser
        self.login_index(1,'18888888888','')
        title = browser.title
        self.assertEqual(u"集鲜丰后台登录",title)
    def test_3(self):
        '错误的用户名，登录'
        browser = self.browser
        self.login_index(1,'18888888884','123456')
        title = browser.title
        self.assertEqual(u"集鲜丰后台登录",title)
    def test_4(self):
        '错误的密码，登录'
        browser = self.browser
        self.login_index(1, '18888888888', '123459')
        title = browser.title
        self.assertEqual(u"集鲜丰后台登录", title)
    def test_5(self):
        '正确的用户名和密码，登录'
        browser = self.browser
        self.login_index(1, '18888888888', '123456')
        title = browser.title
        self.assertEqual(u"集鲜丰后台管理系统", title)
    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Web_login("test_1"))
    suite.addTest(Web_login("test_2"))
    suite.addTest(Web_login("test_3"))
    suite.addTest(Web_login("test_4"))
    suite.addTest(Web_login("test_5"))
    fp = open("result.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'集鲜丰自动化测试报告',description=u'测试结果：',tester=u'易耀通技术部测试组')
    runner.run(suite)
    fp.close()
