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
    path('userpanel/', views.userpanel, name='userpanel'),
    #VPS 1.0
    path('vps1/', views.vps1, name="vps1"),
    #VPS 2.0
    path('vps2/', views.vps2, name="vps2"),
    #VPS PRO
    path('vpspro/', views.vpspro, name="vpspro"),
]