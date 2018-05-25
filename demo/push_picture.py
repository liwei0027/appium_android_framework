#coding=utf-8
import time
from appium import webdriver
capabilities={
    "platformName":"Android",
    "deviceName":"OnePlus X",
   # "deviceName":"9509426",
    "platformVersion":"5.1.1",
   # "platformVersion":"7.1.1",
    "appPackage":"in.haojin.nearbymerchant",
    "appActivity":"in.haojin.nearbymerchant.ui.activity.WelcomeActivity"
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',capabilities)


def login():
    time.sleep(20)
    #登录页面
    driver.find_element_by_id('in.haojin.nearbymerchant:id/et_phoneNum').send_keys('17600695527')
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/password').send_keys('123456')
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/button').click()
    time.sleep(5)

login()
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/tv_tab_me').click()
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/shop_sdv_logo').click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '店铺图片')]").click()
time.sleep(2)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '图库')]").click()
time.sleep(2)
picture_list=[]
pictures=driver.find_elements_by_class_name('android.widget.LinearLayout')

#for i in range(len(pictures)):
#    print picture_list.append()

