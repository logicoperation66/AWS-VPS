from django.shortcuts import render
from .models import Products


# Create your views here.

def index(request):
    #Strona główna aplikacji AWSVPS
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
