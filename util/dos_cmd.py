#coding=utf-8

#执行dos命令获取设备信息
import os
#print os.system('adb devices')
#print os.popen('adb devices').readlines()
class DosCmd:
    def excute_cmd_result(self,command):
        result_list=[]
        result=os.popen(command).readlines()
        for i in result:
            if i=='\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list
    def excute_cmd(self):
        os.system('adb devices')
if __name__=='__main__':
    dos=DosCmd()
    print dos.excute_cmd_result('adb devices')

