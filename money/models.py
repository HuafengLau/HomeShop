#coding: utf-8

from django.db import models
from object.models import Customer


class onCredit(models.Model):
     customer =  models.ForeignKey(Customer, null=True,verbose_name=u'赊账人')
     time =  models.DateField(null=True,verbose_name=u'赊账时间')
     total_price = models.FloatField(verbose_name=u'应付总金额')
     paid = models.FloatField(verbose_name=u'已付金额')
     notPaid = models.FloatField(verbose_name=u'未付金额')
     status = models.IntegerField(verbose_name=u'状态')
     
     
     def __unicode__(self):
        return '%s-%s' %(self.customer.name, self.notPaid)
    
     class Meta:
        ordering = ['status','notPaid','time']
        verbose_name = u'赊账'
        verbose_name_plural = u'赊账'