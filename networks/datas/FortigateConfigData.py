from ..models.FortigateConfigModel import FortigateConfig

def fortigate_config_get_all_data():
    try:
        return FortigateConfig.objects.all()
    except:
        pass

def fortigate_config_get_by_fortigate_all_data(fortigate):
    try:
        return FortigateConfig.objects.filter(fortigate=fortigate)
    except:
        pass

def fortigate_config_get_by_id_data(fortigate_config_id: int):
    try:
        return FortigateConfig.objects.get(id=fortigate_config_id)
    except:
        pass

def fortigate_config_create_data(fortigate_config: FortigateConfig):
    try:
        fortigate_config.save()
    except:
        pass

def fortigate_config_delete_data(fortigate_config_id: int):
    try:
        fortigate_config = FortigateConfig.objects.get(id=fortigate_config_id)
        fortigate_config.delete()
    except:
        pass