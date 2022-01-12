"""Definiuje wzorce adresów URL dla shop"""

from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    #Strona główna
    path('', views.index, name='index')
]