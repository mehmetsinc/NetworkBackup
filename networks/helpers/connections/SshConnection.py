import os
from netmiko import ConnectHandler

def ssh_connection(
        device_ip: str,
        device_username: str,
        device_password: str,
        command: str,
        device_type: str):
    try:
        devices = {
            'device_type': device_type,
            'ip': device_ip,
            'username': device_username,
            'password': device_password
        }
        response = os.system("ping -c 2 " + device_ip)
        if response == 0:
            net_connect = ConnectHandler(**devices)
            output = net_connect.send_command(command)
            net_connect.disconnect()
            if output is not None:
                return output
            else:
                pass
        else:
            pass

    except:
        pass

