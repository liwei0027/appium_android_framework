#coding=utf-8
from dos_cmd import DosCmd
from port import Port
import threading
from write_user_command import WriteUserCommand
import time
#获取设备信息
class Server:
    def __init__(self):
        self.dos = DosCmd()
    def get_devices(self):
        """
        获取设备信息
        :return:
        """
        devices_list=[]
        result_list=self.dos.excute_cmd_result('adb devices')#['List of devices attached', '37b34d04\tdevice']
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
    def create_port_list(self,start_port):
        """
        创建可用端口
        :return:
        """
        port=Port()
        port_list=[]
        port_list=port.create_port_list(start_port,self.get_devices())
        return port_list

    def create_command_list(self):
        #appium -p 4700 -bp 4701 -u 37b34d04
        write_file=WriteUserCommand()
        command_list=[]
        appium_port_list=self.create_port_list(4700)
        bootstrap_port_list=self.create_port_list(4900)
        device_list=self.get_devices()
        for i in range(len(device_list)):
            command="appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+" --no-reset --session-override"
            command_list.append(command)
            write_file.write_data(i,device_list[i],str(bootstrap_port_list[i]),str(appium_port_list[i]))
        return command_list
    def start_server(self,i):
        self.start_list=self.create_command_list()
        self.dos.excute_cmd(self.start_list[i])

    def kill_server(self):
        server_list=self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list)>0:
            self.dos.excute_cmd('taskkill -F -PID node.exe')



    def main(self):
        self.kill_server()
        for i in range(len(self.create_command_list())):
            appium_start=threading.Thread(target=self.start_server,args=(i,))
            appium_start.start()


if __name__=='__main__':
    sever=Server()
    print sever.main()
