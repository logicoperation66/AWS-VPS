from django.shortcuts import render
from .models import Products


# Create your views here.

def index(request):
    #Strona główna aplikacji AWSVPS
    return render(request, 'index.html')

def about(request):
    #Strona 'O nas'
    return render(request, 'about.html')

def docs(request):
    #Strona z dokumentacją
    return render(request, 'docs.html')

def userpanel(request):
    #Strona panel użyszkodnika
    return render(request, 'userpanel.html')
