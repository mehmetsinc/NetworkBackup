from ..models.ExtremeSwitchModel import ExtremeSwitch


def extreme_switch_get_all_data():
    try:
        return ExtremeSwitch.objects.all()
    except:
        pass

def extreme_switch_get_by_id_data(extreme_switch_id: int):
    try:
        return ExtremeSwitch.objects.get(id=extreme_switch_id)
    except:
        pass

def extreme_switch_create_data(extreme_switch: ExtremeSwitch):
    try:
        extreme_switch.save()
    except:
        pass

def extreme_switch_delete_data(extreme_switch_id: int):
    try:
        extreme_switch = ExtremeSwitch.objects.get(id=extreme_switch_id)
        extreme_switch.delete()
    except:
        pass