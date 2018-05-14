#coding=utf-8
from handle.login_handle import LoginHandle
class LoginBusiness:
    def __init__(self,i):
        self.login_handle=LoginHandle(i)

    def login_pass(self):
        #self.login_handle.click_merchant()
        self.login_handle.send_phoneNum('17600695527')
        self.login_handle.send_password('123456')
        self.login_handle.click_loginButton()

    def login_phone_error(self):
        self.login_handle.click_merchant()
        self.login_handle.send_phoneNum('17600695528')
        self.login_handle.send_password('123456')
        self.login_handle.click_loginButton()
        phone_flag=self.login_handle.get_fail_toast('您的帐号未注册，请先注册一下吧')
        if phone_flag:
            return True
        else:
            return False
    def login_password_error(self):
        self.login_handle.click_merchant()
        self.login_handle.send_phoneNum('17600695527')
        self.login_handle.send_password('1234567')
        self.login_handle.click_loginButton()
