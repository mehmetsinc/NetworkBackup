from ..connections.SshConnection import ssh_connection
from networks.models.DellSwitchModel import DellSwitch
from networks.models.DellSwitchConfigModel import DellSwitchConfig
from networks.datas.DellSwitchData import dell_switch_get_all_data
from networks.datas.DellSwitchConfigData import dell_switch_config_create_data
from datetime import datetime

def dell_switch_all_task_sync():
    try:
        dells = dell_switch_get_all_data()
        for item in dells:
            dell_switch_get_config_sync(dell_switch=item)
            dell_switch_get_system_sync(dell_switch=item)
            pass
    except:
        pass

def dell_switch_get_config_sync(dell_switch: DellSwitch):
    try:
        get_output = ssh_connection(
            device_ip=dell_switch.address,
            device_type="dell_os9",
            device_password=dell_switch.systemuser.password,
            device_username=dell_switch.systemuser.username,
            command="show running-config"
        )
        dell_switch_config = DellSwitchConfig()
        dell_switch_config.name = dell_switch.hostname + "_" + str(datetime.now())
        dell_switch_config.text = get_output
        dell_switch_config.dellswitch = dell_switch
        dell_switch_config_create_data(dell_switch_config=dell_switch_config)
    except:
        pass

def dell_switch_get_system_sync(dell_switch: DellSwitch):
    try:
        pass
    except:
        pass