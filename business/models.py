#coding: utf-8

from django.db import models
from goods.models import Goods, Unit
from object.models import Customer, Supply

      
class Market(models.Model):
    customer =  models.ForeignKey(Customer, null=True,verbose_name=u'购买者')
    goods = models.ForeignKey(Goods, null=True,verbose_name=u'售出商品')
    unit = models.ForeignKey(Unit,null=True,verbose_name=u'单位')
    price = models.FloatField(verbose_name=u'售出单价')
    number = models.IntegerField(verbose_name=u'售出数量')
    total_price = models.FloatField(verbose_name=u'售出总金额')
    time =  models.DateField(null=True,blank=True,verbose_name=u'售出时间')
    info = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'额外信息')
   
    def __unicode__(self):
        return '%s-%s' %(self.customer.name, self.total_price)
    
    class Meta:
        ordering = ['time','goods','customer']
        verbose_name = u'出售'
        verbose_name_plural = u'出售'
        
class Stock(models.Model):
    supply =  models.ForeignKey(Supply, null=True,verbose_name=u'货源')
    goods = models.ForeignKey(Goods, null=True,verbose_name=u'进货商品')
    unit = models.ForeignKey(Unit,null=True,verbose_name=u'单位')
    price = models.FloatField(verbose_name=u'进货单价')
    number = models.IntegerField(verbose_name=u'进货数量')
    total_price = models.FloatField(verbose_name=u'进货总金额')
    time =  models.DateField(null=True,blank=True,verbose_name=u'进货时间')
    info = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'额外信息')
   
    def __unicode__(self):
        return '%s-%s' %(self.supply.company, self.total_price)
    
    class Meta:
        ordering = ['time','supply','goods']
        verbose_name = u'进货'
        verbose_name_plural = u'进货'
