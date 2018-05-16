#coding=utf-8
import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
class BaseDriver:
    def android_driver(self,i,):
        print "this is android_driver",i
        #adb devices 显示devices_name
        #port
        write_file=WriteUserCommand()
        devices=write_file.get_value('user_info_'+str(i),'deviceName')
        port=write_file.get_value('user_info_'+str(i),'port')


        capabilities = {
            "platformName": "Android",
         #   "automationName": "UiAutomator2",
            "deviceName": devices,
            "platformVersion": "7.1.1",
            "appPackage": "in.haojin.nearbymerchant",
            "appActivity": "in.haojin.nearbymerchant.ui.activity.WelcomeActivity"

          }

        driver=webdriver.Remote("http://localhost:"+port+"/wd/hub",capabilities)
        time.sleep(10)
        return driver



