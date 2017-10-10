# -*- coding:UTF-8 -*-
#定义一个简单字典类
class SimpleDictionary:
    """"class to make an instance behave like a dictionary"""
    def __getitem__(self, key):
        """"overloaded key-value access"""
        return self.__dict__[key]
    def __setitem__(self, key, value):
        """"overloaded key-value assignment/acreation"""
        self.__dict__[key]=value
    def __delitem__(self, key):
        del self.__dict__[key]
    def __str__(self):
        """overloaded string representation"""
        return str(self.__dict__)
    #common mapping methods
    def keys(self):
        """":return list of keys in dictionary"""
        return self.__dict__.keys()
    def values(self):
        """"returns lisy of values in dictionary"""
        return self.__dict__.values()
    def items(self):
        """"returns list of items in dictionary"""
        return self.__dict__.items()

simple=SimpleDictionary()
print "the empty dictionary:",simple
simple[1]="one"
simple[2]="two"
simple[3]="three"
print "the dictionary after adding values:",simple

del simple[1]
print "the dictionary after removing a value:",simple

print "dictionary keys:",simple.keys()
print "dictionary values:",simple.values()
print "dictionary items:",simple.items()