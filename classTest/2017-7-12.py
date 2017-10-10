# -*- coding: UTF-8 -*-
import time
import calendar
import datetime
localtime=time.asctime(time.localtime(time.time()))
print '本地时间为:',localtime
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
cal=calendar.month(2017,7)
print('2017年7月份的日历')
print(cal)


i=datetime.datetime.now()
print('当前日期和时间是%s'%i)
print('ISO格式的日期和时间是%s'%i.isoformat())
print('当前的年份是%s'%i.year)
print('当前的月份是%s'%i.month)
print('当前的日期是%s'%i.day)
print('dd/mm/yyyy格式是%s%s%s'%(i.day,i.month,i.year))
print('当前小时是%s'%i.hour)
print('当前分钟是%s'%i.minute)
print('当前秒是%s'%i.second)

print('我们都是好孩子')

str=raw_input('请输入：');
print"您输入的内容是：",str

str1=input('请输入：')
print '你输入的内容是：',str1
d=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (i!=j) and (j!=k):
              d.append([i,j,k])
print '总数量',len(d)
print  d

