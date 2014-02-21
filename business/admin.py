#coding:utf-8

from django.contrib import admin
from business.models import Market,Stock

    
class MarketAdmin(admin.ModelAdmin):
    """docstring for MarketAdmin"""
    list_display = ('time','customer','goods','price','number','unit','total_price','info')
    list_filter = ('time','customer','goods')
    ordering = ('time','customer','goods')
    

class StockAdmin(admin.ModelAdmin):
    """docstring for StockAdmin"""
    list_display = ('time','supply','goods','price','number','unit','total_price','info')
    list_filter = ('time','supply','goods')
    ordering = ('time','supply','goods')   
  
admin.site.register(Market, MarketAdmin)
admin.site.register(Stock, StockAdmin)
