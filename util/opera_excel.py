#coding=utf-8
import xlrd
excel=xlrd.open_workbook('D:/PycharmProjects/appium_android_framework/config/case.xlsx')
data=excel.sheets()[0]
print data.nrows
print data.cell(3,4).value

class OperaExcel:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='D:/PycharmProjects/appium_android_framework/config/case.xlsx'
        else:
            self.file_path=self.get_excel()

    def get_excel(self):
        excel = xlrd.open_workbook(self.file_path)
        return excel
