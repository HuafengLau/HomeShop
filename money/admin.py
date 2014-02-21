#coding:utf-8

from django.contrib import admin
from money.models import onCredit  

class onCreditAdmin(admin.ModelAdmin):
    """docstring for onCreditAdmin"""
    list_display = ('status','time','notPaid','paid','total_price','customer')
    list_filter = ('status','time','customer')
    ordering = ('status','time','notPaid','customer')  
   
admin.site.register(onCredit, onCreditAdmin)