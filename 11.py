# coding=utf-8
from selenium import webdriver
from time import sleep
for i in range(2,2):
    print("T-minus")
    print(i)

for i in range(900,100,-100):
    print i

print str(range(900,100,-100))
print (900.0001/100)
a,b=0,1
while b<10:
    print b
    a,b=b,a+b

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.set_window_size(800,900)
#获取网站名及链接地址
import os
if 'HTTP_PROXY' in os.environ:del os.environ['HTTP_PROXY']
dr=webdriver.Chrome()
url='http://www.baidu.com'
dr.get(url)
print "title of current page is %s" %(dr.title)
print "url of current page is %s" %(dr.current_url)
sleep(1)
dr.quit()

#计算学生的平均成绩1
total=0
count=0
while count<=10:
    grade=raw_input(u"请输入学生成绩: ")
    grade=int(grade)
    total=grade+total
    count=count+1
avg=total/10
print u"学生的平均分为：%d" %avg

#计算学生的平均成绩2
grade=raw_input(u"输入一个大于 -1的数")
grade=int(grade)
while grade!=-1:
    total=total+grade
    count=count+1
    grade=raw_input(u"输入一个大于 -1的数")
    grade=int(grade)
if count!=0:
    average=float(total)/count
    print u"平均分是：%f"%average
else:
    print "没有输入成绩"


