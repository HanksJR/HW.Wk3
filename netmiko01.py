from netmiko import ConnectHandler

username = 'admin'
password = 'cisco'
device_ip = ['172.31.182.4','172.31.182.5','172.31.182.6','172.31.182.7','172.31.182.9']

R1 = {
        'hostname': 'R1',
        'device_ip': device_ip[0],
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
                ],
        'routing':[
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.16',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.32',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.20.182.4',
                        'wildcard': '0.0.0.0',
                        'area' : '0'
                    },
        ]
    }

R2 = {
        'hostname': 'R2',
        'device_ip': device_ip[1],
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
                ],
        'routing':[
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.16',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.48',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.20.182.5',
                        'wildcard': '0.0.0.0',
                        'area' : '0'
                    },
        ]
    }

R3 = {
        'hostname': 'R3',
        'device_ip': device_ip[2],
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
                ],
        'routing':[
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.32',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.48',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.64',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.20.182.6',
                        'wildcard': '0.0.0.0',
                        'area' : '0'
                    },
        ]
    }   
R4 = {
        'hostname': 'R4',
        'device_ip': device_ip[3],
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
                ],
        'routing':[
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.64',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.20.182.7',
                        'wildcard': '0.0.0.0',
                        'area' : '0'
                    },
        ]
    }
        

R5 = {
        'hostname': 'R5',
        'device_ip': device_ip[4],
        'info': [ 
                    {
                        'interface': 'g0/1',
                        'ip': '172.31.182.67',
                        'netmask': '255.255.255.240'
                    },
                    {
                        'interface': 'g0/2',
                        'ip': 'dhcp',
                        'netmask': ''
                    },
                    {
                        'interface': "lo0",
                        'ip': "172.20.182.9",
                        'netmask': "255.255.255.255"
                    }
                ],
        'routing':[
                    {
                        'protocol': 'ospf 1',
                        'network': '172.31.182.64',
                        'wildcard': '0.0.0.15',
                        'area' : '0'
                    },
                    {
                        'protocol': 'ospf 1',
                        'network': '172.20.182.9',
                        'wildcard': '0.0.0.0',
                        'area' : '0'
                    },
        ]
    }

all_device = [R1, R2, R3, R4, R5]

def main():
    for dev in all_device:
        config_interface(dev)
        routing(dev)
    
def config(iface, ip, netmask):
    interface_config = [
        "interface {}".format(iface),
        "ip address {} {}".format(ip, netmask)]
    return interface_config

def config_interface(device):
    ip = device["device_ip"]
    name = device["hostname"]
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
    
    write_file(name+"_config_interface.txt", save_show_interface_brief(ip))

def save_show_interface_brief(ip):
    device_params = {'device_type': 'cisco_ios',
                    'ip': ip,
                    'username': username,
                    'password': password,
                    }

    with ConnectHandler(**device_params) as ssh:
        interface = ssh.send_command('sh ip int br')
        ssh.disconnect()
    
    return interface

def routing(device):
    ip = device["device_ip"]
    name = device["hostname"]
    for route in device["routing"]:
        routing = [
            "router {}".format(route["protocol"]),
            "network {} {} area {}".format(route["network"], route["wildcard"], route["area"])]
        
        device_params = {'device_type': 'cisco_ios',
                        'ip': ip,
                        'username': username,
                        'password': password,
                        }

        with ConnectHandler(**device_params) as ssh:
            ssh.send_config_set(routing)
            ssh.disconnect()

    write_file(name+"_routing.txt", save_show_ip_route(ip))

def save_show_ip_route(ip):
    device_params = {'device_type': 'cisco_ios',
                        'ip': ip,
                        'username': username,
                        'password': password,
                        }
    with ConnectHandler(**device_params) as ssh:
        info = ssh.send_command('sh ip route')
        ssh.disconnect()
    return info

def write_file(name, text):
    with open(name, 'w') as f:
        f.write(text)
        f.close()
main()