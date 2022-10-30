from django.shortcuts import render, redirect
from networks.datas.SystemUserData import system_user_get_all_data, system_user_create_data, system_user_remove_data, system_user_get_by_id_data
from networks.models.SystemUserModel import SystemUser

def system_user_view(request):
    system_users = system_user_get_all_data()
    return render(request, 'pages/network/systemuser/index.html', context={
        'system_users': system_users
    })

def system_user_create(request):
    if request.POST:
        get_system_user = SystemUser()
        get_system_user.name = request.POST["name"]
        get_system_user.username = request.POST["username"]
        get_system_user.password = request.POST["password"]
        system_user_create_data(system_user=get_system_user)
        return redirect("system_user_view")
    else:
        return render(request, 'pages/network/systemuser/create.html', context={})

def system_user_update_view(request, id):
    get_system_user = system_user_get_by_id_data(system_user_id=id)
    if request.POST:
        get_system_user.name = request.POST["name"]
        get_system_user.username = request.POST["username"]
        get_system_user.password = request.POST["password"]
        system_user_create_data(system_user=get_system_user)
        return redirect("system_user_view")
        pass
    else:
        return render(request, 'pages/network/systemuser/update.html', context={
            'system_user': get_system_user
        })

def system_user_delete_view(request, id):
    system_user_remove_data(system_user_id=id)
    return redirect("system_user_view")