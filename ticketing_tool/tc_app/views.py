from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def configure(request):
    if request.method == 'POST':
        if request.POST:
            print(request.POST)
            toolname = ''.join(request.POST.get('toolnames', []))
            username = ''.join(request.POST.get('username', ''))
            password = ''.join(request.POST.get('password', ''))
            if toolname or username or password:
                contact = ToolConfiguration.objects.create(toolName=toolname, endPoint='', authenticationType='', userName=username,password=password, projectName='' )
    tools_list = Tools.objects.all()
    return render(request, "ticketingtool.html", {"tools_list":tools_list})