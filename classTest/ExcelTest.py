# -*- coding: UTF-8 -*-
import xlrd
data=xlrd.open_workbook("hello.xls")
table=data.sheets()[0]
nrows=table.nrows
ncols=table.ncols
_cellValue=[]
for i in range(nrows):
    #_cellValue.append(table.cell(i, 0).value)
    print "i的值是",i
    for j in range(ncols):
       #_cellValue.append(table.cell(i, j).value)
        print "j的值是", j
        _cellValue.append(int(table.cell(i, j).value))
    print _cellValue

#for n in range(len(_cellValue)):
m=0
if m<=len(_cellValue):
    n = 2
    for m in range(n):
        print _cellValue[int(m)]
        m=m+2
        print m