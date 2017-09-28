# coding=utf-8
from selenium import webdriver
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

