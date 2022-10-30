from networks.models.ArubaSwitchModel import ArubaSwitch
from networks.datas.SystemUserData import system_user_get_all_data, system_user_get_by_id_data
from django.shortcuts import render, redirect
from networks.datas.ArubaSwitchConfigData import aruba_switch_config_get_by_aruba_all_data, aruba_switch_config_get_by_id_data, aruba_switch_config_delete_data
from networks.datas.ArubaSwitchData import aruba_switch_get_all_data, aruba_switch_create_data, aruba_switch_delete_data, aruba_switch_get_by_id_data
from networks.helpers.routers.ArubaHelper import aruba_switch_all_task_sync, aruba_switch_get_config_sync, aruba_switch_get_system_sync



def aruba_switch_view(request):

    aruba_switcies = aruba_switch_get_all_data()
    return render(request, 'pages/network/aruba/index.html', context={
        'aruba_switcies': aruba_switcies
    })

def aruba_switch_create_view(request):
    if request.POST:
        get_aruba_switch = ArubaSwitch()
        get_aruba_switch.hostname = request.POST["hostname"]
        get_aruba_switch.vendor = "Aruba"
        get_aruba_switch.model = request.POST["model"]
        get_aruba_switch.address = request.POST["address"]
        get_aruba_switch.serial = request.POST["serial"]
        get_aruba_switch.version = request.POST["version"]
        get_aruba_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        aruba_switch_create_data(get_aruba_switch)
        return redirect("aruba_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/aruba/create.html', context={
            "system_users": get_system_users
        })

def aruba_switch_update_view(request, id):
    get_aruba_switch = aruba_switch_get_by_id_data(aruba_switch_id=id)
    if request.POST:
        get_aruba_switch.hostname = request.POST["hostname"]
        get_aruba_switch.model = request.POST["model"]
        get_aruba_switch.address = request.POST["address"]
        get_aruba_switch.serial = request.POST["serial"]
        get_aruba_switch.version = request.POST["version"]
        get_aruba_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        aruba_switch_create_data(get_aruba_switch)
        return redirect("aruba_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/aruba/update.html', context={
            'get_aruba_switch': get_aruba_switch,
            'get_system_users': get_system_users
        })

def aruba_switch_delete_view(request, id):
    aruba_switch_delete_data(aruba_switch_id=id)
    return redirect("aruba_switch_view")

def aruba_switch_config_view(request, id):
    get_aruba_switch = aruba_switch_get_by_id_data(aruba_switch_id=id)
    aruba_switch_configs = aruba_switch_config_get_by_aruba_all_data(aruba_switch=get_aruba_switch)
    return render(request, 'pages/network/aruba/config.html', context={
        'aruba_switch_configs': aruba_switch_configs,
        'aruba_switch': get_aruba_switch
    })

def aruba_switch_config_detail_view(request, id):
    aruba_switch_config = aruba_switch_config_get_by_id_data(aruba_switch_config_id=id)
    return render(request, 'pages/network/aruba/configdetail.html', context={
        'get_aruba_switch_config': aruba_switch_config
    })

def aruba_switch_config_delete_view(request, id):
    aruba_switch_config_delete_data(aruba_switch_config_id=id)
    return redirect("aruba_switch_view")

def aruba_switch_all_sync_view(request):
    aruba_switch_all_task_sync()
    return redirect("aruba_switch_view")

def aruba_switch_backup_sync_view(request, id):
    aruba = aruba_switch_get_by_id_data(aruba_switch_id=id)
    aruba_switch_get_config_sync(aruba_switch=aruba)
    return redirect("aruba_switch_view")

def aruba_switch_system_sync_view(request, id):
    aruba = aruba_switch_get_by_id_data(aruba_switch_id=id)
    aruba_switch_get_system_sync(aruba_switch=aruba)
    return redirect("aruba_switch_view")