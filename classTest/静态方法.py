# -*- coding:UTF-8 -*-
#静态方法，所有类（不仅仅是从object继承的类）都可定义“静态方法”。静态方法可由类的一个客户调用，既是不存在类的任何对象

class Employee:
    numberOfEmployees=0
    maxEmployees=10
    def isCrowded():
        """static method returns true if the employees are  crowded"""
        return Employee.numberOfEmployees>Employee.maxEmployees
    #创建静态方法
    isCrowded=staticmethod(isCrowded)
    def __init__(self,firstName,lastName):
        """职工构造器，构造名和姓"""
        self.firstName=firstName
        self.lastName=lastName
        Employee.numberOfEmployees+=1
    def __del__(self):
        """职工析构函数"""
        Employee.numberOfEmployees-=1
    def __str__(self):
        """职工字符串表示"""
        return "%s %s" %(self.firstName,self.lastName)
#主函数
def main():
    answers=["NO","YES"]
    employeeList=[]
    print "Employee are crowded?"
    print answers[Employee.isCrowded()]
    print "\n Creating 11 objects of class Employee..."
    #创建11个职工对象
    for i in range(11):
        employeeList.append(Employee("John","Doe"+str(i)))
        print "Employees are crowded?"
        print employeeList[i]
        print answers[employeeList[i].isCrowded()]
    print "\nRemoving one employee..."
    del employeeList[0]
    print "Employees are crowded?",answers[Employee.isCrowded()]
if __name__=="__main__":
    main()
