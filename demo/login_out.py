#coding=utf-8
import time
from appium import webdriver
capabilities={
    "platformName":"Android",
    "deviceName":"OneOlus X",
    "platformVersion":"5.1.1",
    "appPackage":"in.haojin.nearbymerchant",
    "appActivity":"in.haojin.nearbymerchant.ui.activity.WelcomeActivity"
}
driver=webdriver.Remote('http://localhost:4723/wd/hub',capabilities)


def login():
    time.sleep(10)
    #登录页面
    driver.find_element_by_id('in.haojin.nearbymerchant:id/et_phoneNum').send_keys('17600695527')
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/password').send_keys('123456')
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/button').click()
    time.sleep(5)


#获取屏幕的尺寸坐标
def get_size():
    size = driver.get_window_size()
    print(driver.get_window_size())
    width = size['width']
    height = size['height']
    return width,height
#向上滑动
def swipe_up():
    #[x,y]
    x1=get_size()[0]/2
    y1=get_size()[1]/10*9
    y=get_size()[1]/2
    driver.swipe(x1,y1,x1,y)
#向下滑动
def swipe_down():
    #[x,y]
    x1=get_size()[0]/2
    y1=get_size()[1]/10
    y=get_size()[1]/10*9
    driver.swipe(x1,y1,x1,y)
#向右滑动
def swipe_right():
    #[x,y]
    x1=get_size()[0]/10
    y1=get_size()[1]/2
    x=get_size()[0]/10*9
    driver.swipe(x1,y1,x,y1)
#向左滑动
def swipe_left():
    #[x,y]
    x1=get_size()[0]/10*9
    y1=get_size()[1]/2
    x=get_size()[0]/10
    driver.swipe(x1,y1,x,y1)
def swipe_on(direction):
    if direction=='up':
        swipe_up()
    elif direction=='down':
        swipe_down()
    elif direction=='left':
        swipe_left()
    else:
        swipe_right()

login()
time.sleep(5)
driver.find_element_by_id('in.haojin.nearbymerchant:id/tv_tab_me').click()
time.sleep(5)
swipe_on('up')
driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '设置')]").click()
#退出登录
time.sleep(5)
driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '退出登录')]").click()

