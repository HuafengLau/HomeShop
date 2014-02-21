#coding: utf-8

from django.db import models

class BigClass(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name=u'商品大类名称')
   
    def __unicode__(self):
        return '%s' %(self.name)
    
    class Meta:
        ordering = ['name',]
        verbose_name = u'商品大类'
        verbose_name_plural = u'商品大类'

        
class SmallClass(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name=u'商品小类名称')
    bigclass = models.ForeignKey(BigClass, null=True,verbose_name=u'所属大类')
   
    def __unicode__(self):
        return '%s-%s' %(self.bigclass, self.name)
    
    class Meta:
        ordering = ['bigclass',]
        verbose_name = u'商品小类'
        verbose_name_plural = u'商品小类'


class Unit(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name=u'商品单位')
   
    def __unicode__(self):
        return '%s' %(self.name)
    
    class Meta:
        ordering = ['name',]
        verbose_name = u'商品单位'
        verbose_name_plural = u'商品单位'

        
class Goods(models.Model):
    name = models.CharField(max_length=100,null=True,verbose_name=u'商品名称')
    smallclass = models.ForeignKey(SmallClass, null=True,verbose_name=u'所属分类')
    unit = models.ForeignKey(Unit,null=True,verbose_name=u'商品单位')
    info = models.CharField(max_length=200,null=True,blank=True,verbose_name=u'商品说明')
   
    def __unicode__(self):
        return '%s-%s' %(self.smallclass, self.name)
    
    class Meta:
        ordering = ['smallclass',]
        verbose_name = u'商品'
        verbose_name_plural = u'商品'

