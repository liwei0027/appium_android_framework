#coding=utf-8
import unittest
import threading
import HTMLTestRunner
import threading
class CaseTeat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "this is class"
    def setUp(self):#自带
        print "this is setup"
    def test_01(self):
        print "this is case"
 #   unittest.skip()
    def test_02(self):
        print "this is case 2"
    def tearDown(self):
        print "this is teardown"
    @classmethod
    def tearDownClass(cls):
        print "this is class teardaom"
if __name__=='__main__':
    #unittest.main()
    suite=unittest.TestSuite()
    suite.addTest(CaseTeat("test_02"))
    suite.addTest(CaseTeat("test_01"))
    #unittest.TextTestRunner().run(suite)
    html_file="D:/PycharmProjects/appium_android_framework/report/report.html"
    fp=file(html_file,"wb")
    HTMLTestRunner.HTMLTestRunner(fp).run(suite)