# -*- coding:UTF-8 -*-
class NameList(list):   #提供一个类名，新类将派生这个类
    def __init__(self,name):
        list.__init__([]) #初始化所派生的类，然后把参数赋至属性
        self.name=name
johnny=NameList("John Paul Jones") #创建一个新的“NameList”对象实例
print johnny
print johnny.name
johnny.append("Bass Player")
print johnny
johnny.extend(['Composer','Arranger','Musician'])
print johnny
for attr in johnny:
    print(johnny.name+" is a "+attr+".")


import httplib
"""接受一个主机名或IP地址，服务器的端口号以及一个路径名，然后尝试和运行在指定主机和端口号上的web服务器链接"""
def check_web_server(host,port,path):
    h=httplib.HTTPConnection(host,port)
    h.request('GET',path)
    resp=h.getresponse()
    print("HTTP Response:")
    print 'status',resp.status
    print 'reason',resp.reason
    print('HTTP Headers:')
    for hdr in resp.getheaders():
        print '%s:%s'%hdr

check_web_server('www.baidu.com',80,'/')

