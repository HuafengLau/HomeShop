#coding:utf-8

from django.contrib import admin
from goods.models import BigClass, SmallClass, Goods, Unit


class BigClassAdmin(admin.ModelAdmin):
    """docstring for BigClassAdmin"""
    list_display = ('name',)
    ordering = ('name',)
    
class UnitAdmin(admin.ModelAdmin):
    """docstring for UnitAdmin"""
    list_display = ('name',)
    ordering = ('name',)
    
class SmallClassAdmin(admin.ModelAdmin):
    """docstring for SmallClassAdmin"""
    list_display = ('bigclass','name')
    list_filter = ('bigclass',)
    ordering = ('bigclass',)

class GoodsAdmin(admin.ModelAdmin):
    """docstring for GoodsAdmin"""
    list_display = ('smallclass','name','unit','info')
    list_filter = ('smallclass',)
    ordering = ('smallclass',)        
 
admin.site.register(BigClass, BigClassAdmin)
admin.site.register(SmallClass, SmallClassAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Unit, UnitAdmin)