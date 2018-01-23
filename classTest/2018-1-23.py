# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/23
describle:循环遍历
describle:循环遍历
"""
for i in range(1, 20, 3):
    if i== 16:
        break
    elif i % 2 == 0:
        print "我是偶数" + str(i)
    else:
        print "我是奇数" + str(i)
else:
    print("循环结束")
