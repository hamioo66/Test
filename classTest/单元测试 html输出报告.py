# -*- coding:UTF-8 -*-
import unittest
from HTMLTestRunner import HTMLTestRunner
class ExampleCase(unittest.TestCase):
    def setUp(self):
        self.a=4
        self.b=3
    def test_add(self):
        self.assertEqual(self.a+self.b,7)
    def test_minus(self):
        print ''
        self.assertEqual(self.a-self.b,2)

class ExampleCase2(unittest.TestCase):
    def setUp(self):
        self.a,self.b=4,3
    def test_plus(self):
        self.assertEqual(self.a * self.b,c)
class ExampleCase3(unittest.TestCase):
    def setUp(self):
        self.a,self.b=4,2
    def test_devide(self):
        self.assertEqual(self.a / self.b,2)
if __name__=="__main__":
    report_title=u"Example用例执行报告"
    desc=u"用户展示修改样式后的HTMLTestRunner"
    report_file='d:\\ExampleReport.html'
    testsuite=unittest.TestSuite()
    testsuite.addTest(ExampleCase("test_add"))
    testsuite.addTest(ExampleCase("test_minus"))
    testsuite.addTest(ExampleCase2("test_plus"))
    testsuite.addTest(ExampleCase3("test_devide"))
    with open(report_file,'wb') as report:
        runner=HTMLTestRunner(stream=report,title=report_title,description=desc)
        runner.run(testsuite)