from django.contrib import admin
from .models import Bot, Table, Delivery, FinalDelivery


class BotAdmin(admin.ModelAdmin):
    list_display = ['bot_no', 'name', 'color']
admin.site.register(Bot, BotAdmin)

admin.site.register(Table)
admin.site.register(Delivery)
admin.site.register(FinalDelivery)


# Register your models here.
