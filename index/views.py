#coding:utf-8

from django.contrib.auth import *
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import PageNotAnInteger, Paginator, InvalidPage, EmptyPage
from django.conf import settings
from business.models import Market, Stock
from money.models import onCredit
from check.models import More, Less
from goods.models import BigClass, SmallClass
import datetime

def index(request):
    return render_to_response('index.html',locals(),
        context_instance=RequestContext(request))
        
def check_db(request):
    marketCompute = {}
    marketUnit = {}
    stockCompute = {}
    stockUnit = {}
    oncreditCompute = {}
    oncreditLogic = {}
    moreUnit = {}
    lessUnit = {}
    
    markets = Market.objects.all()
    stocks = Stock.objects.all()
    oncredits = onCredit.objects.all()
    mores = More.objects.all()
    lesses = Less.objects.all()
    
    #check Market 
    if markets:
        for market in markets:
            if (market.price * market.number) == market.total_price:
                pass
            else:
                message = u'%s * %s ≠ %s' % (market.price,market.number,market.total_price)
                marketCompute[message] = market
                
            if market.unit == market.goods.unit:
                pass
            else:
                message = u'出售单位(%s) ≠ 商品单位(%s)' % (market.unit,market.goods.unit)
                marketUnit[message] = market
                
    #check Stock
    if stocks:
        for stock in stocks:
            if (stock.price * stock.number) == stock.total_price:
                pass
            else:
                message = u'%s * %s ≠ %s' % (stock.price,stock.number,stock.total_price)
                stockCompute[message] = stock
                
            if stock.unit == stock.goods.unit:
                pass
            else:
                message = u'进货单位(%s) ≠ 商品单位(%s)' % (stock.unit,stock.goods.unit)
                stockUnit[message] = stock
     
    #check onCredit
    if oncredits:
        for oncredit in oncredits:
            if (oncredit.paid + oncredit.notPaid) == oncredit.total_price:
                pass
            else:
                message = u'%s + %s ≠ %s' % (oncredit.paid,oncredit.notPaid,oncredit.total_price)
                oncreditCompute[message] = oncredit
            
            if oncredit.notPaid == 0:
                if oncredit.status == 0:
                    pass
                elif oncredit.status == 1:
                    message = u'本次赊账已付清，请把赊账状态修改为 0'
                    oncreditLogic[message] = oncredit
                else:
                    message = u'赊账状态只能填1或者0！当前未支付金额为0，请把赊账状态修改为 0'
                    oncreditLogic[message] = oncredit
            else:
                if oncredit.status == 0:
                    message = u'本次赊账还没有付清，请把赊账状态修改为 1'
                    oncreditLogic[message] = oncredit
                elif oncredit.status == 1:
                    pass
                else:
                    message = u'赊账状态只能填1或者0！这次赊账还没有付清，请把赊账状态修改为 1'
                    oncreditLogic[message] = oncredit
           
    if mores:
        for more in mores:
            if more.unit == more.goods.unit:
                pass
            else:
                message = u'盘盈单位(%s) ≠ 商品单位(%s)' % (more.unit,more.goods.unit)
                moreUnit[message] = more
                
    if lesses:
        for less in lesses:
            if less.unit == less.goods.unit:
                pass
            else:
                message = u'盘亏单位(%s) ≠ 商品单位(%s)' % (less.unit,less.goods.unit)
                lessUnit[message] = less
                
    return render_to_response('check_db.html',locals(),
        context_instance=RequestContext(request))
        
def sales(request):
    today = datetime.datetime.today()
    year = today.year
    month = today.month
    day = today.day   
    
    day_sale = 0
    month_sale = 0
    year_sale = 0
  
    everyMonth = []
    
    year_market = Market.objects.filter(time__year=year)
    for market in year_market:
        year_sale += market.total_price
        
    for i in xrange(1,13):
        num = 0
        this_month = year_market.filter(time__month=i)
        if this_month:
            for market in this_month:
                num += market.total_price  
        everyMonth.append(num)
    
    if max(everyMonth) <= 2000.0:
        step = 20
        width = 100
    elif max(everyMonth) <= 3000.0:
        step = 15
        width = 200
    elif max(everyMonth) <= 4000.0:
        step = 20
        width = 200
    elif max(everyMonth) <= 6000.0:
        step = 20
        width = 300    
    else:   
        step = 20
        width = 400
    month_market = year_market.filter(time__month=month)
    for market in month_market:
        month_sale += market.total_price   

    day_market = month_market.filter(time__day=day)
    for market in day_market:
        day_sale += market.total_price
    
    return render_to_response('sales.html',locals(),
        context_instance=RequestContext(request))
        
def check_store(request):
    bigClasses = BigClass.objects.all()
    return render_to_response('check_store.html',locals(),
        context_instance=RequestContext(request))
    
        
        
            
                 
    

