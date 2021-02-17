from Device import Device

device_ip = ["172.31.182.4", "172.31.182.5", "172.31.182.6", "172.31.182.7", "172.31.182.9", "172.31.182.3", "172.31.182.8"]
username = "admin"
password = "cisco"
path = " routr_info"

if __name__ == "__main__":
    d = Device(username, password, path, device_ip)
    
