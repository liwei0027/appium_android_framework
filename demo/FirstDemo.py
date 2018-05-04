#coding=utf-8
import os
import time
from appium import webdriver
#apk_path=os.path.abspath(os.path.join(os.path.dirname(__file__)),"..")#获取当前项目的根路径


desired_caps={}
desired_caps['platformName']='Android'#设备系统
desired_caps['platformVersion']='5.1.1'#设备系统版本
desired_caps['deviceName']='OneOlus X'#设备名称
#测试apk包的路径
#desired_caps['app']='D:\\PycharmProjects\\appium_android_framework\\app\\Haojin_v4.13.4.apk'
#不需要每次都安装apk
desired_caps['noReset']=True
#应用程序的包名
desired_caps['appPackage']='in.haojin.nearbymerchant'
desired_caps['appActivity']='in.haojin.nearbymerchant.ui.activity.WelcomeActivity'
#如果设置的是app包的路径，则不需要配appPackage和appActivity，同理反之
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)#启动app
time.sleep(10)#app启动后等待5秒，等待加载完成
#根据resource-id定位元素
#driver.find_element_by_id('in.haojin.nearbymerchant:id/ll_login_way_container').click()
#time.sleep(10)
#登录页面
driver.find_element_by_id('in.haojin.nearbymerchant:id/et_phoneNum').send_keys('17600695527')
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/password').send_keys('123456')
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/button').click()
time.sleep(5)
#driver.find_element_by_id('in.haojin.nearbymerchant:id/tv_forget_pwd').click()

#退出帐号
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/tv_tab_me').click()
time.sleep(5)
#打印屏幕高和宽
print(driver.get_window_size())
x=driver.get_window_size()['width']#获取屏幕的宽
y=driver.get_window_size()['height']#获取屏幕的高
#向上滑
driver.swipe(1/2*x, 1/2*y, 1/2*x, 1/7*y, 200)
time.sleep(5)
#driver.find_element_by_id('in.haojin.nearbymerchant:id/metab_rl_root').click()#点击设置