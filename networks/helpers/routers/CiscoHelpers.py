from ..connections.SshConnection import ssh_connection
from networks.models.CiscoSwitchModel import CiscoSwitch
from networks.models.CiscoSwitchConfigModel import CiscoSwitchConfig
from networks.datas.CiscoSwitchConfigData import cisco_switch_config_create_data
from networks.datas.CiscoSwitchData import cisco_switch_get_all_data
from datetime import datetime

def cisco_switch_all_task_sync():
    try:
        fortigates = cisco_switch_get_all_data()
        for item in fortigates:
            cisco_switch_get_config_sync(cisco_switch=item)
            cisco_switch_get_system_sync(cisco_switch=item)
            pass
    except:
        pass

def cisco_switch_get_config_sync(cisco_switch: CiscoSwitch):
    try:
        get_output = ssh_connection(
            device_ip=cisco_switch.address,
            device_type="cisco_ios",
            device_password=cisco_switch.systemuser.password,
            device_username=cisco_switch.systemuser.username,
            command="show running-config"
        )
        cisco_switch_config = CiscoSwitchConfig()
        cisco_switch_config.name = cisco_switch.hostname + "_" + str(datetime.now())
        cisco_switch_config.text = get_output
        cisco_switch_config.ciscoswitch = cisco_switch
        cisco_switch_config_create_data(cisco_switch_config=cisco_switch_config)
    except:
        pass


def cisco_switch_get_system_sync(cisco_switch: CiscoSwitch):
    try:
        pass
    except:
        pass