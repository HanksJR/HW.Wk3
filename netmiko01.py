from netmiko import ConnectHandler

username = 'admin'
password = 'cisco'
device_ip = ['172.31.182.4','172.31.182.5','172.31.182.6','172.31.182.7','172.31.182.8','172.31.182.9']
R1 = {
        'device_ip': '172.31.182.4',
        'info' :[
                    {
                        'interface': "g0/1",
                        'ip': "172.31.182.17",
                        'netmask': "255.255.255.240"
                    },
                    {
                        'interface': "g0/2",
                        'ip': "172.31.182.33",
                        'netmask': "255.255.255.240"
                    },
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.4",
                        'netmask': "255.255.255.255"
                    }
                ]
    }

R2 = {
        'device_ip': '172.31.182.5',
        'info': [
                    {
                        'interface': 'g0/1',
                        'ip': '172.31.182.18',
                        'netmask': '255.255.255.240'
                    },
                    {
                        'interface': 'g0/2',
                        'ip': '172.31.182.49',
                        'netmask': '255.255.255.240'
                    },
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.5",
                        'netmask': "255.255.255.255"
                    }
                ]
    }

R3 = {
        'device_ip': '172.31.182.6',
        'info' :[
                    {
                        'interface': "g0/1",
                        'ip': "172.31.182.34",
                        'netmask': "255.255.255.240"
                    },
                    {
                        'interface': "g0/2",
                        'ip': "172.31.182.50",
                        'netmask': "255.255.255.240"
                    },
                    {
                        'interface': "g0/3",
                        'ip': "172.31.182.65",
                        'netmask': "255.255.255.240"
                    },
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.6",
                        'netmask': "255.255.255.255"
                    }    
                ]
    }   
R4 = {
        'device_ip': '172.31.182.7',
        'info': [
                    {
                        'interface': 'g0/1',
                        'ip': '172.31.182.66',
                        'netmask': '255.255.255.240'
                    },
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.7",
                        'netmask': "255.255.255.255"
                    }
                ]
    }
        

R5 = {
        'device_ip': '172.31.182.9',
        'info': [ 
                    {
                        'interface': 'g0/1',
                        'ip': '172.31.182.67',
                        'netmask': '255.255.255.240'
                    },
                    {
                        'interface': 'g0/2',
                        'ip': 'dhcp'
                    },
                    ,
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.9",
                        'netmask': "255.255.255.255"
                    }
                ]
    }

all_device = [R1, R2, R3, R4, R5]

def main():
    config_interface_all(device_ip)
    for dev in all_device:
        config_interface(dev)
    
def config(iface, ip, netmask):
    interface_config = [
        "interface {}".format(iface),
        "ip address {} {}".format(ip, netmask)]
    return interface_config

def config_interface(device):
    ip = device["device_ip"]
    for router in device["info"]:
        cfg = config(router["interface"], router["ip"], router["netmask"])
        cfg.append("no shutdown")
        device_params = {'device_type': 'cisco_ios',
                        'ip': ip,
                        'username': username,
                        'password': password,
                        }

        with ConnectHandler(**device_params) as ssh:
            ssh.send_config_set(cfg)
            ssh.disconnect()
    print(show_interface_brief(ip))

def show_interface_brief(ip):
    device_params = {'device_type': 'cisco_ios',
                    'ip': ip,
                    'username': username,
                    'password': password,
                    }

    with ConnectHandler(**device_params) as ssh:
        interface = ssh.send_command('sh ip int br')
        ssh.disconnect()
    return interface
main()