# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings
from django.views.decorators.cache import cache_page

from core.models import Shop, Good, GoodInfo, Producer


@cache_page(60 * 30)
def home(request):
    # last added shops
    last_shops = Shop.objects.order_by('-added', '-id')[:2]
    # get their ids to prevent nested query
    last_shops_ids = last_shops.values_list("pk", flat=True)

    # last goods from other than new shops
    last_goods = GoodInfo.objects.exclude(shop__id__in=list(last_shops_ids)).order_by('-added', '-id')[:12]

    # get random good for sidebar and shops where it is
    rgood = Good.objects.order_by('?')[0]
    rshops = rgood.shop_set.all()

    extra = {
        "shops": last_shops,
        "goods": last_goods,
        "random": {"good": rgood, "shops": rshops}
        }

    return direct_to_template(request, "index.html", extra)


def index(request):
    goods = Good.objects.order_by('name').all()
    shops = Shop.objects.order_by('-added').all()
    producers = Producer.objects.order_by("name").all()

    extra = {
        "goods": goods,
        "shops": shops,
        "producers": producers
        }

    return direct_to_template(request, "catalog.html", extra)


def shop_view(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    goods = GoodInfo.objects.filter(shop = shop)

    # get all producers in the shop
    goods_ids = list(goods.values_list("good__id", flat=True))
    producers = Good.objects.filter(id__in = goods_ids).values_list("producer__name", flat=True).distinct()

    extra = {
        "shop": shop,
        "producers": producers,
        "goods": goods
        }
    return direct_to_template(request, "shop.html", extra)


def good_view(request, good_id):
    good = get_object_or_404(Good, pk=good_id)
    shops = GoodInfo.objects.filter(good = good)

    other_goods = Good.objects.filter(producer=good.producer)[:5]

    extra = {
        "good": good,
        "other": other_goods,
        "shops": shops
        }

    return direct_to_template(request, "good.html", extra)


def producer_view(request, producer_id):
    producer = get_object_or_404(Producer, pk=producer_id)

    goods = Good.objects.filter(producer = producer)
    # to prevent nested query
    goods_ids = list(goods.values_list("pk", flat=True))

    shops = GoodInfo.objects.filter(good__id__in = goods_ids).values_list("shop__id", "shop__name").distinct()

    extra = {
        "producer": producer,
        "goods": goods,
        "shops": shops
        }

    return direct_to_template(request, "goods_by_producer.html", extra)
