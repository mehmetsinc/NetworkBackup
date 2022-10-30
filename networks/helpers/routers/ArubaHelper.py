from ..connections.SshConnection import ssh_connection
from networks.models.ArubaSwitchModel import ArubaSwitch
from networks.models.ArubaSwitchConfigModel import ArubaSwitchConfig
from networks.datas.ArubaSwitchData import aruba_switch_get_all_data , aruba_switch_create_data
from networks.datas.ArubaSwitchConfigData import aruba_switch_config_create_data
from datetime import datetime

def aruba_switch_all_task_sync():
    try:
        arubas = aruba_switch_get_all_data()
        for item in arubas:
            aruba_switch_get_config_sync(aruba_switch=item)
            aruba_switch_get_system_sync(aruba_switch=item)
            pass
    except:
        pass

def aruba_switch_get_config_sync(aruba_switch: ArubaSwitch):
    try:
        get_output = ssh_connection(
            device_ip=aruba_switch.address,
            device_type="hp_procurve",
            device_password=aruba_switch.systemuser.password,
            device_username=aruba_switch.systemuser.username,
            command="show running-config"
        )
        aruba_switch_config = ArubaSwitchConfig()
        aruba_switch_config.name = aruba_switch.hostname + "_" + str(datetime.now())
        aruba_switch_config.text = get_output
        aruba_switch_config.arubaswitch = aruba_switch
        aruba_switch_config_create_data(aruba_switch_config=aruba_switch_config)
    except:
        pass

def aruba_switch_get_system_sync(aruba_switch: ArubaSwitch):
    try:
        get_output = ssh_connection(
            device_ip=aruba_switch.address,
            device_type="hp_procurve",
            device_password=aruba_switch.systemuser.password,
            device_username=aruba_switch.systemuser.username,
            command="show system"
        )
        for item in get_output.splitlines():
            if "System Name" in item:
                name = item.split()
                name.pop(0)
                name.pop(0)
                name.pop(0)
                aruba_switch.hostname = name[0]
            if "Software revision" in item:
                version = item.split()
                version.pop(0)
                version.pop(0)
                version.pop(0)
                version.pop(1)
                version.pop(1)
                version.pop(1)
                version.pop(1)
                aruba_switch.version = version[0]
            if "ROM Version" in item:
                serial = item.split()
                serial.pop(0)
                serial.pop(0)
                serial.pop(0)
                serial.pop(0)
                serial.pop(0)
                serial.pop(0)
                serial.pop(0)
                aruba_switch.serial = serial

        aruba_switch_create_data(aruba_switch=aruba_switch)
    except:
        pass