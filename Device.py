import os, yaml
from netmiko import ConnectHandler

class Device:
    
    def __init__(self, username, password, path, ip):
        self.username = username
        self.password = password
        self.path = path
        self.device = ["R1_config.txt", "R2_config.txt", "R3_config.txt", "R4_config.txt", "R5_config.txt", "S1_config.txt", "S2_config.txt", ]
        self.ip = ip

    def config(self):
        counter = 0
        for dev in self.device:
            device_params = {'device_type': 'cisco_ios',
                                'ip': self.ip[counter],
                                'username': self.username,
                                'password': self.password,
                                }
            with ConnectHandler(**device_params) as ssh:
                ssh.send_config_from_file("{}/{}".format(self.path, dev))
                info = ssh.send_command("sh run")
                devices = yaml.load(open('config_info.yaml'), Loader=yaml.FullLoader)
                self.write_file(info, "/home/devasc/Desktop/NPA.HW.netmiko/information/{}_info.txt".format(devices[counter]["name"]))
            counter += 1

    def delete_config(self):
        counter = 0
        for dev in self.device:
            device_params = {'device_type': 'cisco_ios',
                                'ip': self.ip[counter],
                                'username': self.username,
                                'password': self.password,
                                }
            with ConnectHandler(**device_params) as ssh:
                ssh.send_config_from_file("{}/{}".format(self.path, dev))
                info = ssh.send_command("sh run")
                devices = yaml.load(open('config_info.yaml'), Loader=yaml.FullLoader)
                self.write_file(info, "/home/devasc/Desktop/NPA.HW.netmiko/information/{}_info.txt".format(devices[counter]["name"]))
            counter += 1

    def write_file(self, info, name):
        with open(name, "w") as f:
            f.write(info)

    def save():
        counter = 0
        for dev in self.device:
            device_params = {'device_type': 'cisco_ios',
                                'ip': self.ip[counter],
                                'username': self.username,
                                'password': self.password,
                                }
            with ConnectHandler(**device_params) as ssh:
                ssh.save_config()
        counter += 1
                