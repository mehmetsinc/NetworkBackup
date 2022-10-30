from django.shortcuts import render

def network_home(request):

    return render(request, 'pages/network/home/index.html', context={})