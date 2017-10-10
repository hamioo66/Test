# -*- coding=UTF-8 -*-
#生成HTMLTestRunner测试报告
from selenium import webdriver
import unittest,time
import HTMLTestRunner #生成HTMl测试报告库
class Baidu(unittest.TestSuite):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url="http:/www.baidu.com/"
        self.verificationErrors=[]
    #百度搜索用例
    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
if __name__=="__main__":
    #测试套件
    testunit=unittest.TestSuite()
    #添加测试用例到测试套件中
    testunit.addTest(Baidu("test_baidu_search"))
    #定义个报告存放路径
    filename='E;\\test_object\\report\\result.html'
    fp=file(filename,'wb')
    #定义测试报告
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"百度搜索测试报告",
        description=u"用例执行情况" )
    #运行测试用例
    runner.run(testunit)
    #关闭报告文件
    fp.close()
