#coding=utf-8
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait#自动等待
from selenium.webdriver.support import expected_conditions as EC#条件判断@

class HomePage:
    #获取登录页面所有的页面元素信息
    def __init__(self,i):
        #获取driver信息
        base_driver=BaseDriver()
        self.driver=base_driver.android_driver(i)
        self.get_by_local=GetByLocal(self.driver)

    def get_payment_element(self):
        '''
        获取立即收款的元素信息
        :return:
        '''
        return self.get_by_local.get_element('立即收款')
    def get_trade_element(self):
        return self.get_by_local.get_element('查看流水')

if __name__ == '__main__':
    homepage=HomePage()
    homepage.get_trade_element()


