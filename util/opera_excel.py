#coding=utf-8
import xlrd
# excel=xlrd.open_workbook('D:/PycharmProjects/appium_android_framework/config/case.xlsx')
# data=excel.sheets()[0]
# print data.nrows
# print data.cell(4,5).value

class OperaExcel:
    def __init__(self,file_path=None,i=None):
        if file_path==None:
            self.file_path='D:/PycharmProjects/appium_android_framework/config/case.xlsx'
        else:
            self.file_path=file_path
        if i==None:
            i=0
        self.excel=self.get_excel()
        self.data=self.get_sheets(i)

    def get_excel(self):
        '''
        获取excel
        :return:
        '''
        excel = xlrd.open_workbook(self.file_path)
        return excel
    def get_sheets(self,i):
        '''
        获取sheets的内容
        :return:
        '''
        tables=self.excel.sheets()[i]
        return tables

    def get_lines(self):
        '''
        获取行数
        :return:
        '''
        lines=self.data.nrows
        return lines
    def get_cell(self,row,cell):
        '''
        获取单元格
        :param row:
        :param cell:
        :return:
        '''
        data=self.data.cell(row,cell).value
        return data


if __name__=='__main__':
    opera=OperaExcel()
    print opera.get_cell(4,5)
