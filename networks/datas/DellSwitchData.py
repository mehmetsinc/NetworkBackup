from ..models.DellSwitchModel import DellSwitch


def dell_switch_get_all_data():
    try:
        return DellSwitch.objects.all()
    except:
        pass

def dell_switch_get_by_id_data(dell_switch_id: int):
    try:
        return DellSwitch.objects.get(id=dell_switch_id)
    except:
        pass

def dell_switch_create_data(dell_switch: DellSwitch):
    try:
        dell_switch.save()
    except:
        pass

def dell_switch_delete_data(dell_switch_id: int):
    try:
        dell_switch = DellSwitch.objects.get(id=dell_switch_id)
        dell_switch.delete()
    except:
        pass