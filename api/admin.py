from django.contrib import admin
from .models import Bot, Table, Delivery, FinalDelivery

admin.site.register(Bot)
admin.site.register(Table)
admin.site.register(Delivery)
admin.site.register(FinalDelivery)


# Register your models here.
