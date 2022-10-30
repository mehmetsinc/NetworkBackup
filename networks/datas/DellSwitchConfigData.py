from ..models.DellSwitchConfigModel import DellSwitchConfig

def dell_switch_config_get_all_data():
    try:
        return DellSwitchConfig.objects.all()
    except:
        pass

def dell_switch_config_get_by_dell_all_data(dell_switch):
    try:
        return DellSwitchConfig.objects.filter(dellswitch=dell_switch)
    except:
        pass

def dell_switch_config_get_by_id_data(dell_switch_config_id: int):
    try:
        return DellSwitchConfig.objects.get(id=dell_switch_config_id)
    except:
        pass

def dell_switch_config_create_data(dell_switch_config: DellSwitchConfig):
    try:
        dell_switch_config.save()
    except:
        pass

def dell_switch_config_delete_data(dell_switch_config_id: int):
    try:
        dell_switch_config = DellSwitchConfig.objects.get(id=dell_switch_config_id)
        dell_switch_config.delete()
    except:
        pass