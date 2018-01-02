# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2017/12/29
describle:
"""
print coerce(12, 12L)
print [2, 6]
# 序列乘以整数值的次数，实质上，它是一个复制过程
print [2, 6]*3
print range(2)
print range(5, 9)
# 连接序列不管附加物是什么，两个对象必须是同一类型的
print range(2)+range(5, 7)

# 字符串  string %tuple
"""
允许字符串中使用占位符，从元组中引进可选数据并最终代替字符串中的每个占位符。
"""
count = ("%50", 0)
result = 'Result:%s for the silly party %s for the really silly party'
print result % count

# sequence % dictionary
"""
允许在字符串中使用占位符，从字典中引进可选数据并最终代替字符串的每个占位符。
"""
data = {"high": "21 degrees", "low": "14 degrees"}
report = "The high today was %(high)s and the low was %(low)s"
print report % data

# 计算元素在列表中出现多少次
aa = [1, 1, 6, 8, 9, 1, 330]
print "元素出现的次数是：", aa.count(1)
# 返回和a的第一个位置相符合的索引数list.index(element)
lotsanumbers = [1, 21, 3, 2, 4, 5, 2, 4, 7, 10]
print lotsanumbers.index(2)

# list.insert(index,object)
"""
在索引的位置处把对象插入列表，较高的元素就增加一个索引位置
"""
bb = ["aaa", "bbb"]
bb.insert(1, "cccc")
print bb
bb.sort()
print bb
# 删除第一次出现的元素
bb.remove("aaa")
print bb
# 在列表中反转元素的排列次序
bb.reverse()
print bb

# 字典
# del dictionary[key] 删除关键字和它的数值
webster = {"size": "normal", "angle": "sharp", "color": "red"}
del webster["color"]
print webster
# 使用关键字搜索条目
print webster["size"]
webster["name"] = "hamioo"
print webster
print webster.has_key("name")
# dictionary.items()
#  得到作为列表的关键字和数值，列表中是元组而不是字典
print webster.items()
# dictionary.keys() 得到字典的所有关键字
print webster.keys()
# dictionary.values()  得到字典所有数值
print webster.values()
webster.clear()
print webster

# 异常的用法
try:
    open("abc.txt", "r")
    print aa
except BaseException, msg:
    print msg

try:
     aa="异常测试"
     print aa
except Exception, msg:
     print msg
else:
     print "没有异常"


import time
files = file("file/poem.txt", "r")
strs = files.readlines()
try:
    for l in strs:
        print l
        time.sleep(2)
finally:
    files.close()
    print "Cleaning up ...closed the file"


# 抛出异常
filename = raw_input("please input file name:")
if filename == "hello":
    raise NameError("input file name error!")


# 定位元素通过By时要将By类导入
from selenium.webdriver.common.by import By
from selenium import webdriver
driver =  webdriver.Firefox()
# driver.find_element(By.ID, "su")
driver.get("http://mail.126.com/")
print "Before login======="
# 打印当前页面title
title = driver.title
print title
# 打印当前页面URL
now_url = driver.current_url
print now_url
# 执行邮箱登录
driver.find_element_by_id("idInput").clear()
driver.find_element_by_id("idInput").send_keys("zhm200701@126.com")
driver.find_element_by_id("pwdInput").clear()
driver.find_element_by_id("pwdInput").send_keys("zhm811426")
driver.find_element_by_id("loginBtn").click()
print "After login ========"
title = driver.title
print title
now_url = driver.current_url
print now_url
# 获得登录的用户名
user = driver.find_element_by_id("spnUid").text
print user
driver.quit()




