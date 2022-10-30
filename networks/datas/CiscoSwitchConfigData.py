from ..models.CiscoSwitchConfigModel import CiscoSwitchConfig

def cisco_switch_config_get_all_data():
    try:
        return CiscoSwitchConfig.objects.all()
    except:
        pass

def cisco_switch_config_get_by_fortigate_all_data(cisco_switch):
    try:
        return CiscoSwitchConfig.objects.filter(ciscoswitch=cisco_switch)
    except:
        pass

def cisco_switch_config_get_by_id_data(cisco_switch_config_id: int):
    try:
        return CiscoSwitchConfig.objects.get(id=cisco_switch_config_id)
    except:
        pass

def cisco_switch_config_create_data(cisco_switch_config: CiscoSwitchConfig):
    try:
        cisco_switch_config.save()
    except:
        pass

def cisco_switch_config_delete_data(cisco_switch_config_id: int):
    try:
        cisco_switch_config = CiscoSwitchConfig.objects.get(id=cisco_switch_config_id)
        cisco_switch_config.delete()
    except:
        pass