# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:
"""
import count
import unittest
class Test(unittest.TestCase):
    def setUp(self):
        # number = input(u"输入一个数字")
        # self.number = number
        pass

    # def test_case(self):
    #     self.assertEqual(self.number, 10, msg=u"您输入的不是10")

    def test_case1(self):
        self.prime = count.is_prime(4)
        self.assertTrue(self.prime, msg=u"不是质数！")

    def test_case2(self):
        self.a = "good"
        self.b = "hello world"
        self.assertIn(self.a, self.b, msg=u"a没在b里面")

    def tearDown(self):
        pass
if __name__ == "__main__":
    # unittest.main()

    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(Test("test_case1"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)