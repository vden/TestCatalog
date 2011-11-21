from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from catalog.core.views import home


urlpatterns = patterns('core.views',
       url(r'^$', "index", name="catalog_index"),
       url(r'^shop/(?P<shop_id>\d+)/', "shop_view", name="shop"),
       url(r'^good/(?P<good_id>\d+)/(?P<shop_id>\d+)/', "good_in_shop", name="show_good"),
)
