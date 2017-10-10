# -*- coding:UTF-8 -*-
#读取Excel
import xlrd
from selenium import webdriver
import sys
reload(sys)
range(128)
sys.setdefaultencoding('utf-8')

class ExcelAction():
    """只支持excel格式"""
    def Driver(self):
        driver = webdriver.Firefox()
        driver.get("http://123.206.8.92:7000/login")

    def transcode(self,filename,sheetname):
        self.filename=filename.decode('utf-8')
        self.sheetname=sheetname.decode('utf-8')
        return filename,sheetname
    def read_excel(self,filename,sheetname):
        """读取excel"""
        filename,sheetname=self.transcode(filename,sheetname)
        workbook=xlrd.open_workbook(filename)#获得工作簿
        sheet=workbook.sheet_by_name(sheetname)#获得sheet
        rows=sheet.nrows#文件总行数
        list=[]
        print u'----文件内容----'
        for i in range(0,rows):
            line=sheet.row_values(i)
            list.append(line)
            print '['+','.join("'"+str(element)+"'" for element in line)+']'
            for i in list:
                username=i[0]
                password=i[1]
                print "用户名是：%s 密码是：%s" %(username,password)
                #driver.find_element_by_name("telphone").send_keys(username)
                #driver.find_element_by_name("password").send_keys(password)
        print u'----------------'
        return list


if __name__=='__main__':
    e=ExcelAction()
    filename=r'hello.xls'
    sheetname='测试'
    list=e.read_excel(filename,sheetname)


