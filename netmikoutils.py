from netmiko import ConnectHandler

#Describes a device to be used with netmiko
def def_device(type: str, hostname:str, username:str, password:str):
    device = {
        'device_type': type,
        'host': hostname, #hostname or IP address
        'username': username,
        'password': password,
    }
    return device

#Prints results of command(s) sent to device(s)
def printCommandRes(device_list: list, command_res_list: list):
    i=0
    for device in device_list:
        print(f"**************{device['host']}***************")
        print(command_res_list[i])
        i+=1

#Sends a list of commands to a list of devices and returns a list with the results
def sendCommands(devices: list, commands: list):
    results = []
    for device in devices:
        conn = ConnectHandler(**device)
        results.append(conn.send_config_set(commands)) 
    return results  #Return a list with results of commands sent to each device

#Sends a list of commands to a list of devices, and prints the output
def sendAndPrint(devices: list, commands: list):
    res = sendCommands(devices, commands)
    printCommandRes(devices, res)
