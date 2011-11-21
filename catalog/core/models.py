# -*- coding: utf-8 -*-

from django.db import models


class Producer(models.Model):
    name = models.CharField(u"Производитель", max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(u"Название товара", max_length=255, unique=True)
    producer = models.ForeignKey(Producer)

    def __unicode__(self):
        return u"%s (%s)" % (self.name, self.producer.name)


class GoodInfo(models.Model):
    added = models.DateField(u"Дата добавления товара", auto_now=True, auto_now_add=True)
    good = models.ForeignKey(Good)
    shop = models.ForeignKey("Shop")


class Shop(models.Model):
    name = models.CharField(u"Название магазина", max_length=255, unique=True)
    address = models.CharField(u"Адрес магазина", max_length=1000)
    goods = models.ManyToManyField(Good, through=GoodInfo)
    added = models.DateField(u"Дата регистрации магазина", auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return self.name
