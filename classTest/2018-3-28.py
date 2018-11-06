# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:keys(),values()和items()方法分别对应于字典的键、值和键值对，这些方法返回的不是真正的列表，它们不能被修改
"""
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
for s in spam.keys():
    print(s)
for i in spam.items():
    print(i)
    print(type(spam))
print type(spam.keys())
print list(spam.keys())
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))


print 'color' in spam
print 'haii' not in spam


import pprint
message = 'It was a bright cold day in April,and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)


# 漂亮打印
"""
如果字典本身包含嵌套的列表或字典，pprint.pprint()函数特别有用，如果希望得到漂亮的打印的文本作为字符串，
而不是显示在屏幕上，那就调用pprint.pformat(),下面是等价的
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
"""
