#coding=utf-8
from page.login_page import LoginPage

class LoginHandle:
    def __init__(self,i):
        self.login_page=LoginPage(i)

    #操作登录页面的元素
    def click_merchant(self):
        '''
        点击商户按钮
        :return:
        '''
        self.login_page.get_merchant_element().click()

    def click_operator(self):
        '''
        点击收银员按钮
        :return:
        '''
        self.login_page.get_operator_element().click()


    def send_phoneNum(self,phoneNum):
        '''
        输入帐号
        :return:
        '''
        self.login_page.get_phoneNum_element().send_keys(phoneNum)



    def send_password(self,password):
        '''
        输入密码
        :return:
        '''
        self.login_page.get_password_element().send_keys(password)


    def send_operatorId(self,operatorId):
        '''
        输入收银员编号
        :return:
        '''
        self.login_page.get_operatorId_element().send_keys(operatorId)


    def click_loginButton(self):
        '''
        点击登录按钮
        :return:
        '''
        self.login_page.get_loginButton_element().click()


    def click_delPhone(self):
        '''
        点击删除帐号按钮
        :return:
        '''
        self.login_page.get_delPhone_element().click()


    def click_rememberPasswd(self):
        '''
        点击记住密码按钮
        :return:
        '''
        self.login_page.get_rememberPasswd_element().click()


    def click_forgetPassword(self):
        '''
        点击忘记密码
        :return:
        '''
        self.login_page.get_forgetPassword_element().click()


    def get_fail_toast(self, message):
        '''
        获取tost，根据返回信息进行反数据
        '''
        toast_element = self.login_page.get_toast_element(message)
        if toast_element:
            return True
        else:
            return False



