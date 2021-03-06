from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def configure(request):
    if request.method == 'POST':
        if request.POST:
            print(request.POST)
            toolname = ''.join(request.POST.get('select-tool', []))
            username = ''.join(request.POST.get('username', ''))
            password = ''.join(request.POST.get('password', ''))
            auth_type = ''.join(request.POST.get('auth-type', ''))
            end_point = ''.join(request.POST.get('endpoint', ''))
            if toolname and username and auth_type:
                contact = ToolConfiguration.objects.create(toolName=toolname, endPoint=end_point, authenticationType=auth_type, userName=username,password=password, projectName='' )
    tools_list = Tools.objects.all()
    return render(request, "ticketingtool.html", {"tools_list":tools_list})