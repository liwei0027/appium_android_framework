#coding=utf-8
from util.get_by_local import GetByLocal
import time
from base.base_driver import BaseDriver
from selenium.webdriver.support.ui import WebDriverWait#自动等待
from selenium.webdriver.support import expected_conditions as EC#条件判断@

class LoginPage:
    #获取登录页面所有的页面元素信息
    def __init__(self):
        base_driver=BaseDriver()
        self.driver=base_driver.android_driver()
        self.get_by_local=GetByLocal(self.driver)

    def get_merchant_element(self):
        '''
        获取商户元素信息
        :return:
        '''
        return self.get_by_local.get_element('merchant')

    def get_operator_element(self):
        '''
        获取收银员元素信息
        :return:
        '''
        return self.get_by_local.get_element('operator')

    def get_phoneNum_element(self):
        '''
        获取帐号元素信息
        :return:
        '''
        return self.get_by_local.get_element('phoneNum')

    def get_password_element(self):
        '''
        获取密码元素信息
        :return:
        '''
        return self.get_by_local.get_element('password')


    def get_operatorId_element(self):
        '''
        获取收银员编号元素信息
        :return:
        '''
        return self.get_by_local.get_element('operatorId')

    def get_loginButton_element(self):
        '''
        获取登录按钮元素信息
        :return:
        '''
        return self.get_by_local.get_element('loginButton')

    def get_delPhone_element(self):
        '''
        获取删除帐号元素信息
        :return:
        '''
        return self.get_by_local.get_element('delPhone')

    def get_rememberPasswd_element(self):
        '''
        获取记住密码元素信息
        :return:
        '''
        return self.get_by_local.get_element('rememberPasswd')

    def get_forgetPassword_element(self):
        '''
        获取忘记密码元素信息
        :return:
        '''
        return self.get_by_local.get_element('forgetPassword')
    def get_toast_element(self,message):
        '''
        #获取toast
        :return:
        '''
        time.sleep(2)
        toast_element = ("xpath", "//*[contains(@text," + message + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(EC.presence_of_element_located(toast_element))
