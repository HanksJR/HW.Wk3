from Device import Device
import create_config_file as create

device_ip = ["172.31.182.4", "172.31.182.5", "172.31.182.6", "172.31.182.7", "172.31.182.9", "172.31.182.3", "172.31.182.8"]
username = "admin"
password = "cisco"
command = ""

if __name__ == "__main__":
    if input() == "create":
        create.create()
        create.delete()
    command = input()
    if command == "config":
        path = "/home/devasc/Desktop/NPA.HW.netmiko/router_info"
        d = Device(username, password, path, device_ip)
        d.config()
        print("Success")
    elif command == "delete":
        path = "/home/devasc/Desktop/NPA.HW.netmiko/delete_config"
        d = Device(username, password, path, device_ip)
        d.delete_config()
        print("Success")
    else:
        print("command error")
    
