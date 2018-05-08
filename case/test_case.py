#coding=utf-8
import unittest
import threading

class CaseTeat(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "this is class"
    def setUp(self):#自带
        print "this is setup"
    def test_01(self):
        print "this is case"
    def test_02(self):
        print "this is case 2"
    def tearDown(self):
        print "this is teardown"
    @classmethod
    def tearDownClass(cls):
        print "this is class teardaom"
if __name__=='__main__':
    unittest.main()