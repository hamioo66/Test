# -*- coding:UTF-8 -*-
#生成器（generator）的实现
g=(x*x for x in range(10))
for n in g:
    print n

def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
fib(10)
#map/reduce
#python内建map()和reduce()函数
#map函数接收两个参数，一个是函数，一个是序列，map将传入的函数一次作用到序列的每个元素，并把结果作为新的list返回
def f(x):
    return x*x
print map(f,[4,6,8,10])
print map(str,[1,2,3,4,5])
#reduce的用法，reduce把一个函数作用于在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def g(x,y):
    return x*y
print reduce(g,[2,5,8,10])

def fn(x,y):
    return x*10+y
print reduce(fn,[1,3,5,7,9])
"""字符串str也是一个序列配合map()，将str转换为int的函数"""
def char2num(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
print reduce(fn,map(char2num,'13579'))

print map(str.title,['AJSJJK','sdMMM','HelLo'])

#filter()函数用于过滤序列
def is_odd(n):
    return n%2==1
print filter(is_odd,[1,2,3,4,5,6,7,8,9])
def abs(x):
    if x<2:
        return True
    for j in range(2,11):
        if x/j==0:
            return True
    return False
print filter(abs,range(1,101))

#面向对象编程
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print '%s:%s'%(self.name,self.score)
jack=Student('jack',100)
lisa=Student('lisa',60)
jack.print_score()
lisa.print_score()


def reversed_cmp(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    return 0

print sorted([3,2,9],reversed_cmp)




