# -*- coding:UTF-8 -*-
class AthleteList(list):
    def __init__(self, name):
        list.__init__([])  # 初始化所派生的类，然后把参数赋至属性
        self.name = name
johnny=AthleteList("John Paul Jones") #创建一个新的“NameList”对象实例
for attr in johnny:
    print(johnny.name+" is a "+attr+".")