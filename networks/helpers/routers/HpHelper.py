from ..connections.SshConnection import ssh_connection
from networks.models.HpSwitchModel import HpSwitch
from networks.models.HpSwitchConfigModel import HpSwitchConfig
from networks.datas.HpSwitchData import hp_switch_get_all_data , hp_switch_create_data
from networks.datas.HpSwitchConfigData import hp_switch_config_create_data
from datetime import datetime

def hp_switch_all_task_sync():
    try:
        hps = hp_switch_get_all_data()
        for item in hps:
            hp_switch_get_config_sync(hp_switch=item)
            hp_switch_get_system_sync(hp_switch=item)
            pass
    except:
        pass

def hp_switch_get_config_sync(hp_switch: HpSwitch):
    try:
        get_output = ssh_connection(
            device_ip=hp_switch.address,
            device_type="hp_procurve",
            device_password=hp_switch.systemuser.password,
            device_username=hp_switch.systemuser.username,
            command="show running-config"
        )
        hp_switch_config = HpSwitchConfig()
        hp_switch_config.name = hp_switch.hostname + "_" + str(datetime.now())
        hp_switch_config.text = get_output
        hp_switch_config.hpswitch = hp_switch
        hp_switch_config_create_data(hp_switch_config=hp_switch_config)
    except:
        pass

def hp_switch_get_system_sync(hp_switch: HpSwitch):
    try:
        pass
    except:
        pass