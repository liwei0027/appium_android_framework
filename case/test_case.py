#coding=utf-8
import sys
sys.path.append("D:/PycharmProjects/appium_android_framework")
import unittest
import threading
import HTMLTestRunner
import threading
from appium import webdriver
from business.login_business import LoginBusiness
class CaseTeat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "this is class"
        cls.login_business=LoginBusiness()
    def setUp(self):#自带
        print "this is setup\n"
    def test_01(self):
        print "this is case 01"
        self.login_business.login_pass()
        print"登录成功，测试通过"
 #   unittest.skip()
    def test_02(self):
        print "this is case 2"
    def tearDown(self):
        print "this is teardown"
    @classmethod
    def tearDownClass(cls):
        print "this is class teardaom"

def get_suite(i):
    suite=unittest.TestSuite()
    suite.addTest(CaseTeat("test_02"))
    suite.addTest(CaseTeat("test_01"))
    unittest.TextTestRunner().run(suite)
    # html_file="D:/PycharmProjects/appium_android_framework/report/report.html"
    # fp=file(html_file,"wb")
    # HTMLTestRunner.HTMLTestRunner(fp).run(suite)

if __name__ == '__main__':
    threads=[]
    for i in range(2):
        print i
        t=threading.Thread(target=get_suite,args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
