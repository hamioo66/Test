
shopList=['apple','mango','carrot','banana']
print('I have',len(shopList),'items to purchase')
print('These items are:\n')
for item in shopList:
    print(item,'\n')
print('\n I also have to buy rice.')
shopList.append('rice')
print('My shopping list is now',shopList)
print('I will sort my list now')
shopList.sort()
print('Sorted shopping list is',shopList)
print('The first item I will buy is',shopList[0])
olditem=shopList[0]
del shopList[0]
print('I bought the',olditem)
print('My shopping list is now',shopList)


zoo=('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))
new_zoo=('monkey','camel',zoo)
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are',new_zoo)
print('Animals brought from old zoo is',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

class Person:
    def __init__(self,name):
        self.name=name
    def sayHi(self):
        print('Hello,my name is',self.name)
p=Person('ZhouHaimi')
p.sayHi()


class Robot:
    population=0
    def __init__(self,name):
        '"Initializes the data."'
        self.name=name
        print('(initializing {0})'.format(self.name))
        Robot.population+=1
    def __del__(self):
        '"I am dying"'
        print('{0} is being destroyed!'.format(self.name))
        Robot.population-=1
        if Robot.population==0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('These are still {0:d} robots working'.format(Robot.population))
    def sayHi(self):
        '"Greeting by the robot.Yeah,they can do that"'
        print('Greetings,my masters call me {0}.'.format(self.name))
    def howMany():
        '"Prints the current population"'
        print('We have {0:d} robots.'.format(Robot.population))
    howMany=staticmethod(howMany)

droid1=Robot('R2-D2')
droid1.sayHi()
Robot.howMany()
droid2=Robot('C-3PO')
droid2.sayHi()
Robot.howMany()
print('\nRobots can do some work here.\n')
print("Robots have finished their work.So let's destroy them")
del droid1
del droid2
Robot.howMany()


class SchoolMember:
    '"Represents any school member."'
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print('Initialized SchoolMember: {0}'.format(self.name))
    def tell(self):
        '"Tell my detail"'
        print('Name:"{0}"Age:"{1}"'.format(self.name,self.age))
class Teacher(SchoolMember):
    '"Represents a teacher"'
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print('Initialized Teacher: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))
class Student(SchoolMember):
    '"Represents a student"'
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print('Initialized Student: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))
t=Teacher('Mrs.Shrividya',40,30000)
s=Student('Hamioo',25,75)
print()
members=[t,s]
for member in members:
    member.tell()


def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text==reverse(text)
something = str(input("Enter text:"))
if(is_palindrome(something)):
    print("Yes,it is a palindrome")
else:
    print("No,it is not a palindrome")

poem="'Programmng is fun When the work is done if you wanna make your work also fun:use Python'"
f=open('poem.txt','w')
f.write(poem)
f.close()
f=open('poem.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)
f.close()


