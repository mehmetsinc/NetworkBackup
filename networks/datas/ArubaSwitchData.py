from ..models.ArubaSwitchModel import ArubaSwitch


def aruba_switch_get_all_data():
    try:
        return ArubaSwitch.objects.all()
    except:
        pass

def aruba_switch_get_by_id_data(aruba_switch_id: int):
    try:
        return ArubaSwitch.objects.get(id=aruba_switch_id)
    except:
        pass

def aruba_switch_create_data(aruba_switch: ArubaSwitch):
    try:
        aruba_switch.save()
    except:
        pass

def aruba_switch_delete_data(aruba_switch_id: int):
    try:
        aruba_switch = ArubaSwitch.objects.get(id=aruba_switch_id)
        aruba_switch.delete()
    except:
        pass