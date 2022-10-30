from ..connections.SshConnection import ssh_connection
from networks.models.ExtremeSwitchModel import ExtremeSwitch
from networks.models.ExtremeSwitchConfigModel import ExtremeSwitchConfig
from networks.datas.ExtremeSwitchData import extreme_switch_get_all_data , extreme_switch_create_data
from networks.datas.ExtremeSwitchConfigData import extreme_switch_config_create_data
from datetime import datetime

def extreme_switch_all_task_sync():
    try:
        extremes = extreme_switch_get_all_data()
        for item in extremes:
            extreme_switch_get_config_sync(extreme_switch=item)
            extreme_switch_get_system_sync(extreme_switch=item)
            pass
    except:
        pass

def extreme_switch_get_config_sync(extreme_switch: ExtremeSwitch):
    try:
        get_output = ssh_connection(
            device_ip=extreme_switch.address,
            device_type="extreme",
            device_password=extreme_switch.systemuser.password,
            device_username=extreme_switch.systemuser.username,
            command="show configuration"
        )
        extreme_switch_config = ExtremeSwitchConfig()
        extreme_switch_config.name = extreme_switch.hostname + "_" + str(datetime.now())
        extreme_switch_config.text = get_output
        extreme_switch_config.extremeswitch = extreme_switch
        extreme_switch_config_create_data(extreme_switch_config=extreme_switch_config)
    except:
        pass

def extreme_switch_get_system_sync(extreme_switch: ExtremeSwitch):
    try:
        pass
    except:
        pass