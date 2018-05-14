#coding=utf-8
import time
from appium import webdriver

class BaseDriver:
    def android_driver(self):
        #print "this is android_driver"
        #adb devices 显示devices_name
        #port
    #    write_file=WriteUserCommand()

        capabilities = {
            "platformName": "Android",
         #   "automationName": "UiAutomator2",
            "deviceName": "OneOlus X",
            "platformVersion": "5.1.1",
            "appPackage": "in.haojin.nearbymerchant",
            "appActivity": "in.haojin.nearbymerchant.ui.activity.WelcomeActivity"

          }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        #driver=webdriver.Remote("http://localhost:"+port+"/wd/hub",capabilities)
        time.sleep(10)
        return driver



