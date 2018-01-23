# -*- coding: UTF-8 -*-

"""
1、读取excel  workbook = xlrd.open_workbook('file.xls')
2、获取excel中表单数量  workbook.nsheets
3、获取excek中的一个表单
workbook.sheet()[i]
workbook.sheet_by_index(i)
workbook.sheet_by_name(u'sheet')
4、获取行数  sheet.nrows
5、获取列数  sheet.ncols
6、获取整行数据  sheet.row(i)
7、获取整列数据  sheet.col(i)
8、获取单元格数据  sheet.cell(i,j).value
"""
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


