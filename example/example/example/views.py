from django.shortcuts import render


# Create your views here.
def home(request):
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "home.html")