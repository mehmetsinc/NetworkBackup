from ..models.HpSwitchModel import HpSwitch


def hp_switch_get_all_data():
    try:
        return HpSwitch.objects.all()
    except:
        pass

def hp_switch_get_by_id_data(hp_switch_id: int):
    try:
        return HpSwitch.objects.get(id=hp_switch_id)
    except:
        pass

def hp_switch_create_data(hp_switch: HpSwitch):
    try:
        hp_switch.save()
    except:
        pass

def hp_switch_delete_data(hp_switch_id: int):
    try:
        hp_switch = HpSwitch.objects.get(id=hp_switch_id)
        hp_switch.delete()
    except:
        pass