from ..models.CiscoSwitchModel import CiscoSwitch


def cisco_switch_get_all_data():
    try:
        return CiscoSwitch.objects.all()
    except:
        pass

def cisco_switch_get_by_id_data(cisco_switch_id: int):
    try:
        return CiscoSwitch.objects.get(id=cisco_switch_id)
    except:
        pass

def cisco_switch_create_data(cisco_switch: CiscoSwitch):
    try:
        cisco_switch.save()
    except:
        pass

def cisco_switch_delete_data(cisco_switch_id: int):
    try:
        cisco_switch = CiscoSwitch.objects.get(id=cisco_switch_id)
        cisco_switch.delete()
    except:
        pass