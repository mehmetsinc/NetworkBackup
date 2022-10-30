from networks.models.HpSwitchModel import HpSwitch
from networks.datas.SystemUserData import system_user_get_all_data, system_user_get_by_id_data
from django.shortcuts import render, redirect
from networks.datas.HpSwitchConfigData import hp_switch_config_get_by_hp_all_data, hp_switch_config_get_by_id_data, hp_switch_config_delete_data
from networks.datas.HpSwitchData import hp_switch_get_all_data, hp_switch_create_data,hp_switch_delete_data , hp_switch_get_by_id_data
from networks.helpers.routers.HpHelper import hp_switch_all_task_sync, hp_switch_get_config_sync, hp_switch_get_system_sync



def hp_switch_view(request):

    hp_switcies = hp_switch_get_all_data()
    return render(request, 'pages/network/hp/index.html', context={
        'hp_switcies': hp_switcies
    })

def hp_switch_create_view(request):
    if request.POST:
        get_hp_switch = HpSwitch()
        get_hp_switch.hostname = request.POST["hostname"]
        get_hp_switch.vendor = "Hp"
        get_hp_switch.model = request.POST["model"]
        get_hp_switch.address = request.POST["address"]
        get_hp_switch.serial = request.POST["serial"]
        get_hp_switch.version = request.POST["version"]
        get_hp_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        hp_switch_create_data(get_hp_switch)
        return redirect("hp_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/hp/create.html', context={
            "system_users": get_system_users
        })

def hp_switch_update_view(request, id):
    get_hp_switch = hp_switch_get_by_id_data(hp_switch_id=id)
    if request.POST:
        get_hp_switch.hostname = request.POST["hostname"]
        get_hp_switch.model = request.POST["model"]
        get_hp_switch.address = request.POST["address"]
        get_hp_switch.serial = request.POST["serial"]
        get_hp_switch.version = request.POST["version"]
        get_hp_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        hp_switch_create_data(get_hp_switch)
        return redirect("hp_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/hp/update.html', context={
            'get_hp_switch': get_hp_switch,
            'get_system_users': get_system_users
        })

def hp_switch_delete_view(request, id):
    hp_switch_delete_data(hp_switch_id=id)
    return redirect("hp_switch_view")

def hp_switch_config_view(request, id):
    get_hp_switch = hp_switch_get_by_id_data(hp_switch_id=id)
    hp_switch_configs = hp_switch_config_get_by_hp_all_data(hp_switch=get_hp_switch)
    return render(request, 'pages/network/hp/config.html', context={
        'hp_switch_configs': hp_switch_configs,
        'hp_switch': get_hp_switch
    })

def hp_switch_config_detail_view(request, id):
    hp_switch_config = hp_switch_config_get_by_id_data(hp_switch_config_id=id)
    return render(request, 'pages/network/hp/configdetail.html', context={
        'get_hp_switch_config': hp_switch_config
    })

def hp_switch_config_delete_view(request, id):
    hp_switch_config_delete_data(hp_switch_config_id=id)
    return redirect("hp_switch_view")

def hp_switch_all_sync_view(request):
    hp_switch_all_task_sync()
    return redirect("hp_switch_view")

def hp_switch_backup_sync_view(request, id):
    hp = hp_switch_get_by_id_data(hp_switch_id=id)
    hp_switch_get_config_sync(hp_switch=hp)
    return redirect("hp_switch_view")

def hp_switch_system_sync_view(request, id):
    hp = hp_switch_get_by_id_data(hp_switch_id=id)
    hp_switch_get_system_sync(hp_switch=hp)
    return redirect("hp_switch_view")