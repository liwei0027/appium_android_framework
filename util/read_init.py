#coding=utf-8
import ConfigParser#configParser 模块用于操作配置文件

class ReadIni:
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path='D:/PycharmProjects/appium_android_framework/config/LocalElement.ini'
        else:
            self.file_path=file_path
        self.data=self.read_ini()


    def read_ini(self):
        read_ini = ConfigParser.ConfigParser()
        read_ini.read(self.file_path)  # 读取配置文件
     #  print read_ini.get('login_element', 'username')
        return read_ini

    def get_sections(self):
        '''
        获取所有sections
        :return:
        '''
        sections=self.data.sections()
        return sections
    #通过key获取对应的value
    # def get_value(self,key,section=None):
    #     if section==None:
    #         section='login_element'
    #     try:
    #         value=self.data.get(section,key)
    #     except:
    #         value=None
    #     return value
    def get_value(self,key):
        sections=self.data.sections()
        for i in range(len(sections)):
           # print sections[i]
            try:
                value = self.data.get(sections[i], key)
                break
            except:
                value = None
        return value


if __name__=='__main__':
    read_ini=ReadIni()
   # print read_ini.get_value("delPhone")
   # print read_ini.get_value("允许软件后台自启动")