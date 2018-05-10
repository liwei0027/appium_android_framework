#coding=utf-8
from dos_cmd import DosCmd
#获取设备信息
class Server:
    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        self.dos=DosCmd()
        devices_list=[]
        result_list=self.dos.excute_cmd_result('adb devices')
        if len(result_list)>=2:
            for i in result_list:
                if 'List' in i:
                    continue
                devices_info=i.split('\t')
                #判断设备是否有效
                if devices_info[1]=='device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

if __name__=='__main__':
    sever=Server()
    print sever.get_devices()
    