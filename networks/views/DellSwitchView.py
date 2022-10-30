from networks.models.DellSwitchModel import DellSwitch
from networks.datas.SystemUserData import system_user_get_all_data, system_user_get_by_id_data
from django.shortcuts import render, redirect
from networks.datas.DellSwitchConfigData import dell_switch_config_get_by_dell_all_data, dell_switch_config_get_by_id_data, dell_switch_config_delete_data
from networks.datas.DellSwitchData import dell_switch_get_all_data, dell_switch_create_data, dell_switch_delete_data, dell_switch_get_by_id_data
from networks.helpers.routers.DellHelper import dell_switch_all_task_sync, dell_switch_get_config_sync, dell_switch_get_system_sync



def dell_switch_view(request):

    dell_switcies = dell_switch_get_all_data()
    return render(request, 'pages/network/dell/index.html', context={
        'dell_switcies': dell_switcies
    })

def dell_switch_create_view(request):
    if request.POST:
        get_dell_switch = DellSwitch()
        get_dell_switch.hostname = request.POST["hostname"]
        get_dell_switch.vendor = "Dell"
        get_dell_switch.model = request.POST["model"]
        get_dell_switch.address = request.POST["address"]
        get_dell_switch.serial = request.POST["serial"]
        get_dell_switch.version = request.POST["version"]
        get_dell_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        dell_switch_create_data(get_dell_switch)
        return redirect("dell_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/dell/create.html', context={
            "system_users": get_system_users
        })

def dell_switch_update_view(request, id):
    get_dell_switch = dell_switch_get_by_id_data(dell_switch_id=id)
    if request.POST:
        get_dell_switch.hostname = request.POST["hostname"]
        get_dell_switch.model = request.POST["model"]
        get_dell_switch.address = request.POST["address"]
        get_dell_switch.serial = request.POST["serial"]
        get_dell_switch.version = request.POST["version"]
        get_dell_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        dell_switch_create_data(get_dell_switch)
        return redirect("dell_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/dell/update.html', context={
            'get_dell_switch': get_dell_switch,
            'get_system_users': get_system_users
        })

def dell_switch_delete_view(request, id):
    dell_switch_delete_data(dell_switch_id=id)
    return redirect("dell_switch_view")

def dell_switch_config_view(request, id):
    get_dell_switch = dell_switch_get_by_id_data(dell_switch_id=id)
    dell_switch_configs = dell_switch_config_get_by_dell_all_data(dell_switch=get_dell_switch)
    return render(request, 'pages/network/dell/config.html', context={
        'dell_switch_configs': dell_switch_configs,
        'dell_switch': get_dell_switch
    })

def dell_switch_config_detail_view(request, id):
    dell_switch_config = dell_switch_config_get_by_id_data(dell_switch_config_id=id)
    return render(request, 'pages/network/dell/configdetail.html', context={
        'get_dell_switch_config': dell_switch_config
    })

def dell_switch_config_delete_view(request, id):
    dell_switch_config_delete_data(dell_switch_config_id=id)
    return redirect("dell_switch_view")

def dell_switch_all_sync_view(request):
    dell_switch_all_task_sync()
    return redirect("dell_switch_view")

def dell_switch_backup_sync_view(request, id):
    dell = dell_switch_get_by_id_data(dell_switch_id=id)
    dell_switch_get_config_sync(dell_switch=dell)
    return redirect("dell_switch_view")

def dell_switch_system_sync_view(request, id):
    dell = dell_switch_get_by_id_data(dell_switch_id=id)
    dell_switch_get_system_sync(dell_switch=dell)
    return redirect("dell_switch_view")