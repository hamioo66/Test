# -*- coding:UTF-8 -*-
from log import Logger

logger=Logger(logname='log.txt',loglevel=1,logger="fox").getlog()


#try:语句设立了这样一种情形，其中try：语句后面可以跟一个except：语句，每个except：语句都处理错误，错误也被正式地称作异常。
fridge_contents={"egg":8,"mushroom":20,"pepper":3,"cheese":2,"tomato":4,"milk":13}
try:
    if fridge_contents["orange juice"]>3:
        print("sure,let's have some juice!")
except KeyError:
    print("there is no juice,Let's go shopping")