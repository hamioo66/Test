# -*- coding:UTF-8 -*-
class Student(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return '学生对象的名字：%s' %self.name

print Student('Michael')
print Student
#
# try:
#     print 'try'
# except ValueError,e:
#     print 'valueError'
# except ZeroDivisionError:
# finally:
#     print 'finally'

import json
d=dict(name='mike',age=20,score=88)
s=json.dumps(d)
print s

#创建一个基于TCP连接的Socket
#导入socket库
import socket
#创建一个socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.cn',80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
#接收数据
buffer=[]
while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=''.join(buffer)
s.close()
header,html=data.split('\r\n\r\n',1)
print header
with open('sina.html','wb') as f:
    f.write(html)