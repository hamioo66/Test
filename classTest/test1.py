#-*- coding: utf-8 -*-
print("hello world");
x=int(input("please input an integer"))
if x<0:
    print("Nagative changed to zero")
elif x==0:
    print("Zero")
elif x==1:
    print("Single")
else:
    print("Morre")
# case 2
word=['cat','dog','windows']
for w in word:
    print(w,len(w))
# case 3
for i in range(5):
    print i

# case 4
a=['Mary','hada','little','lamb']
print(len(a))
for i in range(len(a)):
    print(i,a[i])

# case 4
def fib(n):
    a,b=0,1
    while a<n:
        print(a)
        a,b=b,a+b
        #print()
fib(2000)

# case 5
age=25
name='hamioo'
print('{0} is {1} years old'.format(name,age))
print('Why is {0} playing with that Python?'.format(name))
print(name+' is '+str(age)+' years old！')
#print('{0:.3}'.format(1/3))
#print('{0:_^11}'.format('hello'))
#print('{name} wrote {book}'.format(name='hello',book='c language'))

# case 6
number =23
running = True
while running:
    guess=int(input('enter an integer'))
    if guess==number:
        print('Congratulations,you guessd it!')
        print('(but you do not win any prizes!)')
        running=False
    elif guess>number:
        print('No,it is a little higher than that')
    else:
        print('NO,it is a little lower than that')
else:
    print('The while loop is over!')
print('Done!')


for i in range(1,5):
    print(i)
else:
    print('The for loop is over')


#while True:
   # s =input('Enter something:')
   # if s == 'quit':
   #     break
  #  if len(s)<3:
    #    print('Too small')
    #    continue
    #print('Input is of sufficient length')



def sayHello():
    print("hello world!")

sayHello()

def printMax(a,b):
    if a>b:
        print(a,'is maximum')
    elif a==b:
        print(a,'is equal to',b)
    else:
        print(b,'is maximum')
printMax(3,5)
x=9
y=199
printMax(x,y)

# case 2017-7-10
def func(a,b=5,c=10):
    print('a is ',a,'and b is',b,'and c is ',c)
func(3,7)
func(25,c=24)
func(c=50,a=100)


def sayhi():
    print('Hi,this is mymodule speaking')
_version_='0.1'