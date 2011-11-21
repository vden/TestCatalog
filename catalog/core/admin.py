from django.contrib import admin

from core.models import Shop, Good, GoodInfo, Producer


admin.site.register(Shop)
admin.site.register(Producer)
admin.site.register(GoodInfo)
admin.site.register(Good)
