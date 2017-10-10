# -*- coding:UTF-8 -*-
import json
print json.dumps({'a':'Runoob','b':7},sort_keys=True,indent=4,separators={',',':'})


class Vector:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        if self.name!="" and self.password!="":
            print "登录成功,用户名:%s,密码：%s" %(self.name,self.password)
        elif self.name=="" and self.password!="":
            print "请输入用户名"
        elif self.name!="" and self.password=="":
            print "请输入密码"
        else:
            print "welcome"

a=Vector("xcvcv","")
a.login()

