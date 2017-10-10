# -*- coding:UTF-8 -*-
#定义一个类
class Time:
    # 文档化字符串，描述了类
    """Time abstract dta type(ADT) defination"""
    def __init__(self):
        """Initializes hour,minute and second to zero"""
        self._hour=0
        self._minute=0
        self._second=0
    def setTime(self,hour,minute,second):
        """"set value of hour,minute,and second"""
        self.setHour(hour)
        self.setMinute(minute)
        self.setSecond(second)
    def setHour(self,hour):
        if 0<=hour<24:
            self._hour=hour
        else:
            raise ValueError,"Invalid hour value:%d" %hour
    def setMinute(self,minute):
        if  0<=minute<60:
            self._minute=minute
        else:
            raise ValueError,"Invalid minute value:%d" %minute
    def setSecond(self,second):
        if 0<=second<60:
            self._second=second
        else:
            raise ValueError,"Invalid second value:%d" %second
    def getHour(self):
        return self._hour
    def getMinute(self):
        return self._minute
    def getSecond(self):
        return self._second
    def printMilitary(self):
        """"prints object of class Time in military format"""
        print "%.2d:%.2d:%.2d" %(self._hour,self._minute,self._second)
    def printStandard(self):
        """"print object of class time in standard format"""
        standardTime=""
        if self._hour==0 or self._hour==12:
            standardTime+="12:"
        else:
            standardTime+="%d:" %(self._hour%12)
        standardTime+="%.2d:%.2d" %(self._minute,self._second)
        if self._hour<12:
            standardTime+="AM"
        else:
            standardTime+="PM"
        print standardTime
