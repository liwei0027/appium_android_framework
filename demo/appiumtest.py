#coding=utf-8
import sys
sys.path.append('D:/PycharmProjects/appium_android_framework')
from util.read_init import ReadIni
from util.get_by_local import GetByLocal
import time
from appium import webdriver



def get_driver():
    capabilities={
        "platformName":"Android",
        "automationName":"UiAutomator2",
        "deviceName":"OneOlus X",
        "platformVersion":"5.1.1",
        "appPackage":"in.haojin.nearbymerchant",
        "appActivity":"in.haojin.nearbymerchant.ui.activity.WelcomeActivity"
    }
    driver=webdriver.Remote('http://localhost:4723/wd/hub',capabilities)
    return  driver


def login():
    time.sleep(10)

    get_by_local=GetByLocal(driver)
    get_by_local.get_element('username').send_keys('17600695527')
    time.sleep(5)
    get_by_local.get_element('password').send_keys('123456')
    time.sleep(5)
    get_by_local.get_element('login_button').click()
    time.sleep(5)
def logout():
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/tv_tab_me').click()
    time.sleep(5)
    swipe_on('up')#上滑操作
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '设置')]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '退出登录')]").click()

#def mine_by_class():


#层级定位，找到定位目标最近的父级节点
def mine_by_node():
    time.sleep(10)
    element=driver.find_element_by_id('in.haojin.nearbymerchant:id/metab_tv_info')
    print element
    elements=element.find_element_by_class_name('android.widget.TextView')
    elements[4].click()

def mine_by_uiautomator():
    driver.find_element_by_android_uiautomator('new UiSelector().text(17600695527)')

def get_web_viem():
    time.sleep(6)
    driver.find_element_by_xpath("//android.widget.TextView[contains(@text, '点餐')]").click()
    time.sleep(5)
    driver.find_element_by_id('in.haojin.nearbymerchant:id/entry_tv_take_out_order').click()

 #  element=driver.find_element_by_id('in.haojin.nearbymerchant:id/message_tv_content')
 #  print element
    webview=driver.contexts#查看有几个窗
    print webview#[u'NATIVE_APP']原生
 #  driver.switch_to.default_content()

def get_toast():
    time.sleep(3)


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

driver=get_driver()
login()
#get_web_viem()
#mine_by_node()
#logout()

