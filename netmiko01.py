from Device import Device
import create_config_file as create

device_ip = ["172.31.182.4", "172.31.182.5", "172.31.182.6", "172.31.182.7", "172.31.182.9", "172.31.182.3", "172.31.182.8"]
username = "admin"
password = "cisco"
command = ""

if __name__ == "__main__":
    print("Do you want to create config and delete file?")
    if input("please type create if you want: ") == "create":
        create.create()
        create.delete()
    command = input("you want to config or delete?: ")
    if command == "config":
        print("Please wait until success")
        path = "/home/devasc/Desktop/NPA.HW.netmiko/router_info"
        d = Device(username, password, path, device_ip)
        d.config()
        print("Success")
    elif command == "delete":
        print("Please wait until success")
        path = "/home/devasc/Desktop/NPA.HW.netmiko/delete_config"
        d = Device(username, password, path, device_ip)
        d.delete_config()
        print("Success")
    else:
        print("command error")
    check = input("You want to save config? [y/n]: ")
    if check == "y":
        d = Device(username, password, path, device_ip)
        print("System is saving.......")
        d.save()
        print("Done")
    elif check == "n":
        print("Done")
        pass 
    
