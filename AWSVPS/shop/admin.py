from django.contrib import admin
from .models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'ami', 'price', 'version']
    list_editable = ['ami', 'price', 'version']

