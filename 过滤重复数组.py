# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/3
describle:l=[[5,6],[5,6],[8,5],[22],[5],[5,8],[5,6],[8,5]]
把这个数组结果输出成：l=[[5,6][8,5],[22],[5],[5,8]]
"""

l = [[5, 6], [5, 6], [8, 5], [22], [5], [5, 8], [5, 6], [8, 5]]


list = []
for i in l:
    if i in list:
        continue
    else:
        list.append(i)
print list




def passed(item):
    try:
        return item != "techbrood" #can be more a complicated condition here
    except ValueError:
        return False

org_words = [["this","is"],["demo","from"],["techbrood"]]
words = [filter(passed, item) for item in org_words]
print words


l = [1, 1, 2, 2, 3, 4, 5]
s = set(l)
print type(s)
c = [i for i in s]
print c

