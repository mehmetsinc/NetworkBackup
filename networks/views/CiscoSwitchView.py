from networks.models.CiscoSwitchModel import CiscoSwitch
from networks.datas.CiscoSwitchConfigData import cisco_switch_config_get_by_fortigate_all_data, cisco_switch_config_get_by_id_data, cisco_switch_config_delete_data
from networks.datas.SystemUserData import system_user_get_all_data, system_user_get_by_id_data
from networks.datas.CiscoSwitchData import cisco_switch_get_all_data, cisco_switch_create_data, cisco_switch_delete_data, cisco_switch_get_by_id_data
from django.shortcuts import render, redirect
from networks.helpers.routers.CiscoHelpers import cisco_switch_all_task_sync, cisco_switch_get_config_sync, cisco_switch_get_system_sync

def cisco_switch_view(request):

    cisco_switcies = cisco_switch_get_all_data()
    return render(request, 'pages/network/cisco/index.html', context={
        'cisco_switcies': cisco_switcies
    })

def cisco_switch_create_view(request):
    if request.POST:
        get_cisco_switch = CiscoSwitch()
        get_cisco_switch.hostname = request.POST["hostname"]
        get_cisco_switch.vendor = "Cisco"
        get_cisco_switch.model = request.POST["model"]
        get_cisco_switch.address = request.POST["address"]
        get_cisco_switch.serial = request.POST["serial"]
        get_cisco_switch.version = request.POST["version"]
        get_cisco_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        cisco_switch_create_data(get_cisco_switch)
        return redirect("cisco_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/cisco/create.html', context={
            "system_users": get_system_users
        })

def cisco_switch_update_view(request, id):
    get_cisco_switch = cisco_switch_get_by_id_data(cisco_switch_id=id)
    if request.POST:
        get_cisco_switch.hostname = request.POST["hostname"]
        get_cisco_switch.model = request.POST["model"]
        get_cisco_switch.address = request.POST["address"]
        get_cisco_switch.serial = request.POST["serial"]
        get_cisco_switch.version = request.POST["version"]
        get_cisco_switch.systemuser = system_user_get_by_id_data(system_user_id=request.POST["systemuser"])
        cisco_switch_create_data(get_cisco_switch)
        return redirect("cisco_switch_view")
    else:
        get_system_users = system_user_get_all_data()
        return render(request, 'pages/network/cisco/update.html', context={
            'get_cisco_switch': get_cisco_switch,
            'get_system_users': get_system_users
        })

def cisco_switch_delete_view(request, id):
    cisco_switch_delete_data(cisco_switch_id=id)
    return redirect("cisco_switch_view")

def cisco_switch_config_view(request, id):
    get_cisco_switch = cisco_switch_get_by_id_data(cisco_switch_id=id)
    cisco_switch_configs = cisco_switch_config_get_by_fortigate_all_data(cisco_switch=get_cisco_switch)
    return render(request, 'pages/network/cisco/config.html', context={
        'cisco_switch_configs': cisco_switch_configs,
        'cisco_switch': get_cisco_switch
    })

def cisco_switch_config_detail_view(request, id):
    cisco_switch_config = cisco_switch_config_get_by_id_data(cisco_switch_config_id=id)
    return render(request, 'pages/network/cisco/configdetail.html', context={
        'get_cisco_switch_config': cisco_switch_config
    })

def cisco_switch_config_delete_view(request, id):
    cisco_switch_config_delete_data(cisco_switch_config_id=id)
    return redirect("cisco_switch_view")

def cisco_switch_all_sync_view(request):
    cisco_switch_all_task_sync()
    return redirect("cisco_switch_view")

def cisco_switch_backup_sync_view(request, id):
    cisco = cisco_switch_get_by_id_data(cisco_switch_id=id)
    cisco_switch_get_config_sync(cisco_switch=cisco)
    return redirect("cisco_switch_view")

def cisco_switch_system_sync_view(request, id):
    cisco = cisco_switch_get_by_id_data(cisco_switch_id=id)
    cisco_switch_get_system_sync(cisco_switch=cisco)
    return redirect("cisco_switch_view")