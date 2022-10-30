from networks.models.SystemUserModel import SystemUser


def system_user_get_by_id_data(system_user_id):
    try:
        get_system_user = SystemUser.objects.get(id=system_user_id)
        return get_system_user
    except:
        pass

def system_user_get_all_data():
    try:
        return SystemUser.objects.all()
    except:
        pass


def system_user_create_data(system_user: SystemUser):
    try:
        system_user.save()
    except:
        pass

def system_user_remove_data(system_user_id):
    try:
        get_system_user = SystemUser.objects.get(id=system_user_id)
        get_system_user.delete()
    except:
        pass

