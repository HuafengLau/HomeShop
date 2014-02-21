#coding: utf-8

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name=u'顾客姓名')
    phone = models.IntegerField(null=True,blank=True,verbose_name=u'电话')
    QQ = models.IntegerField(null=True,blank=True,verbose_name=u'QQ')
    email = models.EmailField(null=True,blank=True,verbose_name='email')
    company = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'顾客公司')
    address = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'顾客住址')
    info = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'额外信息')
    
    def __unicode__(self):
        return '%s-%s' %(self.name, self.phone)
    
    class Meta:
        ordering = ['name',]
        verbose_name = u'顾客'
        verbose_name_plural = u'顾客'
  
class Supply(models.Model):
    company = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'货源公司')
    name = models.CharField(max_length=50,null=True,blank=True,verbose_name=u'联系人')
    phone = models.IntegerField(null=True,blank=True,verbose_name=u'联系电话')
    QQ = models.IntegerField(null=True,blank=True,verbose_name=u'QQ')
    email = models.EmailField(null=True,blank=True,verbose_name='email')   
    address = models.CharField(max_length=100,null=True,blank=True,verbose_name=u'货源地址')
    info = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'额外信息')
    
    def __unicode__(self):
        return '%s-%s' %(self.company, self.phone)
    
    class Meta:
        ordering = ['name',]
        verbose_name = u'货源'
        verbose_name_plural = u'货源'        
