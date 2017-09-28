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
##############
import os
if 'HTTP_PROXY' in os.environ:del os.environ['HTTP_PROXY']
dr=webdriver.Chrome()
url='http://www.baidu.com'
dr.get(url)
print "title of current page is %s" %(dr.title)
print "url of current page is %s" %(dr.current_url)
sleep(1)
dr.quit()

