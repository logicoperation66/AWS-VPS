"""Definiuje wzorce adresów URL dla shop"""

from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
    #Strona główna
    path('', views.index, name='index'),
    #Strona 'O nas"
    path('about/', views.about, name='about'),
    #Dokumentacja
    path('docs/', views.docs, name='docs'),
    #Panel sterowania
    path('userpanel', views.userpanel, name='userpanel'),
]