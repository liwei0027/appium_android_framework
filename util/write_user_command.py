#coding=utf-8
import yaml
class WriteUserCommand:
    def read_data(self):
        '''
        加载yaml数据
        :return:
        '''
        with open("D:/PycharmProjects/appium_android_framework/config/userconfig.yaml") as fr:
            data=yaml.load(fr)
        return data


    def get_value(self,key,port):
        '''
        获取value
        :return:
        '''
        data=self.read_data()
        value=data[key][port]
        return value

    def write_data(self,i,device,bp,port):
        '''
        写入数据
        :return:
        '''
        data=self.join_data(i,device,bp,port)
        with open("D:/PycharmProjects/appium_android_framework/config/userconfig.yaml","a") as fr:
            yaml.dump(data,fr)

    def join_data(self,i,device,bp,port):
        '''
        拼接数据
        :return:
        '''
        data={
        "user_info_"+str(i):{
        "deviceName":device,
        "bp":bp,
        "port":port
        }
        }
        return data

    def clear_data(self):
        with open("D:/PycharmProjects/appium_android_framework/config/userconfig.yaml", "w") as fr:
            fr.truncate()
        fr.close()
    def get_file_lines(self):
        '''
        获取数据行数
        :return:
        '''
        data=self.read_data()
        return len(data)

if __name__=='__main__':
    write_file=WriteUserCommand()
#    print write_file.get_value('user_info_2','bp')