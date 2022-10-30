from ..models.HpSwitchConfigModel import HpSwitchConfig

def hp_switch_config_get_all_data():
    try:
        return HpSwitchConfig.objects.all()
    except:
        pass

def hp_switch_config_get_by_hp_all_data(hp_switch):
    try:
        return HpSwitchConfig.objects.filter(hpswitch=hp_switch)
    except:
        pass

def hp_switch_config_get_by_id_data(hp_switch_config_id: int):
    try:
        return HpSwitchConfig.objects.get(id=hp_switch_config_id)
    except:
        pass

def hp_switch_config_create_data(hp_switch_config: HpSwitchConfig):
    try:
        hp_switch_config.save()
    except:
        pass

def hp_switch_config_delete_data(hp_switch_config_id: int):
    try:
        hp_switch_config = HpSwitchConfig.objects.get(id=hp_switch_config_id)
        hp_switch_config.delete()
    except:
        pass