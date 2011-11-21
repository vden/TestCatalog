# -*- coding: utf-8 -*-

from django.db import models


class Producer(models.Model):
    name = models.CharField(u"Название", max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Производитель"
        verbose_name_plural = u"Производители"


class Good(models.Model):
    name = models.CharField(u"Название товара", max_length=255, unique=True)
    producer = models.ForeignKey(Producer, verbose_name=u"Производитель")

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.producer.name)

    class Meta:
        verbose_name = u"Товар"
        verbose_name_plural = u"Товары"


class GoodInfo(models.Model):
    added = models.DateField(u"Дата добавления товара", auto_now=True, auto_now_add=True)
    good = models.ForeignKey(Good, verbose_name=u"Товар")
    shop = models.ForeignKey("Shop", verbose_name=u"Магазин")
    # there are may be more fields, specifying particular good in the shop, like price, etc

    def __unicode__(self):
        return u'%s в "%s"' % (self.good, self.shop)

    class Meta:
        verbose_name = u"Информация о товаре"
        verbose_name_plural = u"Информация о товарах"
        unique_together = ("good", "shop")


class Shop(models.Model):
    name = models.CharField(u"Название магазина", max_length=255, unique=True)
    address = models.CharField(u"Адрес магазина", max_length=1000)
    goods = models.ManyToManyField(Good, through=GoodInfo)
    added = models.DateField(u"Дата регистрации магазина", auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u"Магазин"
        verbose_name_plural = u"Магазины"
