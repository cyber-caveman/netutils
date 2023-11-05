#v1.1
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
def print_command_res(device_list: list, command_res_dict: dict):
    for device, device_results in command_res_dict.items():
        print(f"**********{device}**********")
        for command, result in device_results.items():
            print(f"{command}:\n{result}")

#Sends a list of commands to a list of devices and returns a dictionary with the results
#Order of hierarchy is device -> command -> result_of_command.
#So you can query any result from any command issued to any device in the list like this: result_var['<device>']['<command>']
def send_commands(devices: list, commands: list):
    results = {}
    
    for device in devices:
        conn = ConnectHandler(**device)
        device_results = {}
        for command in commands:
            res = conn.send_command(command)
            device_results[command] = res
        results[device['host']] = device_results
        conn.disconnect()
    return results  #Return a dictionary with results of commands sent to each device

#Sends a list of commands to a list of devices, and prints the output
def send_and_print(devices: list, commands: list):
    res = send_commands(devices, commands)
    print_command_res(devices, res)
