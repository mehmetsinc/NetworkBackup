from ..connections.SshConnection import ssh_connection
from networks.models.FortigateModel import Fortigate
from networks.models.FortigateConfigModel import FortigateConfig
from networks.datas.FortigateConfigData import fortigate_config_create_data
from networks.datas.FortigateData import fortigate_create_data, fortigate_get_all_data
from datetime import datetime


def fortigate_all_task_sync():
    try:
        fortigates = fortigate_get_all_data()
        for item in fortigates:
            fortigate_get_system_sync(fortigate=item)
            fortigate_get_config_sync(fortigate=item)
    except:
        pass


def fortigate_get_system_sync(fortigate: Fortigate):

    try:
        get_output = ssh_connection(
            device_ip=fortigate.address,
            device_type="fortinet",
            device_password=fortigate.systemuser.password,
            device_username=fortigate.systemuser.username,
            command="get system status"
        )

        output_splitlines = get_output.splitlines()
        for item in output_splitlines:
            item_split = item.split()

            if "Version:" in item_split:
                fortigate.model = item_split[1]
                fortigate.version = item_split[2]
            if "Serial-Number:" in item_split:
                fortigate.serial = item_split[1]
            if "Hostname:" in item_split:
                fortigate.hostname = item_split[1]

        fortigate_create_data(fortigate=fortigate)
    except:
        pass

def fortigate_get_config_sync(fortigate: Fortigate):
    try:
        get_output = ssh_connection(
            device_ip=fortigate.address,
            device_type="fortinet",
            device_password=fortigate.systemuser.password,
            device_username=fortigate.systemuser.username,
            command="show full-configuration"
        )
        fortigate_config = FortigateConfig()
        fortigate_config.name = fortigate.hostname + "_" + str(datetime.now())
        fortigate_config.text = get_output
        fortigate_config.fortigate = fortigate
        fortigate_config_create_data(fortigate_config=fortigate_config)
    except:
        pass
