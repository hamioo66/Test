# -*- coding:UTF-8 -*-
#继承类的实现
import math
class Point:
    """class that represents genmetric point"""
    def __init__(self,xValue=0,yValue=0):
        """"point constructor takes x and y coordinates"""
        self.x=xValue
        self.y=yValue
class Circle(Point):
    """class ths represents a circle"""
    def __init__(self,x=0,y=0,radiusValue=0.0):
        """Circle constructoe takes x and y coordinates of center point and radius"""
        Point.__init__(self,x,y)
        self.radius=float(radiusValue)
    def area(self):
        return math.pi*self.radius**2

print "point bases:",Point.__bases__
print "Circle bases:",Circle.__bases__

print "\nCircle is a subclass of point:",issubclass(Circle,Point)
print "Point is a subclass of Circle:",issubclass(Point,Circle)

point=Point(30,50)
circle=Circle(120,89,2.7)

print "\nCircle is a Point object",isinstance(circle,Point)
print "Point is a Circle object",isinstance(point,Circle)

print "\npoint member:\n\t",point.__dict__
print "circle members:\n\t",circle.__dict__
print "\n Area of circle",circle.area()
