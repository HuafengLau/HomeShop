#coding:utf-8

from django.contrib import admin
from business.models import Customer,Supply


class CustomerAdmin(admin.ModelAdmin):
    """docstring for CustomerAdmin"""
    list_display = ('name','phone','company','address','info')
    ordering = ('name',)
    
class SupplyAdmin(admin.ModelAdmin):
    """docstring for SupplyAdmin"""
    list_display = ('company','name','phone','address','info')
    ordering = ('name',)
 
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Supply, SupplyAdmin)