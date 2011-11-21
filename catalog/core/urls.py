from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.shortcuts import get_object_or_404

from core.models import Producer, GoodInfo
from core.views import index, shop_view, good_view, producer_view


urlpatterns = patterns('core.views',
       url(r'^$', cache_page(index, 60 * 30), name="catalog_index"),
       url(r'^shop/(?P<shop_id>\d+)/$', cache_page(shop_view, 60 * 30), name="shop"),
       url(r'^good/(?P<good_id>\d+)/$', cache_page(good_view, 60 * 30), name="good"),
       url(r'^producer/(\d+)/$', cache_page(producer_view, 60 * 30), name="producer")
)
