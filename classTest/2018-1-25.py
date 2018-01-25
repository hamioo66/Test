# -*- coding=UTF-8 -*-
from __future__ import division
"""
author:hamioo
date:2018/1/25
describle:整数 求和
"""
integer1 = raw_input("输入一个整数：\n")
integer1 = int(integer1)
integer2 = raw_input("输入第二个整数：\n")
integer2 = int(integer2)
sum = integer1+integer2
print "求和是：", sum
if integer1 ==integer2:
    print "%d is equel to %d" %(integer1,integer2)
if integer1 !=integer2:
    print "%d is not equel to %d" %(integer1,integer2)
if integer1 < integer2:
    print "%d is less than %d" %(integer1,integer2)
if integer1 > integer2:
    print "%d is more than %d" %(integer1,integer2)

print range(10)
print range(10,0,-1)

# 求2-100所有偶数整数的和
sum = 0
for number in range(2,101,2):
    sum  = sum + number
print sum

# 新开一个户头，存入1000美元，年利率5%，假定所有利息收入都重新存入户头，计算并打印为期10年的时间里每年结束时的存款金额


principal = 1000.0
rate = 0.05
print "year %21s" %"amount on deposit"
for year in range(1,10):
    amount = principal*(1.0+rate)**year
    print "%4d%21.2f"%(year,amount)



import random
for i in range(1,21):
    print "%10d" %(random.randrange(1,7))
    if i % 5 == 0:
        print