from networks.models.ExtremeSwitchModel import ExtremeSwitch
from networks.datas.SystemUserData import system_user_get_all_data, system_user_get_by_id_data
from django.shortcuts import render, redirect
from networks.datas.ExtremeSwitchConfigData import extreme_switch_config_get_by_extreme_all_data, extreme_switch_config_get_by_id_data, extreme_switch_config_delete_data
from networks.datas.ExtremeSwitchData import extreme_switch_get_all_data, extreme_switch_create_data, extreme_switch_delete_data, extreme_switch_get_by_id_data
from networks.helpers.routers.ExtremeHelper import extreme_switch_all_task_sync, extreme_switch_get_config_sync, extreme_switch_get_system_sync



def extreme_switch_view(request):

    extreme_switcies = extreme_switch_get_all_data()
    return render(request, 'pages/network/extreme/index.html', context={
        'extreme_switcies': extreme_switcies
    })

def extreme_switch_create_view(request):
    if request.POST:
        get_extreme_switch = ExtremeSwitch()
        get_extreme_switch.hostname = request.POST["hostname"]
        get_extreme_switch.vendor = "Extreme"
        get_extreme_switch.model = request.POST["model"]
        get_extreme_switch.address = request.POST["address"]
        get_extreme_switch.serial = request.POST["serial"]
        get_extreme_switch.version = request.POST["version"]
        get_extreme_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        extreme_switch_create_data(get_extreme_switch)
        return redirect("extreme_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/extreme/create.html', context={
            "system_users": get_system_users
        })

def extreme_switch_update_view(request, id):
    get_extreme_switch = extreme_switch_get_by_id_data(extreme_switch_id=id)
    if request.POST:
        get_extreme_switch.hostname = request.POST["hostname"]
        get_extreme_switch.model = request.POST["model"]
        get_extreme_switch.address = request.POST["address"]
        get_extreme_switch.serial = request.POST["serial"]
        get_extreme_switch.version = request.POST["version"]
        get_extreme_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        extreme_switch_create_data(get_extreme_switch)
        return redirect("extreme_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/extreme/update.html', context={
            'get_extreme_switch': get_extreme_switch,
            'get_system_users': get_system_users
        })

def extreme_switch_delete_view(request, id):
    extreme_switch_delete_data(extreme_switch_id=id)
    return redirect("extreme_switch_view")

def extreme_switch_config_view(request, id):
    get_extreme_switch = extreme_switch_get_by_id_data(extreme_switch_id=id)
    extreme_switch_configs = extreme_switch_config_get_by_extreme_all_data(extreme_switch=get_extreme_switch)
    return render(request, 'pages/network/extreme/config.html', context={
        'extreme_switch_configs': extreme_switch_configs,
        'extreme_switch': get_extreme_switch
    })

def extreme_switch_config_detail_view(request, id):
    extreme_switch_config = extreme_switch_config_get_by_id_data(extreme_switch_config_id=id)
    return render(request, 'pages/network/extreme/configdetail.html', context={
        'get_extreme_switch_config': extreme_switch_config
    })

def extreme_switch_config_delete_view(request, id):
    extreme_switch_config_delete_data(extreme_switch_config_id=id)
    return redirect("extreme_switch_view")

def extreme_switch_all_sync_view(request):
    extreme_switch_all_task_sync()
    return redirect("extreme_switch_view")

def extreme_switch_backup_sync_view(request, id):
    extreme = extreme_switch_get_by_id_data(extreme_switch_id=id)
    extreme_switch_get_config_sync(extreme_switch=extreme)
    return redirect("extreme_switch_view")

def extreme_switch_system_sync_view(request, id):
    extreme = extreme_switch_get_by_id_data(extreme_switch_id=id)
    extreme_switch_get_system_sync(extreme_switch=extreme)
    return redirect("extreme_switch_view")