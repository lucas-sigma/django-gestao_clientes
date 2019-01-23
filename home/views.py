from django.shortcuts import render
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def my_logout(request):
    logout(request)
    return render(request, 'home.html')