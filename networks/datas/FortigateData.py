from ..models.FortigateModel import Fortigate

def fortigate_get_all_data():
    try:
        return Fortigate.objects.all()
    except:
        pass

def fortigate_get_by_id_data(fortigate_id: int):
    try:
        return Fortigate.objects.get(id=fortigate_id)
    except:
        pass

def fortigate_create_data(fortigate: Fortigate):
    try:
        fortigate.save()
    except:
        pass

def fortigate_delete_data(fortigate_id: int):
    try:
        fortigate = Fortigate.objects.get(id=fortigate_id)
        fortigate.delete()
    except:
        pass