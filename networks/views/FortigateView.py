from django.shortcuts import render, redirect
from networks.models.FortigateModel import Fortigate
from networks.datas.FortigateData import fortigate_get_all_data, fortigate_delete_data, fortigate_get_by_id_data, fortigate_create_data
from networks.datas.SystemUserData import system_user_get_by_id_data, system_user_get_all_data
from networks.datas.FortigateConfigData import fortigate_config_get_by_fortigate_all_data, fortigate_config_get_by_id_data, fortigate_config_delete_data
from networks.helpers.firewalls.FortigateHelper import fortigate_all_task_sync, fortigate_get_system_sync, fortigate_get_config_sync

def fortigate_view(request):

    fortigate_list = fortigate_get_all_data()
    return render(request, 'pages/network/fortigate/index.html', context={
        'fortigate_list': fortigate_list
    })

def fortigate_create_view(request):
    if request.POST:
        get_fortigate = Fortigate()
        get_fortigate.hostname = request.POST["hostname"]
        get_fortigate.vendor = "Fortigate"
        get_fortigate.model = request.POST["model"]
        get_fortigate.address = request.POST["address"]
        get_fortigate.serial = request.POST["serial"]
        get_fortigate.version = request.POST["version"]
        get_fortigate.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        fortigate_create_data(get_fortigate)
        return redirect("fortigate_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/fortigate/create.html', context={
            "system_users": get_system_users
        })

def fortigate_update_view(request, id):
    get_fortigate = fortigate_get_by_id_data(fortigate_id=id)
    if request.POST:
        get_fortigate.hostname = request.POST["hostname"]
        get_fortigate.model = request.POST["model"]
        get_fortigate.address = request.POST["address"]
        get_fortigate.serial = request.POST["serial"]
        get_fortigate.version = request.POST["version"]
        get_fortigate.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        fortigate_create_data(get_fortigate)
        return redirect("fortigate_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/fortigate/update.html', context={
            'get_fortigate': get_fortigate,
            'get_system_users': get_system_users
        })

def fortigate_delete_view(request, id):
    fortigate_delete_data(fortigate_id=id)
    return redirect("fortigate_view")

def fortigate_config_view(request, id):
    get_fortigate = fortigate_get_by_id_data(fortigate_id=id)
    fortigate_configs = fortigate_config_get_by_fortigate_all_data(fortigate=get_fortigate)
    return render(request, 'pages/network/fortigate/config.html', context={
        'fortigate_configs': fortigate_configs,
        'fortigate': get_fortigate
    })

def fortigate_config_detail_view(request, id):
    get_fortigate_config = fortigate_config_get_by_id_data(fortigate_config_id=id)
    return render(request, 'pages/network/fortigate/configdetail.html', context={
        'get_fortigate_config': get_fortigate_config
    })

def fortigate_config_delete_view(request, id):
    fortigate_config_delete_data(fortigate_config_id=id)
    return redirect("fortigate_view")

def fortigate_all_sync_view(request):
    fortigate_all_task_sync()
    return redirect("fortigate_view")

def fortigate_backup_sync_view(request, id):
    fortigate = fortigate_get_by_id_data(fortigate_id=id)
    fortigate_get_config_sync(fortigate=fortigate)
    return redirect("fortigate_view")

def fortigate_system_sync_view(request, id):
    fortigate = fortigate_get_by_id_data(fortigate_id=id)
    fortigate_get_system_sync(fortigate=fortigate)
    return redirect("fortigate_view")



