# -*- coding: UTF-8 -*-
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return 'Vector (%d,%d)' %(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)
v1=Vector(1,16)
v2=Vector(-22,100)
print v1+v2


import re
print(re.match('www','www.baidu.com').span())
print(re.match('com','www.runoob.com'))
line="Cats are smarter than dogs"
matchObj=re.match(r'(.*) are (.*?).*',line,re.M|re.I)
if matchObj:
    print "matchObj.group():",matchObj.group()
    print "matchObj.group(1):",matchObj.group(1)
    print "matchObj.group(2):",matchObj.group(2)
else:
    print "no match!!!"

import MySQLdb

db=MySQLdb.connect("localhost","root","root","hello",charset="utf8")
cursor=db.cursor()
cursor.execute("select version()")
data=cursor.fetchone()
name="zhm"
age=24
address="重庆渝中区万科锦尚"
#sql="""insert into student values("%s","%s","%s")%(name,age,address)"""
try:
    cursor.execute('insert into student values("%s","%s","%s")' %(name,age,address))
    db.commit()
except:
    db.rollback()
db.close()


