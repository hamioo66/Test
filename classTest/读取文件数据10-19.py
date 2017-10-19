# -*- coding:UTF-8 -*-
import os,logging

"""对于数据中存在某种特定的格式，处理各行数据，根据需要抽取数据行中的各个部分，
split()方法可以提供帮助，split()方法返归一个字符串列表，会赋至一个目标标识符列表，称为多重赋值"""
# logging.info(os.getcwd())
# os.chdir('../file/test')#改变当前工作目录到别的目录

logging.info(os.getcwd())
man=[]
other=[]
try:
    data=open('file/test.txt')
    #print(data.readline())
    for each_line in data:
        if not each_line.find(":")==-1:
            try:
                (role,line_spoken)=each_line.split(':')
                line_spoken=line_spoken.strip()#"strip()方法从字符串中 去除不想要的空白符"
                if role=='Man':
                    man.append(line_spoken)
                elif role=="other man":
                    other.append(line_spoken)
                print(role+" said: "+line_spoken)
            except ValueError:
                pass
    data.close()
except IOError:
    print("数据文件已经丢失")
try:
    man_file=open('file/man_data.txt','w')
    other_file=open('file/other_data.txt','w')
    # print(man,file=man_file)
    # print(other,file=other_file)     //仅支持python2.7
    for i in range(len(man)):
        man_file.write(man[i])
    for j in range(len(other)):
        other_file.write(other[j])

    man_file.close()
    other_file.close()
except IOError:
    print("File error")


#代码存在的问题
#如果数据文件的格式发生改变，这个代码可能会有问题，相应地也需要改变条件
#if语句使用的条件有点不好读，也不好理解
#这个代码有点“脆弱”，如果再出现另一个异常情况它就会出问题。
#数据文件存在丢失情况
#try/except机制
"""try语句提供一个途径，可以运行时系统地处理异常和错误。"""