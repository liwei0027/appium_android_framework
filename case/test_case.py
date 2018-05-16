#coding=utf-8
import sys
sys.path.append("D:/PycharmProjects/appium_android_framework")
import unittest
import threading
import HTMLTestRunner
import threading
from appium import webdriver
from business.login_business import LoginBusiness
from util.write_user_command import WriteUserCommand
from util.server import Server
import time

class ParameTestCase(unittest.TestCase):
    def __init__(self,methodName='runTest',parame=None):
        super(ParameTestCase,self).__init__(methodName)
        self.parame=parame
        global parames
        parames=parame



class CaseTeat(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print "setUpclass--->",parames
        cls.login_business=LoginBusiness(parames)
    def setUp(self):#
        print "this is setup\n"
    def test_01(self):
        print "this is case 1--->：",parames
        self.login_business.login_pass()
        print"登录成功，测试通过"
 #   unittest.skip()
    def test_02(self):
        print "this is case 2\n"
    def tearDown(self):
        print "this is teardown\n"
    @classmethod
    def tearDownClass(cls):
        print "this is class teardown\n"
def appium_init():
    server=Server()
    server.main()

def get_suite(i):
    print "get_suite里面的",i
    suite=unittest.TestSuite()
    suite.addTest(CaseTeat("test_02",parame=i))
    suite.addTest(CaseTeat("test_01",parame=i))
    unittest.TextTestRunner().run(suite)
    # html_file="D:/PycharmProjects/appium_android_framework/report/report.html"
    # fp=file(html_file,"wb")
    # HTMLTestRunner.HTMLTestRunner(fp).run(suite)

if __name__ == '__main__':
    appium_init()
    threads=[]
    for i in range(2):
        print i
        t=threading.Thread(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
