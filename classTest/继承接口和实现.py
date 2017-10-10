# -*- coding:UTF-8 -*-
#继承接口和实现
class Employee:
    """"Abstract base class Employee 抽象基类"""
    def __init__(self,first,last):
        """Employee构造器，不能创建类对象"""
        self.fistName=first
        self.lastName=last
    def __str__(self):
        """用字符串呈现Employee"""
        return  "%s %s" %(self.fistName,self.lastName)
    def _checkPosition(self,value):
        """Utility method to ensure a value is positive 通用方法确保值是可用的"""
        if value<0:
            raise ValueError,"Attribute value (%s) must be positive" %value
        else:
            return value
    def earnings(self):
        """Abstract method;derived classes must override"""
        raise NotImplementedError,"Cannot call abstract method"

class Boss(Employee):
    """继承Employee"""
    def __init__(self,first,last,salary):
        Employee.__init__(self,first,last)
        self.weeklySalary=self._checkPosition(float(salary))
    def earnings(self):
        return self.weeklySalary
    def __str__(self):
        return "%17s: %s" %("Boss",Employee.__str__(self))

class CommissionWorker(Employee):
    def __init__(self,first,last,salary,commission,quantity):
        Employee.__init__(self,first,last)
        self.salary=self._checkPosition(float(salary))
        self.commission=self._checkPosition(float(commission))
        self.quantity=self._checkPosition(quantity)
    def earnings(self):
        return  self.salary+self.commission*self.quantity
    def __str__(self):
        return "%17s: %s" %("Commmission",Employee.__str__(self))

class PieceWorker(Employee):
    def __init__(self,first,last,wage,quantity):
        Employee.__init__(self,first,last)
        self.wagePerPiece=self._checkPosition(float(wage))
        self.quantity=self._checkPosition(quantity)
    def earnings(self):
        return self.quantity*self.wagePerPiece
    def __str__(self):
        return "%17s: %s" %("Pieceworker",Employee.__str__(self))

class HourlyWorker(Employee):
    def __init__(self,first,last,wage,hours):
        Employee.__init__(self,first,last)
        self.wage=self._checkPosition(float(wage))
        self.hours=self._checkPosition(float(hours))
    def earnings(self):
        if self.hours<=40:
            return self.wage*self.hours
        else:
            return 40*self.wage+(self.hours-40)*self.wage*1.5
    def __str__(self):
        return "%17s: %s" %("HourlyWorker",Employee.__str__(self))

employees=[
    Boss("John","Smith",800.00),
    CommissionWorker("Sue","Jones",200.0,3.0,150),
    PieceWorker("Bob","Lewis",2.5,200),
    HourlyWorker("Karen","Price",13.75,40)
]
for employee in employees:
    print "%s earned $%.2f" %(employee,employee.earnings())

