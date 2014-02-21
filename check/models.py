#coding: utf-8

from django.db import models
from goods.models import Goods
from goods.models import Unit

class More(models.Model):
    goods = models.ForeignKey(Goods, null=True,verbose_name=u'盘点商品')
    number = models.IntegerField(null=True,verbose_name=u'盘盈数量')
    unit = models.ForeignKey(Unit,null=True,verbose_name=u'商品单位')
    time =  models.DateField(null=True,verbose_name=u'盘点时间')
    
    def __unicode__(self):
        return '%s++%s' %(self.goods, self.number)
    
    class Meta:
        ordering = ['time','goods']
        verbose_name = u'盘盈'
        verbose_name_plural = u'盘盈'

class Less(models.Model):
    goods = models.ForeignKey(Goods, null=True,verbose_name=u'盘点商品')
    number = models.IntegerField(null=True,verbose_name=u'盘亏数量')
    unit = models.ForeignKey(Unit,null=True,verbose_name=u'商品单位')
    time =  models.DateField(null=True,verbose_name=u'盘点时间')

    def __unicode__(self):
            return '%s--%s' %(self.goods, self.number)
    
    class Meta:
        ordering = ['time','goods']
        verbose_name = u'盘亏'
        verbose_name_plural = u'盘亏'   