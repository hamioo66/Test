# -*- coding: UTF-8 -*-

"""
{'a':1,{'b':2,'c':3,{'d':4,'f':6},'e':5}}将格式转换成
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
"""

# a = {'a':1,{'b':2,'c':3,{'d':4,'f':6},'e':5}}
b = {'a': 1, 'b': 2, 'c': 3}



"""
列表适用于包含一组有序的值，字典适合于包含关联的键与值，但是字典和列表中需要包含其他字典和列表。
"""

stuf = {"rope":1,"torch":6,"gold coin":23,"dagger":1}
def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuf)

print("hello\ngood afternoon")
print('''
年后
就是
2019
''')

print ','.join(['cat', 'rats', 'bats'])
print 'abc'.join(['A', 'B', 'C'])

import pyperclip
pyperclip.copy('Hello world')
print pyperclip.paste()


import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('phone number found:' + mo.group())

haRegex = re.compile(r'(ha){3}')
mo1 = haRegex.search('hahaha')
print(mo1.group())

"""
在正则表达式的开始处使用插入符号（^），表明匹配必须发生在被查找文本开始处。
类似第，可以在正则表达式的米未加上美元符号（$），表示该字符串必须以这个正则
表达式的模式结束。同时使用^和$，表明整个字符串必须匹配该模式。
"""

beginsWithHello = re.compile(r'hello')
print beginsWithHello.search('Hello world!')==None


import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('c:\\User\\asweigart', filename))


print os.getcwd()
os.chdir('c:\\Windows\\System32')
print(os.getcwd())