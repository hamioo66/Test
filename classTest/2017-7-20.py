# -*- coding=UTF-8 -*-
import math
import random
from appium import webdriver #导入python版的appium(webdriver)模板

#定义驱动的参数
#desired_caps={}
#desired_caps['platformName']='Android'
#desired_caps['platformVersion']='4.2'
#desired_caps['deviceName']='Android Emulator'
#desired_caps['appPackage']='com.android.calculator2'
#desired_caps['appActivity']='.calculator'
#driver=webdriver.Remote('http://localhost:4723/wd/hu',desired_caps)

print math.sqrt(900)
print math.pow(3,4)
def square(y):
    return y*y
for x in range(1,11):
    print square(x)
    print

def maxiNumValue(x,y,z):
    maximum=x
    if y>maximum:
        maximum=y
       # print "maximum is %d" %y
    if z>maximum:
        maximum=z
       # print "maximum is %d" %z
    return maximum
a=int(raw_input("enter first integer:"))
b=int(raw_input("enter second integer:"))
c=int(raw_input("enter third integer:"))
print("maximum int is:",maxiNumValue(a,b,c))
print

e=float(raw_input("enter first float:"))
f=float(raw_input("enter second float:"))
g=float(raw_input("enter third float:"))
print("maximum float is:",maxiNumValue(e,f,g))
print

h=raw_input("enter first number")
i=raw_input("enter second number")
j=raw_input("enter third number")
print("maximum number is:",maxiNumValue(h,i,j))
print

for i in range(1,21):
    print "%d" %(random.randrange(1,7)),
    if i%5==0:
        print

#模拟掷筛子6000次
frequency1=0
frequency2=0
frequency3=0
frequency4=0
frequency5=0
frequency6=0
for roll in range(1,6001):
    face=random.randrange(1,7)
    if face==1:
        frequency1+=1
    elif face==2:
        frequency2+=1
    elif face==3:
        frequency3+=1
    elif face==4:
        frequency4+=1
    elif face==5:
        frequency5+=1
    elif face==6:
        frequency6+=1
    else:
        print "never get here"
print "Face %13s" %"Frequency"
print "1 %13d" %frequency1
print "2 %13d" %frequency2
print "3 %13d" %frequency3
print "4 %13d" %frequency4
print "5 %13d" %frequency5
print "6 %13d" %frequency6
