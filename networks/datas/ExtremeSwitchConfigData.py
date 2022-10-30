from ..models.ExtremeSwitchConfigModel import ExtremeSwitchConfig

def extreme_switch_config_get_all_data():
    try:
        return ExtremeSwitchConfig.objects.all()
    except:
        pass

def extreme_switch_config_get_by_extreme_all_data(extreme_switch):
    try:
        return ExtremeSwitchConfig.objects.filter(extremeswitch=extreme_switch)
    except:
        pass

def extreme_switch_config_get_by_id_data(extreme_switch_config_id: int):
    try:
        return ExtremeSwitchConfig.objects.get(id=extreme_switch_config_id)
    except:
        pass

def extreme_switch_config_create_data(extreme_switch_config: ExtremeSwitchConfig):
    try:
        extreme_switch_config.save()
    except:
        pass

def extreme_switch_config_delete_data(extreme_switch_config_id: int):
    try:
        extreme_switch_config = ExtremeSwitchConfig.objects.get(id=extreme_switch_config_id)
        extreme_switch_config.delete()
    except:
        pass