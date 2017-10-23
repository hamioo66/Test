# -*- coding:UTF-8 -*-
import os,logging
class Athlete():
    def __init__(self,a_name,a_dob=None,a_time=[]):
        self.name=a_name
        self.dob=a_dob
        self.times=a_time
# sarah=Athlete('david','2017-10-23',['2.58','2.58','1.56'])
# james=Athlete('James Jones')
# print type(sarah)
# print  sarah.name,sarah.dob,sarah.times
# print type(james),james.name,james.dob,james.times
    """创建一个sanitize()函数，这个函数从各个选手的列表接收一个字符串作为输入，
    然后处理这个字符串，将找到的所有短横线或冒号替换成为一个点号，并返回清理过的字符串，
    已经包含一个点号，则不需要再做处理。"""

    def sanitize(time_string):
        if '-' in time_string:
            splitter = '-'
            (mins, secs) = time_string.split(splitter)
        elif ':' in time_string:
            splitter = ':'
            (mins, secs) = time_string.split(splitter)
        else:
            return time_string
        return (mins + '.' + secs)

    def top3(self):
        return(sorted(set([Athlete.sanitize(t) for t in self.times]))[0:3])

    def get_coach_data(self,filename):
        try:
            with open(filename) as f:
                data=f.readline()
            temp1=data.strip().split(',')
            return Athlete(temp1.pop(0),temp1.pop(0),temp1)
        except IOError as ioerr:
            print('File error:'+str(ioerr))
    james=get_coach_data("file/b.txt")
    print(james.name)+"'s fastest time are'"+str(james.top3())


