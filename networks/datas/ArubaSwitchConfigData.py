from ..models.ArubaSwitchConfigModel import ArubaSwitchConfig

def aruba_switch_config_get_all_data():
    try:
        return ArubaSwitchConfig.objects.all()
    except:
        pass

def aruba_switch_config_get_by_aruba_all_data(aruba_switch):
    try:
        return ArubaSwitchConfig.objects.filter(arubaswitch=aruba_switch)
    except:
        pass

def aruba_switch_config_get_by_id_data(aruba_switch_config_id: int):
    try:
        return ArubaSwitchConfig.objects.get(id=aruba_switch_config_id)
    except:
        pass

def aruba_switch_config_create_data(aruba_switch_config: ArubaSwitchConfig):
    try:
        aruba_switch_config.save()
    except:
        pass

def aruba_switch_config_delete_data(aruba_switch_config_id: int):
    try:
        aruba_switch_config = ArubaSwitchConfig.objects.get(id=aruba_switch_config_id)
        aruba_switch_config.delete()
    except:
        pass