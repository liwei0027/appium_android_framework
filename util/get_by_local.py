#coding=utf-8
from read_init import ReadIni
#定位信息
class GetByLocal:
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        #id>in.haojin.nearbymerchant:id/et_phoneNum
        read_ini=ReadIni()
        local=read_ini.get_value(key)
        if local!=None:

            by=local.split('>')[0]
            local_by=local.split('>')[1]
            try:
                if by=='id':
                    return self.driver.find_element_by_id(local_by)
                elif by=='classname':
                    return self.driver.find_element_by_class_name(local_by)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                return None
        else:
            return None
