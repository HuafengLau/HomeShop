#coding:utf-8

from django import template
from goods.models import Goods
from business.models import Stock, Market
from check.models import More,Less
import re

register = template.Library()

class goods_storeNode(template.Node):
    def __init__(self,sequence):
        self.sequence = sequence

    def render(self, context):
        value = self.sequence.resolve(context, True) 
        
        stocks = Stock.objects.filter(goods=value)
        stock_num = 0
        if stocks:
            for stock in stocks:
                stock_num += stock.number
                
        markets = Market.objects.filter(goods=value)
        market_num = 0
        if markets:
            for market in markets:
                 market_num += market.number
                 
        mores = More.objects.filter(goods=value)
        more_num = 0
        if mores:
            for more in mores:
                more_num += more.number
        
        lesses = Less.objects.filter(goods=value)
        less_num = 0
        if lesses:
            for less in lesses:
                less_num += less.number
        
        store_num = stock_num - market_num + more_num - less_num
        return store_num
        
def goods_store(parser, token):
    try:
        tag_name, text_name= token.split_contents() 
    except:
        raise template.TemplateSyntaxError
        
    sequence = parser.compile_filter(text_name)    
    return goods_storeNode(sequence)

class goods_stockNode(template.Node):
    def __init__(self,sequence):
        self.sequence = sequence

    def render(self, context):
        value = self.sequence.resolve(context, True) 
        stocks = Stock.objects.filter(goods=value)
        num = 0
        if stocks:
            for stock in stocks:
                num += stock.number
        return num
        
def goods_stock(parser, token):
    try:
        tag_name, text_name= token.split_contents() 
    except:
        raise template.TemplateSyntaxError
        
    sequence = parser.compile_filter(text_name)    
    return goods_stockNode(sequence)
    
class goods_marketNode(template.Node):
    def __init__(self,sequence):
        self.sequence = sequence

    def render(self, context):
        value = self.sequence.resolve(context, True) 
        markets = Market.objects.filter(goods=value)
        num = 0
        if markets:
            for market in markets:
                num += market.number
        return num
        
def goods_market(parser, token):
    try:
        tag_name, text_name= token.split_contents() 
    except:
        raise template.TemplateSyntaxError
        
    sequence = parser.compile_filter(text_name)    
    return goods_marketNode(sequence)
    
class goods_moreNode(template.Node):
    def __init__(self,sequence):
        self.sequence = sequence

    def render(self, context):
        value = self.sequence.resolve(context, True) 
        mores = More.objects.filter(goods=value)
        num = 0
        if mores:
            for more in mores:
                num += more.number
        return num
        
def goods_more(parser, token):
    try:
        tag_name, text_name= token.split_contents() 
    except:
        raise template.TemplateSyntaxError
        
    sequence = parser.compile_filter(text_name)    
    return goods_moreNode(sequence)
    
class goods_lessNode(template.Node):
    def __init__(self,sequence):
        self.sequence = sequence

    def render(self, context):
        value = self.sequence.resolve(context, True) 
        lesses = Less.objects.filter(goods=value)
        num = 0
        if lesses:
            for less in lesses:
                num += less.number
        return num
        
def goods_less(parser, token):
    try:
        tag_name, text_name= token.split_contents() 
    except:
        raise template.TemplateSyntaxError
        
    sequence = parser.compile_filter(text_name)    
    return goods_lessNode(sequence)
    
register.tag('goods_store', goods_store)
register.tag('goods_stock', goods_stock)
register.tag('goods_market', goods_market)
register.tag('goods_more', goods_more)
register.tag('goods_less', goods_less)