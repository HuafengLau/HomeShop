#coding:utf-8

from django.contrib import admin
from check.models import More, Less

class MoreAdmin(admin.ModelAdmin):
    """docstring for MoreAdmin"""
    list_display = ('time','goods','number')
    list_filter = ('time','goods')
    ordering = ('time','goods','number')

class LessAdmin(admin.ModelAdmin):
    """docstring for LessAdmin"""
    list_display = ('time','goods','number')
    list_filter = ('time','goods')
    ordering = ('time','goods','number')        
 
admin.site.register(More, MoreAdmin)
admin.site.register(Less, LessAdmin)