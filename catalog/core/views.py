# -*- coding: utf-8 -*-

from django.views.generic.simple import direct_to_template
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.conf import settings

from core.models import Shop, Good, GoodInfo, Producer


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
    return redirect(reverse("home"))


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


def good_in_shop(request, good_id, shop_id):
    return HttpResponse("Ok")
