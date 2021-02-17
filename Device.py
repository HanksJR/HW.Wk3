import os, yaml, create_config_file
from netmiko import ConnectHandler

class Device:
    
    def __init__(self, username, password, path, ip):
        self.username = username
        self.password = password
        self.device = self.create_list(path)
        self.ip = ip
        create_config_file.create()
        create_config_file.delete()
        self.config()

    def create_list(self, path):
        lis = []
        for file in os.listdir(path):
            if file.endswith(".txt"):
                lis.append(file)
        return lis

    def config(self):
        counter = 0
        for dev in self.device:
            device_params = {'device_type': 'cisco_ios',
                                'ip': self.ip[counter],
                                'username': self.username,
                                'password': self.password,
                                }
            with ConnectHandler(**device_params) as ssh:
                ssh.send_config_from_file(dev)
                info = ssh.send_command("sh run")
                devices = yaml.load(open('config_info.yaml'), Loader=yaml.FullLoader)
                self.write_file(info, "information/{}_info.txt".format(devices[counter]["name"]))

    def delete_config(self):
        counter = 0
        for dev in self.device:
            device_params = {'device_type': 'cisco_ios',
                                'ip': self.ip[counter],
                                'username': self.username,
                                'password': self.password,
                                }
            with ConnectHandler(**device_params) as ssh:
                ssh.send_config_from_file(dev)
                info = ssh.send_command("sh run")
                devices = yaml.load(open('config_info.yaml'), Loader=yaml.FullLoader)
                self.write_file(info, "information/{}_info.txt".format(devices[counter]["name"]))

    def write_file(self, info, name):
        with open(name, "w") as f:
            f.write(info)
